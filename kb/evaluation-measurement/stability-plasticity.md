---
{
  "type": "technique",
  "id": "stability-plasticity",
  "title": "Distinguish adaptation failures from unstable behavior before changing memory or prompts",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-08-12T16:00:08Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "I6aiEf3aEFQ",
      "resource": "https://www.youtube.com/watch?v=I6aiEf3aEFQ",
      "title": "Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition",
      "author": "Yu Su, NeoCognition",
      "last_modified": "2026-08-12T16:00:08Z",
      "analysis_file": "analysis/I6aiEf3aEFQ.json"
    },
    {
      "id": "iqloyWCGYQQ",
      "resource": "https://www.youtube.com/watch?v=iqloyWCGYQQ",
      "title": "Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley",
      "author": "Parth Asawa, UC Berkeley",
      "last_modified": "2026-08-12T14:00:19Z",
      "analysis_file": "analysis/iqloyWCGYQQ.json"
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

# Distinguish adaptation failures from unstable behavior before changing memory or prompts

## What

Distinguish adaptation failures from unstable behavior before changing memory or prompts

Classifies continual-learning failure modes into stability failures (not retaining prior information, e.g. reverting to an earlier wrong prediction) and plasticity failures (not updating priors from new evidence, e.g. dismissing a schema as irrelevant when it applies).

## Evidence

Source analysis [^I6aiEf3aEFQ]; no independently matched timestamped quote published.

Source analysis [^iqloyWCGYQQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^I6aiEf3aEFQ]: [Intelligence + Continual Learning = Expertise — Yu Su, NeoCognition](https://www.youtube.com/watch?v=I6aiEf3aEFQ); publication: 2026-08-12T16:00:08Z; analysis: `analysis/I6aiEf3aEFQ.json`.
[^iqloyWCGYQQ]: [Beyond Static Intelligence: Evaluating Continual Learning — Parth Asawa, UC Berkeley](https://www.youtube.com/watch?v=iqloyWCGYQQ); publication: 2026-08-12T14:00:19Z; analysis: `analysis/iqloyWCGYQQ.json`.
