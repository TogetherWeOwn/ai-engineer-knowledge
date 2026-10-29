---
{
  "type": "technique",
  "id": "performance-contracts",
  "title": "Define performance targets on real workload shapes with quality and resource constraints",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-05-31T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "N7b1PJc7SFc",
      "resource": "https://www.youtube.com/watch?v=N7b1PJc7SFc",
      "title": "Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI",
      "author": "Rishabh Bhargava, Together AI",
      "last_modified": "2026-05-31T16:00:06Z",
      "analysis_file": "analysis/N7b1PJc7SFc.json"
    },
    {
      "id": "tHN44yJoeS8",
      "resource": "https://www.youtube.com/watch?v=tHN44yJoeS8",
      "title": "Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor",
      "author": "Naman Jain, Cursor",
      "last_modified": "2025-12-15T17:18:09Z",
      "analysis_file": "analysis/tHN44yJoeS8.json"
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

# Define performance targets on real workload shapes with quality and resource constraints

## What

Define performance targets on real workload shapes with quality and resource constraints

Derive optimization tasks from real commits and pair correctness checks with explicit workload runtime measurements.

## Evidence

Source analysis [^N7b1PJc7SFc]; no independently matched timestamped quote published.

Source analysis [^tHN44yJoeS8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^N7b1PJc7SFc]: [Engineering voice agents: Latency, quality, and scale — Rishabh Bhargava, Together AI](https://www.youtube.com/watch?v=N7b1PJc7SFc); publication: 2026-05-31T16:00:06Z; analysis: `analysis/N7b1PJc7SFc.json`.
[^tHN44yJoeS8]: [Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor](https://www.youtube.com/watch?v=tHN44yJoeS8); publication: 2025-12-15T17:18:09Z; analysis: `analysis/tHN44yJoeS8.json`.
