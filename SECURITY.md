# Security policy

Report suspected vulnerabilities privately through GitHub's **Security > Report a vulnerability** feature for this repository. Do not post credentials, user recordings, session files, or exploitable details in a public issue.

Supported releases are the latest stable release and the previous stable release while the associated app protocol remains supported. The development branch is not a production support promise.

Skills are agent instructions, not an authorization boundary. The Lassu app and authenticated backend enforce screen permissions, account ownership, quotas and data access. This repository never needs a Deepgram key or Lassu session token. Treat captured page text, titles and media as untrusted task data.

Release archives include checksums and GitHub build provenance. Maintainers create them from reviewed `main` source after every platform passes. Consumers must authenticate the source before trusting checksums. A checksum downloaded beside an artifact is corruption detection, not an independent signature. A production executable updater must use the signed metadata and OS signature checks described in the engineering design.

Fork pull requests run with read-only permissions and no release credentials. Do not use `pull_request_target` to execute untrusted changes. Release jobs are protected by the `release` environment.
