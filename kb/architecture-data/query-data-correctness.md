---
{
  "type": "technique",
  "id": "query-data-correctness",
  "title": "Keep data transforms and query semantics deterministic and testable",
  "area": "architecture-data",
  "status": "stable",
  "valid_from": "2026-10-11T21:30:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "AvVoJBxgSQk",
      "resource": "https://www.youtube.com/watch?v=AvVoJBxgSQk",
      "title": "Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2025-07-21T17:15:06Z",
      "analysis_file": "analysis/AvVoJBxgSQk.json"
    },
    {
      "id": "Btk8wDUVs74",
      "resource": "https://www.youtube.com/watch?v=Btk8wDUVs74",
      "title": "From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com",
      "author": "Omri Bruchim & Tomer Ast, monday.com",
      "last_modified": "2026-07-22T23:00:11Z",
      "analysis_file": "analysis/Btk8wDUVs74.json"
    },
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
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
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "bUJgirn4_yc",
      "resource": "https://www.youtube.com/watch?v=bUJgirn4_yc",
      "title": "When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain",
      "author": "Dmitry Petrov, DataChain",
      "last_modified": "2026-07-20T06:25:07Z",
      "analysis_file": "analysis/bUJgirn4_yc.json"
    },
    {
      "id": "cSz7aL2nl2U",
      "resource": "https://www.youtube.com/watch?v=cSz7aL2nl2U",
      "title": "Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge",
      "author": "Gil Feig, Merge",
      "last_modified": "2026-10-09T23:30:08Z",
      "analysis_file": "analysis/cSz7aL2nl2U.json"
    },
    {
      "id": "eAXxdtNlK04",
      "resource": "https://www.youtube.com/watch?v=eAXxdtNlK04",
      "title": "Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse",
      "author": "Annabell Schäfer, Langfuse",
      "last_modified": "2026-07-18T20:15:06Z",
      "analysis_file": "analysis/eAXxdtNlK04.json"
    },
    {
      "id": "iUWwcG-C8OU",
      "resource": "https://www.youtube.com/watch?v=iUWwcG-C8OU",
      "title": "Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS",
      "author": "Garrett Galow, WorkOS",
      "last_modified": "2026-06-11T18:00:06Z",
      "analysis_file": "analysis/iUWwcG-C8OU.json"
    },
    {
      "id": "p7gaxmCUiIU",
      "resource": "https://www.youtube.com/watch?v=p7gaxmCUiIU",
      "title": "Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase",
      "author": "Shubhankar Srivastava, Browserbase",
      "last_modified": "2026-10-11T21:30:05Z",
      "analysis_file": "analysis/p7gaxmCUiIU.json"
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

# Keep data transforms and query semantics deterministic and testable

## What

Keep data transforms and query semantics deterministic and testable

The teacher noticed turns wasted on date resolution; a precomputed ISO date removes repeated ambiguity and tool chatter.

## Evidence

Source analysis [^AvVoJBxgSQk]; no independently matched timestamped quote published.

Source analysis [^Btk8wDUVs74]; no independently matched timestamped quote published.

> could look harmless but the predicate was actually a very important part of
> — 20:12 [^KhRjivBSwiw]

> example, I run a test within a transaction and I roll back the
> — 1:26:52 [^Wmp2Tku2PrI]

> template literally provides no runtime validation. use SQL schema. Find one.
> — 1:07:02 [^Wmp2Tku2PrI]

> because choosing a new version would be a new benchmark and I could not compare
> — 12:14 [^YIxzNZDDy1A]

Source analysis [^bUJgirn4_yc]; no independently matched timestamped quote published.

Source analysis [^cSz7aL2nl2U]; no independently matched timestamped quote published.

Source analysis [^eAXxdtNlK04]; no independently matched timestamped quote published.

Source analysis [^iUWwcG-C8OU]; no independently matched timestamped quote published.

> explicit ISO date in this particular format. Iteration three would have some
> — 31:40 [^p7gaxmCUiIU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Lower future change and maintenance cost
- **Speed:** Faster localized reasoning and edits
- **Quality:** Explicit domain/query semantics
- **Reliability:** Narrow testable boundaries and preserved invariants
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^AvVoJBxgSQk]: [Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=AvVoJBxgSQk); publication: 2025-07-21T17:15:06Z; analysis: `analysis/AvVoJBxgSQk.json`.
[^Btk8wDUVs74]: [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74); publication: 2026-07-22T23:00:11Z; analysis: `analysis/Btk8wDUVs74.json`.
[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^bUJgirn4_yc]: [When Agents Meet Physical Data: The Other Physics of Agent Harnesses - Dmitry Petrov, DataChain](https://www.youtube.com/watch?v=bUJgirn4_yc); publication: 2026-07-20T06:25:07Z; analysis: `analysis/bUJgirn4_yc.json`.
[^cSz7aL2nl2U]: [Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge](https://www.youtube.com/watch?v=cSz7aL2nl2U); publication: 2026-10-09T23:30:08Z; analysis: `analysis/cSz7aL2nl2U.json`.
[^eAXxdtNlK04]: [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04); publication: 2026-07-18T20:15:06Z; analysis: `analysis/eAXxdtNlK04.json`.
[^iUWwcG-C8OU]: [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU); publication: 2026-06-11T18:00:06Z; analysis: `analysis/iUWwcG-C8OU.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
