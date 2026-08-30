# FACTCHECK — weekly-recap

Every claim in this reel is the user's own first-person account of their own
real week, supplied directly in the build request — not sourced from any
external article, dataset, or third party. Nothing here is independently
verifiable by the toolkit (it is personal/organizational activity, not a
public fact), so every beat is treated as first-person testimony, not a
measured/sourced claim, per the DOUBLE-CHECK LAW (NO FABRICATION, strip
anything that could date the video).

## Claims and their status

1. **"Published 'The Death of the Generic Resume' on Substack."** — user-
   supplied. Not independently verified by the toolkit (no fetch performed);
   presented as the user's own statement, matching the article this same
   session's toolkit built a companion long-form video about
   (`death-of-the-generic-resume`).
2. **"Learned the Brutalist video workflow — 16:9 + 9:16."** — user-supplied,
   and independently true within this session: this toolkit was in fact used
   to build and iterate on four prior reels (ai-support-shift,
   two-threads-one-week, death-of-the-generic-resume, and this one) across
   both 16:9 and 9:16 cuts.
3. **"Met with the team about a fashion sustainability project — demand
   forecasting, digital sampling, material traceability."** — user-supplied.
   No specifics beyond what the user stated are asserted; no partner names,
   dates, or figures are invented.

## No fabricated numbers or named entities

No statistics, percentages, company names, or dates are asserted anywhere in
this reel beyond what the user supplied. "Next week" is used as relative
framing per the user's own words, not stamped to a specific calendar date.

## THE ACTUAL-CODE LAW — code beats are real, not invented

`weekly_recap_v1.py` and `weekly_recap_v2.py` are genuine Python scripts in
this reel folder. Both were **actually run** (not hand-typed as fake output)
to capture the CODE/OUTPUT beats' real source and real terminal output:

```
$ python3 weekly_recap_v1.py
- Published "The Death of the 'Generic' Resume"  (Substack)
- Learned the Brutalist video workflow (16:9 + 9:16)  (brutalist.art)
- Met with the team: fashion sustainability project  (kickoff)

$ python3 weekly_recap_v2.py
DONE THIS WEEK
  - Published "The Death of the 'Generic' Resume"  (Substack)
  - Learned the Brutalist video workflow (16:9 + 9:16)  (brutalist.art)
STARTING NEXT WEEK
  - Fashion sustainability: forecasting, sampling, traceability  (kickoff held, work starts next week)
```

The B03/B06 CODE beats show this real source (trimmed to the lines that
teach); the B04/B07 OUTPUT beats visualize this real output, not invented
data.
