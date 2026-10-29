---
{
  "type": "technique",
  "id": "stable-prefix-cache",
  "title": "Keep cacheable prompt prefixes byte-stable and correctly scoped",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-10-14T15:00:14Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "65X0pQ6Lmbg",
      "resource": "https://www.youtube.com/watch?v=65X0pQ6Lmbg",
      "title": "Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs",
      "author": "Allen Pike, Forestwalk Labs",
      "last_modified": "2026-06-28T23:30:33Z",
      "analysis_file": "analysis/65X0pQ6Lmbg.json"
    },
    {
      "id": "8g1N_a3h9H0",
      "resource": "https://www.youtube.com/watch?v=8g1N_a3h9H0",
      "title": "How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival",
      "author": "Alvin Pane, OutRival",
      "last_modified": "2026-10-14T15:00:14Z",
      "analysis_file": "analysis/8g1N_a3h9H0.json"
    },
    {
      "id": "8rABwKRsec4",
      "resource": "https://www.youtube.com/watch?v=8rABwKRsec4",
      "title": "The New Code — Sean Grove, OpenAI",
      "author": "Sean Grove, OpenAI",
      "last_modified": "2025-07-11T16:00:06Z",
      "analysis_file": "analysis/8rABwKRsec4.json"
    },
    {
      "id": "HY_JyxAZsiE",
      "resource": "https://www.youtube.com/watch?v=HY_JyxAZsiE",
      "title": "Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro",
      "author": "Al Harris, Amazon Kiro",
      "last_modified": "2026-01-09T15:15:06Z",
      "analysis_file": "analysis/HY_JyxAZsiE.json"
    },
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
      "id": "QHBjufYK8TA",
      "resource": "https://www.youtube.com/watch?v=QHBjufYK8TA",
      "title": "The State of Model Routing — NVIDIA, Cognition, OpenRouter",
      "author": "NVIDIA, Cognition, OpenRouter",
      "last_modified": "2026-08-06T17:07:24Z",
      "analysis_file": "analysis/QHBjufYK8TA.json"
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
      "id": "b9UhZkKjX_A",
      "resource": "https://www.youtube.com/watch?v=b9UhZkKjX_A",
      "title": "From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot",
      "author": null,
      "last_modified": "2026-10-10T16:30:31Z",
      "analysis_file": "analysis/b9UhZkKjX_A.json"
    },
    {
      "id": "cQQbJqvZkpo",
      "resource": "https://www.youtube.com/watch?v=cQQbJqvZkpo",
      "title": "Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave",
      "author": "Sitanshu Gupta, CoreWeave",
      "last_modified": "2026-09-19T16:30:34Z",
      "analysis_file": "analysis/cQQbJqvZkpo.json"
    },
    {
      "id": "dSg0pu8d6qg",
      "resource": "https://www.youtube.com/watch?v=dSg0pu8d6qg",
      "title": "From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad",
      "author": "Mingsheng Hong, Ironclad",
      "last_modified": "2026-08-29T15:30:28Z",
      "analysis_file": "analysis/dSg0pu8d6qg.json"
    },
    {
      "id": "dvft0Gp9sEE",
      "resource": "https://www.youtube.com/watch?v=dvft0Gp9sEE",
      "title": "Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo",
      "author": "Charlie Guo",
      "last_modified": "2025-06-03T07:00:07Z",
      "analysis_file": "analysis/dvft0Gp9sEE.json"
    },
    {
      "id": "esY99nYXxR4",
      "resource": "https://www.youtube.com/watch?v=esY99nYXxR4",
      "title": "How we solved Context Management in Agents — Sally-Ann Delucia",
      "author": "Sally-Ann Delucia",
      "last_modified": "2026-05-10T19:00:06Z",
      "analysis_file": "analysis/esY99nYXxR4.json"
    },
    {
      "id": "ow1we5PzK-o",
      "resource": "https://www.youtube.com/watch?v=ow1we5PzK-o",
      "title": "The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory",
      "author": "Luke Alvoeiro, Factory",
      "last_modified": "2026-05-06T15:00:06Z",
      "analysis_file": "analysis/ow1we5PzK-o.json"
    },
    {
      "id": "sn79oS4MZFI",
      "resource": "https://www.youtube.com/watch?v=sn79oS4MZFI",
      "title": "Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason",
      "author": "Dan Mason",
      "last_modified": "2025-06-22T16:00:06Z",
      "analysis_file": "analysis/sn79oS4MZFI.json"
    },
    {
      "id": "uiP88SpCi1Q",
      "resource": "https://www.youtube.com/watch?v=uiP88SpCi1Q",
      "title": "Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS",
      "author": "Erik Hanchett, AWS",
      "last_modified": "2026-06-28T22:00:14Z",
      "analysis_file": "analysis/uiP88SpCi1Q.json"
    },
    {
      "id": "vW8wLsb3Nnc",
      "resource": "https://www.youtube.com/watch?v=vW8wLsb3Nnc",
      "title": "POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent",
      "author": "Randall Hunt, Caylent",
      "last_modified": "2025-07-23T15:50:56Z",
      "analysis_file": "analysis/vW8wLsb3Nnc.json"
    },
    {
      "id": "wXVvfFMTyzY",
      "resource": "https://www.youtube.com/watch?v=wXVvfFMTyzY",
      "title": "A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench",
      "author": "Damien Murphy, Bench",
      "last_modified": "2025-07-26T14:15:05Z",
      "analysis_file": "analysis/wXVvfFMTyzY.json"
    },
    {
      "id": "wcUJWP6WpGM",
      "resource": "https://www.youtube.com/watch?v=wcUJWP6WpGM",
      "title": "SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius",
      "author": "Ibragim Badertdinov, Nebius",
      "last_modified": "2026-06-04T14:00:06Z",
      "analysis_file": "analysis/wcUJWP6WpGM.json"
    },
    {
      "id": "wflNENRSUb4",
      "resource": "https://www.youtube.com/watch?v=wflNENRSUb4",
      "title": "Give Your Agent a Computer — Nico Albanese, Vercel",
      "author": "Nico Albanese, Vercel",
      "last_modified": "2026-05-12T18:00:06Z",
      "analysis_file": "analysis/wflNENRSUb4.json"
    },
    {
      "id": "xLUQOqjudtA",
      "resource": "https://www.youtube.com/watch?v=xLUQOqjudtA",
      "title": "Tolan: Voice-First AI Companion — Paula Dozsa, Tolan",
      "author": "Paula Dozsa, Tolan",
      "last_modified": "2026-09-15T14:30:14Z",
      "analysis_file": "analysis/xLUQOqjudtA.json"
    },
    {
      "id": "y2W4FNAuPEA",
      "resource": "https://www.youtube.com/watch?v=y2W4FNAuPEA",
      "title": "Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher",
      "author": "Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher",
      "last_modified": "2026-09-08T15:00:06Z",
      "analysis_file": "analysis/y2W4FNAuPEA.json"
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

# Keep cacheable prompt prefixes byte-stable and correctly scoped

## What

Keep cacheable prompt prefixes byte-stable and correctly scoped

Keep system/tool context stable across turns so provider caching can reuse prefix computation; place volatile task material afterward.

## Evidence

Source analysis [^65X0pQ6Lmbg]; no independently matched timestamped quote published.

Source analysis [^8g1N_a3h9H0]; no independently matched timestamped quote published.

Source analysis [^8rABwKRsec4]; no independently matched timestamped quote published.

Source analysis [^HY_JyxAZsiE]; no independently matched timestamped quote published.

> Consecutive agent steps usually share a huge prefix. If we recomp compute the
> — 05:27 [^Hvb2LfMH58c]

Source analysis [^NTBX-wxUhHs]; no independently matched timestamped quote published.

> Um we we we do spend a lot of time optimizing
> — 25:22 [^QHBjufYK8TA]

Source analysis [^_naLJOqVOEI]; no independently matched timestamped quote published.

Source analysis [^b9UhZkKjX_A]; no independently matched timestamped quote published.

Source analysis [^cQQbJqvZkpo]; no independently matched timestamped quote published.

Source analysis [^dSg0pu8d6qg]; no independently matched timestamped quote published.

Source analysis [^dvft0Gp9sEE]; no independently matched timestamped quote published.

> Um, and so we're keeping the latest result. We don't reset the system prompt
> — 07:12 [^esY99nYXxR4]

> caching heavily to make sure that we're sort of offsetting
> — 13:51 [^ow1we5PzK-o]

Source analysis [^sn79oS4MZFI]; no independently matched timestamped quote published.

> cache your system prompt. Let me show you some code. Now, I'm using AWS's
> — 00:21 [^uiP88SpCi1Q]

Source analysis [^vW8wLsb3Nnc]; no independently matched timestamped quote published.

Source analysis [^wXVvfFMTyzY]; no independently matched timestamped quote published.

Source analysis [^wcUJWP6WpGM]; no independently matched timestamped quote published.

Source analysis [^wflNENRSUb4]; no independently matched timestamped quote published.

> actually get recalled and pin those into a stable and cashable block.
> — 08:06 [^xLUQOqjudtA]

Source analysis [^y2W4FNAuPEA]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^65X0pQ6Lmbg]: [Voice In, Visuals Out: The Agony and the Ecstasy - Allen Pike, Forestwalk Labs](https://www.youtube.com/watch?v=65X0pQ6Lmbg); publication: 2026-06-28T23:30:33Z; analysis: `analysis/65X0pQ6Lmbg.json`.
[^8g1N_a3h9H0]: [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](https://www.youtube.com/watch?v=8g1N_a3h9H0); publication: 2026-10-14T15:00:14Z; analysis: `analysis/8g1N_a3h9H0.json`.
[^8rABwKRsec4]: [The New Code — Sean Grove, OpenAI](https://www.youtube.com/watch?v=8rABwKRsec4); publication: 2025-07-11T16:00:06Z; analysis: `analysis/8rABwKRsec4.json`.
[^HY_JyxAZsiE]: [Spec-Driven Development: Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro](https://www.youtube.com/watch?v=HY_JyxAZsiE); publication: 2026-01-09T15:15:06Z; analysis: `analysis/HY_JyxAZsiE.json`.
[^Hvb2LfMH58c]: [The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI](https://www.youtube.com/watch?v=Hvb2LfMH58c); publication: 2026-09-19T18:00:03Z; analysis: `analysis/Hvb2LfMH58c.json`.
[^NTBX-wxUhHs]: [Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA](https://www.youtube.com/watch?v=NTBX-wxUhHs); publication: 2025-11-24T20:16:36Z; analysis: `analysis/NTBX-wxUhHs.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^_naLJOqVOEI]: [Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI](https://www.youtube.com/watch?v=_naLJOqVOEI); publication: 2026-10-11T19:30:05Z; analysis: `analysis/_naLJOqVOEI.json`.
[^b9UhZkKjX_A]: [From Your Laptop to the Pipeline: Scaling Custom Agents with GitHub Copilot](https://www.youtube.com/watch?v=b9UhZkKjX_A); publication: 2026-10-10T16:30:31Z; analysis: `analysis/b9UhZkKjX_A.json`.
[^cQQbJqvZkpo]: [Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](https://www.youtube.com/watch?v=cQQbJqvZkpo); publication: 2026-09-19T16:30:34Z; analysis: `analysis/cQQbJqvZkpo.json`.
[^dSg0pu8d6qg]: [From Tokenmaxxing to Trusted Throughput — Mingsheng Hong, Ironclad](https://www.youtube.com/watch?v=dSg0pu8d6qg); publication: 2026-08-29T15:30:28Z; analysis: `analysis/dSg0pu8d6qg.json`.
[^dvft0Gp9sEE]: [Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo](https://www.youtube.com/watch?v=dvft0Gp9sEE); publication: 2025-06-03T07:00:07Z; analysis: `analysis/dvft0Gp9sEE.json`.
[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
[^ow1we5PzK-o]: [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](https://www.youtube.com/watch?v=ow1we5PzK-o); publication: 2026-05-06T15:00:06Z; analysis: `analysis/ow1we5PzK-o.json`.
[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
[^uiP88SpCi1Q]: [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](https://www.youtube.com/watch?v=uiP88SpCi1Q); publication: 2026-06-28T22:00:14Z; analysis: `analysis/uiP88SpCi1Q.json`.
[^vW8wLsb3Nnc]: [POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent](https://www.youtube.com/watch?v=vW8wLsb3Nnc); publication: 2025-07-23T15:50:56Z; analysis: `analysis/vW8wLsb3Nnc.json`.
[^wXVvfFMTyzY]: [A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench](https://www.youtube.com/watch?v=wXVvfFMTyzY); publication: 2025-07-26T14:15:05Z; analysis: `analysis/wXVvfFMTyzY.json`.
[^wcUJWP6WpGM]: [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM); publication: 2026-06-04T14:00:06Z; analysis: `analysis/wcUJWP6WpGM.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
[^xLUQOqjudtA]: [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA); publication: 2026-09-15T14:30:14Z; analysis: `analysis/xLUQOqjudtA.json`.
[^y2W4FNAuPEA]: [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](https://www.youtube.com/watch?v=y2W4FNAuPEA); publication: 2026-09-08T15:00:06Z; analysis: `analysis/y2W4FNAuPEA.json`.
