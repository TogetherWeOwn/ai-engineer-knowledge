---
{
  "type": "technique",
  "id": "invariant-sentinels",
  "title": "Add targeted inexpensive invariant sentinels around risky changes",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-04-28T18:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
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

# Add targeted inexpensive invariant sentinels around risky changes

## What

Add targeted inexpensive invariant sentinels around risky changes

Run narrow checks on sensitive paths instead of a broad expensive reviewer panel on every PR.

## Evidence

> that like looks specifically for very very uh specific invariants um of the
> — 39:53 [^rnDm57Py54A]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
