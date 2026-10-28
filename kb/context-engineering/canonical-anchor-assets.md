---
{
  "type": "technique",
  "id": "canonical-anchor-assets",
  "title": "Maintain a small authoritative set of reusable company and repository context assets",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-07-31T01:11:30Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "AMiyLItEtLA",
      "resource": "https://www.youtube.com/watch?v=AMiyLItEtLA",
      "title": "fighting slop with slop — Vaibhav Gupta, Boundary",
      "author": "Vaibhav Gupta, Boundary",
      "last_modified": "2026-07-31T01:11:30Z",
      "analysis_file": "analysis/AMiyLItEtLA.json"
    },
    {
      "id": "YZQsWVeN3rE",
      "resource": "https://www.youtube.com/watch?v=YZQsWVeN3rE",
      "title": "Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech",
      "author": "Alex Bauer, Upside.tech",
      "last_modified": "2026-07-11T00:57:36Z",
      "analysis_file": "analysis/YZQsWVeN3rE.json"
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
      "id": "aHhB3sjGjkI",
      "resource": "https://www.youtube.com/watch?v=aHhB3sjGjkI",
      "title": "Agents Building Agents - Alfonso Graziano, Nearform",
      "author": "Alfonso Graziano, Nearform",
      "last_modified": "2026-06-28T16:00:34Z",
      "analysis_file": "analysis/aHhB3sjGjkI.json"
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

# Maintain a small authoritative set of reusable company and repository context assets

## What

Maintain a small authoritative set of reusable company and repository context assets

Canonical capabilities, personas and definitions scaffold generation so the agent does not rediscover the business from an undifferentiated document dump.

## Evidence

Source analysis [^AMiyLItEtLA]; no independently matched timestamped quote published.

> anchor assets for our entire company. I think documentation is something that
> — 10:20 [^YZQsWVeN3rE]

> no database, just a simple index based on references. And how how this works?
> — 20:13 [^ZRM_TfEZcIo]

> contains summary, what's working, what's not working.
> — 15:12 [^aHhB3sjGjkI]

> production application going in there. What we have is something much thinner.
> — 05:47 [^juoNbJiZUi0]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^AMiyLItEtLA]: [fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA); publication: 2026-07-31T01:11:30Z; analysis: `analysis/AMiyLItEtLA.json`.
[^YZQsWVeN3rE]: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE); publication: 2026-07-11T00:57:36Z; analysis: `analysis/YZQsWVeN3rE.json`.
[^ZRM_TfEZcIo]: [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo); publication: 2026-06-26T14:00:07Z; analysis: `analysis/ZRM_TfEZcIo.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^juoNbJiZUi0]: [LLM codegen fails and how to stop 'em — Danilo Campos, PostHog](https://www.youtube.com/watch?v=juoNbJiZUi0); publication: 2026-04-30T14:00:06Z; analysis: `analysis/juoNbJiZUi0.json`.
