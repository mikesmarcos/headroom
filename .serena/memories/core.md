# Headroom source map
- Python application in `headroom/`; Rust core/proxy in `crates/`; package/build metadata in `pyproject.toml`, `Cargo.toml`, `uv.lock`.
- CLI entrypoints live under `headroom/cli/`; persistent deployment state/models under `headroom/install/`.
- Provider-specific adapters live under `headroom/providers/`; OpenCode lifecycle spans `providers/opencode/config.py` (pure config transforms), `runtime.py` (host/env/config payload), `install.py` (persistent mutation/revert), and `cli/wrap.py` (wrap/unwrap orchestration).
- Config safety invariant: preserve malformed/user configuration, prefer false negatives, and isolate managed ownership from user values.
- Project graph is maintained in `graphify-out/`; it is generated state and must stay out of functional commits.
- Read `mem:tech_stack` for tooling, `mem:conventions` for design rules, and `mem:task_completion` for validation gates.