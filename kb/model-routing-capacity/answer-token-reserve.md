---
{
  "type": "technique",
  "id": "answer-token-reserve",
  "title": "Reserve output capacity and detect reasoning-only exhaustion",
  "area": "model-routing-capacity",
  "status": "stable",
  "valid_from": "2026-09-09T15:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "8EQo4J2BWKw",
      "resource": "https://www.youtube.com/watch?v=8EQo4J2BWKw",
      "title": "Thinking Deeper in Gemini — Jack Rae, Google DeepMind",
      "author": "Jack Rae, Google DeepMind",
      "last_modified": "2025-07-10T16:00:06Z",
      "analysis_file": "analysis/8EQo4J2BWKw.json"
    },
    {
      "id": "XzJD1bvXKjs",
      "resource": "https://www.youtube.com/watch?v=XzJD1bvXKjs",
      "title": "How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-09-09T15:00:06Z",
      "analysis_file": "analysis/XzJD1bvXKjs.json"
    },
    {
      "id": "Z-c11pV_uvU",
      "resource": "https://www.youtube.com/watch?v=Z-c11pV_uvU",
      "title": "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley",
      "author": "Frank Coyle, UC Berkeley",
      "last_modified": "2026-08-08T16:00:06Z",
      "analysis_file": "analysis/Z-c11pV_uvU.json"
    },
    {
      "id": "aqW68Is_Kj4",
      "resource": "https://www.youtube.com/watch?v=aqW68Is_Kj4",
      "title": "Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic",
      "author": "Evolving Claude APIs for Agents, Anthropic",
      "last_modified": "2025-12-04T20:14:55Z",
      "analysis_file": "analysis/aqW68Is_Kj4.json"
    },
    {
      "id": "g03m-WFEu1U",
      "resource": "https://www.youtube.com/watch?v=g03m-WFEu1U",
      "title": "How to Improve your Vibe Coding — Ian Butler",
      "author": "Ian Butler",
      "last_modified": "2025-08-03T04:32:57Z",
      "analysis_file": "analysis/g03m-WFEu1U.json"
    },
    {
      "id": "qLqttdO33UM",
      "resource": "https://www.youtube.com/watch?v=qLqttdO33UM",
      "title": "Vision: Zero Bugs — Johann Schleier-Smith, Temporal",
      "author": "Johann Schleier-Smith, Temporal",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qLqttdO33UM.json"
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

# Reserve output capacity and detect reasoning-only exhaustion

## What

Reserve output capacity and detect reasoning-only exhaustion

Reasoning can consume the full generation budget while producing little useful answer; completion budgeting must distinguish thinking from deliverables.

## Evidence

Source analysis [^8EQo4J2BWKw]; no independently matched timestamped quote published.

> uses its entire token budget thinking. And then it doesn't give any output.
> — 11:50 [^XzJD1bvXKjs]

> but if you have run out of tokens, then you need to take action.
> — 11:08 [^Z-c11pV_uvU]

Source analysis [^aqW68Is_Kj4]; no independently matched timestamped quote published.

> Um, thinking models were significantly better um at finding bugs in a codebase.
> — 02:50 [^g03m-WFEu1U]

Source analysis [^qLqttdO33UM]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Use the cheapest evidenced capable mechanism
- **Speed:** Admit work within real quota and resource limits
- **Quality:** Preserve the role quality floor
- **Reliability:** Avoid exhaustion, unsafe fallback and policy bypass
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^8EQo4J2BWKw]: [Thinking Deeper in Gemini — Jack Rae, Google DeepMind](https://www.youtube.com/watch?v=8EQo4J2BWKw); publication: 2025-07-10T16:00:06Z; analysis: `analysis/8EQo4J2BWKw.json`.
[^XzJD1bvXKjs]: [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs); publication: 2026-09-09T15:00:06Z; analysis: `analysis/XzJD1bvXKjs.json`.
[^Z-c11pV_uvU]: [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley](https://www.youtube.com/watch?v=Z-c11pV_uvU); publication: 2026-08-08T16:00:06Z; analysis: `analysis/Z-c11pV_uvU.json`.
[^aqW68Is_Kj4]: [Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic](https://www.youtube.com/watch?v=aqW68Is_Kj4); publication: 2025-12-04T20:14:55Z; analysis: `analysis/aqW68Is_Kj4.json`.
[^g03m-WFEu1U]: [How to Improve your Vibe Coding — Ian Butler](https://www.youtube.com/watch?v=g03m-WFEu1U); publication: 2025-08-03T04:32:57Z; analysis: `analysis/g03m-WFEu1U.json`.
[^qLqttdO33UM]: [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](https://www.youtube.com/watch?v=qLqttdO33UM); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qLqttdO33UM.json`.
