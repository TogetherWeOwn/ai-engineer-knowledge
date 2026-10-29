---
{
  "type": "technique",
  "id": "parameterized-data-access",
  "title": "Parameterize database operations and constrain data access outside model-generated text",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-17T07:00:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KtBivPzmOM8",
      "resource": "https://www.youtube.com/watch?v=KtBivPzmOM8",
      "title": "Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle",
      "author": "Nacho Martinez, Oracle",
      "last_modified": "2026-10-17T07:00:25Z",
      "analysis_file": "analysis/KtBivPzmOM8.json"
    },
    {
      "id": "_Zcw_sVF6hU",
      "resource": "https://www.youtube.com/watch?v=_Zcw_sVF6hU",
      "title": "The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "author": "Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "last_modified": "2026-04-18T10:30:06Z",
      "analysis_file": "analysis/_Zcw_sVF6hU.json"
    },
    {
      "id": "bI8WyG9YB0I",
      "resource": "https://www.youtube.com/watch?v=bI8WyG9YB0I",
      "title": "SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar",
      "author": "Killian Carlsen-Phelan, Sonar",
      "last_modified": "2026-10-11T19:00:11Z",
      "analysis_file": "analysis/bI8WyG9YB0I.json"
    },
    {
      "id": "bmWZk9vTze0",
      "resource": "https://www.youtube.com/watch?v=bmWZk9vTze0",
      "title": "MCP is all you need — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-07-18T18:52:25Z",
      "analysis_file": "analysis/bmWZk9vTze0.json"
    },
    {
      "id": "spxoDAfh5ig",
      "resource": "https://www.youtube.com/watch?v=spxoDAfh5ig",
      "title": "Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked",
      "author": "Peter Werry, Unblocked",
      "last_modified": "2026-10-11T10:00:18Z",
      "analysis_file": "analysis/spxoDAfh5ig.json"
    },
    {
      "id": "vRFqbEzzDsI",
      "resource": "https://www.youtube.com/watch?v=vRFqbEzzDsI",
      "title": "Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza",
      "author": "Julián Duque & Anush Dsouza",
      "last_modified": "2025-06-27T09:38:08Z",
      "analysis_file": "analysis/vRFqbEzzDsI.json"
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

# Parameterize database operations and constrain data access outside model-generated text

## What

Parameterize database operations and constrain data access outside model-generated text

A consistent query interface limits the places an agent must search and enforces shared transaction/security behavior.

## Evidence

Source analysis [^KtBivPzmOM8]; no independently matched timestamped quote published.

> But yeah, so we also try to have our SQL uh always in one query interface so that
> — 12:55 [^_Zcw_sVF6hU]

> able to fix this. We get a parameterized query. Wonderful. Um, and this post tool
> — 37:14 [^bI8WyG9YB0I]

> from the SQL um if they're there then we will uh check that the table name is
> — 08:30 [^bmWZk9vTze0]

Source analysis [^spxoDAfh5ig]; no independently matched timestamped quote published.

Source analysis [^vRFqbEzzDsI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KtBivPzmOM8]: [Memory-Aware Agent Harnesses for Anti-Money Laundering — Nacho Martinez, Oracle](https://www.youtube.com/watch?v=KtBivPzmOM8); publication: 2026-10-17T07:00:25Z; analysis: `analysis/KtBivPzmOM8.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^bI8WyG9YB0I]: [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](https://www.youtube.com/watch?v=bI8WyG9YB0I); publication: 2026-10-11T19:00:11Z; analysis: `analysis/bI8WyG9YB0I.json`.
[^bmWZk9vTze0]: [MCP is all you need — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=bmWZk9vTze0); publication: 2025-07-18T18:52:25Z; analysis: `analysis/bmWZk9vTze0.json`.
[^spxoDAfh5ig]: [Beyond RAG: Build a Relational Context Engine from Scratch — Peter Werry, Unblocked](https://www.youtube.com/watch?v=spxoDAfh5ig); publication: 2026-10-11T10:00:18Z; analysis: `analysis/spxoDAfh5ig.json`.
[^vRFqbEzzDsI]: [Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza](https://www.youtube.com/watch?v=vRFqbEzzDsI); publication: 2025-06-27T09:38:08Z; analysis: `analysis/vRFqbEzzDsI.json`.
