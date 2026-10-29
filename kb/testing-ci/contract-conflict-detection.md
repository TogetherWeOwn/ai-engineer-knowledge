---
{
  "type": "technique",
  "id": "contract-conflict-detection",
  "title": "Detect incompatible concurrent API and data-contract changes before merge",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-08-20T13:30:38Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "s-aixZYJG4c",
      "resource": "https://www.youtube.com/watch?v=s-aixZYJG4c",
      "title": "The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo",
      "author": "Itamar Friedman, Qodo",
      "last_modified": "2026-08-20T13:30:38Z",
      "analysis_file": "analysis/s-aixZYJG4c.json"
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

# Detect incompatible concurrent API and data-contract changes before merge

## What

Detect incompatible concurrent API and data-contract changes before merge

Inspect in-flight changes together to identify incompatible contract edits, not just textual merge conflicts.

## Evidence

> contracts? What is working? What is not working? What are two PRs are going to
> — 16:39 [^s-aixZYJG4c]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^s-aixZYJG4c]: [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=s-aixZYJG4c); publication: 2026-08-20T13:30:38Z; analysis: `analysis/s-aixZYJG4c.json`.
