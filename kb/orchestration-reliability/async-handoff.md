---
{
  "type": "technique",
  "id": "async-handoff",
  "title": "Use structured asynchronous handoffs with explicit completion and ownership",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-12T05:44:00Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "B0fjR3yaZFU",
      "resource": "https://www.youtube.com/watch?v=B0fjR3yaZFU",
      "title": "How do you diffuse AI into the real world? — Varun Shenoy, Long Lake",
      "author": "Varun Shenoy, Long Lake",
      "last_modified": "2026-08-28T17:30:33Z",
      "analysis_file": "analysis/B0fjR3yaZFU.json"
    },
    {
      "id": "HN-F-OQe6j0",
      "resource": "https://www.youtube.com/watch?v=HN-F-OQe6j0",
      "title": "Defying Gravity - Kevin Hou, Google DeepMind",
      "author": "Kevin Hou, Google DeepMind",
      "last_modified": "2025-12-02T22:51:09Z",
      "analysis_file": "analysis/HN-F-OQe6j0.json"
    },
    {
      "id": "HOYLZ7IVgJo",
      "resource": "https://www.youtube.com/watch?v=HOYLZ7IVgJo",
      "title": "Shipping an Enterprise Voice AI Agent in 100 Days - Peter Bar, Intercom Fin",
      "author": "Peter Bar, Intercom Fin",
      "last_modified": "2025-07-18T16:00:06Z",
      "analysis_file": "analysis/HOYLZ7IVgJo.json"
    },
    {
      "id": "JVuNPL5QO8Q",
      "resource": "https://www.youtube.com/watch?v=JVuNPL5QO8Q",
      "title": "Windsurf everywhere, doing everything, all at once - Kevin Hou, Windsurf",
      "author": "Kevin Hou, Windsurf",
      "last_modified": "2025-06-23T15:00:06Z",
      "analysis_file": "analysis/JVuNPL5QO8Q.json"
    },
    {
      "id": "OXMMN-XbxwA",
      "resource": "https://www.youtube.com/watch?v=OXMMN-XbxwA",
      "title": "Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc",
      "author": "Vaidas Razgaitis, Higharc",
      "last_modified": "2026-06-28T19:30:02Z",
      "analysis_file": "analysis/OXMMN-XbxwA.json"
    },
    {
      "id": "PwCSYy-oGsM",
      "resource": "https://www.youtube.com/watch?v=PwCSYy-oGsM",
      "title": "Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI",
      "author": "Druid AI",
      "last_modified": "2026-10-12T00:00:10Z",
      "analysis_file": "analysis/PwCSYy-oGsM.json"
    },
    {
      "id": "SbcQYbrvAfI",
      "resource": "https://www.youtube.com/watch?v=SbcQYbrvAfI",
      "title": "Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize",
      "author": "SallyAnn DeLucia & Fuad Ali, Arize",
      "last_modified": "2026-01-06T17:30:06Z",
      "analysis_file": "analysis/SbcQYbrvAfI.json"
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
      "id": "Wmp2Tku2PrI",
      "resource": "https://www.youtube.com/watch?v=Wmp2Tku2PrI",
      "title": "Vibe Engineering Effect Apps — Michael Arnaldi, Effectful",
      "author": "Michael Arnaldi, Effectful",
      "last_modified": "2026-05-07T15:00:06Z",
      "analysis_file": "analysis/Wmp2Tku2PrI.json"
    },
    {
      "id": "YgEv7IQzGdM",
      "resource": "https://www.youtube.com/watch?v=YgEv7IQzGdM",
      "title": "How to Kill the Code Review — Ankit Jain, Aviator",
      "author": "Ankit Jain, Aviator",
      "last_modified": "2026-08-17T20:00:08Z",
      "analysis_file": "analysis/YgEv7IQzGdM.json"
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
      "id": "bdHaOXZOhcM",
      "resource": "https://www.youtube.com/watch?v=bdHaOXZOhcM",
      "title": "Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company",
      "author": "Hursh Agrawal, The Browser Company",
      "last_modified": "2026-08-20T14:00:21Z",
      "analysis_file": "analysis/bdHaOXZOhcM.json"
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
      "id": "eXA2tjRZIbY",
      "resource": "https://www.youtube.com/watch?v=eXA2tjRZIbY",
      "title": "The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI",
      "author": "Varun Krovvidi, Resolve AI",
      "last_modified": "2026-10-06T23:30:36Z",
      "analysis_file": "analysis/eXA2tjRZIbY.json"
    },
    {
      "id": "jA_x7F8caHI",
      "resource": "https://www.youtube.com/watch?v=jA_x7F8caHI",
      "title": "No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle",
      "author": "Kay Malcolm, Oracle",
      "last_modified": "2026-09-14T16:30:33Z",
      "analysis_file": "analysis/jA_x7F8caHI.json"
    },
    {
      "id": "kTnfJszFxCg",
      "resource": "https://www.youtube.com/watch?v=kTnfJszFxCg",
      "title": "3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph",
      "author": "Harrison Chase, LangChain/LangGraph",
      "last_modified": "2025-07-23T15:51:25Z",
      "analysis_file": "analysis/kTnfJszFxCg.json"
    },
    {
      "id": "m0dxZ-NDKHo",
      "resource": "https://www.youtube.com/watch?v=m0dxZ-NDKHo",
      "title": "Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco",
      "author": "Ola Mabadeje, Cisco",
      "last_modified": "2025-08-22T06:14:21Z",
      "analysis_file": "analysis/m0dxZ-NDKHo.json"
    },
    {
      "id": "n9rjuBuShko",
      "resource": "https://www.youtube.com/watch?v=n9rjuBuShko",
      "title": "Building LinkedIn's GenAI Platform — Xiaofeng Wang",
      "author": "Xiaofeng Wang",
      "last_modified": "2025-04-16T16:00:06Z",
      "analysis_file": "analysis/n9rjuBuShko.json"
    },
    {
      "id": "ohKt066uFhg",
      "resource": "https://www.youtube.com/watch?v=ohKt066uFhg",
      "title": "Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski",
      "author": "Fryderyk Wiatrowski",
      "last_modified": "2026-05-11T15:00:06Z",
      "analysis_file": "analysis/ohKt066uFhg.json"
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
      "id": "rcsliSIy_YU",
      "resource": "https://www.youtube.com/watch?v=rcsliSIy_YU",
      "title": "Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-01-08T16:30:23Z",
      "analysis_file": "analysis/rcsliSIy_YU.json"
    },
    {
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
    },
    {
      "id": "vSx5IULvBns",
      "resource": "https://www.youtube.com/watch?v=vSx5IULvBns",
      "title": "Always-on agents run production without the on-call tax — Justin Smith, Resolve AI",
      "author": "Justin Smith, Resolve AI",
      "last_modified": "2026-08-09T14:45:06Z",
      "analysis_file": "analysis/vSx5IULvBns.json"
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

# Use structured asynchronous handoffs with explicit completion and ownership

## What

Use structured asynchronous handoffs with explicit completion and ownership

Record done, undone, commands, exit codes, issues, and procedure compliance rather than a narrative completion claim.

## Evidence

Source analysis [^B0fjR3yaZFU]; no independently matched timestamped quote published.

Source analysis [^HN-F-OQe6j0]; no independently matched timestamped quote published.

Source analysis [^HOYLZ7IVgJo]; no independently matched timestamped quote published.

Source analysis [^JVuNPL5QO8Q]; no independently matched timestamped quote published.

Source analysis [^OXMMN-XbxwA]; no independently matched timestamped quote published.

Source analysis [^PwCSYy-oGsM]; no independently matched timestamped quote published.

Source analysis [^SbcQYbrvAfI]; no independently matched timestamped quote published.

Source analysis [^Uv0nAf_7tyU]; no independently matched timestamped quote published.

> implement the small task and then exit and I run that in a loop.
> — 44:32 [^Wmp2Tku2PrI]

> When AI write the code and AI review the code, why are we doing it in a UI?
> — 02:23 [^YgEv7IQzGdM]

> domain where all of the agents and humans collaborate together.
> — 29:07 [^am_oeAoUhew]

> report in the morning on what you do. I need the full stack ready and a report
> — 10:27 [^bdHaOXZOhcM]

> this is that you can use a background agent to do a lot of this work because
> — 13:50 [^eIoohUmYpGI]

Source analysis [^eXA2tjRZIbY]; no independently matched timestamped quote published.

Source analysis [^jA_x7F8caHI]; no independently matched timestamped quote published.

> work but the human still in the loop at key points and first drafts I think are
> — 20:18 [^kTnfJszFxCg]

Source analysis [^m0dxZ-NDKHo]; no independently matched timestamped quote published.

Source analysis [^n9rjuBuShko]; no independently matched timestamped quote published.

Source analysis [^ohKt066uFhg]; no independently matched timestamped quote published.

> were the the exit codes of those commands.
> — 08:32 [^ow1we5PzK-o]

> file themselves. Uh maybe they send a pull request into the file as they learn
> — 33:21 [^rcsliSIy_YU]

Source analysis [^rnDm57Py54A]; no independently matched timestamped quote published.

> some notable changes, etc. Work work completed.
> — 20:17 [^vSx5IULvBns]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^B0fjR3yaZFU]: [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](https://www.youtube.com/watch?v=B0fjR3yaZFU); publication: 2026-08-28T17:30:33Z; analysis: `analysis/B0fjR3yaZFU.json`.
[^HN-F-OQe6j0]: [Defying Gravity - Kevin Hou, Google DeepMind](https://www.youtube.com/watch?v=HN-F-OQe6j0); publication: 2025-12-02T22:51:09Z; analysis: `analysis/HN-F-OQe6j0.json`.
[^HOYLZ7IVgJo]: [Shipping an Enterprise Voice AI Agent in 100 Days - Peter Bar, Intercom Fin](https://www.youtube.com/watch?v=HOYLZ7IVgJo); publication: 2025-07-18T16:00:06Z; analysis: `analysis/HOYLZ7IVgJo.json`.
[^JVuNPL5QO8Q]: [Windsurf everywhere, doing everything, all at once - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=JVuNPL5QO8Q); publication: 2025-06-23T15:00:06Z; analysis: `analysis/JVuNPL5QO8Q.json`.
[^OXMMN-XbxwA]: [Research to Reality: Bringing Frontier ML Research to Production - Vaidas Razgaitis, Higharc](https://www.youtube.com/watch?v=OXMMN-XbxwA); publication: 2026-06-28T19:30:02Z; analysis: `analysis/OXMMN-XbxwA.json`.
[^PwCSYy-oGsM]: [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](https://www.youtube.com/watch?v=PwCSYy-oGsM); publication: 2026-10-12T00:00:10Z; analysis: `analysis/PwCSYy-oGsM.json`.
[^SbcQYbrvAfI]: [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI); publication: 2026-01-06T17:30:06Z; analysis: `analysis/SbcQYbrvAfI.json`.
[^Uv0nAf_7tyU]: [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU); publication: 2026-10-12T05:44:00Z; analysis: `analysis/Uv0nAf_7tyU.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^YgEv7IQzGdM]: [How to Kill the Code Review — Ankit Jain, Aviator](https://www.youtube.com/watch?v=YgEv7IQzGdM); publication: 2026-08-17T20:00:08Z; analysis: `analysis/YgEv7IQzGdM.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^bdHaOXZOhcM]: [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM); publication: 2026-08-20T14:00:21Z; analysis: `analysis/bdHaOXZOhcM.json`.
[^eIoohUmYpGI]: [The Infinite Software Crisis – Jake Nations, Netflix](https://www.youtube.com/watch?v=eIoohUmYpGI); publication: 2025-12-20T17:00:06Z; analysis: `analysis/eIoohUmYpGI.json`.
[^eXA2tjRZIbY]: [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY); publication: 2026-10-06T23:30:36Z; analysis: `analysis/eXA2tjRZIbY.json`.
[^jA_x7F8caHI]: [No Memory, No Harness: Why the Database Is the Last Line of Defense — Kay Malcolm, Oracle](https://www.youtube.com/watch?v=jA_x7F8caHI); publication: 2026-09-14T16:30:33Z; analysis: `analysis/jA_x7F8caHI.json`.
[^kTnfJszFxCg]: [3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph](https://www.youtube.com/watch?v=kTnfJszFxCg); publication: 2025-07-23T15:51:25Z; analysis: `analysis/kTnfJszFxCg.json`.
[^m0dxZ-NDKHo]: [Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco](https://www.youtube.com/watch?v=m0dxZ-NDKHo); publication: 2025-08-22T06:14:21Z; analysis: `analysis/m0dxZ-NDKHo.json`.
[^n9rjuBuShko]: [Building LinkedIn's GenAI Platform — Xiaofeng Wang](https://www.youtube.com/watch?v=n9rjuBuShko); publication: 2025-04-16T16:00:06Z; analysis: `analysis/n9rjuBuShko.json`.
[^ohKt066uFhg]: [Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski](https://www.youtube.com/watch?v=ohKt066uFhg); publication: 2026-05-11T15:00:06Z; analysis: `analysis/ohKt066uFhg.json`.
[^ow1we5PzK-o]: [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](https://www.youtube.com/watch?v=ow1we5PzK-o); publication: 2026-05-06T15:00:06Z; analysis: `analysis/ow1we5PzK-o.json`.
[^rcsliSIy_YU]: [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU); publication: 2026-01-08T16:30:23Z; analysis: `analysis/rcsliSIy_YU.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
[^vSx5IULvBns]: [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](https://www.youtube.com/watch?v=vSx5IULvBns); publication: 2026-08-09T14:45:06Z; analysis: `analysis/vSx5IULvBns.json`.
