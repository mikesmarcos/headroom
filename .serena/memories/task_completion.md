# Task Completion

- For Python changes, normally run: `uv run pytest`, `uv run ruff check .`, `uv run ruff format .`; add `uv run mypy headroom` when types/public interfaces are affected.
- For Rust changes, normally run: `cargo fmt --all -- --check`, `cargo clippy --workspace -- -D warnings`, `cargo test --workspace` or `make ci-precheck-rust`.
- For OpenCode provider/install changes, include targeted tests around OpenCode config/install helpers plus any relevant proxy handler tests.
- For TypeScript plugin changes, run package scripts from the plugin package: `npm test`, `npm run typecheck`, and `npm run build` when build output matters.
- Before push, repo docs recommend `make ci-precheck` after hooks are installed.
- PR body must include Real Behavior Proof; unit tests/CI are not enough by themselves for external PRs.
- If validation cannot run, report the exact command that was skipped and why.