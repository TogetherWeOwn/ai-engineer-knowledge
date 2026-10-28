---
{
  "type": "technique",
  "id": "read-before-overwrite",
  "title": "Require a current read or revision check before destructive file replacement",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-01-05T17:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "TqC1qOfiVcQ",
      "resource": "https://www.youtube.com/watch?v=TqC1qOfiVcQ",
      "title": "Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic",
      "author": "Thariq Shihipar, Anthropic",
      "last_modified": "2026-01-05T17:00:06Z",
      "analysis_file": "analysis/TqC1qOfiVcQ.json"
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

# Require a current read or revision check before destructive file replacement

## What

Require a current read or revision check before destructive file replacement

An unseen existing file cannot be safely overwritten; deterministic hooks can require a current read instead of hoping the model remembers.

## Evidence

> file yet. Try reading it first, right?" And that's an example of sort of like a
> — 1:08:33 [^TqC1qOfiVcQ]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^TqC1qOfiVcQ]: [Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic](https://www.youtube.com/watch?v=TqC1qOfiVcQ); publication: 2026-01-05T17:00:06Z; analysis: `analysis/TqC1qOfiVcQ.json`.
