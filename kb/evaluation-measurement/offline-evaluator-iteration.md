---
{
  "type": "technique",
  "id": "offline-evaluator-iteration",
  "title": "Reuse saved outputs when iterating on evaluators instead of rerunning inference",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-19T14:06:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "UGjk3Uk0MxM",
      "resource": "https://www.youtube.com/watch?v=UGjk3Uk0MxM",
      "title": "The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft",
      "author": "Pamela Fox, Microsoft",
      "last_modified": "2026-10-19T14:06:53Z",
      "analysis_file": "analysis/UGjk3Uk0MxM.json"
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

# Reuse saved outputs when iterating on evaluators instead of rerunning inference

## What

Reuse saved outputs when iterating on evaluators instead of rerunning inference

Freezing input/output/tool traces lets evaluator changes be assessed without rerunning expensive generation.

## Evidence

Source analysis [^UGjk3Uk0MxM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^UGjk3Uk0MxM]: [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](https://www.youtube.com/watch?v=UGjk3Uk0MxM); publication: 2026-10-19T14:06:53Z; analysis: `analysis/UGjk3Uk0MxM.json`.
