---
{
  "type": "technique",
  "id": "staging-soak-tests",
  "title": "Run bounded staging soak tests for leaks, drift and long-duration reliability",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-09-24T14:30:12Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Sjfz1TqxzEs",
      "resource": "https://www.youtube.com/watch?v=Sjfz1TqxzEs",
      "title": "Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics",
      "author": "Jason Ma, Dyna Robotics",
      "last_modified": "2026-09-24T14:30:12Z",
      "analysis_file": "analysis/Sjfz1TqxzEs.json"
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

# Run bounded staging soak tests for leaks, drift and long-duration reliability

## What

Run bounded staging soak tests for leaks, drift and long-duration reliability

Validate with repeated 24-hour continuous runs (four distinct trials) rather than single demos, exposing environment drift like lighting changes.

## Evidence

> uh in the office, you know, so these are four distinct trials of 24-hour runs.
> — 09:50 [^Sjfz1TqxzEs]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Sjfz1TqxzEs]: [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=Sjfz1TqxzEs); publication: 2026-09-24T14:30:12Z; analysis: `analysis/Sjfz1TqxzEs.json`.
