---
{
  "type": "technique",
  "id": "claim-scope-provenance",
  "title": "Tie every performance claim to its population, denominator, date and study design",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-13T18:00:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "MWTJIAwAAnk",
      "resource": "https://www.youtube.com/watch?v=MWTJIAwAAnk",
      "title": "Trust, but Verify: Knowledge Agents for Finance Workflows - Mike Conover",
      "author": "Mike Conover",
      "last_modified": "2025-04-09T15:30:31Z",
      "analysis_file": "analysis/MWTJIAwAAnk.json"
    },
    {
      "id": "McknwOzbmyg",
      "resource": "https://www.youtube.com/watch?v=McknwOzbmyg",
      "title": "Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia",
      "author": "Jared Joselowitz, Ufonia",
      "last_modified": "2026-08-19T15:00:31Z",
      "analysis_file": "analysis/McknwOzbmyg.json"
    },
    {
      "id": "U7ZYBCcdJPg",
      "resource": "https://www.youtube.com/watch?v=U7ZYBCcdJPg",
      "title": "Tokens Are the Cheap Part — Steve Jamison, Jellyfish",
      "author": "Steve Jamison, Jellyfish",
      "last_modified": "2026-10-13T17:00:19Z",
      "analysis_file": "analysis/U7ZYBCcdJPg.json"
    },
    {
      "id": "gDRCpTMCqEU",
      "resource": "https://www.youtube.com/watch?v=gDRCpTMCqEU",
      "title": "What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad",
      "author": "Soukaïna Abelhad",
      "last_modified": "2026-10-13T18:00:17Z",
      "analysis_file": "analysis/gDRCpTMCqEU.json"
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

# Tie every performance claim to its population, denominator, date and study design

## What

Tie every performance claim to its population, denominator, date and study design

Record task, population, denominator, time window and experimental versus observational design so a real number is not generalized into an unsupported company-wide productivity claim.

## Evidence

Source analysis [^MWTJIAwAAnk]; no independently matched timestamped quote published.

Source analysis [^McknwOzbmyg]; no independently matched timestamped quote published.

Source analysis [^U7ZYBCcdJPg]; no independently matched timestamped quote published.

Source analysis [^gDRCpTMCqEU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^MWTJIAwAAnk]: [Trust, but Verify: Knowledge Agents for Finance Workflows - Mike Conover](https://www.youtube.com/watch?v=MWTJIAwAAnk); publication: 2025-04-09T15:30:31Z; analysis: `analysis/MWTJIAwAAnk.json`.
[^McknwOzbmyg]: [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg); publication: 2026-08-19T15:00:31Z; analysis: `analysis/McknwOzbmyg.json`.
[^U7ZYBCcdJPg]: [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](https://www.youtube.com/watch?v=U7ZYBCcdJPg); publication: 2026-10-13T17:00:19Z; analysis: `analysis/U7ZYBCcdJPg.json`.
[^gDRCpTMCqEU]: [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](https://www.youtube.com/watch?v=gDRCpTMCqEU); publication: 2026-10-13T18:00:17Z; analysis: `analysis/gDRCpTMCqEU.json`.
