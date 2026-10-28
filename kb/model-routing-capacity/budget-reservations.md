---
{
  "type": "technique",
  "id": "budget-reservations",
  "title": "Reserve and settle approved capacity atomically across pooled accounts",
  "area": "model-routing-capacity",
  "status": "stable",
  "valid_from": "2026-10-07T00:30:28Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "cf2IhzqeQH4",
      "resource": "https://www.youtube.com/watch?v=cf2IhzqeQH4",
      "title": "Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg",
      "author": "Dor Sasson, Stigg",
      "last_modified": "2026-10-07T00:30:28Z",
      "analysis_file": "analysis/cf2IhzqeQH4.json"
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

# Reserve and settle approved capacity atomically across pooled accounts

## What

Reserve and settle approved capacity atomically across pooled accounts

Check entitlement and reserve budget synchronously at request time, then reconcile actual token usage asynchronously after the run completes.

## Evidence

> reserve before inference and settle actuals after. Um this is like going to
> — 15:05 [^cf2IhzqeQH4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Use the cheapest evidenced capable mechanism
- **Speed:** Admit work within real quota and resource limits
- **Quality:** Preserve the role quality floor
- **Reliability:** Avoid exhaustion, unsafe fallback and policy bypass
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^cf2IhzqeQH4]: [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](https://www.youtube.com/watch?v=cf2IhzqeQH4); publication: 2026-10-07T00:30:28Z; analysis: `analysis/cf2IhzqeQH4.json`.
