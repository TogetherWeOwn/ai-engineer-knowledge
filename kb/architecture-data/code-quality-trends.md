---
{
  "type": "technique",
  "id": "code-quality-trends",
  "title": "Track complexity, warning deltas and copy-paste growth as leading indicators of maintenance risk",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2025-06-10T17:30:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "5s6Q-y42ZZA",
      "resource": "https://www.youtube.com/watch?v=5s6Q-y42ZZA",
      "title": "The Many Ends of Programming - Ray Myers",
      "author": "Ray Myers",
      "last_modified": "2025-06-10T17:30:11Z",
      "analysis_file": "analysis/5s6Q-y42ZZA.json"
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

# Track complexity, warning deltas and copy-paste growth as leading indicators of maintenance risk

## What

Track complexity, warning deltas and copy-paste growth as leading indicators of maintenance risk

Flags that 2024 was the first year copy-pasted code exceeded refactored code, a red flag for tech debt.

## Evidence

Source analysis [^5s6Q-y42ZZA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^5s6Q-y42ZZA]: [The Many Ends of Programming - Ray Myers](https://www.youtube.com/watch?v=5s6Q-y42ZZA); publication: 2025-06-10T17:30:11Z; analysis: `analysis/5s6Q-y42ZZA.json`.
