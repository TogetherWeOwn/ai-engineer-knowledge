---
{
  "type": "technique",
  "id": "skills-deterministic-scripts",
  "title": "Bundle deterministic scripts and known facts into skills rather than recomputing them with an LLM",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-07-20T06:25:15Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "fnLBmfsI_Fg",
      "resource": "https://www.youtube.com/watch?v=fnLBmfsI_Fg",
      "title": "Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft",
      "author": "Joel Allou & Ornella Bahidika, Microsoft",
      "last_modified": "2026-07-20T06:25:15Z",
      "analysis_file": "analysis/fnLBmfsI_Fg.json"
    },
    {
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
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

# Bundle deterministic scripts and known facts into skills rather than recomputing them with an LLM

## What

Bundle deterministic scripts and known facts into skills rather than recomputing them with an LLM

A known git/data command can inject exact current facts rather than requiring the model to rediscover the command each time.

## Evidence

Source analysis [^fnLBmfsI_Fg]; no independently matched timestamped quote published.

> You're saying here are the latest 10 commits in the exact format that I
> — 17:12 [^pFsfax19yOM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^fnLBmfsI_Fg]: [Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft](https://www.youtube.com/watch?v=fnLBmfsI_Fg); publication: 2026-07-20T06:25:15Z; analysis: `analysis/fnLBmfsI_Fg.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
