---
{
  "type": "technique",
  "id": "review-incremental",
  "title": "Reuse reviews on unchanged input and review only the delta on new heads",
  "area": "review-quality",
  "status": "stable",
  "valid_from": "2026-10-22T08:00:01Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1EZdpEhwmNc",
      "resource": "https://www.youtube.com/watch?v=1EZdpEhwmNc",
      "title": "Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk",
      "author": "Manoj Nair, Snyk",
      "last_modified": "2026-07-20T17:17:54Z",
      "analysis_file": "analysis/1EZdpEhwmNc.json"
    },
    {
      "id": "H6MrR5NbTZA",
      "resource": "https://www.youtube.com/watch?v=H6MrR5NbTZA",
      "title": "Don’t get one-shotted: Use AI to test, review, merge, and deploy code — Tomas Reimers, Graphite",
      "author": "Tomas Reimers, Graphite",
      "last_modified": "2025-06-27T10:25:04Z",
      "analysis_file": "analysis/H6MrR5NbTZA.json"
    },
    {
      "id": "Se8jHLliLXE",
      "resource": "https://www.youtube.com/watch?v=Se8jHLliLXE",
      "title": "The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX",
      "author": "Justin Reock, DX",
      "last_modified": "2026-09-30T14:30:20Z",
      "analysis_file": "analysis/Se8jHLliLXE.json"
    },
    {
      "id": "_dTF3NpPzGo",
      "resource": "https://www.youtube.com/watch?v=_dTF3NpPzGo",
      "title": "Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI",
      "author": "Louis-François Bouchard, Towards AI",
      "last_modified": "2026-10-22T07:00:28Z",
      "analysis_file": "analysis/_dTF3NpPzGo.json"
    },
    {
      "id": "c_SPW__jF9w",
      "resource": "https://www.youtube.com/watch?v=c_SPW__jF9w",
      "title": "How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada",
      "author": "Nathanael Weill, Air Canada",
      "last_modified": "2026-10-22T08:00:01Z",
      "analysis_file": "analysis/c_SPW__jF9w.json"
    },
    {
      "id": "k2ClBT4aqAg",
      "resource": "https://www.youtube.com/watch?v=k2ClBT4aqAg",
      "title": "We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman",
      "author": "Kamalakannan Nandagopal, Postman",
      "last_modified": "2026-10-08T21:30:19Z",
      "analysis_file": "analysis/k2ClBT4aqAg.json"
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

# Reuse reviews on unchanged input and review only the delta on new heads

## What

Reuse reviews on unchanged input and review only the delta on new heads

Snyk ran the newest models five times on the same vulnerability and found that detection is not repeatable. Their conclusion is that an LLM validator must sit behind deterministic checks and must not be trusted as a single coin flip.

## Evidence

Source analysis [^1EZdpEhwmNc]; no independently matched timestamped quote published.

Source analysis [^H6MrR5NbTZA]; no independently matched timestamped quote published.

Source analysis [^Se8jHLliLXE]; no independently matched timestamped quote published.

Source analysis [^_dTF3NpPzGo]; no independently matched timestamped quote published.

Source analysis [^c_SPW__jF9w]; no independently matched timestamped quote published.

Source analysis [^k2ClBT4aqAg]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer redundant or low-value review rounds
- **Speed:** Shorter evidence-backed review/repair cycles
- **Quality:** Better focus on actionable defects rather than cosmetic scores
- **Reliability:** Independent, revision-bound verification
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1EZdpEhwmNc]: [Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk](https://www.youtube.com/watch?v=1EZdpEhwmNc); publication: 2026-07-20T17:17:54Z; analysis: `analysis/1EZdpEhwmNc.json`.
[^H6MrR5NbTZA]: [Don’t get one-shotted: Use AI to test, review, merge, and deploy code — Tomas Reimers, Graphite](https://www.youtube.com/watch?v=H6MrR5NbTZA); publication: 2025-06-27T10:25:04Z; analysis: `analysis/H6MrR5NbTZA.json`.
[^Se8jHLliLXE]: [The State of AI in Software Development: Data from 400+ Orgs — Justin Reock, DX](https://www.youtube.com/watch?v=Se8jHLliLXE); publication: 2026-09-30T14:30:20Z; analysis: `analysis/Se8jHLliLXE.json`.
[^_dTF3NpPzGo]: [Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=_dTF3NpPzGo); publication: 2026-10-22T07:00:28Z; analysis: `analysis/_dTF3NpPzGo.json`.
[^c_SPW__jF9w]: [How to Test AI Agents When No Benchmark Exists — Nathanael Weill, Air Canada](https://www.youtube.com/watch?v=c_SPW__jF9w); publication: 2026-10-22T08:00:01Z; analysis: `analysis/c_SPW__jF9w.json`.
[^k2ClBT4aqAg]: [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](https://www.youtube.com/watch?v=k2ClBT4aqAg); publication: 2026-10-08T21:30:19Z; analysis: `analysis/k2ClBT4aqAg.json`.
