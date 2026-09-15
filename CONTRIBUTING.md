# Contributing

Use English for code, comments, documentation, commit messages, issues, and pull requests. Never commit credentials, personal configuration, captured media, private source, or machine-specific paths.

Branch feature work from `dev` and open a pull request into `dev`. Promote `dev` to `main` through a pull request; keep both long-lived branches. Any member of Foundation Engineering with repository write access may merge their own pull request after the required CI checks pass and conversations are resolved. No approval from another contributor or code owner is required. Do not develop directly on `main`, force-push a release tag, or edit an uploaded release asset.

Canonical instructions live in `skills/`. Keep `SKILL.md` focused on triggers, decisions and the normal workflow. Put detailed recovery information in local references. Each skill directory must be portable and self-contained. Avoid mandatory hooks, broad tool permissions, secrets, absolute app paths and installation scripts in skill instructions.

Run the four development commands in the README. Commit generated files after `sync`. Changes to behavior also require an evaluation against `tests/scenarios.md`; static tests establish package integrity, not agent judgment or native video quality. Document the actual client version and results without claiming unavailable platform tests passed.

For instruction changes, review the normal path and failure paths separately. Check that the agent respects account permissions, actual capabilities, revision conflicts, the requested language, privacy, and the difference between upload and sharing. Keep instructions concise and do not reward unnecessary tool calls.

Use descriptive commits, for example `feat: clarify narration recovery` or `fix: preserve plugin references in release archives`. Dependabot targets `dev`. Actions are pinned to immutable commits and updated through pull requests with passing CI.
