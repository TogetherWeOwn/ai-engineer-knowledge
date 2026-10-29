---
{
  "type": "technique",
  "id": "cache-affinity",
  "title": "Preserve justified provider and prefix affinity within a run without defeating quota safety",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-17T09:00:27Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Hvb2LfMH58c",
      "resource": "https://www.youtube.com/watch?v=Hvb2LfMH58c",
      "title": "The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI",
      "author": "Byung-Gon (Gon) Chun, FriendliAI",
      "last_modified": "2026-09-19T18:00:03Z",
      "analysis_file": "analysis/Hvb2LfMH58c.json"
    },
    {
      "id": "NTBX-wxUhHs",
      "resource": "https://www.youtube.com/watch?v=NTBX-wxUhHs",
      "title": "Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA",
      "author": "Val Bercovici, WEKA",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/NTBX-wxUhHs.json"
    },
    {
      "id": "OqM67QG_Ikk",
      "resource": "https://www.youtube.com/watch?v=OqM67QG_Ikk",
      "title": "From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI",
      "author": "Abhishek Bhardwaj, OpenAI",
      "last_modified": "2026-07-13T17:00:06Z",
      "analysis_file": "analysis/OqM67QG_Ikk.json"
    },
    {
      "id": "Ti-BmGU1_mQ",
      "resource": "https://www.youtube.com/watch?v=Ti-BmGU1_mQ",
      "title": "The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI",
      "author": "Eugene Cheah, Featherless AI",
      "last_modified": "2026-10-17T09:00:27Z",
      "analysis_file": "analysis/Ti-BmGU1_mQ.json"
    },
    {
      "id": "_naLJOqVOEI",
      "resource": "https://www.youtube.com/watch?v=_naLJOqVOEI",
      "title": "Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI",
      "author": "FriendliAI",
      "last_modified": "2026-10-11T19:30:05Z",
      "analysis_file": "analysis/_naLJOqVOEI.json"
    },
    {
      "id": "sOB3HSiG8vo",
      "resource": "https://www.youtube.com/watch?v=sOB3HSiG8vo",
      "title": "Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI",
      "author": "Qianru Lao & Lu Zhang, OpenAI",
      "last_modified": "2026-09-19T15:30:04Z",
      "analysis_file": "analysis/sOB3HSiG8vo.json"
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

# Preserve justified provider and prefix affinity within a run without defeating quota safety

## What

Preserve justified provider and prefix affinity within a run without defeating quota safety

Per-turn model churn fragments prompt caches; task-based choices keep repeated context reusable.

## Evidence

Source analysis [^Hvb2LfMH58c]; no independently matched timestamped quote published.

> happening is you don't actually get 100% of the C hits that you could um that you
> — 09:44 [^NTBX-wxUhHs]

> smartly route you to a node which has to download the least amount of stuff. So,
> — 43:34 [^OqM67QG_Ikk]

> your your low cache hit rate will start to wreck your your optimization.
> — 54:41 [^Ti-BmGU1_mQ]

Source analysis [^_naLJOqVOEI]; no independently matched timestamped quote published.

Source analysis [^sOB3HSiG8vo]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Hvb2LfMH58c]: [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](https://www.youtube.com/watch?v=Hvb2LfMH58c); publication: 2026-09-19T18:00:03Z; analysis: `analysis/Hvb2LfMH58c.json`.
[^NTBX-wxUhHs]: [Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA](https://www.youtube.com/watch?v=NTBX-wxUhHs); publication: 2025-11-24T20:16:36Z; analysis: `analysis/NTBX-wxUhHs.json`.
[^OqM67QG_Ikk]: [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk); publication: 2026-07-13T17:00:06Z; analysis: `analysis/OqM67QG_Ikk.json`.
[^Ti-BmGU1_mQ]: [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](https://www.youtube.com/watch?v=Ti-BmGU1_mQ); publication: 2026-10-17T09:00:27Z; analysis: `analysis/Ti-BmGU1_mQ.json`.
[^_naLJOqVOEI]: [Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI](https://www.youtube.com/watch?v=_naLJOqVOEI); publication: 2026-10-11T19:30:05Z; analysis: `analysis/_naLJOqVOEI.json`.
[^sOB3HSiG8vo]: [Routing LLM Inference in Production: From Engine Signals to Policy — Qianru Lao & Lu Zhang, OpenAI](https://www.youtube.com/watch?v=sOB3HSiG8vo); publication: 2026-09-19T15:30:04Z; analysis: `analysis/sOB3HSiG8vo.json`.
