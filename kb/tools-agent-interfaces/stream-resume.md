---
{
  "type": "technique",
  "id": "stream-resume",
  "title": "Reconnect result streams using run IDs and cursors without restarting execution",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-01-06T16:00:07Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "kmV-qg4uoNI",
      "resource": "https://www.youtube.com/watch?v=kmV-qg4uoNI",
      "title": "Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel",
      "author": "Peter Wielander, Vercel",
      "last_modified": "2026-01-06T16:00:07Z",
      "analysis_file": "analysis/kmV-qg4uoNI.json"
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

# Reconnect result streams using run IDs and cursors without restarting execution

## What

Reconnect result streams using run IDs and cursors without restarting execution

Store output independently of an HTTP handler and resume from a chunk index after client disconnection.

## Evidence

> return the same stream that we return in the other endpoint
> — 25:39 [^kmV-qg4uoNI]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^kmV-qg4uoNI]: [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](https://www.youtube.com/watch?v=kmV-qg4uoNI); publication: 2026-01-06T16:00:07Z; analysis: `analysis/kmV-qg4uoNI.json`.
