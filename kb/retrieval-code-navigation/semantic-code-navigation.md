---
{
  "type": "technique",
  "id": "semantic-code-navigation",
  "title": "Use LSP, AST and dependency graphs for exact code navigation",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-10-11T12:30:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "0tVu-V3_fFw",
      "resource": "https://www.youtube.com/watch?v=0tVu-V3_fFw",
      "title": "Designing AI To Scale Human Thought — Jun Yu Tan, Tusk",
      "author": "Jun Yu Tan, Tusk",
      "last_modified": "2025-06-03T07:00:06Z",
      "analysis_file": "analysis/0tVu-V3_fFw.json"
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
      "id": "AMiyLItEtLA",
      "resource": "https://www.youtube.com/watch?v=AMiyLItEtLA",
      "title": "fighting slop with slop — Vaibhav Gupta, Boundary",
      "author": "Vaibhav Gupta, Boundary",
      "last_modified": "2026-07-31T01:11:30Z",
      "analysis_file": "analysis/AMiyLItEtLA.json"
    },
    {
      "id": "AvVoJBxgSQk",
      "resource": "https://www.youtube.com/watch?v=AvVoJBxgSQk",
      "title": "Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2025-07-21T17:15:06Z",
      "analysis_file": "analysis/AvVoJBxgSQk.json"
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
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "MI83buT_23o",
      "resource": "https://www.youtube.com/watch?v=MI83buT_23o",
      "title": "Devin 2.0 and the Future of SWE - Scott Wu, Cognition",
      "author": "Scott Wu, Cognition",
      "last_modified": "2025-07-25T23:07:05Z",
      "analysis_file": "analysis/MI83buT_23o.json"
    },
    {
      "id": "ObTPqBGsEbA",
      "resource": "https://www.youtube.com/watch?v=ObTPqBGsEbA",
      "title": "The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks",
      "author": "Sandipan Bhaumik, Databricks",
      "last_modified": "2026-06-18T13:00:06Z",
      "analysis_file": "analysis/ObTPqBGsEbA.json"
    },
    {
      "id": "Q0VkgCyNVUg",
      "resource": "https://www.youtube.com/watch?v=Q0VkgCyNVUg",
      "title": "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j",
      "author": "Stephen Chin, Neo4j",
      "last_modified": "2026-07-22T18:30:02Z",
      "analysis_file": "analysis/Q0VkgCyNVUg.json"
    },
    {
      "id": "Ve-akpov78Q",
      "resource": "https://www.youtube.com/watch?v=Ve-akpov78Q",
      "title": "Code Generation and Maintenance at Scale: Morgante Pell",
      "author": null,
      "last_modified": "2024-10-17T18:52:20Z",
      "analysis_file": "analysis/Ve-akpov78Q.json"
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
      "id": "_Zcw_sVF6hU",
      "resource": "https://www.youtube.com/watch?v=_Zcw_sVF6hU",
      "title": "The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "author": "Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "last_modified": "2026-04-18T10:30:06Z",
      "analysis_file": "analysis/_Zcw_sVF6hU.json"
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
      "id": "dRmWYHuIJxM",
      "resource": "https://www.youtube.com/watch?v=dRmWYHuIJxM",
      "title": "We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco",
      "author": "Rajkumar Sakthivel, Tesco",
      "last_modified": "2026-06-28T22:30:29Z",
      "analysis_file": "analysis/dRmWYHuIJxM.json"
    },
    {
      "id": "jVjt-2g8NMY",
      "resource": "https://www.youtube.com/watch?v=jVjt-2g8NMY",
      "title": "A Genius With Amnesia - Victor Savkin, Nx",
      "author": "Victor Savkin, Nx",
      "last_modified": "2026-06-26T01:15:06Z",
      "analysis_file": "analysis/jVjt-2g8NMY.json"
    },
    {
      "id": "l0FLhNqBOic",
      "resource": "https://www.youtube.com/watch?v=l0FLhNqBOic",
      "title": "AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents",
      "author": "Vasuman Moza, Varick Agents",
      "last_modified": "2026-07-28T21:00:06Z",
      "analysis_file": "analysis/l0FLhNqBOic.json"
    },
    {
      "id": "uuwDWRbxoYo",
      "resource": "https://www.youtube.com/watch?v=uuwDWRbxoYo",
      "title": "AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar",
      "author": "Ali-Reza Adl-Tabatabai, Sonar",
      "last_modified": "2026-10-09T01:30:15Z",
      "analysis_file": "analysis/uuwDWRbxoYo.json"
    },
    {
      "id": "xIt_mTQp6mY",
      "resource": "https://www.youtube.com/watch?v=xIt_mTQp6mY",
      "title": "Loop Engineering from First Principles — Kyle Mistele, HumanLayer",
      "author": "Kyle Mistele, HumanLayer",
      "last_modified": "2026-07-25T20:41:40Z",
      "analysis_file": "analysis/xIt_mTQp6mY.json"
    },
    {
      "id": "zKk7sDMGDEQ",
      "resource": "https://www.youtube.com/watch?v=zKk7sDMGDEQ",
      "title": "Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer",
      "author": "Kuba Rogut, Turbopuffer",
      "last_modified": "2026-06-03T15:00:06Z",
      "analysis_file": "analysis/zKk7sDMGDEQ.json"
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

# Use LSP, AST and dependency graphs for exact code navigation

## What

Use LSP, AST and dependency graphs for exact code navigation

Keep centralized coordination for dependent work, but dispatch independent tasks from events rather than serial orchestrator exchanges.

## Evidence

Source analysis [^0tVu-V3_fFw]; no independently matched timestamped quote published.

Source analysis [^3ySF0I5iE_0]; no independently matched timestamped quote published.

Source analysis [^AMiyLItEtLA]; no independently matched timestamped quote published.

Source analysis [^AvVoJBxgSQk]; no independently matched timestamped quote published.

> You can't gp what you literally cannot see. This is tools and infrastructure
> — 07:54 [^Bdrs3uAX0_M]

> needs. Don't dump the entire repository at runtime. It'll pull the subgraph and
> — 23:56 [^KhRjivBSwiw]

> trying to build this um you would uh uh use something like SCIP to actually
> — 1:15:10 [^KhRjivBSwiw]

Source analysis [^MI83buT_23o]; no independently matched timestamped quote published.

> message bus and they listen to the events that they
> — 20:54 [^ObTPqBGsEbA]

> So, skills you need to have the right skills, the right chain of skills. Um
> — 05:30 [^Q0VkgCyNVUg]

> second prompt then 1 second recompute from the TS server then 30 seconds to
> — 12:54 [^Ve-akpov78Q]

> TypeScript transformers asbased transformations.
> — 45:39 [^Wmp2Tku2PrI]

Source analysis [^_Zcw_sVF6hU]; no independently matched timestamped quote published.

Source analysis [^c5qJHr3DnT4]; no independently matched timestamped quote published.

> which function called which. So, if you find one piece of code, you can find
> — 04:18 [^dRmWYHuIJxM]

> each repo, what each project in each repo consumes package-wise, what API
> — 07:37 [^jVjt-2g8NMY]

> >> doesn't really matter what you use, but the point is we use a dependency graph.
> — 15:42 [^l0FLhNqBOic]

> taint analysis, control flow analysis, data flow analysis, software composition
> — 09:18 [^uuwDWRbxoYo]

> of band from your TypeScript config or ESLint rules, which if you're a
> — 09:56 [^xIt_mTQp6mY]

Source analysis [^zKk7sDMGDEQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^0tVu-V3_fFw]: [Designing AI To Scale Human Thought — Jun Yu Tan, Tusk](https://www.youtube.com/watch?v=0tVu-V3_fFw); publication: 2025-06-03T07:00:06Z; analysis: `analysis/0tVu-V3_fFw.json`.
[^3ySF0I5iE_0]: [A Practitioner's Guide to Graphs - Tim Ainge, Good Collective](https://www.youtube.com/watch?v=3ySF0I5iE_0); publication: 2026-07-18T21:30:06Z; analysis: `analysis/3ySF0I5iE_0.json`.
[^AMiyLItEtLA]: [fighting slop with slop — Vaibhav Gupta, Boundary](https://www.youtube.com/watch?v=AMiyLItEtLA); publication: 2026-07-31T01:11:30Z; analysis: `analysis/AMiyLItEtLA.json`.
[^AvVoJBxgSQk]: [Agentic GraphRAG: AI’s Logical Edge — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=AvVoJBxgSQk); publication: 2025-07-21T17:15:06Z; analysis: `analysis/AvVoJBxgSQk.json`.
[^Bdrs3uAX0_M]: [AI Coding Agents Are Breaking Big Codebases — Dan Adler, Sourcegraph](https://www.youtube.com/watch?v=Bdrs3uAX0_M); publication: 2026-10-04T19:30:20Z; analysis: `analysis/Bdrs3uAX0_M.json`.
[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^MI83buT_23o]: [Devin 2.0 and the Future of SWE - Scott Wu, Cognition](https://www.youtube.com/watch?v=MI83buT_23o); publication: 2025-07-25T23:07:05Z; analysis: `analysis/MI83buT_23o.json`.
[^ObTPqBGsEbA]: [The Production AI Playbook: Deploying Agents at Enterprise Scale — Sandipan Bhaumik, Databricks](https://www.youtube.com/watch?v=ObTPqBGsEbA); publication: 2026-06-18T13:00:06Z; analysis: `analysis/ObTPqBGsEbA.json`.
[^Q0VkgCyNVUg]: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens — Stephen Chin, Neo4j](https://www.youtube.com/watch?v=Q0VkgCyNVUg); publication: 2026-07-22T18:30:02Z; analysis: `analysis/Q0VkgCyNVUg.json`.
[^Ve-akpov78Q]: [Code Generation and Maintenance at Scale: Morgante Pell](https://www.youtube.com/watch?v=Ve-akpov78Q); publication: 2024-10-17T18:52:20Z; analysis: `analysis/Ve-akpov78Q.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^c5qJHr3DnT4]: [GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft](https://www.youtube.com/watch?v=c5qJHr3DnT4); publication: 2025-06-27T09:48:38Z; analysis: `analysis/c5qJHr3DnT4.json`.
[^dRmWYHuIJxM]: [We Cut 94% of AI Coding Tokens With a Local Code Index - Rajkumar Sakthivel, Tesco](https://www.youtube.com/watch?v=dRmWYHuIJxM); publication: 2026-06-28T22:30:29Z; analysis: `analysis/dRmWYHuIJxM.json`.
[^jVjt-2g8NMY]: [A Genius With Amnesia - Victor Savkin, Nx](https://www.youtube.com/watch?v=jVjt-2g8NMY); publication: 2026-06-26T01:15:06Z; analysis: `analysis/jVjt-2g8NMY.json`.
[^l0FLhNqBOic]: [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](https://www.youtube.com/watch?v=l0FLhNqBOic); publication: 2026-07-28T21:00:06Z; analysis: `analysis/l0FLhNqBOic.json`.
[^uuwDWRbxoYo]: [AI Writes More PRs. Who Validates Them? — Ali-Reza Adl-Tabatabai, Sonar](https://www.youtube.com/watch?v=uuwDWRbxoYo); publication: 2026-10-09T01:30:15Z; analysis: `analysis/uuwDWRbxoYo.json`.
[^xIt_mTQp6mY]: [Loop Engineering from First Principles — Kyle Mistele, HumanLayer](https://www.youtube.com/watch?v=xIt_mTQp6mY); publication: 2026-07-25T20:41:40Z; analysis: `analysis/xIt_mTQp6mY.json`.
[^zKk7sDMGDEQ]: [Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer](https://www.youtube.com/watch?v=zKk7sDMGDEQ); publication: 2026-06-03T15:00:06Z; analysis: `analysis/zKk7sDMGDEQ.json`.
