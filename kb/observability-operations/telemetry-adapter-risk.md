---
{
  "type": "technique",
  "id": "telemetry-adapter-risk",
  "title": "Use supported telemetry hooks and test adapter coverage rather than relying blindly on monkey patches",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2025-02-22T19:00:05Z",
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

# Use supported telemetry hooks and test adapter coverage rather than relying blindly on monkey patches

## What

Use supported telemetry hooks and test adapter coverage rather than relying blindly on monkey patches

Instrumentations monkey-patch the client library (LLM SDK, vector DB client) so spans/metrics are emitted automatically with negligible latency, instead of hand-adding logging in agent code.

## Evidence

Source analysis [^KVgbERRPU4M]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KVgbERRPU4M]: [OpenLLMetry is all you need](https://www.youtube.com/watch?v=KVgbERRPU4M); publication: 2025-02-22T19:00:05Z; analysis: `analysis/KVgbERRPU4M.json`.
