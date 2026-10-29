---
{
  "type": "technique",
  "id": "side-effect-plausibility",
  "title": "Check semantic plausibility and invariants of proposed side effects before execution",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-06-26T20:00:35Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "7_WhRAuP2Wg",
      "resource": "https://www.youtube.com/watch?v=7_WhRAuP2Wg",
      "title": "Building and Scaling an AI Agent Swarm of low latency real time voice bots: Damien Murphy",
      "author": null,
      "last_modified": "2024-10-08T18:28:46Z",
      "analysis_file": "analysis/7_WhRAuP2Wg.json"
    },
    {
      "id": "ij-AU9dpJjc",
      "resource": "https://www.youtube.com/watch?v=ij-AU9dpJjc",
      "title": "Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co",
      "author": "Isadora Martin-Dye, Isadora & Co",
      "last_modified": "2026-06-26T20:00:35Z",
      "analysis_file": "analysis/ij-AU9dpJjc.json"
    },
    {
      "id": "zM9RYqCcioM",
      "resource": "https://www.youtube.com/watch?v=zM9RYqCcioM",
      "title": "Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt",
      "author": "Mustafa Ali & Kyle Corbitt",
      "last_modified": "2025-04-12T16:00:06Z",
      "analysis_file": "analysis/zM9RYqCcioM.json"
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

# Check semantic plausibility and invariants of proposed side effects before execution

## What

Check semantic plausibility and invariants of proposed side effects before execution

Inspect the actual generated output and reject unsupported dates/numbers/promises using authoritative allowlists or typed facts.

## Evidence

Source analysis [^7_WhRAuP2Wg]; no independently matched timestamped quote published.

> against what is real. A date the model offered that isn't in the allow list
> — 16:11 [^ij-AU9dpJjc]

Source analysis [^zM9RYqCcioM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^7_WhRAuP2Wg]: [Building and Scaling an AI Agent Swarm of low latency real time voice bots: Damien Murphy](https://www.youtube.com/watch?v=7_WhRAuP2Wg); publication: 2024-10-08T18:28:46Z; analysis: `analysis/7_WhRAuP2Wg.json`.
[^ij-AU9dpJjc]: [Stop Writing Tone Instructions. Layer Them. - Isadora Martin-Dye, Isadora & Co](https://www.youtube.com/watch?v=ij-AU9dpJjc); publication: 2026-06-26T20:00:35Z; analysis: `analysis/ij-AU9dpJjc.json`.
[^zM9RYqCcioM]: [Finetuning: 500m AI agents in production with 2 engineers — Mustafa Ali & Kyle Corbitt](https://www.youtube.com/watch?v=zM9RYqCcioM); publication: 2025-04-12T16:00:06Z; analysis: `analysis/zM9RYqCcioM.json`.
