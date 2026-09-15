# Lassu skills

Official skills and plugins for creating narrated videos and editing screenshots with [Lassu](https://lassu.ai) in Codex and Claude Code.

> Development preview. `dev` contains the next release. `main` is the distribution branch validated by CI. The plugin provides instructions; it requires a separately connected, signed-in Lassu desktop app. Platform capabilities depend on the installed app.

Ask your agent:

> Create a concise video of today's update. Show the changes on localhost and narrate the important results.

> Record how to compare prices for The Fullerton Hotel Singapore in Google Hotels. Show the dates and currency clearly.

The agent handles preparation, capture, narration, production, and review. It records a dedicated task window using background-capable controls so the user can work elsewhere; it must not take over the desktop, enter full screen, or rearrange user windows. A host with only foreground mouse/keyboard control cannot provide this parallel-work flow. Updates normally stay below five minutes; this is editorial guidance, not a hard cutoff. Shorter useful videos are preferred. No user script or timeline editing is required when the app exposes `demo_production` and the agent can operate a visible local browser.

## Install

You need Codex or Claude Code and the Lassu desktop app, already signed in. In Lassu preferences, enable **Allow AI access** and use the app's MCP setup for your actual installation path. Grant the operating-system screen permission when requested. Do not put Lassu session credentials or a Deepgram key in an AI client configuration.

The current production setup may copy a command or configuration. The direct **Connect** flow and self-contained runtime are implemented on the product development branch and await a production release; this public plugin does not remove a runtime dependency from an older app. Windows already carries its private runtime. Update the app when the new integration release becomes available.

Choose one skill installation method per client. Do not install both personal copies and the plugin.

### Claude Code

In Claude Code:

```text
/plugin marketplace add pageonelab/lassu-skills
/plugin install lassu@lassu
```

Use `/reload-plugins` or start a new session after changes. Third-party marketplace auto-updates are controlled by Claude Code and may be off by default; enable them for the Lassu marketplace in its plugin settings if desired.

For contributors testing the development branch:

```text
/plugin marketplace add https://github.com/pageonelab/lassu-skills.git#dev
```

### Codex

Add `pageonelab/lassu-skills` as a marketplace in a Codex version with plugin support, then install **Lassu**. For users who also have the Codex CLI:

```sh
codex plugin marketplace add pageonelab/lassu-skills
codex plugin add lassu@lassu
```

Alternatively, install Lassu from Codex's plugin browser. For development, use `codex plugin marketplace add pageonelab/lassu-skills --ref dev`. The desktop app does not require a separate Codex CLI installation for normal MCP configuration. Availability of plugin management depends on the host version; do not use undocumented app APIs to automate installation.

### Personal skills or another compatible agent

A released `lassu-skills-<version>.zip` contains `skills/lassu-record-video` and `skills/lassu-edit-screenshot`, including their references. Place those directories in the host's user skill location, such as `~/.agents/skills` for Codex or `~/.claude/skills` for Claude Code. On Windows, resolve `~` to the current user's profile. No package manager is required. Connect Lassu's MCP server through the host's supported configuration UI.

Do not overwrite an existing personal skill. Back it up or uninstall the previous installation through its owner first. An app-managed installation, when available, owns updates to its own files only.

## Check the connection

Start a fresh agent session and ask it to check Lassu status. A successful check must identify the reachable app, login state, screen permission and available capabilities. Installed files alone do not prove that the host loaded the MCP server.

The browser/computer tool belongs to the AI host. It must operate the exact capturable task window on the same local desktop without taking OS focus or driving the user's physical mouse/keyboard. The page must be selected inside that window; the window may remain behind the user's other work. A cloud browser, hidden tab, WSL session, or remote machine is not automatically compatible. This package does not install a browser or copy browser profiles.

## Voice, privacy, and sharing

The native app asks the authenticated production backend whether the requested language is supported. Supported languages use backend speech generation. Unsupported languages use an installed system voice in that language when available. Login, quota, service, and network failures must not silently change the provider. If no suitable system voice exists, the agent reports that requirement.

The app retains credentials. Draft production and review clips are private. After review and playback readiness, newly created AI videos default to **Global / anyone with the link** (`audience: "anyoneWithLink"`, backend `privacy: "public"`). An explicit private or team request takes precedence. The agent applies and verifies the final audience before returning the playable result; this does not change unrelated existing recordings or screenshot defaults. It must not send a link to someone else without authorization. Account limits still apply.

## Compatibility and updates

The skills and plugin archives are identical across macOS Apple Silicon/Intel and Windows x64/ARM64. CI builds and tests their packaging on all four targets and Linux. These checks do not establish native app recording or narration parity; consult `lassu_status` and [validation](docs/VALIDATION.md).

`compatibility.json` describes the protocol and optional capabilities. The app, CLI, skills and browser integration have independent versions. Plugin installations update through the host; personal installations update through their owner. Use released versions for production, and `dev` for testing. A release is not published merely by pushing a branch.

The metadata's `runtimeReadinessChecks` refer to the shared `canRecord` and `canScreenshot` status fields. Check them when performing an operation, not when installing instructions. macOS exposes a capability array and Windows exposes a capability object. A recording quota or a busy recorder must not be mistaken for an incompatible plugin or used to block otherwise available screenshots.

## Development

Maintainers need Python 3.11 or newer. End users do not need Python, Node.js, npm, or Git to use downloaded skill archives.

```sh
python scripts/package.py sync
python scripts/package.py check
python -m unittest discover -s tests -v
python scripts/package.py build
```

Edit `skills/` as the canonical source. `plugins/lassu/skills/` and both marketplace manifests are generated, committed outputs for Git-based plugin installation. Do not edit generated files directly.

See [contributing](CONTRIBUTING.md), [release procedure](docs/RELEASING.md), [engineering design](docs/ENGINEERING_DESIGN.md), and [security policy](SECURITY.md). All repository content, commit messages, issues, and pull requests must be in English.

MIT licensed. The Lassu desktop application and production service have their own distribution and service terms.
