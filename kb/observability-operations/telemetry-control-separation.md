---
{
  "type": "technique",
  "id": "telemetry-control-separation",
  "title": "Separate telemetry transport from evaluation and orchestration control paths",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-08-28T15:00:03Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KVgbERRPU4M",
      "resource": "https://www.youtube.com/watch?v=KVgbERRPU4M",
      "title": "OpenLLMetry is all you need",
      "author": null,
      "last_modified": "2025-02-22T19:00:05Z",
      "analysis_file": "analysis/KVgbERRPU4M.json"
    },
    {
      "id": "bMjlRrWjdT0",
      "resource": "https://www.youtube.com/watch?v=bMjlRrWjdT0",
      "title": "AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "author": "Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "last_modified": "2026-08-28T15:00:03Z",
      "analysis_file": "analysis/bMjlRrWjdT0.json"
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

# Separate telemetry transport from evaluation and orchestration control paths

## What

Separate telemetry transport from evaluation and orchestration control paths

Keep raw traces, scores and observations available independently of the interface used to annotate or review them.

## Evidence

Source analysis [^KVgbERRPU4M]; no independently matched timestamped quote published.

Source analysis [^bMjlRrWjdT0]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KVgbERRPU4M]: [OpenLLMetry is all you need](https://www.youtube.com/watch?v=KVgbERRPU4M); publication: 2025-02-22T19:00:05Z; analysis: `analysis/KVgbERRPU4M.json`.
[^bMjlRrWjdT0]: [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](https://www.youtube.com/watch?v=bMjlRrWjdT0); publication: 2026-08-28T15:00:03Z; analysis: `analysis/bMjlRrWjdT0.json`.
