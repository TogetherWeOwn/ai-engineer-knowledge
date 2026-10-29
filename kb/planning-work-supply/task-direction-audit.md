---
{
  "type": "technique",
  "id": "task-direction-audit",
  "title": "Verify that the requested direction is beneficial before optimizing implementation correctness",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-07-21T03:14:22Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "X1kp-ABIIxQ",
      "resource": "https://www.youtube.com/watch?v=X1kp-ABIIxQ",
      "title": "Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest",
      "author": "Dan Farrelly, CTO, Inngest",
      "last_modified": "2026-07-21T03:14:22Z",
      "analysis_file": "analysis/X1kp-ABIIxQ.json"
    },
    {
      "id": "ZpK5PWX2YRM",
      "resource": "https://www.youtube.com/watch?v=ZpK5PWX2YRM",
      "title": "Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI",
      "author": "Alex Volkov, ThursdAI",
      "last_modified": "2026-07-10T18:00:06Z",
      "analysis_file": "analysis/ZpK5PWX2YRM.json"
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

# Verify that the requested direction is beneficial before optimizing implementation correctness

## What

Verify that the requested direction is beneficial before optimizing implementation correctness

A technically correct change can still be the wrong work; improving agent capability shifts some review toward goals and scope, not just code syntax.

## Evidence

Source analysis [^X1kp-ABIIxQ]; no independently matched timestamped quote published.

> Fable, we check if Claude is doing the right work.
> — 16:40 [^ZpK5PWX2YRM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^X1kp-ABIIxQ]: [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ); publication: 2026-07-21T03:14:22Z; analysis: `analysis/X1kp-ABIIxQ.json`.
[^ZpK5PWX2YRM]: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum — Alex Volkov, ThursdAI](https://www.youtube.com/watch?v=ZpK5PWX2YRM); publication: 2026-07-10T18:00:06Z; analysis: `analysis/ZpK5PWX2YRM.json`.
