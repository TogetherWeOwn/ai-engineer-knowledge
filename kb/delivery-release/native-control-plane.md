---
{
  "type": "technique",
  "id": "native-control-plane",
  "title": "Move orchestration into supported native or plugin surfaces, not a second host control plane",
  "area": "delivery-release",
  "status": "stable",
  "valid_from": "2026-09-27T17:30:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2czYyrTzILg",
      "resource": "https://www.youtube.com/watch?v=2czYyrTzILg",
      "title": "From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik",
      "author": "Sandipan Bhaumik",
      "last_modified": "2026-04-08T10:23:12Z",
      "analysis_file": "analysis/2czYyrTzILg.json"
    },
    {
      "id": "KHudyx5wW3U",
      "resource": "https://www.youtube.com/watch?v=KHudyx5wW3U",
      "title": "Agent Frameworks Considered Harmful — Rémi Louf, .txt",
      "author": "Rémi Louf, .txt",
      "last_modified": "2026-08-22T16:30:39Z",
      "analysis_file": "analysis/KHudyx5wW3U.json"
    },
    {
      "id": "RjfbvDXpFls",
      "resource": "https://www.youtube.com/watch?v=RjfbvDXpFls",
      "title": "Building pi in a World of Slop — Mario Zechner",
      "author": "Mario Zechner",
      "last_modified": "2026-04-16T22:58:06Z",
      "analysis_file": "analysis/RjfbvDXpFls.json"
    },
    {
      "id": "TRfzFJCJ7ZE",
      "resource": "https://www.youtube.com/watch?v=TRfzFJCJ7ZE",
      "title": "Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor",
      "author": "Charlie Holtz, Conductor",
      "last_modified": "2026-09-27T16:30:08Z",
      "analysis_file": "analysis/TRfzFJCJ7ZE.json"
    },
    {
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
    },
    {
      "id": "b2GqTDWtg6s",
      "resource": "https://www.youtube.com/watch?v=b2GqTDWtg6s",
      "title": "Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering",
      "author": "Anju Kambadur, Bloomberg Head of AI Engineering",
      "last_modified": "2025-04-01T15:06:35Z",
      "analysis_file": "analysis/b2GqTDWtg6s.json"
    },
    {
      "id": "h403btjldDQ",
      "resource": "https://www.youtube.com/watch?v=h403btjldDQ",
      "title": "Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa",
      "author": "Dotta Bippa",
      "last_modified": "2026-04-15T21:59:05Z",
      "analysis_file": "analysis/h403btjldDQ.json"
    },
    {
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
    },
    {
      "id": "pMggiOb18tc",
      "resource": "https://www.youtube.com/watch?v=pMggiOb18tc",
      "title": "The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI",
      "author": "Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI",
      "last_modified": "2026-07-09T18:53:34Z",
      "analysis_file": "analysis/pMggiOb18tc.json"
    },
    {
      "id": "pmoDeA3RBZY",
      "resource": "https://www.youtube.com/watch?v=pmoDeA3RBZY",
      "title": "Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-06-05T16:00:06Z",
      "analysis_file": "analysis/pmoDeA3RBZY.json"
    },
    {
      "id": "tUPPVhBBcoM",
      "resource": "https://www.youtube.com/watch?v=tUPPVhBBcoM",
      "title": "Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp",
      "author": "Zach Lloyd, Warp",
      "last_modified": "2026-09-27T17:30:36Z",
      "analysis_file": "analysis/tUPPVhBBcoM.json"
    },
    {
      "id": "zgNvts_2TUE",
      "resource": "https://www.youtube.com/watch?v=zgNvts_2TUE",
      "title": "State of the Claw — Peter Steinberger",
      "author": "Peter Steinberger",
      "last_modified": "2026-04-17T15:30:06Z",
      "analysis_file": "analysis/zgNvts_2TUE.json"
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

# Move orchestration into supported native or plugin surfaces, not a second host control plane

## What

Move orchestration into supported native or plugin surfaces, not a second host control plane

Saying yes to every feature bloats the core; a plugin boundary lets integration owners evolve their own component independently.

## Evidence

Source analysis [^2czYyrTzILg]; no independently matched timestamped quote published.

> when it comes to orchestrating these things. It's just good old software
> — 18:19 [^KHudyx5wW3U]

> actually happens is a new process gets spawned. Basically, the command you
> — 02:58 [^RjfbvDXpFls]

> some code that shows you how to modify yourself by writing extensions."
> — 06:53 [^RjfbvDXpFls]

> yourself why isn't this workflow the default?
> — 03:58 [^TRfzFJCJ7ZE]

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

Source analysis [^b2GqTDWtg6s]; no independently matched timestamped quote published.

Source analysis [^h403btjldDQ]; no independently matched timestamped quote published.

> superpowers, "This is easier for me to show you the variants if I just mock
> — 38:40 [^pFsfax19yOM]

> You can think about an agent taking different approaches, maybe like five or
> — 16:25 [^pMggiOb18tc]

> to rip it into pieces. And a plugin architecture somewhat made sense.
> — 08:07 [^pmoDeA3RBZY]

> probably be focusing on your own product, not building this
> — 12:27 [^tUPPVhBBcoM]

Source analysis [^zgNvts_2TUE]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid failed cutover and repeated integration work
- **Speed:** Shorter safe automated promotion
- **Quality:** Release the actual tested artifact
- **Reliability:** Staging, provenance and rollback contain regressions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2czYyrTzILg]: [From Chaos to Choreography: Multi-Agent Orchestration Patterns That Actually Work — Sandipan Bhaumik](https://www.youtube.com/watch?v=2czYyrTzILg); publication: 2026-04-08T10:23:12Z; analysis: `analysis/2czYyrTzILg.json`.
[^KHudyx5wW3U]: [Agent Frameworks Considered Harmful — Rémi Louf, .txt](https://www.youtube.com/watch?v=KHudyx5wW3U); publication: 2026-08-22T16:30:39Z; analysis: `analysis/KHudyx5wW3U.json`.
[^RjfbvDXpFls]: [Building pi in a World of Slop — Mario Zechner](https://www.youtube.com/watch?v=RjfbvDXpFls); publication: 2026-04-16T22:58:06Z; analysis: `analysis/RjfbvDXpFls.json`.
[^TRfzFJCJ7ZE]: [Orchestras, Not Factories: How the Fastest Builders Work — Charlie Holtz, Conductor](https://www.youtube.com/watch?v=TRfzFJCJ7ZE); publication: 2026-09-27T16:30:08Z; analysis: `analysis/TRfzFJCJ7ZE.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^b2GqTDWtg6s]: [Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering](https://www.youtube.com/watch?v=b2GqTDWtg6s); publication: 2025-04-01T15:06:35Z; analysis: `analysis/b2GqTDWtg6s.json`.
[^h403btjldDQ]: [Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa](https://www.youtube.com/watch?v=h403btjldDQ); publication: 2026-04-15T21:59:05Z; analysis: `analysis/h403btjldDQ.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^pMggiOb18tc]: [The Golden Age of AI Engineering — Alexander Embiricos & Romain Huet & Peter Steinberger, OpenAI](https://www.youtube.com/watch?v=pMggiOb18tc); publication: 2026-07-09T18:53:34Z; analysis: `analysis/pMggiOb18tc.json`.
[^pmoDeA3RBZY]: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY); publication: 2026-06-05T16:00:06Z; analysis: `analysis/pmoDeA3RBZY.json`.
[^tUPPVhBBcoM]: [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](https://www.youtube.com/watch?v=tUPPVhBBcoM); publication: 2026-09-27T17:30:36Z; analysis: `analysis/tUPPVhBBcoM.json`.
[^zgNvts_2TUE]: [State of the Claw — Peter Steinberger](https://www.youtube.com/watch?v=zgNvts_2TUE); publication: 2026-04-17T15:30:06Z; analysis: `analysis/zgNvts_2TUE.json`.
