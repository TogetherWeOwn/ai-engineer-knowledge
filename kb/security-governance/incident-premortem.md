---
{
  "type": "technique",
  "id": "incident-premortem",
  "title": "Run bounded incident premortems against consequential proposed changes",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-14T16:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Wb2v9Phhnns",
      "resource": "https://www.youtube.com/watch?v=Wb2v9Phhnns",
      "title": "Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder",
      "author": "Jiachen Jiang, Coder",
      "last_modified": "2026-10-14T16:00:25Z",
      "analysis_file": "analysis/Wb2v9Phhnns.json"
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

# Run bounded incident premortems against consequential proposed changes

## What

Run bounded incident premortems against consequential proposed changes

Assume a specific destructive-agent or credential incident and trace the actual detection, containment and restore paths to expose missing controls before a real event.

## Evidence

> One suggestion I have for you is to run a premortem with your team. Assume one
> — 30:20 [^Wb2v9Phhnns]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Wb2v9Phhnns]: [Your AI Isn’t the Problem. Your Infrastructure Is. — Jiachen Jiang, Coder](https://www.youtube.com/watch?v=Wb2v9Phhnns); publication: 2026-10-14T16:00:25Z; analysis: `analysis/Wb2v9Phhnns.json`.
