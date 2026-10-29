---
{
  "type": "technique",
  "id": "feedback-cycle-latency",
  "title": "Measure and shorten decision-to-verified-feedback cycles without bypassing gates",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2025-07-28T19:54:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "mHzJhXppwUA",
      "resource": "https://www.youtube.com/watch?v=mHzJhXppwUA",
      "title": "Shipping something to someone always wins — Kenneth Auchenberg (ex. Stripe, VSCode)",
      "author": "Kenneth Auchenberg (ex. Stripe, VSCode)",
      "last_modified": "2025-07-28T19:54:23Z",
      "analysis_file": "analysis/mHzJhXppwUA.json"
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

# Measure and shorten decision-to-verified-feedback cycles without bypassing gates

## What

Measure and shorten decision-to-verified-feedback cycles without bypassing gates

Before locking design decisions, they require a loop where real users see something, feedback comes back, and an improvement ships — all in under a day.

## Evidence

Source analysis [^mHzJhXppwUA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^mHzJhXppwUA]: [Shipping something to someone always wins — Kenneth Auchenberg (ex. Stripe, VSCode)](https://www.youtube.com/watch?v=mHzJhXppwUA); publication: 2025-07-28T19:54:23Z; analysis: `analysis/mHzJhXppwUA.json`.
