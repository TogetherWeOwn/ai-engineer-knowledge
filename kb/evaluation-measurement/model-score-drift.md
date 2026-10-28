---
{
  "type": "technique",
  "id": "model-score-drift",
  "title": "Use observable score-distribution drift only when the endpoint exposes valid comparable signals",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-09-19T18:30:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "btxG75rNJC4",
      "resource": "https://www.youtube.com/watch?v=btxG75rNJC4",
      "title": "Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer",
      "author": "Asaf Gardin & Yuval Belfer",
      "last_modified": "2026-09-19T18:30:06Z",
      "analysis_file": "analysis/btxG75rNJC4.json"
    },
    {
      "id": "hqHC6Z_lXyo",
      "resource": "https://www.youtube.com/watch?v=hqHC6Z_lXyo",
      "title": "20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna",
      "author": "Bertrand Charpentier, Pruna",
      "last_modified": "2026-06-01T17:00:06Z",
      "analysis_file": "analysis/hqHC6Z_lXyo.json"
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

# Use observable score-distribution drift only when the endpoint exposes valid comparable signals

## What

Use observable score-distribution drift only when the endpoint exposes valid comparable signals

Different leaderboards cover different models, tasks and raters; rankings and Elo scales are not interchangeable.

## Evidence

Source analysis [^btxG75rNJC4]; no independently matched timestamped quote published.

> And usually, the main solution for this is not to trust a single one, but you
> — 03:52 [^hqHC6Z_lXyo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^btxG75rNJC4]: [Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story — Asaf Gardin & Yuval Belfer](https://www.youtube.com/watch?v=btxG75rNJC4); publication: 2026-09-19T18:30:06Z; analysis: `analysis/btxG75rNJC4.json`.
[^hqHC6Z_lXyo]: [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](https://www.youtube.com/watch?v=hqHC6Z_lXyo); publication: 2026-06-01T17:00:06Z; analysis: `analysis/hqHC6Z_lXyo.json`.
