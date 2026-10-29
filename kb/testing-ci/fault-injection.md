---
{
  "type": "technique",
  "id": "fault-injection",
  "title": "Inject controlled faults to exercise failure and recovery paths",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2025-11-24T20:16:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "flf_IKnFYnE",
      "resource": "https://www.youtube.com/watch?v=flf_IKnFYnE",
      "title": "From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/flf_IKnFYnE.json"
    },
    {
      "id": "sXXl3YMU7ZI",
      "resource": "https://www.youtube.com/watch?v=sXXl3YMU7ZI",
      "title": "Building Reliable Support Agents Using the Effect Typescript Library - Michael Fester",
      "author": "Michael Fester",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/sXXl3YMU7ZI.json"
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

# Inject controlled faults to exercise failure and recovery paths

## What

Inject controlled faults to exercise failure and recovery paths

Inject failures into an activity to verify retry and resume behavior rather than assuming the happy-path demo proves resilience. Retry only retryable errors, with attempt/deadline limits and visible failure classification.

## Evidence

> now see it succeeding most of the time and failing 10% of the time. So yeah,
> — 08:16 [^flf_IKnFYnE]

Source analysis [^sXXl3YMU7ZI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^flf_IKnFYnE]: [From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/flf_IKnFYnE.json`.
[^sXXl3YMU7ZI]: [Building Reliable Support Agents Using the Effect Typescript Library - Michael Fester](https://www.youtube.com/watch?v=sXXl3YMU7ZI); publication: 2025-06-03T22:22:29Z; analysis: `analysis/sXXl3YMU7ZI.json`.
