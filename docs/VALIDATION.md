# Validation record

## Scope

Public package validation covers instructions, manifests, archives and release workflow configuration. Native app, runtime, service and visible-browser tests belong to the product repository. All-platform packaging is not a claim of all-platform narrated-video readiness.

## Pass one: package and normal paths

Passed locally: source validation, generated-output parity, local references, metadata versions, reproducible archives and checksum verification. Both skills and the Codex plugin passed the official creator validators. Hosted CI run 34826134299 passed on macOS arm64/x64, Windows arm64/x64 and Linux, including identical archive bytes across all five targets. The two archives are approximately 20 KiB and 22 KiB.

## Pass two: adversarial and release paths

Passed: negative tests for changed generated content, missing and escaping references, non-English documentation, version mismatch, unexpected MCP configuration, and marketplace resolution. All eight tests pass on all five hosted targets. Initial Windows runs exposed implicit encoding in test fixtures; reads and affected writes now specify UTF-8. The second review also added a dev-only main-promotion gate and a second eligible code owner to avoid an impossible self-review requirement. Main branch protection, read-only workflow defaults, private vulnerability reporting and the main-only release environment were inspected through the GitHub API. The release workflow itself awaits a reviewed merge to main; no production release has been published.

## Native acceptance

The prior product development run produced an approximately 88-second Fullerton Google Hotels narrated video on macOS. That run predates this public package and does not validate this package's installation flow or Windows narration. No Windows visible-desktop acceptance is recorded here.

See `tests/scenarios.md` for the behavior evaluation matrix. Record actual host/app versions and evidence when running it. Do not mark unavailable production credentials, platform signing or interactive device tests as passed.

The compatibility review also found that the native capability containers differ by platform. Metadata now references shared runtime readiness fields, with a regression case covering both native status shapes and independent screenshot availability. All nine packaging tests and cross-platform archive comparison passed in [development CI](https://github.com/pageonelab/lassu-skills/actions/runs/34830282051) and [promotion PR CI](https://github.com/pageonelab/lassu-skills/actions/runs/34830283160). Both branches require pull requests; main additionally requires an independent code-owner review. The release guide now reflects those enforced settings.

The final instruction review removed a leftover Mac-only path and external Node prerequisite from the recording skill. Recovery now uses the app's actual Connect/configuration flow. Twelve local tests pass, including new regression cases for legacy platform setup, Windows personal paths with different separators, and directory symlinks. The symlink case explicitly skips on a runner without the necessary OS privilege. Hosted checks for the final commit are recorded on the promotion PR.
