# Record without taking over the desktop

The user should be able to work in other apps while Lassu records the demonstration. Window capture and background app control are separate capabilities; verify both before recording.

## Select the target

- Prefer a window already dedicated to this task. Otherwise create a normal-sized task window only through a tool that preserves the user's foreground app. Do not navigate, rearrange, or reuse an unrelated work window.
- Keep the demonstrated page selected inside that task window. A background OS window can be a valid capture source; a hidden browser tab, headless browser, or cloud browser is not equivalent to the local window Lassu records.
- Match the host's window identity with `lassu_list_sources` using kind=window. Record that sourceId, never whichever app currently has focus. If the mapping is ambiguous, resolve it before capture.
- Keep the window open and rendering. Do not minimize, move it to another desktop, put it off-screen, or change its size to hide the automation. Prefer native output focus/cropping for legibility. Full-screen or display capture requires an explicit user request.

## Operate without competing for input

- Use documented, window/page-scoped browser or app operations that preserve OS focus and do not drive the user's physical pointer or keyboard. Browser DOM/CDP tools are suitable only when they control this exact local page without activating its window.
- Never enter full screen, maximize, raise, repeatedly refocus, resize, or reposition a user's existing window for recording. Do not change display resolution, desktop layout, or another app's settings.
- Do not fight the user's app switching or attempt to restore focus after every action. Repeatedly stealing and restoring focus is still disruptive.
- Use window-scoped state and captured frames to verify the result. Never replace a missing window source with a full-display capture that includes the user's parallel work. Native dialogs, detached popups, and other windows may fall outside the selected source; verify required results are actually captured.
- If the user closes, minimizes, or repurposes the target, pause or stop capture and inspect the recoverable draft. Do not reopen, restore, or take over the window automatically.

## Capability boundary

If the available host tool requires foreground activation or global mouse/keyboard input, the default parallel-work flow is unavailable. Explain that a background-capable local control tool is needed and retain any private draft. Do not silently switch to foreground automation or claim that selecting a window alone prevents disruption. If the user explicitly requests a foreground demonstration, use only the requested interaction scope.

Do not promise concurrent-work support on an OS/host combination until it has been tested with another app remaining active. macOS independent-window capture supports occluded windows, but that does not establish the host tool's input behavior or Windows parity.
