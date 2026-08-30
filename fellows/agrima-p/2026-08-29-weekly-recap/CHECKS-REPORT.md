# CHECKS-REPORT — weekly-recap
Written before the first slate compile, per PROOF GATE (skills/make/cli-explainer
SKILL.md — see metadata.note in beat_sheet.json for the two disclosed
substitutions: voice/branding, and render pipeline).

## Per-beat classification

11 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Why |
|---|---|---|
| B00 | SHOW | ClaudeComposerAsk, ask shown answered (cold open); narration opens with the host's self-intro, per cli-explainer's own reference-example B00 convention |
| B01 | SHOW | Manim typographic reveal, names its artifact (the "not a highlight reel" phrase itself) |
| B02 | SHOW | ClaudeComposerAsk, the real v1 build prompt shown |
| B03 | SHOW | ClaudeCodeBeat, the REAL weekly_recap_v1.py source (actually run — see FACTCHECK.md) |
| B04 | SHOW | Manim three-card row, names its artifact (Substack / Brutalist / fashion cards, undifferentiated) — the real v1 output, visualized |
| B05 | SHOW | ClaudeComposerAsk, the real v2 revision prompt shown |
| B06 | SHOW | ClaudeCodeBeat, the REAL weekly_recap_v2.py source (actually run — see FACTCHECK.md) |
| B07 | SHOW | Manim regrouped cards, names its artifact (DONE THIS WEEK / STARTING NEXT WEEK columns + divider) — the real v2 output, visualized |
| B08 | SHOW | Manim typographic beat, names its artifact (the three-line lesson) |
| B09 | SHOW | ClaudeComposerAsk handoff, prompt read + discussed (HANDOFF LAW) |
| B10 | SHOW | ClaudeTitleOutro, title restated |

Every claim-bearing beat names its on-screen artifact in `shot.visual_intent`
or the Remotion props. No beat is a bare CARD carrying an unvisualized claim.

## Teaching-arc checklist

- FRAMEWORK ✓ — B01 states the problem (highlight-reel recaps flatten done
  vs. just-started) before the CLI loop begins, per the REQUIRED spine.
- WORKED EXAMPLE ✓ — B02-B04 (ask -> real code -> real output) and B05-B07
  (the required revision cycle) are a genuine, actually-run build, not
  abstract assertion — see THE ACTUAL-CODE LAW in FACTCHECK.md.
- FALSIFIABILITY ✓ — FACTCHECK.md is explicit that every substantive claim
  is the user's own first-person account, not independently sourced or
  verified by the toolkit; no invented statistics or dates.
- SCAFFOLDED TASK ✓ — B09 hands the viewer a concrete, runnable extension of
  the same exercise (their own week, same done/next split).
- BOOKENDS ✓ — B00 cold open (Claude composer, ask answered, host self-intro
  per cli-explainer's own B00 convention) / B10 title-restate outro — both
  present, correct order.
- NO-SOURCE-NO-VERDICT ✓ — every claim is either the user's own supplied
  framing (explicitly attributed as such in FACTCHECK.md) or the real,
  captured output of a script that was actually run; no invented numbers,
  no named companies/partners beyond what the user stated.

## Deviations from house defaults (disclosed, not hidden)

1. **Voice/branding substitution**: user asked for a woman's voice reading
   this reel. cli-explainer's documented default is Teardown register,
   Kokoro `am_onyx` (male), `@NikBearBrown` handle. This toolkit ships
   exactly two Kokoro voices — `am_onyx` and `af_bella` — so `af_bella` is
   the only female voice available; used here, plus `@HumanitariansAI`
   branding, matching the precedent already set on this user's other three
   reels rather than the house Teardown persona.
2. **Render pipeline substitution**: cli-explainer's SKILL.md documents
   `scripts/vox_run.sh`, `scripts/vox_compile.py`, and `scripts/type_check.py`
   as the build/render/GATE-T tooling. None of these three scripts exist
   anywhere in this toolkit install (confirmed by search under
   `runtime/scripts/` and `runtime/qc/`). Rendered instead through
   `run.sh`/`compile.py`/`static_scene_check.py`/`manim_layout_audit.py`/
   `final_frame_check.py` — the same pipeline used successfully on this
   user's other three reels this session. The story spine, required beats,
   Claude-skin components (`ClaudeComposerAsk`, `ClaudeCodeBeat`,
   `ClaudeTitleOutro` — all confirmed present and registered in Root.tsx),
   and THE ACTUAL-CODE LAW are all honored; only the specific build-script
   names differ from the skill's documentation.
3. **No pantry/vox beats**: every non-composer/code beat is self-generated
   Manim, zero external images — consistent with this user's other reels
   built this session.

GATE F: FACTCHECK.md / SHOTLIST.md / PROMPTS.md all present. CHECKS-REPORT
written before first render. Proceeding to audio generation.
