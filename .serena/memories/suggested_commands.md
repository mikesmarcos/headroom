# Common commands
- Install/sync dev dependencies: `uv sync --extra dev`.
- Focused tests: `uv run pytest tests/<file> -q`.
- Full project tests: `uv run pytest`; optional tests may require extra dependencies and provider/model assets.
- Lint/format/typecheck: `uv run ruff check .`, `uv run ruff format .`, `uv run mypy headroom --ignore-missing-imports`.
- For config-writing CLI tests, use an ephemeral Docker container with temporary `HOME`, `XDG_CONFIG_HOME`, `OPENCODE_CONFIG`, `OPENCODE_HOME`, `HEADROOM_CONFIG_DIR`, and `HEADROOM_WORKSPACE_DIR`; never use `network=host`.