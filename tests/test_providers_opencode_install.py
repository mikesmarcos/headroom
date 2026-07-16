"""Tests for OpenCode install-time helpers."""

from __future__ import annotations

import json
import subprocess
import tarfile
from pathlib import Path

import pytest

from headroom.install.models import ConfigScope, DeploymentManifest
from headroom.providers.opencode.config import snapshot_opencode_config_if_unwrapped
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


def _isolate_opencode_config_dir(monkeypatch: pytest.MonkeyPatch, home: Path) -> Path:
    """Point OpenCode config resolution at ``home`` and clear plugin/config overrides."""
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("USERPROFILE", str(home))
    monkeypatch.delenv("OPENCODE_HOME", raising=False)
    monkeypatch.delenv("OPENCODE_CONFIG", raising=False)
    monkeypatch.delenv("HEADROOM_OPENCODE_PLUGIN_PATH", raising=False)
    monkeypatch.delenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", raising=False)
    return home / ".config" / "opencode"


def _install_opencode_for_provider_scope(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Run the install-time OpenCode artifact prep and provider-scope config write."""
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / "ws"))
    tarball = _plugin_tarball(tmp_path)
    monkeypatch.setattr(
        "headroom.providers.opencode.install._npm_pack_plugin",
        lambda package_spec, *, pack_dir: tarball,
    )

    env = build_install_env(port=8787, backend="anthropic")
    manifest = _manifest(port=8787)
    manifest.tool_envs["opencode"] = {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": env["HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR"],
    }
    apply_provider_scope(manifest)


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


def test_build_install_env_sets_proxy_url(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """build_install_env sets HEADROOM_PROXY_URL using the provided port."""
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / "ws"))
    monkeypatch.setattr(
        "headroom.providers.opencode.install.prepare_opencode_plugin_artifact",
        lambda **kwargs: tmp_path / "plugin",
    )
    env = build_install_env(port=8787, backend="anthropic")
    assert env["HEADROOM_PROXY_URL"] == "http://127.0.0.1:8787"

    env = build_install_env(port=9999, backend="anthropic")
    assert env["HEADROOM_PROXY_URL"] == "http://127.0.0.1:9999"


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
    assert (dest / "dist" / "entry.opencode.js").read_text(encoding="utf-8") == (_PLUGIN_BODY)


def test_prepare_artifact_idempotent(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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


def test_apply_provider_scope_includes_plugin_from_artifact_dir(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope injects plugin path from tool_envs artifact dir."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Create plugin artifact at a known location.
    plugin_dir = tmp_path / "managed" / "headroom-opencode"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    checkout_entry = tmp_path / "checkout" / "plugins" / "opencode" / "dist" / "entry.opencode.js"
    checkout_entry.parent.mkdir(parents=True)
    checkout_entry.write_text("export default () => {}", encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_PATH", str(checkout_entry))

    manifest = _manifest(port=8787)
    manifest.tool_envs["opencode"] = {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(plugin_dir),
    }
    mutation = apply_provider_scope(manifest)
    assert mutation is not None

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config = json.loads(config_file.read_text())
    assert config["plugin"] == [str(plugin_entry)]
    # Provider block is still present.
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://127.0.0.1:8787/v1"


def test_apply_provider_scope_includes_plugin_from_env(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope injects plugin path from os.environ artifact dir."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Create plugin artifact and set env var.
    plugin_dir = tmp_path / "env-managed" / "headroom-opencode"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(plugin_dir))

    manifest = _manifest(port=8787)
    mutation = apply_provider_scope(manifest)
    assert mutation is not None

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config = json.loads(config_file.read_text())
    assert config["plugin"] == [str(plugin_entry)]


def test_apply_provider_scope_no_plugin_by_default(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """No plugin injected when no artifact configured — even if checkout exists.

    Without ``HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR`` or
    ``HEADROOM_OPENCODE_PLUGIN_PATH``, the generated config must not contain
    a plugin reference — even if a development checkout file happens to exist
    on disk (issue #17, acceptance criterion 2).
    """
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Even if a checkout-like file exists on disk, it is not auto-discovered.
    checkout_path = tmp_path / "plugins" / "opencode" / "dist" / "entry.opencode.js"
    checkout_path.parent.mkdir(parents=True)
    checkout_path.write_text("export default () => {}", encoding="utf-8")

    manifest = _manifest(port=8787)
    mutation = apply_provider_scope(manifest)
    assert mutation is not None

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config = json.loads(config_file.read_text())
    # No plugin key when no managed artifact is configured.
    assert "plugin" not in config


def test_apply_provider_scope_preserves_existing_unrelated_config(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope preserves existing unrelated top-level keys."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Pre-populate config with unrelated keys.
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(
        json.dumps(
            {
                "model": "openai/gpt-4o",
                "permission": {"bash": {"*": "ask"}},
            }
        )
    )

    # Create plugin artifact and set env var.
    plugin_dir = tmp_path / "managed"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(plugin_dir))

    manifest = _manifest(port=8787)
    mutation = apply_provider_scope(manifest)
    assert mutation is not None

    config = json.loads(config_file.read_text())
    # Unrelated keys preserved.
    assert config["model"] == "openai/gpt-4o"
    assert config["permission"] == {"bash": {"*": "ask"}}
    # Plugin and provider injected.
    assert config["plugin"] == [str(plugin_entry)]
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://127.0.0.1:8787/v1"


def test_apply_provider_scope_preserves_existing_plugin_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope appends Headroom's artifact without removing user plugins."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(json.dumps({"plugin": ["existing-plugin"]}), encoding="utf-8")

    plugin_dir = tmp_path / "managed"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(plugin_dir))

    manifest = _manifest(port=8787)
    apply_provider_scope(manifest)

    config = json.loads(config_file.read_text())
    assert config["plugin"] == ["existing-plugin", str(plugin_entry)]


def test_apply_provider_scope_preserves_existing_string_plugin_entry(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope preserves a user plugin encoded as a single string."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(json.dumps({"plugin": "existing-plugin"}), encoding="utf-8")

    plugin_dir = tmp_path / "managed"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(plugin_dir))

    manifest = _manifest(port=8787)
    apply_provider_scope(manifest)

    config = json.loads(config_file.read_text())
    assert config["plugin"] == ["existing-plugin", str(plugin_entry)]


def test_apply_provider_scope_raises_when_configured_artifact_is_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope fails clearly when the configured artifact is stale."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(tmp_path / "missing"))

    with pytest.raises(RuntimeError, match="HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR"):
        apply_provider_scope(_manifest(port=8787))


def test_apply_provider_scope_creates_config(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope creates the opencode config with headroom provider."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    manifest = _manifest(port=8787)
    mutation = apply_provider_scope(manifest)
    assert mutation is not None
    assert mutation.target == "opencode"
    assert mutation.kind == "json-block"

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    assert config_file.exists()
    config = json.loads(config_file.read_text())
    # All three provider routes point at the proxy (issue #18).
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://127.0.0.1:8787/v1"
    assert "models" in config["provider"]["headroom"]
    assert config["provider"]["anthropic"]["options"]["baseURL"] == "http://127.0.0.1:8787/v1"
    assert config["provider"]["openai"]["options"]["baseURL"] == "http://127.0.0.1:8787/v1"
    # MCP config is injected (issue #18). Default port 8787 → no HEADROOM_PROXY_URL.
    assert "mcp" in config
    assert config["mcp"]["headroom"]["command"] == ["headroom", "mcp", "serve"]
    assert "environment" not in config["mcp"]["headroom"]


def test_install_does_not_create_npm_state_in_empty_opencode_config_dir(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Installing OpenCode support leaves an empty config dir free of npm state."""
    opencode_dir = _isolate_opencode_config_dir(monkeypatch, tmp_path)

    _install_opencode_for_provider_scope(monkeypatch, tmp_path)

    assert sorted(path.name for path in opencode_dir.iterdir()) == ["opencode.json"]
    assert (opencode_dir / "opencode.json").is_file()
    assert not any(opencode_dir.rglob("package.json"))
    assert not any(opencode_dir.rglob("package-lock.json"))
    assert not any(opencode_dir.rglob("node_modules"))


def test_install_preserves_user_npm_state_in_opencode_config_dir(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Installing OpenCode support does not create or clobber config-dir npm state."""
    opencode_dir = _isolate_opencode_config_dir(monkeypatch, tmp_path)
    opencode_dir.mkdir(parents=True)
    user_package = opencode_dir / "package.json"
    user_package.write_text('{"private": true}\n', encoding="utf-8")
    user_node_modules = opencode_dir / "node_modules"
    user_node_modules.mkdir()
    user_module_marker = user_node_modules / ".user-owned"
    user_module_marker.write_text("keep\n", encoding="utf-8")

    _install_opencode_for_provider_scope(monkeypatch, tmp_path)

    assert sorted(path.name for path in opencode_dir.iterdir()) == [
        "node_modules",
        "opencode.json",
        "package.json",
    ]
    assert (opencode_dir / "opencode.json").is_file()
    assert user_package.read_text(encoding="utf-8") == '{"private": true}\n'
    assert user_module_marker.read_text(encoding="utf-8") == "keep\n"
    assert not (opencode_dir / "package-lock.json").exists()


def test_apply_provider_scope_uses_manifest_host(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope uses the manifest's client-reachable host."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    manifest = _manifest(port=8787, host="::1")
    apply_provider_scope(manifest)

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config = json.loads(config_file.read_text())
    # All providers use the IPv6 host.
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://[::1]:8787/v1"
    assert config["provider"]["anthropic"]["options"]["baseURL"] == "http://[::1]:8787/v1"
    assert config["provider"]["openai"]["options"]["baseURL"] == "http://[::1]:8787/v1"
    assert config["mcp"]["headroom"]["environment"] == {"HEADROOM_PROXY_URL": "http://[::1]:8787"}


def test_apply_provider_scope_non_default_port_consistency(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Non-default port is reflected consistently in provider, MCP, and env."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    manifest = _manifest(port=9999)
    apply_provider_scope(manifest)

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config = json.loads(config_file.read_text())
    # Provider baseURLs reflect the non-default port.
    assert config["provider"]["headroom"]["options"]["baseURL"] == "http://127.0.0.1:9999/v1"
    assert config["provider"]["anthropic"]["options"]["baseURL"] == "http://127.0.0.1:9999/v1"
    assert config["provider"]["openai"]["options"]["baseURL"] == "http://127.0.0.1:9999/v1"
    # MCP config includes HEADROOM_PROXY_URL for non-default port.
    assert config["mcp"]["headroom"]["environment"] == {
        "HEADROOM_PROXY_URL": "http://127.0.0.1:9999"
    }
    assert config["mcp"]["headroom"]["command"] == ["headroom", "mcp", "serve"]


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
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

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


# ---------------------------------------------------------------------------
# Snapshot and byte-for-byte backup/restore contract
# ---------------------------------------------------------------------------


def test_snapshot_backup_is_byte_for_byte(tmp_path: Path) -> None:
    """snapshot copies bytes without normalizing line endings."""
    config_file = tmp_path / "opencode.json"
    # Content with Windows-style line endings to test raw-byte preservation.
    original_bytes = b'{"model": "test"}\r\n'
    config_file.write_bytes(original_bytes)
    backup_file = config_file.with_suffix(".json.headroom-backup")

    snapshot_opencode_config_if_unwrapped(config_file, backup_file)
    assert backup_file.exists()
    # shutil.copy2 preserves raw bytes, including \r\n.
    assert backup_file.read_bytes() == original_bytes


def test_snapshot_noop_when_config_missing(tmp_path: Path) -> None:
    """snapshot is a no-op when the config file does not exist."""
    config_file = tmp_path / "opencode.json"
    backup_file = config_file.with_suffix(".json.headroom-backup")

    snapshot_opencode_config_if_unwrapped(config_file, backup_file)
    assert not backup_file.exists()


def test_apply_revert_restores_byte_for_byte(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Apply->revert restores the original config byte-for-byte.

    Verifies the apply->revert byte-for-byte restore contract:
    - ``apply_provider_scope`` snapshots the original before mutation.
    - The backup matches the original byte-for-byte.
    - Backup content contains no Headroom wiring.
    - ``revert_provider_scope`` restores from the backup.
    - The backup is cleaned up after revert.
    - The restored config no longer contains Headroom-managed plugin,
      provider, or MCP wiring.
    """
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Pre-existing user config.
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    original = (
        json.dumps({"model": "openai/gpt-4o", "custom": True, "plugin": ["user-tool"]}, indent=2)
        + "\n"
    )
    original_bytes = original.encode("utf-8")
    config_file.write_bytes(original_bytes)

    plugin_dir = tmp_path / ".headroom" / "plugins" / "headroom-opencode"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")

    manifest = _manifest(port=8787)
    manifest.tool_envs["opencode"] = {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(plugin_dir),
    }
    mutation = apply_provider_scope(manifest)
    assert mutation is not None

    # Backup was created from the original, before mutation.
    backup_file = config_file.with_suffix(".json.headroom-backup")
    assert backup_file.exists()
    assert backup_file.read_bytes() == original_bytes
    assert "headroom" not in json.loads(backup_file.read_text(encoding="utf-8"))

    # Active config now has Headroom wiring.
    active = json.loads(config_file.read_text(encoding="utf-8"))
    assert "headroom" in active.get("provider", {})
    assert "headroom" in active.get("mcp", {})
    assert str(plugin_entry) in active.get("plugin", [])

    # Revert — should restore from backup.
    revert_provider_scope(mutation, manifest)

    # File restored byte-for-byte.
    assert config_file.read_bytes() == original_bytes

    # Backup cleaned up.
    assert not backup_file.exists()

    # No Headroom-managed wiring remains.
    restored = json.loads(config_file.read_text(encoding="utf-8"))
    assert "headroom" not in restored.get("provider", {})
    assert "headroom" not in restored.get("mcp", {})
    # Original user plugin entry is preserved.
    assert restored.get("plugin") == ["user-tool"]


# ---------------------------------------------------------------------------
# Checkout-coupled plugin rejection safeguards (issue #19)
# ---------------------------------------------------------------------------


def test_apply_provider_scope_rejects_checkout_coupled_plugin_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope raises when tool_envs points at a checkout path."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Create a checkout-like path.
    checkout_path = tmp_path / "repo" / "plugins" / "opencode" / "dist" / "entry.opencode.js"
    checkout_path.parent.mkdir(parents=True)
    checkout_path.write_text("export default () => {}", encoding="utf-8")

    manifest = _manifest(port=8787)
    manifest.tool_envs["opencode"] = {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(checkout_path.parent.parent),
    }

    with pytest.raises(RuntimeError) as exc_info:
        apply_provider_scope(manifest)
    msg = str(exc_info.value)
    assert "checkout" in msg.lower()


def test_apply_provider_scope_rejects_file_dependency_plugin_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope raises when tool_envs contains a file: dependency."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    manifest = _manifest(port=8787)
    manifest.tool_envs["opencode"] = {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": "file:./plugins/opencode",
    }

    with pytest.raises(RuntimeError) as exc_info:
        apply_provider_scope(manifest)
    assert "file:" in str(exc_info.value)


def test_apply_provider_scope_accepts_valid_managed_artifact_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """apply_provider_scope accepts a valid managed artifact path."""
    _isolate_opencode_config_dir(monkeypatch, tmp_path)

    # Create a managed artifact path (not a checkout).
    artifact_dir = tmp_path / ".headroom" / "plugins" / "headroom-opencode"
    plugin_entry = artifact_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")

    manifest = _manifest(port=8787)
    manifest.tool_envs["opencode"] = {
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(artifact_dir),
    }

    mutation = apply_provider_scope(manifest)
    assert mutation is not None

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config = json.loads(config_file.read_text())
    assert config["plugin"] == [str(plugin_entry)]
