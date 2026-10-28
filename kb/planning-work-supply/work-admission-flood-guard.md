---
{
  "type": "technique",
  "id": "work-admission-flood-guard",
  "title": "Prevent issue and wake floods with deterministic deduplication and bounded ready-work admission",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-08-11T00:03:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "aeTb5BdmTTc",
      "resource": "https://www.youtube.com/watch?v=aeTb5BdmTTc",
      "title": "Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab",
      "author": "Aditya Khandelwal, Amazon AGI Lab",
      "last_modified": "2026-08-11T00:03:17Z",
      "analysis_file": "analysis/aeTb5BdmTTc.json"
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

# Prevent issue and wake floods with deterministic deduplication and bounded ready-work admission

## What

Prevent issue and wake floods with deterministic deduplication and bounded ready-work admission

Uncoordinated agents can create hundreds of low-value issues faster than a team can complete them.

## Evidence

Source analysis [^aeTb5BdmTTc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^aeTb5BdmTTc]: [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](https://www.youtube.com/watch?v=aeTb5BdmTTc); publication: 2026-08-11T00:03:17Z; analysis: `analysis/aeTb5BdmTTc.json`.
