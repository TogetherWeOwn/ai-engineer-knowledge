---
{
  "type": "technique",
  "id": "noncompensable-quality-criteria",
  "title": "Make critical quality dimensions non-compensable by a high aggregate score",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-05T22:00:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "JvosMkuNxF8",
      "resource": "https://www.youtube.com/watch?v=JvosMkuNxF8",
      "title": "Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford",
      "author": "Yegor Denisov-Blanch, Stanford",
      "last_modified": "2025-12-11T21:56:44Z",
      "analysis_file": "analysis/JvosMkuNxF8.json"
    },
    {
      "id": "jxrGodnopHo",
      "resource": "https://www.youtube.com/watch?v=jxrGodnopHo",
      "title": "[Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)",
      "author": "David Karam, Pi Labs (fmr Google Search)",
      "last_modified": "2025-07-29T00:29:21Z",
      "analysis_file": "analysis/jxrGodnopHo.json"
    },
    {
      "id": "qZj7sqmidqA",
      "resource": "https://www.youtube.com/watch?v=qZj7sqmidqA",
      "title": "From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-05T22:00:36Z",
      "analysis_file": "analysis/qZj7sqmidqA.json"
    },
    {
      "id": "vNCY9kXXyDQ",
      "resource": "https://www.youtube.com/watch?v=vNCY9kXXyDQ",
      "title": "Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse",
      "author": "Marc Klingen, Clickhouse",
      "last_modified": "2026-05-20T15:00:06Z",
      "analysis_file": "analysis/vNCY9kXXyDQ.json"
    },
    {
      "id": "x4e5O9zN0TE",
      "resource": "https://www.youtube.com/watch?v=x4e5O9zN0TE",
      "title": "Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati",
      "author": "Erina Karati",
      "last_modified": "2026-09-26T16:30:29Z",
      "analysis_file": "analysis/x4e5O9zN0TE.json"
    }
  ],
  "relations": [],
  "relation_transitions": {},
  "generated": {
    "by": "scripts/generate_claims.py",
    "at": "2026-10-28T21:30:11.661690Z"
  },
  "stale_after": "2027-01-26T21:30:11.661690Z"
}
---

# Make critical quality dimensions non-compensable by a high aggregate score

## What

Make critical quality dimensions non-compensable by a high aggregate score

Aggregation must allow a safety-critical failure to veto the overall score rather than being offset by many successful minor dimensions.

## Evidence

> healthy while increasing the primary metric to whatever degree possible.
> — 12:48 [^JvosMkuNxF8]

> what should I some if something fails I should fail everything for example,
> — 34:30 [^jxrGodnopHo]

> are guard rails. They're ship blockers. If an agent hallucinates a stock price,
> — 1:19:34 [^qZj7sqmidqA]

> like the target function really matters. Like I think it's it sounds obvious, but
> — 15:14 [^vNCY9kXXyDQ]

> like a ratchet. Try a change, score it, keep it only if the scorecard improves
> — 18:09 [^x4e5O9zN0TE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^JvosMkuNxF8]: [Can you prove AI ROI in Software Eng? (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford](https://www.youtube.com/watch?v=JvosMkuNxF8); publication: 2025-12-11T21:56:44Z; analysis: `analysis/JvosMkuNxF8.json`.
[^jxrGodnopHo]: [[Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)](https://www.youtube.com/watch?v=jxrGodnopHo); publication: 2025-07-29T00:29:21Z; analysis: `analysis/jxrGodnopHo.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^vNCY9kXXyDQ]: [Skill issue: Lessons from skilling up coding agents to use Langfuse - Marc Klingen, Clickhouse](https://www.youtube.com/watch?v=vNCY9kXXyDQ); publication: 2026-05-20T15:00:06Z; analysis: `analysis/vNCY9kXXyDQ.json`.
[^x4e5O9zN0TE]: [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](https://www.youtube.com/watch?v=x4e5O9zN0TE); publication: 2026-09-26T16:30:29Z; analysis: `analysis/x4e5O9zN0TE.json`.
