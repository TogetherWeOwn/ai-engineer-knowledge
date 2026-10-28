---
{
  "type": "technique",
  "id": "async-cheap-work",
  "title": "Schedule delay-tolerant work for cheaper included capacity without adding a paid batch dependency",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-07-22T23:00:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Btk8wDUVs74",
      "resource": "https://www.youtube.com/watch?v=Btk8wDUVs74",
      "title": "From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com",
      "author": "Omri Bruchim & Tomer Ast, monday.com",
      "last_modified": "2026-07-22T23:00:11Z",
      "analysis_file": "analysis/Btk8wDUVs74.json"
    },
    {
      "id": "kTnfJszFxCg",
      "resource": "https://www.youtube.com/watch?v=kTnfJszFxCg",
      "title": "3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph",
      "author": "Harrison Chase, LangChain/LangGraph",
      "last_modified": "2025-07-23T15:51:25Z",
      "analysis_file": "analysis/kTnfJszFxCg.json"
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

# Schedule delay-tolerant work for cheaper included capacity without adding a paid batch dependency

## What

Schedule delay-tolerant work for cheaper included capacity without adding a paid batch dependency

Background tasks do not need chat-like response latency, enabling cheaper execution and bounded deeper work without confusing a human waiting in the UI.

## Evidence

Source analysis [^Btk8wDUVs74]; no independently matched timestamped quote published.

> So when chat you have this kind of like UX expectation that it responds really
> — 14:34 [^kTnfJszFxCg]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Btk8wDUVs74]: [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74); publication: 2026-07-22T23:00:11Z; analysis: `analysis/Btk8wDUVs74.json`.
[^kTnfJszFxCg]: [3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph](https://www.youtube.com/watch?v=kTnfJszFxCg); publication: 2025-07-23T15:51:25Z; analysis: `analysis/kTnfJszFxCg.json`.
