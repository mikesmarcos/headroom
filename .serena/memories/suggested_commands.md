# Suggested Commands

- Install dev deps: `uv sync --extra dev`.
- Run Python tests: `uv run pytest`.
- Run Python lint: `uv run ruff check .`.
- Format Python: `uv run ruff format .`.
- Type check Python: `uv run mypy headroom`.
- Rust tests: `make test` or `cargo test --workspace`.
- Rust format check: `make fmt-check` or `cargo fmt --all -- --check`.
- Rust lint: `make lint` or `cargo clippy --workspace -- -D warnings`.
- Pre-push gate: `make ci-precheck`.
- Install local git hooks: `make install-git-hooks`.
- OpenCode plugin package: from its package dir, `npm test`, `npm run typecheck`, `npm run build`.
- Docker wrap e2e: `make run-e2e-wrap`.
- Personal harness preference in this environment: prefix shell commands with `rtk` when using Bash, e.g. `rtk git status`, `rtk pytest ...`.