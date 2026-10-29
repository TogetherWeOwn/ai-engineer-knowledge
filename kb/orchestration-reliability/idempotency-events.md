---
{
  "type": "technique",
  "id": "idempotency-events",
  "title": "Deduplicate events and make side effects idempotent",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-21T08:00:37Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "FQwTqUmcbRg",
      "resource": "https://www.youtube.com/watch?v=FQwTqUmcbRg",
      "title": "Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI",
      "author": "Bogdan Gaza, DatologyAI",
      "last_modified": "2026-10-02T23:30:27Z",
      "analysis_file": "analysis/FQwTqUmcbRg.json"
    },
    {
      "id": "KHudyx5wW3U",
      "resource": "https://www.youtube.com/watch?v=KHudyx5wW3U",
      "title": "Agent Frameworks Considered Harmful — Rémi Louf, .txt",
      "author": "Rémi Louf, .txt",
      "last_modified": "2026-08-22T16:30:39Z",
      "analysis_file": "analysis/KHudyx5wW3U.json"
    },
    {
      "id": "NaOkR3VSfR4",
      "resource": "https://www.youtube.com/watch?v=NaOkR3VSfR4",
      "title": "Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya",
      "author": "Viren Baraiya",
      "last_modified": "2026-10-08T22:30:09Z",
      "analysis_file": "analysis/NaOkR3VSfR4.json"
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
      "id": "ZD9-4fW2HhM",
      "resource": "https://www.youtube.com/watch?v=ZD9-4fW2HhM",
      "title": "Build Systems, Not Code - Angie Jones, Agentic AI Foundation",
      "author": "Angie Jones, Agentic AI Foundation",
      "last_modified": "2026-06-25T18:00:06Z",
      "analysis_file": "analysis/ZD9-4fW2HhM.json"
    },
    {
      "id": "_-oIuRH4oGA",
      "resource": "https://www.youtube.com/watch?v=_-oIuRH4oGA",
      "title": "How agents broke app-level infrastructure - Evan Boyle",
      "author": "Evan Boyle",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/_-oIuRH4oGA.json"
    },
    {
      "id": "cf2IhzqeQH4",
      "resource": "https://www.youtube.com/watch?v=cf2IhzqeQH4",
      "title": "Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg",
      "author": "Dor Sasson, Stigg",
      "last_modified": "2026-10-07T00:30:28Z",
      "analysis_file": "analysis/cf2IhzqeQH4.json"
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
      "id": "hD9-V56FNRI",
      "resource": "https://www.youtube.com/watch?v=hD9-V56FNRI",
      "title": "AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok",
      "author": "Salman Munaf, TikTok",
      "last_modified": "2026-08-29T16:00:06Z",
      "analysis_file": "analysis/hD9-V56FNRI.json"
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
      "id": "kmV-qg4uoNI",
      "resource": "https://www.youtube.com/watch?v=kmV-qg4uoNI",
      "title": "Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel",
      "author": "Peter Wielander, Vercel",
      "last_modified": "2026-01-06T16:00:07Z",
      "analysis_file": "analysis/kmV-qg4uoNI.json"
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
      "id": "tZycGA_Fbfo",
      "resource": "https://www.youtube.com/watch?v=tZycGA_Fbfo",
      "title": "Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma",
      "author": "Harish Gaggar, Credit Karma",
      "last_modified": "2026-10-14T17:00:04Z",
      "analysis_file": "analysis/tZycGA_Fbfo.json"
    },
    {
      "id": "uA4ah-dVHvU",
      "resource": "https://www.youtube.com/watch?v=uA4ah-dVHvU",
      "title": "AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard",
      "author": "Gareth Yoder, Vanguard",
      "last_modified": "2026-10-21T08:00:37Z",
      "analysis_file": "analysis/uA4ah-dVHvU.json"
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

# Deduplicate events and make side effects idempotent

## What

Deduplicate events and make side effects idempotent

Resuming at an exact pending tool call must not replay completed external effects or reuse stale authorization.

## Evidence

Source analysis [^FQwTqUmcbRg]; no independently matched timestamped quote published.

> them. I didn't have a proper queue. I wasn't counting the attempts,
> — 09:49 [^KHudyx5wW3U]

> to be idempotent and if not, I want it to be recording that, you know, it is
> — 09:44 [^NaOkR3VSfR4]

> which indicates exactly which tool call for example we need to resume at and
> — 17:42 [^ZB7l4uxW3Yo]

Source analysis [^ZD9-4fW2HhM]; no independently matched timestamped quote published.

Source analysis [^_-oIuRH4oGA]; no independently matched timestamped quote published.

Source analysis [^cf2IhzqeQH4]; no independently matched timestamped quote published.

Source analysis [^flf_IKnFYnE]; no independently matched timestamped quote published.

Source analysis [^hD9-V56FNRI]; no independently matched timestamped quote published.

> activities themselves should be item potent um we don't require it we don't
> — 43:26 [^k8cnVCMYmNc]

> >> for steps, it can have side effects. That's sort of the point.
> — 58:29 [^kmV-qg4uoNI]

Source analysis [^sn79oS4MZFI]; no independently matched timestamped quote published.

> process where you can save and restore the state of your workflow over the
> — 17:15 [^tZycGA_Fbfo]

Source analysis [^uA4ah-dVHvU]; no independently matched timestamped quote published.

Source analysis [^wflNENRSUb4]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^FQwTqUmcbRg]: [Lessons from Generating 12 Trillion Synthetic Tokens — Bogdan Gaza, DatologyAI](https://www.youtube.com/watch?v=FQwTqUmcbRg); publication: 2026-10-02T23:30:27Z; analysis: `analysis/FQwTqUmcbRg.json`.
[^KHudyx5wW3U]: [Agent Frameworks Considered Harmful — Rémi Louf, .txt](https://www.youtube.com/watch?v=KHudyx5wW3U); publication: 2026-08-22T16:30:39Z; analysis: `analysis/KHudyx5wW3U.json`.
[^NaOkR3VSfR4]: [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4); publication: 2026-10-08T22:30:09Z; analysis: `analysis/NaOkR3VSfR4.json`.
[^ZB7l4uxW3Yo]: [Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson](https://www.youtube.com/watch?v=ZB7l4uxW3Yo); publication: 2025-06-03T22:31:07Z; analysis: `analysis/ZB7l4uxW3Yo.json`.
[^ZD9-4fW2HhM]: [Build Systems, Not Code - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=ZD9-4fW2HhM); publication: 2026-06-25T18:00:06Z; analysis: `analysis/ZD9-4fW2HhM.json`.
[^_-oIuRH4oGA]: [How agents broke app-level infrastructure - Evan Boyle](https://www.youtube.com/watch?v=_-oIuRH4oGA); publication: 2025-06-03T22:22:28Z; analysis: `analysis/_-oIuRH4oGA.json`.
[^cf2IhzqeQH4]: [Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg](https://www.youtube.com/watch?v=cf2IhzqeQH4); publication: 2026-10-07T00:30:28Z; analysis: `analysis/cf2IhzqeQH4.json`.
[^flf_IKnFYnE]: [From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/flf_IKnFYnE.json`.
[^hD9-V56FNRI]: [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](https://www.youtube.com/watch?v=hD9-V56FNRI); publication: 2026-08-29T16:00:06Z; analysis: `analysis/hD9-V56FNRI.json`.
[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
[^kmV-qg4uoNI]: [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](https://www.youtube.com/watch?v=kmV-qg4uoNI); publication: 2026-01-06T16:00:07Z; analysis: `analysis/kmV-qg4uoNI.json`.
[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
[^tZycGA_Fbfo]: [Paving the Road to Production: Governed Enterprise AI Agents — Harish Gaggar, Credit Karma](https://www.youtube.com/watch?v=tZycGA_Fbfo); publication: 2026-10-14T17:00:04Z; analysis: `analysis/tZycGA_Fbfo.json`.
[^uA4ah-dVHvU]: [AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard](https://www.youtube.com/watch?v=uA4ah-dVHvU); publication: 2026-10-21T08:00:37Z; analysis: `analysis/uA4ah-dVHvU.json`.
[^wflNENRSUb4]: [Give Your Agent a Computer — Nico Albanese, Vercel](https://www.youtube.com/watch?v=wflNENRSUb4); publication: 2026-05-12T18:00:06Z; analysis: `analysis/wflNENRSUb4.json`.
