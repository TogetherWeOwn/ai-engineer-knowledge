---
{
  "type": "technique",
  "id": "dependency-fix-closure",
  "title": "Update the smallest dependency closure that actually removes a vulnerability",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-20T17:17:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LqLoYksJ6do",
      "resource": "https://www.youtube.com/watch?v=LqLoYksJ6do",
      "title": "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3",
      "author": "Moritz Johner, Form3",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/LqLoYksJ6do.json"
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

# Update the smallest dependency closure that actually removes a vulnerability

## What

Update the smallest dependency closure that actually removes a vulnerability

Update only versions needed to fix the finding, including coupled runtime/linter changes, then rebuild and rescan to prove remediation.

## Evidence

> risk, which we want to avoid. So just bump to the version that actually fixes
> — 06:20 [^LqLoYksJ6do]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
