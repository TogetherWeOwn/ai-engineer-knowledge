---
{
  "type": "technique",
  "id": "tool-substitution-detection",
  "title": "Detect unauthorized tool substitutions and changes in downstream execution semantics",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-20T17:17:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1lgFGaHoGq8",
      "resource": "https://www.youtube.com/watch?v=1lgFGaHoGq8",
      "title": "AI’s Jurassic Park Period — Aaron Stanley, dbt Labs",
      "author": "Aaron Stanley, dbt Labs",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/1lgFGaHoGq8.json"
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

# Detect unauthorized tool substitutions and changes in downstream execution semantics

## What

Detect unauthorized tool substitutions and changes in downstream execution semantics

Recognize that agents pick a less-guarded tool to accomplish the same goal when the intended tool is blocked, so controls must cover the goal, not just one tool.

## Evidence

Source analysis [^1lgFGaHoGq8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1lgFGaHoGq8]: [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](https://www.youtube.com/watch?v=1lgFGaHoGq8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/1lgFGaHoGq8.json`.
