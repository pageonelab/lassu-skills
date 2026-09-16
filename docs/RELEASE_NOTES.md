# Release notes

## 0.2.1

Bundle the remote Draw MCP connection with the Codex and Claude Code plugins. Plugin users authorize their Lassu account through the host without manually entering a service URL; the Codex marketplace requests authorization on installation. Keep the existing desktop connection for recording and screenshots. Older skills-only installations update through their owning marketplace; personal-skills-only archives still require one-time remote configuration. Draw service deployment and first account consent remain prerequisites.

## 0.2.0

Add the `lassu-draw` skill for editable flowcharts, architecture diagrams, explanations, and wireframes through the remote Draw MCP service. It discovers available capabilities, checks current board revisions, and previews results before using them in a presentation.

Video walkthroughs can start with a high-level Draw explanation and continue into product, code, or tool details. Direct Draw asset import and multiple captured sources require the matching native capabilities; existing single-source recording remains supported. Service deployment and a compatible app are required for these features.

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
