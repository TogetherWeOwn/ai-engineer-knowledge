---
{
  "type": "technique",
  "id": "role-specific-guidance",
  "title": "Load role-specific procedural guidance without imposing every policy on every phase",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-10-11T20:30:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LlgiOCmFG_w",
      "resource": "https://www.youtube.com/watch?v=LlgiOCmFG_w",
      "title": "Fixing the PR Bottleneck — Matt Pocock, AIHero",
      "author": "Matt Pocock, AIHero",
      "last_modified": "2026-09-26T00:07:54Z",
      "analysis_file": "analysis/LlgiOCmFG_w.json"
    },
    {
      "id": "aV_vgUSatqs",
      "resource": "https://www.youtube.com/watch?v=aV_vgUSatqs",
      "title": "Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal",
      "author": "Mark Lummus & Navinkumar Patil, PayPal",
      "last_modified": "2026-10-11T20:30:04Z",
      "analysis_file": "analysis/aV_vgUSatqs.json"
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
      "id": "lp0pswT_FEI",
      "resource": "https://www.youtube.com/watch?v=lp0pswT_FEI",
      "title": "Just do it. (let your tools think for themselves) - Robert Chandler",
      "author": "Robert Chandler",
      "last_modified": "2025-06-10T17:30:11Z",
      "analysis_file": "analysis/lp0pswT_FEI.json"
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

# Load role-specific procedural guidance without imposing every policy on every phase

## What

Load role-specific procedural guidance without imposing every policy on every phase

Keep static structure/terminology/personality guidance distinct from the changing requested content and declare which may override which.

## Evidence

Source analysis [^LlgiOCmFG_w]; no independently matched timestamped quote published.

Source analysis [^aV_vgUSatqs]; no independently matched timestamped quote published.

> should be able to you know npx taste and install my CLI taste and then you can
> — 19:23 [^kWOQS3XPZ10]

Source analysis [^lp0pswT_FEI]; no independently matched timestamped quote published.

> to write it. It's basically the styling layer on top of it.
> — 1:17:29 [^mYSRn6PC1mc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LlgiOCmFG_w]: [Fixing the PR Bottleneck — Matt Pocock, AIHero](https://www.youtube.com/watch?v=LlgiOCmFG_w); publication: 2026-09-26T00:07:54Z; analysis: `analysis/LlgiOCmFG_w.json`.
[^aV_vgUSatqs]: [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](https://www.youtube.com/watch?v=aV_vgUSatqs); publication: 2026-10-11T20:30:04Z; analysis: `analysis/aV_vgUSatqs.json`.
[^kWOQS3XPZ10]: [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode](https://www.youtube.com/watch?v=kWOQS3XPZ10); publication: 2025-11-24T20:16:36Z; analysis: `analysis/kWOQS3XPZ10.json`.
[^lp0pswT_FEI]: [Just do it. (let your tools think for themselves) - Robert Chandler](https://www.youtube.com/watch?v=lp0pswT_FEI); publication: 2025-06-10T17:30:11Z; analysis: `analysis/lp0pswT_FEI.json`.
[^mYSRn6PC1mc]: [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](https://www.youtube.com/watch?v=mYSRn6PC1mc); publication: 2026-04-20T18:45:16Z; analysis: `analysis/mYSRn6PC1mc.json`.
