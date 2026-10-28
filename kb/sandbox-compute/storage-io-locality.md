---
{
  "type": "technique",
  "id": "storage-io-locality",
  "title": "Use filesystem and storage measurements to reduce build I/O overhead",
  "area": "sandbox-compute",
  "status": "stable",
  "valid_from": "2026-07-13T17:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OqM67QG_Ikk",
      "resource": "https://www.youtube.com/watch?v=OqM67QG_Ikk",
      "title": "From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI",
      "author": "Abhishek Bhardwaj, OpenAI",
      "last_modified": "2026-07-13T17:00:06Z",
      "analysis_file": "analysis/OqM67QG_Ikk.json"
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

# Use filesystem and storage measurements to reduce build I/O overhead

## What

Use filesystem and storage measurements to reduce build I/O overhead

Guest-native block devices can use guest caches and avoid exiting to the host on every shared-folder filesystem operation; tiered persistence trades latency against durability.

## Evidence

> you give a block device to the micro VM and it is way more efficient
> — 37:07 [^OqM67QG_Ikk]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable idle and duplicated compute
- **Speed:** Reduce measured execution/queue bottlenecks
- **Quality:** Reproducible command and environment evidence
- **Reliability:** Isolation, cleanup and recovery guarantees
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OqM67QG_Ikk]: [From fork() to Fleet: Designing an Agent Sandbox Cloud — Abhishek Bhardwaj, OpenAI](https://www.youtube.com/watch?v=OqM67QG_Ikk); publication: 2026-07-13T17:00:06Z; analysis: `analysis/OqM67QG_Ikk.json`.
