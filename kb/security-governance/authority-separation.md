---
{
  "type": "technique",
  "id": "authority-separation",
  "title": "Separate database, backup, development and deployment authority at real access boundaries",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-20T17:17:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
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

# Separate database, backup, development and deployment authority at real access boundaries

## What

Separate database, backup, development and deployment authority at real access boundaries

An overprivileged development token can destroy both primary data and recovery copies, defeating ordinary backup protection.

## Evidence

> production database being deleted. The backups were also deleted, and so a
> — 02:59 [^cgimkNGNjvU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
