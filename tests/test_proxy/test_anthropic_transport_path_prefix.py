"""Tests for Anthropic transport path-prefix reconstruction from upstream hints."""

from __future__ import annotations

from unittest.mock import AsyncMock

import httpx
import pytest

pytest.importorskip("fastapi")

from fastapi.testclient import TestClient

from headroom.proxy.server import ProxyConfig, create_app


def _build_anthropic_client():
    config = ProxyConfig(
        optimize=False,
        cache_enabled=False,
        rate_limit_enabled=False,
        cost_tracking_enabled=False,
        log_requests=False,
        ccr_inject_tool=False,
        ccr_handle_responses=False,
        ccr_context_tracking=False,
        image_optimize=False,
    )

    app = create_app(config)
    proxy = app.state.proxy
    captured: dict[str, object] = {}

    async def _fake_retry(
        method: str,
        url: str,
        headers: dict[str, str],
        body: dict,
        **_kwargs: object,
    ) -> httpx.Response:
        captured["method"] = method
        captured["url"] = url
        captured["headers"] = headers
        captured["body"] = body
        return httpx.Response(
            200,
            json={
                "id": "msg_1",
                "type": "message",
                "role": "assistant",
                "model": body.get("model", "claude"),
                "content": [{"type": "text", "text": "ok"}],
                "stop_reason": "end_turn",
                "usage": {"input_tokens": 10, "output_tokens": 2},
            },
        )

    proxy._retry_request = _fake_retry
    record_request_outcome = AsyncMock()
    proxy._record_request_outcome = record_request_outcome
    captured["record_request_outcome"] = record_request_outcome

    return TestClient(app), captured


def test_messages_upstream_reconstruction_uses_original_transport_path() -> None:
    body = {
        "model": "minimax-m3",
        "max_tokens": 8,
        "messages": [{"role": "user", "content": "hi"}],
    }
    headers = {
        "x-api-key": "sk-test",
        "anthropic-version": "2023-06-01",
        "x-headroom-base-url": "https://opencode.ai",
        "x-headroom-original-path": "/zen/go/v1/messages",
        "user-agent": "opencode/1.17.14 ai-sdk/provider-utils/4.0.27 runtime/bun/1.3.14",
    }

    client, captured = _build_anthropic_client()
    response = client.post("/v1/messages?foo=1", headers=headers, json=body)
    assert response.status_code == 200, response.text

    assert captured["method"] == "POST"
    assert captured["url"] == "https://opencode.ai/zen/go/v1/messages?foo=1"

    assert isinstance(captured.get("headers"), dict)
    outbound_header_names = {k.lower() for k in captured["headers"].keys()}  # type: ignore[union-attr]
    assert "x-headroom-base-url" not in outbound_header_names
    assert "x-headroom-original-path" not in outbound_header_names

    recorder = captured["record_request_outcome"]
    outcome = recorder.await_args.args[0]  # type: ignore[union-attr]
    assert outcome.provider == "opencode"


def test_invalid_messages_original_path_falls_back_to_v1() -> None:
    body = {
        "model": "minimax-m3",
        "max_tokens": 8,
        "messages": [{"role": "user", "content": "hi"}],
    }
    headers = {
        "x-api-key": "sk-test",
        "anthropic-version": "2023-06-01",
        "x-headroom-base-url": "https://opencode.ai",
        "x-headroom-original-path": "https://evil.example/messages",
    }

    client, captured = _build_anthropic_client()
    response = client.post("/v1/messages", headers=headers, json=body)
    assert response.status_code == 200, response.text

    assert captured["method"] == "POST"
    assert captured["url"] == "https://opencode.ai/v1/messages"
