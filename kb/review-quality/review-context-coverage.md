---
{
  "type": "technique",
  "id": "review-context-coverage",
  "title": "Review cross-file callers, omissions and critical paths, not only the visible diff",
  "area": "review-quality",
  "status": "stable",
  "valid_from": "2026-10-11T12:30:23Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1P1hJ36rxM0",
      "resource": "https://www.youtube.com/watch?v=1P1hJ36rxM0",
      "title": "\"Software engineering is not about writing code\" — Benoit Schillings, Google DeepMind VP of Research",
      "author": "Benoit Schillings, Google DeepMind VP of Research",
      "last_modified": "2026-07-17T15:24:44Z",
      "analysis_file": "analysis/1P1hJ36rxM0.json"
    },
    {
      "id": "1lgFGaHoGq8",
      "resource": "https://www.youtube.com/watch?v=1lgFGaHoGq8",
      "title": "AI’s Jurassic Park Period — Aaron Stanley, dbt Labs",
      "author": "Aaron Stanley, dbt Labs",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/1lgFGaHoGq8.json"
    },
    {
      "id": "474j-n1Ltxc",
      "resource": "https://www.youtube.com/watch?v=474j-n1Ltxc",
      "title": "AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile",
      "author": "Daksh Gupta, Greptile",
      "last_modified": "2026-09-27T18:30:07Z",
      "analysis_file": "analysis/474j-n1Ltxc.json"
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
      "id": "9arM9b7JgOo",
      "resource": "https://www.youtube.com/watch?v=9arM9b7JgOo",
      "title": "Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat",
      "author": "Jeffrey Lee-Chan, Snapchat",
      "last_modified": "2026-07-11T14:45:18Z",
      "analysis_file": "analysis/9arM9b7JgOo.json"
    },
    {
      "id": "KcVkq5L-0f0",
      "resource": "https://www.youtube.com/watch?v=KcVkq5L-0f0",
      "title": "Your agents lack context: Here's how to fix \"You're absolutely right!\" — Brandon Waselnuk, Unblocked",
      "author": "Brandon Waselnuk, Unblocked",
      "last_modified": "2026-09-09T14:30:12Z",
      "analysis_file": "analysis/KcVkq5L-0f0.json"
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
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
    },
    {
      "id": "NuePCNMpWGc",
      "resource": "https://www.youtube.com/watch?v=NuePCNMpWGc",
      "title": "Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar",
      "author": "Prasenjit Sarkar, Sonar",
      "last_modified": "2026-05-31T18:00:21Z",
      "analysis_file": "analysis/NuePCNMpWGc.json"
    },
    {
      "id": "SZStlIhyTCY",
      "resource": "https://www.youtube.com/watch?v=SZStlIhyTCY",
      "title": "Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company",
      "author": "Martin Harrysson & Natasha Maniar, McKinsey & Company",
      "last_modified": "2025-12-12T17:00:06Z",
      "analysis_file": "analysis/SZStlIhyTCY.json"
    },
    {
      "id": "W76woOYHlvY",
      "resource": "https://www.youtube.com/watch?v=W76woOYHlvY",
      "title": "Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban",
      "author": "Louis Knight-Webb, Vibe Kanban",
      "last_modified": "2026-05-02T21:00:06Z",
      "analysis_file": "analysis/W76woOYHlvY.json"
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
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
    },
    {
      "id": "k2ClBT4aqAg",
      "resource": "https://www.youtube.com/watch?v=k2ClBT4aqAg",
      "title": "We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman",
      "author": "Kamalakannan Nandagopal, Postman",
      "last_modified": "2026-10-08T21:30:19Z",
      "analysis_file": "analysis/k2ClBT4aqAg.json"
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
      "id": "prttz9_1XDc",
      "resource": "https://www.youtube.com/watch?v=prttz9_1XDc",
      "title": "Enhancing Quality and Security in CI: Gunjan Patel",
      "author": null,
      "last_modified": "2024-11-27T19:56:40Z",
      "analysis_file": "analysis/prttz9_1XDc.json"
    },
    {
      "id": "qdAkxLoYNI8",
      "resource": "https://www.youtube.com/watch?v=qdAkxLoYNI8",
      "title": "How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked",
      "author": "Peter Werry, Unblocked",
      "last_modified": "2026-08-27T18:00:23Z",
      "analysis_file": "analysis/qdAkxLoYNI8.json"
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
      "id": "yqF6XhzbWBk",
      "resource": "https://www.youtube.com/watch?v=yqF6XhzbWBk",
      "title": "Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo",
      "author": "Sebastian Fox, Composo",
      "last_modified": "2026-08-22T17:00:32Z",
      "analysis_file": "analysis/yqF6XhzbWBk.json"
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

# Review cross-file callers, omissions and critical paths, not only the visible diff

## What

Review cross-file callers, omissions and critical paths, not only the visible diff

A reviewer handling several streams should be able to move from task intent to exact diff, test evidence and live preview without reconstructing identity across disconnected tools.

## Evidence

Source analysis [^1P1hJ36rxM0]; no independently matched timestamped quote published.

Source analysis [^1lgFGaHoGq8]; no independently matched timestamped quote published.

Source analysis [^474j-n1Ltxc]; no independently matched timestamped quote published.

Source analysis [^7JgIS42mz7U]; no independently matched timestamped quote published.

Source analysis [^9arM9b7JgOo]; no independently matched timestamped quote published.

> understand how the operations of the business are so it knows the business
> — 03:50 [^KcVkq5L-0f0]

> blast radius before it actually even acts on it.
> — 18:57 [^KhRjivBSwiw]

Source analysis [^MhHEGMFCEB0]; no independently matched timestamped quote published.

> bugs that is very very hard for a human being to detect. We have seen the total
> — 10:18 [^NuePCNMpWGc]

Source analysis [^SZStlIhyTCY]; no independently matched timestamped quote published.

Source analysis [^W76woOYHlvY]; no independently matched timestamped quote published.

> we have for us. It changed a whole lot of files and it worked out of the box
> — 09:14 [^c5qJHr3DnT4]

> like try to understand the breakability, understand
> — 24:51 [^cgimkNGNjvU]

> noticed that almost 75% of the PRs had some effect on the APIs. So, either
> — 13:41 [^k2ClBT4aqAg]

> uh and then go from there uh so that I can clear the context for each one and
> — 1:02:28 [^pFsfax19yOM]

> St statement needs to go from here to here and that caus the uh security
> — 16:29 [^prttz9_1XDc]

Source analysis [^qdAkxLoYNI8]; no independently matched timestamped quote published.

Source analysis [^utTqdQpe39A]; no independently matched timestamped quote published.

> the most similar outputs that it's judged before and how they
> — 15:39 [^yqF6XhzbWBk]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer redundant or low-value review rounds
- **Speed:** Shorter evidence-backed review/repair cycles
- **Quality:** Better focus on actionable defects rather than cosmetic scores
- **Reliability:** Independent, revision-bound verification
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1P1hJ36rxM0]: ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](https://www.youtube.com/watch?v=1P1hJ36rxM0); publication: 2026-07-17T15:24:44Z; analysis: `analysis/1P1hJ36rxM0.json`.
[^1lgFGaHoGq8]: [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](https://www.youtube.com/watch?v=1lgFGaHoGq8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/1lgFGaHoGq8.json`.
[^474j-n1Ltxc]: [AI-Generated Code Is Already Competing With Human Code — Daksh Gupta, Greptile](https://www.youtube.com/watch?v=474j-n1Ltxc); publication: 2026-09-27T18:30:07Z; analysis: `analysis/474j-n1Ltxc.json`.
[^7JgIS42mz7U]: [The AI bugpocalypse is here. Now what? - Jack Cable, Corridor](https://www.youtube.com/watch?v=7JgIS42mz7U); publication: 2026-07-12T22:00:09Z; analysis: `analysis/7JgIS42mz7U.json`.
[^9arM9b7JgOo]: [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo); publication: 2026-07-11T14:45:18Z; analysis: `analysis/9arM9b7JgOo.json`.
[^KcVkq5L-0f0]: [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=KcVkq5L-0f0); publication: 2026-09-09T14:30:12Z; analysis: `analysis/KcVkq5L-0f0.json`.
[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^NuePCNMpWGc]: [Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar](https://www.youtube.com/watch?v=NuePCNMpWGc); publication: 2026-05-31T18:00:21Z; analysis: `analysis/NuePCNMpWGc.json`.
[^SZStlIhyTCY]: [Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company](https://www.youtube.com/watch?v=SZStlIhyTCY); publication: 2025-12-12T17:00:06Z; analysis: `analysis/SZStlIhyTCY.json`.
[^W76woOYHlvY]: [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](https://www.youtube.com/watch?v=W76woOYHlvY); publication: 2026-05-02T21:00:06Z; analysis: `analysis/W76woOYHlvY.json`.
[^c5qJHr3DnT4]: [GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft](https://www.youtube.com/watch?v=c5qJHr3DnT4); publication: 2025-06-27T09:48:38Z; analysis: `analysis/c5qJHr3DnT4.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
[^k2ClBT4aqAg]: [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](https://www.youtube.com/watch?v=k2ClBT4aqAg); publication: 2026-10-08T21:30:19Z; analysis: `analysis/k2ClBT4aqAg.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^prttz9_1XDc]: [Enhancing Quality and Security in CI: Gunjan Patel](https://www.youtube.com/watch?v=prttz9_1XDc); publication: 2024-11-27T19:56:40Z; analysis: `analysis/prttz9_1XDc.json`.
[^qdAkxLoYNI8]: [How to Generate Mergeable Code with a Context Engine — Peter Werry, Unblocked](https://www.youtube.com/watch?v=qdAkxLoYNI8); publication: 2026-08-27T18:00:23Z; analysis: `analysis/qdAkxLoYNI8.json`.
[^utTqdQpe39A]: [GitHub's AI Powered Security Platform: Sarah Khalife](https://www.youtube.com/watch?v=utTqdQpe39A); publication: 2025-02-08T21:31:24Z; analysis: `analysis/utTqdQpe39A.json`.
[^yqF6XhzbWBk]: [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](https://www.youtube.com/watch?v=yqF6XhzbWBk); publication: 2026-08-22T17:00:32Z; analysis: `analysis/yqF6XhzbWBk.json`.
