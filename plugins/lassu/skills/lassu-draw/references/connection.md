# Remote Draw connection

Lassu Draw is a web service. Its MCP endpoint is `https://api.lassu.ai/mcp/draw`, using Streamable HTTP and browser-based OAuth. Add that endpoint as a remote MCP server in the host client and sign in to Lassu when prompted. Local and staging deployments use their configured API origin with the same `/mcp/draw` path.

The authorization page names the client, callback origin and requested permissions. Read access, board editing and private export are separate scopes. Current board permissions still apply. Manage or revoke connections at `https://lassu.ai/draw/connect`.

After connecting, call `lassu_draw_get_context`. The server reports the user, workspace, collections, quota and renderer readiness. `draw_authoring_v1` enables native authoring. `draw_preview_v1` requires a healthy renderer; `draw_presentation_v1` enables immutable presentations; `draw_presentation_render_v1` enables rendered steps and visual clips. If a renderer is unavailable, save the editable result and report that preview/export could not finish. Do not claim an unrendered drawing passed visual review.

This remote connection is separate from the local desktop MCP connection. Do not replace the desktop socket configuration, request its bearer token, or require Node.js or the native app for a standalone drawing. Local recording needs the existing signed-in app and recording permissions. If a Draw asset is imported into a local demo, both sessions must belong to the same user; use the authenticated handoff tools rather than copying credentials between connections.
