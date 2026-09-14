# Connection recovery

1. Check whether Lassu tools are available in this agent session. A plugin supplies instructions; the native app supplies the MCP connection. Do not register a second server when one already exists.
2. Ask the user to open Lassu, sign in, enable AI access, and connect this AI client in preferences if it is not connected. A new host session may be needed after setup. Never collect passwords, session tokens, or provider keys.
3. Call `lassu_status` once tools are available. Distinguish app reachability, account login, screen permission, capture capability, narration capability, and plan limits. A locally configured server does not prove the host has loaded it.
4. Use the host's browser or computer tools to operate a visible local window. Lassu captures and produces media; it does not itself browse websites. Cloud browsers, hidden pages and remote machines are not the local screen. If no compatible control tool exists, explain that missing capability; do not silently produce a different video.
5. Never copy a browser profile, disable host tool approvals, bypass operating-system permissions, or install an unrequested browser extension. Preserve the user's chosen privacy and sharing scope.
6. If the app reports an unsupported operation, stop that operation and explain the missing capability. Do not claim narrated production works on a platform just because ordinary screen recording is available.
