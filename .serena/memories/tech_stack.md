# Tech Stack

- Python package `headroom-ai`, Python >=3.10, build backend `maturin`.
- Rust extension/core built via Cargo/PyO3; maturin packages Python source plus compiled `headroom._core` into one wheel.
- Python dependency/workspace flow uses `uv`; development install documented with `uv sync --extra dev` or editable pip install.
- Python tooling: `pytest`, `ruff`, `mypy`, coverage via pytest-cov.
- Rust tooling: Cargo workspace, `cargo test`, `cargo fmt`, `cargo clippy`.
- TypeScript plugin/SDK packages use Node 18+, npm package scripts, TypeScript, Vitest, and tsup.
- Docs site is a Node/Next/Fumadocs-style app under `docs/` with its own package files.
- CI includes Python/Rust checks, native install e2e, wrap e2e Docker workflow, docs, release/publish workflows.