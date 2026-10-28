---
{
  "type": "technique",
  "id": "reference-differential-tests",
  "title": "Compare behavior against trusted reference implementations or invariants",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-07-17T21:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "Rx8f05JI_WA",
      "resource": "https://www.youtube.com/watch?v=Rx8f05JI_WA",
      "title": "SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI",
      "author": "Rishi Desai, Abundant AI",
      "last_modified": "2026-07-07T03:45:51Z",
      "analysis_file": "analysis/Rx8f05JI_WA.json"
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
      "id": "c35YoMdnI78",
      "resource": "https://www.youtube.com/watch?v=c35YoMdnI78",
      "title": "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "author": "Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "last_modified": "2026-07-17T21:00:06Z",
      "analysis_file": "analysis/c35YoMdnI78.json"
    },
    {
      "id": "eIoohUmYpGI",
      "resource": "https://www.youtube.com/watch?v=eIoohUmYpGI",
      "title": "The Infinite Software Crisis – Jake Nations, Netflix",
      "author": "Jake Nations, Netflix",
      "last_modified": "2025-12-20T17:00:06Z",
      "analysis_file": "analysis/eIoohUmYpGI.json"
    },
    {
      "id": "kDczF4wBh8s",
      "resource": "https://www.youtube.com/watch?v=kDczF4wBh8s",
      "title": "From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval",
      "author": "Brooke Hopkins, Coval",
      "last_modified": "2025-07-31T16:45:05Z",
      "analysis_file": "analysis/kDczF4wBh8s.json"
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
      "id": "tHN44yJoeS8",
      "resource": "https://www.youtube.com/watch?v=tHN44yJoeS8",
      "title": "Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor",
      "author": "Naman Jain, Cursor",
      "last_modified": "2025-12-15T17:18:09Z",
      "analysis_file": "analysis/tHN44yJoeS8.json"
    },
    {
      "id": "uU5Gv2h8-9g",
      "resource": "https://www.youtube.com/watch?v=uU5Gv2h8-9g",
      "title": "Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison",
      "author": "Cat Wu & Thariq Shihipar ft Simon Willison",
      "last_modified": "2026-07-15T15:05:06Z",
      "analysis_file": "analysis/uU5Gv2h8-9g.json"
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

# Compare behavior against trusted reference implementations or invariants

## What

Compare behavior against trusted reference implementations or invariants

Reference parity catches incorrect semantics that a narrow self-written suite may miss.

## Evidence

> reference parity checks, computer use agent checks for the
> — 03:17 [^Rx8f05JI_WA]

> anything in repos. It was running the effect tests that it
> — 50:56 [^Wmp2Tku2PrI]

> running a browser, cases where you have years and years of test suites and
> — 37:37 [^c35YoMdnI78]

> fed that pull request of the actual manual migration into our research
> — 15:09 [^eIoohUmYpGI]

> what we did at Whimo. So coming up with metrics that apply to lots of scenarios.
> — 06:30 [^kDczF4wBh8s]

> still had these tests that were like extremely over-fitting. And as long as
> — 09:14 [^pmoDeA3RBZY]

> correct code. So we uh generated like a million compression inputs and your test
> — 13:31 [^tHN44yJoeS8]

> input generators where you generate diverse inputs and each of the problems
> — 06:01 [^tHN44yJoeS8]

> >> um I think that like what people I think underount is like a codebase is a spec
> — 05:31 [^uU5Gv2h8-9g]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^Rx8f05JI_WA]: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA); publication: 2026-07-07T03:45:51Z; analysis: `analysis/Rx8f05JI_WA.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^eIoohUmYpGI]: [The Infinite Software Crisis – Jake Nations, Netflix](https://www.youtube.com/watch?v=eIoohUmYpGI); publication: 2025-12-20T17:00:06Z; analysis: `analysis/eIoohUmYpGI.json`.
[^kDczF4wBh8s]: [From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval](https://www.youtube.com/watch?v=kDczF4wBh8s); publication: 2025-07-31T16:45:05Z; analysis: `analysis/kDczF4wBh8s.json`.
[^pmoDeA3RBZY]: [Dark Factory: OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=pmoDeA3RBZY); publication: 2026-06-05T16:00:06Z; analysis: `analysis/pmoDeA3RBZY.json`.
[^tHN44yJoeS8]: [Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor](https://www.youtube.com/watch?v=tHN44yJoeS8); publication: 2025-12-15T17:18:09Z; analysis: `analysis/tHN44yJoeS8.json`.
[^uU5Gv2h8-9g]: [Claude Fable, Claude Tag, and Anthropic's Culture — Cat Wu & Thariq Shihipar ft Simon Willison](https://www.youtube.com/watch?v=uU5Gv2h8-9g); publication: 2026-07-15T15:05:06Z; analysis: `analysis/uU5Gv2h8-9g.json`.
