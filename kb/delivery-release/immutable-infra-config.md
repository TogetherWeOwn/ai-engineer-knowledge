---
{
  "type": "technique",
  "id": "immutable-infra-config",
  "title": "Keep deploy configuration and runtime flags versioned, inspectable and rollbackable",
  "area": "delivery-release",
  "status": "stable",
  "valid_from": "2026-09-14T14:30:38Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "gxVZ_1tuuq4",
      "resource": "https://www.youtube.com/watch?v=gxVZ_1tuuq4",
      "title": "Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS",
      "author": "Mike Chambers, AWS",
      "last_modified": "2026-09-14T14:30:38Z",
      "analysis_file": "analysis/gxVZ_1tuuq4.json"
    },
    {
      "id": "qqrk7CtkuIw",
      "resource": "https://www.youtube.com/watch?v=qqrk7CtkuIw",
      "title": "How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic",
      "author": "Mike Krieger, Anthropic",
      "last_modified": "2026-08-27T16:00:06Z",
      "analysis_file": "analysis/qqrk7CtkuIw.json"
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

# Keep deploy configuration and runtime flags versioned, inspectable and rollbackable

## What

Keep deploy configuration and runtime flags versioned, inspectable and rollbackable

Have agents generate infrastructure-as-code rather than directly clicking/creating cloud resources, preserving owned, reviewable deployments.

## Evidence

Source analysis [^gxVZ_1tuuq4]; no independently matched timestamped quote published.

Source analysis [^qqrk7CtkuIw]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid failed cutover and repeated integration work
- **Speed:** Shorter safe automated promotion
- **Quality:** Release the actual tested artifact
- **Reliability:** Staging, provenance and rollback contain regressions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^gxVZ_1tuuq4]: [Harness Engineering: Building the Production Cage for Powerful Domain Agents — Mike Chambers, AWS](https://www.youtube.com/watch?v=gxVZ_1tuuq4); publication: 2026-09-14T14:30:38Z; analysis: `analysis/gxVZ_1tuuq4.json`.
[^qqrk7CtkuIw]: [How Anthropic Builds: Lessons from Labs — Mike Krieger, Anthropic](https://www.youtube.com/watch?v=qqrk7CtkuIw); publication: 2026-08-27T16:00:06Z; analysis: `analysis/qqrk7CtkuIw.json`.
