"""Ownership-delta tests for OpenCode config transforms."""

from __future__ import annotations

from copy import deepcopy

from headroom.providers.opencode.config import (
    ConfigFileAction,
    apply_config_overlay,
    cleanup_opencode_wrap_config,
    cleanup_opencode_wrap_content,
    revert_config_overlay,
)


def _overlay(plugin: str = "/managed/plugin.js") -> dict[str, object]:
    return {
        "provider": {
            "anthropic": {"options": {"baseURL": "http://127.0.0.1:8787/v1"}},
            "openai": {"options": {"baseURL": "http://127.0.0.1:8787/v1"}},
            "headroom": {"name": "Headroom", "options": {"baseURL": "proxy"}},
        },
        "mcp": {"headroom": {"type": "local", "command": ["headroom", "mcp", "serve"]}},
        "plugin": [plugin],
    }


def test_apply_config_overlay_deep_merges_and_records_independent_ownership() -> None:
    original = {
        "provider": {
            "anthropic": {
                "options": {"apiKey": "anthropic-key", "timeout": 30},
                "models": {"opus": {"name": "User Opus"}},
            },
            "openai": {"options": {"apiKey": "openai-key"}},
        },
        "mcp": {"user": {"command": ["user-mcp"]}},
        "plugin": ["user-plugin"],
    }

    result = apply_config_overlay(original, _overlay())

    assert result.config["provider"]["anthropic"] == {
        "options": {
            "apiKey": "anthropic-key",
            "timeout": 30,
            "baseURL": "http://127.0.0.1:8787/v1",
        },
        "models": {"opus": {"name": "User Opus"}},
    }
    assert result.config["plugin"] == ["user-plugin", "/managed/plugin.js"]
    assert {operation["owner"] for operation in result.operations} == {
        "provider",
        "mcp",
        "plugin",
    }
    assert all(
        {"path", "existed", "previous", "applied"} <= operation.keys()
        for operation in result.operations
    )


def test_apply_config_overlay_preserves_existing_model_definition() -> None:
    original = {
        "provider": {
            "headroom": {
                "models": {
                    "gpt-4o": {
                        "name": "User GPT",
                        "limit": {"output": 4096},
                    }
                }
            }
        }
    }
    overlay = {
        "provider": {
            "headroom": {
                "models": {
                    "gpt-4o": {
                        "name": "Managed GPT",
                        "limit": {"output": 16384},
                    },
                    "new-model": {"name": "Managed new model"},
                }
            }
        }
    }

    result = apply_config_overlay(original, overlay)

    assert result.config["provider"]["headroom"]["models"] == {
        "gpt-4o": {
            "name": "User GPT",
            "limit": {"output": 4096},
        },
        "new-model": {"name": "Managed new model"},
    }


def test_revert_config_overlay_preserves_user_changes_after_apply() -> None:
    original = {
        "provider": {"anthropic": {"options": {"apiKey": "keep"}}},
        "plugin": ["user-plugin"],
    }
    applied = apply_config_overlay(original, _overlay())
    current = deepcopy(applied.config)
    current["provider"]["anthropic"]["options"]["baseURL"] = "https://user.example/v1"
    current["mcp"]["user-after-install"] = {"command": ["new"]}
    current["plugin"].append("later-plugin")

    reverted = revert_config_overlay(current, applied.operations)

    assert reverted.config == {
        "provider": {
            "anthropic": {"options": {"apiKey": "keep", "baseURL": "https://user.example/v1"}}
        },
        "mcp": {"user-after-install": {"command": ["new"]}},
        "plugin": ["user-plugin", "later-plugin"],
    }


def test_apply_config_overlay_does_not_claim_preexisting_plugin() -> None:
    original = {"plugin": ["/managed/plugin.js"]}
    applied = apply_config_overlay(original, {"plugin": ["/managed/plugin.js"]})

    assert applied.operations == []
    assert revert_config_overlay(applied.config, applied.operations).config == original


def test_revert_config_overlay_preserves_originally_empty_maps() -> None:
    original = {"provider": {}, "mcp": {}, "settings": {}}

    applied = apply_config_overlay(original, _overlay())
    reverted = revert_config_overlay(applied.config, applied.operations)

    assert reverted.config == original


def test_revert_config_overlay_handles_multiple_plugins_and_later_user_plugin() -> None:
    original = {"plugin": ["user-plugin"]}
    applied = apply_config_overlay(
        original,
        {"plugin": ["/managed/first.js", "/managed/second.js"]},
    )
    current = deepcopy(applied.config)
    current["plugin"].append("later-user-plugin")

    reverted = revert_config_overlay(current, applied.operations)

    assert reverted.config == {"plugin": ["user-plugin", "later-user-plugin"]}


def test_revert_config_overlay_keeps_ownership_independent_by_component() -> None:
    applied = apply_config_overlay({}, _overlay())
    current = deepcopy(applied.config)
    current["plugin"] = ["user-replaced-plugin"]

    reverted = revert_config_overlay(current, applied.operations)

    assert reverted.config == {"plugin": ["user-replaced-plugin"]}


def test_wrap_cleanup_requires_each_exact_canonical_component() -> None:
    overlay = _overlay()
    config = {
        "provider": {
            "headroom": overlay["provider"]["headroom"],
            "anthropic": {"options": {"baseURL": "https://user.example/v1"}},
        },
        "mcp": {"headroom": {"type": "local", "command": ["different"]}},
        "plugin": ["/user/headroom-opencode/dist/entry.opencode.js"],
    }

    result = cleanup_opencode_wrap_config(config, overlay)

    assert result.action is ConfigFileAction.WRITE
    assert result.config == {
        "provider": {
            "anthropic": {"options": {"baseURL": "https://user.example/v1"}},
        },
        "mcp": {"headroom": {"type": "local", "command": ["different"]}},
        "plugin": ["/user/headroom-opencode/dist/entry.opencode.js"],
    }


def test_wrap_cleanup_preserves_malformed_config() -> None:
    malformed = '{"provider": {"headroom": },}'

    result = cleanup_opencode_wrap_content(malformed, _overlay())

    assert result.action is ConfigFileAction.UNCHANGED
    assert result.config is None


def test_wrap_cleanup_preserves_user_edits_inside_legacy_marker() -> None:
    content = (
        "// --- Headroom proxy provider ---\n"
        '"provider": {"headroom": {"name": "Headroom", '
        '"options": {"baseURL": "proxy"}, "custom": "keep"}},\n'
        "// --- end Headroom proxy provider ---\n"
        '{"model": "openai/gpt-4o"}'
    )

    result = cleanup_opencode_wrap_content(content, _overlay())

    assert result.action is ConfigFileAction.WRITE
    assert result.config == {
        "provider": {"headroom": {"custom": "keep"}},
        "model": "openai/gpt-4o",
    }
