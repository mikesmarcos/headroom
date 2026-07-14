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
    # Collapse multiple blank lines left behind by block removal.
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip()


def _parse_json_loose(text: str) -> dict[str, Any]:
    """Parse JSON text, stripping line comments (// ...) when needed.

    Tries standard JSON first to avoid corrupting URLs that contain ``//``.
    Falls back to stripping ``//`` comments when standard parsing fails.
    Two-pass: (1) remove comment-only lines, (2) strip inline trailing
    comments that follow a comma.
    """
    try:
        parsed = json.loads(text)
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        pass
    # Pass 1: remove lines that are ONLY a comment.
    cleaned = re.sub(r"^\s*//[^\n]*\n", "", text, flags=re.MULTILINE)
    # Pass 2: remove inline trailing comments (", // comment").
    cleaned = re.sub(r",\s*//[^\n]*", ",", cleaned)
    try:
        parsed = json.loads(cleaned)
        return parsed if isinstance(parsed, dict) else {}
    except json.JSONDecodeError:
        return {}


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
    Before the first injection, the pre-wrap file is snapshotted to
    ``opencode.json.headroom-backup`` so ``headroom unwrap opencode``
    can restore it byte-for-byte.
    """
    config_file, backup_file = opencode_config_paths()
    config_dir = config_file.parent

    try:
        config_dir.mkdir(parents=True, exist_ok=True)
        snapshot_opencode_config_if_unwrapped(config_file, backup_file)

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

        # Merge provider into the JSON data structure.
        provider = {"headroom": headroom_provider_entry(port, host=host)}
        data = _inject_key_into_json(data, "provider", provider)

        # Write back as formatted JSON (opencode uses standard JSON with comments).
        output = json.dumps(data, indent=2) + "\n"
        config_file.write_text(output, encoding="utf-8")
    except OSError as exc:
        raise click.ClickException(
            f"could not write OpenCode config at {config_file}: {exc}"
        ) from exc
