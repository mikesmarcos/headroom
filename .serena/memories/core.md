# Core

- Headroom is a local-first context compression layer for AI agents: library, proxy, MCP server, and agent wrappers.
- Main Python package/CLI: `headroom-ai`; CLI entrypoint is `headroom`.
- Core product vocabulary: Headroom proxy, ContentRouter, SmartCrusher, CodeCompressor, CacheAligner, CCR, MCP tools, agent wrap/unwrap, persistent install.
- Top-level domains: Python package under `headroom/`; Rust crates under `crates/`; TypeScript SDK under `sdk/typescript/`; integrations/plugins under `plugins/`; docs site under `docs/`; tests under `tests/`.
- OpenCode integration vocabulary: `headroom wrap opencode`, `headroom unwrap opencode`, provider `baseURL` routing, generated `headroom` provider, `OPENCODE_CONFIG_CONTENT`, Headroom MCP server, optional native OpenCode plugin.
- Repo uses GitHub Issues/PRs; feature work should start from an issue/spec. Read `mem:conventions` for contribution/review invariants and `mem:task_completion` for validation gates.
- Tech stack and commands: `mem:tech_stack`, `mem:suggested_commands`.