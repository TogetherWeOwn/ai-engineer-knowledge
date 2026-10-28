---
{
  "type": "technique",
  "id": "guest-docker-boundary",
  "title": "Keep Docker privileges inside the approved guest boundary, never expose the host socket",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-07-20T17:17:53Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "LqLoYksJ6do",
      "resource": "https://www.youtube.com/watch?v=LqLoYksJ6do",
      "title": "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3",
      "author": "Moritz Johner, Form3",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/LqLoYksJ6do.json"
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

# Keep Docker privileges inside the approved guest boundary, never expose the host socket

## What

Keep Docker privileges inside the approved guest boundary, never expose the host socket

A host Docker socket defeats a process-level sandbox; builds requiring Docker run with a daemon confined to an isolated VM rather than the control-plane host.

## Evidence

Source analysis [^LqLoYksJ6do]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
