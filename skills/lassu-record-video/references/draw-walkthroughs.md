# Draw overview to product detail

When a diagram will clarify the walkthrough, prepare a small editable overview and inspect its rendered preview. Prefer the signed-in local App's `lassu_draw_get_context` and keep the Draw operations on that connection. Use remote Draw when the local bridge is unavailable or the user explicitly chooses it; verify its context because its account may differ. A reachable App reporting `NOT_AUTHENTICATED` needs its login restored, not a silent switch to remote Draw. Drawing is optional and does not require screen permission or a free recorder.

Create an immutable presentation from the reviewed board revision. Explain the outcome and high-level flow, then show the related product behavior or code. Avoid repeating diagram labels or narrating every mouse movement. Keep the tone natural and concise, as if speaking with a teammate.

## One browser window

On an app with `demo_production`, open the returned presentation viewer and product pages in one dedicated browser window. Record that window, select the prepared step and wait for its `data-presentation-ready="true"` marker before explaining it. Then visit the product or browser-based code view. Mark actual source times and trim loading pauses. Do not resize user windows or assume foreground-only host controls permit concurrent user work.

## Multiple sources

If status advertises `demo_sources_v2` and `demo_draw_import_v1`, create the demo with `schemaVersion: 2`. Record product or code windows with that same demoId, stopping each before starting the next. The first capture admits the output video; subsequent component captures reuse that admission and are kept as private drafts. There are at most ten capture sources per project. Use a new demo for a genuinely separate video.

For a Draw artifact, call `lassu_draw_prepare_demo_asset` on the connection used to create it, then local `lassu_import_demo_asset` with its handoffId and the current demo revision. The local Draw bridge supports preparation too. If using remote Draw, both connections must belong to the same user. The app downloads and verifies the artifact; do not pass arbitrary URLs, local paths, or cloud tokens. Import does not share anything.

Read the registered sources and current revision from `get_demo`. Each version-two scene requires a sourceId. Capture and clip ranges use that source's media time. A PNG hold uses startMs zero and endMs as its duration, up to two minutes. Output order follows scene order; time can restart at zero when changing sources. Use the source's actual bounds for focus and inspect the composed framing.

For timed Draw clips, `demo_narration_timing_v1` provides `prepare_demo_narration`. Prepare the sentence groups, poll get_demo for measured narrationTimings, and use those durations plus lead/tail to set the presentation timing on the selected Draw connection. Render and import the silent visual clip; the native demo reuses cached speech for the final mix. A failed speech request is not permission to omit narration.

Continue the normal finalize, private review and reviewed-finalize flow. Inspect source transitions, text readability and narration alignment in addition to structural QA. An edit invalidates prior review. The final video's requested audience is independent of source-board and artifact permissions; never publish the board just to share the video.
