"""OpenCode config file helpers for wrap and persistent install.

The helpers in this module are pure: they format hosts into URL authorities
and render provider blocks, but they do NOT read the process environment.
Runtime host resolution (the bind-host-to-client-host rewrite and the
``HEADROOM_HOST`` lookup) lives in :mod:`headroom.providers.opencode.runtime`
and is performed once at the entry point so the canonical host can be passed
down as a plain string.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import click

from headroom import fsutil
from headroom.install.paths import opencode_config_path

# Headroom-managed JSON marker comments for idempotent block injection.
_PROVIDER_MARKER_START = "// --- Headroom proxy provider ---"
_PROVIDER_MARKER_END = "// --- end Headroom proxy provider ---"
_MCP_MARKER_START = "// --- Headroom MCP server ---"
_MCP_MARKER_END = "// --- end Headroom MCP server ---"

# Regex to strip headroom blocks (including the marker comments).
_PROVIDER_BLOCK_RE = re.compile(
    re.escape(_PROVIDER_MARKER_START) + r".*?" + re.escape(_PROVIDER_MARKER_END),
    re.DOTALL,
)
_MCP_BLOCK_RE = re.compile(
    re.escape(_MCP_MARKER_START) + r".*?" + re.escape(_MCP_MARKER_END),
    re.DOTALL,
)
HEADROOM_OPENCODE_PLUGIN = "headroom-opencode"

# Models exposed by the injected `headroom` provider. OpenCode only resolves
# `headroom/<id>` for ids listed in the provider's `models` map, so an empty
# map means every documented `headroom/*` model fails with "Model not found".
# Keep in sync with DEFAULT_MODELS in plugins/opencode/src/provider.ts and the
# table in plugins/opencode/README.md.
HEADROOM_OPENCODE_MODELS: dict[str, Any] = {
    "claude-sonnet-4-6": {
        "name": "Claude Sonnet 4.6",
        "limit": {"context": 200000, "output": 16384},
    },
    "claude-opus-4-6": {
        "name": "Claude Opus 4.6",
        "limit": {"context": 200000, "output": 16384},
    },
    "claude-haiku-4-5-20251001": {
        "name": "Claude Haiku 4.5",
        "limit": {"context": 200000, "output": 8192},
    },
    "gpt-4o": {
        "name": "GPT-4o",
        "limit": {"context": 128000, "output": 16384},
    },
    "gpt-4.1": {
        "name": "GPT-4.1",
        "limit": {"context": 1048576, "output": 32768},
    },
}


def headroom_url_authority(host: str) -> str:
    """Return ``host`` formatted for use in an HTTP URL authority.

    Brackets IPv6 literals (anything containing a colon) that are not already
    bracketed. Leaves IPv4 and DNS names untouched. ``host`` must be a
    canonical, client-reachable host string — no env reads, no wildcard
    rewrites happen here. See
    :func:`headroom.providers.opencode.runtime.headroom_client_host` for the
    bind-host-to-client-host conversion.
    """
    if ":" in host and not host.startswith("["):
        return f"[{host}]"
    return host


def headroom_provider_entry(port: int, *, host: str) -> dict[str, Any]:
    """Return the `headroom` provider block pointed at the local proxy.

    ``host`` must be the canonical, client-reachable proxy host (the value
    returned by
    :func:`headroom.providers.opencode.runtime.headroom_client_host`). This
    function performs no environment lookups and does not rewrite wildcards.
    """
    return {
        "npm": "@ai-sdk/openai-compatible",
        "name": "Headroom Proxy",
        "options": {"baseURL": f"http://{headroom_url_authority(host)}:{port}/v1"},
        "models": HEADROOM_OPENCODE_MODELS,
    }


def _opencode_home_dir() -> Path:
    """Return the OpenCode home/config directory."""
    env_path = os.environ.get("OPENCODE_HOME", "").strip()
    if env_path:
        return Path(env_path).expanduser()
    return Path.home() / ".config" / "opencode"


def opencode_config_paths() -> tuple[Path, Path]:
    """Return ``(config_file, backup_file)`` for OpenCode."""
    config_file = opencode_config_path()
    backup_file = config_file.with_suffix(".json.headroom-backup")
    return config_file, backup_file


def snapshot_opencode_config_if_unwrapped(config_file: Path, backup_file: Path) -> None:
    """Snapshot ``opencode.json`` to ``backup_file`` before the first injection.

    Guarantees that ``headroom unwrap opencode`` can restore the user's
    original file byte-for-byte.
    """
    if backup_file.exists():
        return
    if not config_file.exists():
        return
    try:
        content = fsutil.read_text(config_file)
    except OSError:
        return
    if _PROVIDER_MARKER_START in content or _MCP_MARKER_START in content:
        return
    backup_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(config_file, backup_file)


def strip_opencode_headroom_blocks(content: str, *, remove_mcp: bool = True) -> str:
    """Remove all Headroom-managed blocks from opencode JSON text.

    Preserves user content. Returns the cleaned string.
    """
    content = _PROVIDER_BLOCK_RE.sub("", content)
    if remove_mcp:
        content = _MCP_BLOCK_RE.sub("", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip()


@dataclass(frozen=True)
class ConfigOverlayResult:
    """A pure config transformation and its JSON-serializable ownership delta."""

    config: dict[str, Any]
    operations: list[dict[str, Any]]

    @property
    def changed(self) -> bool:
        return bool(self.operations)


class ConfigFileAction(str, Enum):
    """What a config-file caller should do with a cleanup result."""

    UNCHANGED = "unchanged"
    WRITE = "write"
    DELETE = "delete"


@dataclass(frozen=True)
class ConfigCleanupResult:
    """Explicit file action produced by a pure parsed-config cleanup."""

    action: ConfigFileAction
    config: dict[str, Any] | None = None


def _operation(
    kind: str,
    path: tuple[str, ...],
    *,
    existed: bool,
    previous: Any,
    applied: Any,
) -> dict[str, Any]:
    return {
        "kind": kind,
        "owner": path[0] if path and path[0] in {"provider", "mcp", "plugin"} else "config",
        "path": list(path),
        "existed": existed,
        "previous": deepcopy(previous),
        "applied": deepcopy(applied),
    }


def _apply_overlay_mapping(
    target: dict[str, Any],
    overlay: dict[str, Any],
    path: tuple[str, ...],
    operations: list[dict[str, Any]],
) -> None:
    for key, applied in overlay.items():
        item_path = (*path, key)
        existed = key in target
        previous = target.get(key)
        if isinstance(applied, dict):
            if not existed:
                target[key] = {}
                # Record the container itself.  Without this operation a
                # newly-created provider/mcp/options map would be left behind
                # after all of its owned leaves were reverted, and an
                # originally absent map could not be distinguished from an
                # originally empty one.
                operations.append(
                    _operation("set", item_path, existed=False, previous=None, applied={})
                )
                _apply_overlay_mapping(target[key], applied, item_path, operations)
            elif isinstance(previous, dict):
                if key == "models":
                    _apply_missing_mapping(previous, applied, item_path, operations)
                else:
                    _apply_overlay_mapping(previous, applied, item_path, operations)
            elif previous != applied:
                operations.append(
                    _operation("set", item_path, existed=True, previous=previous, applied=applied)
                )
                target[key] = deepcopy(applied)
            continue

        # OpenCode's plugin field is additive; other lists (such as MCP
        # commands) are ordinary values and are replaced as a unit.
        if isinstance(applied, list) and item_path == ("plugin",):
            _append_overlay_items(target, key, applied, operations)
        elif previous != applied or not existed:
            operations.append(
                _operation("set", item_path, existed=existed, previous=previous, applied=applied)
            )
            target[key] = deepcopy(applied)


def _apply_missing_mapping(
    target: dict[str, Any],
    overlay: dict[str, Any],
    path: tuple[str, ...],
    operations: list[dict[str, Any]],
) -> None:
    """Add missing model definitions without changing existing user entries."""
    for key, applied in overlay.items():
        if key in target:
            continue
        item_path = (*path, key)
        target[key] = deepcopy(applied)
        operations.append(
            _operation("set", item_path, existed=False, previous=None, applied=applied)
        )


def _append_overlay_items(
    target: dict[str, Any],
    key: str,
    applied_items: list[Any],
    operations: list[dict[str, Any]],
) -> None:
    path = (key,)
    for item in applied_items:
        existed = key in target
        previous = deepcopy(target.get(key))
        current = target.get(key)
        if isinstance(current, list):
            if item in current:
                continue
            current.append(deepcopy(item))
        elif isinstance(current, str) and isinstance(item, str):
            if current == item:
                continue
            target[key] = [current, deepcopy(item)]
        elif not existed:
            target[key] = [deepcopy(item)]
        else:
            replacement = [deepcopy(item)]
            operations.append(
                _operation("set", path, existed=True, previous=previous, applied=replacement)
            )
            target[key] = replacement
            continue
        operations.append(
            _operation("append", path, existed=existed, previous=previous, applied=item)
        )


def apply_config_overlay(config: dict[str, Any], overlay: dict[str, Any]) -> ConfigOverlayResult:
    """Deep-apply *overlay* without replacing unrelated nested user config."""
    updated = deepcopy(config)
    operations: list[dict[str, Any]] = []
    _apply_overlay_mapping(updated, overlay, (), operations)
    return ConfigOverlayResult(updated, operations)


def _resolve_parent(config: dict[str, Any], path: list[str]) -> tuple[dict[str, Any], str] | None:
    if not path:
        return None
    parent = config
    for key in path[:-1]:
        child = parent.get(key)
        if not isinstance(child, dict):
            return None
        parent = child
    return parent, path[-1]


def _prune_empty_parents(config: dict[str, Any], path: list[str]) -> None:
    for depth in range(len(path) - 1, 0, -1):
        resolved = _resolve_parent(config, path[:depth])
        if resolved is None:
            continue
        parent, key = resolved
        if parent.get(key) == {}:
            del parent[key]


def revert_config_overlay(
    config: dict[str, Any], operations: list[dict[str, Any]]
) -> ConfigOverlayResult:
    """Undo recorded operations only while their applied values remain owned."""
    updated = deepcopy(config)
    reverted: list[dict[str, Any]] = []
    for operation in reversed(operations):
        if not isinstance(operation, dict):
            continue
        path = operation.get("path")
        if not isinstance(path, list) or not path or not all(isinstance(key, str) for key in path):
            continue
        resolved = _resolve_parent(updated, path)
        if resolved is None:
            continue
        parent, key = resolved
        kind = operation.get("kind")
        applied = operation.get("applied")
        if kind == "append":
            current = parent.get(key)
            if not isinstance(current, list) or applied not in current:
                continue
            remaining = deepcopy(current)
            remaining.remove(applied)
            previous = operation.get("previous")
            if isinstance(previous, str) and remaining == [previous]:
                parent[key] = previous
            elif not operation.get("existed") and not remaining:
                del parent[key]
                _prune_empty_parents(updated, path)
            else:
                parent[key] = remaining
        elif kind == "set" and key in parent and parent[key] == applied:
            if operation.get("existed"):
                parent[key] = deepcopy(operation.get("previous"))
            else:
                del parent[key]
        else:
            continue
        reverted.append(deepcopy(operation))
    return ConfigOverlayResult(updated, reverted)


def _remove_exact_leaves(current: dict[str, Any], managed: dict[str, Any]) -> bool:
    changed = False
    for key, managed_value in managed.items():
        current_value = current.get(key)
        if isinstance(current_value, dict) and isinstance(managed_value, dict):
            if _remove_exact_leaves(current_value, managed_value):
                changed = True
                if not current_value:
                    del current[key]
        elif key in current and current_value == managed_value:
            del current[key]
            changed = True
    return changed


def _remove_exact_generated_wiring(
    config: dict[str, Any],
    overlay: dict[str, Any],
    *,
    remove_native_provider_routes: bool,
) -> ConfigCleanupResult:
    cleaned = deepcopy(config)
    changed = False

    providers = cleaned.get("provider")
    managed_providers = overlay.get("provider")
    if isinstance(providers, dict) and isinstance(managed_providers, dict):
        for name, managed in managed_providers.items():
            current = providers.get(name)
            if name == "headroom":
                if name in providers and current == managed:
                    del providers[name]
                    changed = True
            elif (
                remove_native_provider_routes
                and isinstance(current, dict)
                and isinstance(managed, dict)
            ):
                changed = _remove_exact_leaves(current, managed) or changed
                if not current:
                    del providers[name]
        if not providers:
            del cleaned["provider"]

    servers = cleaned.get("mcp")
    managed_servers = overlay.get("mcp")
    if isinstance(servers, dict) and isinstance(managed_servers, dict):
        for name, managed in managed_servers.items():
            if name in servers and servers[name] == managed:
                del servers[name]
                changed = True
        if not servers:
            del cleaned["mcp"]

    managed_plugins = overlay.get("plugin")
    plugins = cleaned.get("plugin")
    if isinstance(managed_plugins, list) and isinstance(plugins, list):
        for managed in managed_plugins:
            if managed in plugins:
                plugins.remove(managed)
                changed = True
        if not plugins:
            del cleaned["plugin"]
    elif isinstance(managed_plugins, list) and plugins in managed_plugins:
        del cleaned["plugin"]
        changed = True

    if not changed:
        return ConfigCleanupResult(ConfigFileAction.UNCHANGED)
    if not cleaned:
        return ConfigCleanupResult(ConfigFileAction.DELETE)
    return ConfigCleanupResult(ConfigFileAction.WRITE, cleaned)


def cleanup_opencode_wrap_config(
    config: dict[str, Any], canonical_overlay: dict[str, Any]
) -> ConfigCleanupResult:
    """Conservatively remove exact generated wrap values without a ledger."""
    return _remove_exact_generated_wiring(
        config, canonical_overlay, remove_native_provider_routes=False
    )


def cleanup_legacy_persistent_config(
    config: dict[str, Any], canonical_overlay: dict[str, Any]
) -> ConfigCleanupResult:
    """False-negative-safe fallback for old persistent mutations with no delta."""
    return _remove_exact_generated_wiring(
        config, canonical_overlay, remove_native_provider_routes=True
    )


def _merge_config_parts(target: dict[str, Any], source: dict[str, Any]) -> None:
    """Merge user config over a marked Headroom fragment."""
    for key, value in source.items():
        current = target.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            _merge_config_parts(current, value)
        else:
            target[key] = deepcopy(value)


def _parse_marked_fragment(fragment: str) -> dict[str, Any] | None:
    fragment = fragment.strip()
    if not fragment:
        return {}
    if not (fragment.startswith("{") and fragment.endswith("}")):
        fragment = "{" + fragment.rstrip(",").rstrip() + "}"
    return _parse_json_loose_optional(fragment)


def _extract_marked_config(content: str) -> tuple[dict[str, Any], dict[str, Any]] | None:
    """Parse legacy marker fragments while retaining their user-edited values."""
    marked: dict[str, Any] = {}
    remainder = content
    for start, end in (
        (_PROVIDER_MARKER_START, _PROVIDER_MARKER_END),
        (_MCP_MARKER_START, _MCP_MARKER_END),
    ):
        block_re = re.compile(re.escape(start) + r"(.*?)" + re.escape(end), re.DOTALL)
        matches = list(block_re.finditer(remainder))
        for match in matches:
            fragment = _parse_marked_fragment(match.group(1))
            if fragment is None:
                return None
            _merge_config_parts(marked, fragment)
        remainder = block_re.sub("", remainder)

    combined = deepcopy(marked)
    outside = remainder.strip()
    if outside:
        parsed_outside = _parse_json_loose_optional(outside)
        if parsed_outside is None:
            return None
        _merge_config_parts(combined, parsed_outside)
    return combined, marked


def _remove_marked_headroom_wiring(
    config: dict[str, Any],
    marked: dict[str, Any],
    canonical_overlay: dict[str, Any],
) -> dict[str, Any]:
    """Remove marked canonical leaves while retaining edits inside old blocks."""
    cleaned = deepcopy(config)
    for component in ("provider", "mcp"):
        marked_section = marked.get(component)
        current_section = cleaned.get(component)
        if not isinstance(marked_section, dict) or not isinstance(current_section, dict):
            continue
        if not marked_section and not current_section:
            del cleaned[component]
            continue

        managed_section = canonical_overlay.get(component)
        if not isinstance(managed_section, dict):
            continue
        marked_headroom = marked_section.get("headroom")
        current_headroom = current_section.get("headroom")
        managed_headroom = managed_section.get("headroom")
        if "headroom" not in marked_section or "headroom" not in current_section:
            continue
        if isinstance(current_headroom, dict) and isinstance(managed_headroom, dict):
            if not current_headroom and not marked_headroom:
                del current_section["headroom"]
            else:
                _remove_exact_leaves(current_headroom, managed_headroom)
                if not current_headroom:
                    del current_section["headroom"]
        elif current_headroom == marked_headroom and not marked_headroom:
            del current_section["headroom"]
        if not current_section:
            del cleaned[component]
    return cleaned


def cleanup_opencode_wrap_content(
    content: str, canonical_overlay: dict[str, Any]
) -> ConfigCleanupResult:
    """Parse wrap config, preserving malformed input, and return an explicit action."""
    has_markers = _PROVIDER_MARKER_START in content or _MCP_MARKER_START in content
    parsed: dict[str, Any]
    if has_markers:
        extracted = _extract_marked_config(content)
        if extracted is None:
            return ConfigCleanupResult(ConfigFileAction.UNCHANGED)
        parsed, marked = extracted
        if not parsed:
            return ConfigCleanupResult(ConfigFileAction.DELETE)
        parsed = _remove_marked_headroom_wiring(parsed, marked, canonical_overlay)
    else:
        candidate = _parse_json_loose_optional(content)
        if candidate is None:
            return ConfigCleanupResult(ConfigFileAction.UNCHANGED)
        parsed = candidate
    cleaned = cleanup_opencode_wrap_config(parsed, canonical_overlay)
    if cleaned.action is not ConfigFileAction.UNCHANGED:
        return cleaned
    if not has_markers:
        return cleaned
    if not parsed:
        return ConfigCleanupResult(ConfigFileAction.DELETE)
    return ConfigCleanupResult(ConfigFileAction.WRITE, parsed)


def render_opencode_config(config: dict[str, Any]) -> str:
    """Serialize a transformed OpenCode config for a file write."""
    return json.dumps(config, indent=2) + "\n"


def _parse_json_loose_optional(text: str) -> dict[str, Any] | None:
    """Parse JSON text, stripping line comments (// ...) when needed.

    Tries standard JSON first to avoid corrupting URLs that contain ``//``.
    Falls back to stripping ``//`` comments when standard parsing fails.
    Two-pass: (1) remove comment-only lines, (2) strip inline trailing
    comments that follow a comma.
    """
    try:
        parsed = json.loads(text)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        pass
    # Pass 1: remove lines that are ONLY a comment.
    cleaned = re.sub(r"^\s*//[^\n]*\n", "", text, flags=re.MULTILINE)
    # Pass 2: remove inline trailing comments (", // comment").
    cleaned = re.sub(r",\s*//[^\n]*", ",", cleaned)
    try:
        parsed = json.loads(cleaned)
        return parsed if isinstance(parsed, dict) else None
    except json.JSONDecodeError:
        return None


def _parse_json_loose(text: str) -> dict[str, Any]:
    """Parse an OpenCode object, retaining the legacy empty-object fallback."""
    return _parse_json_loose_optional(text) or {}


def _inject_key_into_json(data: dict[str, Any], key: str, value: Any) -> dict[str, Any]:
    """Merge ``value`` into ``data[key]`` idempotently."""
    existing = data.get(key)
    if isinstance(existing, dict) and isinstance(value, dict):
        merged = {**existing, **value}
        data[key] = merged
    else:
        data[key] = value
    return data


def inject_opencode_provider_config(port: int, *, host: str) -> None:
    """Inject a Headroom model provider into OpenCode's config file.

    ``host`` must be the canonical, client-reachable proxy host (the value
    returned by
    :func:`headroom.providers.opencode.runtime.headroom_client_host`). This
    function performs no environment lookups and does not rewrite wildcards;
    callers are responsible for resolving the canonical host once at the
    entry point.

    Safe to call multiple times — the injected block is fully replaced on
    each call, so re-running with a different ``port`` updates the config.
    Callers must snapshot the pre-wrap config via
    :func:`snapshot_opencode_config_if_unwrapped` before the first
    injection so ``headroom unwrap opencode`` can restore it byte-for-byte.
    """
    config_file = opencode_config_paths()[0]
    config_dir = config_file.parent

    try:
        config_dir.mkdir(parents=True, exist_ok=True)

        if config_file.exists():
            content = fsutil.read_text(config_file)
            data = _parse_json_loose(content)
        else:
            content = ""
            data = {}

        # Strip any prior Headroom-managed blocks before re-injecting.
        if _PROVIDER_MARKER_START in content or _MCP_MARKER_START in content:
            content = strip_opencode_headroom_blocks(content)
            data = _parse_json_loose(content)

        # Merge provider through the same deep overlay contract used by
        # persistent installs.  In particular, a pre-existing headroom
        # provider may contain user options/models that must not be discarded.
        applied = apply_config_overlay(
            data,
            {"provider": {"headroom": headroom_provider_entry(port, host=host)}},
        )
        config_file.write_text(render_opencode_config(applied.config), encoding="utf-8")
    except OSError as exc:
        raise click.ClickException(
            f"could not write OpenCode config at {config_file}: {exc}"
        ) from exc
