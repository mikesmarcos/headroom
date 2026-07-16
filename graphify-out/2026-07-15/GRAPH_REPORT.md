# Graph Report - headroom  (2026-07-15)

## Corpus Check
- 865 files · ~1,188,863 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 18958 nodes · 37257 edges · 674 communities (636 shown, 38 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 1595 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `46251717`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- __init__.py
- LocalBackend
- HeadroomProxy
- Provider
- __init__.py
- LocalBackendConfig
- helpers.py
- server.py
- openai.py
- MemoryBackend
- MemoryHandler
- _Response
- __init__.py
- pipeline.py
- MLModelRegistry
- code_compressor.py
- wrap.py
- utils.py
- ToolIntelligenceNetwork
- TelemetryCollector
- HTMLExtractor
- TrafficLearner
- kompress_compressor.py
- binaries.py
- SmartCrusherConfig
- Any
- install_registry.py
- ContentRouter
- config.py
- OpenAIProvider
- crusher.rs
- content_router.py
- claude
- SessionData
- MemoryBridge
- run.py
- LiteLLMBackend
- BodyMutationTracker
- DeploymentManifest
- doctor.py
- update.py
- PipelineExtensionManager
- anthropic.py
- anchor_selector.rs
- prometheus.rs
- sync.py
- Any
- BaseCacheOptimizer
- suite_runner.py
- batch_compression_eval.py
- __init__.py
- diff_compressor.rs
- init.py
- compression_store.py
- __init__.py
- __init__.py
- SmartCrusher
- paths.py
- ContentType
- LocalToolPattern
- StreamingMixin
- formatter.rs
- dynamic_detector.py
- GoogleCacheOptimizer
- ImageCompressor
- MemoryToolAdapter
- run
- paths.py
- statistics.rs
- HeadroomAgnoModel
- analyzer.rs
- lib.rs
- BatchResultProcessor
- orchestrator.rs
- HeadroomMCPServer
- output_shaper.py
- tag_protector.rs
- LearnPlugin
- planning.rs
- parse_commits
- analyzer.py
- __init__.py
- __init__.py
- release_version.py
- HNSWVectorIndex
- DirectMem0Adapter
- project_context.py
- run.py
- writer.py
- model_metadata.py
- CLI Reference
- EstimatingTokenCounter
- SearchCompressor
- adaptive_sizer.rs
- traits.rs
- wrap.py
- SQLiteMemoryStore
- forwarded_headers.py
- invoke_streaming.rs
- drift_detector.rs
- proxy.rs
- PrefixCacheTracker
- lib.rs
- Any
- WebSocketSessionRegistry
- CcrStore
- volatile_detector.rs
- CompressionStore
- content_detector.rs
- .path
- analyzer.py
- proxy_routes.py
- live_zone.rs
- universal.py
- Memory
- SmartCrusherBuilder
- .plan_smart_sample
- SubscriptionTracker
- diff_noise.rs
- walker.rs
- openclaw
- HeadroomConfig
- PromptComparisonResult
- .get
- _headroom_bypass_enabled
- PrometheusMetrics
- handle_invoke
- api-reference.mdx
- code_handler.py
- registry.py
- ImportanceSignal
- codex_rate_limits.py
- keyword_detector.rs
- hf_impl.rs
- registry.rs
- .new
- network_diff.py
- memory.py
- adversarial_grid.py
- ProjectInfo
- Memory
- __init__.py
- models.py
- BaseTokenizer
- HeadroomHookProvider
- AnthropicCacheOptimizer
- ContextTracker
- QuotaTracker
- embedding.rs
- json_offload.rs
- crushers.rs
- openai_cache_key.rs
- get_compression_store
- SemanticCache
- read_lifecycle.py
- Option
- log_template.rs
- search_offload.rs
- live_zone_anthropic.rs
- session_probes.py
- litellm_pricing.py
- LogCompressor
- hybrid.rs
- magika_detector.rs
- recommendations.rs
- ResponseState
- __init__.py
- compilerOptions
- CCRToolInjector
- StructureMask
- HeadroomPostHook
- responses.py
- images.py
- openai.py
- Phase B — Live-Zone-Only Compression Engine
- Phase I — Test Infrastructure (Continuous, Parallel)
- Image Compression
- Option
- installer.py
- UniversalCompressor
- parser.py
- verbosity.py
- RegisterResult
- PR-D1 — Native Bedrock InvokeModel route (non-streaming)
- Transform Reference
- dependencies
- bm25.rs
- releases.mdx
- SavingsLedger
- models.py
- SavingsTracker
- HuggingFaceTokenizer
- Phase C — Rust Proxy Paths
- Phase E — Phase 3 Cache Stabilization
- PR-F1 — `classify_auth_mode` helper
- repro_codex_replay.py
- Agno Integration
- Configuration
- LangChain Integration
- TrainedRouter
- anchors.rs
- outliers.rs
- eventstream_to_sse.rs
- JSONStructureHandler
- registry.py
- API Reference
- HeadroomChatMessageHistory
- tiktoken_impl.rs
- GcpAdcTokenSource
- e2e_simulators.rs
- PyDiffCompressionResult
- source.ts
- AnyLLMBackend
- CompressionOnlyRunner
- HeadroomLangSmithCallbackHandler
- savings_tracker.py
- Dynamic SmartCrusher Preservation Plan
- Troubleshooting Guide
- InMemoryCcrStore
- diff_offload.rs
- log_offload.rs
- stats_math.rs
- eventstream.rs
- anthropic_cache_control.rs
- Config
- SseEvent
- Self
- Headroom Evaluation Framework
- opencode.py
- AnthropicTokenCounter
- StageTimer
- TiktokenCounter
- Proxy Server Documentation
- HeadroomDocumentCompressor
- start_proxy_with_state
- start_proxy_with
- PySmartCrusherConfig
- agent_savings.py
- mcp.py
- providers.py
- ClaudeCodePlugin
- ServerSpec
- output_savings.py
- generator.py
- savings_ledger.py
- PipelineConfig
- orchestration.rs
- framing.rs
- domain.rs
- troubleshooting.mdx
- read_maturation.py
- copilot_auth.py
- EmbeddingScorer
- MistralTokenizer
- compact_lossless
- PR-H1 — Retire Python proxy request path
- Headroom
- Quickstart Guide
- devDependencies
- cache_control.rs
- Compaction
- AppState
- OpenAICacheOptimizer
- BaseStructureHandler
- TransformPipeline
- CostTracker
- __init__.py
- auth_mode.py
- PR-G1 — Wrap CLI breadth: cline, continue, goose, openhands
- Proxy Metrics
- compute_key
- classifier.rs
- crusher.rs
- ccr_roundtrip.rs
- live_zone_openai.rs
- headers.rs
- mount_anthropic_capture
- API endpoints
- HeadroomError
- qdrant_env.py
- resolve_codex_routing
- memory_ranker.py
- main
- installation.mdx
- copilot_auth.py
- get_store
- TextStatisticsExtractor
- RelevanceScorer
- SharedContext
- pr-governance.py
- Universal Compression
- ws_handler
- .new
- LegacyMutexStore
- .for_mode
- estimator.rs
- .new
- CompactionStage
- traits.rs
- integration_bedrock_invoke.rs
- configuration.mdx
- Proxy-wide (Phase G PR-G3)
- Memory
- HybridScorer
- FileSystemTOINBackend
- Benchmarks
- Headroom Learn
- responses_items.rs
- .new
- LiveZoneOutcome
- LogCompressor
- unidiff_detector.rs
- openai_chat.rs
- handle_vertex_predict_dispatch
- integration_cache_control.rs
- CaptureWriter
- integration_metrics.rs
- HeadroomCallback
- _start_proxy
- _optimize_content_block
- Any
- MemorySystem
- AgentWriter
- ssl_context.py
- 2.2 The cache-safety invariants (every PR enforces)
- replay_codex_ws_load.py
- version-sync.py
- MCP Server — Context Engineering Toolkit
- fix: Codex proxy resilience under reconnect storms
- SDK Guide
- tool_def_normalize.rs
- live_zone_responses.rs
- forward_vertex_request
- integration_bedrock_authmode.rs
- mount_capture
- integration_e4_openai_cache_key.rs
- bundle.py
- prepare_outbound_body_bytes
- cost.py
- WindowTokens
- Error Handling
- CompressionMiddleware
- e2e_real.rs
- SqliteCcrStore
- log_compressor.rs
- auth_mode.rs
- envelope.rs
- toin_publish.py
- is_copilot_api_url
- BaselineModel
- .count_messages
- resolve_policy
- Integration Guide
- TurnContext
- .apply
- sigv4.rs
- handle_responses
- integration_bedrock_streaming.rs
- integration_chat_completions.rs
- CaptureWriter
- config.rs
- CacheOptimizerRegistry
- tools.py
- prometheus_metrics.py
- MemoryBudgetManager
- MemoryTracker
- MemoryQuery
- rate_limiter.py
- LogLine
- integration_bedrock_metrics.rs
- mdx.tsx
- docker-install.mdx
- metrics.mdx
- inject_memory_instruction
- .count_message
- astgrep.py
- tracker.py
- INDEX.md
- 12 — Decisions Needed
- test_version_sync.py
- Docker-Native Install
- API
- detection.rs
- integration_responses_streaming.rs
- mcp.mdx
- persistent-installs.mdx
- BatchContextStore
- tokensave_installer.py
- _MemoryAPI
- MemoryToolsCompletions
- config.py
- install.py
- verbosity_controller.py
- BM25Scorer
- headroom-sbom-all-extra.cdx.json
- test_sync_plugin_versions.py
- Persistent Installs
- TypeScript SDK
- classifier.rs
- start
- community-charts.tsx
- benchmarks.mdx
- limitations.mdx
- opencode.mdx
- OpenCodePlugin
- compression_summary.py
- P5 — Auth-mode + observability + fingerprinting
- Headroom Limitations & Known Behavior
- Text Compression Utilities
- RedisCcrStore
- compress_anthropic_live_zone_with_ccr
- .new
- search_compressor.rs
- String
- cache_control.rs
- live_zone_dispatch.rs
- main
- .index_batch
- marketing.tsx
- failure-learning.mdx
- filesystem-contract.mdx
- .feature_names
- build_proxy_targets
- CCSwitchReconciler
- runtime_env.py
- tool_injection_config.py
- client.py
- count_tokens_messages
- CCR: Compress-Cache-Retrieve
- Filesystem Contract
- mod.rs
- safety.rs
- auth_mode_layer.rs
- envelope.rs
- ProxyHandle
- mount_anthropic_capture
- RequestFacts
- presentation.rs
- errors.mdx
- memory.mdx
- shared-context.mdx
- CacheOptimizer
- CopilotTokenProvider
- resolve_subscription_bearer_token_details
- ._get_conn
- MemoryToolsWrapper
- retag_to_headroom
- .count_message
- OpenAICompatibleTokenCounter
- apply_openai_responses_verbosity_steering
- context.py
- WarmupSlot
- export_kompress_v2_onnx.py
- relevance_split.py
- P4 — OpenAI long-tail + Bedrock/Vertex
- discover_onnxruntime_libraries
- mount_anthropic_capture
- sse_anthropic.rs
- ccr.mdx
- ci-cd-flows.mdx
- image-compression.mdx
- package.json
- RTK architecture — why wrap-CLI only
- install_all
- VectorMetadata
- .extract
- handle_openai_responses_subpath
- test_pr_governance.py
- Persistent Deployments / Installs Design
- Strands Integration
- plan_block_replacements
- model_limits.rs
- main
- PyDiffCompressorConfig
- Claude Code + AWS Bedrock, with Headroom compression
- architecture.mdx
- code-compression.mdx
- MemoryFilter
- wrapper_tools.py
- P1 — Wire-format / streaming corruption
- P2 — Architectural over-build
- P6 — Test-infra & parity
- dispatch_compressor
- EventStreamParser
- integration_sse.rs
- run
- PyTextCrusherConfig
- .new
- agent-orchestration.mdx
- index.mdx
- langchain.mdx
- strands.mdx
- text-and-logs.mdx
- EvalSuiteResult
- SQLiteVectorIndex
- ProcessStats
- .export
- ClaudeCodeMemoryWriter
- build_launch_env
- output_turn_policy.py
- HeadroomContribution
- 01 — Comprehensive Bug & Gap List
- P3 — Missing infrastructure (Phase 3 cache stabilization)
- Headroom SDK: A Complete Explanation
- .flavor_for
- HeaderValue
- handle_chat_completions
- agno.mdx
- claude-code-vertex.mdx
- how-compression-works.mdx
- StructureHandler
- _configured_enterprise_domain
- copilot_macos_keychain.py
- ._serialize_f32
- budget.py
- extraction.py
- .handle_memory_update
- MemoryReport
- MemoryEntry
- .export
- semantic_cache.py
- load_spreadsheet
- install.sh
- CCR Architecture: Compress-Cache-Retrieve
- Getting Started with Headroom
- macOS Deployment Guide
- auth_mode.rs
- create_scorer
- LevelClassifier
- sse_openai_chat.rs
- mitm_capture.py
- map.tsx
- anthropic-sdk.mdx
- claude-code-azure-foundry.mdx
- local-llm-prefill.mdx
- quickstart.mdx
- simulation.mdx
- vercel-ai-sdk.mdx
- .__init__
- .get_all_component_stats
- normalize_request_path
- _get_litellm_module
- .count_text
- .apply
- error_detection.py
- tag_protector.py
- PR-A1 — Make `/v1/messages` compression a passthrough
- PR-A3 — Switch Python forwarders to byte-faithful body forwarding
- PR-A4 — Honor customer `cache_control` markers in Rust; enable `arbitrary_precision`+`raw_value`
- PR-A8 — Hotfix Python wire-format bugs; add SHA-256 round-trip test
- PR-B1 — The big delete: retire ICM and its dependencies
- PR-B2 — Live-zone block dispatcher in Rust
- smoke_issue_327.py
- Headroom Latency Benchmarks
- `signals/` — detection traits
- SmartCrusherConfig
- Provider-specific strategies
- Protection rules
- litellm.mdx
- openai-sdk.mdx
- smart-crusher.mdx
- show_memory
- copilot_linux_secret.py
- Any
- .count_message
- runtime.py
- .snapshot
- compute_semantic_cache_key
- wire_debug_format_policy.py
- wire_debug_redaction_policy.py
- PR-A5 — Strip `x-headroom-*` from upstream-bound headers
- PR-A6 — Pin `anthropic-beta` order; session-stickiness skeleton
- PR-A7 — Memory tool injection session-sticky
- PR-A2 — Stop mutating the system prompt; route memory context to live zone
- PR-B6 — Memory subsystem refactor: live-zone tail injection only
- PR-C3 — `/v1/responses` handler in Rust (HTTP)
- PR-E3 — Auto `cache_control` breakpoint placement (Anthropic)
- PR-E4 — `prompt_cache_key` auto-injection (OpenAI)
- Reproducing the reconnect storm
- Image Compression Architecture
- Troubleshooting
- redact_image_base64
- layout.tsx
- savings.mdx
- docker-native-install.sh
- Service Management
- Configuration
- Manual Installation
- normalize_cloudcode_passthrough_path
- handle_model_metadata_endpoint
- request_limit_policy.py
- sse_byte_buffer_policy.py
- CompressionObserver
- PR-I6 — Make `make test-parity` a per-PR CI gate
- PR-I7 — Cache hot zone non-mutation tests
- PR-I9 — Continuous cache-hit-rate alarm
- PR-I10 — Replace fake RTK shim with real RTK in wrap E2E
- 4. Transforms (`transforms/`) - The Compression Magic
- The Data Flow (Step by Step)
- Shell Integration
- auth_mode.rs
- mod.rs
- TextCrusherConfig
- community-savings.mdx
- Platform Stabilization Matrix
- docs
- ._metadata_insert_params
- .__init__
- __init__.py
- is_known_websocket_callback_failure
- memory_injection_mode_policy.py
- test_pr_health_labels.py
- test_pr_health_workflow.py
- verify-versions.py
- The Core Components (In Simple Terms)
- Key Design Decisions
- .count_messages
- Configuration
- Manual Installation
- Differential Network Capture
- layout.tsx
- pipeline-extensions.mdx
- _find_available_port
- .default_path
- __init__.py
- build_rust_extension.sh
- The Smart Crusher Deep Dive
- Advanced Configuration
- ._compute_prefix_hash
- Shell Integration
- Uninstallation
- tokenizer.rs
- ResponseItem<'a>
- next.config.mjs
- .default_path
- ._count_tokens_estimate
- test_ci_workflow.py
- validate-workflows.sh
- .name
- README.md
- run-claude-lane.sh
- postcss.config.mjs
- source.config.ts
- __init__.py
- make_shim.sh script
- .provider
- ._count_tokens_estimate
- PR-I2 — SSE corner-case fixtures + fuzz tests
- __init__.py
- __init__.py
- __init__.py
- __init__.py
- install-git-hooks.sh
- refresh_model_limits.sh
- useMDXComponents
- diagnostic_decode_policy.py

## God Nodes (most connected - your core abstractions)
1. `ContentRouter` - 119 edges
2. `LocalBackend` - 92 edges
3. `start_proxy_with()` - 90 edges
4. `MemoryHandler` - 71 edges
5. `run()` - 68 edges
6. `SmartCrusher` - 68 edges
7. `MLModelRegistry` - 61 edges
8. `DeploymentManifest` - 59 edges
9. `LocalBackendConfig` - 56 edges
10. `CcrStore` - 55 edges

## Surprising Connections (you probably didn't know these)
- `boot_proxy()` --calls--> `ProxyConfig`  [INFERRED]
  scripts/replay_codex_ws_load.py → headroom/proxy/models.py
- `token_count_of()` --calls--> `get_tokenizer()`  [INFERRED]
  crates/headroom-core/tests/live_zone_token_validation.rs → crates/headroom-core/src/tokenizer/registry.rs
- `detect_id_field_statistically()` --calls--> `is_uuid_format()`  [INFERRED]
  crates/headroom-core/src/transforms/smart_crusher/field_detect.rs → crates/headroom-core/src/transforms/smart_crusher/statistics.rs
- `_expected_headroom_mcp_calls()` --calls--> `resolve_headroom_command()`  [EXTRACTED]
  e2e/init/run.py → headroom/install/runtime.py
- `wait_for_http()` --references--> `_Response`  [EXTRACTED]
  e2e/wrap/run.py → headroom/learn/verbosity.py

## Import Cycles
- 1-file cycle: `crates/headroom-proxy/src/observability/prometheus.rs -> crates/headroom-proxy/src/observability/prometheus.rs`
- 1-file cycle: `headroom/cli.py -> headroom/cli.py`
- 1-file cycle: `headroom/cli/__init__.py -> headroom/cli/__init__.py`
- 1-file cycle: `headroom/cli/__main__.py -> headroom/cli/__main__.py`
- 1-file cycle: `headroom/integrations/langchain/langsmith.py -> headroom/integrations/langchain/langsmith.py`
- 1-file cycle: `headroom/integrations/strands/hooks.py -> headroom/integrations/strands/hooks.py`
- 1-file cycle: `headroom/proxy/interceptors/__init__.py -> headroom/proxy/interceptors/__init__.py`

## Communities (674 total, 38 thin omitted)

### Community 0 - "__init__.py"
Cohesion: 0.05
Nodes (77): _apply_supersession_repair(), db_path_option(), _default_db_path(), delete_memories(), edit_memory(), _export_all(), export_memories(), get_scope_label() (+69 more)

### Community 1 - "LocalBackend"
Cohesion: 0.06
Nodes (33): Any, Connection, Entity, Path, Relationship, Subgraph, Convert Entity object to row dict for insertion., Convert database row to Entity object. (+25 more)

### Community 2 - "HeadroomProxy"
Cohesion: 0.02
Nodes (148): Seed the process env with the savings-profile defaults (default: coding).      C, seed_proxy_env_defaults(), get_dashboard_html(), get_settings_html(), Headroom Dashboard - Real-time proxy monitoring UI., Load the dashboard HTML template., Load the settings GUI HTML template., Memory tracking infrastructure for headroom.  This module provides centralized m (+140 more)

### Community 3 - "Provider"
Cohesion: 0.02
Nodes (98): Agno model wrapper for Headroom optimization.  This module provides HeadroomAgno, Lazily initialize TransformPipeline (thread-safe)., get_headroom_provider(), get_model_name_from_agno(), Any, Provider detection for Agno models.  Automatically detects the correct Headroom, Extract the model name/ID from an Agno model.      Args:         agno_model: An, Get the appropriate Headroom provider for an Agno model.      Detection strategy (+90 more)

### Community 4 - "__init__.py"
Cohesion: 0.03
Nodes (61): _init_cpu_embed_worker(), LocalEmbedder, _normalize_embedding(), _normalize_embeddings_batch(), OllamaEmbedder, OnnxLocalEmbedder, OpenAIEmbedder, Any (+53 more)

### Community 5 - "LocalBackendConfig"
Cohesion: 0.05
Nodes (51): ImportStats, MemoryBridge, _compute_file_hash(), detect_format(), extract_entities_from_text(), extract_relationships_from_section(), parse_chatgpt_facts(), parse_claude_code_memory() (+43 more)

### Community 6 - "helpers.py"
Cohesion: 0.02
Nodes (161): merge_anthropic_beta(), merge_beta_tokens(), merge_openai_beta(), Deterministic merge helpers for provider beta request headers., Merge client beta tokens with Headroom-required tokens deterministically., Merge client anthropic-beta value with Headroom-required tokens., Merge client OpenAI-Beta value with Headroom-required tokens., Split a comma-separated beta-header value into trimmed tokens. (+153 more)

### Community 7 - "server.py"
Cohesion: 0.17
Nodes (11): _bedrock_region_prefix(), _build_bedrock_fallback_map(), _fetch_bedrock_inference_profiles(), _normalize_bedrock_profile_id(), _parse_bedrock_model_overrides(), Return the inference-profile region prefix for an AWS region.      AWS Bedrock c, Build a static Bedrock model map using the region prefix.      When ``_fetch_bed, Fetch available Bedrock inference profiles from AWS API.      Uses boto3 list_in (+3 more)

### Community 8 - "openai.py"
Cohesion: 0.04
Nodes (92): Return an Anthropic model id without terminal styling artifacts., Strip model-id styling artifacts from Anthropic model metadata payloads., sanitize_anthropic_model_id(), sanitize_anthropic_model_metadata(), _allowed_ws_origins_from_env(), _append_unique_transforms(), _apply_stream_usage_option(), _codex_compression_debug_enabled() (+84 more)

### Community 9 - "MemoryBackend"
Cohesion: 0.02
Nodes (86): CacheEntry, CompressionCache, Event, PrefixFreezeConfig, Configuration for cache-aware prefix freezing., Manages PrefixCacheTracker instances across sessions.      Keyed by session ID (, Get existing tracker or create a new one for this session., Remove expired trackers periodically. (+78 more)

### Community 10 - "MemoryHandler"
Cohesion: 0.02
Nodes (94): Get accumulated content., BridgeConfig, MarkdownFormat, Enum, Configuration for the Memory Bridge.  The Memory Bridge provides bidirectional s, Supported markdown memory formats., Configuration for the Memory Bridge.      Attributes:         md_paths: List of, Validate configuration. (+86 more)

### Community 11 - "_Response"
Cohesion: 0.03
Nodes (116): proxy_pipeline_kwargs(), Build per-request pipeline kwargs from proxy config and savings profile.      Th, CCRToolInjector, Manages CCR tool injection into LLM requests.      This class handles:     1. De, Check if any compressed content was detected., Get list of detected compression hashes., build_copilot_upstream_url(), Build an upstream URL, normalizing GitHub Copilot's non-/v1 path layout. (+108 more)

### Community 12 - "__init__.py"
Cohesion: 0.03
Nodes (98): AIMessage, BaseChatModel, ChatGenerationChunk, ChatResult, Headroom integrations with popular LLM frameworks.  Available integrations:  Lan, get_tool_metrics(), Agent tool integration for LangChain with output compression.  This module provi, Get the global tool metrics collector. (+90 more)

### Community 13 - "pipeline.py"
Cohesion: 0.09
Nodes (12): GraphStore, Protocol for knowledge graph storage backends.      Implementations handle entit, Add an entity to the graph.          If an entity with the same ID exists, it wi, Add a relationship between two entities.          If a relationship with the sam, Retrieve an entity by ID.          Args:             entity_id: The unique ident, Retrieve an entity by name within a user's graph.          Args:             nam, Get relationships connected to an entity.          Args:             entity_id:, Extract a subgraph around the given entities.          Args:             entity_ (+4 more)

### Community 14 - "MLModelRegistry"
Cohesion: 0.03
Nodes (85): MLModelRegistry, Singleton registry for shared ML model instances.      Provides lazy-loaded, sha, Initialize the registry., Reset the registry (for testing)., BaseFeatureExtractor, ComplexityLevel, DomainType, EmbeddingExtractor (+77 more)

### Community 15 - "code_compressor.py"
Cohesion: 0.03
Nodes (91): Set up code-aware compression if enabled.          Args:             config: Pro, _check_tree_sitter_available(), CodeAwareCompressor, CodeCompressionResult, CodeLanguage, CodeStructure, coerce_language(), compress_code() (+83 more)

### Community 16 - "wrap.py"
Cohesion: 0.02
Nodes (139): apply_agent_savings_env_defaults(), Apply agent savings env defaults to a proxy subprocess environment.      When ``, _agent_savings_config_mismatches(), _apply_project_header_env(), _build_openclaw_unwrap_entry(), _check_proxy(), codex(), _codex_custom_provider_base_urls() (+131 more)

### Community 17 - "utils.py"
Cohesion: 0.04
Nodes (61): Comprehensive metrics for a single request., RequestMetrics, ABC, Any, datetime, Base storage interface for Headroom SDK., Get summary statistics.          Args:             start_time: Filter by timesta, Close storage connection if applicable. (+53 more)

### Community 18 - "ToolIntelligenceNetwork"
Cohesion: 0.03
Nodes (70): _build_parser(), _eligible_rows(), _format_row(), main(), publish(), Any, ArgumentParser, Path (+62 more)

### Community 19 - "TelemetryCollector"
Cohesion: 0.07
Nodes (25): FTS5SearchResult, FTS5TextIndex, Any, Connection, Memory, Path, Index a single memory for full-text search (low-level).          Args:, Index a single memory for full-text search.          Alias for index_raw for bac (+17 more)

### Community 20 - "HTMLExtractor"
Cohesion: 0.06
Nodes (38): compute_exact_match(), compute_f1(), evaluate_qa_accuracy_preservation(), evaluate_scrapinghub_benchmark(), ExtractionBenchmarkResult, HTMLExtractorBenchmarkSuite, Any, QAAccuracyResult (+30 more)

### Community 21 - "TrafficLearner"
Cohesion: 0.04
Nodes (71): AgentType, _bash_binaries_match(), _bash_first_binary(), _classify_error(), _commands_related_as_retry(), _drop_contradictions(), ExtractedPattern, _is_error() (+63 more)

### Community 22 - "kompress_compressor.py"
Cohesion: 0.04
Nodes (78): BoundedSemaphore, hf_hub_download_local_first(), Download a file from HuggingFace Hub, preferring the local cache.      Tries ``l, _acquire_bounded(), _acquire_execution_slot(), _acquire_timeout_seconds(), _add_kompress_must_keep_words(), _background_download() (+70 more)

### Community 23 - "binaries.py"
Cohesion: 0.04
Nodes (78): aider(), claude(), _client_marker_path(), cline(), _configure_tool_search_env(), cursor(), _emit_wrap_interrupted(), _ensure_proxy() (+70 more)

### Community 24 - "SmartCrusherConfig"
Cohesion: 0.07
Nodes (44): get_provider_config(), Get provider config, with fallback for unknown providers., dashboard(), _get_env_bool(), _get_env_bool_optional(), _get_env_int(), _get_env_int_optional(), proxy() (+36 more)

### Community 25 - "Any"
Cohesion: 0.05
Nodes (59): list_available_datasets(), load_dataset_by_name(), load_tool_output_samples(), Any, List all available datasets by category.      Returns:         Dictionary mappin, Load a dataset by name from the registry.      Args:         name: Dataset name, Load built-in tool output samples for testing.      These are realistic tool out, cmd_benchmark() (+51 more)

### Community 26 - "install_registry.py"
Cohesion: 0.06
Nodes (57): append_text(), PathLike, Encoding- and newline-safe text file I/O.  ``Path.read_text()`` / ``Path.write_t, Read text, preferring UTF-8 and falling back to the locale encoding.      Decodi, Write text as UTF-8 without translating line endings.      ``newline=""`` disabl, Append text as UTF-8 without translating line endings (see ``write_text``)., read_text(), write_text() (+49 more)

### Community 27 - "ContentRouter"
Cohesion: 0.03
Nodes (91): PayloadSpec, One adversarial payload with its class label., Initialize evaluator.          Args:             provider: LLM provider ("anthro, CodeCompressorConfig, Configuration for code-aware compression.      Attributes:         preserve_impo, _compress_live_text_with_markers(), _compress_marker_free_text(), compress_unit_with_router() (+83 more)

### Community 28 - "config.py"
Cohesion: 0.06
Nodes (29): HeadroomClient, Any, datetime, Tokenizer, Update in-memory session statistics., Create a message with optional Headroom optimization.          Args:, Stream a message with optional Headroom optimization.          Args:, Context Budget Controller wrapper for LLM API clients.      Provides automatic c (+21 more)

### Community 29 - "OpenAIProvider"
Cohesion: 0.05
Nodes (46): __getattr__(), Any, Strands Agents integration for Headroom SDK.  This module provides seamless inte, Check if strands-agents is installed and available.      Returns:         True i, Lazy import of integration components., strands_available(), _check_strands_available(), HeadroomStrandsModel (+38 more)

### Community 30 - "crusher.rs"
Cohesion: 0.11
Nodes (40): ccr_hash_changes_with_input(), ccr_hash_is_deterministic(), compaction_kind_str(), compaction_skips_non_object_array(), crush_array_keeps_error_items(), crush_array_low_uniqueness_compresses(), crush_array_passthrough_when_below_adaptive_k(), crush_array_skip_path_returns_original_items() (+32 more)

### Community 31 - "content_router.py"
Cohesion: 0.19
Nodes (15): dedup_blocks(), _index_lines(), is_prefix_monotonic(), _is_trivial(), _longest_match(), _num_and_key(), _pointer(), Cross-turn (whole-conversation) verbatim de-duplication.  Bash coding agents re- (+7 more)

### Community 32 - "claude"
Cohesion: 0.11
Nodes (21): _coerce_float(), _coerce_int(), _dict_or_empty(), _empty_state(), _label(), _model_entry(), PersistentMetricsState, Any (+13 more)

### Community 33 - "SessionData"
Cohesion: 0.09
Nodes (41): ConversationScanner, ABC, Base class for headroom learn plugins.  Each coding agent (Claude Code, Codex, G, Base class for scanning conversation logs from any agent system.      Subclasses, Discover all projects with conversation data., Scan all sessions for a project, returning normalized tool calls., ErrorCategory, ProjectInfo (+33 more)

### Community 34 - "MemoryBridge"
Cohesion: 0.09
Nodes (26): _check_langchain_available(), compress_tool_messages(), CompressToolMessagesConfig, CompressToolMessagesResult, create_compress_tool_messages_node(), _CrusherSingleton, _estimate_tokens(), _get_crusher() (+18 more)

### Community 35 - "run.py"
Cohesion: 0.06
Nodes (71): bare_init_g_cases(), existing_sequence_cases(), _expect_codex_hooks_feature(), _expect_hook_command(), _expected_headroom_mcp_calls(), main(), per_subcommand_cases(), Path (+63 more)

### Community 36 - "LiteLLMBackend"
Cohesion: 0.10
Nodes (22): any-llm backend for Headroom.  Talk to 38+ LLM providers (OpenAI, Mistral, Groq,, Backend, BackendResponse, ABC, Any, Base backend interface for Headroom.  Backends translate between the canonical A, Check if this backend supports a model.          Args:             model: Model, Send an OpenAI-format message request.          Unlike send_message(), this take (+14 more)

### Community 37 - "BodyMutationTracker"
Cohesion: 0.03
Nodes (46): BetaHeaderStickyMode, Policy helpers for beta-header stickiness configuration., Resolve beta-header stickiness mode from an environment value., Resolve the positive LRU session bound for beta-header tracking., resolve_beta_header_sticky_mode(), resolve_beta_tracker_max_sessions(), BodyMutationTracker, Records whether a request body was mutated and why. (+38 more)

### Community 38 - "DeploymentManifest"
Cohesion: 0.07
Nodes (64): _ensure_profile_running(), _ensure_runtime_manifest(), _activate_deployment_mutations(), _deactivate_deployment_mutations(), install(), install_agent(), install_agent_ensure(), install_agent_run() (+56 more)

### Community 39 - "doctor.py"
Cohesion: 0.05
Nodes (72): Command, check_budget(), check_claude_remote_control_gate(), check_claude_routing(), check_codex_routing(), check_deployments(), check_proxy_liveness(), check_savings() (+64 more)

### Community 40 - "update.py"
Cohesion: 0.08
Nodes (16): LRUMemoryCache, Memory, Put a memory in the cache.          If the memory already exists, updates the va, Put multiple memories in the cache.          Args:             memories: List of, Invalidate (remove) a memory from cache.          Args:             memory_id: T, Invalidate multiple memories from cache.          Args:             memory_ids:, Thread-safe LRU (Least Recently Used) cache for Memory objects.      Implements, Invalidate all cached memories at or below a scope.          Args:             u (+8 more)

### Community 41 - "PipelineExtensionManager"
Cohesion: 0.06
Nodes (45): compress(), compress_spreadsheet(), CompressConfig, CompressResult, _get_pipeline(), Any, One-function compression API for Headroom.  The simplest way to use Headroom — n, Result of compressing messages.      Attributes:         messages: The compresse (+37 more)

### Community 42 - "anthropic.py"
Cohesion: 0.03
Nodes (77): CallModel, extract_system_prompt(), Any, Best-effort extraction of the system prompt across providers.      Anthropic put, _anthropic_outcome_provider(), AnthropicHandlerMixin, _header_get(), _normalize_http_origin() (+69 more)

### Community 43 - "anchor_selector.rs"
Cohesion: 0.07
Nodes (42): adjust_weights_both_keywords_no_change(), adjust_weights_historical_shifts_to_front(), adjust_weights_no_query_no_change(), adjust_weights_recency_shifts_to_back(), AnchorConfig, AnchorSelector, AnchorStrategy, AnchorWeights (+34 more)

### Community 44 - "prometheus.rs"
Cohesion: 0.19
Nodes (21): extract_rate_limit_snapshot(), extract_rate_limit_snapshot_anthropic(), extract_rate_limit_snapshot_no_headers(), extract_rate_limit_snapshot_openai(), extract_rate_limit_snapshot_unparseable_value_is_none(), passthrough_bytes_modified_counter(), rate_limit_remaining_input_tokens_gauge(), rate_limit_remaining_output_tokens_gauge() (+13 more)

### Community 45 - "sync.py"
Cohesion: 0.09
Nodes (31): CodexAdapter, Path, Codex CLI memory sync adapter.  Syncs memories to/from a headroom-managed sectio, Hash of AGENTS.md contents., Sync adapter for Codex's AGENTS.md., Read memories from the headroom section of AGENTS.md., AgentMemory, AgentMemoryAdapter (+23 more)

### Community 46 - "Any"
Cohesion: 0.05
Nodes (34): CachedContentInfo, GoogleCacheOptimizer, Any, datetime, Check if cache has expired., Seconds remaining until expiry., Age of the cache in seconds., Serialize to dictionary. (+26 more)

### Community 47 - "BaseCacheOptimizer"
Cohesion: 0.07
Nodes (52): BreakpointPlan, ContentSection, Anthropic Cache Optimizer.  Implements cache optimization for Anthropic's explic, Plan where to place cache breakpoints., Represents a section of content that may be cacheable., Plan for where to insert cache breakpoints., BaseCacheOptimizer, BreakpointLocation (+44 more)

### Community 48 - "suite_runner.py"
Cohesion: 0.11
Nodes (24): codex_backend_url(), codex_backend_ws_url(), ChatGPT Codex backend endpoint formulas., Return a ChatGPT HTTPS backend URL under `/backend-api/codex`., Return a ChatGPT WebSocket backend URL under `/backend-api/codex`., codex_responses_http_url(), codex_responses_subpath_url(), codex_responses_websocket_url() (+16 more)

### Community 49 - "batch_compression_eval.py"
Cohesion: 0.04
Nodes (80): BatchCompressionEvaluator, BatchEvalResult, BatchEvalSuiteResult, BatchRequest, BatchTestCase, evaluate_token_counting_accuracy(), generate_code_understanding_test_cases(), generate_factual_test_cases() (+72 more)

### Community 50 - "__init__.py"
Cohesion: 0.03
Nodes (102): adversarial(), evals(), memory_eval(), memory_eval_compat(), memory_eval_v2(), memory_eval_v2_compat(), _parse_categories(), probes() (+94 more)

### Community 51 - "diff_compressor.rs"
Cohesion: 0.09
Nodes (59): binary_files_simplification_is_recorded(), binary_regex(), bugfix_combined_diff_3way_content_is_parsed_and_emitted(), bugfix_no_newline_marker_preserved_despite_distance(), bugfix_pre_diff_content_is_preserved(), bugfix_rename_markers_are_preserved_in_output(), build_n_hunk_diff(), build_synthetic_diff() (+51 more)

### Community 52 - "init.py"
Cohesion: 0.06
Nodes (70): _claude_scope_path(), _codex_dotted_feature_block(), _codex_feature_block(), _codex_features(), _codex_features_has_hooks(), _codex_features_table_index(), _codex_hooks_path(), _codex_scope_path() (+62 more)

### Community 53 - "compression_store.py"
Cohesion: 0.05
Nodes (32): DatabaseError, Base protocol for CompressionStore backends.  This protocol defines the minimal, Storage backends for CompressionStore.  This module provides pluggable storage b, InMemoryBackend, Any, In-memory storage backend for CompressionStore.  This is the default backend, pr, Get all hash keys in storage.          Returns:             List of all hash key, Get all entries as (hash_key, entry) pairs.          Returns:             List o (+24 more)

### Community 54 - "__init__.py"
Cohesion: 0.06
Nodes (48): Reset the global batch context store (for testing)., reset_batch_context_store(), CCR (Compress-Cache-Retrieve) module for reversible compression.  This module pr, CCRResponseHandler, CCRToolResult, Any, Response handling for CCR (Compress-Cache-Retrieve).  This module provides respo, Check if response contains CCR tool calls.          Args:             response: (+40 more)

### Community 55 - "__init__.py"
Cohesion: 0.05
Nodes (44): AnchorConfig, Configuration for dynamic anchor allocation in SmartCrusher.      Anchor selecti, AnchorSelector, AnchorStrategy, AnchorWeights, calculate_information_score(), _calculate_length_score(), _calculate_structural_uniqueness() (+36 more)

### Community 56 - "SmartCrusher"
Cohesion: 0.06
Nodes (31): SmartCrusherConfig, Initialize evaluator.          Args:             llm_fn: Function that takes (co, is_ccr_sentinel(), Any, Pattern, Walk `rendered` for any `<<ccr:HASH ...>>` markers and mirror         each into, Find every distinct `<<ccr:HASH...>>` hash in `rendered` and         mirror Rust, Recursively walk a parsed-JSON value, appending every CCR         hash found ins (+23 more)

### Community 57 - "paths.py"
Cohesion: 0.06
Nodes (63): beacon_lock_path(), bin_dir(), bridge_state_path(), codex_wire_debug_dir(), config_dir(), debug_400_dir(), deploy_root(), ensure_config_dir() (+55 more)

### Community 58 - "ContentType"
Cohesion: 0.10
Nodes (19): BaseTool, _check_langchain_available(), HeadroomToolWrapper, Any, Get per-tool statistics., Wraps a LangChain tool to compress its output.      Applies SmartCrusher compres, Initialize HeadroomToolWrapper.          Args:             tool: The LangChain B, Invoke the tool and compress output.          Args:             *args: Arguments (+11 more)

### Community 59 - "LocalToolPattern"
Cohesion: 0.03
Nodes (61): CompressionFeedback, CompressionHints, get_compression_feedback(), LocalToolPattern, Any, Compression Feedback Loop for learning optimal compression strategies.  This mod, Find the strategy with lowest retrieval rate (most successful)., Record strategy compression outcome. (+53 more)

### Community 60 - "StreamingMixin"
Cohesion: 0.09
Nodes (21): Any, StreamingResponse, Actual streaming implementation, guarded by _stream_response's cleanup wrapper., Clear active mid-turn state, optionally returning queued messages., Extract observed Anthropic cache-write TTL bucket usage., Parse usage information from SSE chunk.          For Anthropic: Looks for messag, Stream response from Bedrock backend with metrics tracking.          Translates, Stream OpenAI chat completion response from backend.          Routes stream:true (+13 more)

### Community 61 - "formatter.rs"
Cohesion: 0.13
Nodes (44): cell_to_json(), cfg(), compaction_to_json(), csv_formatter_drop_summary_opt_in(), csv_formatter_emits_ccr_marker(), csv_formatter_escapes_internal_quotes(), csv_formatter_nested_cell_inline_json(), csv_formatter_pure_tabular() (+36 more)

### Community 62 - "dynamic_detector.py"
Cohesion: 0.05
Nodes (42): calculate_entropy(), detect_dynamic_content(), DetectionResult, DetectorConfig, DynamicCategory, DynamicContentDetector, DynamicSpan, NERDetector (+34 more)

### Community 63 - "GoogleCacheOptimizer"
Cohesion: 0.10
Nodes (21): _build_frontmatter(), ClaudeCodeAdapter, encode_claude_project_path(), get_claude_memory_dir(), _parse_frontmatter(), Any, Path, Claude Code memory sync adapter.  Reads/writes Claude Code's native memory forma (+13 more)

### Community 64 - "ImageCompressor"
Cohesion: 0.08
Nodes (27): compress_images(), CompressionResult, get_compressor(), ImageCompressor, Any, Image Compressor - Seamless image token optimization.  This is the main entry po, Result of image compression., Seamless image compression for LLM requests.      Automatically detects images, (+19 more)

### Community 65 - "MemoryToolAdapter"
Cohesion: 0.06
Nodes (32): MemoryToolAdapter, Any, Handle STR_REPLACE command - update memory content., Handle DELETE command - remove from vector store., Perform semantic search and format results., Get memory overview with search instructions., Execute a custom memory tool., Execute memory_save tool. (+24 more)

### Community 66 - "run"
Cohesion: 0.06
Nodes (41): _candidate_secret_tool_commands(), Linux secret-service lookup helpers for GitHub Copilot CLI auth., Return a Copilot CLI OAuth token from Linux Secret Service, if available., _read_copilot_config_login(), read_copilot_oauth_token(), _run_secret_tool_lookup(), BenchmarkResult, BenchmarkSuiteResult (+33 more)

### Community 67 - "paths.py"
Cohesion: 0.05
Nodes (54): ChatCompletions, Messages, Main HeadroomClient implementation for Headroom SDK., Simulate optimization without calling the API.          Args:             model:, Wrapper for messages API (Anthropic-style)., Simulate optimization without calling the API.          Args:             model:, Wrapper for chat.completions API (OpenAI-style)., CacheOptimizerConfig (+46 more)

### Community 68 - "statistics.rs"
Cohesion: 0.06
Nodes (9): calculate_string_entropy(), detect_sequential_pattern(), entropy_high_for_random_looking_string(), entropy_mostly_repeated_low(), entropy_perfectly_uniform_normalized_to_one(), is_uuid_format(), python_int_parse(), Option (+1 more)

### Community 69 - "HeadroomAgnoModel"
Cohesion: 0.05
Nodes (34): _check_agno_available(), HeadroomAgnoModel, OptimizationMetrics, optimize_messages(), Any, Model, Initialize HeadroomAgnoModel after dataclass construction., Forward capability attributes from wrapped model.          This ensures that fra (+26 more)

### Community 70 - "analyzer.rs"
Cohesion: 0.11
Nodes (45): analyze_field_all_null_yields_null_type_constant(), analyze_field_constant_detected(), analyze_field_numeric_basic_stats(), analyze_field_numeric_filters_nan_and_inf(), analyze_field_numeric_overflow_resets_all_stats_to_none(), analyze_field_string_avg_length_and_top_values(), analyzer(), change_points_constant_values_empty() (+37 more)

### Community 71 - "lib.rs"
Cohesion: 0.07
Nodes (38): main(), Result, Cli, Cmd, first_line(), main(), Option, PathBuf (+30 more)

### Community 72 - "BatchResultProcessor"
Cohesion: 0.05
Nodes (49): APIClient, BatchResultProcessor, BatchResultProcessorConfig, process_batch_results(), ProcessedBatchResult, Any, AsyncClient, Protocol (+41 more)

### Community 73 - "orchestrator.rs"
Cohesion: 0.15
Nodes (38): AlwaysInternalError, builder_dispatches_by_applies_to(), builder_preserves_registration_order_for_offloads(), CompressionPipeline, CompressionPipelineBuilder, ctx(), empty_input_returns_empty_output(), empty_pipeline_passes_input_through() (+30 more)

### Community 74 - "HeadroomMCPServer"
Cohesion: 0.06
Nodes (36): format_retrieval_miss_detail(), Return an operator-facing miss reason for CCR retrieval failures., _append_shared_event(), _build_proxy_unreachable_payload(), create_ccr_mcp_server(), _format_session_summary(), HeadroomMCPServer, main() (+28 more)

### Community 75 - "output_shaper.py"
Cohesion: 0.04
Nodes (94): Apply OpenAI Responses output shaping and attach holdout labels., Output shaping for a Responses payload (opt-in, HEADROOM_OUTPUT_SHAPER).      Th, _shape_openai_responses_for_output(), _shape_openai_responses_payload(), can_create_openai_text_verbosity(), clamp_legacy_thinking_budget(), lower_effort_value(), lower_text_verbosity_value() (+86 more)

### Community 76 - "tag_protector.rs"
Cohesion: 0.08
Nodes (51): attribute_with_gt_inside_quotes(), compress_tagged_content_true_emits_marker_placeholders(), count_close_tags(), count_open_tags(), custom_tag_replaced_with_placeholder(), custom_tag_with_attributes(), emit_output(), empty_input_returns_empty() (+43 more)

### Community 77 - "LearnPlugin"
Cohesion: 0.05
Nodes (43): CompletionItem, _activate_output_shaper(), _AgentChoice, learn(), _make_llm_judge(), Any, Context, Path (+35 more)

### Community 78 - "planning.rs"
Cohesion: 0.15
Nodes (27): default_oss_constraints(), Box, hash_field_name(), String, cluster_sample_assigns_cluster_field(), create_plan_routes_smart_sample_to_smart_sample(), create_plan_skip_returns_all_indices(), fixture() (+19 more)

### Community 79 - "parse_commits"
Cohesion: 0.07
Nodes (24): NamedTuple, generate_changelog(), get_merge_summary(), iter_commit_entries(), main(), parse_commits(), ParsedCommit, Path (+16 more)

### Community 80 - "analyzer.py"
Cohesion: 0.06
Nodes (55): _build_digest(), _build_prior_patterns_section(), FailureAnalyzer, _format_event(), _format_tool_call(), _parse_llm_response(), Recommendation, Session analysis via LLM — replaces all regex/heuristic analysis.  Pipeline: Sca (+47 more)

### Community 81 - "__init__.py"
Cohesion: 0.08
Nodes (32): Operational observability helpers for Headroom., configure_otel_metrics(), get_otel_metrics(), get_otel_metrics_status(), _headroom_version(), HeadroomOtelMetrics, OTelMetricsConfig, _parse_bool() (+24 more)

### Community 82 - "__init__.py"
Cohesion: 0.09
Nodes (29): audit_codex(), classify_command(), CodexAuditReport, _output_text(), Path, Codex transcript audit — read-pattern analysis for shell-based clients.  Codex h, Audit all Codex ``*.jsonl`` transcripts under ``root``., Human-readable Codex audit summary. (+21 more)

### Community 83 - "release_version.py"
Cohesion: 0.04
Nodes (39): Any, Record a compression event.          Args:             items: Sample items from, Record a retrieval event.          This is called when an LLM retrieves compress, Get overall telemetry statistics.          Returns:             Dictionary with, Get statistics for a specific tool signature.          Args:             signatu, Get statistics for all tracked tool signatures.          Returns:             Di, Get learned recommendations for a tool signature.          Args:             sig, Export all telemetry data for aggregation.          This is the data that can be (+31 more)

### Community 84 - "HNSWVectorIndex"
Cohesion: 0.05
Nodes (38): _check_hnswlib_available(), HNSWVectorIndex, IndexedMemoryMetadata, Any, Memory, ndarray, Path, Update the ef_search parameter for query time.          Higher values give bette (+30 more)

### Community 85 - "DirectMem0Adapter"
Cohesion: 0.06
Nodes (30): DirectMem0Adapter, Any, datetime, Memory, Adapter that bypasses Mem0's LLM extraction for pre-extracted data.      This ad, Initialize the Direct Mem0 adapter.          Args:             config: Configura, Ensure all clients are initialized., Public initialization hook for callers that need readiness guarantees. (+22 more)

### Community 86 - "project_context.py"
Cohesion: 0.10
Nodes (26): drop_header(), header_name(), Case-insensitive header helpers for Codex provider adapters., Remove the header matching ``name`` case-insensitively from ``headers``., Return the existing header key matching ``name`` case-insensitively., codex_image_forward_error_response(), codex_image_url(), CodexImageForwardHttpClient (+18 more)

### Community 87 - "run.py"
Cohesion: 0.12
Nodes (42): BaseHTTPRequestHandler, assert_true(), create_shims(), log(), main(), MockOpenAIHandler, MockOpenAIServer, prepare_local_openclaw_plugin() (+34 more)

### Community 88 - "writer.py"
Cohesion: 0.08
Nodes (43): _build_windows_handoff_argv(), detect_install_method(), _find_core_pyd(), _format_cmd(), _in_docker(), _in_virtualenv(), InstallMethod, _is_editable_install() (+35 more)

### Community 89 - "model_metadata.py"
Cohesion: 0.09
Nodes (44): chatgpt_backend_url(), Return a ChatGPT HTTPS backend URL for an absolute backend path., codex_client_version(), codex_model_registry_entry(), CodexModelRegistryHttpClient, CodexModelRegistryOptions, CodexModelRegistryResponse, display_name_from_model_id() (+36 more)

### Community 90 - "CLI Reference"
Cohesion: 0.04
Nodes (49): Captured `--help` output, CLI Reference, Command index, Docker-native parity matrix, Entry points, Global behavior, Global options, `headroom evals` (+41 more)

### Community 91 - "EstimatingTokenCounter"
Cohesion: 0.07
Nodes (24): Initialize LiteLLM token counter.          Args:             model: Model name i, EstimatingTokenCounter, Token counter using estimation heuristics.      This is the fallback tokenizer u, Initialize estimating counter.          Args:             chars_per_token: Overr, TokenCounter, Initialize default tokenizer factories., Get tokenizer for a model.          Args:             model: Model name (e.g., ', Register a tokenizer or factory for a model.          Args:             model: M (+16 more)

### Community 92 - "SearchCompressor"
Cohesion: 0.10
Nodes (17): _cjk_bigrams(), FileMatches, _is_cjk_char(), Rust-backed search-results compressor.  Phase 3e.2 ported the implementation to, Result of search result compression., Estimate tokens saved (rough: 1 token per 4 chars)., Compresses grep/ripgrep search results via the Rust port.      Drop-in replaceme, Parse via the Rust parser, build legacy Python dataclasses. (+9 more)

### Community 93 - "adaptive_sizer.rs"
Cohesion: 0.06
Nodes (16): compute_optimal_k(), compute_optimal_k_bias_keeps_more(), compute_optimal_k_respects_max_k(), compute_optimal_k_respects_min_k(), compute_unique_bigram_curve(), count_unique_simhash(), find_knee(), hamming_distance() (+8 more)

### Community 94 - "traits.rs"
Cohesion: 0.09
Nodes (26): AlwaysHalf, Result, TransformError, compression_context_constructors(), CompressionContext, offload_estimate_bloat_is_safe_on_empty_input(), offload_output_clamps_negative_savings_to_zero(), offload_trait_writes_to_store_and_returns_required_cache_key() (+18 more)

### Community 95 - "wrap.py"
Cohesion: 0.05
Nodes (70): _append_text(), _check_and_clear_stale_wrap_marker(), _claude_wrap_base_url_env_key(), _clear_wrap_marker(), _codex_config_has_headroom_markers(), _codex_config_paths(), _codex_home_dir(), _codex_session_home_overlay() (+62 more)

### Community 96 - "SQLiteMemoryStore"
Cohesion: 0.06
Nodes (33): Any, Connection, datetime, Memory, ndarray, Path, Serialize numpy array to bytes for BLOB storage., Deserialize bytes back to numpy array. (+25 more)

### Community 97 - "forwarded_headers.py"
Cohesion: 0.04
Nodes (69): Address, _emit_rejection_event(), _header_first(), load_trusted_dashboard_client_cidrs(), load_trusted_gateway_cidrs(), _normalize_ip(), _parse_cidr_list(), _peer_host() (+61 more)

### Community 98 - "invoke_streaming.rs"
Cohesion: 0.08
Nodes (42): build_bedrock_streaming_upstream(), build_streaming_upstream_supports_converse_stream_action(), build_streaming_upstream_uses_region_default(), collect_signed_headers(), error_response(), error_sse_frame(), error_sse_frame_shape(), extract_streaming_action() (+34 more)

### Community 99 - "drift_detector.rs"
Cohesion: 0.13
Nodes (41): anthropic_body(), ApiKind, compute_structural_hash(), derive_session_key(), does_not_mutate_input(), drift_dims(), DriftState, early_messages_drift_detected_with_correct_dim() (+33 more)

### Community 100 - "proxy.rs"
Cohesion: 0.08
Nodes (38): ProxyError, Error, IntoResponse, String, body_to_bytes(), build_app(), build_upstream_url(), catch_all() (+30 more)

### Community 101 - "PrefixCacheTracker"
Cohesion: 0.06
Nodes (30): CacheMissAttribution, _canonicalize_for_prefix_compare(), extract_cache_stable_delta(), FreezeStats, normalize_message_cache_control(), overlay_cached_prefix(), PrefixCacheTracker, Any (+22 more)

### Community 102 - "lib.rs"
Cohesion: 0.07
Nodes (21): compress_openai_responses_live_zone(), content_has_error_indicators(), ctx_from_str(), detect_log_format(), is_json_array_of_dicts(), known_html_tag_names(), parse_search_lines(), protect_tags() (+13 more)

### Community 103 - "Any"
Cohesion: 0.07
Nodes (48): _apply_rtk_to_systemmessage_field(), _disable_serena_mcp(), _disable_tokensave_mcp(), _find_persistent_manifest(), _index_tokensave_project(), _live_wrap_module(), _proxy_active_session_count(), _proxy_health_config() (+40 more)

### Community 104 - "WebSocketSessionRegistry"
Cohesion: 0.07
Nodes (25): _age_for_named_task(), collect_tasks(), _coro_qualname(), Any, Pure serializers for the loopback-only /debug/* introspection endpoints.  Unit 5, Enumerate ``asyncio.all_tasks()`` for /debug/tasks.      Each entry carries: ``n, Return the coroutine qualname for ``task`` without touching locals.      The qua, Return a short stack-depth summary for ``task``.      Uses :meth:`asyncio.Task.g (+17 more)

### Community 105 - "CcrStore"
Cohesion: 0.14
Nodes (40): CcrStore, Send, Sync, bucket_by(), build_homogeneous_table(), build_row(), cell_from_value(), cfg() (+32 more)

### Community 106 - "volatile_detector.rs"
Cohesion: 0.08
Nodes (46): ApiKind, apikind_anthropic_scans_correct_paths(), caps_findings_at_ten(), detect_volatile_content(), detects_iso8601_timestamp_in_system_prompt(), detects_request_id_field_in_nested_object(), detects_uuid_v4_in_user_message(), does_not_mutate_input() (+38 more)

### Community 107 - "CompressionStore"
Cohesion: 0.05
Nodes (52): ContentType, _decode_concatenated_json(), detect_content_type(), DetectionResult, is_json_array_of_dicts(), _is_md_separator(), _looks_like_prose(), _md_cell_count() (+44 more)

### Community 108 - "content_detector.rs"
Cohesion: 0.10
Nodes (34): build_output_detected(), CodePatterns, ContentType, detect_content_type(), DetectionResult, diff_low_confidence_does_not_short_circuit(), empty_json_array_not_dict_array(), empty_returns_plain_text_zero_confidence() (+26 more)

### Community 109 - ".path"
Cohesion: 0.09
Nodes (33): empty_recommendation_array_is_valid(), loads_valid_toml(), malformed_toml_logs_and_yields_empty(), missing_file_yields_empty_recommendations(), Drop, Path, PathBuf, TempDir (+25 more)

### Community 110 - "analyzer.py"
Cohesion: 0.08
Nodes (41): perf(), Performance analysis CLI command., Analyze proxy performance from logs.      \b     Reads logs from ~/.headroom/log, build_perf_summary(), calculate_throughput(), _calculate_throughput_stats(), _cli_filtering_report_lines(), _context_tool_lifetime_savings() (+33 more)

### Community 111 - "proxy_routes.py"
Cohesion: 0.10
Nodes (38): model_metadata_get_endpoint(), Return the single-model metadata endpoint for ``model_id``., OpenAIResponsesSubpathRoute, Responses API subpath alias exposed by provider route registration., Any, FastAPI, Register provider-specific proxy endpoints., _register_openai_image_route() (+30 more)

### Community 112 - "live_zone.rs"
Cohesion: 0.11
Nodes (42): assistant_message_not_in_live_zone(), auth_mode_does_not_affect_b3_outcome_for_short_input(), AuthMode, body(), compress_anthropic_live_zone(), compress_openai_chat_live_zone(), compress_openai_responses_live_zone(), compresses_multiple_same_frame_outputs() (+34 more)

### Community 113 - "universal.py"
Cohesion: 0.07
Nodes (34): ContentType, DetectionResult, FallbackDetector, get_detector(), MagikaDetector, Enum, ML-based content type detection using Google's Magika.  Magika is a deep learnin, ML-based content type detector using Google's Magika.      This detector uses a (+26 more)

### Community 114 - "Memory"
Cohesion: 0.05
Nodes (42): Advanced Usage: Direct HierarchicalMemory API, Agent Provenance, Architecture, Best Practices, Comparison with State of the Art, Components, Configuration, Cross-Agent Memory (Proxy) (+34 more)

### Community 115 - "SmartCrusherBuilder"
Cohesion: 0.14
Nodes (20): add_constraint_preserves_order(), add_default_oss_constraints_appends_two(), builder_observer_fires_on_crush(), empty_builder_builds_with_default_scorer(), MarkerConstraint, AnchorConfig, Arc, Box (+12 more)

### Community 116 - ".plan_smart_sample"
Cohesion: 0.14
Nodes (28): for_each_anomaly(), item_has_preserve_field_match(), map_to_anchor_pattern(), query_or_none(), BTreeSet, CompressionStrategy, Option, String (+20 more)

### Community 117 - "SubscriptionTracker"
Cohesion: 0.07
Nodes (19): Any, timedelta, Background tracker for Anthropic Claude Code subscription windows.      Implemen, Returns ``True`` when subscription tracking is enabled in config., Return current tracker state dict for ``/stats``., Start the background polling loop., Stop the background polling loop and persist current state., Called by the proxy handler when an OAuth request comes through.          Stores (+11 more)

### Community 118 - "diff_noise.rs"
Cohesion: 0.13
Nodes (31): DiffNoiseConfig, String, Vec, apply_drops_lockfile_and_stores_original(), apply_drops_whitespace_only_hunk(), apply_skipped_when_no_droppable_hunks(), build_diff(), cfg() (+23 more)

### Community 119 - "walker.rs"
Cohesion: 0.13
Nodes (30): array_of_scalars_left_alone(), cascading_recursion_outer_table_sees_inner_compacted_string(), compact_document(), dc(), deeply_nested_arrays_compact_at_every_level(), DocumentCompactor, emit_opaque_ccr_marker(), humanize() (+22 more)

### Community 120 - "openclaw"
Cohesion: 0.17
Nodes (15): _build_openclaw_plugin_entry(), _normalize_openclaw_gateway_provider_ids(), Normalize configured OpenClaw provider ids, defaulting to openai-codex., Merge managed Headroom plugin settings with any existing entry payload., OpenClaw-specific provider helpers., build_plugin_entry(), build_unwrap_entry(), decode_entry_json() (+7 more)

### Community 121 - "HeadroomConfig"
Cohesion: 0.04
Nodes (71): CCRConfig, Configuration for Compress-Cache-Retrieve architecture.      CCR makes compressi, Output of a transform operation., Counted summary of transforms_applied (e.g. {'router:tool_result:text': 4})., TransformResult, apply_to_messages(), _build_tool_use_index(), InterceptionResult (+63 more)

### Community 122 - "PromptComparisonResult"
Cohesion: 0.08
Nodes (28): batch_compare_prompts(), compare_messages(), compare_prompts(), _parse_judge_response(), PromptComparer, PromptComparisonResult, Any, Path (+20 more)

### Community 123 - ".get"
Cohesion: 0.06
Nodes (25): get_sentence_transformer(), get_siglip(), get_spacy(), Any, Centralized registry for ML model instances.  Provides shared access to ML model, Unload one cached model entry., Unload several cached model entries with one runtime cleanup pass., Unload every cached model entry matching a prefix. (+17 more)

### Community 124 - "_headroom_bypass_enabled"
Cohesion: 0.14
Nodes (14): MemoryDecision, apply_memory_skip_reason(), decide_memory_injection(), MemoryInjectionDecision, Any, Pure memory-injection decision policy helpers., Raw memory-injection decision before wrapping in public value types., Compute the canonical memory-injection decision. (+6 more)

### Community 125 - "PrometheusMetrics"
Cohesion: 0.04
Nodes (34): RTK invocation metrics for the wrap CLI.  Phase G PR-G3 remediation (C4): RTK li, Record one (or `delta`) RTK invocation(s) for the given tool.      `tool` is the, Return a snapshot of the current invocation counts.      Returns a plain dict (n, Reset the counter map. Test-only — never called from production., record_rtk_invocation(), reset_rtk_invocations(), rtk_invocation_counts(), _append_metric() (+26 more)

### Community 126 - "handle_invoke"
Cohesion: 0.10
Nodes (30): build_bedrock_upstream(), build_upstream_honors_explicit_endpoint(), build_upstream_routes_converse_to_converse_endpoint(), build_upstream_uses_region_default(), collect_signed_headers(), collect_signed_headers_strips_client_managed(), error_response(), extract_invoke_action() (+22 more)

### Community 127 - "api-reference.mdx"
Cohesion: 0.05
Nodes (30): AnthropicProvider, BM25Scorer, CacheAligner, CacheAlignerConfig, compress() (TypeScript), CompressResult (TypeScript), Configuration, Context management (+22 more)

### Community 128 - "code_handler.py"
Cohesion: 0.08
Nodes (30): HandlerResult, Result from a structure handler.      Contains the mask plus metadata about what, Fraction of content marked for preservation., _check_tree_sitter(), CodeSpan, CodeStructureHandler, _get_parser(), is_tree_sitter_available() (+22 more)

### Community 129 - "registry.py"
Cohesion: 0.08
Nodes (29): _family_fallback(), get_model_info(), _infer_provider(), list_models(), ModelInfo, ModelRegistry, Any, Model registry with capabilities database.  Centralized database of LLM models w (+21 more)

### Community 130 - "ImportanceSignal"
Cohesion: 0.10
Nodes (22): ImportanceContext, ImportanceSignal, LineImportanceDetector, Option, Self, Send, Sync, AlwaysFiresHigh (+14 more)

### Community 131 - "codex_rate_limits.py"
Cohesion: 0.06
Nodes (41): Initialize async resources., get_quota_registry(), QuotaTrackerRegistry, Base abstractions for pluggable AI-tool quota / rate-limit trackers.  Every prov, Process-global registry of all :class:`QuotaTracker` instances.      Typical usa, Return the process-global :class:`QuotaTrackerRegistry` singleton., Replace the global registry with a fresh empty instance.      Intended for use i, reset_quota_registry() (+33 more)

### Community 132 - "keyword_detector.rs"
Cohesion: 0.11
Nodes (26): auth_still_flags_security_in_diff(), CategoryAutomaton, contains_error_indicator_is_lax_substring_match(), detect(), fires_on_uppercase_error_in_search(), is_word_boundary(), is_word_byte(), KeywordDetector (+18 more)

### Community 133 - "hf_impl.rs"
Cohesion: 0.10
Nodes (27): clone_shares_inner(), deterministic(), from_pretrained_downloads_real_tokenizer(), from_pretrained_invalid_repo_returns_hub_error(), HfTokenizer, HfTokenizerError, invalid_bytes_returns_error(), known_vocab_matches_count() (+19 more)

### Community 134 - "registry.rs"
Cohesion: 0.11
Nodes (31): from_file_loads_a_real_file(), Backend, case_insensitive_registration(), clear_hf_registrations(), clear_resets_state(), detect_backend(), detect_backend_ignores_runtime_registrations(), estimator_density_per_family() (+23 more)

### Community 135 - ".new"
Cohesion: 0.14
Nodes (32): assert_byte_equal_sha256(), buffer(), CaptureWriter, compression_decision_logged(), compression_off_passes_body_unchanged(), compression_on_long_body_passes_through_in_phase_a(), compression_on_non_json_skips(), compression_on_non_llm_path_skips() (+24 more)

### Community 136 - "network_diff.py"
Cohesion: 0.11
Nodes (31): Network capture comparison helpers., _anthropic_request_summary(), _body_bytes(), CapturedExchange, CaptureDiff, compare_captures(), exchange_from_record(), _header_delta() (+23 more)

### Community 137 - "memory.py"
Cohesion: 0.08
Nodes (29): OnnxTechniqueRouter, ONNX-based image technique router — no PyTorch dependency.  Uses ONNX INT8 model, Classify query intent using ONNX technique router., Analyze image properties using SigLIP ONNX encoder., Combined query + image classification., ONNX-based technique router — no PyTorch dependency.      Uses:     1. MiniLM ON, Lazy-load the technique router ONNX model., Lazy-load the SigLIP ONNX image encoder. (+21 more)

### Community 138 - "adversarial_grid.py"
Cohesion: 0.08
Nodes (25): AdversarialReport, _benign_lines(), CellResult, ClassSummary, _compression_ratio(), _contains(), _normalize(), _position_index() (+17 more)

### Community 139 - "ProjectInfo"
Cohesion: 0.13
Nodes (20): _build_section(), ClaudeCodeWriter, _merge_into_file(), _merge_recommendations(), _parse_prior_recommendations(), Path, Recommendation, Parse recommendations out of a prior marker block.      Returns [] if no marker (+12 more)

### Community 140 - "Memory"
Cohesion: 0.01
Nodes (160): Create and configure the memory system., Thread-safe LRU cache for hot memories in Headroom Memory.  Provides O(1) get/se, SQLite FTS5 full-text search index for Headroom Memory.  Provides fast, local fu, HNSW vector index for Headroom Memory using hnswlib.  Provides fast approximate, # NOTE: We don't import hnswlib at module level because it can crash with SIGILL, # NOTE: Use len() directly, not self.size - Lock is not reentrant!, SQLite memory store for Headroom's hierarchical memory system.  Provides persist, SQLite vector index for Headroom Memory using sqlite-vec.  Provides vector simil (+152 more)

### Community 141 - "__init__.py"
Cohesion: 0.09
Nodes (19): CopilotQuotaCategory, CopilotQuotaSnapshot, CopilotQuotaState, _CopilotQuotaTracker, discover_github_token(), parse_copilot_quota(), Any, GitHub Copilot monthly quota tracking via the copilot_internal/user API.  GitHub (+11 more)

### Community 142 - "models.py"
Cohesion: 0.09
Nodes (24): Fetch current subscription window data.          :param token: OAuth access toke, ExtraUsage, _parse_timestamp(), Any, datetime, timedelta, RateLimitWindow, Data models for Anthropic subscription window tracking.  Mirrors the Anthropic O (+16 more)

### Community 143 - "BaseTokenizer"
Cohesion: 0.10
Nodes (22): BaseTokenizer, ABC, Protocol, Base classes for tokenizer implementations.  Defines the TokenCounter protocol a, Protocol for token counting implementations.      Any class implementing this pr, Count tokens in a text string.          Args:             text: The text to coun, Encode text to token IDs.          Optional method - not all backends support en, Decode token IDs to text.          Optional method - not all backends support de (+14 more)

### Community 144 - "HeadroomHookProvider"
Cohesion: 0.05
Nodes (40): AfterToolCallEvent, _client_for(), HeadroomBundle, _make_headroom_client(), _make_serena_client(), _make_tokensave_client(), Any, HeadroomBundle — single-helper MCP wiring for a Strands Agent.  The cleanest pro (+32 more)

### Community 145 - "AnthropicCacheOptimizer"
Cohesion: 0.09
Nodes (15): AnthropicCacheOptimizer, Any, Optimize messages for Anthropic's cache.          Steps:         1. Analyze mess, Analyze messages to identify distinct content sections., Assess whether a section is cacheable., Check if content has dynamic elements., Determine if a message looks like a few-shot example., Estimate token count for tool definitions. (+7 more)

### Community 146 - "ContextTracker"
Cohesion: 0.11
Nodes (15): CompressedContext, ContextTracker, ContextTrackerConfig, Any, Track a compression event.          Args:             hash_key: The CCR hash for, Analyze a query to find relevant compressed contexts.          Args:, Calculate relevance score between query and compressed context.          Uses si, Extract meaningful keywords from text. (+7 more)

### Community 147 - "QuotaTracker"
Cohesion: 0.08
Nodes (16): Any, QuotaTracker, Register a tracker.  Duplicate keys are rejected., Return the registered tracker for *key*, or ``None``., Read-only snapshot of the registered tracker list., Start every available tracker and log its status., Stop all registered trackers (regardless of availability)., Return ``{key: stats_dict}`` for every available tracker.          Trackers that (+8 more)

### Community 148 - "embedding.rs"
Cohesion: 0.11
Nodes (23): batch_with_empty_items_returns_empty_vec(), cosine_similarity(), cosine_similarity_identical_vectors(), EmbeddingScorer, fastembed_batch_returns_one_score_per_item(), fastembed_enabled(), fastembed_loads_default_model(), fastembed_semantic_match_outranks_unrelated() (+15 more)

### Community 149 - "json_offload.rs"
Cohesion: 0.13
Nodes (24): JsonOffloadConfig, apply_compresses_large_tabular_array_and_stores_original(), apply_propagates_query_anchors_into_smart_crusher(), apply_skipped_for_non_json_input(), apply_skipped_when_smart_crusher_passes_through(), build_tabular_array(), cache_key_is_stable_across_calls_for_same_input(), cfg() (+16 more)

### Community 150 - "crushers.rs"
Cohesion: 0.15
Nodes (34): bug1_percentile_interpolates_when_index_non_integer(), bug1_percentile_proper_linear_interpolation(), bug4_k_split_no_overshoot_when_k_total_is_one(), bug4_k_split_no_overshoot_when_k_total_is_two(), cfg(), compute_k_split(), crush_number_array(), crush_object() (+26 more)

### Community 151 - "openai_cache_key.rs"
Cohesion: 0.13
Nodes (30): canonical_sha256(), derive_key(), different_model_yields_different_key(), different_system_yields_different_key(), different_tools_yields_different_key(), empty_string_key_treated_as_absent(), extract_system(), first_system_in_array() (+22 more)

### Community 152 - "get_compression_store"
Cohesion: 0.12
Nodes (23): build_qdrant_client_kwargs(), _parse_bool(), _parse_port(), qdrant_env_api_key(), qdrant_env_grpc_port(), qdrant_env_host(), qdrant_env_https(), qdrant_env_port() (+15 more)

### Community 153 - "SemanticCache"
Cohesion: 0.10
Nodes (23): _anthropic_usage_from_litellm(), _build_openai_extra_body(), _convert_anthropic_tool(), _convert_tool_choice(), LiteLLMBackend, _parse_tool_arguments(), Any, Backend (+15 more)

### Community 154 - "read_lifecycle.py"
Cohesion: 0.09
Nodes (24): FileOperation, _format_read_lifecycle_transform(), Any, Enum, str, Event-driven Read lifecycle management.  Detects stale and superseded Read tool, Apply lifecycle management to messages.          Single-pass analysis, targeted, Build tool_call_id → (tool_name, file_path) mapping.          Scans assistant me (+16 more)

### Community 155 - "Option"
Cohesion: 0.10
Nodes (29): apply_replacements(), BlockAction, BlockHeader, BlockOutcome, BodyView, compress_one_block(), CompressionManifest, ExclusionReason (+21 more)

### Community 156 - "log_template.rs"
Cohesion: 0.15
Nodes (25): LogTemplateConfig, all_unique_lines_are_emitted_verbatim(), below_min_lines_skipped(), blank_lines_break_runs(), cfg(), empty_input_skipped(), LogTemplate, lossless_round_trip_via_template_and_variants() (+17 more)

### Community 157 - "search_offload.rs"
Cohesion: 0.11
Nodes (18): SearchBloatConfig, apply_emits_cache_key_and_stores_original_for_clustered_input(), apply_skipped_when_compressor_declines_ccr(), default_bloat(), estimate_bloat_clustered_matches_score_high(), estimate_bloat_distributed_matches_score_low(), estimate_bloat_moderate_clustering(), estimate_bloat_safe_on_huge_inputs() (+10 more)

### Community 158 - "live_zone_anthropic.rs"
Cohesion: 0.14
Nodes (31): body_of(), cache_control_disabled_yields_floor_zero(), compress_anthropic_request(), e1_already_sorted_idempotent(), e1_passes_through_when_oauth(), e1_passes_through_when_subscription(), e1_skips_when_marker_present(), e1_skips_when_no_tools_field() (+23 more)

### Community 159 - "session_probes.py"
Cohesion: 0.12
Nodes (25): _all_text(), DimensionTally, EventProbeResult, extract_probe_targets(), _format_tally(), _normalize(), probe_event(), ProbeReport (+17 more)

### Community 160 - "litellm_pricing.py"
Cohesion: 0.07
Nodes (31): _litellm_cost(), Compute input cost via litellm.cost_per_token (cache-aware).      Returns total, LiteLLMModelPrefixRule, pricing_lookup_candidates(), Pure LiteLLM model-name resolution rules., Case-insensitive bare-model prefix mapping to a LiteLLM provider key., Return ordered LiteLLM keys to try for cost-per-token resolution., Return ordered LiteLLM model_cost keys to try for pricing lookup. (+23 more)

### Community 161 - "LogCompressor"
Cohesion: 0.06
Nodes (36): compute_optimal_k(), compute_unique_bigram_curve(), count_unique_simhash(), find_knee(), _hamming_distance(), _is_cjk_char(), Adaptive compression sizing via information saturation detection.  Instead of ha, Find the knee point in a monotonically increasing curve.      Uses the Kneedle a (+28 more)

### Community 162 - "hybrid.rs"
Cohesion: 0.15
Nodes (21): alpha_clamped_within_range(), alpha_hostname_modest_boost(), alpha_multiple_numeric_ids_boosts_alpha(), alpha_natural_language_query_is_base(), alpha_non_adaptive_returns_base(), alpha_single_numeric_id_modest_boost(), alpha_uuid_query_pushes_to_high_bm25_weight(), fallback_score_batch_consistent_with_single() (+13 more)

### Community 163 - "magika_detector.rs"
Cohesion: 0.13
Nodes (30): assert_detect(), detects_html(), detects_javascript_source(), detects_json(), detects_json_array(), detects_markdown_as_plain_text(), detects_plain_text(), detects_python_source() (+22 more)

### Community 164 - "recommendations.rs"
Cohesion: 0.13
Nodes (24): default_path(), empty_store_lookup_is_none(), from_toml_str_defaults_missing_skip_field_to_false(), from_toml_str_indexes_by_tuple_key(), get(), load_default(), lookup_returns_none_for_missing_slice(), malformed_toml_yields_parse_error() (+16 more)

### Community 165 - "ResponseState"
Cohesion: 0.19
Nodes (16): ContentPartState, ItemState, parse_json(), payload_preview(), ResponseState, Bytes, Error, HashMap (+8 more)

### Community 166 - "__init__.py"
Cohesion: 0.11
Nodes (23): date, get_anthropic_registry(), Anthropic model pricing information., Create and return an Anthropic pricing registry.      Returns:         PricingRe, get_deepseek_registry(), DeepSeek model pricing information., Create and return a DeepSeek pricing registry.      Returns:         PricingRegi, Pricing module for LLM cost estimation.  This module provides pricing informatio (+15 more)

### Community 167 - "compilerOptions"
Cohesion: 0.06
Nodes (32): compilerOptions, allowJs, esModuleInterop, forceConsistentCasingInFileNames, incremental, isolatedModules, jsx, lib (+24 more)

### Community 168 - "CCRToolInjector"
Cohesion: 0.21
Nodes (8): create_ccr_tool_definition(), Any, Scan messages for compression markers and extract hashes.          Args:, Create the CCR retrieval tool definition.      This tool definition is injected, Scan text for compression markers from any compressor., Inject CCR retrieval tool into tools list.          PR-B7 (`REALIGNMENT/04-phase, Inject retrieval instructions into system message.          Args:             me, Process a request, scanning for markers and injecting as needed.          This i

### Community 169 - "StructureMask"
Cohesion: 0.05
Nodes (42): extract_json_schema(), JSONStructureHandler, JSONToken, JSONTokenType, Any, Enum, JSON structure handler.  Extracts structural elements from JSON content: - Keys, Check if content is valid JSON. (+34 more)

### Community 170 - "HeadroomPostHook"
Cohesion: 0.08
Nodes (23): create_headroom_hooks(), HeadroomPostHook, HeadroomPreHook, HookMetrics, Any, Agno hooks for Headroom integration.  This module provides pre_hooks and post_ho, History of optimization metrics (thread-safe copy)., Track the run input.          This is called by Agno before the LLM processes th (+15 more)

### Community 171 - "responses.py"
Cohesion: 0.09
Nodes (42): Persistent install / deployment helpers for Headroom., ArtifactRecord, ConfigScope, InstallPreset, ProviderSelectionMode, Enum, str, Models used by the install / deployment subsystem. (+34 more)

### Community 172 - "images.py"
Cohesion: 0.07
Nodes (50): iso_utc_now(), Return the current UTC timestamp in ISO-8601 format., deploy_root(), log_path(), manifest_path(), openclaw_config_path(), pid_path(), profile_root() (+42 more)

### Community 173 - "openai.py"
Cohesion: 0.15
Nodes (17): canonical_array_json(), canonical_json_for_match(), CrushArrayResult, estimate_array_bytes(), group_key(), GroupBuckets, opaque_kind_label(), process_string_does_not_alter_short_quoted_strings() (+9 more)

### Community 174 - "Phase B — Live-Zone-Only Compression Engine"
Cohesion: 0.10
Nodes (16): Any, datetime, Memory, Add a new memory to the system.          Creates a memory with the specified con, Add multiple memories in a batch operation.          More efficient than calling, Get a memory by ID.          Checks cache first, then falls back to store., Record retrieval metadata for memories returned to a caller., Update an existing memory.          Updates the specified fields and re-indexes (+8 more)

### Community 175 - "Phase I — Test Infrastructure (Continuous, Parallel)"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I1 — SHA-256 byte-faithful round-trip test on recorded production payload, Scope

### Community 176 - "Image Compression"
Cohesion: 0.06
Nodes (33): Anthropic, API Reference, `CompressionResult`, Configuration, `crop` (50-90% savings), Direct API, Disable Image Compression, `full_low` (87% savings) (+25 more)

### Community 177 - "Option"
Cohesion: 0.07
Nodes (7): PyLogCompressionResult, PySearchCompressionResult, Option, RustLogResult, RustLogStats, RustSearchResult, RustSearchStats

### Community 178 - "installer.py"
Cohesion: 0.11
Nodes (28): get_rtk_path(), is_rtk_installed(), _managed_rtk_candidates(), Path, rtk (Rust Token Killer) integration for Headroom.  rtk compresses CLI output (te, Return known Headroom-managed rtk binary paths., Get path to rtk binary — check PATH first, then ~/.headroom/bin/., Check if rtk is available. (+20 more)

### Community 179 - "UniversalCompressor"
Cohesion: 0.29
Nodes (4): Compress content with structure preservation.          Args:             content, Apply compression respecting structure mask.          Args:             content:, Estimate token count.          Uses simple heuristic: ~4 characters per token., Store original in CCR for retrieval.          Args:             original: Origin

### Community 180 - "parser.py"
Cohesion: 0.10
Nodes (29): Block, Atomic unit of context analysis., Detected waste signals in a request., Total waste tokens detected., Convert to dictionary for storage., WasteSignals, _canonical_call_key(), _coerce_tool_call_to_dict() (+21 more)

### Community 181 - "verbosity.py"
Cohesion: 0.12
Nodes (24): analyze(), _assistant_words_and_text(), extract_signals(), _human_text(), _HumanMsg, _ordered_events(), _parse_session(), _parse_ts() (+16 more)

### Community 182 - "RegisterResult"
Cohesion: 0.09
Nodes (47): _apply_user_env(), DeploymentManifest, ManagedMutation, A reversible change applied by `headroom install`., Persisted deployment state for a named profile., Return user shell files that can carry the persistent env block., unix_user_env_targets(), apply_mutations() (+39 more)

### Community 183 - "PR-D1 — Native Bedrock InvokeModel route (non-streaming)"
Cohesion: 0.06
Nodes (31): Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by, Blocked by (+23 more)

### Community 184 - "Transform Reference"
Cohesion: 0.06
Nodes (32): Cache Hit Improvement, CacheAligner, CodeAwareCompressor (Optional), Compression Strategies, Configuration, Configuration, Configuration, Configuration (+24 more)

### Community 185 - "dependencies"
Cohesion: 0.07
Nodes (29): class-variance-authority, clsx, dependencies, class-variance-authority, clsx, fumadocs-core, fumadocs-mdx, fumadocs-twoslash (+21 more)

### Community 186 - "bm25.rs"
Cohesion: 0.16
Nodes (21): BM25Scorer, higher_term_frequency_increases_score(), long_match_bonus_applied_only_for_8plus_chars(), Default, HashMap, RelevanceScore, RelevanceScorer, Self (+13 more)

### Community 187 - "releases.mdx"
Cohesion: 0.06
Nodes (30): build, build-wheels, collect-dist, Configuration, Conventional Commits & Semantic Bumping, create-release, detect-version, Dry-run Test (+22 more)

### Community 188 - "SavingsLedger"
Cohesion: 0.10
Nodes (17): output_savings(), CLI: show counterfactual output-token reduction., Show estimated/measured output-token reduction from the shaper.      Output toke, process_is_stateless(), True when the process must not write to the workspace.      True if ``set_proces, Any, Result of an estimation pass., Accumulates shaped (treatment) and unshaped (control) observations and     produ (+9 more)

### Community 189 - "models.py"
Cohesion: 0.06
Nodes (38): CompressionEvaluator, EvalMode, EvalResult, EvalSuiteResult, Enum, Core evaluation infrastructure for Headroom.  This module provides the foundatio, Aggregated results from an evaluation suite., Generate human-readable summary. (+30 more)

### Community 190 - "SavingsTracker"
Cohesion: 0.08
Nodes (19): get_default_savings_storage_path(), Any, Return frontend-friendly historical data for `/stats-history`., Return export rows for history or a rollup series., Export history or rollup series as CSV., Best-effort retention of unreadable state before starting fresh., Seed the v5 aggregate from the best information available in v4., Persist any records held back by the save throttle.          Call on graceful sh (+11 more)

### Community 191 - "HuggingFaceTokenizer"
Cohesion: 0.08
Nodes (20): get_tokenizer_name(), HuggingFaceTokenizer, _load_timeout_secs(), _load_tokenizer(), Any, HuggingFace tokenizer wrapper for open models.  Supports Llama, Mistral, Falcon,, Load and cache HuggingFace tokenizer.      The first attempt is cache-only (``lo, Get HuggingFace tokenizer name for a model.      Args:         model: Model name (+12 more)

### Community 192 - "Phase C — Rust Proxy Paths"
Cohesion: 0.05
Nodes (37): Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by (+29 more)

### Community 193 - "Phase E — Phase 3 Cache Stabilization"
Cohesion: 0.05
Nodes (37): Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by (+29 more)

### Community 194 - "PR-F1 — `classify_auth_mode` helper"
Cohesion: 0.06
Nodes (30): Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by, Blocked by (+22 more)

### Community 195 - "repro_codex_replay.py"
Cohesion: 0.13
Nodes (24): _anthropic_client(), AnthropicHttpStats, _asyncio_timeout(), build_parser(), _check_reachable(), _classify_exit(), CodexWsStats, format_summary() (+16 more)

### Community 196 - "Agno Integration"
Cohesion: 0.06
Nodes (30): 1. Basic Model Wrapping, 2. Agent with Observability Hooks, 3. Convenience Hook Factory, 4. Custom Configuration, 5. Standalone Message Optimization, 6. Async Operations, Agno Integration, Best Practices for Maximum Savings (+22 more)

### Community 197 - "Configuration"
Cohesion: 0.06
Nodes (32): All Options, Anthropic, Cache Aligner Configuration, Command Line Options, Config File Format, Configuration, Configuration Methods, Configuration Precedence (+24 more)

### Community 198 - "LangChain Integration"
Cohesion: 0.06
Nodes (31): 1. Chat Model Wrapper, 2. Memory Integration, 3. Retriever Integration, 4. Agent Tool Wrapping, 5. Streaming Metrics, 6. LangSmith Integration, Async Support, Check Your Savings (+23 more)

### Community 199 - "TrainedRouter"
Cohesion: 0.09
Nodes (18): BaseModelOutputWithPooling, _extract_tensor(), get_trained_router(), Initialize the router.          Args:             model_path: Path to trained mo, Check if required models can be loaded., Lazy load the classifier and optionally SigLIP., Release router-held model references and optional shared cache entries., Alias for release_models() while preserving subclass dispatch. (+10 more)

### Community 200 - "anchors.rs"
Cohesion: 0.12
Nodes (19): email_typo_pattern_still_matches_real_emails(), extract_query_anchors(), extracts_email(), extracts_hostname(), extracts_numeric_id_unchanged(), extracts_quoted_string_double(), extracts_quoted_string_single(), extracts_uuid_lowercased() (+11 more)

### Community 201 - "outliers.rs"
Cohesion: 0.08
Nodes (33): default_oss_constraints_returns_two(), keep_errors_constraint_finds_error_items(), keep_errors_constraint_uses_item_strings_when_provided(), keep_structural_outliers_constraint_returns_indices(), KeepErrorsConstraint, KeepStructuralOutliersConstraint, Option, String (+25 more)

### Community 202 - "eventstream_to_sse.rs"
Cohesion: 0.14
Nodes (25): accept_eventstream_selects_passthrough(), accept_eventstream_with_q_param_still_selects_passthrough(), accept_text_event_stream_selects_sse(), extract_anthropic_event_type(), header_value_preview(), header_value_preview_truncates_at_char_boundary(), missing_event_type_is_loud(), multi_accept_with_eventstream_among_them_selects_passthrough() (+17 more)

### Community 203 - "JSONStructureHandler"
Cohesion: 0.12
Nodes (20): Mechanism B: hold-back Read maturation (compress before cache entry).      Motiv, ReadMaturationConfig, _Activity, MaturationResult, MaturedRead, Any, Mechanism B: hold-back Read maturation — compress before cache entry.  The prefi, Per-session Read maturation state machine.      Construct once per session (or h (+12 more)

### Community 204 - "registry.py"
Cohesion: 0.17
Nodes (9): _is_anthropic_auth(), _is_claude_code_client(), ProxyProviderRuntime, Return True for Claude Code/Claude CLI requests using Anthropic gateway auth., Provider runtime state used by the proxy server., Return the resolved upstream target for a provider., Return the pipeline provider instance for a provider., Resolve the upstream provider that should serve OpenAI-style model metadata. (+1 more)

### Community 205 - "API Reference"
Cohesion: 0.06
Nodes (28): AnthropicProvider, API Reference, BM25Scorer, CacheAligner, CacheAlignerConfig, `chat.completions.create(**kwargs)`, `chat.completions.simulate(**kwargs)`, Configuration Classes (+20 more)

### Community 206 - "HeadroomChatMessageHistory"
Cohesion: 0.10
Nodes (18): BaseChatMessageHistory, _check_langchain_available(), HeadroomChatMessageHistory, Any, BaseMessage, Initialize HeadroomChatMessageHistory.          Args:             base_history:, Get messages, applying compression if over threshold.          Returns:, Add a message to the underlying history.          Args:             message: The (+10 more)

### Community 207 - "tiktoken_impl.rs"
Cohesion: 0.12
Nodes (22): CoreBPE, backend_is_tiktoken(), case_insensitive_dispatch(), determinism(), empty_string_is_zero(), encoding_dispatch(), encoding_for(), known_token_counts_for_o200k() (+14 more)

### Community 208 - "GcpAdcTokenSource"
Cohesion: 0.14
Nodes (19): CachedToken, GcpAdcTokenSource, Arc, Debug, Default, Into, Mutex, Option (+11 more)

### Community 209 - "e2e_simulators.rs"
Cohesion: 0.18
Nodes (26): anthropic_messages_json_and_stream_use_simulator(), assert_not_simulator_response(), assert_simulator_header(), bedrock_invoke_converse_and_streaming_use_simulator(), headroom_preflight_errors_stop_before_simulator_fallback(), json_error_stub(), json_post(), openai_chat_responses_and_conversations_use_simulator() (+18 more)

### Community 210 - "PyDiffCompressionResult"
Cohesion: 0.07
Nodes (8): PyDiffCompressionResult, PyDiffCompressor, PyTextCrusher, PyTextCrusherResult, DiffCompressor, DiffCompressionResult, RustTextCrusher, RustTextCrusherResult

### Community 211 - "source.ts"
Cohesion: 0.11
Nodes (15): { GET }, generateMetadata(), Page(), GET(), generateStaticParams(), GET(), generateStaticParams(), gitConfig (+7 more)

### Community 212 - "AnyLLMBackend"
Cohesion: 0.10
Nodes (16): AnyLLMBackend, Any, Backend, Exception, Convert Anthropic content blocks to OpenAI format., Convert any-llm/OpenAI response to Anthropic format., Send message via any-llm., Stream message via any-llm. (+8 more)

### Community 213 - "CompressionOnlyRunner"
Cohesion: 0.12
Nodes (14): OpenAICacheOptimizer, Any, Name of this optimizer., Provider this optimizer is for., The caching strategy this optimizer uses., Optimize messages for OpenAI's prefix caching.          This method stabilizes t, Estimate potential cost savings from caching.          OpenAI provides 50% disco, Normalize whitespace in content.          Ensures consistent whitespace formatti (+6 more)

### Community 214 - "HeadroomLangSmithCallbackHandler"
Cohesion: 0.09
Nodes (20): _check_langchain_available(), HeadroomLangSmithCallbackHandler, PendingMetrics, Any, BaseCallbackHandler, BaseMessage, UUID, Initialize HeadroomLangSmithCallbackHandler.          Args:             langsmit (+12 more)

### Community 215 - "savings_tracker.py"
Cohesion: 0.17
Nodes (25): Project-name normalization policy for proxy attribution., _bucket_start(), _coerce_float(), _coerce_int(), _empty_by_model_entry(), _empty_display_session(), _empty_project_entry(), _normalize_by_model() (+17 more)

### Community 216 - "Dynamic SmartCrusher Preservation Plan"
Cohesion: 0.07
Nodes (28): Configuration Schema, Current Implementation Analysis, Dynamic SmartCrusher Preservation Plan, Idea 1: Size-Proportional Anchor Budget, Idea 2: Pattern-Aware Anchor Weighting, Idea 3: Query-Aware Dynamic Weighting, Idea 4: Information-Density Anchor Selection, Idea 5: TOIN-Learned Position Importance (+20 more)

### Community 217 - "Troubleshooting Guide"
Cohesion: 0.07
Nodes (29): Anthropic: "Authentication error", Check Storage Contents, "Compression too aggressive", "Connection refused" when calling proxy, Debugging Techniques, Enable Full Logging, Error Reference, Getting Help (+21 more)

### Community 218 - "InMemoryCcrStore"
Cohesion: 0.15
Nodes (19): capacity_evicts_oldest(), concurrent_puts_and_gets_do_not_corrupt(), Entry, expired_entries_are_dropped_on_get(), expired_get_does_not_wipe_concurrent_refresh(), InMemoryCcrStore, missing_hash_returns_none(), put_overwrites_under_same_hash() (+11 more)

### Community 219 - "diff_offload.rs"
Cohesion: 0.16
Nodes (19): DiffBloatConfig, apply_emits_key_and_persists_original(), apply_skipped_when_compressor_declines_ccr(), build_diff(), default_bloat(), DiffOffload, estimate_bloat_at_threshold_scores_zero(), estimate_bloat_below_min_lines_is_zero() (+11 more)

### Community 220 - "log_offload.rs"
Cohesion: 0.15
Nodes (17): LogBloatConfig, apply_emits_cache_key_and_stores_original_for_repetitive_log(), apply_returns_skipped_when_underlying_compressor_declines_ccr(), default_bloat(), estimate_bloat_high_repetition_scores_high(), estimate_bloat_priority_dilution_alone_scores_meaningfully(), estimate_bloat_safe_on_huge_inputs(), estimate_bloat_unique_errors_score_low() (+9 more)

### Community 221 - "stats_math.rs"
Cohesion: 0.10
Nodes (11): format_g(), median(), normalize_scientific_exp(), Option, String, sample_stdev(), sample_stdev_basic(), sample_variance() (+3 more)

### Community 222 - "eventstream.rs"
Cohesion: 0.13
Nodes (31): build_chunk_message(), crc_validation_off_accepts_corrupt_prelude(), CrcValidation, empty_buffer_yields_none(), EventStreamMessage, EventStreamParser, header_bytes_round_trip(), HeaderValue (+23 more)

### Community 223 - "anthropic_cache_control.rs"
Cohesion: 0.13
Nodes (23): any_anthropic_cache_control(), applied_path_preserves_other_tool_fields(), applies_only_one_marker_in_first_ship_default(), auto_place_anthropic_cache_control(), AutoPlaceOutcome, block_has_cache_control(), body_one_tool_no_markers(), does_nothing_when_no_tools_present() (+15 more)

### Community 224 - "Config"
Cohesion: 0.16
Nodes (15): AuthModePolicyEnforcement, CacheControlAutoFrozen, CliArgs, CompressionMode, Config, parse_bytes(), parse_duration(), Duration (+7 more)

### Community 225 - "SseEvent"
Cohesion: 0.18
Nodes (19): AnthropicStreamState, BlockState, parse_json(), payload_preview(), Bytes, Error, HashMap, Option (+11 more)

### Community 226 - "Self"
Cohesion: 0.08
Nodes (12): _core(), PyCrushResult, PyLogCompressor, PyLogCompressorConfig, PySmartCrusher, Self, PyModule, PyResult (+4 more)

### Community 227 - "Headroom Evaluation Framework"
Cohesion: 0.07
Nodes (27): Architecture, Available Datasets, Before/After (Default), CI/CD Integration, Code, Compression Benchmarks — "Big Savings, Accuracy Preserved", Compression-Only (Zero Cost), Environment Variables (+19 more)

### Community 228 - "opencode.py"
Cohesion: 0.07
Nodes (40): EvalCase, EvalSuite, Path, Save results to JSON file., A collection of evaluation cases., Load suite from JSONL file., Save suite to JSONL file., A single evaluation case.      Attributes:         id: Unique identifier for thi (+32 more)

### Community 229 - "AnthropicTokenCounter"
Cohesion: 0.12
Nodes (17): AnthropicTokenCounter, _load_custom_model_config(), Any, TokenCounter, Load custom model configuration from environment or config file.      Checks (in, Token counter for Anthropic models.      When an Anthropic client is provided, u, Initialize token counter.          Args:             model: Anthropic model name, Count tokens in text.          Note: For single text strings, uses tiktoken appr (+9 more)

### Community 230 - "StageTimer"
Cohesion: 0.09
Nodes (15): emit_stage_timings_log(), Any, BaseException, Stage-timing instrumentation for request handlers.  Provides a lightweight, sync, Return a context manager that records the named stage's duration., Record a pre-computed duration (e.g. from an existing timer).          If the st, Internal: record a duration from a ``StageMeasurement``., Return total milliseconds since the timer was created. (+7 more)

### Community 231 - "TiktokenCounter"
Cohesion: 0.09
Nodes (20): _get_encoding(), get_encoding_for_model(), load_encoding(), _load_timeout_seconds(), Any, RuntimeError, Tiktoken-based token counter for OpenAI models.  Tiktoken is OpenAI's fast BPE t, Get a tiktoken encoding, cached for performance.      Bounded by ``HEADROOM_TIKT (+12 more)

### Community 233 - "Proxy Server Documentation"
Cohesion: 0.07
Nodes (28): Aggregate Health, API Endpoints, Command Line Options, Common agent CLI entrypoints, Configuration via Environment, Context Management Options, Core Options, Cost Tracking (+20 more)

### Community 234 - "HeadroomDocumentCompressor"
Cohesion: 0.10
Nodes (19): Callbacks, Document, BaseDocumentCompressor, _check_langchain_available(), HeadroomDocumentCompressor, Any, Retriever integration for LangChain with intelligent document compression.  This, Compresses retrieved documents based on relevance to query.      Uses BM25-style (+11 more)

### Community 235 - "start_proxy_with_state"
Cohesion: 0.18
Nodes (26): install_static_token_source(), start_proxy_with_state(), start_simulator_proxy_without_bedrock_credentials(), adc_bearer_token_signed_correctly(), adc_failure_returns_5xx_no_silent_forward(), assert_byte_equal_sha256(), CapturedUpstream, minimal_vertex_body() (+18 more)

### Community 236 - "start_proxy_with"
Cohesion: 0.11
Nodes (45): start_proxy_with(), assert_byte_equal(), create_conversation_passthrough_byte_equal(), create_items_byte_equal_through_proxy(), delete_conversation_passthrough(), delete_item_passthrough(), get_conversation_passthrough(), get_item_passthrough() (+37 more)

### Community 238 - "agent_savings.py"
Cohesion: 0.16
Nodes (13): AgentSavingsProfile, apply_agent_savings_profile(), CompressConfigLike, get_agent_savings_profile(), Protocol, Shared token-savings profiles for coding agents., Seed proxy env defaults without overriding explicit user settings., Return a named agent savings profile.      An unrecognized name falls back to th (+5 more)

### Community 239 - "mcp.py"
Cohesion: 0.03
Nodes (101): get_headroom_command(), mcp(), mcp_install(), mcp_status(), mcp_uninstall(), MCP (Model Context Protocol) CLI commands for Claude Code integration.  Provides, Install the Headroom MCP server into every detected coding agent.      \b     By, Remove Headroom MCP server from detected agent configs.      \b     Removes head (+93 more)

### Community 240 - "providers.py"
Cohesion: 0.05
Nodes (30): get_sample_eval_cases(), HTMLEvalCase, HTMLEvalResult, HTMLEvalSuiteResult, HTMLExtractionEvaluator, Any, Evaluation framework for HTML content extraction.  This module evaluates whether, Aggregated results from HTML extraction evaluation suite. (+22 more)

### Community 241 - "ClaudeCodePlugin"
Cohesion: 0.08
Nodes (22): ClaudeCodePlugin, _component_tokenizations(), _decode_project_path(), _decode_windows_path(), _greedy_path_decode(), _project_display_name(), Path, Scan all conversation JSONL files for a project.          Claude Code writes the (+14 more)

### Community 242 - "ServerSpec"
Cohesion: 0.06
Nodes (31): _check_pricing_staleness(), _get_encoding(), _get_encoding_name_for_model(), _get_litellm_module(), _infer_model_family(), _load_custom_model_config(), OpenAITokenCounter, Any (+23 more)

### Community 243 - "output_savings.py"
Cohesion: 0.08
Nodes (19): Any, Initialize the semantic cache.          Args:             config: Cache configur, Look up a cached entry.          Args:             query: Query text to search f, Store a response in the cache.          Args:             query: Query text, Invalidate a cache entry by key., Clear all cache entries., Get cache statistics., Find the most similar cached entry. (+11 more)

### Community 244 - "generator.py"
Cohesion: 0.23
Nodes (11): codex_image_subpath(), handle_openai_image_endpoint(), OpenAIImageEndpoint, Any, Request, OpenAI image endpoint routing helpers., An OpenAI image endpoint with a possible Codex ChatGPT-auth override., Return the Codex image backend subpath for an OpenAI image endpoint. (+3 more)

### Community 245 - "savings_ledger.py"
Cohesion: 0.17
Nodes (22): aggregate_savings(), _Bucket, _coerce_timestamp(), estimate_cost_usd(), _label(), _maybe_compact(), Any, datetime (+14 more)

### Community 246 - "PipelineConfig"
Cohesion: 0.13
Nodes (19): ConfigError, bloat_log_weights_sum_to_at_most_one(), BloatConfigs, ConfigError, defaults_carry_reformat_and_offload_sections(), defaults_match_documented_thresholds(), from_default_str_does_not_panic(), from_toml_str_overrides_defaults() (+11 more)

### Community 247 - "orchestration.rs"
Cohesion: 0.21
Nodes (25): cfg(), dedup_all_distinct_unchanged(), dedup_empty_input(), dedup_key_order_independent(), dedup_lowest_index_wins_for_duplicates(), dedup_skips_out_of_bounds(), deduplicate_indices_by_content(), fill_adds_diverse_uniques_up_to_max() (+17 more)

### Community 248 - "framing.rs"
Cohesion: 0.16
Nodes (16): comment_skipped_no_event_yielded(), data_line_only_yields_event_with_no_event_name(), done_sentinel_detected(), empty_buffer_yields_nothing(), event_name_and_data(), find_double_newline(), FramingError, multiple_data_lines_joined_with_newline() (+8 more)

### Community 249 - "domain.rs"
Cohesion: 0.23
Nodes (22): anthropic_message(), anthropic_sse(), bedrock_eventstream(), bedrock_invoke(), conversation_collection(), conversation_item(), conversation_items(), conversation_object() (+14 more)

### Community 250 - "troubleshooting.mdx"
Cohesion: 0.08
Nodes (25): Anthropic: Authentication error, Claude Code context window is larger through the proxy, Compression Too Aggressive, Connection refused when calling proxy, Debugging Techniques, Enable Full Logging, Getting Help, High Latency (+17 more)

### Community 251 - "read_maturation.py"
Cohesion: 0.11
Nodes (13): _check_properties_recursive(), CompressionOnlyResult, Any, Compression-only evaluation runner.  Evaluates compression quality WITHOUT makin, Check if probe facts survive compression.          Each test_case should have:, Result from a compression-only evaluation., Generate synthetic test cases for CCR needle-retention testing.          Each ca, Generate test cases with probe facts for information retention testing. (+5 more)

### Community 252 - "copilot_auth.py"
Cohesion: 0.09
Nodes (26): discover_pipeline_extensions(), PipelineEvent, PipelineExtension, PipelineStage, Any, Enum, Protocol, str (+18 more)

### Community 253 - "EmbeddingScorer"
Cohesion: 0.11
Nodes (19): _cosine_similarity(), embedding_available(), EmbeddingScorer, _get_numpy(), _pinned_revision(), RelevanceScore, RelevanceScorer, TextEmbedding (+11 more)

### Community 254 - "MistralTokenizer"
Cohesion: 0.08
Nodes (17): get_mistral_tokenizer(), Get MistralTokenizer class (requires mistral-common)., _get_tokenizer(), get_tokenizer_version(), MistralTokenizer, Any, Token counter using Mistral's official tokenizer.      Uses mistral-common packa, Initialize Mistral tokenizer.          Args:             model: Mistral model na (+9 more)

### Community 255 - "compact_lossless"
Cohesion: 0.15
Nodes (25): collapse_runs(), compact_lossless(), diff_strip_index(), expand_runs(), is_run_collapsed(), _join(), path_heading(), path_unheading() (+17 more)

### Community 256 - "PR-H1 — Retire Python proxy request path"
Cohesion: 0.08
Nodes (25): Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by, Blocks, Blocks (+17 more)

### Community 257 - "Headroom"
Cohesion: 0.08
Nodes (26): Accuracy Benchmarks, Agno, Cache Optimization, Cloud Providers, Failure Learning, Framework Integrations, Headroom, How It Works (+18 more)

### Community 258 - "Quickstart Guide"
Cohesion: 0.08
Nodes (26): Adjust Compression, Audit Mode (Observe Only), Basic Example, Common Configuration, "Compression too aggressive", "High latency", Installation, Method 1: Enable Logging (+18 more)

### Community 259 - "devDependencies"
Cohesion: 0.08
Nodes (25): ai, @ai-sdk/openai, @anthropic-ai/sdk, devDependencies, ai, @ai-sdk/openai, @anthropic-ai/sdk, openai (+17 more)

### Community 260 - "cache_control.rs"
Cohesion: 0.17
Nodes (13): compute_frozen_count(), extract_ttl(), Option, Self, String, Value, ttl_walker_accepts_1h_before_5m(), ttl_walker_flags_5m_before_1h() (+5 more)

### Community 261 - "Compaction"
Cohesion: 0.10
Nodes (17): CsvSchemaFormatter, JsonFormatter, Self, write_compaction(), write_table(), Bucket, CellValue, Compaction (+9 more)

### Community 262 - "AppState"
Cohesion: 0.32
Nodes (23): forward_conversations(), handle_conversations_create(), handle_conversations_delete(), handle_conversations_get(), handle_conversations_item_delete(), handle_conversations_item_get(), handle_conversations_items_create(), handle_conversations_items_list() (+15 more)

### Community 263 - "OpenAICacheOptimizer"
Cohesion: 0.14
Nodes (18): get_python_forwarder_mode(), OutboundBody, prepare_outbound_body_bytes(), Any, PythonForwarderMode, Byte-faithful outbound request body forwarding policy.  This module owns the sma, Compatibility tuple wrapper around :func:`select_outbound_body`., Concrete outbound body bytes plus their provenance. (+10 more)

### Community 264 - "BaseStructureHandler"
Cohesion: 0.10
Nodes (15): BaseStructureHandler, NoOpHandler, ABC, Any, Base class and protocol for structure handlers.  Structure handlers extract stru, Extract structure mask from content.          This is the main entry point. It h, Check if this handler can process the content.          Default implementation r, Extract structure mask from content.          Subclasses implement this to provi (+7 more)

### Community 265 - "TransformPipeline"
Cohesion: 0.09
Nodes (23): _CacheEntry, CompressionCache, _extract_text_from_blocks(), _extract_tool_result_content(), _is_tool_result_message(), Content-addressed compression cache with LRU eviction.  Used in "token headroom, Content-addressed cache mapping content hashes to compressed versions.      Uses, Retrieve compressed content by hash, refreshing LRU position on hit. (+15 more)

### Community 266 - "CostTracker"
Cohesion: 0.10
Nodes (14): CostTracker, Any, Cost tracking for evaluation suite runs.  Tracks actual API spend per benchmark,, Estimate cost for a benchmark run before executing it., Check if we can afford a benchmark run within remaining budget., Return summary of spending., Print a formatted cost summary., Record of a single API call's token usage. (+6 more)

### Community 267 - "__init__.py"
Cohesion: 0.09
Nodes (33): _cache_path(), _env_off(), _env_on(), fetch_latest_version(), format_update_notice(), _in_docker(), installed_version(), _is_source_checkout() (+25 more)

### Community 268 - "auth_mode.py"
Cohesion: 0.12
Nodes (25): _auth_signals(), classify_auth_mode(), _header_get(), Any, AuthMode, Auth-mode classifier — Phase F PR-F1 (Python port).  Direct port of ``crates/hea, Whether to stamp ``X-Client: codex`` on a request to the proxy.      Stamping ``, Read a single header, case-insensitively, returning ``""`` on miss.      Accepts (+17 more)

### Community 269 - "PR-G1 — Wrap CLI breadth: cline, continue, goose, openhands"
Cohesion: 0.08
Nodes (24): Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by, Blocks, Blocks (+16 more)

### Community 270 - "Proxy Metrics"
Cohesion: 0.08
Nodes (25): Anonymous Telemetry vs OTEL, Beacon identity fields, Budget Alerts, Cost Tracking, Enable Logging, Grafana Dashboard, Health Check, Historical Metrics (+17 more)

### Community 271 - "compute_key"
Cohesion: 0.14
Nodes (21): from_config(), Box, Result, compute_key(), compute_key_diverges_for_different_payloads(), compute_key_is_24_hex_chars(), compute_key_is_deterministic(), marker_for() (+13 more)

### Community 272 - "classifier.rs"
Cohesion: 0.18
Nodes (19): base64_blob_detected(), CellClass, cfg(), classify_cell(), classify_string(), ClassifyConfig, config_threshold_respected(), html_chunk_detected() (+11 more)

### Community 273 - "crusher.rs"
Cohesion: 0.18
Nodes (18): deterministic(), doc(), extractive_and_compresses(), is_salient(), passthrough_when_small(), BM25Scorer, Default, HashSet (+10 more)

### Community 274 - "ccr_roundtrip.rs"
Cohesion: 0.16
Nodes (22): default_crusher_stores_dropped_rows(), distinct_inputs_produce_distinct_store_entries(), document_walker_with_store_roundtrips_opaque_blob(), dropped_summary_marker_points_at_stored_hash(), extract_hash_from_marker(), extract_inner_hash(), force_lossy_config(), full_crush_pipeline_roundtrips_through_store() (+14 more)

### Community 275 - "live_zone_openai.rs"
Cohesion: 0.18
Nodes (19): body_of(), compress_openai_chat_request(), e1_passes_through_when_oauth(), e1_sorts_tools_when_payg(), invalid_json_passthrough(), mode_off_short_circuits(), n_absent_no_skip(), n_eq_one_no_skip() (+11 more)

### Community 276 - "headers.rs"
Cohesion: 0.18
Nodes (21): append_xff(), build_forward_keeps_internal_when_disabled(), build_forward_request_headers(), build_forward_strips_internal_when_enabled(), connection_listed_headers(), connection_listed_strip(), filter_response_headers(), is_hop_by_hop() (+13 more)

### Community 277 - "mount_anthropic_capture"
Cohesion: 0.14
Nodes (20): buffer(), CaptureWriter, mount_anthropic_capture(), oauth_body_passes_through_byte_equal(), payg_apply_emits_e3_applied_event(), payg_body_with_existing_marker_passes_through_byte_equal(), payg_body_without_markers_gets_marker_on_last_tool(), Arc (+12 more)

### Community 278 - "API endpoints"
Cohesion: 0.07
Nodes (29): Agent wrapping, API endpoints, Bedrock via a local gateway, Built-in profiles, CLI options, Cloud providers, Context management, Core (+21 more)

### Community 279 - "HeadroomError"
Cohesion: 0.11
Nodes (21): CacheError, CompressionError, ConfigurationError, HeadroomError, ProviderError, Any, Exception, Custom exceptions for Headroom.  This module provides explicit exception classes (+13 more)

### Community 280 - "qdrant_env.py"
Cohesion: 0.08
Nodes (14): CompressionStoreBackend, Any, Protocol, Get all hash keys in storage.          Returns:             List of all hash key, Get all entries as (hash_key, entry) pairs.          Returns:             List o, Get backend-specific statistics.          Returns:             Dict with backend, Protocol for CompressionStore storage backends.      This protocol defines the m, Retrieve an entry by hash key.          Args:             hash_key: The unique h (+6 more)

### Community 281 - "resolve_codex_routing"
Cohesion: 0.11
Nodes (16): DiffArtifact, Diff info for a single transform (for debugging/perf)., Complete diff artifact for debugging transform pipeline.      Opt-in via Headroo, TransformDiff, create_pipeline(), Any, Tokenizer, Get tokenizer for model.          Uses provider's tokenizer if available, otherw (+8 more)

### Community 282 - "memory_ranker.py"
Cohesion: 0.13
Nodes (19): boost_memory_score(), memory_recency_factor(), parse_memory_created_at(), datetime, Pure memory ranking policy helpers.  This module owns timestamp parsing and rece, Best-effort parse of a memory timestamp into a UTC-aware datetime., Compute the recency multiplier for one memory candidate.      Missing timestamps, Apply the recency multiplier to a backend similarity score. (+11 more)

### Community 283 - "main"
Cohesion: 0.12
Nodes (29): apply_to_environ(), _atomic_write_text(), _coerce(), effective_values(), load(), _mask(), Any, Exception (+21 more)

### Community 284 - "installation.mdx"
Cohesion: 0.09
Nodes (22): Build from source, Core package, Dashboard, Docker, Editable install fails (`pip install -e`), Environment variables, Extras, Image tags (+14 more)

### Community 285 - "copilot_auth.py"
Cohesion: 0.04
Nodes (100): copilot_auth(), login(), GitHub Copilot authentication commands., Manage Headroom's GitHub Copilot OAuth token., Sign in with GitHub's Copilot OAuth device-code flow., Show whether Headroom has a saved Copilot OAuth token., status(), _api_url_from_exchange_payload() (+92 more)

### Community 286 - "get_store"
Cohesion: 0.27
Nodes (18): detect_id_field_statistically(), detect_score_field_statistically(), id_field_high_entropy_strings(), id_field_high_uniqueness_alone_triggers_catchall(), id_field_low_uniqueness_rejected(), id_field_sequential_numeric(), id_field_uuid_strings_high_confidence(), Value (+10 more)

### Community 287 - "TextStatisticsExtractor"
Cohesion: 0.12
Nodes (13): Counter, Calculate Flesch Reading Ease score., Calculate Flesch-Kincaid Grade Level., Extract top N keywords using TF-IDF approximation., Extracts text statistics features., Initialize with optional tokenizer for exact token counts.          Args:, Extract text statistics features.          Args:             text: Input text to, Calculate Yule's K statistic for vocabulary richness. (+5 more)

### Community 288 - "RelevanceScorer"
Cohesion: 0.15
Nodes (14): default_batch_score(), ABC, Base protocol for relevance scoring in Headroom SDK.  This module defines the Re, Relevance score with explainability.      Attributes:         score: Relevance s, Clamp score to valid range., Abstract base class for relevance scoring.      All relevance scorers must imple, Score a single item's relevance to the context.          Args:             item:, Check if this scorer is available (dependencies installed).          Override in (+6 more)

### Community 289 - "SharedContext"
Cohesion: 0.11
Nodes (13): ContextEntry, SharedContext — compressed inter-agent context sharing.  When agents hand off to, Get content by key.          Args:             key: The key to retrieve., Get the full ContextEntry with metadata., List all non-expired keys., Get aggregated stats., Evict expired and oldest entries if at capacity. Lock must be held.          ``i, A stored context entry with original and compressed versions. (+5 more)

### Community 290 - "pr-governance.py"
Cohesion: 0.19
Nodes (21): checked_items(), emit_outputs(), extract_sections(), GovernanceReport, has_descriptive_text(), has_non_placeholder_bullets(), has_test_output(), load_event() (+13 more)

### Community 291 - "Universal Compression"
Cohesion: 0.09
Nodes (23): Batch Compression, CCR Integration, Code Handler, Compression Result, Configuration, Configuration Options, Content Handlers, Custom Handlers (+15 more)

### Community 292 - "ws_handler"
Cohesion: 0.15
Nodes (20): AxMsg, ax_to_tg(), build_upstream_ws_url(), IntoResponseBody, Body, HeaderMap, Option, Request (+12 more)

### Community 293 - ".new"
Cohesion: 0.18
Nodes (10): Bound, build_crush_array_dict(), detect_content_type(), keyword_registry_snapshot(), PyDetectionResult, PySearchCompressor, PyDict, Python (+2 more)

### Community 294 - "LegacyMutexStore"
Cohesion: 0.17
Nodes (17): bench_get_single_threaded(), bench_mixed_multi_threaded(), bench_put_single_threaded(), LegacyEntry, LegacyInner, LegacyMutexStore, Arc, Criterion (+9 more)

### Community 295 - ".for_mode"
Cohesion: 0.18
Nodes (16): break_even_reads_matches_research_anchor(), CompressionPolicy, max_lossy_ratio_in_unit_interval(), net_gain_big_shave_shallow_suffix_is_win(), net_gain_clamps_out_of_range_inputs(), net_gain_cold_cache_ignores_suffix(), net_gain_guards_nan_inputs(), net_gain_no_suffix_edit_profitable_with_reads_remaining() (+8 more)

### Community 296 - "estimator.rs"
Cohesion: 0.14
Nodes (16): backend_is_estimation(), claude_density_matches_python(), default_is_four_chars_per_token(), deterministic(), empty_string_is_zero(), EstimatingCounter, min_is_one_for_non_empty_input(), rejects_negative_density() (+8 more)

### Community 297 - ".new"
Cohesion: 0.10
Nodes (30): ccr_marker_emitted_when_thresholds_clear(), ccr_skipped_when_below_min_matches(), ccr_skipped_when_disabled(), cjk_bigrams(), cjk_bigrams_from_runs(), empty_input_returns_unchanged(), FileMatches, hash_u64() (+22 more)

### Community 298 - "CompactionStage"
Cohesion: 0.13
Nodes (13): Formatter, Send, Sync, CompactionStage, Arc, Box, Debug, Option (+5 more)

### Community 299 - "traits.rs"
Cohesion: 0.10
Nodes (19): MarkerObserver, AtomicUsize, tracing_observer_does_not_panic_on_event(), TracingObserver, AlwaysKeepFirst, constraint_handles_empty_input(), constraint_returns_indices_in_bounds(), CountingObserver (+11 more)

### Community 300 - "integration_bedrock_invoke.rs"
Cohesion: 0.21
Nodes (21): assert_byte_equal_sha256(), bedrock_proxy(), CapturedRequest, document_block_preserved(), mount_capture_invoke(), native_envelope_round_trip_byte_equal(), redacted_thinking_preserved(), Capture (+13 more)

### Community 301 - "configuration.mdx"
Cohesion: 0.09
Nodes (21): CacheAligner Configuration, CLI Context Tool, Command Line Options, Configuration Precedence, Context Window Management, Custom Model Configuration, Environment Variables, Feature Flags (+13 more)

### Community 302 - "Proxy-wide (Phase G PR-G3)"
Cohesion: 0.09
Nodes (21): Bedrock route (Phase D PR-D3), C2 alarm wiring, Cache + compression, Cache-safety alarm, Cardinality discipline, H1 per-strategy ratio wiring, H2 aborted-stream gate, H3 force-zero (+13 more)

### Community 303 - "Memory"
Cohesion: 0.11
Nodes (27): get_lean_ctx_path(), is_lean_ctx_installed(), _managed_lean_ctx_candidates(), Path, lean-ctx integration for Headroom.  lean-ctx configures supported coding agents, Return known Headroom-managed lean-ctx binary paths., Get path to lean-ctx binary — check PATH first, then ~/.headroom/bin/., Check if lean-ctx is available. (+19 more)

### Community 304 - "HybridScorer"
Cohesion: 0.10
Nodes (16): HybridScorer, BM25Scorer, EmbeddingScorer, RelevanceScore, RelevanceScorer, Check if embedding scoring is available.          Returns:             True if s, Compute adaptive alpha based on query characteristics.          Higher alpha = m, Score item using hybrid BM25 + embedding fusion.          Args:             item (+8 more)

### Community 305 - "FileSystemTOINBackend"
Cohesion: 0.11
Nodes (14): Any, Protocol, Base protocol for TOIN storage backends.  This protocol defines the minimal inte, Protocol for TOIN storage backends.      Implementations can use any storage mec, Load serialized TOIN data.          Returns:             Dict with TOIN data (as, Save serialized TOIN data.          The implementation must ensure atomicity — a, TOINBackend, FileSystemTOINBackend (+6 more)

### Community 306 - "Benchmarks"
Cohesion: 0.09
Nodes (21): Accuracy Benchmarks, Benchmarks, Compression Performance, Compression Rate, Compression Ratio, Fleet Summary, HTML Extraction, JSON Compression (SmartCrusher) (+13 more)

### Community 307 - "Headroom Learn"
Cohesion: 0.09
Nodes (22): 1. Environment Facts → CLAUDE.md, 2. File Path Corrections → CLAUDE.md, 3. Search Scope → CLAUDE.md, 4. Command Patterns → CLAUDE.md, 5. Known Large Files → CLAUDE.md, 6. Retry Prevention → MEMORY.md, 7. Permission Notes → MEMORY.md, Adding Support for a New Agent (+14 more)

### Community 308 - "responses_items.rs"
Cohesion: 0.21
Nodes (20): Cow, ApplyPatchOperation, ClassifiedItem, classify_items(), classify_message_with_phase(), ClassifyError, function_call_arguments_string(), is_output_item_correct() (+12 more)

### Community 309 - ".new"
Cohesion: 0.19
Nodes (15): default_batch_calls_score_per_item(), default_batch_score(), empty_score_zero_with_reason(), relevance_score_clamps_above_one(), relevance_score_clamps_below_zero(), relevance_score_passes_through_valid_range(), RelevanceScore, RelevanceScorer (+7 more)

### Community 310 - "LiveZoneOutcome"
Cohesion: 0.18
Nodes (19): LiveZoneOutcome, Box, above_threshold_compression_attempted(), below_threshold_no_compression_attempted(), body_of(), body_with_tool_result(), dispatch(), first_tool_result_action() (+11 more)

### Community 311 - "LogCompressor"
Cohesion: 0.20
Nodes (10): ccr_marker_emitted_when_thresholds_clear(), LogCompressionResult, LogCompressorConfig, LogCompressorStats, md5_hex_24(), BTreeMap, Default, Option (+2 more)

### Community 312 - "unidiff_detector.rs"
Cohesion: 0.11
Nodes (5): detect_diff(), is_diff(), ContentType, Option, truncated_diff_treated_consistently()

### Community 313 - "openai_chat.rs"
Cohesion: 0.20
Nodes (17): apply_tool_call_delta(), ChoiceState, ChunkState, parse_json(), payload_preview(), Bytes, Error, HashMap (+9 more)

### Community 314 - "handle_vertex_predict_dispatch"
Cohesion: 0.12
Nodes (14): handle_vertex_predict_dispatch(), Body, ConnectInfo, HeaderMap, Method, Option, Path, Self (+6 more)

### Community 315 - "integration_cache_control.rs"
Cohesion: 0.10
Nodes (12): resolve_frozen_count(), Value, buffer(), cache_control_ttl_5m_before_1h_warns_and_passes(), CaptureWriter, Arc, MakeWriter, Result (+4 more)

### Community 316 - "CaptureWriter"
Cohesion: 0.15
Nodes (17): anthropic_payload(), buffer(), cache_drift_observed_when_system_prompt_changes_mid_session(), CaptureWriter, mount_anthropic_capture_all(), Arc, MakeWriter, MockServer (+9 more)

### Community 317 - "integration_metrics.rs"
Cohesion: 0.21
Nodes (19): record_passthrough_bytes_modified(), anthropic_simple_non_stream_upstream(), anthropic_streaming_upstream(), cache_hit_rate_emitted_per_session(), compression_ratio_emitted_per_strategy(), compression_ratio_per_strategy_does_not_replicate_aggregate(), find_value_with_labels(), incomplete_status_logged_with_reason() (+11 more)

### Community 318 - "HeadroomCallback"
Cohesion: 0.13
Nodes (12): _CustomLogger, HeadroomCallback, Any, LiteLLM callback — add Headroom compression to LiteLLM with one line.      # Loc, Called by LiteLLM before each API call. Compresses messages., Compress locally using headroom.compress()., Compress via Headroom Cloud API (managed CCR, TOIN, analytics)., Called after successful completion. No-op for now. (+4 more)

### Community 319 - "_start_proxy"
Cohesion: 0.04
Nodes (48): InMemoryGraphStore, Entity, Any, Enum, Graph data models for Headroom's knowledge graph memory system.  Provides Entity, Convert to dictionary for serialization., Create from dictionary., A subset of the knowledge graph containing entities and their relationships. (+40 more)

### Community 320 - "_optimize_content_block"
Cohesion: 0.14
Nodes (18): estimate_anthropic_tokens(), estimate_openai_tokens(), find_optimal_anthropic_dimensions(), find_optimal_openai_dimensions(), _optimize_content_block(), optimize_images_in_messages(), Any, Tile-boundary image optimizer — reduce vision tokens with zero quality loss.  Re (+10 more)

### Community 321 - "Any"
Cohesion: 0.03
Nodes (66): MemoryBackend, MemorySystem, Any, Memory, Protocol, MemorySystem orchestrator for LLM-driven memory operations.  This module provide, Delete a memory from the backend.          Args:             memory_id: ID of th, Retrieve a specific memory by ID.          Args:             memory_id: The memo (+58 more)

### Community 322 - "MemorySystem"
Cohesion: 0.07
Nodes (29): _build_tool_name_index(), _format_smart_crush_transform(), Tokenizer, Map tool_call_id/tool_use_id → tool name across OpenAI + Anthropic formats., Transform-protocol entry point. Walks every tool/tool_result         message, ap, Format ``smart_crush:<count>[:<name1,name2,...>]``.      Names are included when, compute_hash(), compute_messages_hash() (+21 more)

### Community 323 - "AgentWriter"
Cohesion: 0.11
Nodes (23): AgentWriter, ExportResult, MemoryEntry, ABC, Base class and shared utilities for agent-native memory writers.  Writers conver, A memory entry to be written to an agent's file.      Simplified view of Hierarc, Combined score for ranking: importance × recency × access., Result of a memory export operation. (+15 more)

### Community 324 - "ssl_context.py"
Cohesion: 0.17
Nodes (20): _additive_ca_context(), apply_global_tls_relaxation(), build_httpx_verify(), _clear_x509_strict(), _default_strict_relaxed_context(), find_ca_bundle(), SSL context builder for the Headroom upstream httpx client.  Respects the standa, Build an additive trust-store context from a CA bundle path. (+12 more)

### Community 325 - "2.2 The cache-safety invariants (every PR enforces)"
Cohesion: 0.10
Nodes (20): 02 — Realigned Target Architecture, 2.1 Request lifecycle (Rust, post-Phase-C), 2.2 The cache-safety invariants (every PR enforces), 2.3 The compressor module layout (post-Phase-B), 2.4 The auth-mode policy matrix (Phase F), 2.5 Preserved primitives detail, 2.6 What this architecture explicitly does NOT do, CCR (post-Phase-B-PR-B7) (+12 more)

### Community 326 - "replay_codex_ws_load.py"
Cohesion: 0.18
Nodes (20): boot_proxy(), Frame, FrameResult, main(), _parse_kv(), parse_log(), _percentile(), print_report() (+12 more)

### Community 327 - "version-sync.py"
Cohesion: 0.18
Nodes (20): bump_version(), get_version_from_pyproject(), main(), Path, Update pyproject.toml version., Write .releasemetadata JSON file., Read version from pyproject.toml., Bump version according to bump_type (major, minor, patch). (+12 more)

### Community 328 - "MCP Server — Context Engineering Toolkit"
Cohesion: 0.10
Nodes (21): Architecture, Claude doesn't see headroom tools, CLI Commands, Cross-Tool Compatibility, Debug, "Entry not found or expired", headroom_compress, headroom_retrieve (+13 more)

### Community 329 - "fix: Codex proxy resilience under reconnect storms"
Cohesion: 0.10
Nodes (20): Context & Research, Deferred to Implementation, Deferred to Separate Tasks, Documentation / Operational Notes, External References, fix: Codex proxy resilience under reconnect storms, High-Level Technical Design, Implementation Units (+12 more)

### Community 330 - "SDK Guide"
Cohesion: 0.09
Nodes (21): Advanced Configuration, Anthropic, Audit, Check Stats, Comparison with Proxy, Enable Logging, Error Handling, Google (+13 more)

### Community 331 - "tool_def_normalize.rs"
Cohesion: 0.18
Nodes (17): any_tool_has_cache_control(), byte_stable_across_runs(), does_not_alter_arrays_within_arrays(), handles_deeply_nested_schemas(), idempotent_resort_no_change(), idempotent_resort_schema(), preserves_array_order_in_oneof(), String (+9 more)

### Community 332 - "live_zone_responses.rs"
Cohesion: 0.25
Nodes (15): body_of(), compress_openai_responses_request(), e1_passes_through_when_oauth(), e1_sorts_tools_when_payg(), invalid_json_passthrough(), log_item_telemetry(), mode_off_short_circuits(), no_input_passthrough() (+7 more)

### Community 333 - "forward_vertex_request"
Cohesion: 0.14
Nodes (18): error_response(), forward_vertex_request(), Body, Bytes, HeaderMap, Method, Receiver, SocketAddr (+10 more)

### Community 334 - "integration_bedrock_authmode.rs"
Cohesion: 0.15
Nodes (18): bedrock_proxy(), CapturedRequest, mount_capture_invoke(), oauth_policy_passthrough_prefer(), _pin(), Body, Bytes, Capture (+10 more)

### Community 335 - "mount_capture"
Cohesion: 0.08
Nodes (15): HeadroomCallbackHandler, BaseCallbackHandler, BaseException, UUID, LangChain callback handler for Headroom metrics and observability.      NOTE: Ca, Initialize callback handler.          Args:             log_level: Logging level, Total tokens used across all requests., Total number of requests tracked. (+7 more)

### Community 336 - "integration_e4_openai_cache_key.rs"
Cohesion: 0.26
Nodes (19): assert_byte_equal(), captured_body(), mount_chat_capture(), mount_responses_capture(), oauth_chat_completions_no_injection_byte_equal(), oauth_responses_no_injection_byte_equal(), parse_json(), payg_chat_completions_injects_prompt_cache_key() (+11 more)

### Community 337 - "bundle.py"
Cohesion: 0.18
Nodes (9): _MemoryAPI, Memory, Direct API for memory operations., Run async coroutine in sync context., Semantic search for memories.          Args:             query: Search query, Manually add a memory.          Args:             content: Memory content, Get all memories for this user., Clear all memories for this user. (+1 more)

### Community 338 - "prepare_outbound_body_bytes"
Cohesion: 0.08
Nodes (24): Mem0Backend, Any, Memory, Initialize the Mem0 backend.          Args:             config: Configuration fo, Ensure Mem0 client is initialized.          Returns:             The initialized, Convert Memory object to Mem0 metadata dict.          Args:             memory:, Convert Mem0 result dict to Memory object.          Args:             result: Th, Build Mem0 filter dict from MemoryFilter or VectorFilter.          Args: (+16 more)

### Community 339 - "cost.py"
Cohesion: 0.32
Nodes (10): AnchorSelector, Arc, Box, Option, RelevanceScorer, Self, Send, SmartCrusherConfig (+2 more)

### Community 340 - "WindowTokens"
Cohesion: 0.16
Nodes (19): Token breakdown from Claude transcript JSONL files for one time window., WindowTokens, _add_usage_to_tokens(), _claude_config_dir(), compute_window_tokens(), find_transcript_files(), get_model_weight(), Any (+11 more)

### Community 341 - "Error Handling"
Cohesion: 0.10
Nodes (19): 1. Catch Specific Exceptions, 2. Let StorageError Pass, 3. Validate on Startup, Best Practices, Check Stats After Error, CompressionError, ConfigurationError, Debugging (+11 more)

### Community 342 - "CompressionMiddleware"
Cohesion: 0.13
Nodes (12): ASGIApp, CompressionMiddleware, Any, Receive, Scope, Send, ASGI Middleware — add Headroom compression to any Python proxy.  Drop-in middlew, Compress locally using headroom.compress(). (+4 more)

### Community 343 - "e2e_real.rs"
Cohesion: 0.27
Nodes (15): Child, e2e_anthropic_non_streaming(), e2e_anthropic_streaming(), e2e_enabled(), e2e_health_through_full_chain(), e2e_openai_non_streaming(), e2e_request_id_propagates(), load_dotenv() (+7 more)

### Community 344 - "SqliteCcrStore"
Cohesion: 0.15
Nodes (10): AsRef, Connection, Mutex, Option, Path, PathBuf, Result, Self (+2 more)

### Community 345 - "log_compressor.rs"
Cohesion: 0.15
Nodes (23): cmp(), dedupe_collapses_genuinely_repeated_warnings(), detects_cargo_format(), detects_generic_for_unrecognised_input(), detects_jest_format(), detects_make_format(), detects_npm_format(), detects_pytest_format() (+15 more)

### Community 346 - "auth_mode.rs"
Cohesion: 0.19
Nodes (17): anthropic_cli_ua_classified_subscription(), anthropic_x_api_key_classified_payg(), antigravity_ua_classified_subscription(), api_key_classified_payg(), bedrock_no_auth_classified_oauth(), classify_under_10us_per_call(), claude_code_ua_classified_subscription(), copilot_ua_classified_subscription() (+9 more)

### Community 347 - "envelope.rs"
Cohesion: 0.19
Nodes (16): anthropic_version_not_string_errors(), BedrockEnvelope, ensure_first_no_op_when_already_first(), ensure_first_reorders_when_not_first(), EnvelopeError, invalid_json_errors(), missing_anthropic_version_errors(), ModelPath (+8 more)

### Community 348 - "toin_publish.py"
Cohesion: 0.11
Nodes (21): assetsDir, __dirname, flags, openClawDir, positional, quoteCmdArg(), rawArgs, readJson() (+13 more)

### Community 349 - "is_copilot_api_url"
Cohesion: 0.09
Nodes (18): Read shared events within the session time window, pruning old entries., _read_shared_events(), _aggregate_mcp_events(), build_prefix_cache_stats(), build_session_summary(), _get_litellm_module(), Any, CostTracker (+10 more)

### Community 350 - "BaselineModel"
Cohesion: 0.12
Nodes (8): _Accum, BaselineModel, Per-stratum baseline of unshaped output tokens (the synthetic control).      Bui, Fold another baseline's observations into this one.          Per-stratum and glo, Return ``(mean, var, n)`` for *key* with hierarchical back-off.          Falls b, Running count / sum / sum-of-squares for online mean & variance., Sample variance (unbiased). 0 when fewer than 2 observations., Fold another accumulator's observations into this one.          n / sum / sumsq

### Community 351 - ".count_messages"
Cohesion: 0.16
Nodes (10): Any, Count tokens in multi-part content.          Handles both Anthropic format ({"ty, Count tokens for a non-string content blob.          Small blobs are counted exa, Estimate tokens for an image using Anthropic's formula: (w*h)/750.          Trie, Count tokens in tool calls., Count tokens in legacy function call., Count tokens in a list of chat messages.          Args:             messages: Li, Count tokens in a text string. Must be implemented by subclasses. (+2 more)

### Community 352 - "resolve_policy"
Cohesion: 0.16
Nodes (15): CompressionPolicy, is_enforcement_enabled(), policy_default_payg(), policy_for_mode(), AuthMode, Per-auth-mode compression policy — Phase F PR-F2.1, extended in F2.2 (Python par, Net gain (in plain-input-token cost units) of a mutation that         removes ``, Decision form of :meth:`net_mutation_gain`: mutate iff the         gain is stric (+7 more)

### Community 353 - "Integration Guide"
Cohesion: 0.11
Nodes (19): Agno, ASGI Middleware, compress() Function, Compression Hooks (Advanced), FAQ, Integration Guide, LangChain, LiteLLM (+11 more)

### Community 354 - "TurnContext"
Cohesion: 0.15
Nodes (19): Internal implementation of simulate., _build_waste_histogram(), _generate_recommendations(), generate_report(), _get_jinja2_template(), _get_top_waste_requests(), Any, datetime (+11 more)

### Community 355 - ".apply"
Cohesion: 0.18
Nodes (13): already_compact_yields_zero_savings(), empty_input_skipped(), invalid_json_errors_with_invalid_input(), JsonMinifier, minifier_never_grows_output(), nested_structure_round_trips_semantically(), pretty_array_minifies(), pretty_object_minifies() (+5 more)

### Community 356 - "sigv4.rs"
Cohesion: 0.25
Nodes (16): changing_body_changes_signature(), changing_region_changes_signature(), fixed_time(), fixture_credentials(), Credentials, Result, String, SystemTime (+8 more)

### Community 357 - "handle_responses"
Cohesion: 0.15
Nodes (12): accepts_sse(), extract_request_service_tier(), handle_responses(), Bytes, ConnectInfo, HeaderMap, Method, Option (+4 more)

### Community 358 - "integration_bedrock_streaming.rs"
Cohesion: 0.26
Nodes (17): bedrock_proxy(), client_can_choose_eventstream_or_sse(), converse_stream_route_translates_to_sse(), eventstream_crc_mismatch_surfaces_structured_error(), eventstream_parses_correctly(), eventstream_parses_correctly_one_byte_at_a_time(), eventstream_translated_to_sse(), eventstream_validation_off_accepts_corrupt() (+9 more)

### Community 359 - "integration_chat_completions.rs"
Cohesion: 0.19
Nodes (15): assert_byte_equal_sha256(), compressible_tool_array_payload(), mount_capture(), n_greater_than_one_passthrough(), passthrough_no_compression_byte_equal(), Arc, MockServer, Mutex (+7 more)

### Community 360 - "CaptureWriter"
Cohesion: 0.17
Nodes (14): buffer(), CaptureWriter, mount_anthropic_capture(), Arc, MakeWriter, MockServer, Mutex, Option (+6 more)

### Community 361 - "config.rs"
Cohesion: 0.24
Nodes (16): ConfigError, ConfiguredResponse, JsonPointerMatch, load_config(), BTreeMap, Error, Option, Path (+8 more)

### Community 362 - "CacheOptimizerRegistry"
Cohesion: 0.21
Nodes (7): CCSwitchReconciler, Path, cc-switch reconciler: keep Headroom in the request path without fighting cc-swit, One reconcile pass. Returns True if it rewrote settings.json., Polls Claude settings.json and keeps Headroom in the path (see module docstring), _route_official(), _settings_path()

### Community 363 - "tools.py"
Cohesion: 0.10
Nodes (22): Headroom CLI - Command-line interface for memory and proxy management.  The subc, main(), Context, Allow running CLI with python -m headroom.cli., Headroom - The Context Optimization Layer for LLM Applications.      Manage memo, diff_cmd(), _exec_tool(), _is_windows() (+14 more)

### Community 364 - "prometheus_metrics.py"
Cohesion: 0.11
Nodes (49): _asset_for_platform(), _binary_name(), BinaryError, BinaryFetchError, cache_dir(), _cached_path(), detect_platform(), _download() (+41 more)

### Community 365 - "MemoryBudgetManager"
Cohesion: 0.10
Nodes (17): BudgetConfig, BudgetReport, MemoryBudgetManager, Path, Memory file budget manager — token-optimized memory file maintenance.  Manages t, Apply temporal decay to importance scores., Separate fresh memories from stale ones.          A memory is stale if it refere, Check if a memory references entities that no longer exist. (+9 more)

### Community 366 - "MemoryTracker"
Cohesion: 0.03
Nodes (49): Get memory statistics for the MemoryTracker.          Thread-safe: takes a snaps, Get memory statistics for the MemoryTracker.          Returns:             Compo, Get memory statistics for the MemoryTracker.          Returns:             Compo, ComponentStats, estimate_object_size(), MemoryReport, MemoryTracker, ProcessStats (+41 more)

### Community 367 - "MemoryQuery"
Cohesion: 0.16
Nodes (14): MemoryQuery, _append_anthropic_tool_results(), _assistant_text(), extract_memory_query_sources(), Any, Pure policy helpers for building memory retrieval queries., Concatenate memory query sources into a delimited embedding input., Extract user, tool, and assistant sources from chat-style messages.      Returns (+6 more)

### Community 368 - "rate_limiter.py"
Cohesion: 0.13
Nodes (17): create_streamable_http_app(), create_streamable_http_session_manager(), _normalize_path(), Any, Receive, Scope, Send, Streamable HTTP transport helpers for the Headroom MCP server. (+9 more)

### Community 369 - "LogLine"
Cohesion: 0.12
Nodes (17): count_level(), LevelClassifier, LogCompressor, LogLevel, LogLine, Into, Self, Vec (+9 more)

### Community 370 - "integration_bedrock_metrics.rs"
Cohesion: 0.13
Nodes (24): _config_ref(), ProxyHandle, Arc, JoinHandle, Option, Sender, SocketAddr, String (+16 more)

### Community 371 - "mdx.tsx"
Cohesion: 0.25
Nodes (14): CommunityCharts(), CommunityStatsHeader(), LiveStats(), FrameworkIntegrations(), KeyFeatures(), generator, getMDXComponents(), MDXProvidedComponents (+6 more)

### Community 372 - "docker-install.mdx"
Cohesion: 0.12
Nodes (16): Docker Compose support, Environment passthrough, How the wrapper behaves, Linux, macOS (bash 4.3+), macOS / Linux, Native Headroom commands, Next steps (+8 more)

### Community 373 - "metrics.mdx"
Cohesion: 0.12
Nodes (16): Budget Alerts, Compression Result Metrics, Cost Tracking, Grafana Dashboard, Health Check, Historical Metrics, Historical Savings, Key Metrics to Monitor (+8 more)

### Community 374 - "inject_memory_instruction"
Cohesion: 0.18
Nodes (13): inject_memory_instruction(), InlineMemoryWrapper, parse_response_with_memory(), ParsedResponse, Any, Inline memory extraction - zero extra latency.  Instead of making a separate LLM, Parse LLM response to extract memories.      Args:         response_text: Raw LL, Wrapper that extracts memories from LLM responses inline.      This is the zero- (+5 more)

### Community 375 - ".count_message"
Cohesion: 0.13
Nodes (17): CachePrefixMetrics, Detailed cache prefix metrics for debugging cache misses.      Log these per-req, align_for_cache(), CacheAligner, detect_volatile_content(), Any, Tokenizer, Split content into whitespace-delimited tokens for inspection.      No regex. `` (+9 more)

### Community 376 - "astgrep.py"
Cohesion: 0.22
Nodes (13): AstGrepReadOutline, _build_outline(), _detect_lang_from_input(), _min_chars_to_rewrite(), _path_from_input(), Any, Path, ast-grep interceptor: replace verbose Read outputs with function-level outlines. (+5 more)

### Community 377 - "tracker.py"
Cohesion: 0.13
Nodes (10): GeminiPlugin, Path, Scan all Gemini session files for a project.          ``include_subagents`` is a, Parse a single Gemini session file (JSON or JSONL)., Parse a Gemini JSON session file., Parse a Gemini JSONL session file., Reads Google Gemini CLI session logs from ~/.gemini/tmp/<project>/chats/.      G, Try to detect the project path from a session file. (+2 more)

### Community 378 - "INDEX.md"
Cohesion: 0.14
Nodes (14): ImageCompressionDecision, Any, ``ImageCompressionDecision``: canonical "should this request have images compres, Stamp the skip reason into a tags dict for dashboard slicing.          Mutates `, Immutable, value-equal snapshot of the image-compression gate.      Construction, Compute the canonical image-compression decision.          Parameters         --, apply_image_skip_reason(), decide_image_compression() (+6 more)

### Community 379 - "12 — Decisions Needed"
Cohesion: 0.12
Nodes (17): 12 — Decisions Needed, Q10. Bedrock/Vertex priority — parallel with proxy port (Phase D in calendar) or after Phase H?, Q11. Memory subsystem — auto-tail mode default, or tool-only?, Q12. Parity harness post-Phase-H — keep or delete?, Q13. Auth-mode UA detection list — which CLIs to recognize?, Q14. The ICM removal blast radius — confirm acceptable, Q15. Calendar + capacity — sequential or parallel?, Q1. Phase A timing — land tonight or wait? (+9 more)

### Community 380 - "test_version_sync.py"
Cohesion: 0.16
Nodes (16): Path, Tests for version-sync.py., Create a temporary project with all versioned files., Test --bump patch bumps 0.5.25 to 0.5.26., Test --bump minor bumps 0.5.25 to 0.6.0., Test --bump major bumps 0.5.25 to 1.0.0., Test .releasemetadata is written correctly., Test plugin-only sync leaves canonical package versions alone. (+8 more)

### Community 381 - "Docker-Native Install"
Cohesion: 0.12
Nodes (17): Docker Compose support, Docker-Native Install, Environment passthrough, `HEADROOM_WORKSPACE` vs `HEADROOM_WORKSPACE_DIR`, How the wrapper behaves, Linux, macOS (bash 4.3+), macOS / Linux (+9 more)

### Community 382 - "API"
Cohesion: 0.12
Nodes (16): Any Framework, API, `clear()`, Configuration, CrewAI, Framework Examples, `get_entry(key)`, `get(key, *, full=False)` (+8 more)

### Community 383 - "detection.rs"
Cohesion: 0.20
Nodes (11): build_log_output_routes_via_chain(), chain_is_deterministic_across_repeated_calls(), detect(), grep_search_results_route_to_plain_text_per_locked_design(), html_routes_via_tier_1(), json_array_routes_via_tier_1(), magika_available(), ContentType (+3 more)

### Community 384 - "integration_responses_streaming.rs"
Cohesion: 0.23
Nodes (15): assert_byte_equal(), responses_sse_upstream(), Arc, JoinHandle, Mutex, Option, SocketAddr, String (+7 more)

### Community 385 - "mcp.mdx"
Cohesion: 0.12
Nodes (15): Architecture, Claude Code `/usage` attributes a large share to `headroom` MCP, CLI commands, `command: "headroom"` fails to start, Cross-tool compatibility, headroom_compress, headroom_retrieve, headroom_stats (+7 more)

### Community 386 - "persistent-installs.mdx"
Cohesion: 0.12
Nodes (16): Claude Code VSCode extension caveat, Command surface, Configuration scopes, Docker-native relationship, Health and wrap behavior, Persistent Docker, Persistent service on the local machine, Persistent watchdog task (+8 more)

### Community 387 - "BatchContextStore"
Cohesion: 0.18
Nodes (13): compute_anthropic_session_hit_rate(), compute_hit_rate(), h2_completed_anthropic_stream_returns_rate(), histogram(), hit_rate_one_when_all_reads_are_cache_hits(), hit_rate_split_three_ways(), hit_rate_zero_when_no_cache_reads(), observe() (+5 more)

### Community 388 - "tokensave_installer.py"
Cohesion: 0.19
Nodes (15): _ensure_tokensave_binary(), Resolve the tokensave binary, fetching the release asset if missing.      Return, _detect_asset(), download_tokensave(), ensure_tokensave(), get_tokensave_path(), _pinned_version(), Path (+7 more)

### Community 389 - "_MemoryAPI"
Cohesion: 0.25
Nodes (17): eventstream_counter(), eventstream_counter_records_event_type_label(), handle_metrics(), invoke_counter(), invoke_counter_advertises_metric_in_scrape(), invoke_increment_appears_with_labels(), invoke_latency(), latency_histogram_records_observation() (+9 more)

### Community 390 - "MemoryToolsCompletions"
Cohesion: 0.12
Nodes (23): Codex-specific provider helpers., build_launch_env(), CodexRoutingDecision, decode_openai_bearer_payload(), Any, Runtime helpers for Codex/OpenAI-facing integrations., Resolved Codex routing headers and whether they target ChatGPT auth., Build environment variables for Codex through the local proxy. (+15 more)

### Community 391 - "config.py"
Cohesion: 0.13
Nodes (13): get_default_embedding_dim(), get_default_embedding_model(), get_default_siglip_model(), get_default_spacy_model(), MLModelConfig, Central configuration for all ML models used in Headroom.  This is the SINGLE SO, Get total estimated memory if all configured models are loaded.          Returns, Get the default sentence transformer model name. (+5 more)

### Community 392 - "install.py"
Cohesion: 0.06
Nodes (40): Aider-specific provider helpers., build_install_env(), Aider install-time helpers., Build the persistent install environment for Aider., build_launch_env(), Runtime helpers for Aider integrations., Build environment variables for Aider through the local proxy.      ``project``, apply_provider_scope() (+32 more)

### Community 393 - "verbosity_controller.py"
Cohesion: 0.19
Nodes (12): ControllerState, load_state(), Enum, Path, AIMD controller for live verbosity adjustment.  The offline ``learn --verbosity`, An abstract feedback signal about the last response's verbosity., Per-conversation (or per-project) controller state., Pure AIMD controller. ``observe`` maps (state, signal) → new state. (+4 more)

### Community 394 - "BM25Scorer"
Cohesion: 0.17
Nodes (10): BM25Scorer, RelevanceScore, RelevanceScorer, Compute inverse document frequency.          Uses the standard BM25 IDF formula:, Compute BM25 score between document and query.          Args:             doc_to, Score item relevance to context using BM25.          Args:             item: Ite, Score multiple items.          BM25 is fast enough that sequential scoring is ef, BM25 keyword relevance scorer.      Zero dependencies, instant execution. Excell (+2 more)

### Community 395 - "headroom-sbom-all-extra.cdx.json"
Cohesion: 0.12
Nodes (15): bomFormat, bom-ref, name, type, version, components, metadata, component (+7 more)

### Community 396 - "test_sync_plugin_versions.py"
Cohesion: 0.18
Nodes (15): _load_module(), Tests for sync-plugin-versions.py., On ``main``, sync runs without needing the env var., On any non-main branch without the env var, sync is a no-op., Defensive: if ``_current_branch`` returns None (git not on     PATH, detached HE, Locks the sync-execution path. ``_should_sync`` is forced True so     we don't d, Locks the branch-aware contract: when ``_should_sync`` returns     False (featur, ``HEADROOM_SYNC_VERSIONS=1`` forces a sync even on feature     branches — the re (+7 more)

### Community 397 - "Persistent Installs"
Cohesion: 0.12
Nodes (16): Command surface, Configuration scopes, Docker-native relationship, Health and wrap behavior, Persistent Docker, Persistent Installs, Persistent service on the local machine, Persistent watchdog task (+8 more)

### Community 398 - "TypeScript SDK"
Cohesion: 0.12
Nodes (16): Anthropic SDK, Comparison with Python SDK, Core API: `compress()`, Environment Variables, Error Handling, Fallback Behavior, Framework Adapters, How It Works (+8 more)

### Community 399 - "classifier.rs"
Cohesion: 0.15
Nodes (3): ArrayType, classify_array(), Value

### Community 400 - "start"
Cohesion: 0.25
Nodes (12): bedrock_stream_can_emit_binary_eventstream(), configured_stub_overrides_default_response(), openai_chat_default_is_provider_shaped(), responses_stream_returns_named_sse_events(), JoinHandle, Option, Sender, SocketAddr (+4 more)

### Community 401 - "community-charts.tsx"
Cohesion: 0.25
Nodes (13): AreaChartSection(), BarChartSection(), CustomTooltip(), DATA, DataTable(), fmt(), fmtDateDaily(), fmtDateHourly() (+5 more)

### Community 402 - "benchmarks.mdx"
Cohesion: 0.13
Nodes (14): Accuracy Benchmarks, Compression Performance, Compression Rate, Cost-Benefit Analysis, Fleet Summary, HTML Extraction, JSON Compression (SmartCrusher), Latency Overhead (+6 more)

### Community 403 - "limitations.mdx"
Cohesion: 0.13
Nodes (14): Adaptive K: How Item Retention Works, Code Compression, Configuration Tuning, Edge Cases, JSON Compression Constraints, Provider Interactions, Safety Gates, TOIN Cold Start (+6 more)

### Community 404 - "opencode.mdx"
Cohesion: 0.13
Nodes (14): Environment Variables, Failure Learning, How future installers should find or produce the artifact, How It Works Under The Hood, Native OpenCode Plugin, Options, Persistent Installs, Plugin Artifact Contract (+6 more)

### Community 405 - "OpenCodePlugin"
Cohesion: 0.20
Nodes (6): OpenCodePlugin, Connection, Path, Scan all sessions for a project and return normalized tool calls., Read OpenCode sessions from the SQLite database.      OpenCode stores all conver, Discover all projects that have at least one session.

### Community 406 - "compression_summary.py"
Cohesion: 0.18
Nodes (14): _categorize_by_fields(), _common_keys(), _extract_name_from_signature(), _find_notable_items(), _item_key(), Counter, Compression summary generator — describes what was dropped.  When content is com, Create a hashable key for an item (for dropped detection without id()). (+6 more)

### Community 407 - "P5 — Auth-mode + observability + fingerprinting"
Cohesion: 0.13
Nodes (15): P5-49. `X-Headroom-*` request headers leak upstream, P5-50. `anthropic-beta` mutated when memory enabled, not session-sticky, P5-51. `OpenAI-Beta` auto-injection on WS path, P5-52. `accept-encoding` stripped — fingerprint signal, P5-53. `X-Forwarded-*` always added by Rust proxy, P5-54. Subscription tracker stores raw OAuth bearer token in process memory, P5-55. Auth-mode never drives compression policy, P5-56. TOIN aggregates globally by `structure_hash` only (+7 more)

### Community 408 - "Headroom Limitations & Known Behavior"
Cohesion: 0.13
Nodes (15): Adaptive K: How Item Retention Works, CacheAligner Behavior, Code Compression, Configuration Tuning, Edge cases, Error Handling, Headroom Limitations & Known Behavior, JSON Compression Constraints (+7 more)

### Community 409 - "Text Compression Utilities"
Cohesion: 0.13
Nodes (14): Available Utilities, Configuration, Content Type Detection, Content Types, Integration Pattern, LogCompressor, Performance, SearchCompressor (+6 more)

### Community 410 - "RedisCcrStore"
Cohesion: 0.23
Nodes (6): RedisCcrStore, Client, Option, Self, String, RedisResult

### Community 411 - "compress_anthropic_live_zone_with_ccr"
Cohesion: 0.39
Nodes (8): compress_anthropic_live_zone_with_ccr(), body_with_payload(), ccr_marker_injected_when_store_wired(), large_json_array_payload(), no_marker_when_store_omitted(), String, Vec, store_only_populated_after_token_gate_admits()

### Community 412 - ".new"
Cohesion: 0.38
Nodes (3): FormatDetector, LogFormat, AhoCorasick

### Community 413 - "search_compressor.rs"
Cohesion: 0.14
Nodes (9): Strategy outcome view backed by this pattern's public counters., CompressionStrategyOutcomes, Strategy outcome accounting for local compression feedback., Track compression and retrieval outcomes by compression strategy., Record one compression for a strategy., Record one retrieval for a strategy., Return the retrievals-per-compression rate for one strategy., Return the sampled strategy with the lowest retrieval rate. (+1 more)

### Community 414 - "String"
Cohesion: 0.33
Nodes (6): find_headroom_registration(), load_mcp_config(), Any, Path, Load existing MCP config or return empty structure., Locate an existing 'headroom' MCP server registration.      Claude Code stores s

### Community 416 - "live_zone_dispatch.rs"
Cohesion: 0.31
Nodes (12): body_of(), body_with_tool_result(), byte_fidelity_outside_compressed_block(), diff_tool_result_routes_to_diff_compressor(), dispatch(), find_byte_range(), json_tool_result_routes_to_smart_crusher(), log_tool_result_routes_to_log_compressor() (+4 more)

### Community 417 - "main"
Cohesion: 0.19
Nodes (13): Cli, init_tracing(), main(), Box, Error, Option, PathBuf, Result (+5 more)

### Community 418 - ".index_batch"
Cohesion: 0.20
Nodes (8): Cursor, Memory, Create metadata from a Memory object., Validate a memory and prepare it for indexing., Build UPDATE parameters for vector metadata., Return a non-null SQLite cursor lastrowid., Index a memory's embedding.          Args:             memory: The memory to ind, Index multiple memories.          Args:             memories: List of memories t

### Community 419 - "marketing.tsx"
Cohesion: 0.19
Nodes (9): Button, ButtonProps, buttonVariants, CodeBlock(), CodeBlockProps, features, integrations, LiveStats (+1 more)

### Community 420 - "failure-learning.mdx"
Cohesion: 0.14
Nodes (13): Architecture, CLI Reference, Command Patterns, Environment Facts, File Path Corrections, Known Large Files, Marker-Based Updates, Quick Start (+5 more)

### Community 421 - "filesystem-contract.mdx"
Cohesion: 0.14
Nodes (13): Backward compatibility — models.json, Bucket assignments, Config bucket (`HEADROOM_CONFIG_DIR`), Docker naming overlap: `HEADROOM_WORKSPACE` vs `HEADROOM_WORKSPACE_DIR`, Legacy per-resource env vars, npm SDK, Plugin authors, Precedence (+5 more)

### Community 422 - ".feature_names"
Cohesion: 0.14
Nodes (7): Get feature names for vector., Get ordered list of feature names.          Args:             include_raw_embedd, Get feature names for vector., Get feature names for vector., Get feature names for vector., Get feature names for vector., Get all feature names.

### Community 423 - "build_proxy_targets"
Cohesion: 0.12
Nodes (11): CacheOptimizerRegistry, List all registered provider names (excluding tier suffixes)., List all registered optimizer names., Registry for cache optimizer plugins.      This registry allows:     - Registrat, Check if an optimizer is registered., Clear all registrations. Mainly for testing., Reset to default registrations., Register default optimizers. (+3 more)

### Community 424 - "CCSwitchReconciler"
Cohesion: 0.19
Nodes (7): Any, Count tokens in text.          Uses tokenize API if client available, otherwise, Count tokens in a message., Count tokens in messages., Extract text content from message., Initialize Cohere provider.          Args:             client: Optional cohere.C, Initialize Cohere token counter.          Args:             model: Cohere model

### Community 425 - "runtime_env.py"
Cohesion: 0.17
Nodes (16): Supported tool targets for persistent proxy wiring., ToolTarget, Validate and normalize a deployment profile name., validate_profile_name(), _binary_name(), build_manifest(), build_tool_envs(), detect_targets() (+8 more)

### Community 426 - "tool_injection_config.py"
Cohesion: 0.12
Nodes (13): 00 — Overview & Wrong Mental Model, Executive summary, Top 5 wrong assumptions, What changes, What's deleted, What's preserved, Conventions, Cross-cutting invariants (+5 more)

### Community 427 - "client.py"
Cohesion: 0.09
Nodes (24): _credentials_path(), _load_credentials_file(), Any, Path, Async HTTP client for Anthropic's OAuth usage API.  Endpoint: GET https://api.an, Load raw credentials dict from the Claude Code credentials file., Resolve a stored OAuth token for background polling (no request needed).      Re, Thin async wrapper around the Anthropic OAuth usage endpoint. (+16 more)

### Community 428 - "count_tokens_messages"
Cohesion: 0.26
Nodes (16): anthropic_messages_passthrough_when_no_suffix(), anthropic_messages_strips_1m_suffix_claude(), anthropic_messages_strips_1m_suffix_glm(), assert_byte_equal_sha256(), mount_anthropic_capture(), mount_chat_capture(), mount_responses_capture(), openai_chat_completions_passthrough_with_1m_model() (+8 more)

### Community 429 - "CCR: Compress-Cache-Retrieve"
Cohesion: 0.14
Nodes (14): Architecture, CCR: Compress-Cache-Retrieve, CCR-Enabled Components, CCR Stores Content Blocks, Not Dropped Messages, Configuration, Demo, Features, How CCR Works (+6 more)

### Community 430 - "Filesystem Contract"
Cohesion: 0.14
Nodes (14): Backward compatibility — models.json, Bucket assignments, Config bucket (`HEADROOM_CONFIG_DIR`), Docker naming overlap: `HEADROOM_WORKSPACE` vs `HEADROOM_WORKSPACE_DIR`, Filesystem Contract, Legacy per-resource env vars, npm SDK, Plugin authors (+6 more)

### Community 431 - "mod.rs"
Cohesion: 0.23
Nodes (9): CcrBackendConfig, CcrBackendInitError, Error, From, Option, PathBuf, Self, String (+1 more)

### Community 432 - "safety.rs"
Cohesion: 0.26
Nodes (11): anthropic_pair_is_detected(), collect_assistant_tool_call_ids(), multiple_anthropic_tool_results_in_one_user_message(), openai_pair_is_detected(), HashSet, String, Value, Vec (+3 more)

### Community 433 - "auth_mode_layer.rs"
Cohesion: 0.24
Nodes (12): classify_and_attach_auth_mode(), empty_headers_classify_as_oauth_for_bedrock(), probe(), router(), AuthMode, Body, Extension, Next (+4 more)

### Community 434 - "envelope.rs"
Cohesion: 0.28
Nodes (12): empty_messages_array_marks_has_messages_false(), parse(), ParsedEnvelope, parses_minimal_envelope(), rejects_invalid_json(), rejects_missing_anthropic_version(), rejects_model_field_present(), rejects_non_object_body() (+4 more)

### Community 435 - "ProxyHandle"
Cohesion: 0.21
Nodes (13): Cortex Code provider helpers., build_install_env(), Cortex Code install-time helpers., Render the Cortex Code setup instructions for the local proxy., Build the persistent install environment for Cortex Code., render_setup_lines(), build_launch_env(), default_api_url() (+5 more)

### Community 436 - "mount_anthropic_capture"
Cohesion: 0.24
Nodes (12): mount_anthropic_capture(), oauth_request_passes_tools_through_byte_equal(), payg_request_with_unsorted_tools_is_sorted_at_upstream(), payg_with_marker_passes_tools_through_byte_equal(), Arc, MockServer, Mutex, Option (+4 more)

### Community 437 - "RequestFacts"
Cohesion: 0.21
Nodes (9): configured_response(), exact_stub_overrides_bottled_default(), MatchesRequest, Self, StubRule, RequestFacts, Option, String (+1 more)

### Community 438 - "presentation.rs"
Cohesion: 0.27
Nodes (10): Simulator, build_app(), health_route_returns_ok(), response_from(), Arc, Body, Request, Router (+2 more)

### Community 439 - "errors.mdx"
Cohesion: 0.15
Nodes (12): Best Practices, Catching Errors, CompressionError, ConfigurationError, Error Details, Error Hierarchy, Error Types in Detail, HeadroomConnectionError (TypeScript) (+4 more)

### Community 440 - "memory.mdx"
Cohesion: 0.15
Nodes (12): Backends, Embedder Backends, Embedding Runtime / GPU Offload (Apple Silicon), Hierarchical Scoping, How It Works, Memory API, Memory Categories, Performance (+4 more)

### Community 441 - "shared-context.mdx"
Cohesion: 0.15
Nodes (12): API, Configuration, CrewAI, Framework Examples, `get(key, full?)`, How It Works, `keys()` and `clear()`, LangGraph (+4 more)

### Community 442 - "CacheOptimizer"
Cohesion: 0.15
Nodes (8): CacheOptimizer, Protocol, Protocol for cache optimizers.      All provider-specific optimizers must implem, Name of this optimizer., Provider this optimizer is for., The caching strategy this optimizer uses., Get aggregated metrics from this optimizer., Estimate potential savings from optimization.          Returns:             Esti

### Community 443 - "CopilotTokenProvider"
Cohesion: 0.15
Nodes (11): consume_from_bucket(), Pure token-bucket rate-limit policy helpers., Return token count after time-based refill, capped at bucket capacity., Return ``(allowed, remaining_tokens, wait_seconds)`` for a token request., Return bucket keys whose last update is older than the stale threshold., refilled_tokens(), stale_bucket_keys(), Remove buckets that haven't been used in the last 10 minutes. (+3 more)

### Community 444 - "resolve_subscription_bearer_token_details"
Cohesion: 0.22
Nodes (12): _Agg, audit_reads(), _audit_session(), _block_text(), _classify_path(), _fmt(), _parse_ts(), Path (+4 more)

### Community 445 - "._get_conn"
Cohesion: 0.21
Nodes (16): _compress_messages(), compress_scoped_passthrough_body(), _encode_payload(), _is_compressible_chat_message(), is_scoped_coding_agent_path(), _normalize_responses_text_parts(), Any, Hermes Studio scoped coding-agent proxy support.  Hermes owns authentication and (+8 more)

### Community 446 - "MemoryToolsWrapper"
Cohesion: 0.20
Nodes (12): _detect_platform(), download_cbm(), ensure_cbm(), get_cbm_path(), Path, Download and install codebase-memory-mcp binary from GitHub releases., Ensure codebase-memory-mcp is available. Download if needed.      Returns path t, Detect platform and return the release asset suffix. (+4 more)

### Community 447 - "retag_to_headroom"
Cohesion: 0.02
Nodes (114): ContentSection, DetectionResult, _magika_available(), Check if Magika is available without loading it., is_tool_excluded(), Return True if ``name`` matches the tool-exclusion set.      Plain entries match, Try to detect grep/ripgrep search results., Try to detect build/log output. (+106 more)

### Community 448 - ".count_message"
Cohesion: 0.18
Nodes (14): _call_claude_cli_streaming(), _call_cli_llm(), _call_llm(), _parse_stream_event(), Strip optional markdown fences and parse JSON.      Handles raw JSON and fenced, Call a locally installed CLI tool as the LLM backend.      Enables keyless usage, Run claude-cli with stream-json output and an idle-timeout watchdog.      Each l, Parse one line of claude-cli stream-json output, returning None on junk. (+6 more)

### Community 449 - "OpenAICompatibleTokenCounter"
Cohesion: 0.19
Nodes (8): OpenAICompatibleTokenCounter, Any, Token counter for OpenAI-compatible providers.      Uses the TokenizerRegistry t, Initialize token counter.          Args:             model: Model name., Count tokens in text., Count tokens in a single message., Count tokens in a list of messages., Get token counter for a model.          Uses the TokenizerRegistry to find the b

### Community 450 - "apply_openai_responses_verbosity_steering"
Cohesion: 0.25
Nodes (8): Acceptance criteria, Blocked by, Blocks, Files, Notes, PR-A4 — Honor customer `cache_control` markers in Rust; enable `arbitrary_precision`+`raw_value`, Rollback, Scope

### Community 451 - "context.py"
Cohesion: 0.21
Nodes (15): _build_mcp_package_spec(), _build_runtime_contract(), build_server_json(), load_project_metadata(), _project_root(), ProjectMetadata, Path, Canonical MCP publication metadata for the Headroom server. (+7 more)

### Community 452 - "WarmupSlot"
Cohesion: 0.17
Nodes (6): Any, Warmup registry for proxy cold-start state.  Holds references to preloaded heavy, Serialize the whole registry (for ``/debug/warmup``)., Status record for one warmed-up component.      ``handle`` is the concrete asset, Serialize for /debug/warmup. Never includes the raw handle., WarmupSlot

### Community 453 - "export_kompress_v2_onnx.py"
Cohesion: 0.33
Nodes (10): _build_core(), export(), _export_wrapper(), main(), Path, Wrap the dual head so forward() returns `final_scores` (== get_scores)., Compare ONNX scores against PyTorch get_scores on a real tokenized sample., Instantiate HeadroomCompressorModel and load the merged v2 weights.      The v2 (+2 more)

### Community 454 - "relevance_split.py"
Cohesion: 0.14
Nodes (13): Get the relevance scorer for the split (lazy, cached, non-blocking).          Ti, Warm the embedding model off the request thread, then swap it in.          Idemp, Prompt-conditioned KEEP/DROP split for the compression tail.          Keeps high, adaptive_threshold(), _otsu_threshold(), plan_relevance_split(), RelevanceScorer, Prompt-conditioned relevance split for KEEP/DROP compression decisions.  Segment (+5 more)

### Community 455 - "P4 — OpenAI long-tail + Bedrock/Vertex"
Cohesion: 0.31
Nodes (11): block_has_string_text_field(), bytes_offset_of(), OpenAiPlanSlot, plan_block_replacements(), plan_openai_tool_message(), plan_openai_user_message(), plan_responses_item(), PlanError (+3 more)

### Community 456 - "discover_onnxruntime_libraries"
Cohesion: 0.38
Nodes (12): dedup_existing_files(), discover_onnxruntime_libraries(), env_path(), onnxruntime_candidates_under(), onnxruntime_dylibs_in(), python_site_packages_dirs(), Option, Path (+4 more)

### Community 457 - "mount_anthropic_capture"
Cohesion: 0.23
Nodes (11): mount_anthropic_capture(), oauth_request_passes_schema_through_byte_equal(), payg_request_with_shuffled_schema_keys_arrives_sorted(), payg_with_marker_runs_e2_but_not_e1(), Arc, MockServer, Mutex, Option (+3 more)

### Community 458 - "sse_anthropic.rs"
Cohesion: 0.29
Nodes (10): citations_delta_accumulated(), four_event_dance_text_block(), input_json_delta_concatenated_parsed_at_stop(), interleaved_blocks_by_index(), message_delta_finalizes_stop_reason_and_output_tokens(), mid_stream_error_event_handled(), _ref_event(), run() (+2 more)

### Community 459 - "ccr.mdx"
Cohesion: 0.17
Nodes (11): Architecture, CCR-enabled components, Message-level CCR, Phase 1: Compression Store, Phase 2: Tool Injection, Phase 3: Response Handler, Phase 4: Context Tracker, Retention (+3 more)

### Community 460 - "ci-cd-flows.mdx"
Cohesion: 0.17
Nodes (11): Docker Publish Flow, Docs Deploy Flow, Fork Workflow Approval, Gate Summary, Manual Validation Flow, PR Decision Tree, PR Flow, Purpose (+3 more)

### Community 461 - "image-compression.mdx"
Cohesion: 0.17
Nodes (11): Compression Techniques, Configuration, Direct API, How It Works, Performance, Provider Support, Proxy Configuration, Quick Start (+3 more)

### Community 462 - "package.json"
Cohesion: 0.17
Nodes (11): name, overrides, postcss, private, scripts, build, dev, postinstall (+3 more)

### Community 463 - "RTK architecture — why wrap-CLI only"
Cohesion: 0.17
Nodes (11): 1. Cache hot zone risk, 2. Parallel implementation with `log_compressor.rs`, 3. Command-rewrite vs output-rewrite — different value propositions, Background, Proxy-side RTK was considered and rejected, Re-litigation policy, References, RTK architecture — why wrap-CLI only (+3 more)

### Community 464 - "install_all"
Cohesion: 0.24
Nodes (9): discover(), install_all(), Any, Third-party proxy extension point.  External packages hook into the Headroom pro, Run only the explicitly-enabled extensions' ``install(app, config)``.      Disco, Yield ``(name, install_callable)`` pairs for every registered extension.      En, Resolve the set of enabled extension names.      Precedence: explicit ``enabled`, _resolve_enabled() (+1 more)

### Community 465 - "VectorMetadata"
Cohesion: 0.30
Nodes (15): build_artifacts(), ensure_empty_dir(), find_one_artifact(), load_project_version(), main(), parse_args(), Namespace, Path (+7 more)

### Community 466 - ".extract"
Cohesion: 0.18
Nodes (11): P2-18. ICM-as-history-dropper (the structural mismatch), P2-19. `RollingWindow`, `ProgressiveSummarizer` (head-truncation strategies), P2-20. `MessageScorer`, `scoring/`, `relevance/` machinery, P2-21. `crates/headroom-core/src/context/` — except `safety.rs`, P2-22. `ToolCrusher` operates without `frozen_message_count`, P2-23. `CacheAligner` rewrite path violates the very thing it claims to stabilize, P2-24. Memory-handler injection at request lifecycle entry, P2-25. CCR `ccr_retrieve` tool injected only when content was compressed (+3 more)

### Community 467 - "handle_openai_responses_subpath"
Cohesion: 0.21
Nodes (11): handle_openai_responses_subpath(), normalize_openai_responses_headers(), openai_responses_subpath_url(), Any, Request, OpenAI Responses API passthrough helpers., Return a log-safe single-line representation of untrusted text., Build an OpenAI Responses API subpath URL. (+3 more)

### Community 468 - "test_pr_governance.py"
Cohesion: 0.39
Nodes (11): _event(), _load_module(), Path, Tests for pr-governance.py., test_cli_body_file_override_uses_live_body(), test_validate_pull_request_accepts_crlf_test_output_code_block(), test_validate_pull_request_allows_draft_without_ready_checkboxes(), test_validate_pull_request_body_override_uses_live_body() (+3 more)

### Community 469 - "Persistent Deployments / Installs Design"
Cohesion: 0.17
Nodes (11): Architecture, Command model, Docs strategy, Goals, Persistent Deployments / Installs Design, Problem, Risks, Runtime adapters (+3 more)

### Community 470 - "Strands Integration"
Cohesion: 0.17
Nodes (11): 1. Model Wrapping, 2. Hook Provider (Tool Output Compression), 3. Both Together, How It Works, Installation, Integration Patterns, Metrics, Quick Start (+3 more)

### Community 471 - "plan_block_replacements"
Cohesion: 0.17
Nodes (7): Connection, Create a SQLite connection with sqlite-vec loaded., Get a cached per-thread SQLite connection with sqlite-vec loaded., Return the number of vectors indexed., Remove a memory from the index.          Args:             memory_id: The memory, Get memory statistics for MemoryTracker., Reclaim unused space in the database.

### Community 472 - "model_limits.rs"
Cohesion: 0.24
Nodes (6): context_window_for(), current_claude_models_present(), empty_or_garbage_string_does_not_panic(), parse_vendored(), HashMap, String

### Community 473 - "main"
Cohesion: 0.33
Nodes (10): init_tracing(), load_bedrock_credentials(), main(), Box, Credentials, Error, Result, Send (+2 more)

### Community 475 - "Claude Code + AWS Bedrock, with Headroom compression"
Cohesion: 0.18
Nodes (10): Application inference profiles (account-specific ARNs), Claude Code + AWS Bedrock, with Headroom compression, Prerequisites, Region prefix notes, Terminal 1 — start the Headroom proxy (Bedrock backend), Terminal 2 — run Claude Code (normal Anthropic mode) against the proxy, TL;DR, Troubleshooting (+2 more)

### Community 476 - "architecture.mdx"
Cohesion: 0.18
Nodes (10): CCR: Compress-Cache-Retrieve, Entry Points, High-Level Flow, Provider Cache Optimization, Stage 1: Cache Aligner, Stage 2: Smart Crusher, Stage 3: Context Manager, The Transform Pipeline (+2 more)

### Community 477 - "code-compression.mdx"
Cohesion: 0.18
Nodes (10): Before and After, Configuration, Configuration Options, Example, Installation, Memory Management, Performance, Supported Languages (+2 more)

### Community 478 - "MemoryFilter"
Cohesion: 0.02
Nodes (111): CaseResultV3, EvalConfigV3, EvalResultV3, LoCoMoEvaluatorV3, Path, LoCoMo Evaluator V3 - Tests retrieval quality of memory systems.  This evaluator, Aggregated evaluation results., Evaluator focused on retrieval quality.      This evaluator answers the question (+103 more)

### Community 479 - "wrapper_tools.py"
Cohesion: 0.18
Nodes (11): Increment the per-stack request counter.          ``stack`` is the ``X-Headroom-, detect_install_mode(), detect_stack(), normalize_stack(), Any, Deployment context detection for telemetry.  Derives two orthogonal identity fie, Classify how Headroom is being invoked.      Resolution order:      1. ``HEADROO, Validate and normalize a stack slug.      Returns the lowercased/stripped slug i (+3 more)

### Community 480 - "P1 — Wire-format / streaming corruption"
Cohesion: 0.15
Nodes (10): _get_deepseek_pricing(), _get_litellm_clients(), _infer_model_tier(), Get fallback pricing for a DeepSeek model.      Used when the Anthropic provider, Infer the model tier (opus/sonnet/haiku) from model name.      Uses pattern matc, Import LiteLLM only when pricing/context metadata is needed., Get context window limit for a model.          Resolution order:         1. Expl, Warn about unknown model (once per model). (+2 more)

### Community 481 - "P2 — Architectural over-build"
Cohesion: 0.06
Nodes (34): 01 — Comprehensive Bug & Gap List, P0-1. System prompt mutated by `.strip()` and memory-context append, P0-2. Every Python forwarder re-serializes JSON via `httpx ... json=body`, P0-3. Rust proxy ignores customer `cache_control` markers, P0-4. ICM compresses by dropping messages from cache hot zone (wrong scope), P0-5. Numeric precision lost via `serde_json::Value` round-trip, P0-6. Memory tool injection toggles tools list and mutates `anthropic-beta`, P0-7. `responses_converter.py` drops Codex `phase` field and corrupts multi-text-part rebuild (+26 more)

### Community 482 - "P6 — Test-infra & parity"
Cohesion: 0.17
Nodes (17): Return the ZCode user configuration directory., zcode_config_dir(), ZCode (zcode.z.ai desktop app) provider helpers., build_proxy_targets(), detect_upstream(), Path, Runtime helpers for ZCode (zcode.z.ai desktop app) integrations., Map :class:`ZCodeUpstream` to headroom proxy URL params.      Returns ``(anthrop (+9 more)

### Community 483 - "dispatch_compressor"
Cohesion: 0.20
Nodes (10): diff_compressor(), dispatch_compressor(), DispatchResult, log_compressor(), DiffCompressor, LogCompressor, SearchCompressor, SmartCrusher (+2 more)

### Community 484 - "EventStreamParser"
Cohesion: 0.09
Nodes (17): _create_default_ccr_backend(), get_compression_store(), _get_env_default_ttl_seconds(), Get the compression store instance.      If a request-scoped store was set (e.g., Create a CCR backend from env (e.g. HEADROOM_CCR_BACKEND=redis).      Default (e, ExpansionRecommendation, get_context_tracker(), Multi-turn context tracking for CCR (Compress-Cache-Retrieve).  This module trac (+9 more)

### Community 485 - "integration_sse.rs"
Cohesion: 0.43
Nodes (7): client_disconnect_propagates_to_upstream(), Arc, JoinHandle, SocketAddr, sse_chunks_arrive_with_preserved_timing(), sse_upstream(), Notify

### Community 487 - "run"
Cohesion: 0.38
Nodes (9): chunk_boundary_invariance_pr_c4(), function_call_arguments_string_preserved(), minimal_upstream_response_pr_c4(), out_of_order_item_completion_by_id(), output_text_delta_accumulated_per_item(), reasoning_summary_accumulated(), response_failed_status(), response_incomplete_status() (+1 more)

### Community 489 - ".new"
Cohesion: 0.24
Nodes (7): header_contains(), is_conversation(), is_conversation_item(), is_conversation_items(), ProviderPath, HeaderMap, Self

### Community 490 - "agent-orchestration.mdx"
Cohesion: 0.20
Nodes (9): CacheAligner is detector-only, CCR digest curation, Digest routing, Integration modes, Local-first deployment, Real wake measurements, Repeated wake anatomy, Source-backed caveats (+1 more)

### Community 491 - "index.mdx"
Cohesion: 0.20
Nodes (9): Community stats, Framework Integrations, Key Features, Next steps, Nothing is lost, Quick preview, Real-world results, What gets compressed (+1 more)

### Community 492 - "langchain.mdx"
Cohesion: 0.20
Nodes (9): Agent tool wrapping, Custom configuration, Installation, LangGraph custom graph, LangGraph ReAct agent, Memory integration, Quick start, Retriever integration (+1 more)

### Community 493 - "strands.mdx"
Cohesion: 0.20
Nodes (9): Both together, Hook provider (tool output compression), How it works, Installation, Metrics, Model wrapping, Quick start, Structured output (+1 more)

### Community 494 - "text-and-logs.mdx"
Cohesion: 0.20
Nodes (9): Configuration, Content Type Detection, DiffCompressor, Kompress, LogCompressor, Performance, SearchCompressor, TextCompressor (+1 more)

### Community 495 - "EvalSuiteResult"
Cohesion: 0.20
Nodes (7): Serialize to JSON string., Deserialize from JSON string., Reconstruct a Memory object from metadata., Search for similar vectors.          Args:             filter: Search filter wit, Check if metadata passes filter constraints., Metadata stored alongside vectors for filtering and reconstruction., VectorMetadata

### Community 496 - "SQLiteVectorIndex"
Cohesion: 0.05
Nodes (39): Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by (+31 more)

### Community 497 - "ProcessStats"
Cohesion: 0.22
Nodes (11): Cursor-specific provider helpers., build_install_env(), Cursor install-time helpers., Build the persistent install environment for Cursor., build_proxy_targets(), CursorProxyTargets, Runtime helpers for Cursor integrations., Resolved local proxy targets shown in Cursor setup instructions. (+3 more)

### Community 498 - ".export"
Cohesion: 0.24
Nodes (6): _merge_section(), Path, Export memories to agent-native format.          Args:             memories: Mem, Format memories in agent-specific format.          Args:             memories: R, Default output path for this agent., Merge a marker-delimited section into an existing file.

### Community 499 - "ClaudeCodeMemoryWriter"
Cohesion: 0.33
Nodes (3): Path, Default: Claude Code project memory directory., Export high-importance memories to per-topic files.          Claude Code loads t

### Community 500 - "build_launch_env"
Cohesion: 0.20
Nodes (6): BackgroundCompressor, _Job, Any, Off-path background compression (Phase 3, #1171).  The request path must never b, Single per-process async drain that compresses enqueued work off the     request, Queue a compression job. Returns False (and drops) if the key is         already

### Community 501 - "output_turn_policy.py"
Cohesion: 0.15
Nodes (13): clear_overrides(), effective_runtime_env(), explicit_env(), getenv(), Knob, Live (per-request) env knobs and a hot-reload override store.  Most Headroom set, Apply hot-reload overrides for known knobs. Returns what was applied.      Unkno, Drop all overrides (used by tests and to reset state). (+5 more)

### Community 502 - "HeadroomContribution"
Cohesion: 0.44
Nodes (3): HeadroomContribution, Tokens conserved within the current 5h window by Headroom's layers.      These a, Tokens removed before model context by compression plus CLI filtering.

### Community 503 - "01 — Comprehensive Bug & Gap List"
Cohesion: 0.19
Nodes (12): get_tool_injection_sticky_mode(), get_tool_tracker_max_sessions(), ToolInjectionStickyMode, Operator configuration policy for proxy tool injection., Return the active memory-tool stickiness mode., Return the LRU bound for memory tool session tracking., ToolInjectionStickyMode, Policy helpers for memory tool injection stickiness configuration. (+4 more)

### Community 504 - "P3 — Missing infrastructure (Phase 3 cache stabilization)"
Cohesion: 0.20
Nodes (10): P3-28. No tool-array deterministic sort in Rust path, P3-29. JSON Schema keys never sorted recursively, P3-30. No `prompt_cache_key` auto-injection, P3-31. No `cache_control` auto-placement (Anthropic), P3-32. No volatile-content detector + warning, P3-33. No per-block token validation with fallback, P3-34. No per-content-type byte thresholds, P3-35. No cache-bust drift detector telemetry (+2 more)

### Community 505 - "Headroom SDK: A Complete Explanation"
Cohesion: 0.20
Nodes (10): Architecture Overview, File Structure Explained, Headroom SDK: A Complete Explanation, How Headroom Works: The Big Picture, Summary, The Numbers (From Our Tests), vs. Simple Truncation, vs. Summarization (LLM-based compression) (+2 more)

### Community 507 - "HeaderValue"
Cohesion: 0.25
Nodes (8): Acceptance criteria, Blocked by, Blocks, Files, Notes, PR-B2 — Live-zone block dispatcher in Rust, Rollback, Scope

### Community 508 - "handle_chat_completions"
Cohesion: 0.28
Nodes (8): handle_chat_completions(), Bytes, ConnectInfo, HeaderMap, Method, SocketAddr, State, Uri

### Community 509 - "agno.mdx"
Cohesion: 0.22
Nodes (8): Async support, Installation, Observability hooks, Quick start, Session management, Standalone message optimization, Supported providers, Tool-heavy agents

### Community 510 - "claude-code-vertex.mdx"
Cohesion: 0.22
Nodes (8): Alternative: let Headroom talk to Vertex for you, Before you start, Check that compression is working, How it works, Notes, Run it (one command), Troubleshooting, What you get

### Community 511 - "how-compression-works.mdx"
Cohesion: 0.22
Nodes (8): Batch Compression, Configuring the Compressor, Content Type Detection, Quick Start, Real Compression Ratios, Structure Preservation, The Three-Stage Pipeline, What Happens Under the Hood

### Community 512 - "StructureHandler"
Cohesion: 0.15
Nodes (9): Protocol, Protocol for structure handlers.      Any class implementing get_mask() can be u, Handler name for logging and metadata., Extract structure mask from content.          Args:             content: The con, Check if this handler can process the content.          Default implementation r, StructureHandler, ContentType, Get handler for content type.          Args:             content_type: Content t (+1 more)

### Community 513 - "_configured_enterprise_domain"
Cohesion: 0.15
Nodes (10): count_tokens_messages(), count_tokens_text(), Any, TokenCounter, Initialize tokenizer with a provider's token counter.          Args:, Count tokens in text., Count tokens in a message., Count tokens in a list of messages. (+2 more)

### Community 514 - "copilot_macos_keychain.py"
Cohesion: 0.33
Nodes (8): _candidate_security_commands(), macOS Keychain lookup helpers for GitHub Copilot CLI auth., Return a Copilot CLI OAuth token from macOS Keychain, if available., Return the last logged-in Copilot CLI username from ~/.copilot/config.json., _read_copilot_config_login(), read_copilot_oauth_token(), _run_security_lookup(), _split_env_list()

### Community 515 - "._serialize_f32"
Cohesion: 0.22
Nodes (9): observe_ratio(), ratio_50_percent_recorded(), ratio_histogram(), record_rejected_by_token_check(), rejected_counter(), HistogramVec, IntCounterVec, Registry (+1 more)

### Community 516 - "budget.py"
Cohesion: 0.24
Nodes (6): SQLite-based vector index using sqlite-vec extension.      Features:     - Cosin, Close all cached SQLite connections., Return the embedding dimension., Clear all entries from the index., Close the index (cleanup)., SQLiteVectorIndex

### Community 517 - "extraction.py"
Cohesion: 0.22
Nodes (8): get_conversation_extraction_prompt(), get_extraction_tools(), get_memory_answer_prompt(), Any, Memory extraction prompts and utilities.  This module contains extraction prompt, Generate a balanced conversation extraction prompt.      This prompt is designed, Generate a balanced answer prompt for memory-based Q&A.      Based on research f, Get tool definitions for standalone extraction (if needed).      These tools can

### Community 518 - ".handle_memory_update"
Cohesion: 0.24
Nodes (11): _estimate_cache_savings_usd(), _estimate_compression_savings_usd(), _estimate_input_cost_usd(), _get_litellm_module(), Resolve model name to one LiteLLM recognizes., Estimate compression savings in USD from saved input tokens., Estimate cache-read savings in USD — the discount delta vs list price.      Cach, Estimate input spend in USD for a request.      Uses provider cache pricing when (+3 more)

### Community 519 - "MemoryReport"
Cohesion: 0.12
Nodes (13): CodexPlugin, _parse_codex_arguments(), _parse_codex_output(), Path, Parse a single Codex session file., Parse a single Codex session file., Parse a modern Codex rollout session stored as JSONL., Reads OpenAI Codex CLI session logs from ~/.codex/sessions/.      Codex stores s (+5 more)

### Community 520 - "MemoryEntry"
Cohesion: 0.18
Nodes (11): P6-63. No SHA-256 byte-faithful round-trip test on recorded production payload, P6-64. `ccr`, `log_compressor`, `cache_aligner` parity comparators are `Skipped` stubs, P6-65. `make test-parity` not a per-PR gate, P6-66. No SSE corner-case fixtures (UTF-8 split, ping, all delta types, [DONE], mid-stream error), P6-67. No real-traffic shadow test comparing Python vs Rust output byte-for-byte, P6-68. No per-session cache-hit-rate metric, P6-69. No per-block compression-ratio histogram (only invocation count), P6-70. No token-validation rejection counter (+3 more)

### Community 521 - ".export"
Cohesion: 0.31
Nodes (6): CursorMemoryWriter, Path, Writes memories to Cursor's .cursor/rules/*.mdc format., Format as Cursor .mdc content (body only, no frontmatter).          Frontmatter, Default: .cursor/rules/headroom-memory.mdc in project root., Export with Cursor-specific .mdc frontmatter.

### Community 522 - "semantic_cache.py"
Cohesion: 0.22
Nodes (8): _check_strands_available(), CompressionMetrics, Strands SDK hook provider for Headroom tool output compression.  This module pro, Initialize the hook provider after dataclass construction., Raise ImportError if Strands is not installed., Check if Strands SDK is installed.      Returns:         True if strands-agents, Metrics from a single tool output compression., strands_available()

### Community 523 - "load_spreadsheet"
Cohesion: 0.39
Nodes (8): _bar(), _money(), Any, CLI: show durable compression savings over time.  Reads the append-only savings, Show durable compression savings over time., savings(), _tokens(), _window_line()

### Community 524 - "install.sh"
Cohesion: 0.42
Nodes (7): append_path_block(), die(), info(), main(), require_cmd(), install.sh script, write_wrapper()

### Community 525 - "CCR Architecture: Compress-Cache-Retrieve"
Cohesion: 0.22
Nodes (9): CCR Architecture: Compress-Cache-Retrieve, CCR Phase 1: Compression Store, CCR Phase 2: Retrieval API, CCR Phase 3: Tool Injection, CCR Phase 4: Feedback Loop, CCR Phase 5: Response Handler (Automatic Tool Call Handling), CCR Phase 6: Context Tracker (Multi-Turn Awareness), The Key Insight (+1 more)

### Community 526 - "Getting Started with Headroom"
Cohesion: 0.22
Nodes (9): Audit Mode, Getting Started with Headroom, Installation, Modes, Next Steps, Optimize Mode, Quick Start: Proxy Mode (Recommended), Quick Start: Python SDK (+1 more)

### Community 527 - "macOS Deployment Guide"
Cohesion: 0.22
Nodes (9): Apple GPU (MPS) Embedding Offload, FAQ, Installation Options, macOS Deployment Guide, Overview, Platform Alternatives, Production Deployment, Quick Install (+1 more)

### Community 528 - "auth_mode.rs"
Cohesion: 0.32
Nodes (3): AuthMode, classify(), HeaderMap

### Community 529 - "create_scorer"
Cohesion: 0.25
Nodes (7): create_scorer(), Box, RelevanceScorer, Result, Send, String, Sync

### Community 530 - "LevelClassifier"
Cohesion: 0.28
Nodes (5): ndarray, Serialize numpy array to compact float32 bytes., Deserialize bytes to numpy array., Get the stored embedding for a memory.          Args:             memory_id: The, Update the embedding for an indexed memory.          Args:             memory_id

### Community 531 - "sse_openai_chat.rs"
Cohesion: 0.46
Nodes (7): done_sentinel_terminates_stream_status(), multiple_choices_keyed_by_index(), refusal_field_handled(), run(), tool_call_arguments_concatenated(), tool_call_id_and_name_only_first_chunk(), usage_in_final_chunk_when_include_usage_set()

### Community 532 - "mitm_capture.py"
Cohesion: 0.36
Nodes (7): Headers, mitmproxy addon that writes sanitized HTTP exchanges as JSONL., _redact_headers(), _request_json(), response(), _sanitize_url(), HTTPFlow

### Community 533 - "map.tsx"
Cohesion: 0.38
Nodes (5): buildSvg(), Map(), pins, dotted-map, dotted-map

### Community 534 - "anthropic-sdk.mdx"
Cohesion: 0.25
Nodes (7): How it works, Installation, Message format conversion, Options, Quick start, Streaming, Tool use

### Community 535 - "claude-code-azure-foundry.mdx"
Cohesion: 0.25
Nodes (7): Before you start, Check that compression is working, How it works, If you have ANTHROPIC_FOUNDRY_BASE_URL set explicitly, Run it (one command), Troubleshooting, What you get

### Community 536 - "local-llm-prefill.mdx"
Cohesion: 0.25
Nodes (7): 1. Baseline passthrough run, 2. Reset the task, 3. Optimized run, Interpreting results, Optional: traffic learning, Setup, What to report

### Community 537 - "quickstart.mdx"
Cohesion: 0.25
Nodes (7): 1. Install, 2. Compress messages, 3. Send to your LLM, 4. Check your savings, Alternative: proxy mode (zero code changes), Next steps, What gets compressed

### Community 538 - "simulation.mdx"
Cohesion: 0.25
Nodes (7): Basic Usage, Block Breakdown, Comparing Configurations, Cost Estimation, Debugging Compression, Use Cases, Waste Signals

### Community 539 - "vercel-ai-sdk.mdx"
Cohesion: 0.25
Nodes (7): compressVercelMessages() standalone, generateObject with compressed context, headroomMiddleware() for composition, How it works, Installation, Streaming with streamText, withHeadroom() one-liner

### Community 540 - ".__init__"
Cohesion: 0.25
Nodes (4): Count dense-script (CJK/Kana/Hangul/fullwidth) codepoints.          These script, Detect optimal chars-per-token ratio based on content.          Args:, Count additional tokens for special patterns.          URLs and UUIDs often toke, Estimate token count for text.          Args:             text: Text to count to

### Community 541 - ".get_all_component_stats"
Cohesion: 0.07
Nodes (52): classify_commit_bump(), commit_height_since(), CommitInfo, compute_release_version(), determine_bump_level(), find_latest_release_tag(), get_canonical_version(), list_release_commits() (+44 more)

### Community 542 - "normalize_request_path"
Cohesion: 0.29
Nodes (7): normalize_request_path(), normalize_scope_path(), Any, Request, ASGI request-scope mutation helpers., Set an ASGI scope path and keep ``raw_path`` aligned when present., Set a FastAPI request path and clear its cached URL, if any.

### Community 543 - "_get_litellm_module"
Cohesion: 0.20
Nodes (8): assetsDir, [assetsDirArg, version], extractDistPackageJson(), extractJsonFromTarball(), extractPackageJson(), installDir, packages, tarballPaths

### Community 544 - ".count_text"
Cohesion: 0.16
Nodes (9): Any, Lazy-load the GenerativeModel for API calls., Count tokens in text.          Uses countTokens API if client available, otherwi, Count tokens in a message., Count tokens in messages.          Uses countTokens API with full conversation i, Convert OpenAI-format message to text content for counting., Estimate tokens in a message without API., Initialize Google provider.          Args:             client: Optional google.g (+1 more)

### Community 545 - ".apply"
Cohesion: 0.22
Nodes (7): _get_magika(), Get or create the singleton Magika instance.      Lazy-loads on first use to avo, Ensure Magika is loaded., Detect content type using ML.          Args:             content: The content to, Detect content types for multiple contents.          Args:             contents:, Map Magika label to our ContentType.          Args:             label: Raw Magik, Magika

### Community 546 - "error_detection.py"
Cohesion: 0.33
Nodes (4): Any, Count tokens in a single message., Count tokens in messages using LiteLLM., Count tokens in text using LiteLLM.

### Community 547 - "tag_protector.py"
Cohesion: 0.29
Nodes (7): Acceptance criteria, Blocked by, Blocks, Files, PR-A7 — Memory tool injection session-sticky, Rollback, Scope

### Community 548 - "PR-A1 — Make `/v1/messages` compression a passthrough"
Cohesion: 0.29
Nodes (7): Acceptance criteria, Blocked by, Blocks, Files, PR-E6 — Cache-bust drift detector telemetry, Rollback, Scope

### Community 549 - "PR-A3 — Switch Python forwarders to byte-faithful body forwarding"
Cohesion: 0.29
Nodes (10): audit_so(), glibc_version_from_token(), list_undef_symbols(), main(), parse_manylinux_floor(), Path, `GLIBC_2.28` → (2, 28). Returns None for non-GLIBC tokens., Return a list of human-readable violation strings. (+2 more)

### Community 550 - "PR-A4 — Honor customer `cache_control` markers in Rust; enable `arbitrary_precision`+`raw_value`"
Cohesion: 0.05
Nodes (39): Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Acceptance criteria, Blocked by, Blocked by, Blocked by (+31 more)

### Community 551 - "PR-A8 — Hotfix Python wire-format bugs; add SHA-256 round-trip test"
Cohesion: 0.25
Nodes (8): Acceptance criteria, Blocked by, Blocks, Files, Notes, PR-A8 — Hotfix Python wire-format bugs; add SHA-256 round-trip test, Rollback, Scope

### Community 552 - "PR-B1 — The big delete: retire ICM and its dependencies"
Cohesion: 0.29
Nodes (7): ANTHROPIC_BASE_URL Not Set, Permission Issues, Port Already in Use, Service Crashes Immediately, Service Not Auto-Starting on Login, Service Won't Start, Troubleshooting

### Community 554 - "smoke_issue_327.py"
Cohesion: 0.43
Nodes (7): _drive_conversation(), main(), _make_list_tool_result(), _make_string_tool_result(), Anthropic, Issue #327 — live API smoke test.  Drives a 10-turn multi-turn conversation agai, Drive a 10-turn conversation, return aggregate stats.

### Community 555 - "Headroom Latency Benchmarks"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I3 — Property tests for compression invariants, Scope

### Community 556 - "`signals/` — detection traits"
Cohesion: 0.29
Nodes (6): Canonical future ML extension — BGE classifier head, How to add a new detector, `signals/` — detection traits, Tiering — composition, not inheritance, Trait family, What does NOT live here

### Community 557 - "SmartCrusherConfig"
Cohesion: 0.33
Nodes (4): defaults_match_python(), Default, Self, SmartCrusherConfig

### Community 558 - "Provider-specific strategies"
Cohesion: 0.29
Nodes (6): Anthropic, Google, OpenAI, Provider-specific strategies, What CacheAligner reports, What this means in practice

### Community 559 - "Protection rules"
Cohesion: 0.29
Nodes (6): Configuration, How It Works, Output buffer reservation, Protection rules, System message protection, Turn protection

### Community 560 - "litellm.mdx"
Cohesion: 0.29
Nodes (6): ASGI middleware, Direct compress() with LiteLLM, How it works, Installation, Quick start, With LiteLLM Proxy

### Community 561 - "openai-sdk.mdx"
Cohesion: 0.29
Nodes (6): How it works, Installation, Options, Quick start, Streaming, Tool calling

### Community 562 - "smart-crusher.mdx"
Cohesion: 0.29
Nodes (6): Configuration, Configuration Options, Example: Before and After, How It Works, Quick Start, What Gets Preserved

### Community 563 - "show_memory"
Cohesion: 0.36
Nodes (9): agent_savings(), _check_required_agents(), _perf_line(), Path, CLI helpers for agent token-savings profiles., Render or verify Codex/Claude/Cursor token-savings settings., _read_accuracy_rate(), _split_required_agents() (+1 more)

### Community 564 - "copilot_linux_secret.py"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I5 — Promote stub parity comparators to real, Scope

### Community 565 - "Any"
Cohesion: 0.31
Nodes (9): is_base64_image_payload(), Any, Pure request-log redaction policy for image-bearing payloads., A redacted value and the number of replacements made., Return True if ``value`` is an over-threshold image data URL.      Per M2 remedi, Return ``payload`` with over-threshold image strings redacted., redact_image_base64_value(), _redact_value() (+1 more)

### Community 566 - ".count_message"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I6 — Make `make test-parity` a per-PR CI gate, Scope

### Community 567 - "runtime.py"
Cohesion: 0.50
Nodes (3): hash_query_for_log(), Privacy-preserving query identifiers for proxy logs., Stable short hash of a memory-context query, safe to log.

### Community 568 - ".snapshot"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I7 — Cache hot zone non-mutation tests, Scope

### Community 569 - "compute_semantic_cache_key"
Cohesion: 0.38
Nodes (6): compute_semantic_cache_key(), Any, Pure semantic-cache key construction policy., Recursively drop ``cache_control`` annotations before hashing., Compute the proxy semantic-cache key from generation-shaping inputs., strip_cache_control()

### Community 570 - "wire_debug_format_policy.py"
Cohesion: 0.29
Nodes (6): Any, Formatting policy for opt-in proxy wire debug artifacts., Return a filename-safe wire-debug name fragment., Return the compact wire payload preview used in proxy logs., safe_wire_debug_name(), wire_debug_preview()

### Community 571 - "wire_debug_redaction_policy.py"
Cohesion: 0.33
Nodes (6): Any, Secret redaction policy for opt-in proxy wire debug capture., Return whether a wire-debug field name should be redacted., Redact obvious secrets while preserving request/response shape., redact_for_wire_debug(), should_redact_key()

### Community 572 - "PR-A5 — Strip `x-headroom-*` from upstream-bound headers"
Cohesion: 0.36
Nodes (9): ensure_empty_dir(), load_project_version(), main(), parse_args(), Namespace, Path, PathLike, quote_arg() (+1 more)

### Community 573 - "PR-A6 — Pin `anthropic-beta` order; session-stickiness skeleton"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I9 — Continuous cache-hit-rate alarm, Scope

### Community 574 - "PR-A7 — Memory tool injection session-sticky"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I10 — Replace fake RTK shim with real RTK in wrap E2E, Scope

### Community 575 - "PR-A2 — Stop mutating the system prompt; route memory context to live zone"
Cohesion: 0.25
Nodes (8): Acceptance criteria, Blocked by, Blocks, Files, Notes, PR-B7 — CCR hardening: persistent backend + always-on tool registration, Rollback, Scope

### Community 576 - "PR-B6 — Memory subsystem refactor: live-zone tail injection only"
Cohesion: 0.25
Nodes (8): Break-Even Across Models, Compression Overhead by Scenario, Cost-Benefit Analysis, Environment, Headroom Latency Benchmarks, Key Takeaways, Per-Transform Latency Breakdown, TL;DR

### Community 577 - "PR-C3 — `/v1/responses` handler in Rust (HTTP)"
Cohesion: 0.33
Nodes (6): 1. Check Service Status, 2. Check Port, 3. Test Health Endpoint, 4. Test Proxy Functionality, 5. Check Logs for Errors, Verification

### Community 579 - "PR-E4 — `prompt_cache_key` auto-injection (OpenAI)"
Cohesion: 0.29
Nodes (4): CharacterCounter, Simple character-based counter.      Uses a fixed character-to-token ratio. Usef, Initialize character counter.          Args:             chars_per_token: Charac, Count tokens based on character count.          Args:             text: Text to

### Community 580 - "Reproducing the reconnect storm"
Cohesion: 0.18
Nodes (10): Fixtures, Full local release smoke, Install scripts, Interpretation, npm release asset smoke, Python release artifact smoke, Reproducing the reconnect storm, Run (+2 more)

### Community 581 - "Image Compression Architecture"
Cohesion: 0.29
Nodes (7): Code Location, How It Works, Image Compression Architecture, Integration Points, Provider-Specific Compression, The Key Insight, The Trained Router

### Community 582 - "Troubleshooting"
Cohesion: 0.40
Nodes (3): Any, Count tokens in a single message dict., Count tokens in a list of messages.

### Community 583 - "redact_image_base64"
Cohesion: 0.40
Nodes (4): Any, Log a request. Oldest entries are automatically removed when limit reached., Public entry point for base64-image redaction.      Walks ``payload`` (a dict, l, redact_image_base64()

### Community 584 - "layout.tsx"
Cohesion: 0.60
Nodes (3): Layout(), Layout(), baseOptions()

### Community 585 - "savings.mdx"
Cohesion: 0.33
Nodes (5): Configuration, Cost basis, Example, How it works, Usage

### Community 586 - "docker-native-install.sh"
Cohesion: 0.33
Nodes (4): HEADROOM_DOCKER_IMAGE, HOME, PATH, docker-native-install.sh script

### Community 587 - "Service Management"
Cohesion: 0.40
Nodes (5): Check Status, Restart Service, Service Management, Stop Service Temporarily, View Logs

### Community 588 - "Configuration"
Cohesion: 0.40
Nodes (5): Configuration, Crash Recovery, Environment Variables, Log Location, Port Customization

### Community 589 - "Manual Installation"
Cohesion: 0.40
Nodes (5): Manual Installation, Step 1: Create Log Directory, Step 2: Generate LaunchAgent Plist, Step 3: Load the LaunchAgent, Step 4: Verify Service

### Community 590 - "normalize_cloudcode_passthrough_path"
Cohesion: 0.40
Nodes (4): Cloud Code provider helpers., normalize_cloudcode_passthrough_path(), Cloud Code Assist route classification helpers., Return the canonical Cloud Code internal path, or ``None`` when unrelated.

### Community 591 - "handle_model_metadata_endpoint"
Cohesion: 0.33
Nodes (6): handle_model_metadata_endpoint(), ModelMetadataEndpoint, Any, Request, OpenAI-compatible model metadata endpoint shape., Handle OpenAI-compatible model metadata with Codex ChatGPT-auth support.

### Community 592 - "request_limit_policy.py"
Cohesion: 0.33
Nodes (5): Validation policy for proxy request and stream limits., Resolve the per-event SSE size cap from an optional env string., Resolve the HTTP status code for body-too-large rejections., resolve_body_too_large_status(), resolve_sse_event_max_bytes()

### Community 593 - "sse_byte_buffer_policy.py"
Cohesion: 0.40
Nodes (5): find_sse_event_terminator(), parse_sse_events_from_byte_buffer(), Pure SSE byte-buffer parsing policy., Return the earliest complete SSE event terminator in ``buf``., Drain complete ``event:`` + ``data:`` events from a bytes buffer.      Returns l

### Community 594 - "CompressionObserver"
Cohesion: 0.33
Nodes (4): CompressionObserver, Protocol, Observability protocol for compression events.  A single `CompressionObserver` i, Receive one notification per real compression event.      Implementations should

### Community 596 - "PR-I6 — Make `make test-parity` a per-PR CI gate"
Cohesion: 0.50
Nodes (4): Advanced Configuration, Custom LaunchAgent Schedule, Multiple Proxy Instances, Resource Limits

### Community 597 - "PR-I7 — Cache hot zone non-mutation tests"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I8 — Tool-definition byte-stability snapshot tests, Scope

### Community 598 - "PR-I9 — Continuous cache-hit-rate alarm"
Cohesion: 0.40
Nodes (3): Split a list into SQLite-friendly chunks., Fetch rowids for the given memory IDs., Remove multiple memories from the index.          Args:             memory_ids:

### Community 599 - "PR-I10 — Replace fake RTK shim with real RTK in wrap E2E"
Cohesion: 0.50
Nodes (4): API Key Security, LaunchAgent vs LaunchDaemon, Network Security, Security Considerations

### Community 601 - "4. Transforms (`transforms/`) - The Compression Magic"
Cohesion: 0.33
Nodes (6): 4. Transforms (`transforms/`) - The Compression Magic, Context Management: Live-Zone-Only Compression, Transform 1: Cache Aligner, Transform 2: Tool Crusher (Naive) - DISABLED BY DEFAULT, Transform 3: Smart Crusher (NEW DEFAULT), Transform 4: ML Compressor (Optional, Kompress)

### Community 602 - "The Data Flow (Step by Step)"
Cohesion: 0.33
Nodes (6): Step 1: You call the API, Step 2: HeadroomClient intercepts, Step 3: Transform Pipeline runs, Step 4: Call real API, Step 5: Log metrics and return, The Data Flow (Step by Step)

### Community 603 - "Shell Integration"
Cohesion: 0.50
Nodes (4): Manual Configuration, Setup, Shell Integration, What It Does

### Community 604 - "auth_mode.rs"
Cohesion: 0.60
Nodes (4): bench_classify(), build_headers(), Criterion, HeaderMap

### Community 605 - "mod.rs"
Cohesion: 0.40
Nodes (4): Debug, Send, Sync, Tokenizer

### Community 606 - "TextCrusherConfig"
Cohesion: 0.40
Nodes (3): Default, Self, TextCrusherConfig

### Community 608 - "community-savings.mdx"
Cohesion: 0.40
Nodes (4): Instance Details, Overview, Savings Over Time, Top Savings by Instance

### Community 609 - "Platform Stabilization Matrix"
Cohesion: 0.40
Nodes (4): Current Priorities, Issue 1843 Coverage Map, Platform Stabilization Matrix, Status Values

### Community 610 - "docs"
Cohesion: 0.40
Nodes (4): docs, Explore, Fumadocs MDX, Learn More

### Community 611 - "._metadata_insert_params"
Cohesion: 0.73
Nodes (5): Ensure-Rust(), Get-CommandPath(), Invoke-NpmCi(), Resolve-Python(), Write-Step()

### Community 612 - ".__init__"
Cohesion: 0.40
Nodes (4): buildCommand, framework, installCommand, outputDirectory

### Community 613 - "__init__.py"
Cohesion: 0.40
Nodes (3): __getattr__(), Model registry and shared ML model helpers.  Provides a centralized registry of, Resolve model exports lazily while preserving package imports.

### Community 614 - "is_known_websocket_callback_failure"
Cohesion: 0.50
Nodes (4): Manual Uninstall, Quick Uninstall, Remove Everything, Uninstallation

### Community 615 - "memory_injection_mode_policy.py"
Cohesion: 0.40
Nodes (4): MemoryInjectionMode, Memory-injection mode resolution policy., Resolve the active memory-injection routing mode from an optional value., resolve_memory_injection_mode()

### Community 616 - "test_pr_health_labels.py"
Cohesion: 0.60
Nodes (4): _load_module(), Tests for pr-health-labels.py., test_check_state_fails_when_latest_attempt_failed(), test_check_state_ignores_historical_failures_when_latest_attempt_passed()

### Community 618 - "verify-versions.py"
Cohesion: 0.70
Nodes (4): main(), Path, _read_json_version(), _read_marketplace_versions()

### Community 619 - "The Core Components (In Simple Terms)"
Cohesion: 0.40
Nodes (5): 1. HeadroomClient (`client.py`) - The Wrapper, 2. Providers (`providers/`) - Model-Specific Knowledge, 3. Parser (`parser.py`) - Understanding Your Messages, 5. Storage (`storage/`) - Metrics Database, The Core Components (In Simple Terms)

### Community 620 - "Key Design Decisions"
Cohesion: 0.40
Nodes (5): 1. Provider-Agnostic, 2. Deterministic Transforms, 3. Safety First, 4. Smart by Default, Key Design Decisions

### Community 623 - "Manual Installation"
Cohesion: 0.40
Nodes (3): Any, Build INSERT parameters for vector metadata., Get index statistics.

### Community 624 - "Differential Network Capture"
Cohesion: 0.40
Nodes (4): Custom Claude Invocation, Differential Network Capture, Generate A Report, Run The Harness

### Community 626 - "pipeline-extensions.mdx"
Cohesion: 0.50
Nodes (3): Lifecycle stages, Per-request upstream routing with `x-headroom-base-url`, Recipe: normalize requests for a quirky upstream provider

### Community 627 - "_find_available_port"
Cohesion: 0.40
Nodes (3): Path, Initialize the SQLite vector index.          Args:             dimension: Embedd, Initialize the database schema.

### Community 630 - "build_rust_extension.sh"
Cohesion: 0.83
Nodes (3): fail(), log(), build_rust_extension.sh script

### Community 631 - "The Smart Crusher Deep Dive"
Cohesion: 0.50
Nodes (4): Compression Strategy, Field Analysis, Pattern Detection, The Smart Crusher Deep Dive

### Community 632 - "Advanced Configuration"
Cohesion: 0.67
Nodes (3): API Key Configuration, Installing Headroom with Proxy Support, Prerequisites

### Community 635 - "Uninstallation"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I4 — Real-traffic shadow test (Python vs Rust), Scope

### Community 658 - "PR-I2 — SSE corner-case fixtures + fuzz tests"
Cohesion: 0.33
Nodes (6): Acceptance criteria, Blocked by, Blocks, Files, PR-I2 — SSE corner-case fixtures + fuzz tests, Scope

### Community 679 - "diagnostic_decode_policy.py"
Cohesion: 0.50
Nodes (3): Lossy byte decoding policy for diagnostics and logs., Decode bytes to a string for log/diagnostic display only.      Wire/protocol par, safe_decode_for_logging()

## Knowledge Gaps
- **1793 isolated node(s):** `ResponsesBodyView<'a>`, `Segment<'a>`, `run-claude-lane.sh script`, `{ GET }`, `inter` (+1788 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **38 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MLModelRegistry` connect `MLModelRegistry` to `HeadroomProxy`, `__init__.py`, `TrainedRouter`, `memory.py`, `MemoryBackend`, `batch_compression_eval.py`, `.get`, `dynamic_detector.py`, `TextStatisticsExtractor`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `run()` connect `run` to `copilot_macos_keychain.py`, `tokensave_installer.py`, `helpers.py`, `wrap.py`, `binaries.py`, `install_registry.py`, `copilot_auth.py`, `.get_all_component_stats`, `DeploymentManifest`, `doctor.py`, `responses.py`, `images.py`, `Memory`, `installer.py`, `init.py`, `RegisterResult`, `MemoryToolsWrapper`, `.count_message`, `analyzer.py`, `run.py`, `writer.py`, `Any`, `prometheus_metrics.py`, `MemoryBudgetManager`, `mcp.py`, `astgrep.py`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Why does `ContentRouter` connect `ContentRouter` to `HeadroomProxy`, `openai.py`, `MemoryBackend`, `adversarial_grid.py`, `code_compressor.py`, `HTMLExtractor`, `resolve_codex_routing`, `Any`, `LogCompressor`, `batch_compression_eval.py`, `__init__.py`, `SmartCrusher`, `models.py`, `retag_to_headroom`, `relevance_split.py`, `SearchCompressor`, `CompressionStore`, `HeadroomConfig`, `read_maturation.py`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Are the 44 inferred relationships involving `ContentRouter` (e.g. with `AdversarialReport` and `CellResult`) actually correct?**
  _`ContentRouter` has 44 INFERRED edges - model-reasoned connections that need verification._
- **Are the 40 inferred relationships involving `LocalBackend` (e.g. with `EvalMetrics` and `LoCoMoEvaluatorV2`) actually correct?**
  _`LocalBackend` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Are the 85 inferred relationships involving `start_proxy_with()` (e.g. with `anthropic_messages_passthrough_when_no_suffix()` and `anthropic_messages_strips_1m_suffix_claude()`) actually correct?**
  _`start_proxy_with()` has 85 INFERRED edges - model-reasoned connections that need verification._
- **Are the 17 inferred relationships involving `MemoryHandler` (e.g. with `DirectMem0Adapter` and `Mem0Config`) actually correct?**
  _`MemoryHandler` has 17 INFERRED edges - model-reasoned connections that need verification._