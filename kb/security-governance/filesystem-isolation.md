---
{
  "type": "technique",
  "id": "filesystem-isolation",
  "title": "Enforce filesystem and process isolation for untrusted code",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-21T19:01:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "33Oct2hqGnk",
      "resource": "https://www.youtube.com/watch?v=33Oct2hqGnk",
      "title": "Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS",
      "author": "Sandhya Subramani, AWS",
      "last_modified": "2026-10-04T21:00:13Z",
      "analysis_file": "analysis/33Oct2hqGnk.json"
    },
    {
      "id": "5eJqXtevlXg",
      "resource": "https://www.youtube.com/watch?v=5eJqXtevlXg",
      "title": "Hacking Subagents Into Codex CLI — Brian John, Betterup",
      "author": "Brian John, Betterup",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/5eJqXtevlXg.json"
    },
    {
      "id": "G7aSH6N7qY4",
      "resource": "https://www.youtube.com/watch?v=G7aSH6N7qY4",
      "title": "AI + Security & Safety — Don Bosco Durai",
      "author": "Don Bosco Durai",
      "last_modified": "2025-04-19T16:00:06Z",
      "analysis_file": "analysis/G7aSH6N7qY4.json"
    },
    {
      "id": "OE_lLNCNfQo",
      "resource": "https://www.youtube.com/watch?v=OE_lLNCNfQo",
      "title": "YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker",
      "author": "Rowan Christmas, Docker",
      "last_modified": "2026-10-03T00:30:06Z",
      "analysis_file": "analysis/OE_lLNCNfQo.json"
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
      "id": "T3SS931wU0I",
      "resource": "https://www.youtube.com/watch?v=T3SS931wU0I",
      "title": "Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust",
      "author": "Braintrust",
      "last_modified": "2026-10-05T15:30:36Z",
      "analysis_file": "analysis/T3SS931wU0I.json"
    },
    {
      "id": "WE_Gnowy3uw",
      "resource": "https://www.youtube.com/watch?v=WE_Gnowy3uw",
      "title": "Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor",
      "author": "David Gomes, Cursor",
      "last_modified": "2026-04-30T12:00:06Z",
      "analysis_file": "analysis/WE_Gnowy3uw.json"
    },
    {
      "id": "YBYUvGOuotE",
      "resource": "https://www.youtube.com/watch?v=YBYUvGOuotE",
      "title": "MCP = Mega Context Problem - Matt Carey",
      "author": "Matt Carey",
      "last_modified": "2026-04-25T17:00:06Z",
      "analysis_file": "analysis/YBYUvGOuotE.json"
    },
    {
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "ZUZVNKFSmTM",
      "resource": "https://www.youtube.com/watch?v=ZUZVNKFSmTM",
      "title": "How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker",
      "author": "Jim Clark, Docker",
      "last_modified": "2026-10-06T00:30:15Z",
      "analysis_file": "analysis/ZUZVNKFSmTM.json"
    },
    {
      "id": "aqW68Is_Kj4",
      "resource": "https://www.youtube.com/watch?v=aqW68Is_Kj4",
      "title": "Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic",
      "author": "Evolving Claude APIs for Agents, Anthropic",
      "last_modified": "2025-12-04T20:14:55Z",
      "analysis_file": "analysis/aqW68Is_Kj4.json"
    },
    {
      "id": "bU5gDVyu_28",
      "resource": "https://www.youtube.com/watch?v=bU5gDVyu_28",
      "title": "Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One",
      "author": "Max Kanat-Alexander, Capital One",
      "last_modified": "2026-10-21T19:01:02Z",
      "analysis_file": "analysis/bU5gDVyu_28.json"
    },
    {
      "id": "fz6-NS7qpZc",
      "resource": "https://www.youtube.com/watch?v=fz6-NS7qpZc",
      "title": "How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B",
      "author": "Matt Brockman, E2B",
      "last_modified": "2026-10-05T18:00:17Z",
      "analysis_file": "analysis/fz6-NS7qpZc.json"
    },
    {
      "id": "iH_wV8BbS24",
      "resource": "https://www.youtube.com/watch?v=iH_wV8BbS24",
      "title": "Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-10-12T05:10:18Z",
      "analysis_file": "analysis/iH_wV8BbS24.json"
    },
    {
      "id": "iQ5xldZ9StU",
      "resource": "https://www.youtube.com/watch?v=iQ5xldZ9StU",
      "title": "Realtime multiplayer, automation, and you! — Idan Gazit, GitHub",
      "author": "Idan Gazit, GitHub",
      "last_modified": "2026-08-08T21:30:06Z",
      "analysis_file": "analysis/iQ5xldZ9StU.json"
    },
    {
      "id": "k0VIgKAUkP4",
      "resource": "https://www.youtube.com/watch?v=k0VIgKAUkP4",
      "title": "[Full Workshop] How to add secure code interpreting in your AI app: Vasek Mlejnsky",
      "author": null,
      "last_modified": "2025-02-06T21:56:42Z",
      "analysis_file": "analysis/k0VIgKAUkP4.json"
    },
    {
      "id": "kiClTcJUnhc",
      "resource": "https://www.youtube.com/watch?v=kiClTcJUnhc",
      "title": "Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic",
      "author": "CJ Avilla & Harrison Stall, Anthropic",
      "last_modified": "2026-10-16T19:00:10Z",
      "analysis_file": "analysis/kiClTcJUnhc.json"
    },
    {
      "id": "kv-QAuKWllQ",
      "resource": "https://www.youtube.com/watch?v=kv-QAuKWllQ",
      "title": "How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco",
      "author": "Rene Brandel, Casco",
      "last_modified": "2025-07-30T15:45:06Z",
      "analysis_file": "analysis/kv-QAuKWllQ.json"
    },
    {
      "id": "l1-D89bAuOA",
      "resource": "https://www.youtube.com/watch?v=l1-D89bAuOA",
      "title": "Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google",
      "author": "Ashok Chandrasekar & Jason Kramberger, Google",
      "last_modified": "2026-09-19T16:00:07Z",
      "analysis_file": "analysis/l1-D89bAuOA.json"
    },
    {
      "id": "spNAUEgq_A8",
      "resource": "https://www.youtube.com/watch?v=spNAUEgq_A8",
      "title": "The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents",
      "author": "Justin Schroeder, StandardAgents",
      "last_modified": "2026-06-29T03:00:14Z",
      "analysis_file": "analysis/spNAUEgq_A8.json"
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
      "id": "w7IMuYsBNr8",
      "resource": "https://www.youtube.com/watch?v=w7IMuYsBNr8",
      "title": "OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)",
      "author": "Fouad Matin (Codex, Agent Robustness)",
      "last_modified": "2025-07-30T15:00:06Z",
      "analysis_file": "analysis/w7IMuYsBNr8.json"
    },
    {
      "id": "wCIYViPd4SU",
      "resource": "https://www.youtube.com/watch?v=wCIYViPd4SU",
      "title": "Tethered: Our Agents Are Us — Shu Fang, Two Sigma",
      "author": "Shu Fang, Two Sigma",
      "last_modified": "2026-09-03T14:30:21Z",
      "analysis_file": "analysis/wCIYViPd4SU.json"
    },
    {
      "id": "wsFd22SL1s8",
      "resource": "https://www.youtube.com/watch?v=wsFd22SL1s8",
      "title": "Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI",
      "author": "Abhishek Bhardwaj, OpenAI",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/wsFd22SL1s8.json"
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

# Enforce filesystem and process isolation for untrusted code

## What

Enforce filesystem and process isolation for untrusted code

A guest kernel boundary makes host compromise materially harder than processes sharing the host kernel, without assuming any sandbox is invulnerable.

## Evidence

Source analysis [^33Oct2hqGnk]; no independently matched timestamped quote published.

Source analysis [^5eJqXtevlXg]; no independently matched timestamped quote published.

Source analysis [^G7aSH6N7qY4]; no independently matched timestamped quote published.

Source analysis [^OE_lLNCNfQo]; no independently matched timestamped quote published.

> a hardware level. You can still attack the host, but it's
> — 27:23 [^OqM67QG_Ikk]

> device, we've only given it permission to access block resources. So, you can't
> — 24:04 [^OqM67QG_Ikk]

> passing the parent span IDs as environment variables. So, if that
> — 13:36 [^T3SS931wU0I]

> Now, we're trusting the model. So, it's you could say it's a bit vibes-based
> — 12:51 [^WE_Gnowy3uw]

> on your computer, um and then finally, uh they only work in Git repos. So, if
> — 18:28 [^WE_Gnowy3uw]

> And if we print them, there are no secrets.
> — 11:51 [^YBYUvGOuotE]

> your offering where you have an isolated box for each task, which is super
> — 09:40 [^YIxzNZDDy1A]

> What resources? What work trees? We get used to thinking about modeling
> — 15:51 [^ZUZVNKFSmTM]

Source analysis [^aqW68Is_Kj4]; no independently matched timestamped quote published.

Source analysis [^bU5gDVyu_28]; no independently matched timestamped quote published.

Source analysis [^fz6-NS7qpZc]; no independently matched timestamped quote published.

> pick the right environment for the job. Right? Sometimes you really do want to
> — 13:35 [^iH_wV8BbS24]

> none of this is running on my machine. It's all micro VMs in the cloud. So,
> — 15:09 [^iQ5xldZ9StU]

Source analysis [^k0VIgKAUkP4]; no independently matched timestamped quote published.

Source analysis [^kiClTcJUnhc]; no independently matched timestamped quote published.

Source analysis [^kv-QAuKWllQ]; no independently matched timestamped quote published.

Source analysis [^l1-D89bAuOA]; no independently matched timestamped quote published.

> every agent should really have a file system. If you've ever done this with
> — 27:01 [^spNAUEgq_A8]

Source analysis [^vAIDdLKB6-w]; no independently matched timestamped quote published.

Source analysis [^w7IMuYsBNr8]; no independently matched timestamped quote published.

Source analysis [^wCIYViPd4SU]; no independently matched timestamped quote published.

Source analysis [^wsFd22SL1s8]; no independently matched timestamped quote published.

> always recommended to uh use it in a sandbox environment. Also in langun it
> — 36:53 [^ynJyIKwjonM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^33Oct2hqGnk]: [Agents That Write Their Own Tools at Runtime — Sandhya Subramani, AWS](https://www.youtube.com/watch?v=33Oct2hqGnk); publication: 2026-10-04T21:00:13Z; analysis: `analysis/33Oct2hqGnk.json`.
[^5eJqXtevlXg]: [Hacking Subagents Into Codex CLI — Brian John, Betterup](https://www.youtube.com/watch?v=5eJqXtevlXg); publication: 2025-11-24T20:16:36Z; analysis: `analysis/5eJqXtevlXg.json`.
[^G7aSH6N7qY4]: [AI + Security & Safety — Don Bosco Durai](https://www.youtube.com/watch?v=G7aSH6N7qY4); publication: 2025-04-19T16:00:06Z; analysis: `analysis/G7aSH6N7qY4.json`.
[^OE_lLNCNfQo]: [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo); publication: 2026-10-03T00:30:06Z; analysis: `analysis/OE_lLNCNfQo.json`.
[^OqM67QG_Ikk]: [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk); publication: 2026-07-13T17:00:06Z; analysis: `analysis/OqM67QG_Ikk.json`.
[^T3SS931wU0I]: [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](https://www.youtube.com/watch?v=T3SS931wU0I); publication: 2026-10-05T15:30:36Z; analysis: `analysis/T3SS931wU0I.json`.
[^WE_Gnowy3uw]: [Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor](https://www.youtube.com/watch?v=WE_Gnowy3uw); publication: 2026-04-30T12:00:06Z; analysis: `analysis/WE_Gnowy3uw.json`.
[^YBYUvGOuotE]: [MCP = Mega Context Problem - Matt Carey](https://www.youtube.com/watch?v=YBYUvGOuotE); publication: 2026-04-25T17:00:06Z; analysis: `analysis/YBYUvGOuotE.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^ZUZVNKFSmTM]: [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](https://www.youtube.com/watch?v=ZUZVNKFSmTM); publication: 2026-10-06T00:30:15Z; analysis: `analysis/ZUZVNKFSmTM.json`.
[^aqW68Is_Kj4]: [Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic](https://www.youtube.com/watch?v=aqW68Is_Kj4); publication: 2025-12-04T20:14:55Z; analysis: `analysis/aqW68Is_Kj4.json`.
[^bU5gDVyu_28]: [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=bU5gDVyu_28); publication: 2026-10-21T19:01:02Z; analysis: `analysis/bU5gDVyu_28.json`.
[^fz6-NS7qpZc]: [How I Learned to Stop Worrying and Love the Sandbox — Matt Brockman, E2B](https://www.youtube.com/watch?v=fz6-NS7qpZc); publication: 2026-10-05T18:00:17Z; analysis: `analysis/fz6-NS7qpZc.json`.
[^iH_wV8BbS24]: [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](https://www.youtube.com/watch?v=iH_wV8BbS24); publication: 2026-10-12T05:10:18Z; analysis: `analysis/iH_wV8BbS24.json`.
[^iQ5xldZ9StU]: [Realtime multiplayer, automation, and you! — Idan Gazit, GitHub](https://www.youtube.com/watch?v=iQ5xldZ9StU); publication: 2026-08-08T21:30:06Z; analysis: `analysis/iQ5xldZ9StU.json`.
[^k0VIgKAUkP4]: [[Full Workshop] How to add secure code interpreting in your AI app: Vasek Mlejnsky](https://www.youtube.com/watch?v=k0VIgKAUkP4); publication: 2025-02-06T21:56:42Z; analysis: `analysis/k0VIgKAUkP4.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^kv-QAuKWllQ]: [How we hacked YC Spring 2025 batch’s AI agents — Rene Brandel, Casco](https://www.youtube.com/watch?v=kv-QAuKWllQ); publication: 2025-07-30T15:45:06Z; analysis: `analysis/kv-QAuKWllQ.json`.
[^l1-D89bAuOA]: [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](https://www.youtube.com/watch?v=l1-D89bAuOA); publication: 2026-09-19T16:00:07Z; analysis: `analysis/l1-D89bAuOA.json`.
[^spNAUEgq_A8]: [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](https://www.youtube.com/watch?v=spNAUEgq_A8); publication: 2026-06-29T03:00:14Z; analysis: `analysis/spNAUEgq_A8.json`.
[^vAIDdLKB6-w]: [A Piece of Pi: Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon](https://www.youtube.com/watch?v=vAIDdLKB6-w); publication: 2026-05-11T17:00:06Z; analysis: `analysis/vAIDdLKB6-w.json`.
[^w7IMuYsBNr8]: [OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)](https://www.youtube.com/watch?v=w7IMuYsBNr8); publication: 2025-07-30T15:00:06Z; analysis: `analysis/w7IMuYsBNr8.json`.
[^wCIYViPd4SU]: [Tethered: Our Agents Are Us — Shu Fang, Two Sigma](https://www.youtube.com/watch?v=wCIYViPd4SU); publication: 2026-09-03T14:30:21Z; analysis: `analysis/wCIYViPd4SU.json`.
[^wsFd22SL1s8]: [Arrakis: How To Build An AI Sandbox From Scratch - Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=wsFd22SL1s8); publication: 2025-06-03T22:22:29Z; analysis: `analysis/wsFd22SL1s8.json`.
[^ynJyIKwjonM]: [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM); publication: 2026-05-08T13:00:06Z; analysis: `analysis/ynJyIKwjonM.json`.
