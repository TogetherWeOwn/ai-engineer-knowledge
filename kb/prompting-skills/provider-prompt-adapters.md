---
{
  "type": "technique",
  "id": "provider-prompt-adapters",
  "title": "Adapt prompt formatting to actual endpoint behavior while retaining provider-independent task policy",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-06-06T16:00:00Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Bf71xMwd-Y0",
      "resource": "https://www.youtube.com/watch?v=Bf71xMwd-Y0",
      "title": "Buy Now, Maybe Pay Later: Dealing with Prompt-Tax While Staying at the Frontier - Andrew Thomspson",
      "author": "Andrew Thomspson",
      "last_modified": "2025-06-03T22:22:25Z",
      "analysis_file": "analysis/Bf71xMwd-Y0.json"
    },
    {
      "id": "QuuIywMG4s8",
      "resource": "https://www.youtube.com/watch?v=QuuIywMG4s8",
      "title": "Evals Are Broken, Use Them Anyway — Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-06-06T16:00:00Z",
      "analysis_file": "analysis/QuuIywMG4s8.json"
    },
    {
      "id": "Wmp2Tku2PrI",
      "resource": "https://www.youtube.com/watch?v=Wmp2Tku2PrI",
      "title": "Vibe Engineering Effect Apps — Michael Arnaldi, Effectful",
      "author": "Michael Arnaldi, Effectful",
      "last_modified": "2026-05-07T15:00:06Z",
      "analysis_file": "analysis/Wmp2Tku2PrI.json"
    },
    {
      "id": "qdmxApz3EJI",
      "resource": "https://www.youtube.com/watch?v=qdmxApz3EJI",
      "title": "On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks",
      "author": "Omar Khattab, DSPy & Databricks",
      "last_modified": "2025-08-06T16:15:49Z",
      "analysis_file": "analysis/qdmxApz3EJI.json"
    },
    {
      "id": "wVl6ZjELpBk",
      "resource": "https://www.youtube.com/watch?v=wVl6ZjELpBk",
      "title": "Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI",
      "author": "Bill Chen & Brian Fioca, OpenAI",
      "last_modified": "2025-12-05T17:00:06Z",
      "analysis_file": "analysis/wVl6ZjELpBk.json"
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

# Adapt prompt formatting to actual endpoint behavior while retaining provider-independent task policy

## What

Adapt prompt formatting to actual endpoint behavior while retaining provider-independent task policy

Nuanced instructions, formatting and tool contracts can differ across families, so a good model may be underused by the wrong harness.

## Evidence

Source analysis [^Bf71xMwd-Y0]; no independently matched timestamped quote published.

> be very different from Gemini model family. And those are the nuance of like
> — 16:18 [^QuuIywMG4s8]

> and then be passive and like agree on everything.
> — 1:01:04 [^Wmp2Tku2PrI]

Source analysis [^qdmxApz3EJI]; no independently matched timestamped quote published.

Source analysis [^wVl6ZjELpBk]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Bf71xMwd-Y0]: [Buy Now, Maybe Pay Later: Dealing with Prompt-Tax While Staying at the Frontier - Andrew Thomspson](https://www.youtube.com/watch?v=Bf71xMwd-Y0); publication: 2025-06-03T22:22:25Z; analysis: `analysis/Bf71xMwd-Y0.json`.
[^QuuIywMG4s8]: [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8); publication: 2026-06-06T16:00:00Z; analysis: `analysis/QuuIywMG4s8.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^qdmxApz3EJI]: [On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks](https://www.youtube.com/watch?v=qdmxApz3EJI); publication: 2025-08-06T16:15:49Z; analysis: `analysis/qdmxApz3EJI.json`.
[^wVl6ZjELpBk]: [Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI](https://www.youtube.com/watch?v=wVl6ZjELpBk); publication: 2025-12-05T17:00:06Z; analysis: `analysis/wVl6ZjELpBk.json`.
