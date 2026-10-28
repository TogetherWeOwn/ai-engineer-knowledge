---
{
  "type": "technique",
  "id": "bounded-commands",
  "title": "Expose one-shot executable commands with deadlines instead of accidental watch loops",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-05-07T15:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Wmp2Tku2PrI",
      "resource": "https://www.youtube.com/watch?v=Wmp2Tku2PrI",
      "title": "Vibe Engineering Effect Apps — Michael Arnaldi, Effectful",
      "author": "Michael Arnaldi, Effectful",
      "last_modified": "2026-05-07T15:00:06Z",
      "analysis_file": "analysis/Wmp2Tku2PrI.json"
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

# Expose one-shot executable commands with deadlines instead of accidental watch loops

## What

Expose one-shot executable commands with deadlines instead of accidental watch loops

A short command manifest makes correct tests discoverable; finite commands and explicit server lifecycle prevent agents from hanging on watch mode.

## Evidence

> already know because the model is going to try to run this and get stuck. Same
> — 40:16 [^Wmp2Tku2PrI]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
