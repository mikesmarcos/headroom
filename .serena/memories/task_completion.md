# Completion gates
- Run focused tests for changed seams first, then the full executable suite once at the end.
- Required static checks: `ruff check .`, `ruff format --check .`, `mypy headroom --ignore-missing-imports`.
- OpenCode/config tests must run in a disposable Docker container, with temporary config/workspace env vars and no host-network access; verify the official service port is not touched.
- Before commit inspect `git status`, `git diff --check`, `git diff`, and recent log; stage only intended files and exclude `graphify-out/` and unrelated worktree changes.
- Run an independent `test-*` review against the originating issue/spec before committing.