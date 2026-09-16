# Draw connection

Prefer the signed-in local Lassu app when its AI integration is available. The local `lassu` MCP server and the plugin's remote `lassu-draw` server expose the same `lassu_draw_*` tool names; choose by server identity, not just the unqualified name.

## Choose and keep one connection

1. If local `lassu_draw_get_context` is available, call it first. It uses the App's existing login and enabled AI access. A successful response establishes the account, workspace and Draw capabilities; do not request separate remote OAuth. Drawing does not require screen permission, a free recorder or recording quota. Local `lassu_status` may advertise `local_draw_v1`, but recording readiness is not a Draw prerequisite.
2. After context succeeds, keep board operations, rendering, job polling and presentation calls on that connection. App credentials remain inside the App. Do not read or copy its login token into host configuration or the remote MCP connection.
3. If no local connection exists, the App is unreachable, or an older App returns `UNKNOWN_TOOL`/`APP_VERSION_UNSUPPORTED`, use an existing authorized remote connection or its normal OAuth flow. Updating the App is another way to enable local drawing. Missing tools alone do not prove the user is logged out; inspect host plugin/MCP status and reload or start a new session when required. Do not install a duplicate local server or duplicate personal skills.
4. If a reachable App reports `NOT_AUTHENTICATED`, explain that its login needs restoring. If AI access is disabled, restore the user's intended App integration. Do not silently switch to a remote account. Permission, quota, revision, renderer and service errors also stay on the selected connection. Following an uncertain mutation, inspect or retry the same arguments/key on that connection instead of issuing it through another account.
5. A user may explicitly choose remote drawing even with an installed App. Verify the remote context before any edits; never infer that local and remote sessions belong to the same account. A remote/cloud agent that cannot reach the local App uses this remote path.

## Remote setup when needed

The plugin includes a Streamable HTTP connection at `https://api.lassu.ai/mcp/draw`. Codex marketplace metadata uses `ON_USE` authorization so installation does not require a second Draw login for local App users. Invoke the host's Connect/sign-in flow only when the remote path is needed. Host UI and loading behavior vary. Do not ask plugin users to paste the endpoint as the normal setup path.

A signed-in browser can help complete remote consent but does not itself grant MCP access. The authorization page names the client, callback origin and read/write/export scopes. Manage connections at `https://lassu.ai/draw/connect`. Never request passwords, bearer tokens or copied browser credentials.

For personal-skills-only installations or hosts without bundled MCP support, the App's existing local connection is sufficient when it supports Draw. Otherwise configure the remote endpoint once through the host's supported settings, then authorize it. Keep a working existing connection rather than creating a duplicate. When migrating a manually configured remote connection to the plugin, verify the plugin connection before removing the old entry through the host.

## Readiness and errors

Call `lassu_draw_get_context` on the selected connection. `draw_authoring_v1` enables native authoring. `draw_preview_v1` requires a healthy renderer; `draw_presentation_v1` enables immutable presentations; `draw_presentation_render_v1` enables rendered steps and clips. If rendering is unavailable, save the editable board and report that preview/export could not finish. Do not claim an unrendered drawing passed visual review.

A 404 from the remote MCP endpoint or OAuth discovery means that deployment does not expose Draw AI. A 404 from the local Draw API bridge may mean the backend needs updating. Reinstalling skills or repeating OAuth cannot repair an unavailable service. Report network/service errors separately from expired authorization.

Local recording still requires a signed-in App and the relevant capture permissions. Draw artifact import uses the authenticated handoff tools and requires the same user on both connections; never move credentials between them. Cloud Draw alone does not establish local recording support.
