---
{
  "type": "technique",
  "id": "portable-task-bundle",
  "title": "Package instruction, environment and authoritative verifier as one reproducible task bundle",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-07T17:00:07Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "jRCpXUjz4CI",
      "resource": "https://www.youtube.com/watch?v=jRCpXUjz4CI",
      "title": "Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute",
      "author": "Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute",
      "last_modified": "2026-07-24T16:00:06Z",
      "analysis_file": "analysis/jRCpXUjz4CI.json"
    },
    {
      "id": "oWTEiYpxl80",
      "resource": "https://www.youtube.com/watch?v=oWTEiYpxl80",
      "title": "Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind",
      "author": "Philipp Schmid, Google DeepMind",
      "last_modified": "2026-10-07T17:00:07Z",
      "analysis_file": "analysis/oWTEiYpxl80.json"
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

# Package instruction, environment and authoritative verifier as one reproducible task bundle

## What

Package instruction, environment and authoritative verifier as one reproducible task bundle

A versioned directory holds instructions, environment setup and a verifier, making tasks reproducible across execution providers.

## Evidence

> then it can easily pass between hands and becomes interoperable. Um and then
> — 09:05 [^jRCpXUjz4CI]

> agent is just files. So we have an agents MD file inside our environment.
> — 16:48 [^oWTEiYpxl80]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^jRCpXUjz4CI]: [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](https://www.youtube.com/watch?v=jRCpXUjz4CI); publication: 2026-07-24T16:00:06Z; analysis: `analysis/jRCpXUjz4CI.json`.
[^oWTEiYpxl80]: [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=oWTEiYpxl80); publication: 2026-10-07T17:00:07Z; analysis: `analysis/oWTEiYpxl80.json`.
