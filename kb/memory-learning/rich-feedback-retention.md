---
{
  "type": "technique",
  "id": "rich-feedback-retention",
  "title": "Retain detailed corrections, explanations and interventions alongside scalar scores",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-08-20T14:00:21Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "SbcQYbrvAfI",
      "resource": "https://www.youtube.com/watch?v=SbcQYbrvAfI",
      "title": "Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize",
      "author": "SallyAnn DeLucia & Fuad Ali, Arize",
      "last_modified": "2026-01-06T17:30:06Z",
      "analysis_file": "analysis/SbcQYbrvAfI.json"
    },
    {
      "id": "bdHaOXZOhcM",
      "resource": "https://www.youtube.com/watch?v=bdHaOXZOhcM",
      "title": "Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company",
      "author": "Hursh Agrawal, The Browser Company",
      "last_modified": "2026-08-20T14:00:21Z",
      "analysis_file": "analysis/bdHaOXZOhcM.json"
    },
    {
      "id": "pP_dSNz_EdQ",
      "resource": "https://www.youtube.com/watch?v=pP_dSNz_EdQ",
      "title": "The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize",
      "author": "Aparna Dhinakaran, Arize",
      "last_modified": "2025-12-23T17:00:06Z",
      "analysis_file": "analysis/pP_dSNz_EdQ.json"
    },
    {
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
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

# Retain detailed corrections, explanations and interventions alongside scalar scores

## What

Retain detailed corrections, explanations and interventions alongside scalar scores

Which criterion failed and why are more useful prompt-learning inputs than a bare correct/incorrect or 5/5 label.

## Evidence

> or through your own as a judge. That text is really really valuable. I think
> — 08:23 [^SbcQYbrvAfI]

> save a dump of each of the runs with the system prompt and the inputs and my
> — 11:41 [^bdHaOXZOhcM]

Source analysis [^pP_dSNz_EdQ]; no independently matched timestamped quote published.

> leaves a comment, there's probably like high high value and high signal and high
> — 27:23 [^rnDm57Py54A]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^SbcQYbrvAfI]: [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI); publication: 2026-01-06T17:30:06Z; analysis: `analysis/SbcQYbrvAfI.json`.
[^bdHaOXZOhcM]: [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM); publication: 2026-08-20T14:00:21Z; analysis: `analysis/bdHaOXZOhcM.json`.
[^pP_dSNz_EdQ]: [The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize](https://www.youtube.com/watch?v=pP_dSNz_EdQ); publication: 2025-12-23T17:00:06Z; analysis: `analysis/pP_dSNz_EdQ.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
