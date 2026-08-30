# Chaitanya Malepati

Humanitarians AI fellow. Weekly research-log teardowns of the **Medhavi** hub
(`medhavi-hub`) — subsystem audits documented as they happen, in the Brutalist
format. Video projects live in one dated lowercase-kebab folder per episode,
`YYYY-MM-DD-slug/`, with a `beat_sheet.json` and a README.

## Voice choice

**Voice:** Onyx (`am_onyx`)
**Register:** Lab note — flat, dry, no trailer voice.

Selected for the series and recorded as `metadata.voice_kokoro` in every beat
sheet. Kept across the series unless an explicit, documented re-voice decision
is made.

## House style

These reels are **Brutalist, not Claude-branded `ai-explainer`s**. Four colours
(`#0A0A0A` ground, `#F2F0EB` paper, `#E8452C` signal, `#6B6B6B` mute), two type
families, hard cuts only, no music bed. No `ClaudeComposerAsk` cold open, no
verdict page, no HANDOFF beat, no channel logo bug. Departures from
`ai-explainer` frame law are enumerated per-episode in that episode's
`BUILD-LOG.md`.

Visuals are rendered out-of-tree by a deterministic Pillow renderer and dropped
into per-beat `media/` slots; the brutalist toolkit is used **read-only** for
Kokoro narration, conform/mux, and the 9:16 derivation.

## Reports

| Date | Title | Subject | Status |
|---|---|---|---|
| 2026-08-28 | [What Is a Concept Map](2026-08-28-what-is-a-concept-map/) | Concept Map subsystem audit — schema, S3 layer, review gate, and the verified output's zero consumers | Built · QC'd · fact-checked · not published |

## Media policy

Rebuild with the free local toolkit
([brutalist.art](https://github.com/nikbearbrown/brutalist.art)). MP4, MP3, and
per-beat renders are never committed — they stay local and gitignored. What
lands here is the text package: beat sheets, script, shot list, fact check,
sources, pedagogy sign-off, build log, QC report, and the renderer.
