---
{
  "type": "technique",
  "id": "shared-volume-boundaries",
  "title": "Share immutable base data, not mutable or secret-bearing workspaces across sandboxes",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2025-07-24T14:15:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "e9sLVMN76qU",
      "resource": "https://www.youtube.com/watch?v=e9sLVMN76qU",
      "title": "AX is the only Experience that Matters - Ivan Burazin, Daytona",
      "author": "Ivan Burazin, Daytona",
      "last_modified": "2025-07-24T14:15:04Z",
      "analysis_file": "analysis/e9sLVMN76qU.json"
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

# Share immutable base data, not mutable or secret-bearing workspaces across sandboxes

## What

Share immutable base data, not mutable or secret-bearing workspaces across sandboxes

Large datasets are uploaded once to a volume and mounted as a network drive into every sandbox, avoiding repeated S3 download/upload per environment.

## Evidence

Source analysis [^e9sLVMN76qU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^e9sLVMN76qU]: [AX is the only Experience that Matters - Ivan Burazin, Daytona](https://www.youtube.com/watch?v=e9sLVMN76qU); publication: 2025-07-24T14:15:04Z; analysis: `analysis/e9sLVMN76qU.json`.
