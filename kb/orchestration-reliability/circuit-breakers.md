---
{
  "type": "technique",
  "id": "circuit-breakers",
  "title": "Break correlated failures before retries amplify them",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-08-29T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2czYyrTzILg",
      "resource": "https://www.youtube.com/watch?v=2czYyrTzILg",
      "title": "From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik",
      "author": "Sandipan Bhaumik",
      "last_modified": "2026-04-08T10:23:12Z",
      "analysis_file": "analysis/2czYyrTzILg.json"
    },
    {
      "id": "b2GqTDWtg6s",
      "resource": "https://www.youtube.com/watch?v=b2GqTDWtg6s",
      "title": "Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering",
      "author": "Anju Kambadur, Bloomberg Head of AI Engineering",
      "last_modified": "2025-04-01T15:06:35Z",
      "analysis_file": "analysis/b2GqTDWtg6s.json"
    },
    {
      "id": "hD9-V56FNRI",
      "resource": "https://www.youtube.com/watch?v=hD9-V56FNRI",
      "title": "AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok",
      "author": "Salman Munaf, TikTok",
      "last_modified": "2026-08-29T16:00:06Z",
      "analysis_file": "analysis/hD9-V56FNRI.json"
    },
    {
      "id": "vi-2nasppAg",
      "resource": "https://www.youtube.com/watch?v=vi-2nasppAg",
      "title": "Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate",
      "author": "Jonas Templestein, Iterate",
      "last_modified": "2026-05-14T14:00:06Z",
      "analysis_file": "analysis/vi-2nasppAg.json"
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

# Break correlated failures before retries amplify them

## What

Break correlated failures before retries amplify them

Stop repeated calls to an unhealthy downstream instead of allowing agent fan-out to produce cascading failures.

## Evidence

Source analysis [^2czYyrTzILg]; no independently matched timestamped quote published.

Source analysis [^b2GqTDWtg6s]; no independently matched timestamped quote published.

> system break uh circuit breakers in place that prevents AI agents to call
> — 13:57 [^hD9-V56FNRI]

Source analysis [^vi-2nasppAg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2czYyrTzILg]: [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik](https://www.youtube.com/watch?v=2czYyrTzILg); publication: 2026-04-08T10:23:12Z; analysis: `analysis/2czYyrTzILg.json`.
[^b2GqTDWtg6s]: [Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering](https://www.youtube.com/watch?v=b2GqTDWtg6s); publication: 2025-04-01T15:06:35Z; analysis: `analysis/b2GqTDWtg6s.json`.
[^hD9-V56FNRI]: [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](https://www.youtube.com/watch?v=hD9-V56FNRI); publication: 2026-08-29T16:00:06Z; analysis: `analysis/hD9-V56FNRI.json`.
[^vi-2nasppAg]: [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](https://www.youtube.com/watch?v=vi-2nasppAg); publication: 2026-05-14T14:00:06Z; analysis: `analysis/vi-2nasppAg.json`.
