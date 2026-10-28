---
{
  "type": "technique",
  "id": "compensating-actions",
  "title": "Use transaction, outbox and compensating-action semantics for partial multi-system failures",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-17T07:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KtBivPzmOM8",
      "resource": "https://www.youtube.com/watch?v=KtBivPzmOM8",
      "title": "Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle",
      "author": "Nacho Martinez, Oracle",
      "last_modified": "2026-10-17T07:00:25Z",
      "analysis_file": "analysis/KtBivPzmOM8.json"
    },
    {
      "id": "OD13PiXw60o",
      "resource": "https://www.youtube.com/watch?v=OD13PiXw60o",
      "title": "Building Multi agent Systems with Finite State Machines",
      "author": null,
      "last_modified": "2025-02-22T17:00:05Z",
      "analysis_file": "analysis/OD13PiXw60o.json"
    },
    {
      "id": "Wmp2Tku2PrI",
      "resource": "https://www.youtube.com/watch?v=Wmp2Tku2PrI",
      "title": "Vibe Engineering Effect Apps — Michael Arnaldi, Effectful",
      "author": "Michael Arnaldi, Effectful",
      "last_modified": "2026-05-07T15:00:06Z",
      "analysis_file": "analysis/Wmp2Tku2PrI.json"
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

# Use transaction, outbox and compensating-action semantics for partial multi-system failures

## What

Use transaction, outbox and compensating-action semantics for partial multi-system failures

A DB write followed by an email or API action needs durable intent, retries and idempotency because there is no shared transaction across systems.

## Evidence

Source analysis [^KtBivPzmOM8]; no independently matched timestamped quote published.

> transactions to undo the previous steps and get the customer back into a valid
> — 05:50 [^OD13PiXw60o]

> there is no transaction between them, no database transaction between them and
> — 1:38:40 [^Wmp2Tku2PrI]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KtBivPzmOM8]: [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](https://www.youtube.com/watch?v=KtBivPzmOM8); publication: 2026-10-17T07:00:25Z; analysis: `analysis/KtBivPzmOM8.json`.
[^OD13PiXw60o]: [Building Multi agent Systems with Finite State Machines](https://www.youtube.com/watch?v=OD13PiXw60o); publication: 2025-02-22T17:00:05Z; analysis: `analysis/OD13PiXw60o.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
