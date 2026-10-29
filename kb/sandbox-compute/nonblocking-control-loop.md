---
{
  "type": "technique",
  "id": "nonblocking-control-loop",
  "title": "Move blocking I/O and expensive command work off the control loop through supported boundaries",
  "area": "sandbox-compute",
  "status": "stable",
  "valid_from": "2025-08-25T15:00:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "bCGbuyv8PMk",
      "resource": "https://www.youtube.com/watch?v=bCGbuyv8PMk",
      "title": "Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems",
      "author": "Challenges in High Performance Robotics Systems",
      "last_modified": "2025-08-25T15:00:05Z",
      "analysis_file": "analysis/bCGbuyv8PMk.json"
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

# Move blocking I/O and expensive command work off the control loop through supported boundaries

## What

Move blocking I/O and expensive command work off the control loop through supported boundaries

Logging to disk froze the control loop for 30ms on a Raspberry Pi; they added a third CPU dedicated to logging so the real-time loop never blocks on disk.

## Evidence

Source analysis [^bCGbuyv8PMk]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable idle and duplicated compute
- **Speed:** Reduce measured execution/queue bottlenecks
- **Quality:** Reproducible command and environment evidence
- **Reliability:** Isolation, cleanup and recovery guarantees
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^bCGbuyv8PMk]: [Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems](https://www.youtube.com/watch?v=bCGbuyv8PMk); publication: 2025-08-25T15:00:05Z; analysis: `analysis/bCGbuyv8PMk.json`.
