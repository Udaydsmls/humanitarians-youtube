# Month 3 Renewal Request - Aishwarya Patil

**Request date:** 2026-10-29

**Project:** Mycroft patent intelligence system

**Current agreement:** 2026-08-01 - 2026-10-31

**Requested period:** 2026-11-01 - 2027-01-31

**Period reviewed:** 2026-08-01 - 2026-10-29

**Project Manager and supervisor (12-29 October):** Shradha Katte (katte.shradha@humanitarians.ai). The supervisor for 1 August - 11 October is not stated in this report.

**Degree:** MS in Information Systems

**Authorization:** OPT, 2026-04-15 - 2027-02-20. Supporting documents go to HR privately, not in this file.

## Summary of work

### 1. Mycroft Patent Reader

#### The Project

A system that reads a patent's claims and citation lineage from real public data. It splits a patent's claims into independent and dependent claims, traces what the patent cites, and can optionally classify each independent claim's protection scope (broad or narrow; defensive, offensive or exploratory) with the Claude API. The data comes from Google's public patent dataset in BigQuery (`patents-public-data.patents.publications`, about 98 million rows). The system is served by a FastAPI backend with a React frontend, and is measured by an evaluation harness against hand-labelled claims.

#### Repository

[nikbearbrown/mycroft, main, projects/Patents-Intelligence-Engine/patent-reader](https://github.com/nikbearbrown/mycroft/tree/main/projects/Patents-Intelligence-Engine/patent-reader)

#### Summary of work

- **ClaimsAgent: structural reading.** I built `claims_parser.py`, which splits a patent's claims and classifies each one as independent or dependent. It was tested against 4 real patents.
  - I narrowed the multi-dependency detector to genuine claim-reference patterns.
  - Broader testing found a real bug: one patent numbers its claims `"1 ."` instead of `"1."`, and the parser silently returned 0 claims for a patent with 14. I fixed it and verified both formats.
- **ClaimsAgent: scope classification.** I built `claim_classifier.py`, which calls the Claude API for each independent claim's breadth and posture, and wired the parser and classifier together as `ClaimsAgent`.
  - Refusals on sensitive subject matter are returned as "unclear" with a caveat instead of crashing.
- **LineageAgent: backward citations.** I built `lineage_agent.py`, which reads a patent's backward citations from the same row as its claims, so there's no second query.
  - I found and fixed a real bug: BigQuery returns empty strings, not `None`, for missing fields, which made every citation look like non-patent literature.
  - I confirmed it handles international publication numbers (for example `CN-103154936-A` and `WO-2022015730-A1`).
  - Forward citations were deliberately deferred because of their expensive query pattern, and the zero-citation case is still untested.
- **Query cost discipline.** The patents table has no partitioning or clustering, so a single new patent lookup scans about 116 GB, roughly $0.71 at list price. I documented that, kept every query an exact parameterized match, and reused cached patents in all test scripts.
- **CLI, then API.** I built `patent_reader.py`, a command-line tool that wires both agents together. Then I built `api.py`, a FastAPI backend with CORS that loads its API key through python-dotenv, which removed a recurring failure where the key had to be exported by hand in every terminal.
- **React frontend.** I built a Vite React frontend that calls the backend, then hardened it:
  - three distinct error messages (wrong publication number, server error, backend unreachable);
  - a loading spinner with a hint for the slow classify path;
  - inputs disabled during a fetch;
  - classify set to off by default, so the free path is the default.
- **Classifier evaluation harness.** I built `eval_classifier.py`, which scores the classifier against hand labels with accuracy, Cohen's kappa, a majority-class baseline and a collapse check. I also built `pull_eval_claims.py`, which runs one capped BigQuery query.
  - The pull scanned 161.8 GB for $0.92 at list price and returned 160 candidate patents.
  - 147 of those 160 have only 1-3 independent claims, so the test set became 50 claims from 16 patents, 2 per CPC section A-H.
- **First baseline result.** I labelled all 50 claims by hand and ran the baseline. The cost upper bound was $0.32; the actual cost wasn't recorded.
  - Breadth: accuracy 0.66, kappa 0.08.
  - Posture: accuracy 0.60, kappa 0.00.
  - Both fall below the always-most-common-answer baseline, and the classifier leans broad/offensive on functional claim wording, not narrow/defensive as suspected.
  - All 50 posture labels are defensive, so this set can't measure posture agreement yet.
  - I also fixed a refusal bug: the model can refuse partway through an answer, so `claim_classifier.py` now treats `stop_reason == "refusal"` as declined, and all 50 claims score.
- **Communication.** 12 project progress videos and 12 STEM/AI explainers, each with narration, beat sheet, scenes and an evidence-discipline PEDAGOGY.md.

Tools: Python, Google BigQuery, Claude API, FastAPI, React (Vite), Manim, Remotion, Kokoro TTS, Claude Code.

#### Degree relevance

This work is directly relevant to an MS in Information Systems. It covers:
- building a patent intelligence system;
- querying a large public dataset in BigQuery under a cost model;
- designing an evaluation methodology for a multi-agent AI system (hand-labelled test sets, Cohen's kappa, majority-class baselines).

## Weekly Log

Weeks run Saturday to Friday, starting on the agreement's first day (1 August). The last week runs to the report date (24-29 October). Hours are my own estimate; I have no separate hours log for this period. Evidence is the commit date in each repository. A week with no commit and no dated folder is marked as a gap. All video files are in the [Mycroft videos Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6).

### 2026-08-01 - 2026-08-07: Claims and Lineage agents, first video (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Two work folders are dated 2026-08-03: the first project video, on a two-agent design that reads a patent's claims and citations, and a finance-desk concept explainer.
- These folders reached the repository on 2026-08-27, in a snapshot commit by Nik Bear Brown ([e6e678cc](https://github.com/nikbearbrown/humanitarians-youtube/commit/e6e678cc99477b65bcd820926fd5bfb508d270b9)), not in a commit of my own. No mycroft commit is dated this week.

**Evidence folders:** [2026-08-03-patent-claims-lineage-agents](../2026-08-03-patent-claims-lineage-agents/), [2026-08-03-fluency-trap-in-a-variance-note](../2026-08-03-fluency-trap-in-a-variance-note/)

**Videos:** Project Video: Two Agents Read a Patent: Claims and Lineage with Claude. STEM Video: The Fluency Trap in a Variance Note ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-08-08 - 2026-08-14: Gap

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- **Gap.** Neither repository has a commit dated this week, and no work folder is dated in it. There's no evidence to link for this week.

**Evidence folder:** none

**Videos:** none

### 2026-08-15 - 2026-08-21: Gap

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- **Gap.** Neither repository has a commit dated this week, and no work folder is dated in it. There's no evidence to link for this week.

**Evidence folder:** none

**Videos:** none

### 2026-08-22 - 2026-08-28: Splitting the claims, three finance-data explainers (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Progress video 2, on the claim-splitting parser and its stress test ([8c752fb9](https://github.com/nikbearbrown/humanitarians-youtube/commit/8c752fb9ad2c4749b6acdc98f83774305141b9c0), [PR #59](https://github.com/nikbearbrown/humanitarians-youtube/pull/59)).
- Three STEM explainers on financial data pitfalls:
  - survivorship bias ([9b1eaeff](https://github.com/nikbearbrown/humanitarians-youtube/commit/9b1eaefff00e84641603805adc14fb57a6484135), [PR #47](https://github.com/nikbearbrown/humanitarians-youtube/pull/47));
  - correlation vs. causation ([d5212b6a](https://github.com/nikbearbrown/humanitarians-youtube/commit/d5212b6ae089a414fd78f56d77b299d911cb85e2), [PR #51](https://github.com/nikbearbrown/humanitarians-youtube/pull/51));
  - point-in-time vs. restated data ([17a2e0e2](https://github.com/nikbearbrown/humanitarians-youtube/commit/17a2e0e24e9ba89af2d9f59d472e6ad6f598e62c), [PR #52](https://github.com/nikbearbrown/humanitarians-youtube/pull/52)).
- Renamed the three explainer folders from 08-27 to 08-28 and added a NARRATION.md to each ([7e959205](https://github.com/nikbearbrown/humanitarians-youtube/commit/7e9592056b9df1b0668f8fecfe9390e361f96e1b), [PR #57](https://github.com/nikbearbrown/humanitarians-youtube/pull/57)). All of these commits are dated 2026-08-28.

**Evidence folders:** [2026-08-28-patent-agent-video2-splitting-claims](../2026-08-28-patent-agent-video2-splitting-claims/), [2026-08-28-survivorship-bias-datasets](../2026-08-28-survivorship-bias-datasets/), [2026-08-28-correlation-vs-causation-signals](../2026-08-28-correlation-vs-causation-signals/), [2026-08-28-pointintime-vs-restated-data](../2026-08-28-pointintime-vs-restated-data/)

**Videos:** Project Video: Splitting the Claims. STEM Videos: Survivorship Bias in Financial Datasets; Correlation vs. Causation in Signal-Finding; Point-in-Time vs. Restated Data ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-08-29 - 2026-09-04: Claims parser, scope classifier and ClaimsAgent (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Added the claims parser, which splits and classifies claims and was tested against 4 real patents ([mycroft 23f6f47](https://github.com/nikbearbrown/mycroft/commit/23f6f47e0bbd3bd4c85be7efaa2c7190f751b300), [PR #32](https://github.com/nikbearbrown/mycroft/pull/32)).
- Narrowed the multi-dependency detector to genuine claim-reference patterns ([mycroft aaa2939](https://github.com/nikbearbrown/mycroft/commit/aaa29394e8ae66825e3561d0e332f770c139e7c9), [PR #33](https://github.com/nikbearbrown/mycroft/pull/33)).
- Added the claim scope classifier and the ClaimsAgent class, and fixed a test to use exact-match queries ([mycroft 3a89f97](https://github.com/nikbearbrown/mycroft/commit/3a89f97797dc545118e2f683047300ab89a9fd85), [PR #34](https://github.com/nikbearbrown/mycroft/pull/34)).
- Progress videos 3, on the real cost of a query ([8262adc5](https://github.com/nikbearbrown/humanitarians-youtube/commit/8262adc599e76c317a1c62a0af70a81c1e5d87c2), [PR #74](https://github.com/nikbearbrown/humanitarians-youtube/pull/74)), and 4, on reading the claims ([53c9b823](https://github.com/nikbearbrown/humanitarians-youtube/commit/53c9b8236672b2be90a1684105853a6d12e4e0cf), [PR #76](https://github.com/nikbearbrown/humanitarians-youtube/pull/76)). All of these commits are dated 2026-08-31.

**Evidence folders:** [2026-08-31-patent-agent-video3-real-cost-of-a-query](../2026-08-31-patent-agent-video3-real-cost-of-a-query/), [2026-08-31-patent-agent-video4-reading-the-claims](../2026-08-31-patent-agent-video4-reading-the-claims/)

**Videos:** Project Videos: The Real Cost of a Query; Reading the Claims ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-09-05 - 2026-09-11: Broader testing and the start of the Lineage Agent (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Broadened domain testing: found and fixed the `"1 ."` claim-numbering bug on 3 new patents, with zero refusals on that batch ([mycroft e994422](https://github.com/nikbearbrown/mycroft/commit/e99442238a43e1806ecbd425777a817f5fee3715)).
- Started the Lineage Agent: backward citations, and the empty-string bug found and fixed ([mycroft ff4b369](https://github.com/nikbearbrown/mycroft/commit/ff4b369fde0aabce2bc1b0c63f9def8b0948dd4f)).
- Progress videos 5, on broadening the test ([5fd9625c](https://github.com/nikbearbrown/humanitarians-youtube/commit/5fd9625c8a669908892fa2d33262e6e9c2bb6b07), [PR #106](https://github.com/nikbearbrown/humanitarians-youtube/pull/106)), and 6, on starting the lineage agent ([57d02a45](https://github.com/nikbearbrown/humanitarians-youtube/commit/57d02a455dd0ea49509c016e1036e0d03b103d7e), [PR #107](https://github.com/nikbearbrown/humanitarians-youtube/pull/107)). All of these commits are dated 2026-09-11.
- The Schema Drift explainer folder is dated 2026-09-11. It was committed on 2026-09-12 and is linked under next week.

**Evidence folders:** [2026-09-11-patent-agent-video5-broadening-the-test](../2026-09-11-patent-agent-video5-broadening-the-test/), [2026-09-11-patent-agent-video6-starting-lineage-agent](../2026-09-11-patent-agent-video6-starting-lineage-agent/), [2026-09-11-schema-drift](../2026-09-11-schema-drift/)

**Videos:** Project Videos: Broadening the Test; Starting the Lineage Agent. STEM Video: Schema Drift ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-09-12 - 2026-09-18: The two agents wired together (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Broadened Lineage Agent testing to 2 more real patents and confirmed international citation formats ([mycroft cf4f9f1](https://github.com/nikbearbrown/mycroft/commit/cf4f9f13c01ed09220bde1a86d67aa6061932993), 2026-09-18).
- Progress video 7, on the two agents wired together, with a real CLI recording ([c7cd8270](https://github.com/nikbearbrown/humanitarians-youtube/commit/c7cd82707412603455ee77f8f91268fdaf14797e), [PR #129](https://github.com/nikbearbrown/humanitarians-youtube/pull/129), 2026-09-18).
- STEM explainers:
  - Schema Drift ([bc35151e](https://github.com/nikbearbrown/humanitarians-youtube/commit/bc35151eb3e4a6bfd75f5e7d71ab275d71bb263c), [PR #113](https://github.com/nikbearbrown/humanitarians-youtube/pull/113), 2026-09-12);
  - The Finance Agent Market, Right Now ([be0b4a5b](https://github.com/nikbearbrown/humanitarians-youtube/commit/be0b4a5b7ba42ca9b8a081bb907f4b4a450f97d6), [PR #114](https://github.com/nikbearbrown/humanitarians-youtube/pull/114), 2026-09-12);
  - Why AI Models Refuse ([0f9759fa](https://github.com/nikbearbrown/humanitarians-youtube/commit/0f9759fa50011fc4ce62a06b4b40cf24740cce85), [PR #132](https://github.com/nikbearbrown/humanitarians-youtube/pull/132), 2026-09-18).

**Evidence folders:** [2026-09-18-patent-agent-video7-two-agents-wired-together](../2026-09-18-patent-agent-video7-two-agents-wired-together/), [2026-09-12-finance-agent-market-2026](../2026-09-12-finance-agent-market-2026/), [2026-09-18-why-ai-models-refuse](../2026-09-18-why-ai-models-refuse/)

**Videos:** Project Video: The Two Agents, Wired Together. STEM Videos: The Finance Agent Market, Right Now; Why AI Models Refuse ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-09-19 - 2026-09-25: Gap

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- **Gap.** Neither repository has a commit dated this week, and no work folder is dated in it. There's no evidence to link for this week.

**Evidence folder:** none

**Videos:** none

### 2026-09-26 - 2026-10-02: From CLI to API, and the React frontend (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Added the FastAPI backend wrapping ClaimsAgent and LineageAgent ([mycroft f85d177](https://github.com/nikbearbrown/mycroft/commit/f85d17728fdcaba975e133441eb09c7136ec1185), [PR #55](https://github.com/nikbearbrown/mycroft/pull/55), 2026-09-30).
- Updated the README with corrected lineage numbers and documentation for `patent_reader.py` and `api.py` ([mycroft 46af37c](https://github.com/nikbearbrown/mycroft/commit/46af37ce5ada9480822b1d0344ff4aada1c46e62), 2026-09-30).
- Reorganized the project into a backend/frontend split and added the React frontend ([mycroft 85c2ce0](https://github.com/nikbearbrown/mycroft/commit/85c2ce020063de317f3ad6b558dbf841bbc2befa), [PR #56](https://github.com/nikbearbrown/mycroft/pull/56), 2026-10-02). Restored `load_dotenv()` after it was missed in that move ([mycroft 10df6ba](https://github.com/nikbearbrown/mycroft/commit/10df6ba3ff225a2c4cd03e54bb64a2e04a9dd98a), [PR #57](https://github.com/nikbearbrown/mycroft/pull/57)).
- Progress videos 8, From CLI to API ([3257add3](https://github.com/nikbearbrown/humanitarians-youtube/commit/3257add3b0b9e76454cf7d4fab3da83c61e9b804), [PR #194](https://github.com/nikbearbrown/humanitarians-youtube/pull/194), 2026-09-30), and 9, Building the Frontend ([c62d4b37](https://github.com/nikbearbrown/humanitarians-youtube/commit/c62d4b37debc64276f4a496b7b6b27c86ecdf6df), [PR #202](https://github.com/nikbearbrown/humanitarians-youtube/pull/202), 2026-10-02).
- STEM explainers: What Is an Agent Harness? ([3e48f6b4](https://github.com/nikbearbrown/humanitarians-youtube/commit/3e48f6b4764e4be7735ab26015ad8bf1c61ba349), [PR #195](https://github.com/nikbearbrown/humanitarians-youtube/pull/195), 2026-09-30) and What Is AI Red Teaming? ([3f22af06](https://github.com/nikbearbrown/humanitarians-youtube/commit/3f22af0684089a6e752294d0f290571d6c0eafe1), [PR #204](https://github.com/nikbearbrown/humanitarians-youtube/pull/204), 2026-10-02).

**Evidence folders:** [2026-09-30-patent-agent-video8-cli-to-api](../2026-09-30-patent-agent-video8-cli-to-api/), [2026-10-02-building-the-frontend](../2026-10-02-building-the-frontend/), [2026-09-30-what-is-an-agent-harness](../2026-09-30-what-is-an-agent-harness/), [2026-10-02-what-is-ai-red-teaming](../2026-10-02-what-is-ai-red-teaming/)

**Videos:** Project Videos: From CLI to API; Building the Frontend. STEM Videos: What Is an Agent Harness?; What Is AI Red Teaming? ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-10-03 - 2026-10-09: Gap

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- **Gap.** Neither repository has a commit dated this week, and no work folder is dated in it. There's no evidence to link for this week.

**Evidence folder:** none

**Videos:** none

### 2026-10-10 - 2026-10-16: Hardening the frontend (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- Hardened the React frontend ([mycroft 00d3baa](https://github.com/nikbearbrown/mycroft/commit/00d3baa65e13b17ba8bb660b0fdef58df52b2bc1), [PR #65](https://github.com/nikbearbrown/mycroft/pull/65), 2026-10-12):
  - three distinct error messages;
  - a loading spinner with a hint for the slow classify path;
  - inputs disabled during a fetch;
  - classify off by default.
- Progress video 10, Hardening the Frontend ([fb0bb25f](https://github.com/nikbearbrown/humanitarians-youtube/commit/fb0bb25fdf18375b477382212030cda00421fa29), [PR #244](https://github.com/nikbearbrown/humanitarians-youtube/pull/244)), and the STEM explainer What Is Prompt Injection? ([49402aa9](https://github.com/nikbearbrown/humanitarians-youtube/commit/49402aa93ced4e5281db78c435ab5dee8028f4dc), [PR #245](https://github.com/nikbearbrown/humanitarians-youtube/pull/245)), both 2026-10-12.

**Evidence folders:** [2026-10-12-hardening-the-frontend](../2026-10-12-hardening-the-frontend/) ([frictional log](../2026-10-12-hardening-the-frontend/FRICTIONAL.md)), [2026-10-12-what-is-prompt-injection](../2026-10-12-what-is-prompt-injection/)

**Videos:** Project Video: Hardening the Frontend. STEM Video: What Is Prompt Injection? ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

### 2026-10-17 - 2026-10-23: Gap

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- **Gap.** Neither repository has a commit dated this week, and no work folder is dated in it.
- I report local development and debugging between 19 and 25 October (my own report), with no committed artifact from it.

**Evidence folder:** none

**Videos:** none

### 2026-10-24 - 2026-10-29: Measuring the classifier, and the first baseline (Mycroft Patent Reader)

**Hours completed:** ~25-30 (self-reported)

**Work completed:**

- **27 Oct:** built the classifier evaluation harness and the BigQuery pull: one query, 161.8 GB, $0.92 at list price, 160 candidate patents. The real data changed the plan: 147 of 160 patents have only 1-3 independent claims, so the set became 50 claims from 16 patents.
- **29 Oct:** labelled all 50 claims by hand and ran the baseline (cost upper bound $0.32; actual cost not recorded).
  - Breadth: accuracy 0.66, kappa 0.08.
  - Posture: accuracy 0.60, kappa 0.00.
  - Both fall below the always-most-common-answer baseline.
  - All 50 posture labels are defensive, so posture agreement can't be measured on this set.
- **29 Oct:** fixed the refusal bug in `claim_classifier.py`, so a refusal partway through an answer is now treated as declined, and all 50 claims score.
- Evidence:
  - The code, labels and results are in [mycroft 3bcf1b1](https://github.com/nikbearbrown/mycroft/commit/3bcf1b1cea28265bb89bfea85f4034b6b7da37f0) ([PR #76](https://github.com/nikbearbrown/mycroft/pull/76), 2026-10-29).
  - Progress videos 11 ([aa97f2ce](https://github.com/nikbearbrown/humanitarians-youtube/commit/aa97f2ce8ae88c4953cb6174ef6186fb990d1ccd), [PR #308](https://github.com/nikbearbrown/humanitarians-youtube/pull/308), 2026-10-28) and 12 ([7c165d76](https://github.com/nikbearbrown/humanitarians-youtube/commit/7c165d76550648aecfaf4e411ee6d1c1bf7260cf), [PR #319](https://github.com/nikbearbrown/humanitarians-youtube/pull/319), 2026-10-29).
  - STEM explainers What Is RLHF? ([f1314c95](https://github.com/nikbearbrown/humanitarians-youtube/commit/f1314c95479777839910cc3ecf906aa3da242730), [PR #317](https://github.com/nikbearbrown/humanitarians-youtube/pull/317)) and How AI Agents Are Changing Payments ([0cc27d30](https://github.com/nikbearbrown/humanitarians-youtube/commit/0cc27d309304d2e53f90bedde634652ce6181889), [PR #321](https://github.com/nikbearbrown/humanitarians-youtube/pull/321)), both 2026-10-29.

**Evidence folders:** [2026-10-28-patent-agent-video11-classifier-eval-harness](../2026-10-28-patent-agent-video11-classifier-eval-harness/) ([frictional log](../2026-10-28-patent-agent-video11-classifier-eval-harness/FRICTIONAL.md)), [2026-10-29-patent-agent-video12-baseline-results](../2026-10-29-patent-agent-video12-baseline-results/) ([frictional log](../2026-10-29-patent-agent-video12-baseline-results/FRICTIONAL.md)), [2026-10-29-what-is-rlhf](../2026-10-29-what-is-rlhf/), [2026-10-29-how-ai-agents-are-changing-payments](../2026-10-29-how-ai-agents-are-changing-payments/)

**Videos:** Project Videos: Measuring the Classifier; What the Baseline Found. STEM Videos: What Is RLHF?; How AI Agents Are Changing Payments ([Drive folder](https://drive.google.com/drive/folders/1XbqBd1aPhlHIYKBQBL3cPPeqFzhPYcB6))

---

**Total: ~325-390 hours across 13 weeks (self-reported, ~25-30 per week).** Eight weeks have committed evidence. Five weeks (8-14 Aug, 15-21 Aug, 19-25 Sep, 3-9 Oct, 17-23 Oct) have no commit or dated folder.

## Next period

- **Prompt fix and re-measurement.** Make one prompt change so functional wording alone does not count as broad, and posture is judged separately from breadth. Then re-run the 50 claims and compare the two runs with the harness. Target date: 2026-11-15.
- **Better posture coverage.** Add offensive and broad claims to the test set, so posture agreement can actually be measured. Target date: 2026-11-15.

## Outstanding issues

- **Hours** are self-reported estimates, not a documented hours log. Five weeks have no committed evidence.
- **Supervisor:** the supervisor for 1 August - 11 October isn't stated, and no supervisor feedback evidence is linked.
- **Videos** are linked to one Drive folder rather than to each video.
- **Baseline cost:** the actual cost wasn't recorded; the harness logged only the $0.32 upper bound.
- **Open items on the patent system:** deployment hasn't started, forward citations are deferred, and the zero-citation case is still untested.
