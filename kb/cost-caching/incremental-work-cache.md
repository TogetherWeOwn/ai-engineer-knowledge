---
{
  "type": "technique",
  "id": "incremental-work-cache",
  "title": "Reuse expensive work keyed to all correctness-relevant input versions",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-18T19:00:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7T-gldvgfpo",
      "resource": "https://www.youtube.com/watch?v=7T-gldvgfpo",
      "title": "Stop Telling Agents How — Dan Barrett, Raymond Weitekamp & Jose Montes de Oca, OpenProse",
      "author": "Dan Barrett, Raymond Weitekamp & Jose Montes de Oca, OpenProse",
      "last_modified": "2026-10-18T19:00:05Z",
      "analysis_file": "analysis/7T-gldvgfpo.json"
    },
    {
      "id": "KHudyx5wW3U",
      "resource": "https://www.youtube.com/watch?v=KHudyx5wW3U",
      "title": "Agent Frameworks Considered Harmful — Rémi Louf, .txt",
      "author": "Rémi Louf, .txt",
      "last_modified": "2026-08-22T16:30:39Z",
      "analysis_file": "analysis/KHudyx5wW3U.json"
    },
    {
      "id": "U3MVU6JpocU",
      "resource": "https://www.youtube.com/watch?v=U3MVU6JpocU",
      "title": "AI Agents, Meet Test Driven Development",
      "author": null,
      "last_modified": "2025-02-22T22:05:15Z",
      "analysis_file": "analysis/U3MVU6JpocU.json"
    },
    {
      "id": "UM6sFg_jdlE",
      "resource": "https://www.youtube.com/watch?v=UM6sFg_jdlE",
      "title": "RAG is dead, right?? — Kuba Rogut, Turbopuffer",
      "author": "Kuba Rogut, Turbopuffer",
      "last_modified": "2026-06-09T17:00:27Z",
      "analysis_file": "analysis/UM6sFg_jdlE.json"
    },
    {
      "id": "phchDt63qAA",
      "resource": "https://www.youtube.com/watch?v=phchDt63qAA",
      "title": "How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed",
      "author": "Ben Kunkle, Zed",
      "last_modified": "2026-05-30T16:00:06Z",
      "analysis_file": "analysis/phchDt63qAA.json"
    },
    {
      "id": "q4WC4TowkBo",
      "resource": "https://www.youtube.com/watch?v=q4WC4TowkBo",
      "title": "Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS",
      "author": "Nick Nisi & Zack Proser, WorkOS",
      "last_modified": "2026-10-18T07:00:17Z",
      "analysis_file": "analysis/q4WC4TowkBo.json"
    },
    {
      "id": "zrZ1amZBSPw",
      "resource": "https://www.youtube.com/watch?v=zrZ1amZBSPw",
      "title": "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio",
      "author": "Kanish Manuja, Twilio",
      "last_modified": "2026-08-28T15:30:03Z",
      "analysis_file": "analysis/zrZ1amZBSPw.json"
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

# Reuse expensive work keyed to all correctness-relevant input versions

## What

Reuse expensive work keyed to all correctness-relevant input versions

In a DAG of contracts, a cheap check decides whether an upstream change invalidates a downstream result before the expensive step runs again. The speakers want a Jev-class decision model to act as this 'semantic memoizer', but have not built it yet.

## Evidence

Source analysis [^7T-gldvgfpo]; no independently matched timestamped quote published.

> before rendering the text, we actually represent the prompt as a list of these
> — 12:50 [^KHudyx5wW3U]

Source analysis [^U3MVU6JpocU]; no independently matched timestamped quote published.

> like embeddings and semantic search are kind of cash compute. And you may be
> — 06:41 [^UM6sFg_jdlE]

Source analysis [^phchDt63qAA]; no independently matched timestamped quote published.

Source analysis [^q4WC4TowkBo]; no independently matched timestamped quote published.

> fallbacks, have secondary provider, secondary checks, cache decisions uh to
> — 11:53 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7T-gldvgfpo]: [Stop Telling Agents How — Dan Barrett, Raymond Weitekamp & Jose Montes de Oca, OpenProse](https://www.youtube.com/watch?v=7T-gldvgfpo); publication: 2026-10-18T19:00:05Z; analysis: `analysis/7T-gldvgfpo.json`.
[^KHudyx5wW3U]: [Agent Frameworks Considered Harmful — Rémi Louf, .txt](https://www.youtube.com/watch?v=KHudyx5wW3U); publication: 2026-08-22T16:30:39Z; analysis: `analysis/KHudyx5wW3U.json`.
[^U3MVU6JpocU]: [AI Agents, Meet Test Driven Development](https://www.youtube.com/watch?v=U3MVU6JpocU); publication: 2025-02-22T22:05:15Z; analysis: `analysis/U3MVU6JpocU.json`.
[^UM6sFg_jdlE]: [RAG is dead, right?? — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=UM6sFg_jdlE); publication: 2026-06-09T17:00:27Z; analysis: `analysis/UM6sFg_jdlE.json`.
[^phchDt63qAA]: [How We Built Zeta2: Training an Edit Prediction Model in Production — Ben Kunkle, Zed](https://www.youtube.com/watch?v=phchDt63qAA); publication: 2026-05-30T16:00:06Z; analysis: `analysis/phchDt63qAA.json`.
[^q4WC4TowkBo]: [Teach Your Agent to Prove It's Done — Nick Nisi & Zack Proser, WorkOS](https://www.youtube.com/watch?v=q4WC4TowkBo); publication: 2026-10-18T07:00:17Z; analysis: `analysis/q4WC4TowkBo.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
