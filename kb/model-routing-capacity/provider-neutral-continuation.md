---
{
  "type": "technique",
  "id": "provider-neutral-continuation",
  "title": "Keep resumable task state provider-neutral while preserving exact tool and instruction semantics",
  "area": "model-routing-capacity",
  "status": "stable",
  "valid_from": "2026-06-26T01:15:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "jVjt-2g8NMY",
      "resource": "https://www.youtube.com/watch?v=jVjt-2g8NMY",
      "title": "A Genius With Amnesia - Victor Savkin, Nx",
      "author": "Victor Savkin, Nx",
      "last_modified": "2026-06-26T01:15:06Z",
      "analysis_file": "analysis/jVjt-2g8NMY.json"
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

# Keep resumable task state provider-neutral while preserving exact tool and instruction semantics

## What

Keep resumable task state provider-neutral while preserving exact tool and instruction semantics

Keep continuation state independent of any one model's proprietary conversation format so an outage need not discard completed work.

## Evidence

> So, a side note, this is also useful when I want to switch from say Claude to
> — 14:57 [^jVjt-2g8NMY]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Use the cheapest evidenced capable mechanism
- **Speed:** Admit work within real quota and resource limits
- **Quality:** Preserve the role quality floor
- **Reliability:** Avoid exhaustion, unsafe fallback and policy bypass
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^jVjt-2g8NMY]: [A Genius With Amnesia - Victor Savkin, Nx](https://www.youtube.com/watch?v=jVjt-2g8NMY); publication: 2026-06-26T01:15:06Z; analysis: `analysis/jVjt-2g8NMY.json`.
