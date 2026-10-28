---
{
  "type": "technique",
  "id": "durable-waits",
  "title": "Persist wait conditions and resume on signals instead of holding a polling agent open",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-04T16:30:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "ZB7l4uxW3Yo",
      "resource": "https://www.youtube.com/watch?v=ZB7l4uxW3Yo",
      "title": "Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson",
      "author": "Greg Benson",
      "last_modified": "2025-06-03T22:31:07Z",
      "analysis_file": "analysis/ZB7l4uxW3Yo.json"
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
      "id": "flf_IKnFYnE",
      "resource": "https://www.youtube.com/watch?v=flf_IKnFYnE",
      "title": "From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/flf_IKnFYnE.json"
    },
    {
      "id": "jc3kbZkuHTo",
      "resource": "https://www.youtube.com/watch?v=jc3kbZkuHTo",
      "title": "The Human Is an Async API — Melanie Warrick, Temporal",
      "author": "Melanie Warrick, Temporal",
      "last_modified": "2026-10-04T16:30:17Z",
      "analysis_file": "analysis/jc3kbZkuHTo.json"
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
      "id": "vi-2nasppAg",
      "resource": "https://www.youtube.com/watch?v=vi-2nasppAg",
      "title": "Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate",
      "author": "Jonas Templestein, Iterate",
      "last_modified": "2026-05-14T14:00:06Z",
      "analysis_file": "analysis/vi-2nasppAg.json"
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

# Persist wait conditions and resume on signals instead of holding a polling agent open

## What

Persist wait conditions and resume on signals instead of holding a polling agent open

A durable timer can suspend a workflow until a future event without occupying an agent process or repeatedly re-entering an LLM loop.

## Evidence

Source analysis [^ZB7l4uxW3Yo]; no independently matched timestamped quote published.

> while we are waiting this process actually suspends. So if it's running on
> — 08:56 [^cI7zfqusmFU]

> days in here. Temporal would take care of pausing everything. Again, I'm not
> — 18:12 [^flf_IKnFYnE]

Source analysis [^jc3kbZkuHTo]; no independently matched timestamped quote published.

> when the user comes back and gives you that input, it just reconstitutes memory
> — 59:32 [^k8cnVCMYmNc]

Source analysis [^vi-2nasppAg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^ZB7l4uxW3Yo]: [Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson](https://www.youtube.com/watch?v=ZB7l4uxW3Yo); publication: 2025-06-03T22:31:07Z; analysis: `analysis/ZB7l4uxW3Yo.json`.
[^cI7zfqusmFU]: [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU); publication: 2026-09-14T15:30:30Z; analysis: `analysis/cI7zfqusmFU.json`.
[^flf_IKnFYnE]: [From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/flf_IKnFYnE.json`.
[^jc3kbZkuHTo]: [The Human Is an Async API — Melanie Warrick, Temporal](https://www.youtube.com/watch?v=jc3kbZkuHTo); publication: 2026-10-04T16:30:17Z; analysis: `analysis/jc3kbZkuHTo.json`.
[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
[^vi-2nasppAg]: [Make your own event-sourced agent harness using stream processors — Jonas Templestein, Iterate](https://www.youtube.com/watch?v=vi-2nasppAg); publication: 2026-05-14T14:00:06Z; analysis: `analysis/vi-2nasppAg.json`.
