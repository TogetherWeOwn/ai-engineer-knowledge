---
{
  "type": "technique",
  "id": "domain-judge-contracts",
  "title": "Use narrow domain-specific semantic judges only where objective validators are insufficient",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-07-25T23:00:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "O72p-rBb2bA",
      "resource": "https://www.youtube.com/watch?v=O72p-rBb2bA",
      "title": "Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind",
      "author": "Akele Reed & Dave Revere, SonderMind",
      "last_modified": "2026-07-25T23:00:36Z",
      "analysis_file": "analysis/O72p-rBb2bA.json"
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

# Use narrow domain-specific semantic judges only where objective validators are insufficient

## What

Use narrow domain-specific semantic judges only where objective validators are insufficient

They disabled the frontier providers' built-in guardrails because they over-filtered their eval data, and built their own domain-specific judges calibrated with clinicians.

## Evidence

Source analysis [^O72p-rBb2bA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^O72p-rBb2bA]: [Evals-Driven Development for a Mental Health AI Coach — Akele Reed & Dave Revere, SonderMind](https://www.youtube.com/watch?v=O72p-rBb2bA); publication: 2026-07-25T23:00:36Z; analysis: `analysis/O72p-rBb2bA.json`.
