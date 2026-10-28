---
{
  "type": "technique",
  "id": "context-composition",
  "title": "Measure context composition and remove irrelevant payloads without an arbitrary window cap",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-10-06T23:30:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0n3MKk7r60w",
      "resource": "https://www.youtube.com/watch?v=0n3MKk7r60w",
      "title": "Scaling GitHub for your Agents — Sam Morrow, GitHub",
      "author": "Sam Morrow, GitHub",
      "last_modified": "2026-04-27T22:00:06Z",
      "analysis_file": "analysis/0n3MKk7r60w.json"
    },
    {
      "id": "72XxWkd8Jrk",
      "resource": "https://www.youtube.com/watch?v=72XxWkd8Jrk",
      "title": "Effective agent design patterns in production — Laurie Voss, LlamaIndex",
      "author": "Laurie Voss, LlamaIndex",
      "last_modified": "2025-06-27T10:22:56Z",
      "analysis_file": "analysis/72XxWkd8Jrk.json"
    },
    {
      "id": "AvVoJBxgSQk",
      "resource": "https://www.youtube.com/watch?v=AvVoJBxgSQk",
      "title": "Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2025-07-21T17:15:06Z",
      "analysis_file": "analysis/AvVoJBxgSQk.json"
    },
    {
      "id": "BEKc4P87XKo",
      "resource": "https://www.youtube.com/watch?v=BEKc4P87XKo",
      "title": "Agentic Engineering: Working With AI, Not Just Using It — Brendan O'Leary",
      "author": "Brendan O'Leary",
      "last_modified": "2026-04-07T23:00:06Z",
      "analysis_file": "analysis/BEKc4P87XKo.json"
    },
    {
      "id": "D7_ipDqhtwk",
      "resource": "https://www.youtube.com/watch?v=D7_ipDqhtwk",
      "title": "How We Build Effective Agents: Barry Zhang, Anthropic",
      "author": null,
      "last_modified": "2025-04-04T18:46:36Z",
      "analysis_file": "analysis/D7_ipDqhtwk.json"
    },
    {
      "id": "E0k9Ppq6yXY",
      "resource": "https://www.youtube.com/watch?v=E0k9Ppq6yXY",
      "title": "Stateful Agents — Full Workshop with Charles Packer of Letta and MemGPT",
      "author": "Full Workshop with Charles Packer of Letta and MemGPT",
      "last_modified": "2025-04-19T16:00:06Z",
      "analysis_file": "analysis/E0k9Ppq6yXY.json"
    },
    {
      "id": "LC3-P7v3yoI",
      "resource": "https://www.youtube.com/watch?v=LC3-P7v3yoI",
      "title": "Skills are the New SDKs - Elvin Aghammadzada, DataRobot",
      "author": "Elvin Aghammadzada, DataRobot",
      "last_modified": "2026-07-20T06:24:53Z",
      "analysis_file": "analysis/LC3-P7v3yoI.json"
    },
    {
      "id": "ZSQb5fzRFPw",
      "resource": "https://www.youtube.com/watch?v=ZSQb5fzRFPw",
      "title": "Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua",
      "author": "Francesco Bonacci, Cua",
      "last_modified": "2026-07-15T22:45:06Z",
      "analysis_file": "analysis/ZSQb5fzRFPw.json"
    },
    {
      "id": "_B4Pv9ttFgY",
      "resource": "https://www.youtube.com/watch?v=_B4Pv9ttFgY",
      "title": "Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google",
      "author": "Michael Hablich, Google",
      "last_modified": "2026-06-05T17:00:06Z",
      "analysis_file": "analysis/_B4Pv9ttFgY.json"
    },
    {
      "id": "aeTb5BdmTTc",
      "resource": "https://www.youtube.com/watch?v=aeTb5BdmTTc",
      "title": "Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab",
      "author": "Aditya Khandelwal, Amazon AGI Lab",
      "last_modified": "2026-08-11T00:03:17Z",
      "analysis_file": "analysis/aeTb5BdmTTc.json"
    },
    {
      "id": "c35YoMdnI78",
      "resource": "https://www.youtube.com/watch?v=c35YoMdnI78",
      "title": "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "author": "Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "last_modified": "2026-07-17T21:00:06Z",
      "analysis_file": "analysis/c35YoMdnI78.json"
    },
    {
      "id": "cwjs1WAG9CM",
      "resource": "https://www.youtube.com/watch?v=cwjs1WAG9CM",
      "title": "Building Context-Aware Reasoning Applications with LangChain and LangSmith: Harrison Chase",
      "author": null,
      "last_modified": "2023-11-01T15:15:07Z",
      "analysis_file": "analysis/cwjs1WAG9CM.json"
    },
    {
      "id": "eXA2tjRZIbY",
      "resource": "https://www.youtube.com/watch?v=eXA2tjRZIbY",
      "title": "The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI",
      "author": "Varun Krovvidi, Resolve AI",
      "last_modified": "2026-10-06T23:30:36Z",
      "analysis_file": "analysis/eXA2tjRZIbY.json"
    },
    {
      "id": "shRR1e2HXMk",
      "resource": "https://www.youtube.com/watch?v=shRR1e2HXMk",
      "title": "How Codex Works — Dominik Kundel, OpenAI",
      "author": "Dominik Kundel, OpenAI",
      "last_modified": "2026-08-10T16:00:06Z",
      "analysis_file": "analysis/shRR1e2HXMk.json"
    },
    {
      "id": "t4359sKBu4w",
      "resource": "https://www.youtube.com/watch?v=t4359sKBu4w",
      "title": "Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver",
      "author": "Angus J. McLean, Oliver",
      "last_modified": "2026-05-25T13:00:06Z",
      "analysis_file": "analysis/t4359sKBu4w.json"
    },
    {
      "id": "tDArkCqjA-c",
      "resource": "https://www.youtube.com/watch?v=tDArkCqjA-c",
      "title": "Human-in-the-Loop Automation with n8n — Liam McGarrigle",
      "author": "Liam McGarrigle",
      "last_modified": "2026-05-02T23:00:06Z",
      "analysis_file": "analysis/tDArkCqjA-c.json"
    },
    {
      "id": "xs-ob87TTzg",
      "resource": "https://www.youtube.com/watch?v=xs-ob87TTzg",
      "title": "Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle",
      "author": "Ignacio Martinez, Oracle",
      "last_modified": "2026-09-18T16:00:11Z",
      "analysis_file": "analysis/xs-ob87TTzg.json"
    },
    {
      "id": "ynJyIKwjonM",
      "resource": "https://www.youtube.com/watch?v=ynJyIKwjonM",
      "title": "Agentic Search for Context Engineering — Leonie Monigatti, Elastic",
      "author": "Leonie Monigatti, Elastic",
      "last_modified": "2026-05-08T13:00:06Z",
      "analysis_file": "analysis/ynJyIKwjonM.json"
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

# Measure context composition and remove irrelevant payloads without an arbitrary window cap

## What

Measure context composition and remove irrelevant payloads without an arbitrary window cap

Irrelevant tool schemas, stale instructions and noisy outputs compete with task evidence for attention and cost.

## Evidence

Source analysis [^0n3MKk7r60w]; no independently matched timestamped quote published.

Source analysis [^72XxWkd8Jrk]; no independently matched timestamped quote published.

Source analysis [^AvVoJBxgSQk]; no independently matched timestamped quote published.

> The quality can degrade as you get over about 50% full.
> — 05:27 [^BEKc4P87XKo]

Source analysis [^D7_ipDqhtwk]; no independently matched timestamped quote published.

Source analysis [^E0k9Ppq6yXY]; no independently matched timestamped quote published.

> downloaded the package. Same for skills. Closing thoughts. Context is a budget.
> — 25:52 [^LC3-P7v3yoI]

Source analysis [^ZSQb5fzRFPw]; no independently matched timestamped quote published.

> They are not free lunch. If you pile in too many skills, uh,
> — 18:12 [^_B4Pv9ttFgY]

Source analysis [^aeTb5BdmTTc]; no independently matched timestamped quote published.

> But also leaving a bit of a headroom. Leaving a bit of headroom. So, I also I
> — 31:37 [^c35YoMdnI78]

Source analysis [^cwjs1WAG9CM]; no independently matched timestamped quote published.

Source analysis [^eXA2tjRZIbY]; no independently matched timestamped quote published.

Source analysis [^shRR1e2HXMk]; no independently matched timestamped quote published.

Source analysis [^t4359sKBu4w]; no independently matched timestamped quote published.

Source analysis [^tDArkCqjA-c]; no independently matched timestamped quote published.

> as small as possible to avoid context rot.
> — 30:24 [^xs-ob87TTzg]

> place and then if it's not, you can just take them out temporarily.
> — 38:13 [^xs-ob87TTzg]

> your context window longterm could have the problem of confusing your agent long
> — 58:18 [^ynJyIKwjonM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0n3MKk7r60w]: [Scaling GitHub for your Agents — Sam Morrow, GitHub](https://www.youtube.com/watch?v=0n3MKk7r60w); publication: 2026-04-27T22:00:06Z; analysis: `analysis/0n3MKk7r60w.json`.
[^72XxWkd8Jrk]: [Effective agent design patterns in production — Laurie Voss, LlamaIndex](https://www.youtube.com/watch?v=72XxWkd8Jrk); publication: 2025-06-27T10:22:56Z; analysis: `analysis/72XxWkd8Jrk.json`.
[^AvVoJBxgSQk]: [Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=AvVoJBxgSQk); publication: 2025-07-21T17:15:06Z; analysis: `analysis/AvVoJBxgSQk.json`.
[^BEKc4P87XKo]: [Agentic Engineering: Working With AI, Not Just Using It — Brendan O'Leary](https://www.youtube.com/watch?v=BEKc4P87XKo); publication: 2026-04-07T23:00:06Z; analysis: `analysis/BEKc4P87XKo.json`.
[^D7_ipDqhtwk]: [How We Build Effective Agents: Barry Zhang, Anthropic](https://www.youtube.com/watch?v=D7_ipDqhtwk); publication: 2025-04-04T18:46:36Z; analysis: `analysis/D7_ipDqhtwk.json`.
[^E0k9Ppq6yXY]: [Stateful Agents — Full Workshop with Charles Packer of Letta and MemGPT](https://www.youtube.com/watch?v=E0k9Ppq6yXY); publication: 2025-04-19T16:00:06Z; analysis: `analysis/E0k9Ppq6yXY.json`.
[^LC3-P7v3yoI]: [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](https://www.youtube.com/watch?v=LC3-P7v3yoI); publication: 2026-07-20T06:24:53Z; analysis: `analysis/LC3-P7v3yoI.json`.
[^ZSQb5fzRFPw]: [Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua](https://www.youtube.com/watch?v=ZSQb5fzRFPw); publication: 2026-07-15T22:45:06Z; analysis: `analysis/ZSQb5fzRFPw.json`.
[^_B4Pv9ttFgY]: [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](https://www.youtube.com/watch?v=_B4Pv9ttFgY); publication: 2026-06-05T17:00:06Z; analysis: `analysis/_B4Pv9ttFgY.json`.
[^aeTb5BdmTTc]: [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](https://www.youtube.com/watch?v=aeTb5BdmTTc); publication: 2026-08-11T00:03:17Z; analysis: `analysis/aeTb5BdmTTc.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^cwjs1WAG9CM]: [Building Context-Aware Reasoning Applications with LangChain and LangSmith: Harrison Chase](https://www.youtube.com/watch?v=cwjs1WAG9CM); publication: 2023-11-01T15:15:07Z; analysis: `analysis/cwjs1WAG9CM.json`.
[^eXA2tjRZIbY]: [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY); publication: 2026-10-06T23:30:36Z; analysis: `analysis/eXA2tjRZIbY.json`.
[^shRR1e2HXMk]: [How Codex Works — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk); publication: 2026-08-10T16:00:06Z; analysis: `analysis/shRR1e2HXMk.json`.
[^t4359sKBu4w]: [Bounded Autonomy: Between Free Will and Determinism — Angus J. McLean, Oliver](https://www.youtube.com/watch?v=t4359sKBu4w); publication: 2026-05-25T13:00:06Z; analysis: `analysis/t4359sKBu4w.json`.
[^tDArkCqjA-c]: [Human-in-the-Loop Automation with n8n — Liam McGarrigle](https://www.youtube.com/watch?v=tDArkCqjA-c); publication: 2026-05-02T23:00:06Z; analysis: `analysis/tDArkCqjA-c.json`.
[^xs-ob87TTzg]: [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg); publication: 2026-09-18T16:00:11Z; analysis: `analysis/xs-ob87TTzg.json`.
[^ynJyIKwjonM]: [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM); publication: 2026-05-08T13:00:06Z; analysis: `analysis/ynJyIKwjonM.json`.
