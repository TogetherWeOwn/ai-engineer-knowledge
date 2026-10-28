---
{
  "type": "technique",
  "id": "deterministic-search",
  "title": "Prefer bounded cheap exhaustive search when correctness can be checked deterministically",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-05-29T14:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "V-L0INGTEOg",
      "resource": "https://www.youtube.com/watch?v=V-L0INGTEOg",
      "title": "Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs",
      "author": "Boris Starkov, Eleven Labs",
      "last_modified": "2026-05-29T14:00:06Z",
      "analysis_file": "analysis/V-L0INGTEOg.json"
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

# Prefer bounded cheap exhaustive search when correctness can be checked deterministically

## What

Prefer bounded cheap exhaustive search when correctness can be checked deterministically

Rather than reasoning about the checksum, the agent brute-forced the one-byte value and confirmed it empirically.

## Evidence

Source analysis [^V-L0INGTEOg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^V-L0INGTEOg]: [Reverse engineering a Viking VOIP phone protocol with Claude Code — Boris Starkov, Eleven Labs](https://www.youtube.com/watch?v=V-L0INGTEOg); publication: 2026-05-29T14:00:06Z; analysis: `analysis/V-L0INGTEOg.json`.
