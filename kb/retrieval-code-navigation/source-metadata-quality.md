---
{
  "type": "technique",
  "id": "source-metadata-quality",
  "title": "Measure and improve metadata quality used to filter and join retrieved evidence",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2025-12-23T17:45:00Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LU9KgcZDRfY",
      "resource": "https://www.youtube.com/watch?v=LU9KgcZDRfY",
      "title": "Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual",
      "author": "Asaf Bord, Northwestern Mutual",
      "last_modified": "2025-12-23T17:45:00Z",
      "analysis_file": "analysis/LU9KgcZDRfY.json"
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

# Measure and improve metadata quality used to filter and join retrieved evidence

## What

Measure and improve metadata quality used to filter and join retrieved evidence

A/B tested LLM performance on a database with good metadata vs poor metadata to prove enrichment value quantitatively.

## Evidence

Source analysis [^LU9KgcZDRfY]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LU9KgcZDRfY]: [Small Bets, Big Impact Building GenBI at a Fortune 100 – Asaf Bord, Northwestern Mutual](https://www.youtube.com/watch?v=LU9KgcZDRfY); publication: 2025-12-23T17:45:00Z; analysis: `analysis/LU9KgcZDRfY.json`.
