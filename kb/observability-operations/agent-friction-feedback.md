---
{
  "type": "technique",
  "id": "agent-friction-feedback",
  "title": "Collect sparse agent-reported friction and verify it against traces before acting",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-06-02T16:00:33Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-aM2EDTiaMs",
      "resource": "https://www.youtube.com/watch?v=-aM2EDTiaMs",
      "title": "Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop",
      "author": "Danny Gollapalli & Zubin Koticha, Raindrop",
      "last_modified": "2026-05-07T13:00:06Z",
      "analysis_file": "analysis/-aM2EDTiaMs.json"
    },
    {
      "id": "KA5kPbdkK2E",
      "resource": "https://www.youtube.com/watch?v=KA5kPbdkK2E",
      "title": "How Lovable self-improves every hour — Benjamin Verbeek, Lovable",
      "author": "Benjamin Verbeek, Lovable",
      "last_modified": "2026-06-02T16:00:33Z",
      "analysis_file": "analysis/KA5kPbdkK2E.json"
    },
    {
      "id": "blrovBxxN9o",
      "resource": "https://www.youtube.com/watch?v=blrovBxxN9o",
      "title": "Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier",
      "author": "Rafal Willinski, Vitor Balocco, Zapier",
      "last_modified": "2025-06-30T17:15:06Z",
      "analysis_file": "analysis/blrovBxxN9o.json"
    },
    {
      "id": "juoNbJiZUi0",
      "resource": "https://www.youtube.com/watch?v=juoNbJiZUi0",
      "title": "LLM codegen fails and how to stop 'em — Danilo Campos, PostHog",
      "author": "Danilo Campos, PostHog",
      "last_modified": "2026-04-30T14:00:06Z",
      "analysis_file": "analysis/juoNbJiZUi0.json"
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

# Collect sparse agent-reported friction and verify it against traces before acting

## What

Collect sparse agent-reported friction and verify it against traces before acting

The working agent already holds rich failure context; let it report material tooling friction instead of paying an external frontier judge to reread every turn.

## Evidence

Source analysis [^-aM2EDTiaMs]; no independently matched timestamped quote published.

> it's prompted to only send feedback if it is really frustrated. And you can
> — 13:28 [^KA5kPbdkK2E]

> Uh recently we had a lot of success as well using an LLM to detect and group
> — 05:36 [^blrovBxxN9o]

> what could we have done better to set you up for success in this
> — 11:29 [^juoNbJiZUi0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-aM2EDTiaMs]: [Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop](https://www.youtube.com/watch?v=-aM2EDTiaMs); publication: 2026-05-07T13:00:06Z; analysis: `analysis/-aM2EDTiaMs.json`.
[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^blrovBxxN9o]: [Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier](https://www.youtube.com/watch?v=blrovBxxN9o); publication: 2025-06-30T17:15:06Z; analysis: `analysis/blrovBxxN9o.json`.
[^juoNbJiZUi0]: [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](https://www.youtube.com/watch?v=juoNbJiZUi0); publication: 2026-04-30T14:00:06Z; analysis: `analysis/juoNbJiZUi0.json`.
