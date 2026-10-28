---
{
  "type": "technique",
  "id": "exhaustive-completion-check",
  "title": "Verify complete enumerated coverage and final intent, not a convincing partial result",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-16T19:00:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "XzJD1bvXKjs",
      "resource": "https://www.youtube.com/watch?v=XzJD1bvXKjs",
      "title": "How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-09-09T15:00:06Z",
      "analysis_file": "analysis/XzJD1bvXKjs.json"
    },
    {
      "id": "c35YoMdnI78",
      "resource": "https://www.youtube.com/watch?v=c35YoMdnI78",
      "title": "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "author": "Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "last_modified": "2026-07-17T21:00:06Z",
      "analysis_file": "analysis/c35YoMdnI78.json"
    },
    {
      "id": "kiClTcJUnhc",
      "resource": "https://www.youtube.com/watch?v=kiClTcJUnhc",
      "title": "Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic",
      "author": "CJ Avilla & Harrison Stall, Anthropic",
      "last_modified": "2026-10-16T19:00:10Z",
      "analysis_file": "analysis/kiClTcJUnhc.json"
    },
    {
      "id": "yqF6XhzbWBk",
      "resource": "https://www.youtube.com/watch?v=yqF6XhzbWBk",
      "title": "Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo",
      "author": "Sebastian Fox, Composo",
      "last_modified": "2026-08-22T17:00:32Z",
      "analysis_file": "analysis/yqF6XhzbWBk.json"
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

# Verify complete enumerated coverage and final intent, not a convincing partial result

## What

Verify complete enumerated coverage and final intent, not a convincing partial result

An answer can look correct while explicitly abandoning the rest; inspect every required section and final state.

## Evidence

> looks like a real answer. Uh you have to read the whole thing to notice that it
> — 18:06 [^XzJD1bvXKjs]

> It's actually defined when you've enumerated all of those linear tickets.
> — 06:09 [^c35YoMdnI78]

> where after it sees 35 services are healthy, then it starts to like convince
> — 1:12:50 [^kiClTcJUnhc]

> It kept the plan that they talked out of, not the one they chose. Every line
> — 05:15 [^yqF6XhzbWBk]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^XzJD1bvXKjs]: [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs); publication: 2026-09-09T15:00:06Z; analysis: `analysis/XzJD1bvXKjs.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^kiClTcJUnhc]: [Why One AI Agent Isn’t Enough (And How to Run 1,000) - CJ Avilla & Harrison Stall, Anthropic](https://www.youtube.com/watch?v=kiClTcJUnhc); publication: 2026-10-16T19:00:10Z; analysis: `analysis/kiClTcJUnhc.json`.
[^yqF6XhzbWBk]: [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](https://www.youtube.com/watch?v=yqF6XhzbWBk); publication: 2026-08-22T17:00:32Z; analysis: `analysis/yqF6XhzbWBk.json`.
