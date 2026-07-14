"""Runtime helpers for OpenCode integrations.

This module owns the runtime/environment side of OpenCode host resolution:

* :func:`headroom_client_host` reads ``HEADROOM_HOST`` (from the supplied env
  mapping or ``os.environ``), applies the bind-host-to-client-host wildcard
  rewrite (``0.0.0.0`` → ``127.0.0.1``, ``::`` → ``::1``), and returns a
  canonical, client-reachable host string. Callers pass that string down to
  the pure helpers in :mod:`headroom.providers.opencode.config`.

The config helpers in :mod:`headroom.providers.opencode.config` are pure
formatters — they perform no environment lookups and no wildcard rewrites —
so the canonical host is resolved exactly once, here, at the entry point.
"""

from __future__ import annotations

import json
import os
from collections.abc import Mapping
from ipaddress import ip_address
from pathlib import Path

from headroom.mcp_registry.install import DEFAULT_PROXY_URL

from .config import (
    HEADROOM_OPENCODE_PLUGIN,
    headroom_provider_entry,
    headroom_url_authority,
)


def headroom_client_host(*, env: Mapping[str, str] | None = None) -> str:
    """Return the client-reachable proxy host for generated OpenCode config.

    Reads ``HEADROOM_HOST`` from ``env`` if provided, otherwise from
    :data:`os.environ`. The returned value is canonical and safe to use
    directly as a URL host:

    * unset / empty → ``"127.0.0.1"``
    * IPv4 unspecified (``0.0.0.0``) → ``"127.0.0.1"``
    * IPv6 unspecified (``::``) → ``"::1"``
    * bracketed IPv6 (``"[::1]"``) is unbracketed before parsing
    * any other literal is returned as ``str(ipaddress)`` (or as-is for
      non-IP strings like DNS names)
    """
    raw = (env if env is not None else os.environ).get("HEADROOM_HOST", "").strip()
    if not raw:
        return "127.0.0.1"
    try:
        parsed = ip_address(raw.strip("[]"))
    except ValueError:
        return raw
    if parsed.is_unspecified:
        return "::1" if parsed.version == 6 else "127.0.0.1"
    return str(parsed)


def proxy_base_url(port: int, host: str) -> str:
    """Return the local proxy base URL used by OpenCode integrations.

    ``host`` must be a canonical, client-reachable host string (no
    wildcards). Callers that need bind-host-to-client-host rewriting should
    resolve the host with :func:`headroom_client_host` first.
    """
    return f"http://{headroom_url_authority(host)}:{port}/v1"


def headroom_opencode_plugin_path(env: Mapping[str, str] | None = None) -> str | None:
    """Return the configured OpenCode transport plugin path, or None.

    Operational wrapping does not discover ``plugins/opencode/dist`` from a
    mutable development checkout. Installers that enable the optional native
    plugin must resolve a stable artifact and pass that explicit path through
    ``HEADROOM_OPENCODE_PLUGIN_PATH``. Without that configured artifact, wrap
    falls back to provider ``baseURL`` routing.

    The plugin's loader entry exports ONLY the plugin function
    (``dist/entry.opencode.js``); the library barrel cannot be loaded directly
    ("Plugin export is not a function").
    """
    environ = env if env is not None else os.environ
    override = environ.get("HEADROOM_OPENCODE_PLUGIN_PATH", "").strip()
    if override:
        return override if Path(override).is_file() else None
    return None


def build_opencode_config_content(
    *,
    port: int,
    host: str,
    env: Mapping[str, str] | None = None,
    include_mcp: bool = True,
    include_plugin: bool = True,
) -> dict[str, object]:
    """Build JSON payload for ``OPENCODE_CONFIG_CONTENT``.

    ``host`` must be the canonical, client-reachable proxy host (the value
    returned by :func:`headroom_client_host`). This function performs no
    environment lookups and does not rewrite wildcards; the host is taken
    as-is.

    Two complementary routing layers (both verified against opencode 1.17):

    1. **Native-provider baseURL override** — points OpenCode's built-in
       ``anthropic`` / ``openai`` providers at the proxy. Keeps native provider
       identity (model metadata, output-token limits) and reuses the user's own
       API keys (env / ``opencode auth``); the proxy forwards upstream by path
       (``/v1/messages`` → Anthropic, ``/v1/chat/completions`` → OpenAI). This
       is the reliable always-on layer and the only one shipped pip-only
       installs need.

    2. **Transparent transport plugin** — when a stable plugin artifact path is
       explicitly configured, it is loaded by absolute path and patches
       ``fetch``/``http`` to reroute *every* provider's traffic through the
       proxy, tagging the real upstream via ``x-headroom-base-url``. This covers
       providers we don't name (Gemini, Copilot, custom gateways) and providers
       added mid-session. The plugin self-configures from ``HEADROOM_PROXY_URL``
       (set in :func:`build_launch_env`). Loopback URLs are not double-routed,
       so it coexists with layer 1.

    ponytail: config-level ``options.baseURL`` is reliable where the env-var
    override (``ANTHROPIC_BASE_URL``) is not — verified against opencode 1.17.
    """
    authority = headroom_url_authority(host)
    base_url = proxy_base_url(port, host)
    config: dict[str, object] = {
        "provider": {
            "anthropic": {"options": {"baseURL": base_url}},
            "openai": {"options": {"baseURL": base_url}},
            "headroom": headroom_provider_entry(port, host=host),
        }
    }
    if include_mcp:
        proxy_url = f"http://{authority}:{port}"
        mcp_entry: dict[str, object] = {
            "type": "local",
            "command": ["headroom", "mcp", "serve"],
            "enabled": True,
        }
        if proxy_url != DEFAULT_PROXY_URL:
            mcp_entry["environment"] = {"HEADROOM_PROXY_URL": proxy_url}
        config["mcp"] = {
            "headroom": mcp_entry,
        }
    if include_plugin:
        plugin_path = headroom_opencode_plugin_path(env)
        if plugin_path:
            # Plain absolute-path string; the plugin reads HEADROOM_PROXY_URL
            # from the launch env (build_launch_env sets it).
            config["plugin"] = [plugin_path]
    return config


def build_launch_env(
    port: int,
    environ: Mapping[str, str] | None = None,
    project: str | None = None,
    *,
    host: str | None = None,
    include_mcp: bool = True,
    include_plugin: bool = True,
) -> tuple[dict[str, str], list[str]]:
    """Build environment variables for launching OpenCode through Headroom.

    ``OPENCODE_CONFIG_CONTENT`` carries Headroom provider/MCP/plugin config.
    Existing provider/base URL environment variables are preserved. When the
    transport plugin is loaded, ``HEADROOM_PROXY_URL`` tells it which proxy to
    route to.

    Unless ``host`` is provided by the caller, the proxy host is resolved once
    via :func:`headroom_client_host` (from ``HEADROOM_HOST`` in ``environ`` or
    ``os.environ``) and the resulting canonical value is passed down to the
    config helpers — no env reads or wildcard rewrites happen downstream.
    """
    env = dict(environ if environ is not None else os.environ)

    host = host or headroom_client_host(env=env)
    config_content = build_opencode_config_content(
        port=port,
        host=host,
        env=env,
        include_mcp=include_mcp,
        include_plugin=include_plugin,
    )
    env["OPENCODE_CONFIG_CONTENT"] = json.dumps(config_content, separators=(",", ":"))

    display = ["OPENCODE_CONFIG_CONTENT={provider: headroom}"]
    if "plugin" in config_content:
        env["HEADROOM_PROXY_URL"] = f"http://{headroom_url_authority(host)}:{port}"
        display.append(f"plugin={HEADROOM_OPENCODE_PLUGIN}")

    if project and "HEADROOM_PROJECT" not in env:
        env["HEADROOM_PROJECT"] = project

    return env, display
