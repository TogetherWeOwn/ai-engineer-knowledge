---
{
  "type": "technique",
  "id": "security-static-analysis",
  "title": "Use static and taint analysis for recurring vulnerability classes before semantic repair",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-11T19:00:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-CnA2lGfymY",
      "resource": "https://www.youtube.com/watch?v=-CnA2lGfymY",
      "title": "\"I've never seen anything scarier than an LLM with tool calls.\" — Erik Meijer aka @HeadinTheBox",
      "author": "Erik Meijer aka @HeadinTheBox",
      "last_modified": "2026-07-13T19:25:09Z",
      "analysis_file": "analysis/-CnA2lGfymY.json"
    },
    {
      "id": "3ySF0I5iE_0",
      "resource": "https://www.youtube.com/watch?v=3ySF0I5iE_0",
      "title": "A Practitioner's Guide to Graphs - Tim Ainge, Good Collective",
      "author": "Tim Ainge, Good Collective",
      "last_modified": "2026-07-18T21:30:06Z",
      "analysis_file": "analysis/3ySF0I5iE_0.json"
    },
    {
      "id": "7JgIS42mz7U",
      "resource": "https://www.youtube.com/watch?v=7JgIS42mz7U",
      "title": "The AI bugpocalypse is here. Now what? - Jack Cable, Corridor",
      "author": "Jack Cable, Corridor",
      "last_modified": "2026-07-12T22:00:09Z",
      "analysis_file": "analysis/7JgIS42mz7U.json"
    },
    {
      "id": "Bdrs3uAX0_M",
      "resource": "https://www.youtube.com/watch?v=Bdrs3uAX0_M",
      "title": "AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph",
      "author": "Dan Adler, Sourcegraph",
      "last_modified": "2026-10-04T19:30:20Z",
      "analysis_file": "analysis/Bdrs3uAX0_M.json"
    },
    {
      "id": "LqLoYksJ6do",
      "resource": "https://www.youtube.com/watch?v=LqLoYksJ6do",
      "title": "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3",
      "author": "Moritz Johner, Form3",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/LqLoYksJ6do.json"
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
      "id": "f3o0-9Dlw3E",
      "resource": "https://www.youtube.com/watch?v=f3o0-9Dlw3E",
      "title": "AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk",
      "author": "Eli Cohen, Snyk",
      "last_modified": "2026-10-07T21:30:34Z",
      "analysis_file": "analysis/f3o0-9Dlw3E.json"
    },
    {
      "id": "rcsliSIy_YU",
      "resource": "https://www.youtube.com/watch?v=rcsliSIy_YU",
      "title": "Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-01-08T16:30:23Z",
      "analysis_file": "analysis/rcsliSIy_YU.json"
    },
    {
      "id": "utTqdQpe39A",
      "resource": "https://www.youtube.com/watch?v=utTqdQpe39A",
      "title": "GitHub's AI Powered Security Platform: Sarah Khalife",
      "author": null,
      "last_modified": "2025-02-08T21:31:24Z",
      "analysis_file": "analysis/utTqdQpe39A.json"
    },
    {
      "id": "yWS0udrIOc8",
      "resource": "https://www.youtube.com/watch?v=yWS0udrIOc8",
      "title": "Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town",
      "author": "Steve Yegge, Gas Town",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/yWS0udrIOc8.json"
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

# Use static and taint analysis for recurring vulnerability classes before semantic repair

## What

Use static and taint analysis for recurring vulnerability classes before semantic repair

Discover actionable vulnerable dependencies, dispatch bounded fixes and verify that dependency/API changes actually remediate them.

## Evidence

Source analysis [^-CnA2lGfymY]; no independently matched timestamped quote published.

Source analysis [^3ySF0I5iE_0]; no independently matched timestamped quote published.

Source analysis [^7JgIS42mz7U]; no independently matched timestamped quote published.

Source analysis [^Bdrs3uAX0_M]; no independently matched timestamped quote published.

Source analysis [^LqLoYksJ6do]; no independently matched timestamped quote published.

Source analysis [^bI8WyG9YB0I]; no independently matched timestamped quote published.

Source analysis [^f3o0-9Dlw3E]; no independently matched timestamped quote published.

> relevant dependency, fix any breaking API changes throughout the codebase, and
> — 36:11 [^rcsliSIy_YU]

Source analysis [^utTqdQpe39A]; no independently matched timestamped quote published.

> them check each other's work, too. Right? If
> — 11:35 [^yWS0udrIOc8]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-CnA2lGfymY]: ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](https://www.youtube.com/watch?v=-CnA2lGfymY); publication: 2026-07-13T19:25:09Z; analysis: `analysis/-CnA2lGfymY.json`.
[^3ySF0I5iE_0]: [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0); publication: 2026-07-18T21:30:06Z; analysis: `analysis/3ySF0I5iE_0.json`.
[^7JgIS42mz7U]: [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](https://www.youtube.com/watch?v=7JgIS42mz7U); publication: 2026-07-12T22:00:09Z; analysis: `analysis/7JgIS42mz7U.json`.
[^Bdrs3uAX0_M]: [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](https://www.youtube.com/watch?v=Bdrs3uAX0_M); publication: 2026-10-04T19:30:20Z; analysis: `analysis/Bdrs3uAX0_M.json`.
[^LqLoYksJ6do]: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3](https://www.youtube.com/watch?v=LqLoYksJ6do); publication: 2026-07-20T17:17:53Z; analysis: `analysis/LqLoYksJ6do.json`.
[^bI8WyG9YB0I]: [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](https://www.youtube.com/watch?v=bI8WyG9YB0I); publication: 2026-10-11T19:00:11Z; analysis: `analysis/bI8WyG9YB0I.json`.
[^f3o0-9Dlw3E]: [AI Hackers Are Faster Than Your Pen Test — Eli Cohen, Snyk](https://www.youtube.com/watch?v=f3o0-9Dlw3E); publication: 2026-10-07T21:30:34Z; analysis: `analysis/f3o0-9Dlw3E.json`.
[^rcsliSIy_YU]: [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU); publication: 2026-01-08T16:30:23Z; analysis: `analysis/rcsliSIy_YU.json`.
[^utTqdQpe39A]: [GitHub's AI Powered Security Platform: Sarah Khalife](https://www.youtube.com/watch?v=utTqdQpe39A); publication: 2025-02-08T21:31:24Z; analysis: `analysis/utTqdQpe39A.json`.
[^yWS0udrIOc8]: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/yWS0udrIOc8.json`.
