---
{
  "type": "technique",
  "id": "cheap-scheduled-routines",
  "title": "Run deterministic scheduled work without waking a full agent",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-21T09:00:26Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "DouK81O8R3o",
      "resource": "https://www.youtube.com/watch?v=DouK81O8R3o",
      "title": "One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO",
      "author": "Ford Prior, GEICO",
      "last_modified": "2026-10-21T09:00:26Z",
      "analysis_file": "analysis/DouK81O8R3o.json"
    },
    {
      "id": "q4Tr-DknG2M",
      "resource": "https://www.youtube.com/watch?v=q4Tr-DknG2M",
      "title": "Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI",
      "author": "Lee Robinson, Cursor, SpaceXAI",
      "last_modified": "2026-07-15T20:13:51Z",
      "analysis_file": "analysis/q4Tr-DknG2M.json"
    },
    {
      "id": "qJtcEDc_WJU",
      "resource": "https://www.youtube.com/watch?v=qJtcEDc_WJU",
      "title": "Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T06:07:42Z",
      "analysis_file": "analysis/qJtcEDc_WJU.json"
    },
    {
      "id": "sJ2jc7leKBk",
      "resource": "https://www.youtube.com/watch?v=sJ2jc7leKBk",
      "title": "I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)",
      "author": "Radek Sienkiewicz (@velvetshark-com)",
      "last_modified": "2026-05-02T22:00:06Z",
      "analysis_file": "analysis/sJ2jc7leKBk.json"
    },
    {
      "id": "sn79oS4MZFI",
      "resource": "https://www.youtube.com/watch?v=sn79oS4MZFI",
      "title": "Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason",
      "author": "Dan Mason",
      "last_modified": "2025-06-22T16:00:06Z",
      "analysis_file": "analysis/sn79oS4MZFI.json"
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

# Run deterministic scheduled work without waking a full agent

## What

Run deterministic scheduled work without waking a full agent

Check-ins should be driven by deterministic code. An agent that sets up crons to check on work starts a new frontier session on every tick.

## Evidence

Source analysis [^DouK81O8R3o]; no independently matched timestamped quote published.

Source analysis [^q4Tr-DknG2M]; no independently matched timestamped quote published.

Source analysis [^qJtcEDc_WJU]; no independently matched timestamped quote published.

Source analysis [^sJ2jc7leKBk]; no independently matched timestamped quote published.

> we're not checking, right? There's no polling going on in the system where
> — 30:46 [^sn79oS4MZFI]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^DouK81O8R3o]: [One Day, $1,000 in Tokens: An AI War Room for Legacy Code — Ford Prior, GEICO](https://www.youtube.com/watch?v=DouK81O8R3o); publication: 2026-10-21T09:00:26Z; analysis: `analysis/DouK81O8R3o.json`.
[^q4Tr-DknG2M]: [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](https://www.youtube.com/watch?v=q4Tr-DknG2M); publication: 2026-07-15T20:13:51Z; analysis: `analysis/q4Tr-DknG2M.json`.
[^qJtcEDc_WJU]: [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](https://www.youtube.com/watch?v=qJtcEDc_WJU); publication: 2026-10-12T06:07:42Z; analysis: `analysis/qJtcEDc_WJU.json`.
[^sJ2jc7leKBk]: [I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)](https://www.youtube.com/watch?v=sJ2jc7leKBk); publication: 2026-05-02T22:00:06Z; analysis: `analysis/sJ2jc7leKBk.json`.
[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
