---
{
  "type": "technique",
  "id": "policy-cache-invalidation",
  "title": "Invalidate cached decisions whenever policy, scope, evidence or authorization changes",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-08-14T16:30:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Ot4OPrPH4xY",
      "resource": "https://www.youtube.com/watch?v=Ot4OPrPH4xY",
      "title": "The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data",
      "author": "Omer Primor, Bright Data",
      "last_modified": "2026-08-14T16:30:36Z",
      "analysis_file": "analysis/Ot4OPrPH4xY.json"
    },
    {
      "id": "zU4EagB311U",
      "resource": "https://www.youtube.com/watch?v=zU4EagB311U",
      "title": "Agents Need Feature Flags - Sachin Gupta",
      "author": "Sachin Gupta",
      "last_modified": "2026-07-18T07:00:06Z",
      "analysis_file": "analysis/zU4EagB311U.json"
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

# Invalidate cached decisions whenever policy, scope, evidence or authorization changes

## What

Invalidate cached decisions whenever policy, scope, evidence or authorization changes

A flag flip is ineffective if semantic/result caches keep serving output from the old policy.

## Evidence

Source analysis [^Ot4OPrPH4xY]; no independently matched timestamped quote published.

> Aggressive caching at your LLM gateway returns the old prompt response even
> — 15:57 [^zU4EagB311U]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Ot4OPrPH4xY]: [The Rise of CaaS: Context-as-a-Service for Agentic AI — Omer Primor, Bright Data](https://www.youtube.com/watch?v=Ot4OPrPH4xY); publication: 2026-08-14T16:30:36Z; analysis: `analysis/Ot4OPrPH4xY.json`.
[^zU4EagB311U]: [Agents Need Feature Flags - Sachin Gupta](https://www.youtube.com/watch?v=zU4EagB311U); publication: 2026-07-18T07:00:06Z; analysis: `analysis/zU4EagB311U.json`.
