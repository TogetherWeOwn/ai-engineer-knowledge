---
{
  "type": "technique",
  "id": "expertise-map",
  "title": "Build a deterministic repository expertise map from accepted changes and review history",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-09-09T14:30:12Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KcVkq5L-0f0",
      "resource": "https://www.youtube.com/watch?v=KcVkq5L-0f0",
      "title": "Your agents lack context: Here's how to fix \"You're absolutely right!\" — Brandon Waselnuk, Unblocked",
      "author": "Brandon Waselnuk, Unblocked",
      "last_modified": "2026-09-09T14:30:12Z",
      "analysis_file": "analysis/KcVkq5L-0f0.json"
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

# Build a deterministic repository expertise map from accepted changes and review history

## What

Build a deterministic repository expertise map from accepted changes and review history

Commit/review relations can map module expertise and tailor relevant context without a language model.

## Evidence

> deterministic programming, goes over your GitHub and understands who works on
> — 10:18 [^KcVkq5L-0f0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KcVkq5L-0f0]: [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=KcVkq5L-0f0); publication: 2026-09-09T14:30:12Z; analysis: `analysis/KcVkq5L-0f0.json`.
