---
{
  "type": "technique",
  "id": "optimization-accounting",
  "title": "Classify avoidable work into eliminate, share, move or defer before increasing inference",
  "area": "cost-caching",
  "status": "stable",
  "valid_from": "2026-09-19T15:00:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7c9FSUVcXR0",
      "resource": "https://www.youtube.com/watch?v=7c9FSUVcXR0",
      "title": "Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta",
      "author": "Nishant Gupta & Naman Ahuja, Meta",
      "last_modified": "2026-09-19T15:00:10Z",
      "analysis_file": "analysis/7c9FSUVcXR0.json"
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

# Classify avoidable work into eliminate, share, move or defer before increasing inference

## What

Classify avoidable work into eliminate, share, move or defer before increasing inference

## Evidence

Source analysis [^7c9FSUVcXR0]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable repeated work and improve usage attribution
- **Speed:** Reuse valid prior computation
- **Quality:** Do not trade correctness for superficial token reduction
- **Reliability:** Version- and policy-correct cache/budget decisions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7c9FSUVcXR0]: [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](https://www.youtube.com/watch?v=7c9FSUVcXR0); publication: 2026-09-19T15:00:10Z; analysis: `analysis/7c9FSUVcXR0.json`.
