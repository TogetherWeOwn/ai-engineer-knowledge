---
{
  "type": "technique",
  "id": "least-privilege-output",
  "title": "Return only the minimum authorized endpoint information needed for the task",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2025-02-08T21:31:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "GVbPiq3Pet0",
      "resource": "https://www.youtube.com/watch?v=GVbPiq3Pet0",
      "title": "Building security around ML: Dr. Andrew Davis",
      "author": null,
      "last_modified": "2025-02-08T21:31:25Z",
      "analysis_file": "analysis/GVbPiq3Pet0.json"
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

# Return only the minimum authorized endpoint information needed for the task

## What

Return only the minimum authorized endpoint information needed for the task

Return only the bare minimum output (hard label instead of logits/soft scores) so attackers can't cheaply distill a surrogate model from query responses.

## Evidence

Source analysis [^GVbPiq3Pet0]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^GVbPiq3Pet0]: [Building security around ML: Dr. Andrew Davis](https://www.youtube.com/watch?v=GVbPiq3Pet0); publication: 2025-02-08T21:31:25Z; analysis: `analysis/GVbPiq3Pet0.json`.
