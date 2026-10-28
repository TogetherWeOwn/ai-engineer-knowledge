---
{
  "type": "technique",
  "id": "workflow-observation",
  "title": "Observe the real workflow before choosing an automation boundary",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-10-13T18:00:17Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "RmJ4rTLV_x4",
      "resource": "https://www.youtube.com/watch?v=RmJ4rTLV_x4",
      "title": "Your Support Team Should Ship Code – Lisa Orr, Zapier",
      "author": "Lisa Orr, Zapier",
      "last_modified": "2025-12-16T17:00:06Z",
      "analysis_file": "analysis/RmJ4rTLV_x4.json"
    },
    {
      "id": "gDRCpTMCqEU",
      "resource": "https://www.youtube.com/watch?v=gDRCpTMCqEU",
      "title": "What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad",
      "author": "Soukaïna Abelhad",
      "last_modified": "2026-10-13T18:00:17Z",
      "analysis_file": "analysis/gDRCpTMCqEU.json"
    },
    {
      "id": "kDEvo2__Ijg",
      "resource": "https://www.youtube.com/watch?v=kDEvo2__Ijg",
      "title": "From Copilot to Colleague: Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters",
      "author": "Joel Hron, CTO Thomson Reuters",
      "last_modified": "2025-07-23T12:15:13Z",
      "analysis_file": "analysis/kDEvo2__Ijg.json"
    },
    {
      "id": "ow1we5PzK-o",
      "resource": "https://www.youtube.com/watch?v=ow1we5PzK-o",
      "title": "The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory",
      "author": "Luke Alvoeiro, Factory",
      "last_modified": "2026-05-06T15:00:06Z",
      "analysis_file": "analysis/ow1we5PzK-o.json"
    },
    {
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
    },
    {
      "id": "u6jJcIFDLE4",
      "resource": "https://www.youtube.com/watch?v=u6jJcIFDLE4",
      "title": "Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates",
      "author": "Subbiah Sethuraman and Abhilash Asokan, ZS Associates",
      "last_modified": "2026-07-23T05:00:02Z",
      "analysis_file": "analysis/u6jJcIFDLE4.json"
    },
    {
      "id": "v42opQpCy60",
      "resource": "https://www.youtube.com/watch?v=v42opQpCy60",
      "title": "Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.",
      "author": "Paul Bakaus, Renaissance Geek, Inc.",
      "last_modified": "2026-09-10T15:30:14Z",
      "analysis_file": "analysis/v42opQpCy60.json"
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

# Observe the real workflow before choosing an automation boundary

## What

Observe the real workflow before choosing an automation boundary

Dogfooding and shadowing reveal the actual bottleneck instead of assuming code generation is the slow part.

## Evidence

> the way? What are the phases of the work and how much time is spent?
> — 04:05 [^RmJ4rTLV_x4]

Source analysis [^gDRCpTMCqEU]; no independently matched timestamped quote published.

Source analysis [^kDEvo2__Ijg]; no independently matched timestamped quote published.

> have you burned through. So, using a mission actually, we built
> — 10:43 [^ow1we5PzK-o]

> again uh I can ask uh looking at my uh chat history what repetitive tasks am I
> — 25:01 [^rnDm57Py54A]

> give it just bash and the database. Then give it an actual signal which we
> — 06:40 [^u6jJcIFDLE4]

Source analysis [^v42opQpCy60]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^RmJ4rTLV_x4]: [Your Support Team Should Ship Code – Lisa Orr, Zapier](https://www.youtube.com/watch?v=RmJ4rTLV_x4); publication: 2025-12-16T17:00:06Z; analysis: `analysis/RmJ4rTLV_x4.json`.
[^gDRCpTMCqEU]: [What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad](https://www.youtube.com/watch?v=gDRCpTMCqEU); publication: 2026-10-13T18:00:17Z; analysis: `analysis/gDRCpTMCqEU.json`.
[^kDEvo2__Ijg]: [From Copilot to Colleague: Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters](https://www.youtube.com/watch?v=kDEvo2__Ijg); publication: 2025-07-23T12:15:13Z; analysis: `analysis/kDEvo2__Ijg.json`.
[^ow1we5PzK-o]: [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](https://www.youtube.com/watch?v=ow1we5PzK-o); publication: 2026-05-06T15:00:06Z; analysis: `analysis/ow1we5PzK-o.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
[^u6jJcIFDLE4]: [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](https://www.youtube.com/watch?v=u6jJcIFDLE4); publication: 2026-07-23T05:00:02Z; analysis: `analysis/u6jJcIFDLE4.json`.
[^v42opQpCy60]: [Design at the Speed of Adjectives — Paul Bakaus, Renaissance Geek, Inc.](https://www.youtube.com/watch?v=v42opQpCy60); publication: 2026-09-10T15:30:14Z; analysis: `analysis/v42opQpCy60.json`.
