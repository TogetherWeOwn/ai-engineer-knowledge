---
{
  "type": "technique",
  "id": "capability-preflight",
  "title": "Check tool availability and operation support before planning or prompt tuning",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-12T05:36:31Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "B8l81jhvHbI",
      "resource": "https://www.youtube.com/watch?v=B8l81jhvHbI",
      "title": "Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla",
      "author": "Ishita Daga, Tesla",
      "last_modified": "2026-07-20T06:25:12Z",
      "analysis_file": "analysis/B8l81jhvHbI.json"
    },
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "SQMCtZX3trg",
      "resource": "https://www.youtube.com/watch?v=SQMCtZX3trg",
      "title": "The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)",
      "author": "Paul Bakaus, Renaissance Geek (Impeccable)",
      "last_modified": "2026-09-21T19:00:10Z",
      "analysis_file": "analysis/SQMCtZX3trg.json"
    },
    {
      "id": "Wmp2Tku2PrI",
      "resource": "https://www.youtube.com/watch?v=Wmp2Tku2PrI",
      "title": "Vibe Engineering Effect Apps — Michael Arnaldi, Effectful",
      "author": "Michael Arnaldi, Effectful",
      "last_modified": "2026-05-07T15:00:06Z",
      "analysis_file": "analysis/Wmp2Tku2PrI.json"
    },
    {
      "id": "aHhB3sjGjkI",
      "resource": "https://www.youtube.com/watch?v=aHhB3sjGjkI",
      "title": "Agents Building Agents - Alfonso Graziano, Nearform",
      "author": "Alfonso Graziano, Nearform",
      "last_modified": "2026-06-28T16:00:34Z",
      "analysis_file": "analysis/aHhB3sjGjkI.json"
    },
    {
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
    },
    {
      "id": "fmZWvE7yDZo",
      "resource": "https://www.youtube.com/watch?v=fmZWvE7yDZo",
      "title": "UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft",
      "author": "Victor Dibia, Microsoft",
      "last_modified": "2025-07-21T19:11:17Z",
      "analysis_file": "analysis/fmZWvE7yDZo.json"
    },
    {
      "id": "ghJmWQCIHRM",
      "resource": "https://www.youtube.com/watch?v=ghJmWQCIHRM",
      "title": "The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google",
      "author": "Tara Agyemang, Google",
      "last_modified": "2026-06-11T16:00:06Z",
      "analysis_file": "analysis/ghJmWQCIHRM.json"
    },
    {
      "id": "juoNbJiZUi0",
      "resource": "https://www.youtube.com/watch?v=juoNbJiZUi0",
      "title": "LLM codegen fails and how to stop 'em — Danilo Campos, PostHog",
      "author": "Danilo Campos, PostHog",
      "last_modified": "2026-04-30T14:00:06Z",
      "analysis_file": "analysis/juoNbJiZUi0.json"
    },
    {
      "id": "k72eLcYpVys",
      "resource": "https://www.youtube.com/watch?v=k72eLcYpVys",
      "title": "1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS",
      "author": "Kevin Orellana, AWS",
      "last_modified": "2026-10-12T05:36:31Z",
      "analysis_file": "analysis/k72eLcYpVys.json"
    },
    {
      "id": "k8cnVCMYmNc",
      "resource": "https://www.youtube.com/watch?v=k8cnVCMYmNc",
      "title": "OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal",
      "author": "Cornelia Davis, Temporal",
      "last_modified": "2026-01-12T19:30:06Z",
      "analysis_file": "analysis/k8cnVCMYmNc.json"
    },
    {
      "id": "l0FLhNqBOic",
      "resource": "https://www.youtube.com/watch?v=l0FLhNqBOic",
      "title": "AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents",
      "author": "Vasuman Moza, Varick Agents",
      "last_modified": "2026-07-28T21:00:06Z",
      "analysis_file": "analysis/l0FLhNqBOic.json"
    },
    {
      "id": "oWTEiYpxl80",
      "resource": "https://www.youtube.com/watch?v=oWTEiYpxl80",
      "title": "Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind",
      "author": "Philipp Schmid, Google DeepMind",
      "last_modified": "2026-10-07T17:00:07Z",
      "analysis_file": "analysis/oWTEiYpxl80.json"
    },
    {
      "id": "pAnLpiAG6Es",
      "resource": "https://www.youtube.com/watch?v=pAnLpiAG6Es",
      "title": "MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify",
      "author": "Jan Čurn, Apify",
      "last_modified": "2026-10-02T14:00:05Z",
      "analysis_file": "analysis/pAnLpiAG6Es.json"
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

# Check tool availability and operation support before planning or prompt tuning

## What

Check tool availability and operation support before planning or prompt tuning

An agent cannot pass a task requiring tools or context that its profile does not expose.

## Evidence

Source analysis [^B8l81jhvHbI]; no independently matched timestamped quote published.

> instructions in it to use the tools. I got 34% of tool usage. I went back. I
> — 1:08:57 [^KhRjivBSwiw]

Source analysis [^SQMCtZX3trg]; no independently matched timestamped quote published.

> Let's see if it catches anything. Import.
> — 29:11 [^Wmp2Tku2PrI]

Source analysis [^aHhB3sjGjkI]; no independently matched timestamped quote published.

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

Source analysis [^fmZWvE7yDZo]; no independently matched timestamped quote published.

Source analysis [^ghJmWQCIHRM]; no independently matched timestamped quote published.

> tool. Wait, the the MCP does not have a tool by this name."
> — 10:47 [^juoNbJiZUi0]

> the file system uh is persistent or uh ephemeral. Um and the tests were pretty
> — 08:42 [^k72eLcYpVys]

> APIs. This is a public API. It's part of the in the integration. and you're going
> — 48:18 [^k8cnVCMYmNc]

> right there saying, "Oh, you forgot about this edge case.
> — 13:59 [^l0FLhNqBOic]

> checks what uh version west version I'm running on what CPU memory I have and
> — 18:28 [^oWTEiYpxl80]

> actually MCP protocol has instructions where server kind of explains what it
> — 14:00 [^pAnLpiAG6Es]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^B8l81jhvHbI]: [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](https://www.youtube.com/watch?v=B8l81jhvHbI); publication: 2026-07-20T06:25:12Z; analysis: `analysis/B8l81jhvHbI.json`.
[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^SQMCtZX3trg]: [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](https://www.youtube.com/watch?v=SQMCtZX3trg); publication: 2026-09-21T19:00:10Z; analysis: `analysis/SQMCtZX3trg.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^fmZWvE7yDZo]: [UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft](https://www.youtube.com/watch?v=fmZWvE7yDZo); publication: 2025-07-21T19:11:17Z; analysis: `analysis/fmZWvE7yDZo.json`.
[^ghJmWQCIHRM]: [The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google](https://www.youtube.com/watch?v=ghJmWQCIHRM); publication: 2026-06-11T16:00:06Z; analysis: `analysis/ghJmWQCIHRM.json`.
[^juoNbJiZUi0]: [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](https://www.youtube.com/watch?v=juoNbJiZUi0); publication: 2026-04-30T14:00:06Z; analysis: `analysis/juoNbJiZUi0.json`.
[^k72eLcYpVys]: [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](https://www.youtube.com/watch?v=k72eLcYpVys); publication: 2026-10-12T05:36:31Z; analysis: `analysis/k72eLcYpVys.json`.
[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
[^l0FLhNqBOic]: [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](https://www.youtube.com/watch?v=l0FLhNqBOic); publication: 2026-07-28T21:00:06Z; analysis: `analysis/l0FLhNqBOic.json`.
[^oWTEiYpxl80]: [Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind](https://www.youtube.com/watch?v=oWTEiYpxl80); publication: 2026-10-07T17:00:07Z; analysis: `analysis/oWTEiYpxl80.json`.
[^pAnLpiAG6Es]: [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](https://www.youtube.com/watch?v=pAnLpiAG6Es); publication: 2026-10-02T14:00:05Z; analysis: `analysis/pAnLpiAG6Es.json`.
