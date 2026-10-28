---
{
  "type": "technique",
  "id": "unknown-failure-discovery",
  "title": "Cluster unclassified production symptoms to discover missing failure categories",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-04-28T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "_fQ7Z_Wfouk",
      "resource": "https://www.youtube.com/watch?v=_fQ7Z_Wfouk",
      "title": "Why building eval platforms is hard — Phil Hetzel, Braintrust",
      "author": "Phil Hetzel, Braintrust",
      "last_modified": "2026-04-28T16:00:06Z",
      "analysis_file": "analysis/_fQ7Z_Wfouk.json"
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

# Cluster unclassified production symptoms to discover missing failure categories

## What

Cluster unclassified production symptoms to discover missing failure categories

Instead of making humans read all traces, they cluster/topic-model production data to tell you how the agent is actually being used and where to spend engineering time.

## Evidence

Source analysis [^_fQ7Z_Wfouk]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^_fQ7Z_Wfouk]: [Why building eval platforms is hard — Phil Hetzel, Braintrust](https://www.youtube.com/watch?v=_fQ7Z_Wfouk); publication: 2026-04-28T16:00:06Z; analysis: `analysis/_fQ7Z_Wfouk.json`.
