---
{
  "type": "technique",
  "id": "async-investigation",
  "title": "Make investigations and research self-contained and resumable",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-10-06T23:30:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "MGzymaYBiss",
      "resource": "https://www.youtube.com/watch?v=MGzymaYBiss",
      "title": "Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I",
      "author": "Dan Shipper, Every, AI & I",
      "last_modified": "2025-12-18T18:00:06Z",
      "analysis_file": "analysis/MGzymaYBiss.json"
    },
    {
      "id": "MLhAA9yguwM",
      "resource": "https://www.youtube.com/watch?v=MLhAA9yguwM",
      "title": "The 3 Pillars of Autonomy – Michele Catasta, Replit",
      "author": "Michele Catasta, Replit",
      "last_modified": "2025-12-22T16:30:06Z",
      "analysis_file": "analysis/MLhAA9yguwM.json"
    },
    {
      "id": "XyV6bSMyq-I",
      "resource": "https://www.youtube.com/watch?v=XyV6bSMyq-I",
      "title": "How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases",
      "author": "Zubin Aysola, Weights & Biases",
      "last_modified": "2026-09-26T16:00:08Z",
      "analysis_file": "analysis/XyV6bSMyq-I.json"
    },
    {
      "id": "ZRM_TfEZcIo",
      "resource": "https://www.youtube.com/watch?v=ZRM_TfEZcIo",
      "title": "Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "author": "Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "last_modified": "2026-06-26T14:00:07Z",
      "analysis_file": "analysis/ZRM_TfEZcIo.json"
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
      "id": "eXA2tjRZIbY",
      "resource": "https://www.youtube.com/watch?v=eXA2tjRZIbY",
      "title": "The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI",
      "author": "Varun Krovvidi, Resolve AI",
      "last_modified": "2026-10-06T23:30:36Z",
      "analysis_file": "analysis/eXA2tjRZIbY.json"
    },
    {
      "id": "li0SaBt9RDM",
      "resource": "https://www.youtube.com/watch?v=li0SaBt9RDM",
      "title": "The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry",
      "author": "Priscila Andre de Oliveira, Sentry",
      "last_modified": "2026-05-27T17:00:06Z",
      "analysis_file": "analysis/li0SaBt9RDM.json"
    },
    {
      "id": "mYSRn6PC1mc",
      "resource": "https://www.youtube.com/watch?v=mYSRn6PC1mc",
      "title": "Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi",
      "author": "Louis-François Bouchard, Paul Iusztin, Samridhi",
      "last_modified": "2026-04-20T18:45:16Z",
      "analysis_file": "analysis/mYSRn6PC1mc.json"
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

# Make investigations and research self-contained and resumable

## What

Make investigations and research self-contained and resumable

Delegate a bounded investigation, then return to its evidence and proposed fix instead of requiring continuous attention.

## Evidence

> you to investigate this bug." And then go do something else and then come back
> — 15:52 [^MGzymaYBiss]

> agent is running because you can inject useful information back into the main
> — 22:20 [^MLhAA9yguwM]

> for itself to run a bunch of parallel executions of its own research loop.
> — 08:32 [^XyV6bSMyq-I]

Source analysis [^ZRM_TfEZcIo]; no independently matched timestamped quote published.

> will unblock the workflow and will spin up a set of parallel research agents. So
> — 05:56 [^cI7zfqusmFU]

Source analysis [^eXA2tjRZIbY]; no independently matched timestamped quote published.

Source analysis [^li0SaBt9RDM]; no independently matched timestamped quote published.

> human-written guideline, which would basically be just what is the topic
> — 28:46 [^mYSRn6PC1mc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^MGzymaYBiss]: [Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I](https://www.youtube.com/watch?v=MGzymaYBiss); publication: 2025-12-18T18:00:06Z; analysis: `analysis/MGzymaYBiss.json`.
[^MLhAA9yguwM]: [The 3 Pillars of Autonomy – Michele Catasta, Replit](https://www.youtube.com/watch?v=MLhAA9yguwM); publication: 2025-12-22T16:30:06Z; analysis: `analysis/MLhAA9yguwM.json`.
[^XyV6bSMyq-I]: [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](https://www.youtube.com/watch?v=XyV6bSMyq-I); publication: 2026-09-26T16:00:08Z; analysis: `analysis/XyV6bSMyq-I.json`.
[^ZRM_TfEZcIo]: [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo); publication: 2026-06-26T14:00:07Z; analysis: `analysis/ZRM_TfEZcIo.json`.
[^cI7zfqusmFU]: [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU); publication: 2026-09-14T15:30:30Z; analysis: `analysis/cI7zfqusmFU.json`.
[^eXA2tjRZIbY]: [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY); publication: 2026-10-06T23:30:36Z; analysis: `analysis/eXA2tjRZIbY.json`.
[^li0SaBt9RDM]: [The AI Skill I Rely On Daily — Priscila Andre de Oliveira, Sentry](https://www.youtube.com/watch?v=li0SaBt9RDM); publication: 2026-05-27T17:00:06Z; analysis: `analysis/li0SaBt9RDM.json`.
[^mYSRn6PC1mc]: [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](https://www.youtube.com/watch?v=mYSRn6PC1mc); publication: 2026-04-20T18:45:16Z; analysis: `analysis/mYSRn6PC1mc.json`.
