---
{
  "type": "technique",
  "id": "reward-hacking-measurement",
  "title": "Measure suspicious shortcuts separately from confirmed verifier bypasses",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-09-26T16:30:29Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Rx8f05JI_WA",
      "resource": "https://www.youtube.com/watch?v=Rx8f05JI_WA",
      "title": "SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI",
      "author": "Rishi Desai, Abundant AI",
      "last_modified": "2026-07-07T03:45:51Z",
      "analysis_file": "analysis/Rx8f05JI_WA.json"
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

# Measure suspicious shortcuts separately from confirmed verifier bypasses

## What

Measure suspicious shortcuts separately from confirmed verifier bypasses

Attempt rate, shipped exploit rate and rewarded bypass rate distinguish attack pressure from verifier effectiveness.

## Evidence

> Zero rollouts earned reward through an exploit, because our defenses caught
> — 10:08 [^Rx8f05JI_WA]

> hide all the interesting failures. Instead you want a balanced scorecard.
> — 13:20 [^x4e5O9zN0TE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Rx8f05JI_WA]: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA); publication: 2026-07-07T03:45:51Z; analysis: `analysis/Rx8f05JI_WA.json`.
[^x4e5O9zN0TE]: [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](https://www.youtube.com/watch?v=x4e5O9zN0TE); publication: 2026-09-26T16:30:29Z; analysis: `analysis/x4e5O9zN0TE.json`.
