# Validation record

## Scope

Public package validation covers instructions, manifests, archives and release workflow configuration. Native app, runtime, service and visible-browser tests belong to the product repository. All-platform packaging is not a claim of all-platform narrated-video readiness.

## Pass one: package and normal paths

Pending final execution: source validation, generated-output parity, local references, metadata versions, reproducible archives and checksum verification. GitHub Actions runs the same artifact build on five native runner targets.

## Pass two: adversarial and release paths

Pending final execution: changed generated content, missing and escaping references, non-English documentation, version mismatch, unexpected MCP configuration, and marketplace resolution. Review branch protection, workflow permissions, release source gating and provenance separately from the package tests.

## Native acceptance

The prior product development run produced an approximately 88-second Fullerton Google Hotels narrated video on macOS. That run predates this public package and does not validate this package's installation flow or Windows narration. No Windows visible-desktop acceptance is recorded here.

See `tests/scenarios.md` for the behavior evaluation matrix. Record actual host/app versions and evidence when running it. Do not mark unavailable production credentials, platform signing or interactive device tests as passed.
