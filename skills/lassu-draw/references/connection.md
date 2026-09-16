# Remote Draw connection

The Lassu plugin includes a `lassu-draw` remote MCP connection at `https://api.lassu.ai/mcp/draw`, using Streamable HTTP and browser-based OAuth. Install or update the plugin, enable its Draw connection, and authorize the Lassu account through the host when prompted. Codex marketplace metadata requests authorization on installation. Do not ask plugin users to paste the endpoint or add another server as the normal setup path.

## Diagnose before requesting setup

1. Discover `lassu_draw_get_context` and use it when available. A successful response establishes the connected account and capabilities; do not request login again.
2. If tools are missing, inspect the host's plugin and MCP status when available. Distinguish an older skills-only plugin, a disabled connection, a connection that has not loaded in this session, and pending or expired authorization. Missing tools alone do not prove the user is logged out. Update or enable the existing plugin connection as appropriate; start a new session after an update if required by the host. Do not install duplicate personal skills or replace the local desktop server.
3. If the host reports that Draw needs authorization, use its Connect or sign-in flow. A signed-in Lassu browser session can help complete consent, but does not itself grant MCP access. Never request passwords, bearer tokens or copied browser credentials.
4. If the configured endpoint or OAuth discovery returns 404, report that the Draw service is unavailable on that deployment. Reinstalling skills or repeating login will not repair it. Report network and service errors separately from authorization failures.

For a personal-skills-only installation or a host without bundled MCP support, configure the remote endpoint once through the host's supported MCP settings, then authorize it. Local and staging deployments use their configured API origin with the same `/mcp/draw` path. Keep a working existing connection instead of creating a duplicate; when migrating a manually configured production Draw connection to the plugin, verify the plugin connection before removing the old entry through the host.

## Authorization and readiness

The authorization page names the client, callback origin and requested permissions. Read access, board editing and private export are separate scopes. Current board permissions still apply. Manage or revoke connections at `https://lassu.ai/draw/connect`.

After connecting, call `lassu_draw_get_context`. The server reports the user, workspace, collections, quota and renderer readiness. `draw_authoring_v1` enables native authoring. `draw_preview_v1` requires a healthy renderer; `draw_presentation_v1` enables immutable presentations; `draw_presentation_render_v1` enables rendered steps and visual clips. If a renderer is unavailable, save the editable result and report that preview/export could not finish. Do not claim an unrendered drawing passed visual review.

This remote connection is separate from the local desktop MCP connection. Do not replace the desktop socket configuration, request its bearer token, or require Node.js or the native app for a standalone drawing. Local recording needs the existing signed-in app and recording permissions. If a Draw asset is imported into a local demo, both sessions must belong to the same user; use the authenticated handoff tools rather than copying credentials between connections.
