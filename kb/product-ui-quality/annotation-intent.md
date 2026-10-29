---
{
  "type": "technique",
  "id": "annotation-intent",
  "title": "Capture human visual intent as structured, actionable change requests",
  "area": "product-ui-quality",
  "status": "stable",
  "valid_from": "2026-10-11T20:00:38Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2JX6JYyQG4Y",
      "resource": "https://www.youtube.com/watch?v=2JX6JYyQG4Y",
      "title": "Perception Agents — Antje Barth, Amazon AGI Lab",
      "author": "Antje Barth, Amazon AGI Lab",
      "last_modified": "2026-07-23T16:00:06Z",
      "analysis_file": "analysis/2JX6JYyQG4Y.json"
    },
    {
      "id": "BurJvbqFr4c",
      "resource": "https://www.youtube.com/watch?v=BurJvbqFr4c",
      "title": "Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses",
      "author": "Tun Shwe, Lenses",
      "last_modified": "2026-04-08T07:31:01Z",
      "analysis_file": "analysis/BurJvbqFr4c.json"
    },
    {
      "id": "SQMCtZX3trg",
      "resource": "https://www.youtube.com/watch?v=SQMCtZX3trg",
      "title": "The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)",
      "author": "Paul Bakaus, Renaissance Geek (Impeccable)",
      "last_modified": "2026-09-21T19:00:10Z",
      "analysis_file": "analysis/SQMCtZX3trg.json"
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
      "id": "XdAWgO11zuk",
      "resource": "https://www.youtube.com/watch?v=XdAWgO11zuk",
      "title": "What We Learned from Using LLMs in Pinterest — Mukuntha Narayanan, Han Wang, Pinterest",
      "author": "Mukuntha Narayanan, Han Wang, Pinterest",
      "last_modified": "2025-07-16T17:58:25Z",
      "analysis_file": "analysis/XdAWgO11zuk.json"
    },
    {
      "id": "ZGzthw4BZiA",
      "resource": "https://www.youtube.com/watch?v=ZGzthw4BZiA",
      "title": "Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab",
      "author": "Emile Baizel & Shruti Arora, Amazon AGI Lab",
      "last_modified": "2026-10-11T20:00:38Z",
      "analysis_file": "analysis/ZGzthw4BZiA.json"
    },
    {
      "id": "bMjlRrWjdT0",
      "resource": "https://www.youtube.com/watch?v=bMjlRrWjdT0",
      "title": "AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "author": "Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash",
      "last_modified": "2026-08-28T15:00:03Z",
      "analysis_file": "analysis/bMjlRrWjdT0.json"
    },
    {
      "id": "eLXF0VojuSs",
      "resource": "https://www.youtube.com/watch?v=eLXF0VojuSs",
      "title": "How to Construct Domain Specific LLM Evaluation Systems: Hamel Husain and Emil Sedgh",
      "author": null,
      "last_modified": "2024-09-19T16:47:24Z",
      "analysis_file": "analysis/eLXF0VojuSs.json"
    },
    {
      "id": "il1c1a2FufU",
      "resource": "https://www.youtube.com/watch?v=il1c1a2FufU",
      "title": "Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex",
      "author": null,
      "last_modified": "2026-07-24T15:00:06Z",
      "analysis_file": "analysis/il1c1a2FufU.json"
    },
    {
      "id": "zl4EdALzktU",
      "resource": "https://www.youtube.com/watch?v=zl4EdALzktU",
      "title": "AI Engineering 201: The Rest of the Owl",
      "author": null,
      "last_modified": "2023-11-08T17:00:09Z",
      "analysis_file": "analysis/zl4EdALzktU.json"
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

# Capture human visual intent as structured, actionable change requests

## What

Capture human visual intent as structured, actionable change requests

Dictation accepts a messy high-bandwidth description; the agent organizes it into a structured request with source links.

## Evidence

Source analysis [^2JX6JYyQG4Y]; no independently matched timestamped quote published.

Source analysis [^BurJvbqFr4c]; no independently matched timestamped quote published.

> and then if I like one of them I can click accept and accept it. If I don't
> — 38:46 [^SQMCtZX3trg]

> edge cases and you know, front end is very stateful. Uh there's like
> — 06:29 [^W76woOYHlvY]

Source analysis [^XdAWgO11zuk]; no independently matched timestamped quote published.

Source analysis [^ZGzthw4BZiA]; no independently matched timestamped quote published.

> our scores our data sets uh these are all powered by very stable APIs uh that
> — 07:29 [^bMjlRrWjdT0]

> viewing app this is also a data labeling app where it it's like facilitates human
> — 08:10 [^eLXF0VojuSs]

Source analysis [^il1c1a2FufU]; no independently matched timestamped quote published.

Source analysis [^zl4EdALzktU]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less rework from misunderstood intent
- **Speed:** Faster useful feedback on runnable behavior
- **Quality:** Better usability, accessibility and actual task completion
- **Reliability:** Real-app evidence rather than attractive but broken demos
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2JX6JYyQG4Y]: [Perception Agents — Antje Barth, Amazon AGI Lab](https://www.youtube.com/watch?v=2JX6JYyQG4Y); publication: 2026-07-23T16:00:06Z; analysis: `analysis/2JX6JYyQG4Y.json`.
[^BurJvbqFr4c]: [Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses](https://www.youtube.com/watch?v=BurJvbqFr4c); publication: 2026-04-08T07:31:01Z; analysis: `analysis/BurJvbqFr4c.json`.
[^SQMCtZX3trg]: [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](https://www.youtube.com/watch?v=SQMCtZX3trg); publication: 2026-09-21T19:00:10Z; analysis: `analysis/SQMCtZX3trg.json`.
[^W76woOYHlvY]: [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](https://www.youtube.com/watch?v=W76woOYHlvY); publication: 2026-05-02T21:00:06Z; analysis: `analysis/W76woOYHlvY.json`.
[^XdAWgO11zuk]: [What We Learned from Using LLMs in Pinterest — Mukuntha Narayanan, Han Wang, Pinterest](https://www.youtube.com/watch?v=XdAWgO11zuk); publication: 2025-07-16T17:58:25Z; analysis: `analysis/XdAWgO11zuk.json`.
[^ZGzthw4BZiA]: [Build with Perception Agents — Emile Baizel & Shruti Arora, Amazon AGI Lab](https://www.youtube.com/watch?v=ZGzthw4BZiA); publication: 2026-10-11T20:00:38Z; analysis: `analysis/ZGzthw4BZiA.json`.
[^bMjlRrWjdT0]: [AI Evals for Cross-Functional Teams — Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash](https://www.youtube.com/watch?v=bMjlRrWjdT0); publication: 2026-08-28T15:00:03Z; analysis: `analysis/bMjlRrWjdT0.json`.
[^eLXF0VojuSs]: [How to Construct Domain Specific LLM Evaluation Systems: Hamel Husain and Emil Sedgh](https://www.youtube.com/watch?v=eLXF0VojuSs); publication: 2024-09-19T16:47:24Z; analysis: `analysis/eLXF0VojuSs.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^zl4EdALzktU]: [AI Engineering 201: The Rest of the Owl](https://www.youtube.com/watch?v=zl4EdALzktU); publication: 2023-11-08T17:00:09Z; analysis: `analysis/zl4EdALzktU.json`.
