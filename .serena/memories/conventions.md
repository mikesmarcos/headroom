# Conventions

- New features/architectural changes should start from a feature issue/spec and maintainer approval.
- One logical change per PR; title format follows conventional commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).
- Bug fixes require a reproduction and a test that fails before/passes after, or explicit explanation if no test is possible.
- Every external PR needs Real Behavior Proof: tested setup, exact commands/steps, after-fix evidence/result, and not-tested notes.
- Python style: Ruff, line length 100, double quotes via formatter, type hints on public functions, Google-style docstrings.
- Safety invariants: never drop user/assistant content, never break tool-call/response pairing, malformed content passes through unchanged, prefer false negatives.
- Performance invariant: transforms should stay under 50ms P99 where applicable; lazy-load optional deps.
- Dependency changes require human review and written justification covering package choice, maintainer health, install surface, and version reason.
- User-facing changes should update `CHANGELOG.md` when applicable.