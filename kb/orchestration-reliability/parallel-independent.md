---
{
  "type": "technique",
  "id": "parallel-independent",
  "title": "Parallelize only independent work and account for duplicated context",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-20T09:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "6NIr_cYPglk",
      "resource": "https://www.youtube.com/watch?v=6NIr_cYPglk",
      "title": "To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball",
      "author": "Forrest Brazeal, Matt Ball",
      "last_modified": "2025-06-27T10:46:59Z",
      "analysis_file": "analysis/6NIr_cYPglk.json"
    },
    {
      "id": "8KkibGU_DDY",
      "resource": "https://www.youtube.com/watch?v=8KkibGU_DDY",
      "title": "Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori",
      "author": "Maximillian Piras, Yutori",
      "last_modified": "2026-09-10T15:00:39Z",
      "analysis_file": "analysis/8KkibGU_DDY.json"
    },
    {
      "id": "9WiBJRO84yY",
      "resource": "https://www.youtube.com/watch?v=9WiBJRO84yY",
      "title": "Building on the Codex Harness — Dominik Kundel, OpenAI",
      "author": "Dominik Kundel, OpenAI",
      "last_modified": "2026-10-09T15:30:04Z",
      "analysis_file": "analysis/9WiBJRO84yY.json"
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
      "id": "9mzfioh1Zag",
      "resource": "https://www.youtube.com/watch?v=9mzfioh1Zag",
      "title": "Grounded Reasoning Systems for Cloud Architecture - Iman Makaremi",
      "author": "Iman Makaremi",
      "last_modified": "2025-06-03T22:23:31Z",
      "analysis_file": "analysis/9mzfioh1Zag.json"
    },
    {
      "id": "Bz1HFxQA1o8",
      "resource": "https://www.youtube.com/watch?v=Bz1HFxQA1o8",
      "title": "Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco",
      "author": "Al Chen, Cisco",
      "last_modified": "2026-10-20T09:00:06Z",
      "analysis_file": "analysis/Bz1HFxQA1o8.json"
    },
    {
      "id": "ClWD8OEYgp8",
      "resource": "https://www.youtube.com/watch?v=ClWD8OEYgp8",
      "title": "Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub",
      "author": "Maggie Appleton, GitHub",
      "last_modified": "2026-04-26T15:00:06Z",
      "analysis_file": "analysis/ClWD8OEYgp8.json"
    },
    {
      "id": "I8fs4omN1no",
      "resource": "https://www.youtube.com/watch?v=I8fs4omN1no",
      "title": "Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline",
      "author": "Nik Pash, Cline",
      "last_modified": "2025-12-12T15:00:06Z",
      "analysis_file": "analysis/I8fs4omN1no.json"
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
      "id": "Lue8K2jqfKk",
      "resource": "https://www.youtube.com/watch?v=Lue8K2jqfKk",
      "title": "Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic",
      "author": "Boris Cherny, Anthropic",
      "last_modified": "2025-07-04T16:00:06Z",
      "analysis_file": "analysis/Lue8K2jqfKk.json"
    },
    {
      "id": "MGzymaYBiss",
      "resource": "https://www.youtube.com/watch?v=MGzymaYBiss",
      "title": "Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I",
      "author": "Dan Shipper, Every, AI & I",
      "last_modified": "2025-12-18T18:00:06Z",
      "analysis_file": "analysis/MGzymaYBiss.json"
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
      "id": "Q5IVm_CxN2w",
      "resource": "https://www.youtube.com/watch?v=Q5IVm_CxN2w",
      "title": "Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway",
      "author": "Mahmoud Abdelwahab, Railway",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/Q5IVm_CxN2w.json"
    },
    {
      "id": "QuuIywMG4s8",
      "resource": "https://www.youtube.com/watch?v=QuuIywMG4s8",
      "title": "Evals Are Broken, Use Them Anyway — Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-06-06T16:00:00Z",
      "analysis_file": "analysis/QuuIywMG4s8.json"
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
      "id": "T7NWjoD_OuY",
      "resource": "https://www.youtube.com/watch?v=T7NWjoD_OuY",
      "title": "The Making of Devin by Cognition AI: Scott Wu",
      "author": null,
      "last_modified": "2024-07-11T17:12:07Z",
      "analysis_file": "analysis/T7NWjoD_OuY.json"
    },
    {
      "id": "TqC1qOfiVcQ",
      "resource": "https://www.youtube.com/watch?v=TqC1qOfiVcQ",
      "title": "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-01-05T17:00:06Z",
      "analysis_file": "analysis/TqC1qOfiVcQ.json"
    },
    {
      "id": "UGjk3Uk0MxM",
      "resource": "https://www.youtube.com/watch?v=UGjk3Uk0MxM",
      "title": "The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft",
      "author": "Pamela Fox, Microsoft",
      "last_modified": "2026-10-19T14:06:53Z",
      "analysis_file": "analysis/UGjk3Uk0MxM.json"
    },
    {
      "id": "X4BwOu0GWb8",
      "resource": "https://www.youtube.com/watch?v=X4BwOu0GWb8",
      "title": "Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules",
      "author": "Rustin Banks, Google Jules",
      "last_modified": "2025-07-25T23:06:43Z",
      "analysis_file": "analysis/X4BwOu0GWb8.json"
    },
    {
      "id": "XAsb7MIAzm8",
      "resource": "https://www.youtube.com/watch?v=XAsb7MIAzm8",
      "title": "Don’t be data poor — Anuj Iravane, Anterior",
      "author": "Anuj Iravane, Anterior",
      "last_modified": "2026-08-19T18:00:17Z",
      "analysis_file": "analysis/XAsb7MIAzm8.json"
    },
    {
      "id": "YYcNm2RexnY",
      "resource": "https://www.youtube.com/watch?v=YYcNm2RexnY",
      "title": "Lessons from building GenAI based applications — Juan Peredo",
      "author": "Juan Peredo",
      "last_modified": "2025-02-22T15:00:06Z",
      "analysis_file": "analysis/YYcNm2RexnY.json"
    },
    {
      "id": "_4Ph2dhmUFI",
      "resource": "https://www.youtube.com/watch?v=_4Ph2dhmUFI",
      "title": "How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase",
      "author": "Evan Kormos, Coinbase",
      "last_modified": "2026-10-19T23:00:08Z",
      "analysis_file": "analysis/_4Ph2dhmUFI.json"
    },
    {
      "id": "coKKKKh8Vns",
      "resource": "https://www.youtube.com/watch?v=coKKKKh8Vns",
      "title": "How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe",
      "author": "Muktesh Mishra, Adobe",
      "last_modified": "2025-07-22T19:46:22Z",
      "analysis_file": "analysis/coKKKKh8Vns.json"
    },
    {
      "id": "eJOjdjO45Sc",
      "resource": "https://www.youtube.com/watch?v=eJOjdjO45Sc",
      "title": "How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind",
      "author": "Mukund Sridhar & Aarush Selvan, Google DeepMind",
      "last_modified": "2025-03-26T19:41:41Z",
      "analysis_file": "analysis/eJOjdjO45Sc.json"
    },
    {
      "id": "flf_IKnFYnE",
      "resource": "https://www.youtube.com/watch?v=flf_IKnFYnE",
      "title": "From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/flf_IKnFYnE.json"
    },
    {
      "id": "kmV-qg4uoNI",
      "resource": "https://www.youtube.com/watch?v=kmV-qg4uoNI",
      "title": "Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel",
      "author": "Peter Wielander, Vercel",
      "last_modified": "2026-01-06T16:00:07Z",
      "analysis_file": "analysis/kmV-qg4uoNI.json"
    },
    {
      "id": "mMNkdYnIVC4",
      "resource": "https://www.youtube.com/watch?v=mMNkdYnIVC4",
      "title": "Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI",
      "author": "James Zou, Together AI",
      "last_modified": "2026-08-25T20:46:01Z",
      "analysis_file": "analysis/mMNkdYnIVC4.json"
    },
    {
      "id": "pmoDeA3RBZY",
      "resource": "https://www.youtube.com/watch?v=pmoDeA3RBZY",
      "title": "Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-06-05T16:00:06Z",
      "analysis_file": "analysis/pmoDeA3RBZY.json"
    },
    {
      "id": "qeDPKbWjsuk",
      "resource": "https://www.youtube.com/watch?v=qeDPKbWjsuk",
      "title": "Keynote: The AI developer experience doesn't have to suck – why and how we built Modal",
      "author": "why and how we built Modal",
      "last_modified": "2025-02-22T14:00:06Z",
      "analysis_file": "analysis/qeDPKbWjsuk.json"
    },
    {
      "id": "so9l_MwS2yg",
      "resource": "https://www.youtube.com/watch?v=so9l_MwS2yg",
      "title": "Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS",
      "author": "Zack Proser, WorkOS",
      "last_modified": "2026-06-11T14:00:06Z",
      "analysis_file": "analysis/so9l_MwS2yg.json"
    },
    {
      "id": "uFPAtKIN-FQ",
      "resource": "https://www.youtube.com/watch?v=uFPAtKIN-FQ",
      "title": "Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri",
      "author": null,
      "last_modified": "2025-06-11T16:57:37Z",
      "analysis_file": "analysis/uFPAtKIN-FQ.json"
    },
    {
      "id": "vGCJ7diEtrw",
      "resource": "https://www.youtube.com/watch?v=vGCJ7diEtrw",
      "title": "What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory",
      "author": "Tereza Tížková, Factory",
      "last_modified": "2026-09-27T15:00:02Z",
      "analysis_file": "analysis/vGCJ7diEtrw.json"
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
      "id": "whue9_YquGA",
      "resource": "https://www.youtube.com/watch?v=whue9_YquGA",
      "title": "Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation",
      "author": "Angie Jones, Agentic AI Foundation",
      "last_modified": "2026-06-28T19:00:10Z",
      "analysis_file": "analysis/whue9_YquGA.json"
    },
    {
      "id": "y2W4FNAuPEA",
      "resource": "https://www.youtube.com/watch?v=y2W4FNAuPEA",
      "title": "Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher",
      "author": "Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher",
      "last_modified": "2026-09-08T15:00:06Z",
      "analysis_file": "analysis/y2W4FNAuPEA.json"
    },
    {
      "id": "z0sh8HyTrDo",
      "resource": "https://www.youtube.com/watch?v=z0sh8HyTrDo",
      "title": "Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI",
      "author": "Ramana Siddanth Emani, Auditoria AI",
      "last_modified": "2026-07-30T03:00:06Z",
      "analysis_file": "analysis/z0sh8HyTrDo.json"
    },
    {
      "id": "zeAyuLc_f3Q",
      "resource": "https://www.youtube.com/watch?v=zeAyuLc_f3Q",
      "title": "The Future of Knowledge Assistants: Jerry Liu",
      "author": null,
      "last_modified": "2024-07-13T17:58:56Z",
      "analysis_file": "analysis/zeAyuLc_f3Q.json"
    },
    {
      "id": "zgNvts_2TUE",
      "resource": "https://www.youtube.com/watch?v=zgNvts_2TUE",
      "title": "State of the Claw — Peter Steinberger",
      "author": "Peter Steinberger",
      "last_modified": "2026-04-17T15:30:06Z",
      "analysis_file": "analysis/zgNvts_2TUE.json"
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

# Parallelize only independent work and account for duplicated context

## What

Parallelize only independent work and account for duplicated context

Independent tasks can progress concurrently instead of serially consuming one developer’s attention.

## Evidence

Source analysis [^6NIr_cYPglk]; no independently matched timestamped quote published.

Source analysis [^8KkibGU_DDY]; no independently matched timestamped quote published.

Source analysis [^9WiBJRO84yY]; no independently matched timestamped quote published.

Source analysis [^9arM9b7JgOo]; no independently matched timestamped quote published.

Source analysis [^9mzfioh1Zag]; no independently matched timestamped quote published.

Source analysis [^Bz1HFxQA1o8]; no independently matched timestamped quote published.

Source analysis [^ClWD8OEYgp8]; no independently matched timestamped quote published.

Source analysis [^I8fs4omN1no]; no independently matched timestamped quote published.

> which kind of serves the purpose of keeping the context clean, as well as
> — 23:37 [^LC3-P7v3yoI]

Source analysis [^Lue8K2jqfKk]; no independently matched timestamped quote published.

> uh the reason we can go much faster is we can work on multiple multiple
> — 06:10 [^MGzymaYBiss]

> running probably shares say 80% of the context across the board. So of course
> — 21:14 [^MLhAA9yguwM]

Source analysis [^Q5IVm_CxN2w]; no independently matched timestamped quote published.

> defined in infrastructure where each of these 89 tasks have like the proper
> — 12:13 [^QuuIywMG4s8]

> comments. This one does not work for me, but uh running commands in parallel
> — 32:46 [^RFKCzGlAU6Q]

Source analysis [^T7NWjoD_OuY]; no independently matched timestamped quote published.

Source analysis [^TqC1qOfiVcQ]; no independently matched timestamped quote published.

Source analysis [^UGjk3Uk0MxM]; no independently matched timestamped quote published.

> So, first we're going to add some tests. And then I'm going to actually I'm going
> — 06:41 [^X4BwOu0GWb8]

> just I have 10 different things on my backlog. Let's do them all at once and
> — 04:00 [^X4BwOu0GWb8]

Source analysis [^XAsb7MIAzm8]; no independently matched timestamped quote published.

Source analysis [^YYcNm2RexnY]; no independently matched timestamped quote published.

Source analysis [^_4Ph2dhmUFI]; no independently matched timestamped quote published.

Source analysis [^coKKKKh8Vns]; no independently matched timestamped quote published.

Source analysis [^eJOjdjO45Sc]; no independently matched timestamped quote published.

Source analysis [^flf_IKnFYnE]; no independently matched timestamped quote published.

> right um right right now we expose it in observability um if you have access but
> — 1:09:11 [^kmV-qg4uoNI]

Source analysis [^mMNkdYnIVC4]; no independently matched timestamped quote published.

> Let's just say CI to one side, you might have features on one side, you might
> — 09:59 [^pmoDeA3RBZY]

Source analysis [^qeDPKbWjsuk]; no independently matched timestamped quote published.

Source analysis [^so9l_MwS2yg]; no independently matched timestamped quote published.

Source analysis [^uFPAtKIN-FQ]; no independently matched timestamped quote published.

> they work in a sequence. So they don't work in a swarm or parallel. The agents
> — 12:54 [^vGCJ7diEtrw]

Source analysis [^wXVvfFMTyzY]; no independently matched timestamped quote published.

> explore different parts of the system in parallel, each building their own
> — 15:52 [^whue9_YquGA]

Source analysis [^y2W4FNAuPEA]; no independently matched timestamped quote published.

Source analysis [^z0sh8HyTrDo]; no independently matched timestamped quote published.

Source analysis [^zeAyuLc_f3Q]; no independently matched timestamped quote published.

Source analysis [^zgNvts_2TUE]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^6NIr_cYPglk]: [To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball](https://www.youtube.com/watch?v=6NIr_cYPglk); publication: 2025-06-27T10:46:59Z; analysis: `analysis/6NIr_cYPglk.json`.
[^8KkibGU_DDY]: [Mousepower: agents that can’t be measured, can’t be managed. — Maximillian Piras, Yutori](https://www.youtube.com/watch?v=8KkibGU_DDY); publication: 2026-09-10T15:00:39Z; analysis: `analysis/8KkibGU_DDY.json`.
[^9WiBJRO84yY]: [Building on the Codex Harness — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=9WiBJRO84yY); publication: 2026-10-09T15:30:04Z; analysis: `analysis/9WiBJRO84yY.json`.
[^9arM9b7JgOo]: [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo); publication: 2026-07-11T14:45:18Z; analysis: `analysis/9arM9b7JgOo.json`.
[^9mzfioh1Zag]: [Grounded Reasoning Systems for Cloud Architecture - Iman Makaremi](https://www.youtube.com/watch?v=9mzfioh1Zag); publication: 2025-06-03T22:23:31Z; analysis: `analysis/9mzfioh1Zag.json`.
[^Bz1HFxQA1o8]: [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](https://www.youtube.com/watch?v=Bz1HFxQA1o8); publication: 2026-10-20T09:00:06Z; analysis: `analysis/Bz1HFxQA1o8.json`.
[^ClWD8OEYgp8]: [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](https://www.youtube.com/watch?v=ClWD8OEYgp8); publication: 2026-04-26T15:00:06Z; analysis: `analysis/ClWD8OEYgp8.json`.
[^I8fs4omN1no]: [Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline](https://www.youtube.com/watch?v=I8fs4omN1no); publication: 2025-12-12T15:00:06Z; analysis: `analysis/I8fs4omN1no.json`.
[^LC3-P7v3yoI]: [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](https://www.youtube.com/watch?v=LC3-P7v3yoI); publication: 2026-07-20T06:24:53Z; analysis: `analysis/LC3-P7v3yoI.json`.
[^Lue8K2jqfKk]: [Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic](https://www.youtube.com/watch?v=Lue8K2jqfKk); publication: 2025-07-04T16:00:06Z; analysis: `analysis/Lue8K2jqfKk.json`.
[^MGzymaYBiss]: [Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I](https://www.youtube.com/watch?v=MGzymaYBiss); publication: 2025-12-18T18:00:06Z; analysis: `analysis/MGzymaYBiss.json`.
[^MLhAA9yguwM]: [The 3 Pillars of Autonomy – Michele Catasta, Replit](https://www.youtube.com/watch?v=MLhAA9yguwM); publication: 2025-12-22T16:30:06Z; analysis: `analysis/MLhAA9yguwM.json`.
[^Q5IVm_CxN2w]: [Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=Q5IVm_CxN2w); publication: 2025-11-24T20:16:36Z; analysis: `analysis/Q5IVm_CxN2w.json`.
[^QuuIywMG4s8]: [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8); publication: 2026-06-06T16:00:00Z; analysis: `analysis/QuuIywMG4s8.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^T7NWjoD_OuY]: [The Making of Devin by Cognition AI: Scott Wu](https://www.youtube.com/watch?v=T7NWjoD_OuY); publication: 2024-07-11T17:12:07Z; analysis: `analysis/T7NWjoD_OuY.json`.
[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
[^UGjk3Uk0MxM]: [The Model Swap Workshop: GPT-5.5 vs Kimi vs DeepSeek vs Mistral — Pamela Fox, Microsoft](https://www.youtube.com/watch?v=UGjk3Uk0MxM); publication: 2026-10-19T14:06:53Z; analysis: `analysis/UGjk3Uk0MxM.json`.
[^X4BwOu0GWb8]: [Your Coding Agent Just Got Cloned And Your Brain Isn't Ready - Rustin Banks, Google Jules](https://www.youtube.com/watch?v=X4BwOu0GWb8); publication: 2025-07-25T23:06:43Z; analysis: `analysis/X4BwOu0GWb8.json`.
[^XAsb7MIAzm8]: [Don’t be data poor — Anuj Iravane, Anterior](https://www.youtube.com/watch?v=XAsb7MIAzm8); publication: 2026-08-19T18:00:17Z; analysis: `analysis/XAsb7MIAzm8.json`.
[^YYcNm2RexnY]: [Lessons from building GenAI based applications — Juan Peredo](https://www.youtube.com/watch?v=YYcNm2RexnY); publication: 2025-02-22T15:00:06Z; analysis: `analysis/YYcNm2RexnY.json`.
[^_4Ph2dhmUFI]: [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](https://www.youtube.com/watch?v=_4Ph2dhmUFI); publication: 2026-10-19T23:00:08Z; analysis: `analysis/_4Ph2dhmUFI.json`.
[^coKKKKh8Vns]: [How to run Evals at Scale: Thinking beyond Accuracy or Similarity — Muktesh Mishra, Adobe](https://www.youtube.com/watch?v=coKKKKh8Vns); publication: 2025-07-22T19:46:22Z; analysis: `analysis/coKKKKh8Vns.json`.
[^eJOjdjO45Sc]: [How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind](https://www.youtube.com/watch?v=eJOjdjO45Sc); publication: 2025-03-26T19:41:41Z; analysis: `analysis/eJOjdjO45Sc.json`.
[^flf_IKnFYnE]: [From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/flf_IKnFYnE.json`.
[^kmV-qg4uoNI]: [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](https://www.youtube.com/watch?v=kmV-qg4uoNI); publication: 2026-01-06T16:00:07Z; analysis: `analysis/kmV-qg4uoNI.json`.
[^mMNkdYnIVC4]: [Einstein Arena: Harnessing Collective Agent Intelligence for Open Science — James Zou, Together AI](https://www.youtube.com/watch?v=mMNkdYnIVC4); publication: 2026-08-25T20:46:01Z; analysis: `analysis/mMNkdYnIVC4.json`.
[^pmoDeA3RBZY]: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY); publication: 2026-06-05T16:00:06Z; analysis: `analysis/pmoDeA3RBZY.json`.
[^qeDPKbWjsuk]: [Keynote: The AI developer experience doesn't have to suck – why and how we built Modal](https://www.youtube.com/watch?v=qeDPKbWjsuk); publication: 2025-02-22T14:00:06Z; analysis: `analysis/qeDPKbWjsuk.json`.
[^so9l_MwS2yg]: [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](https://www.youtube.com/watch?v=so9l_MwS2yg); publication: 2026-06-11T14:00:06Z; analysis: `analysis/so9l_MwS2yg.json`.
[^uFPAtKIN-FQ]: [Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri](https://www.youtube.com/watch?v=uFPAtKIN-FQ); publication: 2025-06-11T16:57:37Z; analysis: `analysis/uFPAtKIN-FQ.json`.
[^vGCJ7diEtrw]: [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw); publication: 2026-09-27T15:00:02Z; analysis: `analysis/vGCJ7diEtrw.json`.
[^wXVvfFMTyzY]: [A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench](https://www.youtube.com/watch?v=wXVvfFMTyzY); publication: 2025-07-26T14:15:05Z; analysis: `analysis/wXVvfFMTyzY.json`.
[^whue9_YquGA]: [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=whue9_YquGA); publication: 2026-06-28T19:00:10Z; analysis: `analysis/whue9_YquGA.json`.
[^y2W4FNAuPEA]: [Deep dive on LLM Inference at Scale — Harshul Jain, Audible & Tanmay Sah, Independent AI Researcher](https://www.youtube.com/watch?v=y2W4FNAuPEA); publication: 2026-09-08T15:00:06Z; analysis: `analysis/y2W4FNAuPEA.json`.
[^z0sh8HyTrDo]: [Your Finance Agent's Bottleneck Is You — Ramana Siddanth Emani, Auditoria AI](https://www.youtube.com/watch?v=z0sh8HyTrDo); publication: 2026-07-30T03:00:06Z; analysis: `analysis/z0sh8HyTrDo.json`.
[^zeAyuLc_f3Q]: [The Future of Knowledge Assistants: Jerry Liu](https://www.youtube.com/watch?v=zeAyuLc_f3Q); publication: 2024-07-13T17:58:56Z; analysis: `analysis/zeAyuLc_f3Q.json`.
[^zgNvts_2TUE]: [State of the Claw — Peter Steinberger](https://www.youtube.com/watch?v=zgNvts_2TUE); publication: 2026-04-17T15:30:06Z; analysis: `analysis/zgNvts_2TUE.json`.
