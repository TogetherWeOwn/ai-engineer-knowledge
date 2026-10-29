---
{
  "type": "technique",
  "id": "patch-hygiene",
  "title": "Check scope, generated artifacts and policy drift in addition to passing tests",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-06-04T14:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "wcUJWP6WpGM",
      "resource": "https://www.youtube.com/watch?v=wcUJWP6WpGM",
      "title": "SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius",
      "author": "Ibragim Badertdinov, Nebius",
      "last_modified": "2026-06-04T14:00:06Z",
      "analysis_file": "analysis/wcUJWP6WpGM.json"
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

# Check scope, generated artifacts and policy drift in addition to passing tests

## What

Check scope, generated artifacts and policy drift in addition to passing tests

Agents can leave temporary repro scripts, logs and unrelated artifacts in an otherwise passing patch; quality includes intentional repository contents.

## Evidence

Source analysis [^wcUJWP6WpGM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^wcUJWP6WpGM]: [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM); publication: 2026-06-04T14:00:06Z; analysis: `analysis/wcUJWP6WpGM.json`.
