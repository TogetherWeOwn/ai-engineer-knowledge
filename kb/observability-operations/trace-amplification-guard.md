---
{
  "type": "technique",
  "id": "trace-amplification-guard",
  "title": "Prevent recursive self-ingestion and duplicated trace-context amplification",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-05-10T19:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "esY99nYXxR4",
      "resource": "https://www.youtube.com/watch?v=esY99nYXxR4",
      "title": "How we solved Context Management in Agents — Sally-Ann Delucia",
      "author": "Sally-Ann Delucia",
      "last_modified": "2026-05-10T19:00:06Z",
      "analysis_file": "analysis/esY99nYXxR4.json"
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

# Prevent recursive self-ingestion and duplicated trace-context amplification

## What

Prevent recursive self-ingestion and duplicated trace-context amplification

An agent analyzing its own growing traces can add enough new trace data on retries to recreate the same context overflow indefinitely.

## Evidence

Source analysis [^esY99nYXxR4]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^esY99nYXxR4]: [How we solved Context Management in Agents — Sally-Ann Delucia](https://www.youtube.com/watch?v=esY99nYXxR4); publication: 2026-05-10T19:00:06Z; analysis: `analysis/esY99nYXxR4.json`.
