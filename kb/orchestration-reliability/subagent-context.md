---
{
  "type": "technique",
  "id": "subagent-context",
  "title": "Give subagents a minimal self-contained task packet and bounded result",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-09-16T16:30:16Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "3hXJI2q0Jz8",
      "resource": "https://www.youtube.com/watch?v=3hXJI2q0Jz8",
      "title": "Recursive Coding Agents - Raymond Weitekamp, OpenProse",
      "author": "Raymond Weitekamp, OpenProse",
      "last_modified": "2026-06-25T21:00:06Z",
      "analysis_file": "analysis/3hXJI2q0Jz8.json"
    },
    {
      "id": "8oyalrfwgjw",
      "resource": "https://www.youtube.com/watch?v=8oyalrfwgjw",
      "title": "RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI",
      "author": "Shashi, Superagentic AI",
      "last_modified": "2026-07-12T23:00:06Z",
      "analysis_file": "analysis/8oyalrfwgjw.json"
    },
    {
      "id": "9arM9b7JgOo",
      "resource": "https://www.youtube.com/watch?v=9arM9b7JgOo",
      "title": "Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat",
      "author": "Jeffrey Lee-Chan, Snapchat",
      "last_modified": "2026-07-11T14:45:18Z",
      "analysis_file": "analysis/9arM9b7JgOo.json"
    },
    {
      "id": "F_RyElT_gJk",
      "resource": "https://www.youtube.com/watch?v=F_RyElT_gJk",
      "title": "The emerging skillset of wielding coding agents — Beyang Liu, Sourcegraph / Amp",
      "author": "Beyang Liu, Sourcegraph / Amp",
      "last_modified": "2025-06-30T22:54:36Z",
      "analysis_file": "analysis/F_RyElT_gJk.json"
    },
    {
      "id": "GdvKNwMcfd0",
      "resource": "https://www.youtube.com/watch?v=GdvKNwMcfd0",
      "title": "From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft",
      "author": "Chris Noring, Microsoft",
      "last_modified": "2026-07-11T14:00:06Z",
      "analysis_file": "analysis/GdvKNwMcfd0.json"
    },
    {
      "id": "MLhAA9yguwM",
      "resource": "https://www.youtube.com/watch?v=MLhAA9yguwM",
      "title": "The 3 Pillars of Autonomy – Michele Catasta, Replit",
      "author": "Michele Catasta, Replit",
      "last_modified": "2025-12-22T16:30:06Z",
      "analysis_file": "analysis/MLhAA9yguwM.json"
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
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "XKup1pj-34M",
      "resource": "https://www.youtube.com/watch?v=XKup1pj-34M",
      "title": "The New Application Layer - Malte Ubl, CTO Vercel",
      "author": "Malte Ubl, CTO Vercel",
      "last_modified": "2026-04-20T15:15:06Z",
      "analysis_file": "analysis/XKup1pj-34M.json"
    },
    {
      "id": "XLEYtv3cMlw",
      "resource": "https://www.youtube.com/watch?v=XLEYtv3cMlw",
      "title": "Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait",
      "author": "Sina Shahandeh, Radicait",
      "last_modified": "2026-07-18T23:30:06Z",
      "analysis_file": "analysis/XLEYtv3cMlw.json"
    },
    {
      "id": "ckLXb15BnM8",
      "resource": "https://www.youtube.com/watch?v=ckLXb15BnM8",
      "title": "The Adversarial Path to the Personal Assistant: Sumit Agarwal",
      "author": null,
      "last_modified": "2025-02-15T19:30:06Z",
      "analysis_file": "analysis/ckLXb15BnM8.json"
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
      "id": "iJVxxxHM_Oc",
      "resource": "https://www.youtube.com/watch?v=iJVxxxHM_Oc",
      "title": "Where RL Will Take Search — Maximilian-David Rumpf, SID.ai",
      "author": "Maximilian-David Rumpf, SID.ai",
      "last_modified": "2026-09-16T16:30:16Z",
      "analysis_file": "analysis/iJVxxxHM_Oc.json"
    },
    {
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
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
      "id": "wVl6ZjELpBk",
      "resource": "https://www.youtube.com/watch?v=wVl6ZjELpBk",
      "title": "Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI",
      "author": "Bill Chen & Brian Fioca, OpenAI",
      "last_modified": "2025-12-05T17:00:06Z",
      "analysis_file": "analysis/wVl6ZjELpBk.json"
    },
    {
      "id": "wflNENRSUb4",
      "resource": "https://www.youtube.com/watch?v=wflNENRSUb4",
      "title": "Give Your Agent a Computer — Nico Albanese, Vercel",
      "author": "Nico Albanese, Vercel",
      "last_modified": "2026-05-12T18:00:06Z",
      "analysis_file": "analysis/wflNENRSUb4.json"
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

# Give subagents a minimal self-contained task packet and bounded result

## What

Give subagents a minimal self-contained task packet and bounded result

Keep independent exploration out of the main conversation and return a compact result with source references rather than all raw tool output.

## Evidence

Source analysis [^3hXJI2q0Jz8]; no independently matched timestamped quote published.

Source analysis [^8oyalrfwgjw]; no independently matched timestamped quote published.

> Um so imagine like 25% of your context already taken up by implementation.
> — 05:51 [^9arM9b7JgOo]

Source analysis [^F_RyElT_gJk]; no independently matched timestamped quote published.

Source analysis [^GdvKNwMcfd0]; no independently matched timestamped quote published.

Source analysis [^MLhAA9yguwM]; no independently matched timestamped quote published.

Source analysis [^NTBX-wxUhHs]; no independently matched timestamped quote published.

> how do you train models to actually work collaboratively with other models? I
> — 19:11 [^QHBjufYK8TA]

> own context and it feeds back only the results and this is how you don't
> — 29:09 [^RFKCzGlAU6Q]

> switching a string to maybe an object here uh depending on what you're
> — 30:39 [^RFKCzGlAU6Q]

Source analysis [^XKup1pj-34M]; no independently matched timestamped quote published.

> Spinberger's Oracle CLI which packages the code and package the data and send
> — 15:59 [^XLEYtv3cMlw]

Source analysis [^ckLXb15BnM8]; no independently matched timestamped quote published.

Source analysis [^esY99nYXxR4]; no independently matched timestamped quote published.

Source analysis [^iJVxxxHM_Oc]; no independently matched timestamped quote published.

> I want it to have its own standalone context
> — 33:19 [^pFsfax19yOM]

> without all of the surrounding context. It's also
> — 18:01 [^spNAUEgq_A8]

Source analysis [^wVl6ZjELpBk]; no independently matched timestamped quote published.

> Used 30,000 tokens, but just returned like 500 at the very end. So that keeps
> — 1:08:13 [^wflNENRSUb4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^3hXJI2q0Jz8]: [Recursive Coding Agents - Raymond Weitekamp, OpenProse](https://www.youtube.com/watch?v=3hXJI2q0Jz8); publication: 2026-06-25T21:00:06Z; analysis: `analysis/3hXJI2q0Jz8.json`.
[^8oyalrfwgjw]: [RLM: Recursive Language Models for Large Codebases - Shashi, Superagentic AI](https://www.youtube.com/watch?v=8oyalrfwgjw); publication: 2026-07-12T23:00:06Z; analysis: `analysis/8oyalrfwgjw.json`.
[^9arM9b7JgOo]: [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo); publication: 2026-07-11T14:45:18Z; analysis: `analysis/9arM9b7JgOo.json`.
[^F_RyElT_gJk]: [The emerging skillset of wielding coding agents — Beyang Liu, Sourcegraph / Amp](https://www.youtube.com/watch?v=F_RyElT_gJk); publication: 2025-06-30T22:54:36Z; analysis: `analysis/F_RyElT_gJk.json`.
[^GdvKNwMcfd0]: [From Writing Code to Designing Systems: How the Developer Role is Changing — Chris Noring, Microsoft](https://www.youtube.com/watch?v=GdvKNwMcfd0); publication: 2026-07-11T14:00:06Z; analysis: `analysis/GdvKNwMcfd0.json`.
[^MLhAA9yguwM]: [The 3 Pillars of Autonomy – Michele Catasta, Replit](https://www.youtube.com/watch?v=MLhAA9yguwM); publication: 2025-12-22T16:30:06Z; analysis: `analysis/MLhAA9yguwM.json`.
[^NTBX-wxUhHs]: [Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA](https://www.youtube.com/watch?v=NTBX-wxUhHs); publication: 2025-11-24T20:16:36Z; analysis: `analysis/NTBX-wxUhHs.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^XKup1pj-34M]: [The New Application Layer - Malte Ubl, CTO Vercel](https://www.youtube.com/watch?v=XKup1pj-34M); publication: 2026-04-20T15:15:06Z; analysis: `analysis/XKup1pj-34M.json`.
[^XLEYtv3cMlw]: [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](https://www.youtube.com/watch?v=XLEYtv3cMlw); publication: 2026-07-18T23:30:06Z; analysis: `analysis/XLEYtv3cMlw.json`.
[^ckLXb15BnM8]: [The Adversarial Path to the Personal Assistant: Sumit Agarwal](https://www.youtube.com/watch?v=ckLXb15BnM8); publication: 2025-02-15T19:30:06Z; analysis: `analysis/ckLXb15BnM8.json`.
[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
[^iJVxxxHM_Oc]: [Where RL Will Take Search — Maximilian-David Rumpf, SID.ai](https://www.youtube.com/watch?v=iJVxxxHM_Oc); publication: 2026-09-16T16:30:16Z; analysis: `analysis/iJVxxxHM_Oc.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^spNAUEgq_A8]: [The Future Is Domain-Specific Agents - Justin Schroeder, StandardAgents](https://www.youtube.com/watch?v=spNAUEgq_A8); publication: 2026-06-29T03:00:14Z; analysis: `analysis/spNAUEgq_A8.json`.
[^wVl6ZjELpBk]: [Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI](https://www.youtube.com/watch?v=wVl6ZjELpBk); publication: 2025-12-05T17:00:06Z; analysis: `analysis/wVl6ZjELpBk.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
