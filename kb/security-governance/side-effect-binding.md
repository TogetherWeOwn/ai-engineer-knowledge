---
{
  "type": "technique",
  "id": "side-effect-binding",
  "title": "Bind sensitive side effects to exact validated payload and current state",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-12T17:00:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2e9ANoOEn28",
      "resource": "https://www.youtube.com/watch?v=2e9ANoOEn28",
      "title": "What if the harness mattered more than the model? - Aditya Bhargava, Etsy",
      "author": "Aditya Bhargava, Etsy",
      "last_modified": "2026-07-07T23:31:54Z",
      "analysis_file": "analysis/2e9ANoOEn28.json"
    },
    {
      "id": "8g0g1ncwzG0",
      "resource": "https://www.youtube.com/watch?v=8g0g1ncwzG0",
      "title": "Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual",
      "author": "Karthic Rao, Perpetual",
      "last_modified": "2026-10-12T17:00:05Z",
      "analysis_file": "analysis/8g0g1ncwzG0.json"
    },
    {
      "id": "9R--1tg45Jg",
      "resource": "https://www.youtube.com/watch?v=9R--1tg45Jg",
      "title": "Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google",
      "author": "Averi Kitsch & Prerna Kakkar, Google",
      "last_modified": "2026-09-09T13:00:04Z",
      "analysis_file": "analysis/9R--1tg45Jg.json"
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
      "id": "khVX_BUnEwU",
      "resource": "https://www.youtube.com/watch?v=khVX_BUnEwU",
      "title": "Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital",
      "author": "Yohei Nakajima, Untapped Capital",
      "last_modified": "2026-07-22T20:00:06Z",
      "analysis_file": "analysis/khVX_BUnEwU.json"
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

# Bind sensitive side effects to exact validated payload and current state

## What

Bind sensitive side effects to exact validated payload and current state

Deterministic code owns control flow, evidence and side effects. Each external action has its own gate, and its approval is tied to the hash of the exact payload and re-checked right before execution. Side effects move through prepared → sent → completed. An unknown outcome goes to manual review, never to an automatic retry. Follow-ups run as new child plans (at most 5 rounds); the approved parent never changes. Wait expiry (default 72 h) is decided by a rule, not a model.

## Evidence

Source analysis [^2e9ANoOEn28]; no independently matched timestamped quote published.

Source analysis [^8g0g1ncwzG0]; no independently matched timestamped quote published.

Source analysis [^9R--1tg45Jg]; no independently matched timestamped quote published.

Source analysis [^NaOkR3VSfR4]; no independently matched timestamped quote published.

> now with continuations, we can designate a tool as needing approval. So here
> — 12:37 [^ZB7l4uxW3Yo]

> control on what it's allowed to change by itself, what uh what kind of changes
> — 06:25 [^khVX_BUnEwU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2e9ANoOEn28]: [What if the harness mattered more than the model? - Aditya Bhargava, Etsy](https://www.youtube.com/watch?v=2e9ANoOEn28); publication: 2026-07-07T23:31:54Z; analysis: `analysis/2e9ANoOEn28.json`.
[^8g0g1ncwzG0]: [Reliable, Smart Workflows for Finance, Wealth and Insurance — Karthic Rao, Perpetual](https://www.youtube.com/watch?v=8g0g1ncwzG0); publication: 2026-10-12T17:00:05Z; analysis: `analysis/8g0g1ncwzG0.json`.
[^9R--1tg45Jg]: [Build-Time vs. Run-Time: Why Dev Tools Fail in Production — Averi Kitsch & Prerna Kakkar, Google](https://www.youtube.com/watch?v=9R--1tg45Jg); publication: 2026-09-09T13:00:04Z; analysis: `analysis/9R--1tg45Jg.json`.
[^NaOkR3VSfR4]: [Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya](https://www.youtube.com/watch?v=NaOkR3VSfR4); publication: 2026-10-08T22:30:09Z; analysis: `analysis/NaOkR3VSfR4.json`.
[^ZB7l4uxW3Yo]: [Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson](https://www.youtube.com/watch?v=ZB7l4uxW3Yo); publication: 2025-06-03T22:31:07Z; analysis: `analysis/ZB7l4uxW3Yo.json`.
[^khVX_BUnEwU]: [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU); publication: 2026-07-22T20:00:06Z; analysis: `analysis/khVX_BUnEwU.json`.
