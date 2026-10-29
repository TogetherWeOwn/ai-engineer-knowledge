---
{
  "type": "technique",
  "id": "guard-scope-fixtures",
  "title": "Scope enforcement so deliberately bad fixtures remain testable without weakening production rules",
  "area": "testing-ci",
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

# Scope enforcement so deliberately bad fixtures remain testable without weakening production rules

## What

Scope enforcement so deliberately bad fixtures remain testable without weakening production rules

A scanner/fixer needs workspace context; automatic remediation can otherwise alter intentionally vulnerable benchmark inputs and corrupt validation.

## Evidence

> different workspace what I want to apply to each one of those.
> — 15:57 [^cgimkNGNjvU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
