---
{
  "type": "technique",
  "id": "product-style-validation",
  "title": "Assess taste and usability separately from correctness without adding human merge or deployment gates",
  "area": "product-ui-quality",
  "status": "stable",
  "valid_from": "2026-08-20T15:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "_ehJyfHg1Vk",
      "resource": "https://www.youtube.com/watch?v=_ehJyfHg1Vk",
      "title": "The Era of Compound Engineering — Kieran Klaassen, Every/Cora",
      "author": "Kieran Klaassen, Every/Cora",
      "last_modified": "2026-08-20T15:00:06Z",
      "analysis_file": "analysis/_ehJyfHg1Vk.json"
    },
    {
      "id": "kWOQS3XPZ10",
      "resource": "https://www.youtube.com/watch?v=kWOQS3XPZ10",
      "title": "Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode",
      "author": "Ahmad Awais, CommandCode",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/kWOQS3XPZ10.json"
    },
    {
      "id": "wjk0ulMAkbc",
      "resource": "https://www.youtube.com/watch?v=wjk0ulMAkbc",
      "title": "Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer",
      "author": null,
      "last_modified": "2026-04-21T14:00:06Z",
      "analysis_file": "analysis/wjk0ulMAkbc.json"
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

# Assess taste and usability separately from correctness without adding human merge or deployment gates

## What

Assess taste and usability separately from correctness without adding human merge or deployment gates

After correctness works, inspect product quality and extract repeatable taste decisions; polish must not disguise broken functionality.

## Evidence

> think? And this is not QA. This is raising the bar like it should work. If
> — 15:49 [^_ehJyfHg1Vk]

Source analysis [^kWOQS3XPZ10]; no independently matched timestamped quote published.

Source analysis [^wjk0ulMAkbc]; no independently matched timestamped quote published.

Source analysis [^zgNvts_2TUE]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less rework from misunderstood intent
- **Speed:** Faster useful feedback on runnable behavior
- **Quality:** Better usability, accessibility and actual task completion
- **Reliability:** Real-app evidence rather than attractive but broken demos
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^_ehJyfHg1Vk]: [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk); publication: 2026-08-20T15:00:06Z; analysis: `analysis/_ehJyfHg1Vk.json`.
[^kWOQS3XPZ10]: [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode](https://www.youtube.com/watch?v=kWOQS3XPZ10); publication: 2025-11-24T20:16:36Z; analysis: `analysis/kWOQS3XPZ10.json`.
[^wjk0ulMAkbc]: [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer](https://www.youtube.com/watch?v=wjk0ulMAkbc); publication: 2026-04-21T14:00:06Z; analysis: `analysis/wjk0ulMAkbc.json`.
[^zgNvts_2TUE]: [State of the Claw — Peter Steinberger](https://www.youtube.com/watch?v=zgNvts_2TUE); publication: 2026-04-17T15:30:06Z; analysis: `analysis/zgNvts_2TUE.json`.
