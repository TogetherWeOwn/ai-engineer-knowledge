---
{
  "type": "technique",
  "id": "compaction-fidelity",
  "title": "Validate compaction and pruning against evidence loss",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-10-17T07:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-QFHIoCo-Ko",
      "resource": "https://www.youtube.com/watch?v=-QFHIoCo-Ko",
      "title": "Full Walkthrough: Workflow for AI Coding — Matt Pocock",
      "author": "Matt Pocock",
      "last_modified": "2026-04-24T15:15:38Z",
      "analysis_file": "analysis/-QFHIoCo-Ko.json"
    },
    {
      "id": "8kMaTybvDUw",
      "resource": "https://www.youtube.com/watch?v=8kMaTybvDUw",
      "title": "12-Factor Agents: Patterns of reliable LLM applications — Dex Horthy, HumanLayer",
      "author": "Dex Horthy, HumanLayer",
      "last_modified": "2025-07-03T20:50:54Z",
      "analysis_file": "analysis/8kMaTybvDUw.json"
    },
    {
      "id": "ACPEpji5NV4",
      "resource": "https://www.youtube.com/watch?v=ACPEpji5NV4",
      "title": "Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash",
      "author": "Raghav Saboo, DoorDash",
      "last_modified": "2026-09-25T13:30:37Z",
      "analysis_file": "analysis/ACPEpji5NV4.json"
    },
    {
      "id": "CvRngaQZQ3Y",
      "resource": "https://www.youtube.com/watch?v=CvRngaQZQ3Y",
      "title": "Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain",
      "author": "Vivek Trivedy, LangChain",
      "last_modified": "2026-08-12T19:00:01Z",
      "analysis_file": "analysis/CvRngaQZQ3Y.json"
    },
    {
      "id": "IN-rb-9WmiY",
      "resource": "https://www.youtube.com/watch?v=IN-rb-9WmiY",
      "title": "Pinecone 2.0 — Edo Liberty, Pinecone",
      "author": "Edo Liberty, Pinecone",
      "last_modified": "2026-09-16T13:00:06Z",
      "analysis_file": "analysis/IN-rb-9WmiY.json"
    },
    {
      "id": "JnubYCYunk8",
      "resource": "https://www.youtube.com/watch?v=JnubYCYunk8",
      "title": "Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI",
      "author": "Kushan Raj, Sarvam AI",
      "last_modified": "2026-06-28T15:30:40Z",
      "analysis_file": "analysis/JnubYCYunk8.json"
    },
    {
      "id": "KcVkq5L-0f0",
      "resource": "https://www.youtube.com/watch?v=KcVkq5L-0f0",
      "title": "Your agents lack context: Here's how to fix \"You're absolutely right!\" — Brandon Waselnuk, Unblocked",
      "author": "Brandon Waselnuk, Unblocked",
      "last_modified": "2026-09-09T14:30:12Z",
      "analysis_file": "analysis/KcVkq5L-0f0.json"
    },
    {
      "id": "KtBivPzmOM8",
      "resource": "https://www.youtube.com/watch?v=KtBivPzmOM8",
      "title": "Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle",
      "author": "Nacho Martinez, Oracle",
      "last_modified": "2026-10-17T07:00:25Z",
      "analysis_file": "analysis/KtBivPzmOM8.json"
    },
    {
      "id": "LrGCT7G_rU8",
      "resource": "https://www.youtube.com/watch?v=LrGCT7G_rU8",
      "title": "Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon",
      "author": "Anna Marie Benzon",
      "last_modified": "2026-06-29T00:30:05Z",
      "analysis_file": "analysis/LrGCT7G_rU8.json"
    },
    {
      "id": "N4vCBM5YbN0",
      "resource": "https://www.youtube.com/watch?v=N4vCBM5YbN0",
      "title": "Building Code First AI Agents with Azure AI Agent Service — Cedric Vidal, Microsoft",
      "author": "Cedric Vidal, Microsoft",
      "last_modified": "2025-06-27T10:03:21Z",
      "analysis_file": "analysis/N4vCBM5YbN0.json"
    },
    {
      "id": "Nqb7JTx0Pqo",
      "resource": "https://www.youtube.com/watch?v=Nqb7JTx0Pqo",
      "title": "MCP Agent Fine tuning Workshop - Ronan McGovern",
      "author": "Ronan McGovern",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/Nqb7JTx0Pqo.json"
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
      "id": "RjfbvDXpFls",
      "resource": "https://www.youtube.com/watch?v=RjfbvDXpFls",
      "title": "Building pi in a World of Slop — Mario Zechner",
      "author": "Mario Zechner",
      "last_modified": "2026-04-16T22:58:06Z",
      "analysis_file": "analysis/RjfbvDXpFls.json"
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
      "id": "UPwGaM2MKHY",
      "resource": "https://www.youtube.com/watch?v=UPwGaM2MKHY",
      "title": "The Log Is The Agent - Ishaan Sehgal, Omnara",
      "author": "Ishaan Sehgal, Omnara",
      "last_modified": "2026-06-25T21:15:06Z",
      "analysis_file": "analysis/UPwGaM2MKHY.json"
    },
    {
      "id": "Uv0nAf_7tyU",
      "resource": "https://www.youtube.com/watch?v=Uv0nAf_7tyU",
      "title": "Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T05:44:00Z",
      "analysis_file": "analysis/Uv0nAf_7tyU.json"
    },
    {
      "id": "XsvUhpnHepE",
      "resource": "https://www.youtube.com/watch?v=XsvUhpnHepE",
      "title": "The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs",
      "author": "Giedrius Šteimantas, Oxylabs",
      "last_modified": "2026-08-26T07:00:06Z",
      "analysis_file": "analysis/XsvUhpnHepE.json"
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
      "id": "Z-c11pV_uvU",
      "resource": "https://www.youtube.com/watch?v=Z-c11pV_uvU",
      "title": "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley",
      "author": "Frank Coyle, UC Berkeley",
      "last_modified": "2026-08-08T16:00:06Z",
      "analysis_file": "analysis/Z-c11pV_uvU.json"
    },
    {
      "id": "ZB7l4uxW3Yo",
      "resource": "https://www.youtube.com/watch?v=ZB7l4uxW3Yo",
      "title": "Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson",
      "author": "Greg Benson",
      "last_modified": "2025-06-03T22:31:07Z",
      "analysis_file": "analysis/ZB7l4uxW3Yo.json"
    },
    {
      "id": "ZRM_TfEZcIo",
      "resource": "https://www.youtube.com/watch?v=ZRM_TfEZcIo",
      "title": "Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "author": "Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "last_modified": "2026-06-26T14:00:07Z",
      "analysis_file": "analysis/ZRM_TfEZcIo.json"
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
      "id": "bjNYEc908oQ",
      "resource": "https://www.youtube.com/watch?v=bjNYEc908oQ",
      "title": "Building Reliable Agentic Systems: Eno Reyes",
      "author": null,
      "last_modified": "2024-08-20T13:44:51Z",
      "analysis_file": "analysis/bjNYEc908oQ.json"
    },
    {
      "id": "bmWZk9vTze0",
      "resource": "https://www.youtube.com/watch?v=bmWZk9vTze0",
      "title": "MCP is all you need — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-07-18T18:52:25Z",
      "analysis_file": "analysis/bmWZk9vTze0.json"
    },
    {
      "id": "cKhpeEBnT1o",
      "resource": "https://www.youtube.com/watch?v=cKhpeEBnT1o",
      "title": "Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa",
      "author": "Jakub Hojsan, Exa",
      "last_modified": "2026-10-02T15:30:31Z",
      "analysis_file": "analysis/cKhpeEBnT1o.json"
    },
    {
      "id": "cZ5ZJy19KMo",
      "resource": "https://www.youtube.com/watch?v=cZ5ZJy19KMo",
      "title": "Mission-Critical Evals at Scale (Learnings from 100k medical decisions)",
      "author": null,
      "last_modified": "2025-02-22T19:00:06Z",
      "analysis_file": "analysis/cZ5ZJy19KMo.json"
    },
    {
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
    },
    {
      "id": "eIoohUmYpGI",
      "resource": "https://www.youtube.com/watch?v=eIoohUmYpGI",
      "title": "The Infinite Software Crisis – Jake Nations, Netflix",
      "author": "Jake Nations, Netflix",
      "last_modified": "2025-12-20T17:00:06Z",
      "analysis_file": "analysis/eIoohUmYpGI.json"
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
      "id": "fnLBmfsI_Fg",
      "resource": "https://www.youtube.com/watch?v=fnLBmfsI_Fg",
      "title": "Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft",
      "author": "Joel Allou & Ornella Bahidika, Microsoft",
      "last_modified": "2026-07-20T06:25:15Z",
      "analysis_file": "analysis/fnLBmfsI_Fg.json"
    },
    {
      "id": "g03m-WFEu1U",
      "resource": "https://www.youtube.com/watch?v=g03m-WFEu1U",
      "title": "How to Improve your Vibe Coding — Ian Butler",
      "author": "Ian Butler",
      "last_modified": "2025-08-03T04:32:57Z",
      "analysis_file": "analysis/g03m-WFEu1U.json"
    },
    {
      "id": "iRcX54EO5g8",
      "resource": "https://www.youtube.com/watch?v=iRcX54EO5g8",
      "title": "Your agent is blindfolded — Johan Lajili, Poolside AI",
      "author": "Johan Lajili, Poolside AI",
      "last_modified": "2026-07-08T13:45:06Z",
      "analysis_file": "analysis/iRcX54EO5g8.json"
    },
    {
      "id": "il1c1a2FufU",
      "resource": "https://www.youtube.com/watch?v=il1c1a2FufU",
      "title": "Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex",
      "author": null,
      "last_modified": "2026-07-24T15:00:06Z",
      "analysis_file": "analysis/il1c1a2FufU.json"
    },
    {
      "id": "jJQoVkd5yLg",
      "resource": "https://www.youtube.com/watch?v=jJQoVkd5yLg",
      "title": "Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto",
      "author": "Abhi Arya, Reducto",
      "last_modified": "2026-10-08T17:00:23Z",
      "analysis_file": "analysis/jJQoVkd5yLg.json"
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
      "id": "oVsEddfhdxc",
      "resource": "https://www.youtube.com/watch?v=oVsEddfhdxc",
      "title": "We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect",
      "author": "Elie Bakouch, Prime Intellect",
      "last_modified": "2026-09-26T17:30:10Z",
      "analysis_file": "analysis/oVsEddfhdxc.json"
    },
    {
      "id": "prttz9_1XDc",
      "resource": "https://www.youtube.com/watch?v=prttz9_1XDc",
      "title": "Enhancing Quality and Security in CI: Gunjan Patel",
      "author": null,
      "last_modified": "2024-11-27T19:56:40Z",
      "analysis_file": "analysis/prttz9_1XDc.json"
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
      "id": "s67bE2Ur3bY",
      "resource": "https://www.youtube.com/watch?v=s67bE2Ur3bY",
      "title": "Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi",
      "author": "Sai Krishna Rallabandi",
      "last_modified": "2026-07-29T22:58:19Z",
      "analysis_file": "analysis/s67bE2Ur3bY.json"
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
      "id": "spxoDAfh5ig",
      "resource": "https://www.youtube.com/watch?v=spxoDAfh5ig",
      "title": "Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked",
      "author": "Peter Werry, Unblocked",
      "last_modified": "2026-10-11T10:00:18Z",
      "analysis_file": "analysis/spxoDAfh5ig.json"
    },
    {
      "id": "uIiA6DquRiE",
      "resource": "https://www.youtube.com/watch?v=uIiA6DquRiE",
      "title": "Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth",
      "author": "Daniel Han, Unsloth",
      "last_modified": "2026-07-17T17:00:06Z",
      "analysis_file": "analysis/uIiA6DquRiE.json"
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
      "id": "wVl6ZjELpBk",
      "resource": "https://www.youtube.com/watch?v=wVl6ZjELpBk",
      "title": "Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI",
      "author": "Bill Chen & Brian Fioca, OpenAI",
      "last_modified": "2025-12-05T17:00:06Z",
      "analysis_file": "analysis/wVl6ZjELpBk.json"
    },
    {
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
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
      "id": "zwItokY087U",
      "resource": "https://www.youtube.com/watch?v=zwItokY087U",
      "title": "10x Development: LLMs For the working Programmer - Manuel Odendahl",
      "author": "Manuel Odendahl",
      "last_modified": "2024-08-21T16:36:00Z",
      "analysis_file": "analysis/zwItokY087U.json"
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

# Validate compaction and pruning against evidence loss

## What

Validate compaction and pruning against evidence loss

Dropping old results can erase facts the model needs later; retain full evidence even when reducing injected context.

## Evidence

Source analysis [^-QFHIoCo-Ko]; no independently matched timestamped quote published.

Source analysis [^8kMaTybvDUw]; no independently matched timestamped quote published.

Source analysis [^ACPEpji5NV4]; no independently matched timestamped quote published.

Source analysis [^CvRngaQZQ3Y]; no independently matched timestamped quote published.

Source analysis [^IN-rb-9WmiY]; no independently matched timestamped quote published.

Source analysis [^JnubYCYunk8]; no independently matched timestamped quote published.

> things are no longer there when it's hydrated with context. Hydrated.
> — 09:42 [^KcVkq5L-0f0]

Source analysis [^KtBivPzmOM8]; no independently matched timestamped quote published.

Source analysis [^LrGCT7G_rU8]; no independently matched timestamped quote published.

Source analysis [^N4vCBM5YbN0]; no independently matched timestamped quote published.

Source analysis [^Nqb7JTx0Pqo]; no independently matched timestamped quote published.

> Instead of dumping the full thing, it just references them by file. And then
> — 23:54 [^QHBjufYK8TA]

> just starting a new thread and you're giving it the information it needs for a
> — 46:14 [^RFKCzGlAU6Q]

> given some conditions, open code code would just uh prune tool outputs
> — 03:44 [^RjfbvDXpFls]

> and the most important lesson from this is if the gate can be skipped it will be
> — 48:31 [^SQMCtZX3trg]

> point is the full log is the record and a compaction is just one projection of
> — 05:05 [^UPwGaM2MKHY]

> thrown away. We're not compacting and changing your event stream. We're always
> — 10:00 [^Uv0nAf_7tyU]

Source analysis [^XsvUhpnHepE]; no independently matched timestamped quote published.

> trajectories, those have been uploaded to weave and you can just inspect them.
> — 34:02 [^YIxzNZDDy1A]

> he's got he you can extend his base class and have your own
> — 17:56 [^Z-c11pV_uvU]

> you can check your token count, and you can determine how big the token
> — 16:46 [^Z-c11pV_uvU]

Source analysis [^ZB7l4uxW3Yo]; no independently matched timestamped quote published.

Source analysis [^ZRM_TfEZcIo]; no independently matched timestamped quote published.

Source analysis [^aqW68Is_Kj4]; no independently matched timestamped quote published.

> also facilitates error propagation a simple mistake especially early on in
> — 03:55 [^bjNYEc908oQ]

Source analysis [^bmWZk9vTze0]; no independently matched timestamped quote published.

Source analysis [^cKhpeEBnT1o]; no independently matched timestamped quote published.

> needs surfaced in an accessible way without any scrolling required so they
> — 02:33 [^cZ5ZJy19KMo]

> heavy reads and writes. You can see which ones are my heavy reads that have
> — 17:42 [^cgimkNGNjvU]

> three focused outputs, each validated before proceeding. No abandoned
> — 13:38 [^eIoohUmYpGI]

> Um, and so we're keeping the latest result. We don't reset the system prompt
> — 07:12 [^esY99nYXxR4]

> inconsistent. There was no control over what was important, you know, we're just
> — 06:29 [^esY99nYXxR4]

> a system in place to do that, and they hand the model a summary every turn.
> — 01:19 [^fnLBmfsI_Fg]

Source analysis [^g03m-WFEu1U]; no independently matched timestamped quote published.

> to say like a very token compressed version of what's going on on a web page
> — 04:09 [^iRcX54EO5g8]

Source analysis [^il1c1a2FufU]; no independently matched timestamped quote published.

> back the live state of our pipeline from the context of the entire flow to the
> — 07:41 [^jJQoVkd5yLg]

> individual contexts, we can make sure that that that goal is copied in like a
> — 1:16:09 [^kiClTcJUnhc]

Source analysis [^oVsEddfhdxc]; no independently matched timestamped quote published.

> three but things like what is the cloud provider what is the service where is it
> — 11:41 [^prttz9_1XDc]

Source analysis [^qJtcEDc_WJU]; no independently matched timestamped quote published.

Source analysis [^s67bE2Ur3bY]; no independently matched timestamped quote published.

> and it will turn your transcription into or your your previous context window
> — 19:22 [^shRR1e2HXMk]

Source analysis [^spxoDAfh5ig]; no independently matched timestamped quote published.

Source analysis [^uIiA6DquRiE]; no independently matched timestamped quote published.

> looks back at the last 10 messages and only sends those back. And you can set
> — 04:10 [^uiP88SpCi1Q]

Source analysis [^vW8wLsb3Nnc]; no independently matched timestamped quote published.

Source analysis [^wVl6ZjELpBk]; no independently matched timestamped quote published.

> about 50 keys per violation, so we're just going to filter it down to four and
> — 10:28 [^xIt_mTQp6mY]

> it will state the current intent of an AI agent. And the relevant information
> — 32:41 [^xs-ob87TTzg]

Source analysis [^zwItokY087U]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-QFHIoCo-Ko]: [Full Walkthrough: Workflow for AI Coding — Matt Pocock](https://www.youtube.com/watch?v=-QFHIoCo-Ko); publication: 2026-04-24T15:15:38Z; analysis: `analysis/-QFHIoCo-Ko.json`.
[^8kMaTybvDUw]: [12-Factor Agents: Patterns of reliable LLM applications — Dex Horthy, HumanLayer](https://www.youtube.com/watch?v=8kMaTybvDUw); publication: 2025-07-03T20:50:54Z; analysis: `analysis/8kMaTybvDUw.json`.
[^ACPEpji5NV4]: [Distill the LLM, Don't Serve It: Search & Personalization at DoorDash — Raghav Saboo, DoorDash](https://www.youtube.com/watch?v=ACPEpji5NV4); publication: 2026-09-25T13:30:37Z; analysis: `analysis/ACPEpji5NV4.json`.
[^CvRngaQZQ3Y]: [Improving Agents is a Data Mining Problem — Vivek Trivedy, LangChain](https://www.youtube.com/watch?v=CvRngaQZQ3Y); publication: 2026-08-12T19:00:01Z; analysis: `analysis/CvRngaQZQ3Y.json`.
[^IN-rb-9WmiY]: [Pinecone 2.0 — Edo Liberty, Pinecone](https://www.youtube.com/watch?v=IN-rb-9WmiY); publication: 2026-09-16T13:00:06Z; analysis: `analysis/IN-rb-9WmiY.json`.
[^JnubYCYunk8]: [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI](https://www.youtube.com/watch?v=JnubYCYunk8); publication: 2026-06-28T15:30:40Z; analysis: `analysis/JnubYCYunk8.json`.
[^KcVkq5L-0f0]: [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=KcVkq5L-0f0); publication: 2026-09-09T14:30:12Z; analysis: `analysis/KcVkq5L-0f0.json`.
[^KtBivPzmOM8]: [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](https://www.youtube.com/watch?v=KtBivPzmOM8); publication: 2026-10-17T07:00:25Z; analysis: `analysis/KtBivPzmOM8.json`.
[^LrGCT7G_rU8]: [Using RL Agent to Detect and Remediate ETL Pipeline Failures - Anna Marie Benzon](https://www.youtube.com/watch?v=LrGCT7G_rU8); publication: 2026-06-29T00:30:05Z; analysis: `analysis/LrGCT7G_rU8.json`.
[^N4vCBM5YbN0]: [Building Code First AI Agents with Azure AI Agent Service — Cedric Vidal, Microsoft](https://www.youtube.com/watch?v=N4vCBM5YbN0); publication: 2025-06-27T10:03:21Z; analysis: `analysis/N4vCBM5YbN0.json`.
[^Nqb7JTx0Pqo]: [MCP Agent Fine tuning Workshop - Ronan McGovern](https://www.youtube.com/watch?v=Nqb7JTx0Pqo); publication: 2025-06-03T22:22:28Z; analysis: `analysis/Nqb7JTx0Pqo.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^RjfbvDXpFls]: [Building pi in a World of Slop — Mario Zechner](https://www.youtube.com/watch?v=RjfbvDXpFls); publication: 2026-04-16T22:58:06Z; analysis: `analysis/RjfbvDXpFls.json`.
[^SQMCtZX3trg]: [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](https://www.youtube.com/watch?v=SQMCtZX3trg); publication: 2026-09-21T19:00:10Z; analysis: `analysis/SQMCtZX3trg.json`.
[^UPwGaM2MKHY]: [The Log Is The Agent - Ishaan Sehgal, Omnara](https://www.youtube.com/watch?v=UPwGaM2MKHY); publication: 2026-06-25T21:15:06Z; analysis: `analysis/UPwGaM2MKHY.json`.
[^Uv0nAf_7tyU]: [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU); publication: 2026-10-12T05:44:00Z; analysis: `analysis/Uv0nAf_7tyU.json`.
[^XsvUhpnHepE]: [The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs](https://www.youtube.com/watch?v=XsvUhpnHepE); publication: 2026-08-26T07:00:06Z; analysis: `analysis/XsvUhpnHepE.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^Z-c11pV_uvU]: [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Z-c11pV_uvU); publication: 2026-08-08T16:00:06Z; analysis: `analysis/Z-c11pV_uvU.json`.
[^ZB7l4uxW3Yo]: [Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson](https://www.youtube.com/watch?v=ZB7l4uxW3Yo); publication: 2025-06-03T22:31:07Z; analysis: `analysis/ZB7l4uxW3Yo.json`.
[^ZRM_TfEZcIo]: [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo); publication: 2026-06-26T14:00:07Z; analysis: `analysis/ZRM_TfEZcIo.json`.
[^aqW68Is_Kj4]: [Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic](https://www.youtube.com/watch?v=aqW68Is_Kj4); publication: 2025-12-04T20:14:55Z; analysis: `analysis/aqW68Is_Kj4.json`.
[^bjNYEc908oQ]: [Building Reliable Agentic Systems: Eno Reyes](https://www.youtube.com/watch?v=bjNYEc908oQ); publication: 2024-08-20T13:44:51Z; analysis: `analysis/bjNYEc908oQ.json`.
[^bmWZk9vTze0]: [MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0); publication: 2025-07-18T18:52:25Z; analysis: `analysis/bmWZk9vTze0.json`.
[^cKhpeEBnT1o]: [Your Coding Agent Is 6 Months Out of Date — Jakub Hojsan, Exa](https://www.youtube.com/watch?v=cKhpeEBnT1o); publication: 2026-10-02T15:30:31Z; analysis: `analysis/cKhpeEBnT1o.json`.
[^cZ5ZJy19KMo]: [Mission-Critical Evals at Scale (Learnings from 100k medical decisions)](https://www.youtube.com/watch?v=cZ5ZJy19KMo); publication: 2025-02-22T19:00:06Z; analysis: `analysis/cZ5ZJy19KMo.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
[^eIoohUmYpGI]: [The Infinite Software Crisis – Jake Nations, Netflix](https://www.youtube.com/watch?v=eIoohUmYpGI); publication: 2025-12-20T17:00:06Z; analysis: `analysis/eIoohUmYpGI.json`.
[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
[^fnLBmfsI_Fg]: [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](https://www.youtube.com/watch?v=fnLBmfsI_Fg); publication: 2026-07-20T06:25:15Z; analysis: `analysis/fnLBmfsI_Fg.json`.
[^g03m-WFEu1U]: [How to Improve your Vibe Coding — Ian Butler](https://www.youtube.com/watch?v=g03m-WFEu1U); publication: 2025-08-03T04:32:57Z; analysis: `analysis/g03m-WFEu1U.json`.
[^iRcX54EO5g8]: [Your agent is blindfolded — Johan Lajili, Poolside AI](https://www.youtube.com/watch?v=iRcX54EO5g8); publication: 2026-07-08T13:45:06Z; analysis: `analysis/iRcX54EO5g8.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^jJQoVkd5yLg]: [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](https://www.youtube.com/watch?v=jJQoVkd5yLg); publication: 2026-10-08T17:00:23Z; analysis: `analysis/jJQoVkd5yLg.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^oVsEddfhdxc]: [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](https://www.youtube.com/watch?v=oVsEddfhdxc); publication: 2026-09-26T17:30:10Z; analysis: `analysis/oVsEddfhdxc.json`.
[^prttz9_1XDc]: [Enhancing Quality and Security in CI: Gunjan Patel](https://www.youtube.com/watch?v=prttz9_1XDc); publication: 2024-11-27T19:56:40Z; analysis: `analysis/prttz9_1XDc.json`.
[^qJtcEDc_WJU]: [Scheduled Agents, Dreaming and Q&A: Claude Managed Agents (Part 3 of 4) — Anthropic](https://www.youtube.com/watch?v=qJtcEDc_WJU); publication: 2026-10-12T06:07:42Z; analysis: `analysis/qJtcEDc_WJU.json`.
[^s67bE2Ur3bY]: [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](https://www.youtube.com/watch?v=s67bE2Ur3bY); publication: 2026-07-29T22:58:19Z; analysis: `analysis/s67bE2Ur3bY.json`.
[^shRR1e2HXMk]: [How Codex Works — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk); publication: 2026-08-10T16:00:06Z; analysis: `analysis/shRR1e2HXMk.json`.
[^spxoDAfh5ig]: [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](https://www.youtube.com/watch?v=spxoDAfh5ig); publication: 2026-10-11T10:00:18Z; analysis: `analysis/spxoDAfh5ig.json`.
[^uIiA6DquRiE]: [Special Topics in Kernels, RL, Reward Hacking in Agents — Daniel Han, Unsloth](https://www.youtube.com/watch?v=uIiA6DquRiE); publication: 2026-07-17T17:00:06Z; analysis: `analysis/uIiA6DquRiE.json`.
[^uiP88SpCi1Q]: [Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS](https://www.youtube.com/watch?v=uiP88SpCi1Q); publication: 2026-06-28T22:00:14Z; analysis: `analysis/uiP88SpCi1Q.json`.
[^vW8wLsb3Nnc]: [POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent](https://www.youtube.com/watch?v=vW8wLsb3Nnc); publication: 2025-07-23T15:50:56Z; analysis: `analysis/vW8wLsb3Nnc.json`.
[^wVl6ZjELpBk]: [Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI](https://www.youtube.com/watch?v=wVl6ZjELpBk); publication: 2025-12-05T17:00:06Z; analysis: `analysis/wVl6ZjELpBk.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
[^xs-ob87TTzg]: [Total Recall: Agent Memory and Harness Engineering — Ignacio Martinez, Oracle](https://www.youtube.com/watch?v=xs-ob87TTzg); publication: 2026-09-18T16:00:11Z; analysis: `analysis/xs-ob87TTzg.json`.
[^zwItokY087U]: [10x Development: LLMs For the working Programmer - Manuel Odendahl](https://www.youtube.com/watch?v=zwItokY087U); publication: 2024-08-21T16:36:00Z; analysis: `analysis/zwItokY087U.json`.
