---
{
  "type": "technique",
  "id": "async-control-handles",
  "title": "Expose stable async task handles with status, progress, cancellation and result retrieval",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-10-02T14:00:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1izYWsokr9s",
      "resource": "https://www.youtube.com/watch?v=1izYWsokr9s",
      "title": "Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal",
      "author": "Preeti Somal, Temporal",
      "last_modified": "2025-07-28T15:15:00Z",
      "analysis_file": "analysis/1izYWsokr9s.json"
    },
    {
      "id": "7CrPrHgoEYk",
      "resource": "https://www.youtube.com/watch?v=7CrPrHgoEYk",
      "title": "What the Best Agents Share — Mardu Swanepoel, Flinn AI",
      "author": "Mardu Swanepoel, Flinn AI",
      "last_modified": "2026-05-26T15:00:06Z",
      "analysis_file": "analysis/7CrPrHgoEYk.json"
    },
    {
      "id": "7_WhRAuP2Wg",
      "resource": "https://www.youtube.com/watch?v=7_WhRAuP2Wg",
      "title": "Building and Scaling an AI Agent Swarm of low latency real time voice bots: Damien Murphy",
      "author": null,
      "last_modified": "2024-10-08T18:28:46Z",
      "analysis_file": "analysis/7_WhRAuP2Wg.json"
    },
    {
      "id": "KUEmEb71vzQ",
      "resource": "https://www.youtube.com/watch?v=KUEmEb71vzQ",
      "title": "Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI",
      "author": "Full Workshop, with Ilan Bigio of OpenAI",
      "last_modified": "2025-04-23T16:00:26Z",
      "analysis_file": "analysis/KUEmEb71vzQ.json"
    },
    {
      "id": "OV56RddyFuU",
      "resource": "https://www.youtube.com/watch?v=OV56RddyFuU",
      "title": "Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face",
      "author": "Merve Noyan, Hugging Face",
      "last_modified": "2026-05-13T17:00:06Z",
      "analysis_file": "analysis/OV56RddyFuU.json"
    },
    {
      "id": "YNJvm7t3yq8",
      "resource": "https://www.youtube.com/watch?v=YNJvm7t3yq8",
      "title": "Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably",
      "author": "Mike Christensen, Ably",
      "last_modified": "2026-05-17T15:30:06Z",
      "analysis_file": "analysis/YNJvm7t3yq8.json"
    },
    {
      "id": "cI7zfqusmFU",
      "resource": "https://www.youtube.com/watch?v=cI7zfqusmFU",
      "title": "Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate",
      "author": "Giselle van Dongen, Restate",
      "last_modified": "2026-09-14T15:30:30Z",
      "analysis_file": "analysis/cI7zfqusmFU.json"
    },
    {
      "id": "dKcTBQzR7jI",
      "resource": "https://www.youtube.com/watch?v=dKcTBQzR7jI",
      "title": "Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face",
      "author": "Merve Noyan, Hugging Face",
      "last_modified": "2026-09-23T13:30:16Z",
      "analysis_file": "analysis/dKcTBQzR7jI.json"
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
      "id": "pAnLpiAG6Es",
      "resource": "https://www.youtube.com/watch?v=pAnLpiAG6Es",
      "title": "MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify",
      "author": "Jan Čurn, Apify",
      "last_modified": "2026-10-02T14:00:05Z",
      "analysis_file": "analysis/pAnLpiAG6Es.json"
    },
    {
      "id": "qqXdLf3wy1E",
      "resource": "https://www.youtube.com/watch?v=qqXdLf3wy1E",
      "title": "Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant",
      "author": "Jesse Hu, Abundant",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qqXdLf3wy1E.json"
    },
    {
      "id": "s4r6nk5WsZw",
      "resource": "https://www.youtube.com/watch?v=s4r6nk5WsZw",
      "title": "MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal",
      "author": "Cornelia Davis, Temporal",
      "last_modified": "2026-08-02T20:00:06Z",
      "analysis_file": "analysis/s4r6nk5WsZw.json"
    },
    {
      "id": "v3Fr2JR47KA",
      "resource": "https://www.youtube.com/watch?v=v3Fr2JR47KA",
      "title": "The Future of MCP — David Soria Parra, Anthropic",
      "author": "David Soria Parra, Anthropic",
      "last_modified": "2026-04-19T15:00:06Z",
      "analysis_file": "analysis/v3Fr2JR47KA.json"
    },
    {
      "id": "vAIDdLKB6-w",
      "resource": "https://www.youtube.com/watch?v=vAIDdLKB6-w",
      "title": "A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon",
      "author": "Matthias Luebken, Tavon",
      "last_modified": "2026-05-11T17:00:06Z",
      "analysis_file": "analysis/vAIDdLKB6-w.json"
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
      "id": "zuMw0pkPXpU",
      "resource": "https://www.youtube.com/watch?v=zuMw0pkPXpU",
      "title": "Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks",
      "author": "Roy Derks",
      "last_modified": "2025-02-22T17:00:24Z",
      "analysis_file": "analysis/zuMw0pkPXpU.json"
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

# Expose stable async task handles with status, progress, cancellation and result retrieval

## What

Expose stable async task handles with status, progress, cancellation and result retrieval

A tool can start server-side work, return a handle, detach and expose progress/results later rather than holding a blocking model turn.

## Evidence

Source analysis [^1izYWsokr9s]; no independently matched timestamped quote published.

Source analysis [^7CrPrHgoEYk]; no independently matched timestamped quote published.

Source analysis [^7_WhRAuP2Wg]; no independently matched timestamped quote published.

Source analysis [^KUEmEb71vzQ]; no independently matched timestamped quote published.

Source analysis [^OV56RddyFuU]; no independently matched timestamped quote published.

Source analysis [^YNJvm7t3yq8]; no independently matched timestamped quote published.

> can use that identifier to connect to it from other processes. for example, to
> — 11:35 [^cI7zfqusmFU]

Source analysis [^dKcTBQzR7jI]; no independently matched timestamped quote published.

> of a digital twin of something else. We call it entity workflows as well. So,
> — 1:13:12 [^k8cnVCMYmNc]

> new feature called asynchronous task again most clients don't support it but
> — 15:25 [^pAnLpiAG6Es]

Source analysis [^qqXdLf3wy1E]; no independently matched timestamped quote published.

> celebrate a little bit is that the protocol is going stateless.
> — 16:16 [^s4r6nk5WsZw]

Source analysis [^v3Fr2JR47KA]; no independently matched timestamped quote published.

> creating and reusing existing sessions so we can back and forth um um
> — 16:40 [^vAIDdLKB6-w]

Source analysis [^wflNENRSUb4]; no independently matched timestamped quote published.

> you don't have any control over the tool calling process don't really know how
> — 13:19 [^zuMw0pkPXpU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1izYWsokr9s]: [Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal](https://www.youtube.com/watch?v=1izYWsokr9s); publication: 2025-07-28T15:15:00Z; analysis: `analysis/1izYWsokr9s.json`.
[^7CrPrHgoEYk]: [What the Best Agents Share — Mardu Swanepoel, Flinn AI](https://www.youtube.com/watch?v=7CrPrHgoEYk); publication: 2026-05-26T15:00:06Z; analysis: `analysis/7CrPrHgoEYk.json`.
[^7_WhRAuP2Wg]: [Building and Scaling an AI Agent Swarm of low latency real time voice bots: Damien Murphy](https://www.youtube.com/watch?v=7_WhRAuP2Wg); publication: 2024-10-08T18:28:46Z; analysis: `analysis/7_WhRAuP2Wg.json`.
[^KUEmEb71vzQ]: [Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI](https://www.youtube.com/watch?v=KUEmEb71vzQ); publication: 2025-04-23T16:00:26Z; analysis: `analysis/KUEmEb71vzQ.json`.
[^OV56RddyFuU]: [Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP & Finetuning  — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=OV56RddyFuU); publication: 2026-05-13T17:00:06Z; analysis: `analysis/OV56RddyFuU.json`.
[^YNJvm7t3yq8]: [Why Your AI UX Is Broken (and It's Not the Model's Fault) — Mike Christensen, Ably](https://www.youtube.com/watch?v=YNJvm7t3yq8); publication: 2026-05-17T15:30:06Z; analysis: `analysis/YNJvm7t3yq8.json`.
[^cI7zfqusmFU]: [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU); publication: 2026-09-14T15:30:30Z; analysis: `analysis/cI7zfqusmFU.json`.
[^dKcTBQzR7jI]: [Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face](https://www.youtube.com/watch?v=dKcTBQzR7jI); publication: 2026-09-23T13:30:16Z; analysis: `analysis/dKcTBQzR7jI.json`.
[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
[^pAnLpiAG6Es]: [MCP Doesn't Suck. Your Agent Does. — Jan Čurn, Apify](https://www.youtube.com/watch?v=pAnLpiAG6Es); publication: 2026-10-02T14:00:05Z; analysis: `analysis/pAnLpiAG6Es.json`.
[^qqXdLf3wy1E]: [Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant](https://www.youtube.com/watch?v=qqXdLf3wy1E); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qqXdLf3wy1E.json`.
[^s4r6nk5WsZw]: [MCP Tasks (async): Why Aren't Any Agents Supporting Them? — Cornelia Davis, Temporal](https://www.youtube.com/watch?v=s4r6nk5WsZw); publication: 2026-08-02T20:00:06Z; analysis: `analysis/s4r6nk5WsZw.json`.
[^v3Fr2JR47KA]: [The Future of MCP — David Soria Parra, Anthropic](https://www.youtube.com/watch?v=v3Fr2JR47KA); publication: 2026-04-19T15:00:06Z; analysis: `analysis/v3Fr2JR47KA.json`.
[^vAIDdLKB6-w]: [A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon](https://www.youtube.com/watch?v=vAIDdLKB6-w); publication: 2026-05-11T17:00:06Z; analysis: `analysis/vAIDdLKB6-w.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
[^zuMw0pkPXpU]: [Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks](https://www.youtube.com/watch?v=zuMw0pkPXpU); publication: 2025-02-22T17:00:24Z; analysis: `analysis/zuMw0pkPXpU.json`.
