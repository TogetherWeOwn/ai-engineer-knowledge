---
{
  "type": "technique",
  "id": "formal-verification",
  "title": "Use formal or symbolic checks for narrow high-consequence invariants",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2025-11-24T20:16:38Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "qLqttdO33UM",
      "resource": "https://www.youtube.com/watch?v=qLqttdO33UM",
      "title": "Vision: Zero Bugs — Johann Schleier-Smith, Temporal",
      "author": "Johann Schleier-Smith, Temporal",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qLqttdO33UM.json"
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

# Use formal or symbolic checks for narrow high-consequence invariants

## What

Use formal or symbolic checks for narrow high-consequence invariants

Use inline assertions/proofs (Dafny-style) on small critical functions, verified before the generated code runs, rather than across the whole codebase.

## Evidence

Source analysis [^qLqttdO33UM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^qLqttdO33UM]: [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](https://www.youtube.com/watch?v=qLqttdO33UM); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qLqttdO33UM.json`.
