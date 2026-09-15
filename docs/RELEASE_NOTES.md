# Release notes

## 0.1.3

Coding daily updates discover relevant work through the current conversation, accessible AI work history, file timestamps, and version-control records. Verify these leads and completion status before choosing a few meaningful outcomes. An optional scope check lets the user add missing items when they have not already specified the scope.

Verify that the selected local, staging, or production environment includes the changes being shown. Use brief, conversational narration focused on what changed, why it matters, and the result.

## 0.1.2

New AI-created videos use Global access after review and playback readiness, unless the user explicitly requests another audience. Global maps to the existing `anyoneWithLink` sharing audience and `public` backend privacy. Drafts and review clips remain private; screenshots and unrelated existing recordings retain their prior behavior.

Default to an exact task-window capture with background control. Do not enter full screen, maximize, rearrange user windows, or compete for OS focus and physical input. Hosts that only support foreground automation must report that limitation. This release adds workflow guidance, not a new browser-control engine.

## 0.1.1

Use bounded private audio/video clips to review narrated demos when the app exposes `demo_clip_review`. Document queued-production cancellation and draft recovery through `demo_management`. Older app capabilities remain supported; unavailable media review is reported accurately.

# Lassu skills 0.1.0

Initial development release of the canonical narrated-video and screenshot-editing skills, packaged for Codex and Claude Code.

- Produces concise videos with capability discovery, language-aware voice selection, agent review and explicit sharing behavior.
- Separates reusable instructions from the app's local MCP transport and credentials.
- Includes deterministic archives, compatibility metadata, checksums and build provenance.

Requires a connected Lassu app. Native feature availability depends on the installed app; the skill does not add unsupported Windows narration capabilities. This release does not include native executables or browser automation tools.
