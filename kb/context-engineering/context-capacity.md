---
{
  "type": "technique",
  "id": "context-capacity",
  "title": "Use the actual served context capacity and preserve full-source reads when required",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-10-14T15:00:14Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "3E7VAZaTG9M",
      "resource": "https://www.youtube.com/watch?v=3E7VAZaTG9M",
      "title": "Scaling AI in Education: A Khanmigo case study: Shawn Jansepar",
      "author": null,
      "last_modified": "2025-02-05T02:56:08Z",
      "analysis_file": "analysis/3E7VAZaTG9M.json"
    },
    {
      "id": "8g1N_a3h9H0",
      "resource": "https://www.youtube.com/watch?v=8g1N_a3h9H0",
      "title": "How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival",
      "author": "Alvin Pane, OutRival",
      "last_modified": "2026-10-14T15:00:14Z",
      "analysis_file": "analysis/8g1N_a3h9H0.json"
    },
    {
      "id": "D6v5rlqUIc8",
      "resource": "https://www.youtube.com/watch?v=D6v5rlqUIc8",
      "title": "Keynote: Why people think \"agent\" is a buzzword but it isn't",
      "author": null,
      "last_modified": "2025-02-22T14:00:06Z",
      "analysis_file": "analysis/D6v5rlqUIc8.json"
    },
    {
      "id": "GgLQ02aO-hs",
      "resource": "https://www.youtube.com/watch?v=GgLQ02aO-hs",
      "title": "The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller",
      "author": "Maxime Rivest & Isaac Miller",
      "last_modified": "2026-07-23T17:45:06Z",
      "analysis_file": "analysis/GgLQ02aO-hs.json"
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
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "c5qJHr3DnT4",
      "resource": "https://www.youtube.com/watch?v=c5qJHr3DnT4",
      "title": "GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft",
      "author": "Jonathan Larson, Microsoft",
      "last_modified": "2025-06-27T09:48:38Z",
      "analysis_file": "analysis/c5qJHr3DnT4.json"
    },
    {
      "id": "nbZzSC5A6hs",
      "resource": "https://www.youtube.com/watch?v=nbZzSC5A6hs",
      "title": "Lessons from the Trenches: Building LLM Evals That Work IRL: Aparna Dhinkaran",
      "author": null,
      "last_modified": "2025-02-06T09:24:01Z",
      "analysis_file": "analysis/nbZzSC5A6hs.json"
    },
    {
      "id": "ro5HkZvzfiQ",
      "resource": "https://www.youtube.com/watch?v=ro5HkZvzfiQ",
      "title": "The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:",
      "author": "Almog Baku:",
      "last_modified": "2025-02-22T15:00:06Z",
      "analysis_file": "analysis/ro5HkZvzfiQ.json"
    },
    {
      "id": "tbDDYKRFjhk",
      "resource": "https://www.youtube.com/watch?v=tbDDYKRFjhk",
      "title": "Does AI Actually Boost Developer Productivity? (100k Devs Study) - Yegor Denisov-Blanch, Stanford",
      "author": "Yegor Denisov-Blanch, Stanford",
      "last_modified": "2025-07-23T17:00:06Z",
      "analysis_file": "analysis/tbDDYKRFjhk.json"
    },
    {
      "id": "vSx5IULvBns",
      "resource": "https://www.youtube.com/watch?v=vSx5IULvBns",
      "title": "Always-on agents run production without the on-call tax — Justin Smith, Resolve AI",
      "author": "Justin Smith, Resolve AI",
      "last_modified": "2026-08-09T14:45:06Z",
      "analysis_file": "analysis/vSx5IULvBns.json"
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

# Use the actual served context capacity and preserve full-source reads when required

## What

Use the actual served context capacity and preserve full-source reads when required

Tracking named constraints is different from resolving ambiguity, contradictions and long-context reasoning degradation.

## Evidence

Source analysis [^3E7VAZaTG9M]; no independently matched timestamped quote published.

Source analysis [^8g1N_a3h9H0]; no independently matched timestamped quote published.

Source analysis [^D6v5rlqUIc8]; no independently matched timestamped quote published.

Source analysis [^GgLQ02aO-hs]; no independently matched timestamped quote published.

> instructions, but it's not necessarily going to uh reason clearly over them.
> — 17:42 [^XzJD1bvXKjs]

> some providers choose to deliver a different size, a smaller size, for
> — 18:50 [^YIxzNZDDy1A]

Source analysis [^c5qJHr3DnT4]; no independently matched timestamped quote published.

> really hard time almost remembering or retrieving to pull that document and so
> — 15:38 [^nbZzSC5A6hs]

> with the right answer so we need to find the right
> — 22:34 [^ro5HkZvzfiQ]

Source analysis [^tbDDYKRFjhk]; no independently matched timestamped quote published.

Source analysis [^vSx5IULvBns]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^3E7VAZaTG9M]: [Scaling AI in Education: A Khanmigo case study: Shawn Jansepar](https://www.youtube.com/watch?v=3E7VAZaTG9M); publication: 2025-02-05T02:56:08Z; analysis: `analysis/3E7VAZaTG9M.json`.
[^8g1N_a3h9H0]: [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](https://www.youtube.com/watch?v=8g1N_a3h9H0); publication: 2026-10-14T15:00:14Z; analysis: `analysis/8g1N_a3h9H0.json`.
[^D6v5rlqUIc8]: [Keynote: Why people think "agent" is a buzzword but it isn't](https://www.youtube.com/watch?v=D6v5rlqUIc8); publication: 2025-02-22T14:00:06Z; analysis: `analysis/D6v5rlqUIc8.json`.
[^GgLQ02aO-hs]: [The Unreasonable Effectiveness of Separating the Task from the Model — Maxime Rivest & Isaac Miller](https://www.youtube.com/watch?v=GgLQ02aO-hs); publication: 2026-07-23T17:45:06Z; analysis: `analysis/GgLQ02aO-hs.json`.
[^XzJD1bvXKjs]: [How long can your skills be before your agent forgets what you told it? — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=XzJD1bvXKjs); publication: 2026-09-09T15:00:06Z; analysis: `analysis/XzJD1bvXKjs.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^c5qJHr3DnT4]: [GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft](https://www.youtube.com/watch?v=c5qJHr3DnT4); publication: 2025-06-27T09:48:38Z; analysis: `analysis/c5qJHr3DnT4.json`.
[^nbZzSC5A6hs]: [Lessons from the Trenches: Building LLM Evals That Work IRL: Aparna Dhinkaran](https://www.youtube.com/watch?v=nbZzSC5A6hs); publication: 2025-02-06T09:24:01Z; analysis: `analysis/nbZzSC5A6hs.json`.
[^ro5HkZvzfiQ]: [The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:](https://www.youtube.com/watch?v=ro5HkZvzfiQ); publication: 2025-02-22T15:00:06Z; analysis: `analysis/ro5HkZvzfiQ.json`.
[^tbDDYKRFjhk]: [Does AI Actually Boost Developer Productivity? (100k Devs Study) - Yegor Denisov-Blanch, Stanford](https://www.youtube.com/watch?v=tbDDYKRFjhk); publication: 2025-07-23T17:00:06Z; analysis: `analysis/tbDDYKRFjhk.json`.
[^vSx5IULvBns]: [Always-on agents run production without the on-call tax — Justin Smith, Resolve AI](https://www.youtube.com/watch?v=vSx5IULvBns); publication: 2026-08-09T14:45:06Z; analysis: `analysis/vSx5IULvBns.json`.
