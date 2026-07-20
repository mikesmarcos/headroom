# Stack
- Python >=3.10, maturin build backend, Rust workspace for native proxy/core components.
- Dependency lock/package manager: `uv.lock` with `uv`; editable development environment is commonly `.venv`.
- Main quality tools: pytest/pytest-asyncio/pytest-cov, Ruff, mypy; Click powers the CLI.
- Optional/provider features are dependency-gated and some test files require extras not present in the minimal environment.
- OpenCode uses JSON/JSONC-like config at `OPENCODE_CONFIG` or the XDG/OpenCode home default; persistent Headroom state uses `HEADROOM_CONFIG_DIR`/`HEADROOM_WORKSPACE_DIR`.