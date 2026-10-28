---
{
  "type": "technique",
  "id": "stream-billing-cancellation",
  "title": "Track cancellation semantics and charged usage for interrupted streams",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2025-06-25T19:47:43Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "84Vtz2IL1Ug",
      "resource": "https://www.youtube.com/watch?v=84Vtz2IL1Ug",
      "title": "Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter",
      "author": "Alex Atallah, OpenRouter",
      "last_modified": "2025-06-25T19:47:43Z",
      "analysis_file": "analysis/84Vtz2IL1Ug.json"
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

# Track cancellation semantics and charged usage for interrupted streams

## What

Track cancellation semantics and charged usage for interrupted streams

They standardized wildly different provider stream-cancellation policies because dropping a stream can still bill you for the whole completion or extra tokens.

## Evidence

Source analysis [^84Vtz2IL1Ug]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^84Vtz2IL1Ug]: [Fun stories from building OpenRouter and where all this is going - Alex Atallah, OpenRouter](https://www.youtube.com/watch?v=84Vtz2IL1Ug); publication: 2025-06-25T19:47:43Z; analysis: `analysis/84Vtz2IL1Ug.json`.
