---
{
  "type": "technique",
  "id": "decision-boundary-guidance",
  "title": "Place concise procedural guidance at the decision boundary where it is needed",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-09-21T19:00:10Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "3ZMUiFaQ3qg",
      "resource": "https://www.youtube.com/watch?v=3ZMUiFaQ3qg",
      "title": "Verifiable Environments for AI in Biology — Kenny Workman, LatchBio",
      "author": "Kenny Workman, LatchBio",
      "last_modified": "2026-07-31T20:00:35Z",
      "analysis_file": "analysis/3ZMUiFaQ3qg.json"
    },
    {
      "id": "SQMCtZX3trg",
      "resource": "https://www.youtube.com/watch?v=SQMCtZX3trg",
      "title": "The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)",
      "author": "Paul Bakaus, Renaissance Geek (Impeccable)",
      "last_modified": "2026-09-21T19:00:10Z",
      "analysis_file": "analysis/SQMCtZX3trg.json"
    },
    {
      "id": "bjNYEc908oQ",
      "resource": "https://www.youtube.com/watch?v=bjNYEc908oQ",
      "title": "Building Reliable Agentic Systems: Eno Reyes",
      "author": null,
      "last_modified": "2024-08-20T13:44:51Z",
      "analysis_file": "analysis/bjNYEc908oQ.json"
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

# Place concise procedural guidance at the decision boundary where it is needed

## What

Place concise procedural guidance at the decision boundary where it is needed

Targeted external guidance can rescue uncertain trajectories without requiring continuous supervision of every step.

## Evidence

Source analysis [^3ZMUiFaQ3qg]; no independently matched timestamped quote published.

Source analysis [^SQMCtZX3trg]; no independently matched timestamped quote published.

> want to ask the human to interfere or when do we want them to provide guidance
> — 17:26 [^bjNYEc908oQ]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^3ZMUiFaQ3qg]: [Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](https://www.youtube.com/watch?v=3ZMUiFaQ3qg); publication: 2026-07-31T20:00:35Z; analysis: `analysis/3ZMUiFaQ3qg.json`.
[^SQMCtZX3trg]: [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](https://www.youtube.com/watch?v=SQMCtZX3trg); publication: 2026-09-21T19:00:10Z; analysis: `analysis/SQMCtZX3trg.json`.
[^bjNYEc908oQ]: [Building Reliable Agentic Systems: Eno Reyes](https://www.youtube.com/watch?v=bjNYEc908oQ); publication: 2024-08-20T13:44:51Z; analysis: `analysis/bjNYEc908oQ.json`.
