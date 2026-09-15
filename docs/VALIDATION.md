# Validation record

## Scope

Public package validation covers instructions, manifests, archives and release workflow configuration. Native app, runtime, service and visible-browser tests belong to the product repository. All-platform packaging is not a claim of all-platform narrated-video readiness.

## Pass one: package and normal paths

Passed locally: source validation, generated-output parity, local references, metadata versions, reproducible archives and checksum verification. Both skills and the Codex plugin passed the official creator validators. Hosted CI run 34826134299 passed on macOS arm64/x64, Windows arm64/x64 and Linux, including identical archive bytes across all five targets. The two archives are approximately 20 KiB and 22 KiB.

## Pass two: adversarial and release paths

Passed: negative tests for changed generated content, missing and escaping references, non-English documentation, version mismatch, unexpected MCP configuration, and marketplace resolution. All eight tests passed on all five hosted targets at this stage. Initial Windows runs exposed implicit encoding in test fixtures; reads and affected writes now specify UTF-8. The second review also added a dev-only main-promotion gate and a second eligible code owner to avoid an impossible self-review requirement. Main branch protection, read-only workflow defaults, private vulnerability reporting and the main-only release environment were inspected through the GitHub API. The main promotion happened after this review; see the subsequent installation record below. No release has been published.

## Native acceptance

The prior product development run produced an approximately 88-second Fullerton Google Hotels narrated video on macOS. That run predates this public package and does not validate this package's installation flow or Windows narration. No Windows visible-desktop acceptance is recorded here.

See `tests/scenarios.md` for the behavior evaluation matrix. Record actual host/app versions and evidence when running it. Do not mark unavailable production credentials, platform signing or interactive device tests as passed.

The compatibility review also found that the native capability containers differ by platform. Metadata now references shared runtime readiness fields, with a regression case covering both native status shapes and independent screenshot availability. All nine packaging tests and cross-platform archive comparison passed in [development CI](https://github.com/pageonelab/lassu-skills/actions/runs/34830282051) and [promotion PR CI](https://github.com/pageonelab/lassu-skills/actions/runs/34830283160). At that stage, both branches required pull requests and main additionally required an independent code-owner review. The Foundation Engineering policy below supersedes that approval requirement.

The final instruction review removed a leftover Mac-only path and external Node prerequisite from the recording skill. Recovery now uses the app's actual Connect/configuration flow. Twelve local tests pass, including new regression cases for legacy platform setup, Windows personal paths with different separators, and directory symlinks. The symlink case explicitly skips on a runner without the necessary OS privilege. Hosted checks for the final commit are recorded on the promotion PR.

## Actual client installation

Codex CLI 0.154.0 and Claude Code 2.1.119 each added this local Git marketplace and installed `lassu@lassu` in a temporary user profile. Both loaded version 0.1.0 into their private plugin caches. Claude Code's own marketplace validator passed; its missing-description warning was addressed by adding marketplace metadata. This verifies local marketplace resolution and plugin installation on Mac. It does not establish published-main or release-archive availability, host approval of MCP, or Windows visible-desktop operation. The temporary profiles were removed after inspection; normal user profiles were not modified.

A second actual-client check installed each plugin, then configured and removed the app-owned MCP connection. The product installer detected host ownership in both clients, created no duplicate personal skills, and preserved the enabled plugin and its cached files when disconnecting. This check also used temporary profiles.

## Default GitHub marketplace installation

On September 14, 2026, a maintainer reviewed and merged [the initial promotion](https://github.com/pageonelab/lassu-skills/pull/1). All five packaging targets and the exact-artifact gate passed on main commit `d5ca9f779c744740ed4e5ed5efdb24b6c5b4321c` in [main CI](https://github.com/pageonelab/lassu-skills/actions/runs/34840350530). [PR #7](https://github.com/pageonelab/lassu-skills/pull/7) then merged main back into dev without changing the file tree.

Codex CLI 0.154.0 and Claude Code 2.1.119 each installed `pageonelab/lassu-skills` from GitHub using the README's default-branch commands. Both cached exactly two skills and the product installer detected host ownership. This verifies the public GitHub entry point, beyond the earlier local-marketplace test. Fresh temporary profiles were removed afterward; normal user profiles were untouched. Release archives, native app rollout and Windows interactive acceptance remain separate gates.


## Global delivery and window isolation (0.1.2)

The instruction change was walked through against the default tutorial, explicit private/team audience, version-conflict, foreground-only tool, and changed-window scenarios. The review checked the actual sharing contract: `anyoneWithLink` maps to backend `public`, and sharing requires ready playback, a current version, and an idempotency key. Draft review stays private. The capture/control review distinguishes a selected page in a background task window from a hidden tab, and independent-window capture from tools that drive global input.

This is a source/contract walkthrough, not an independent agent execution. All 12 package tests, generated-file parity, deterministic archive building, English-content checks, and the recording skill creator validator passed locally. No live video was recorded or published to validate this instruction change, and no user foreground app or window was manipulated. Concurrent-work acceptance still requires a real host test with another app active and physical input in use; Windows capture behavior requires its own device validation.

## Coding daily-update discovery

Source walkthrough against the daily-update scenario in `tests/scenarios.md`: discovery now uses relevant file timestamps, version-control records, and accessible AI work history; timestamps and summaries require verification. The optional scope check allows the user to confirm or add items and is skipped when scope is already specified. Local, staging, and production demonstrations require the chosen environment to contain the described changes. Narration stays brief and conversational.

Failure-path review covered misleading timestamps, incomplete work, and an environment missing a change. Existing recording, review, permission, language, and sharing requirements remain in place. All 12 package tests, generated-file parity, and archive building passed locally. This was a source review; no host client or live recording was used, so client-version and native-media acceptance do not apply to this check.

## Foundation Engineering merge policy

On September 15, 2026 (UTC), the repository owner requested contributor self-service merging. GitHub membership and access checks confirmed that all four Foundation Engineering members have Maintain or Admin access. Main now requires zero approving reviews, with code-owner approval and last-push approval disabled. The existing strict `CI gate`, required pull requests, conversation resolution, administrator enforcement, and force-push/deletion protections remain enabled. The separate draft-release environment retains its existing approval rule.

## Draw and walkthroughs (0.2.0 development)

The new Draw skill and recording reference were reviewed against the implemented remote MCP and native v2 contracts. The product regression run exercised real MongoDB authorization and mutation transactions, native Excalidraw rendering in Chrome, silent MP4 decoding and seeking, and native image/capture/second-source composition with narration. These tests establish tool behavior, not independent agent judgment.

Local packaging validation covers all three skills, generated plugin parity, deterministic archives, and separate remote-service readiness. The cloud-only case does not depend on native canRecord or canScreenshot. The existing daily-update discovery, single-source recording, screenshot, audience and window-isolation instructions remain in effect.

No new independent Codex/Claude agent walkthrough, production OAuth deployment, Windows native device run, release publication or hosted CI result is claimed for this development change. Run the new cases in tests/scenarios.md with actual host versions before a production release.
