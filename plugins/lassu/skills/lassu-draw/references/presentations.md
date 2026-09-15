# Presentations and video

## Freeze the explanation

Create a presentation from an exact board epoch/revision. The server copies the complete scene and its image bytes into a private immutable snapshot. Later board edits do not change this presentation. Source deletion, lost access or a replaced board epoch still prevents access.

Each step has a stable ID, title, purpose, visible/emphasized object IDs, optional viewport, narration suggestion, duration and optional short camera transition. Steps are complete states: visiting step four must not require playing the first three. Use the returned viewer URL with `?step=<stepId>` to open a specific step. Wait for `data-presentation-ready="true"` and verify `data-step-id` before recording it. Arrow keys and the step selector navigate the presentation.

If the drawing changes, either keep the reviewed snapshot or explicitly rebase the presentation using `update_presentation` and a new authorized snapshot ID from a render job. Check missing object references and inspect the new output. Do not silently switch a prepared video to the latest board.

## Choose the available recording path

- With ordinary `demo_production`, keep the presentation and product in the same dedicated browser window. Record that exact window, visit the prepared overview step, then the product details. A different tab in the same window is still the same source. Code can be shown in a browser-based viewer when appropriate. Wait for visual readiness, mark source times and omit loading pauses.
- With `demo_sources_v2` and `demo_draw_import_v1`, create a demo with `schemaVersion: 2`. Capture the relevant product/code windows using the same `demoId`; each stopped capture is a registered source. Additional captures share that demo's existing video admission. Import rendered Draw PNG/MP4 artifacts with `prepare_demo_asset` remotely and `import_demo_asset` locally. Read the current demo revision after adding each source.

Every version-two scene uses a registered `sourceId`. Capture/clip timestamps are relative to that source; a still starts at zero and its end sets the hold duration. Scene order controls the output sequence, so a later scene may start at zero on another source. Do not use one source's markers for another source. Keep source assets private even if the final video's audience is Global.

## Time visuals to measured speech

For a static overview, hold the image long enough for the sentence and a short reading tail. For a timed Draw clip, use `demo_narration_timing_v1`: arrange the draft's sentence groups, call `prepare_demo_narration`, then poll `get_demo` for `narrationTimings`. Set presentation durations from those measured segments, including narration lead and tail. Render the presentation revision, import its clip, and update the video scenes with the same text and voice. Cached speech is reused.

Keep transitions short and purposeful. A direct cut is often enough. The rendered visual clip is silent; the video production pipeline owns the final narration and mix. An estimate of reading speed does not replace measured audio duration.

Finish through `finalize_demo`, inspect the exact rendered revision's frames and private motion/audio clips, then finalize that reviewed revision. Confirm playback readiness and the requested final audience before delivering the link. Source readiness, structural QA and subjective playback review are distinct checks; report any unavailable review accurately.
