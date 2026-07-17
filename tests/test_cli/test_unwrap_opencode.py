"""Tests for ``headroom unwrap opencode``."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

import pytest
from click.testing import CliRunner

from headroom.cli import wrap as wrap_mod
from headroom.cli.main import main
from headroom.mcp_registry import build_headroom_spec
from headroom.providers.opencode.config import (
    _PROVIDER_MARKER_END,
    _PROVIDER_MARKER_START,
    headroom_provider_entry,
)
from headroom.providers.opencode.runtime import build_opencode_config_content
from tests.opencode_test_utils import set_test_home


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture(autouse=True)
def isolate_proxy_startup(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep unwrap setup tests from starting or reusing a real proxy process."""
    monkeypatch.setattr(
        wrap_mod,
        "_ensure_proxy",
        lambda port, no_proxy, **kwargs: (None, port),
    )


def test_unwrap_opencode_removes_rtk_from_agents_md(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("HEADROOM_CONTEXT_TOOL", raising=False)
    set_test_home(monkeypatch, tmp_path)

    with patch.object(wrap_mod.shutil, "which", return_value="opencode"):
        with patch.object(wrap_mod, "_launch_tool", side_effect=SystemExit(0)):
            with patch.object(wrap_mod, "_ensure_rtk_binary", return_value=Path("/tmp/rtk")):
                runner.invoke(main, ["wrap", "opencode", "--port", "9000", "--no-mcp"])

    global_agents = tmp_path / ".config" / "opencode" / "AGENTS.md"
    project_agents = tmp_path / "AGENTS.md"
    assert wrap_mod._RTK_MARKER in global_agents.read_text(encoding="utf-8")
    assert wrap_mod._RTK_MARKER in project_agents.read_text(encoding="utf-8")

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    for path in (global_agents, project_agents):
        assert not path.exists() or wrap_mod._RTK_MARKER not in path.read_text(encoding="utf-8")


def test_unwrap_opencode_restores_from_backup(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    backup_file = config_file.with_suffix(".json.headroom-backup")
    config_file.parent.mkdir(parents=True, exist_ok=True)
    headroom_spec = build_headroom_spec()
    original = (
        json.dumps(
            {
                "model": "openai/gpt-4o",
                "mcp": {
                    "headroom": {
                        "type": "local",
                        "command": [headroom_spec.command, *headroom_spec.args],
                        "enabled": True,
                    }
                },
            },
            indent=2,
        ).replace("\n", "\r\n")
        + "\r\n"
    ).encode()
    config_file.write_text("managed", encoding="utf-8")
    backup_file.write_bytes(original)

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert "Restored prior" in result.output
    assert not backup_file.exists()
    assert config_file.read_bytes() == original


def test_unwrap_opencode_strips_blocks_when_no_backup(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    user_content = '{"model": "openai/gpt-4o"}'
    config_file.write_text(
        _PROVIDER_MARKER_START + '\n"provider": {},\n' + _PROVIDER_MARKER_END + "\n" + user_content,
        encoding="utf-8",
    )

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert "Removed Headroom wiring" in result.output
    assert json.loads(config_file.read_text(encoding="utf-8")) == {"model": "openai/gpt-4o"}


def test_unwrap_opencode_removes_config_when_only_headroom_content(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(
        _PROVIDER_MARKER_START + "\n" + _PROVIDER_MARKER_END,
        encoding="utf-8",
    )

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert not config_file.exists()


def test_unwrap_opencode_removes_structured_managed_only_config(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(
        json.dumps({"provider": {"headroom": headroom_provider_entry(9999, host="127.0.0.1")}}),
        encoding="utf-8",
    )

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode", "--port", "9999"])

    assert result.exit_code == 0, result.output
    assert not config_file.exists()


def test_unwrap_opencode_preserves_malformed_config_without_backup(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    malformed = b'{"provider": {"headroom": },}\r\n'
    config_file.write_bytes(malformed)

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode", "--port", "9999"])

    assert result.exit_code == 0, result.output
    assert config_file.read_bytes() == malformed


def test_unwrap_opencode_missing_plugin_does_not_block_other_cleanup(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    plugin_dir = tmp_path / "managed" / "headroom-opencode"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    config = build_opencode_config_content(
        port=9999,
        host="127.0.0.1",
        env={"HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(plugin_dir)},
    )
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(json.dumps(config), encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(tmp_path / "missing-plugin"))

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode", "--port", "9999"])

    assert result.exit_code == 0, result.output
    restored = json.loads(config_file.read_text(encoding="utf-8"))
    assert "headroom" not in restored["provider"]
    assert "headroom" not in restored.get("mcp", {})
    assert restored["plugin"] == [str(plugin_entry)]


def test_unwrap_opencode_noop_when_config_missing(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert "does not exist" in result.output


def test_unwrap_opencode_noop_when_no_headroom_markers(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    original = json.dumps(
        {
            "provider": {"openai": {"options": {"baseURL": "http://127.0.0.1:8787/v1"}}},
            "plugin": ["/user/headroom-opencode/dist/entry.opencode.js"],
        }
    )
    config_file.write_text(original, encoding="utf-8")

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert "no Headroom wiring" in result.output
    assert config_file.read_text(encoding="utf-8") == original


def test_unwrap_opencode_preserves_noncanonical_user_headroom_mcp(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    original = {"mcp": {"headroom": {"type": "local", "command": ["user-command"]}}}
    config_file.write_text(json.dumps(original), encoding="utf-8")

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert json.loads(config_file.read_text(encoding="utf-8")) == original


def test_unwrap_opencode_removes_matching_registered_headroom_mcp(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    expected = build_headroom_spec("http://127.0.0.1:9999")
    removed: list[str] = []

    class FakeRegistrar:
        name = "opencode"
        display_name = "OpenCode"

        def detect(self) -> bool:
            return True

        def get_server(self, name: str) -> object | None:
            return expected if name == "headroom" else None

        def unregister_server(self, name: str) -> bool:
            removed.append(name)
            return True

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text('{"model": "openai/gpt-4o"}', encoding="utf-8")

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        with patch("headroom.mcp_registry.OpencodeRegistrar", FakeRegistrar):
            result = runner.invoke(main, ["unwrap", "opencode", "--port", "9999"])

    assert result.exit_code == 0, result.output
    assert removed == ["headroom"]


def test_unwrap_opencode_missing_plugin_artifact_does_not_block_other_cleanup(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    monkeypatch.setenv(
        "HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR",
        str(tmp_path / "missing-plugin"),
    )
    config = build_opencode_config_content(
        port=9999,
        host="127.0.0.1",
        env={},
        include_plugin=False,
    )
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(json.dumps(config), encoding="utf-8")
    fake_registrar = type("FakeRegistrar", (), {"detect": lambda self: False})()

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        with patch("headroom.mcp_registry.OpencodeRegistrar", return_value=fake_registrar):
            result = runner.invoke(main, ["unwrap", "opencode", "--port", "9999"])

    assert result.exit_code == 0, result.output
    restored = json.loads(config_file.read_text(encoding="utf-8"))
    assert restored == {
        "provider": {
            "anthropic": {"options": {"baseURL": "http://127.0.0.1:9999/v1"}},
            "openai": {"options": {"baseURL": "http://127.0.0.1:9999/v1"}},
        }
    }


def test_unwrap_opencode_strips_structured_content_when_no_backup_no_markers(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """CLI delegates no-ledger cleanup to the conservative structured fallback."""
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    plugin_dir = tmp_path / "managed" / "headroom-opencode"
    plugin_entry = plugin_dir / "dist" / "entry.opencode.js"
    plugin_entry.parent.mkdir(parents=True)
    plugin_entry.write_text("export default () => {}", encoding="utf-8")
    monkeypatch.setenv("HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR", str(plugin_dir))

    config = build_opencode_config_content(
        port=8787,
        host="127.0.0.1",
        env={"HEADROOM_OPENCODE_PLUGIN_ARTIFACT_DIR": str(plugin_dir)},
    )
    provider = config["provider"]
    assert isinstance(provider, dict)
    provider["openai"]["apiKey"] = "sk-user"
    provider["anthropic"]["models"] = {"opus": {"name": "Opus"}}
    provider["custom"] = {"npm": "custom-pkg"}
    mcp = config["mcp"]
    assert isinstance(mcp, dict)
    # Keep the canonical headroom MCP entry produced by
    # build_opencode_config_content exactly; the conservative wrap fallback
    # only removes values that match the canonical overlay, so a resolved-path
    # variant (see test_*_preserves_noncanonical_user_headroom_mcp) is
    # intentionally preserved.
    mcp["user-server"] = {"type": "local", "command": ["user-tool"]}
    config["plugin"] = ["/user/plugin.js", str(plugin_entry)]
    config["model"] = "openai/gpt-4o"
    config["permission"] = {"edit": "allow"}

    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text(json.dumps(config), encoding="utf-8")
    fake_registrar = type("FakeRegistrar", (), {"detect": lambda self: False})()

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        with patch("headroom.mcp_registry.OpencodeRegistrar", return_value=fake_registrar):
            result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    restored = json.loads(config_file.read_text(encoding="utf-8"))
    assert restored == {
        "provider": {
            "anthropic": {
                "options": {"baseURL": "http://127.0.0.1:8787/v1"},
                "models": {"opus": {"name": "Opus"}},
            },
            "openai": {
                "options": {"baseURL": "http://127.0.0.1:8787/v1"},
                "apiKey": "sk-user",
            },
            "custom": {"npm": "custom-pkg"},
        },
        "mcp": {"user-server": {"type": "local", "command": ["user-tool"]}},
        "plugin": ["/user/plugin.js"],
        "model": "openai/gpt-4o",
        "permission": {"edit": "allow"},
    }


def test_unwrap_opencode_restores_backup_and_removes_it(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    backup_file = config_file.with_suffix(".json.headroom-backup")
    config_file.parent.mkdir(parents=True, exist_ok=True)
    config_file.write_text("managed", encoding="utf-8")
    backup_file.write_text('{"model": "openai/gpt-4o"}', encoding="utf-8")

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert not backup_file.exists()


def test_unwrap_opencode_preserves_utf8_user_content(
    runner: CliRunner,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    set_test_home(monkeypatch, tmp_path)
    config_file = tmp_path / ".config" / "opencode" / "opencode.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    user_json = json.dumps(
        {"model": "openai/gpt-4o", "description": "“smart quotes” and an em dash — here"},
        ensure_ascii=False,
    )
    config_file.write_text(
        _PROVIDER_MARKER_START + '\n"provider": {},\n' + _PROVIDER_MARKER_END + "\n" + user_json,
        encoding="utf-8",
    )
    fake_registrar = type("FakeRegistrar", (), {"detect": lambda self: False})()

    with patch.object(wrap_mod, "_stop_local_proxy_for_unwrap", return_value="stopped"):
        with patch("headroom.mcp_registry.OpencodeRegistrar", return_value=fake_registrar):
            result = runner.invoke(main, ["unwrap", "opencode"])

    assert result.exit_code == 0, result.output
    assert json.loads(config_file.read_text(encoding="utf-8"))["description"] == (
        "“smart quotes” and an em dash — here"
    )
