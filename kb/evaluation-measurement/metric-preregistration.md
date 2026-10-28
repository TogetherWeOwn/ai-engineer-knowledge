---
{
  "type": "technique",
  "id": "metric-preregistration",
  "title": "Declare the evaluation instrument, predictions and stopping rules before observing new results",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-06-25T16:30:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "IJXjTLPzvAU",
      "resource": "https://www.youtube.com/watch?v=IJXjTLPzvAU",
      "title": "The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen",
      "author": "Jacob E. Thomas, Results Gen",
      "last_modified": "2026-06-25T16:30:06Z",
      "analysis_file": "analysis/IJXjTLPzvAU.json"
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

# Declare the evaluation instrument, predictions and stopping rules before observing new results

## What

Declare the evaluation instrument, predictions and stopping rules before observing new results

Moments, conditions, questions, weighted rubric and predicted directions are locked and timestamped before any response is collected, so results can't be accused of cherry-picking.

## Evidence

Source analysis [^IJXjTLPzvAU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^IJXjTLPzvAU]: [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](https://www.youtube.com/watch?v=IJXjTLPzvAU); publication: 2026-06-25T16:30:06Z; analysis: `analysis/IJXjTLPzvAU.json`.
