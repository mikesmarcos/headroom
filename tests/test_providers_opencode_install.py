"""Tests for OpenCode install-time helpers."""

from __future__ import annotations

import subprocess
import tarfile
from pathlib import Path

import pytest

from headroom.install.models import ConfigScope, DeploymentManifest
from headroom.providers.opencode.install import (
    apply_provider_scope,
    build_install_env,
    prepare_opencode_plugin_artifact,
    revert_provider_scope,
)

_PLUGIN_BODY = "export default () => {}"


def _manifest(port: int = 8787, host: str = "127.0.0.1") -> DeploymentManifest:
    return DeploymentManifest(
        profile="test",
        preset="persistent-task",
        runtime_kind="python",
        supervisor_kind="none",
        scope=ConfigScope.PROVIDER.value,
        provider_mode="auto",
        targets=[],
        port=port,
        host=host,
        backend="anthropic",
        proxy_args=[],
        base_env={},
        tool_envs={},
    )


def _plugin_tarball(tmp_path: Path, content: str = _PLUGIN_BODY) -> Path:
    package_root = tmp_path / "package"
    _write_plugin_entry(package_root, content=content)
    tarball = tmp_path / "headroom-opencode-0.1.0.tgz"
    with tarfile.open(tarball, "w:gz") as archive:
        archive.add(package_root, arcname="package")
    return tarball


def _write_plugin_entry(plugin_dir: Path, content: str = _PLUGIN_BODY) -> Path:
    entry = plugin_dir / "dist" / "entry.opencode.js"
    entry.parent.mkdir(parents=True)
    entry.write_text(content, encoding="utf-8")
    return entry


def test_build_install_env_errors_when_package_unavailable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """build_install_env fails clearly when the plugin artifact cannot be prepared."""
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / "ws"))
    monkeypatch.setattr(
        "headroom.providers.opencode.install._npm_pack_plugin",
        lambda package_spec, *, pack_dir: None,
    )
    with pytest.raises(RuntimeError, match="headroom-opencode@0.1.0"):
        build_install_env(port=8787, backend="anthropic")


def test_build_install_env_includes_npm_error_details(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """npm pack stderr is preserved in artifact preparation errors."""
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / "ws"))

    def fail_npm(*args: object, **kwargs: object) -> object:
        raise subprocess.CalledProcessError(
            1,
            ["npm", "pack", "headroom-opencode@0.1.0"],
            stderr="npm ERR! 404 Not Found",
        )

    monkeypatch.setattr("subprocess.run", fail_npm)

    with pytest.raises(RuntimeError, match="npm ERR! 404 Not Found"):
        build_install_env(port=8787, backend="anthropic")


def test_build_install_env_sets_artifact_dir(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """build_install_env sets HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR when plugin exists."""
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / "ws"))
    plugin_dir = tmp_path / "ws" / "plugins" / "headroom-opencode"
    _write_plugin_entry(plugin_dir)

    env = build_install_env(port=8787, backend="anthropic")
    assert "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR" in env
    assert env["HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR"] == str(plugin_dir)


# ---------------------------------------------------------------------------
# prepare_opencode_plugin_artifact
# ---------------------------------------------------------------------------


def test_prepare_artifact_returns_dest_dir(
    tmp_path: Path,
) -> None:
    """prepare_opencode_plugin_artifact returns the dest_dir path."""
    dest = tmp_path / "plugin"
    _write_plugin_entry(dest)
    result = prepare_opencode_plugin_artifact(dest_dir=dest)
    assert result == dest


def test_prepare_artifact_creates_dist_from_versioned_package(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """prepare_opencode_plugin_artifact extracts dist/ from the npm package."""
    tarball = _plugin_tarball(tmp_path)

    monkeypatch.setattr(
        "headroom.providers.opencode.install._npm_pack_plugin",
        lambda package_spec, *, pack_dir: tarball,
    )

    dest = tmp_path / "dest-plugin"
    result = prepare_opencode_plugin_artifact(dest_dir=dest)

    assert result == dest
    assert (dest / "dist" / "entry.opencode.js").is_file()
    assert (dest / "dist" / "entry.opencode.js").read_text(encoding="utf-8") == (
        _PLUGIN_BODY
    )


def test_prepare_artifact_idempotent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """prepare_opencode_plugin_artifact does not overwrite an existing artifact."""
    monkeypatch.setattr(
        "headroom.providers.opencode.install._npm_pack_plugin",
        lambda package_spec, *, pack_dir: pytest.fail("idempotent path should not call npm"),
    )
    dest = tmp_path / "plugin"
    entry = dest / "dist" / "entry.opencode.js"
    entry.parent.mkdir(parents=True)
    original_content = "export default () => original"
    entry.write_text(original_content, encoding="utf-8")

    result = prepare_opencode_plugin_artifact(dest_dir=dest)
    assert result == dest
    assert entry.read_text(encoding="utf-8") == original_content


def test_prepare_artifact_defaults_to_plugin_workspace(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """prepare_opencode_plugin_artifact uses plugin_workspace_dir by default."""
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / "ws"))
    tarball = _plugin_tarball(tmp_path)
    monkeypatch.setattr(
        "headroom.providers.opencode.install._npm_pack_plugin",
        lambda package_spec, *, pack_dir: tarball,
    )
    result = prepare_opencode_plugin_artifact()
    expected = tmp_path / "ws" / "plugins" / "headroom-opencode"
    assert result == expected


def test_prepare_artifact_raises_when_package_unavailable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """prepare_opencode_plugin_artifact fails clearly when npm pack fails."""
    monkeypatch.setattr(
        "headroom.providers.opencode.install._npm_pack_plugin",
        lambda package_spec, *, pack_dir: None,
    )
    dest = tmp_path / "plugin"
    with pytest.raises(RuntimeError, match="npm pack did not produce"):
        prepare_opencode_plugin_artifact(dest_dir=dest)
    assert not (dest / "dist" / "entry.opencode.js").is_file()


# ---------------------------------------------------------------------------


def test_apply_provider_scope_creates_config(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope creates the opencode config with headroom provider."""
    home = str(tmp_path)
    monkeypatch.setenv("HOME", home)
    monkeypatch.setenv("USERPROFILE", home)
    monkeypatch.delenv("OPENCODE_HOME", raising=False)
    monkeypatch.delenv("OPENCODE_CONFIG", raising=False)

    manifest = _manifest(port=8787)
    mutation = apply_provider_scope(manifest)
    assert mutation is not None
    assert mutation.target == "opencode"
    assert mutation.kind == "json-block"

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    assert config_file.exists()
    import json

    config = json.loads(config_file.read_text())
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://127.0.0.1:8787/v1"
    assert "models" in config["provider"]["headroom"]
    assert "mcp" not in config


def test_apply_provider_scope_uses_manifest_host(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope uses the manifest's client-reachable host."""
    home = str(tmp_path)
    monkeypatch.setenv("HOME", home)
    monkeypatch.setenv("USERPROFILE", home)
    monkeypatch.delenv("OPENCODE_HOME", raising=False)
    monkeypatch.delenv("OPENCODE_CONFIG", raising=False)

    manifest = _manifest(port=8787, host="::1")
    apply_provider_scope(manifest)

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    import json

    config = json.loads(config_file.read_text())
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://[::1]:8787/v1"


def test_apply_provider_scope_skips_when_scope_is_not_provider(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope returns None when scope is not PROVIDER."""
    manifest = _manifest()
    manifest.scope = ConfigScope.USER.value
    result = apply_provider_scope(manifest)
    assert result is None


def test_revert_provider_scope_restores_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """revert_provider_scope strips the Headroom block from the config."""
    home = str(tmp_path)
    monkeypatch.setenv("HOME", home)
    monkeypatch.setenv("USERPROFILE", home)
    monkeypatch.delenv("OPENCODE_HOME", raising=False)
    monkeypatch.delenv("OPENCODE_CONFIG", raising=False)

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text('{"model": "openai/gpt-4o"}')

    from headroom.install.models import ManagedMutation

    mutation = ManagedMutation(
        target="opencode",
        kind="json-block",
        path=str(config_file),
    )
    manifest = _manifest()
    revert_provider_scope(mutation, manifest)
    assert config_file.exists()
    assert config_file.read_text().strip() == '{"model": "openai/gpt-4o"}'


def test_revert_provider_scope_noop_when_file_missing(
    tmp_path: Path,
) -> None:
    """revert_provider_scope is a safe no-op when the config file is gone."""
    from headroom.install.models import ManagedMutation

    mutation = ManagedMutation(
        target="opencode",
        kind="json-block",
        path=str(tmp_path / "nonexistent.json"),
    )
    manifest = _manifest()
    revert_provider_scope(mutation, manifest)
    # Should not raise
