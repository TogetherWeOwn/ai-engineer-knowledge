---
{
  "type": "technique",
  "id": "fixed-label-taxonomy",
  "title": "Use fixed validated label vocabularies for repeatable classification",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2025-07-23T15:50:35Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Wv1tAxKYLeE",
      "resource": "https://www.youtube.com/watch?v=Wv1tAxKYLeE",
      "title": "The Billable Hour is Dead; Long Live the Billable Hour — Kevin Madura + Mo Bhasin, Alix Partners",
      "author": "Kevin Madura + Mo Bhasin, Alix Partners",
      "last_modified": "2025-07-23T15:50:35Z",
      "analysis_file": "analysis/Wv1tAxKYLeE.json"
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

# Use fixed validated label vocabularies for repeatable classification

## What

Use fixed validated label vocabularies for repeatable classification

Business-defined labels and structured outputs constrain categorization and make mistakes measurable rather than generating free-form categories each run.

## Evidence

> factors, and you have to categorize it into a taxonomy. Here the taxonomy would
> — 08:29 [^Wv1tAxKYLeE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Wv1tAxKYLeE]: [The Billable Hour is Dead; Long Live the Billable Hour — Kevin Madura + Mo Bhasin, Alix Partners](https://www.youtube.com/watch?v=Wv1tAxKYLeE); publication: 2025-07-23T15:50:35Z; analysis: `analysis/Wv1tAxKYLeE.json`.
