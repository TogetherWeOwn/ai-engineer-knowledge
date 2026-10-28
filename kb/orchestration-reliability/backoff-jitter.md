---
{
  "type": "technique",
  "id": "backoff-jitter",
  "title": "Use bounded exponential backoff and jitter for transient failures",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-09-14T15:30:30Z",
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
      "id": "KJ9eZYTWS1Y",
      "resource": "https://www.youtube.com/watch?v=KJ9eZYTWS1Y",
      "title": "Events are the Wrong Abstraction for Your AI Agents - Mason Egger, Temporal.io",
      "author": "Mason Egger, Temporal.io",
      "last_modified": "2025-06-27T09:35:48Z",
      "analysis_file": "analysis/KJ9eZYTWS1Y.json"
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
      "id": "cI7zfqusmFU",
      "resource": "https://www.youtube.com/watch?v=cI7zfqusmFU",
      "title": "Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate",
      "author": "Giselle van Dongen, Restate",
      "last_modified": "2026-09-14T15:30:30Z",
      "analysis_file": "analysis/cI7zfqusmFU.json"
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
      "id": "kQmXtrmQ5Zg",
      "resource": "https://www.youtube.com/watch?v=kQmXtrmQ5Zg",
      "title": "Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic",
      "author": "Full Workshop with Mahesh Murag of Anthropic",
      "last_modified": "2025-03-01T16:59:35Z",
      "analysis_file": "analysis/kQmXtrmQ5Zg.json"
    },
    {
      "id": "kmV-qg4uoNI",
      "resource": "https://www.youtube.com/watch?v=kmV-qg4uoNI",
      "title": "Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel",
      "author": "Peter Wielander, Vercel",
      "last_modified": "2026-01-06T16:00:07Z",
      "analysis_file": "analysis/kmV-qg4uoNI.json"
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

# Use bounded exponential backoff and jitter for transient failures

## What

Use bounded exponential backoff and jitter for transient failures

Configure which activities retry, maximum attempts/elapsed time and delay, rather than ad hoc infinite retry loops.

## Evidence

Source analysis [^1izYWsokr9s]; no independently matched timestamped quote published.

Source analysis [^KJ9eZYTWS1Y]; no independently matched timestamped quote published.

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

> successfully. So instead of starting over, it uses the journal to recover the
> — 06:52 [^cI7zfqusmFU]

> exponential back back off in place to ensure that uh the downstream
> — 10:02 [^hD9-V56FNRI]

> uh configuration. So you can decide are you going to do exponential backoffs?
> — 15:10 [^k8cnVCMYmNc]

> shakes out is a lot of that should happen on the server side um the server
> — 45:02 [^kQmXtrmQ5Zg]

> to have timeouts. The nice thing is that every step runs in its own serless
> — 48:17 [^kmV-qg4uoNI]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1izYWsokr9s]: [Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal](https://www.youtube.com/watch?v=1izYWsokr9s); publication: 2025-07-28T15:15:00Z; analysis: `analysis/1izYWsokr9s.json`.
[^KJ9eZYTWS1Y]: [Events are the Wrong Abstraction for Your AI Agents - Mason Egger, Temporal.io](https://www.youtube.com/watch?v=KJ9eZYTWS1Y); publication: 2025-06-27T09:35:48Z; analysis: `analysis/KJ9eZYTWS1Y.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^cI7zfqusmFU]: [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU); publication: 2026-09-14T15:30:30Z; analysis: `analysis/cI7zfqusmFU.json`.
[^hD9-V56FNRI]: [AI Agents Are Just Distributed Systems Now — Salman Munaf, TikTok](https://www.youtube.com/watch?v=hD9-V56FNRI); publication: 2026-08-29T16:00:06Z; analysis: `analysis/hD9-V56FNRI.json`.
[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
[^kQmXtrmQ5Zg]: [Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg); publication: 2025-03-01T16:59:35Z; analysis: `analysis/kQmXtrmQ5Zg.json`.
[^kmV-qg4uoNI]: [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](https://www.youtube.com/watch?v=kmV-qg4uoNI); publication: 2026-01-06T16:00:07Z; analysis: `analysis/kmV-qg4uoNI.json`.
