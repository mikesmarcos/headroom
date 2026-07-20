# Conventions
- Ruff line length is 100; public functions use type hints and Google-style docstrings.
- Safety-first behavior is explicit: malformed content passes through unchanged; user-owned values are preserved; false negatives are preferred over destructive cleanup.
- Provider/config transforms should be pure where possible; runtime/environment resolution belongs at entrypoints and canonical payload builders.
- Reversible install mutations persist ownership information and only revert values still matching what Headroom applied.
- Tests assert public seams and user-visible behavior, including malformed input, nested config, byte preservation, and post-apply user edits.