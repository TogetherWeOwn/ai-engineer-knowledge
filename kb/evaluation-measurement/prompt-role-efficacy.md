---
{
  "type": "technique",
  "id": "prompt-role-efficacy",
  "title": "Treat persona prompting as a style hypothesis, not evidence of improved factual accuracy",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2025-07-14T19:00:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "_BRhRh7mOX0",
      "resource": "https://www.youtube.com/watch?v=_BRhRh7mOX0",
      "title": "Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting",
      "author": "Sander Schulhoff, HackAPrompt/LearnPrompting",
      "last_modified": "2025-07-14T19:00:11Z",
      "analysis_file": "analysis/_BRhRh7mOX0.json"
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

# Treat persona prompting as a style hypothesis, not evidence of improved factual accuracy

## What

Treat persona prompting as a style hypothesis, not evidence of improved factual accuracy

Ran a case study giving models 'genius math professor' vs 'idiot who can't do math' roles on GSM8K; the dumb role scored higher, showing role prompts don't improve accuracy.

## Evidence

Source analysis [^_BRhRh7mOX0]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^_BRhRh7mOX0]: [Prompt Engineering and AI Red Teaming — Sander Schulhoff, HackAPrompt/LearnPrompting](https://www.youtube.com/watch?v=_BRhRh7mOX0); publication: 2025-07-14T19:00:11Z; analysis: `analysis/_BRhRh7mOX0.json`.
