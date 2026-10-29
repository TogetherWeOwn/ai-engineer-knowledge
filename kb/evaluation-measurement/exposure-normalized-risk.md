---
{
  "type": "technique",
  "id": "exposure-normalized-risk",
  "title": "Convert rare failure rates into expected exposure and downstream error cost",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2024-11-22T20:27:24Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OrtBEBLMXdM",
      "resource": "https://www.youtube.com/watch?v=OrtBEBLMXdM",
      "title": "Iterating on LLM apps at scale  Learnings from Discord: Ian Webster",
      "author": null,
      "last_modified": "2024-11-22T20:27:24Z",
      "analysis_file": "analysis/OrtBEBLMXdM.json"
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

# Convert rare failure rates into expected exposure and downstream error cost

## What

Convert rare failure rates into expected exposure and downstream error cost

A tiny per-interaction risk becomes frequent at large volume; quantify exposure and severity rather than accepting a good-looking average score.

## Evidence

> you have a one in a million uh sort of occurrence uh it will happen 200 times
> — 02:27 [^OrtBEBLMXdM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OrtBEBLMXdM]: [Iterating on LLM apps at scale  Learnings from Discord: Ian Webster](https://www.youtube.com/watch?v=OrtBEBLMXdM); publication: 2024-11-22T20:27:24Z; analysis: `analysis/OrtBEBLMXdM.json`.
