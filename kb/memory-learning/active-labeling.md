---
{
  "type": "technique",
  "id": "active-labeling",
  "title": "Prioritize uncertain and high-impact cases for labeling",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-08-28T15:00:03Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "bMjlRrWjdT0",
      "resource": "https://www.youtube.com/watch?v=bMjlRrWjdT0",
      "title": "AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "author": "Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "last_modified": "2026-08-28T15:00:03Z",
      "analysis_file": "analysis/bMjlRrWjdT0.json"
    },
    {
      "id": "lCBf9slCanI",
      "resource": "https://www.youtube.com/watch?v=lCBf9slCanI",
      "title": "Ending AI Slop — Thais Castello Branco, Taste Labs",
      "author": "Thais Castello Branco, Taste Labs",
      "last_modified": "2026-07-31T19:26:20Z",
      "analysis_file": "analysis/lCBf9slCanI.json"
    },
    {
      "id": "wEc9aG7cRQc",
      "resource": "https://www.youtube.com/watch?v=wEc9aG7cRQc",
      "title": "Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog",
      "author": "Diane Lin, Datadog",
      "last_modified": "2026-07-20T06:25:22Z",
      "analysis_file": "analysis/wEc9aG7cRQc.json"
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

# Prioritize uncertain and high-impact cases for labeling

## What

Prioritize uncertain and high-impact cases for labeling

Select historically conflicting verdicts for investigation rather than label every output; disagreement can concentrate useful examples but agreement does not certify truth.

## Evidence

Source analysis [^bMjlRrWjdT0]; no independently matched timestamped quote published.

Source analysis [^lCBf9slCanI]; no independently matched timestamped quote published.

Source analysis [^wEc9aG7cRQc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^bMjlRrWjdT0]: [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](https://www.youtube.com/watch?v=bMjlRrWjdT0); publication: 2026-08-28T15:00:03Z; analysis: `analysis/bMjlRrWjdT0.json`.
[^lCBf9slCanI]: [Ending AI Slop — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=lCBf9slCanI); publication: 2026-07-31T19:26:20Z; analysis: `analysis/lCBf9slCanI.json`.
[^wEc9aG7cRQc]: [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](https://www.youtube.com/watch?v=wEc9aG7cRQc); publication: 2026-07-20T06:25:22Z; analysis: `analysis/wEc9aG7cRQc.json`.
