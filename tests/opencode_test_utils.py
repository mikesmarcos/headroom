"""Shared test helpers for OpenCode CLI tests."""

from pathlib import Path

import pytest


def set_test_home(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Isolate OpenCode path resolution from the host environment."""
    home = str(tmp_path)
    monkeypatch.setenv("HOME", home)
    monkeypatch.setenv("USERPROFILE", home)
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / ".config"))
    monkeypatch.setenv("OPENCODE_HOME", str(tmp_path / ".config" / "opencode"))
    monkeypatch.setenv(
        "OPENCODE_CONFIG",
        str(tmp_path / ".config" / "opencode" / "opencode.json"),
    )
    monkeypatch.setenv("HEADROOM_CONFIG_DIR", str(tmp_path / ".headroom" / "config"))
    monkeypatch.setenv("HEADROOM_WORKSPACE_DIR", str(tmp_path / ".headroom" / "workspace"))
