---
{
  "type": "technique",
  "id": "harm-aware-latency",
  "title": "Include harmful early actions and time-to-correction when optimizing response latency",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-09-15T14:30:14Z",
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
      "id": "xLUQOqjudtA",
      "resource": "https://www.youtube.com/watch?v=xLUQOqjudtA",
      "title": "Tolan: Voice-First AI Companion — Paula Dozsa, Tolan",
      "author": "Paula Dozsa, Tolan",
      "last_modified": "2026-09-15T14:30:14Z",
      "analysis_file": "analysis/xLUQOqjudtA.json"
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

# Include harmful early actions and time-to-correction when optimizing response latency

## What

Include harmful early actions and time-to-correction when optimizing response latency

Slightly slower decisions can improve outcomes if they avoid premature interruption.

## Evidence

> it's a 8 Minute feedback loop it's a 20-minute feedback loop goodness you're
> — 12:49 [^MWTJIAwAAnk]

> half. And we happily paid about 60
> — 04:46 [^xLUQOqjudtA]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^MWTJIAwAAnk]: [Trust, but Verify: Knowledge Agents for Finance Workflows - Mike Conover](https://www.youtube.com/watch?v=MWTJIAwAAnk); publication: 2025-04-09T15:30:31Z; analysis: `analysis/MWTJIAwAAnk.json`.
[^xLUQOqjudtA]: [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA); publication: 2026-09-15T14:30:14Z; analysis: `analysis/xLUQOqjudtA.json`.
