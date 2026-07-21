"""OpenCode install-time helpers."""

from __future__ import annotations

import os
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path
from typing import Any

from headroom import fsutil
from headroom import paths as _paths
from headroom._subprocess import run
from headroom.install.models import ConfigScope, DeploymentManifest, ManagedMutation, ToolTarget
from headroom.install.paths import opencode_config_path

from .config import (
    ConfigFileAction,
    _parse_json_loose_optional,
    apply_config_overlay,
    cleanup_legacy_persistent_config,
    cleanup_opencode_wrap_content,
    render_opencode_config,
    revert_config_overlay,
    snapshot_opencode_config_if_unwrapped,
)
from .runtime import build_opencode_config_content

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
        result = run(
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
    operational artifact location and returns environment variables so the
    plugin can be loaded by OpenCode at runtime without depending on the
    Headroom repository checkout.

    ``HEADROOM_PROXY_URL`` tells the transport plugin which proxy to route
    all provider traffic through. The host is always ``127.0.0.1`` because
    the persistent proxy binds to loopback.

    If the plugin artifact cannot be prepared (e.g. npm unavailable), raises
    an actionable error instead of silently falling back to a missing native
    plugin.
    """
    del backend
    artifact_dir = prepare_opencode_plugin_artifact()
    return {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(artifact_dir),
        "HEADROOM_PROXY_URL": f"http://127.0.0.1:{port}",
    }


def _persistent_config_overlay(manifest: DeploymentManifest) -> dict[str, Any]:
    tool_env = manifest.tool_envs.get(ToolTarget.OPENCODE.value, {})
    artifact_dir = tool_env.get("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR")
    if artifact_dir is None:
        artifact_dir = os.environ.get("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", "")
    artifact_env = {"HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": artifact_dir}
    return build_opencode_config_content(
        port=manifest.port,
        host=manifest.host,
        env=artifact_env,
    )


def _persistent_cleanup_overlay(manifest: DeploymentManifest) -> dict[str, Any]:
    """Build the old-manifest cleanup overlay without requiring the plugin."""
    try:
        return _persistent_config_overlay(manifest)
    except RuntimeError:
        # A missing optional artifact cannot justify retaining independent
        # provider/MCP wiring.  It also cannot prove ownership of any plugin
        # path, so leave plugin entries for the user rather than guessing.
        return build_opencode_config_content(
            port=manifest.port,
            host=manifest.host,
            env={},
            include_plugin=False,
        )


def apply_provider_scope(manifest: DeploymentManifest) -> ManagedMutation | None:
    """Apply OpenCode provider-scope configuration when requested.

    Raises
    ------
    RuntimeError
        If a configured transport plugin artifact cannot be resolved.
    """
    if manifest.scope != ConfigScope.PROVIDER.value:
        return None

    config_file = opencode_config_path()
    config_file.parent.mkdir(parents=True, exist_ok=True)
    overlay = _persistent_config_overlay(manifest)

    if config_file.exists():
        try:
            content = fsutil.read_text(config_file)
        except OSError:
            return None
        data = {} if not content.strip() else _parse_json_loose_optional(content)
        # A provider-scope install is a full JSON rewrite.  Never turn an
        # unreadable or malformed existing config into an empty managed file,
        # and do not create a backup for an apply that did not happen.
        if data is None:
            return None
    else:
        data = {}

    snapshot_opencode_config_if_unwrapped(
        config_file, config_file.with_suffix(".json.headroom-backup")
    )

    applied = apply_config_overlay(data, overlay)
    config_file.write_text(render_opencode_config(applied.config), encoding="utf-8")
    return ManagedMutation(
        target=ToolTarget.OPENCODE.value,
        kind="json-block",
        path=str(config_file),
        data={"version": 1, "operations": applied.operations},
    )


def revert_provider_scope(mutation: ManagedMutation, manifest: DeploymentManifest) -> None:
    """Revert OpenCode provider-scope configuration.

    Restores from pre-wrap backup when available, otherwise strips only
    Headroom-managed plugin, provider, and MCP wiring from the config file.
    """
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
    data = _parse_json_loose_optional(content)
    if data is None:
        cleaned_content = cleanup_opencode_wrap_content(
            content, _persistent_cleanup_overlay(manifest)
        )
        if cleaned_content.action is ConfigFileAction.WRITE and cleaned_content.config is not None:
            path.write_text(render_opencode_config(cleaned_content.config), encoding="utf-8")
        elif cleaned_content.action is ConfigFileAction.DELETE:
            path.unlink(missing_ok=True)
        return

    mutation_data = mutation.data if isinstance(mutation.data, dict) else {}
    operations = mutation_data.get("operations")
    if mutation_data.get("version") == 1 and isinstance(operations, list):
        reverted = revert_config_overlay(data, operations)
        if not reverted.changed:
            return
        if reverted.config:
            path.write_text(render_opencode_config(reverted.config), encoding="utf-8")
        else:
            path.unlink(missing_ok=True)
        return

    # Old manifests did not persist ownership. Exact canonical values are the
    # only safe fallback; ambiguity intentionally leaves stale wiring behind.
    cleaned = cleanup_legacy_persistent_config(data, _persistent_cleanup_overlay(manifest))
    if cleaned.action is ConfigFileAction.WRITE and cleaned.config is not None:
        path.write_text(render_opencode_config(cleaned.config), encoding="utf-8")
    elif cleaned.action is ConfigFileAction.DELETE:
        path.unlink(missing_ok=True)
