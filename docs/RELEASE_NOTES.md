# Release notes

## 0.1.1

Use bounded private audio/video clips to review narrated demos when the app exposes `demo_clip_review`. Document queued-production cancellation and draft recovery through `demo_management`. Older app capabilities remain supported; unavailable media review is reported accurately.

# Lassu skills 0.1.0

Initial development release of the canonical narrated-video and screenshot-editing skills, packaged for Codex and Claude Code.

- Produces concise videos with capability discovery, language-aware voice selection, agent review and explicit sharing behavior.
- Separates reusable instructions from the app's local MCP transport and credentials.
- Includes deterministic archives, compatibility metadata, checksums and build provenance.

Requires a connected Lassu app. Native feature availability depends on the installed app; the skill does not add unsupported Windows narration capabilities. This release does not include native executables or browser automation tools.
