# Connection recovery

1. Check whether local Lassu recording tools are available in this agent session. The native app supplies this MCP connection; the plugin's remote Draw connection is separate. Do not register a second local server when one already exists.
2. Ask the user to open Lassu, sign in, enable AI access, and connect this AI client in preferences if it is not connected. A new host session may be needed after setup. Never collect passwords, session tokens, or provider keys.
3. Call `lassu_status` once tools are available. Distinguish app reachability, account login, screen permission, capture capability, narration capability, and plan limits. A locally configured server does not prove the host has loaded it.
4. Use a host tool that controls the selected local task window without taking OS focus or global mouse/keyboard input; see [window recording](window-recording.md). A window can remain behind the user's work while its selected page renders. Lassu captures and produces media; it does not itself browse websites. Cloud browsers and hidden tabs are not the recorded local page. If no compatible background control tool exists, explain that missing capability; do not silently take over the desktop.
5. Never copy a browser profile, disable host tool approvals, bypass operating-system permissions, or install an unrequested browser extension. Preserve an explicit audience choice; newly created AI videos otherwise use Global after review, while drafts and review media stay private.
6. If the app reports an unsupported operation, stop that operation and explain the missing capability. Do not claim narrated production works on a platform just because ordinary screen recording is available.

## Account and session recovery

The App signs in one Lassu user and works in the selected workspace. Switching workspaces does not sign the App out; using a different user requires signing out and signing in again. Signing out of the browser session that authorized the App also signs out that App; independent device logins and remote Draw OAuth connections have separate lifecycles. Restore the intended login through normal sign-in. Retained captures, uploads and demos keep their original user and workspace: never retry them under a different user or copy credentials between connections.
