---
{
  "type": "technique",
  "id": "work-deduplication",
  "title": "Deduplicate new tasks and investigations against existing work and outcomes",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-10-18T09:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "W4pnzOURwHQ",
      "resource": "https://www.youtube.com/watch?v=W4pnzOURwHQ",
      "title": "Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs",
      "author": "Denys Linkov, Wisedocs",
      "last_modified": "2026-10-18T09:00:25Z",
      "analysis_file": "analysis/W4pnzOURwHQ.json"
    },
    {
      "id": "WLXxTaPagA8",
      "resource": "https://www.youtube.com/watch?v=WLXxTaPagA8",
      "title": "Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony",
      "author": "Sumaiya Shrabony",
      "last_modified": "2026-07-11T16:30:04Z",
      "analysis_file": "analysis/WLXxTaPagA8.json"
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
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
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
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
    },
    {
      "id": "zMXKhhwiCIc",
      "resource": "https://www.youtube.com/watch?v=zMXKhhwiCIc",
      "title": "Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage",
      "author": "Alex Gavrilescu, Funstage",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/zMXKhhwiCIc.json"
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

# Deduplicate new tasks and investigations against existing work and outcomes

## What

Compare a candidate artifact, task or finding with prior outputs so locally coherent results do not repeatedly cover the same underlying issue.

## Evidence

Source analysis [^W4pnzOURwHQ]; no independently matched timestamped quote published.

Source analysis [^WLXxTaPagA8]; no independently matched timestamped quote published.

> goes, "Oh, yeah. I think this is the same issue." Not only is the same issue,
> — 56:57 [^il1c1a2FufU]

> monitors and when someone asked me for something new in Slack it goes and looks
> — 52:09 [^pFsfax19yOM]

> we have a way of kind of deduplicating and seeing what's out there. This might
> — 15:07 [^pmoDeA3RBZY]

> created or any PR with the loops label on it is open. And if so, we just shut
> — 15:55 [^xIt_mTQp6mY]

> tasks. Before creating new task, AI agents should search if that task
> — 07:11 [^zMXKhhwiCIc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^W4pnzOURwHQ]: [Insurance Claims Are AI's Messiest Data Problem — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=W4pnzOURwHQ); publication: 2026-10-18T09:00:25Z; analysis: `analysis/W4pnzOURwHQ.json`.
[^WLXxTaPagA8]: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD - Sumaiya Shrabony](https://www.youtube.com/watch?v=WLXxTaPagA8); publication: 2026-07-11T16:30:04Z; analysis: `analysis/WLXxTaPagA8.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^pmoDeA3RBZY]: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY); publication: 2026-06-05T16:00:06Z; analysis: `analysis/pmoDeA3RBZY.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
[^zMXKhhwiCIc]: [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage](https://www.youtube.com/watch?v=zMXKhhwiCIc); publication: 2025-11-24T20:16:38Z; analysis: `analysis/zMXKhhwiCIc.json`.
