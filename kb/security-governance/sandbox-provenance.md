---
{
  "type": "technique",
  "id": "sandbox-provenance",
  "title": "Verify execution provenance and prevent forbidden hidden delegation",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-06T00:30:15Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OE_lLNCNfQo",
      "resource": "https://www.youtube.com/watch?v=OE_lLNCNfQo",
      "title": "YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker",
      "author": "Rowan Christmas, Docker",
      "last_modified": "2026-10-03T00:30:06Z",
      "analysis_file": "analysis/OE_lLNCNfQo.json"
    },
    {
      "id": "Rx8f05JI_WA",
      "resource": "https://www.youtube.com/watch?v=Rx8f05JI_WA",
      "title": "SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI",
      "author": "Rishi Desai, Abundant AI",
      "last_modified": "2026-07-07T03:45:51Z",
      "analysis_file": "analysis/Rx8f05JI_WA.json"
    },
    {
      "id": "ZUZVNKFSmTM",
      "resource": "https://www.youtube.com/watch?v=ZUZVNKFSmTM",
      "title": "How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker",
      "author": "Jim Clark, Docker",
      "last_modified": "2026-10-06T00:30:15Z",
      "analysis_file": "analysis/ZUZVNKFSmTM.json"
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

# Verify execution provenance and prevent forbidden hidden delegation

## What

Verify execution provenance and prevent forbidden hidden delegation

Matching output is insufficient when the implementation secretly calls a prohibited external solver.

## Evidence

Source analysis [^OE_lLNCNfQo]; no independently matched timestamped quote published.

> by using S trace to find the forbidden subprocesses
> — 11:00 [^Rx8f05JI_WA]

Source analysis [^ZUZVNKFSmTM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OE_lLNCNfQo]: [YOLO Mode, Safely: MicroVM Sandboxes for Any Agent — Rowan Christmas, Docker](https://www.youtube.com/watch?v=OE_lLNCNfQo); publication: 2026-10-03T00:30:06Z; analysis: `analysis/OE_lLNCNfQo.json`.
[^Rx8f05JI_WA]: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA); publication: 2026-07-07T03:45:51Z; analysis: `analysis/Rx8f05JI_WA.json`.
[^ZUZVNKFSmTM]: [How Many Credentials Should Your AI Agent Have? Zero. — Jim Clark, Docker](https://www.youtube.com/watch?v=ZUZVNKFSmTM); publication: 2026-10-06T00:30:15Z; analysis: `analysis/ZUZVNKFSmTM.json`.
