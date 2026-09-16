# Release procedure

## Branches and review

1. Merge feature pull requests into `dev` after `CI gate` passes.
2. Update `VERSION`, `compatibility.json` and `docs/RELEASE_NOTES.md`; run `python scripts/package.py sync` and all local checks. Commit the generated output.
3. Open a pull request from `dev` to `main`. Review the behavior and the failure/recovery paths separately. Include native app evidence when changing capability claims.
4. Require `CI gate` and resolved conversations. Any Foundation Engineering contributor with repository write access may merge, including the pull request author; no approval from another contributor or code owner is required. Keep `dev` and `main`; after squash promotion, merge `main` back into `dev` so their history remains aligned.

Squash merges are appropriate for feature changes. The repository also enables merge commits for the main-to-dev reconciliation PR: use a merge commit for that PR so main remains an ancestor of dev. Squashing the reconciliation would discard the ancestry it is meant to preserve. Both merge methods remain subject to branch protection and required checks.

`CI gate` is the stable required check. It requires all five jobs, downloads their artifacts, and compares the bytes. Missing, skipped or failed platform jobs fail the gate. Documentation changes also run validation.

## Prepare and publish

Run **Prepare release** from `main`. The workflow rejects other refs, reruns the platform matrix, verifies checksums and version, produces GitHub provenance, and creates a draft `v<version>` release from exactly the tested commit. It does not rebuild after testing.

Inspect the draft, provenance, release notes and installation checks. Publish the draft only after the matching app/backend capabilities are available. Before releasing the bundled Draw connection, verify production OAuth discovery, an unauthenticated MCP authorization challenge, host account consent, and a successful `lassu_draw_get_context` call. A 404 from the endpoint or discovery is a failed deployment gate, not a reason to ask users to reinstall. Do not publish narrated Windows capability claims without Windows native acceptance evidence. Publishing the skills release does not deploy the app or backend.

Downloaded release artifacts can be verified with:

```sh
gh attestation verify lassu-skills-0.1.0.zip --repo pageonelab/lassu-skills
```

Use the archive name for the actual version. Verify each artifact you consume. The two archives contain the same canonical skill content; the plugin archive additionally includes both host manifests, marketplace entries and the remote Draw MCP configuration.

## Repository settings

- Default branch: `main`; development branch: `dev`.
- Foundation Engineering owns this repository and has Maintain access. Every team member can merge a passing pull request without a second person's approval. `CODEOWNERS` points to the team for ownership and optional review routing.
- Protect `main`: require a pull request, conversation resolution, and the up-to-date `CI gate` check. Set required approving reviews to zero; disable required code-owner reviews, last-push approval and stale-review dismissal. Disallow force pushes and deletion, including administrators.
- Protect `dev`: require a pull request, resolved conversations and the up-to-date `CI gate`; disallow force pushes and deletion, including administrators. Maintainer changes use the same feature-branch pull request path.
- Protect `v*` tags against updates and deletion. New tags are created by the release workflow.
- Enable private vulnerability reporting and Dependabot alerts.
- Environment `release`: allow only `main`; require a maintainer review and prevent self-review where team membership permits it.
- Use read-only default workflow permissions. Never give fork checks signing or production credentials.

The separate `release` environment still requires a second maintainer when self-review prevention is enabled; this is a draft-release job approval, not a pull request merge requirement. Keep missing release approval or signing prerequisites visible.

## Rollback and update ownership

A bad skill release is fixed by a new version with corrected content or a restored known-good skill. Do not move tags or replace immutable artifacts. Users can pin a prior release until the replacement is available.

Host-managed plugins update through that host's marketplace mechanism. App-managed personal skills update through Lassu's installation receipt. User-managed files are never silently overwritten. The plugin owns remote `lassu-draw`; the app owns local `lassu`. Do not duplicate the desktop server. When migrating an existing manually configured remote Draw connection, verify the plugin connection before removing the old entry through the host.

## Native binaries

This public repository builds platform-neutral instructions. The private product repository builds the self-contained CLI and platform-specific native helpers on macOS arm64/x64 and Windows arm64/x64. Its pipeline must test the produced executable with no Node on PATH, preserve Windows native IPC identity checks, and sign/notarize artifacts before production publication.

GitHub skill provenance is not a replacement for native executable signing or the app's signed component index. Native integration rollout is tracked in the engineering design and validation record.
