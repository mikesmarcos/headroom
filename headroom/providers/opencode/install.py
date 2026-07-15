"""OpenCode install-time helpers."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

from headroom import fsutil
from headroom import paths as _paths
from headroom.install.models import ConfigScope, DeploymentManifest, ManagedMutation, ToolTarget
from headroom.install.paths import opencode_config_path

from .config import (
    _inject_key_into_json,
    _parse_json_loose,
    headroom_provider_entry,
    snapshot_opencode_config_if_unwrapped,
    strip_opencode_headroom_blocks,
)
from .runtime import headroom_opencode_plugin_path

# Well-known plugin artifact contract. The package version is intentionally
# explicit: operational installs must not resolve mutable npm tags like latest.
_PLUGIN_PACKAGE_SPEC = "headroom-opencode@0.1.0"
_PLUGIN_ENTRY_REL = "dist/entry.opencode.js"


def _plugin_artifact_error(reason: str) -> RuntimeError:
    return RuntimeError(
        f"OpenCode transport plugin artifact could not be prepared from "
        f"{_PLUGIN_PACKAGE_SPEC}: {reason}. Install npm or rebuild the stable "
        f"artifact, then re-run the install. The plugin entry point "
        f"{_PLUGIN_ENTRY_REL} from the versioned headroom-opencode npm package "
        f"is required."
    )


def _npm_pack_plugin(package_spec: str, *, pack_dir: Path) -> Path | None:
    """Download the versioned plugin package into ``pack_dir`` with npm pack."""
    try:
        result = subprocess.run(
            ["npm", "pack", package_spec, "--pack-destination", str(pack_dir)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        raise _plugin_artifact_error("npm executable was not found") from None
    except subprocess.TimeoutExpired:
        raise _plugin_artifact_error("npm pack timed out") from None
    except subprocess.CalledProcessError as exc:
        details = (exc.stderr or exc.stdout or "").strip()
        reason = "npm pack failed"
        if details:
            reason = f"{reason}: {details}"
        raise _plugin_artifact_error(reason) from None

    tarball_name = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else ""
    if not tarball_name:
        return None
    tarball = pack_dir / tarball_name
    if tarball.is_file():
        return tarball
    return None


def prepare_opencode_plugin_artifact(*, dest_dir: Path | None = None) -> Path:
    """Ensure the OpenCode transport plugin artifact is installed at a stable location.

    The plugin artifact is resolved from the explicit versioned npm package
    ``headroom-opencode@0.1.0`` and extracted into ``dest_dir`` so runtime
    OpenCode config never points at a mutable Headroom development checkout.
    Re-running is a no-op when the artifact is already present (idempotent).

    Parameters
    ----------
    dest_dir:
        Target directory for the unpacked plugin. Defaults to
        ``plugin_workspace_dir("headroom-opencode")``
        (``~/.headroom/plugins/headroom-opencode/``).

    Raises
    ------
    RuntimeError
        If the versioned package cannot be packed, extracted, or does not
        contain ``dist/entry.opencode.js``.
    """
    if dest_dir is None:
        dest_dir = _paths.plugin_workspace_dir("headroom-opencode")

    # Already present — idempotent.
    if (dest_dir / _PLUGIN_ENTRY_REL).is_file():
        return dest_dir

    with tempfile.TemporaryDirectory(prefix="headroom-opencode-") as tmp:
        tmp_dir = Path(tmp)
        tarball = _npm_pack_plugin(_PLUGIN_PACKAGE_SPEC, pack_dir=tmp_dir)
        if tarball is None:
            raise _plugin_artifact_error("npm pack did not produce a package tarball")

        extract_dir = tmp_dir / "extract"
        extract_dir.mkdir()
        try:
            with tarfile.open(tarball) as archive:
                extract_root = extract_dir.resolve()
                for member in archive.getmembers():
                    if not member.isfile() or not member.name.startswith("package/"):
                        continue
                    target = (extract_dir / member.name).resolve()
                    if not target.is_relative_to(extract_root):
                        raise tarfile.TarError("unsafe package path")
                    target.parent.mkdir(parents=True, exist_ok=True)
                    source = archive.extractfile(member)
                    if source is None:
                        raise tarfile.TarError("package member could not be read")
                    with source, target.open("wb") as dest:
                        shutil.copyfileobj(source, dest)
        except (tarfile.TarError, OSError):
            raise _plugin_artifact_error("package tarball could not be extracted") from None

        package_root = extract_dir / "package"
        if not (package_root / _PLUGIN_ENTRY_REL).is_file():
            raise _plugin_artifact_error(f"package tarball does not contain {_PLUGIN_ENTRY_REL}")

        shutil.copytree(package_root, dest_dir, dirs_exist_ok=True)

    return dest_dir


def build_install_env(*, port: int, backend: str) -> dict[str, str]:
    """Build the persistent install environment for OpenCode.

    Prepares the OpenCode transport plugin artifact at the managed
    operational artifact location and returns an environment variable
    pointing to it so the plugin can be loaded by OpenCode at runtime
    without depending on the Headroom repository checkout.

    If the plugin artifact cannot be prepared (e.g. npm unavailable), raises
    an actionable error instead of silently falling back to a missing native
    plugin.
    """
    del backend
    del port
    artifact_dir = prepare_opencode_plugin_artifact()
    return {"HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(artifact_dir)}


def apply_provider_scope(manifest: DeploymentManifest) -> ManagedMutation | None:
    """Apply OpenCode provider-scope configuration when requested."""
    if manifest.scope != ConfigScope.PROVIDER.value:
        return None

    config_file = opencode_config_path()
    config_file.parent.mkdir(parents=True, exist_ok=True)

    snapshot_opencode_config_if_unwrapped(
        config_file, config_file.with_suffix(".json.headroom-backup")
    )

    if config_file.exists():
        content = fsutil.read_text(config_file)
        data = _parse_json_loose(content)
    else:
        data = {}

    provider = {"headroom": headroom_provider_entry(manifest.port, host=manifest.host)}
    data = _inject_key_into_json(data, "provider", provider)

    # Inject plugin reference from managed operational artifact (issue #17).
    tool_env = manifest.tool_envs.get(ToolTarget.OPENCODE.value, {})
    if "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR" in tool_env:
        artifact_dir = tool_env["HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR"]
    else:
        artifact_dir = os.environ.get("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", "")
    plugin_path = headroom_opencode_plugin_path(
        env={"HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": artifact_dir}
    )
    if plugin_path:
        plugins = data.get("plugin")
        if isinstance(plugins, str):
            plugins = [plugins]
            data["plugin"] = plugins
        if not isinstance(plugins, list):
            plugins = []
            data["plugin"] = plugins
        if plugin_path not in plugins:
            plugins.append(plugin_path)

    config_file.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return ManagedMutation(
        target=ToolTarget.OPENCODE.value,
        kind="json-block",
        path=str(config_file),
    )


def revert_provider_scope(mutation: ManagedMutation, manifest: DeploymentManifest) -> None:
    """Revert OpenCode provider-scope configuration.

    Restores from pre-wrap backup when available, otherwise strips the
    headroom provider from the config file.
    """
    del manifest
    if not mutation.path:
        return
    path = Path(mutation.path)
    backup_file = path.with_suffix(".json.headroom-backup")
    if backup_file.exists():
        try:
            shutil.copy2(backup_file, path)
            backup_file.unlink()
            return
        except OSError:
            pass
    if not path.exists():
        return
    content = fsutil.read_text(path)
    cleaned = strip_opencode_headroom_blocks(content)
    if cleaned:
        path.write_text(cleaned + "\n", encoding="utf-8")
    else:
        path.unlink(missing_ok=True)
