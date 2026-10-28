---
{
  "type": "technique",
  "id": "flaky-test-control",
  "title": "Separate flaky tests and nondeterminism from actual regressions",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-09T01:30:15Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "kDczF4wBh8s",
      "resource": "https://www.youtube.com/watch?v=kDczF4wBh8s",
      "title": "From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval",
      "author": "Brooke Hopkins, Coval",
      "last_modified": "2025-07-31T16:45:05Z",
      "analysis_file": "analysis/kDczF4wBh8s.json"
    },
    {
      "id": "uuwDWRbxoYo",
      "resource": "https://www.youtube.com/watch?v=uuwDWRbxoYo",
      "title": "AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar",
      "author": "Ali-Reza Adl-Tabatabai, Sonar",
      "last_modified": "2026-10-09T01:30:15Z",
      "analysis_file": "analysis/uuwDWRbxoYo.json"
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

# Separate flaky tests and nondeterminism from actual regressions

## What

Separate flaky tests and nondeterminism from actual regressions

Distinguish intermittent test failures from defects using history; retry only eligible checks with bounded attempts and keep remediation work visible.

## Evidence

> maybe if it fails one time. You really want to know what is the probability of
> — 11:40 [^kDczF4wBh8s]

> can even set up rules that automatically retry flaky tests if you want. That's a
> — 04:55 [^uuwDWRbxoYo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^kDczF4wBh8s]: [From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval](https://www.youtube.com/watch?v=kDczF4wBh8s); publication: 2025-07-31T16:45:05Z; analysis: `analysis/kDczF4wBh8s.json`.
[^uuwDWRbxoYo]: [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](https://www.youtube.com/watch?v=uuwDWRbxoYo); publication: 2026-10-09T01:30:15Z; analysis: `analysis/uuwDWRbxoYo.json`.
