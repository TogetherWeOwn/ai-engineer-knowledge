---
{
  "type": "technique",
  "id": "sandbox-security-contract",
  "title": "Specify isolation, permission, persistence and cleanup guarantees independently",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-12T05:10:18Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "iH_wV8BbS24",
      "resource": "https://www.youtube.com/watch?v=iH_wV8BbS24",
      "title": "Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-10-12T05:10:18Z",
      "analysis_file": "analysis/iH_wV8BbS24.json"
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
      "id": "wVl6ZjELpBk",
      "resource": "https://www.youtube.com/watch?v=wVl6ZjELpBk",
      "title": "Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI",
      "author": "Bill Chen & Brian Fioca, OpenAI",
      "last_modified": "2025-12-05T17:00:06Z",
      "analysis_file": "analysis/wVl6ZjELpBk.json"
    },
    {
      "id": "xn8EsW0wxyc",
      "resource": "https://www.youtube.com/watch?v=xn8EsW0wxyc",
      "title": "How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI",
      "author": "Venice AI",
      "last_modified": "2026-10-11T16:30:34Z",
      "analysis_file": "analysis/xn8EsW0wxyc.json"
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

# Specify isolation, permission, persistence and cleanup guarantees independently

## What

Specify isolation, permission, persistence and cleanup guarantees independently

A durable workflow does not manage VM state or supply network/tool permissions; those require separate execution and capability boundaries.

## Evidence

> Uh, I did want to, uh, touch on the fact that sandboxing is not a panacea. Um,
> — 12:25 [^iH_wV8BbS24]

> like in a sandbox there sandbox being a VM and so this VM state is not managed
> — 44:40 [^kmV-qg4uoNI]

Source analysis [^wVl6ZjELpBk]; no independently matched timestamped quote published.

Source analysis [^xn8EsW0wxyc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^iH_wV8BbS24]: [Sandboxes Aren't Optional: 4 Ways to Isolate Coding Agents — Robert Brennan, OpenHands](https://www.youtube.com/watch?v=iH_wV8BbS24); publication: 2026-10-12T05:10:18Z; analysis: `analysis/iH_wV8BbS24.json`.
[^kmV-qg4uoNI]: [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](https://www.youtube.com/watch?v=kmV-qg4uoNI); publication: 2026-01-06T16:00:07Z; analysis: `analysis/kmV-qg4uoNI.json`.
[^wVl6ZjELpBk]: [Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI](https://www.youtube.com/watch?v=wVl6ZjELpBk); publication: 2025-12-05T17:00:06Z; analysis: `analysis/wVl6ZjELpBk.json`.
[^xn8EsW0wxyc]: [How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI](https://www.youtube.com/watch?v=xn8EsW0wxyc); publication: 2026-10-11T16:30:34Z; analysis: `analysis/xn8EsW0wxyc.json`.
