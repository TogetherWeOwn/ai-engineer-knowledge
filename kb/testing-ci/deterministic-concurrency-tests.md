---
{
  "type": "technique",
  "id": "deterministic-concurrency-tests",
  "title": "Reproduce concurrency defects with seeded scheduling and controlled interleavings",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2025-06-27T09:22:37Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "WXy8Yy9xGss",
      "resource": "https://www.youtube.com/watch?v=WXy8Yy9xGss",
      "title": "CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed",
      "author": "Nathan Sobo, Zed",
      "last_modified": "2025-06-27T09:22:37Z",
      "analysis_file": "analysis/WXy8Yy9xGss.json"
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

# Reproduce concurrency defects with seeded scheduling and controlled interleavings

## What

Reproduce concurrency defects with seeded scheduling and controlled interleavings

Control scheduling and network interleavings so a rare race can be replayed exactly, isolated and fixed instead of dismissed as a flaky integration test.

## Evidence

Source analysis [^WXy8Yy9xGss]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^WXy8Yy9xGss]: [CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed](https://www.youtube.com/watch?v=WXy8Yy9xGss); publication: 2025-06-27T09:22:37Z; analysis: `analysis/WXy8Yy9xGss.json`.
