---
{
  "type": "technique",
  "id": "completion-verifier",
  "title": "Verify completion against external artifacts rather than an agent's assertion",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-13T12:00:08Z",
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
      "id": "4VhbYlfC7Gs",
      "resource": "https://www.youtube.com/watch?v=4VhbYlfC7Gs",
      "title": "Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw",
      "author": "Vincent Koc, OpenClaw",
      "last_modified": "2026-05-12T16:00:06Z",
      "analysis_file": "analysis/4VhbYlfC7Gs.json"
    },
    {
      "id": "AGkzpxMdPn8",
      "resource": "https://www.youtube.com/watch?v=AGkzpxMdPn8",
      "title": "Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture",
      "author": "Jess Grogan-Avignon & Jack Wang, Accenture",
      "last_modified": "2026-05-28T21:00:02Z",
      "analysis_file": "analysis/AGkzpxMdPn8.json"
    },
    {
      "id": "AQv3qRCG6Gw",
      "resource": "https://www.youtube.com/watch?v=AQv3qRCG6Gw",
      "title": "Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect",
      "author": "Will Brown, Prime Intellect",
      "last_modified": "2026-07-31T15:00:06Z",
      "analysis_file": "analysis/AQv3qRCG6Gw.json"
    },
    {
      "id": "BInpv7lGp1o",
      "resource": "https://www.youtube.com/watch?v=BInpv7lGp1o",
      "title": "The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI",
      "author": "Vinoth Govindarajan, OpenAI",
      "last_modified": "2026-07-29T16:00:06Z",
      "analysis_file": "analysis/BInpv7lGp1o.json"
    },
    {
      "id": "CLttOU7n6sI",
      "resource": "https://www.youtube.com/watch?v=CLttOU7n6sI",
      "title": "Respect The Process - Andrew Dumit, Watershed Technology Inc.",
      "author": "Andrew Dumit, Watershed Technology Inc.",
      "last_modified": "2026-07-07T23:31:49Z",
      "analysis_file": "analysis/CLttOU7n6sI.json"
    },
    {
      "id": "HN-F-OQe6j0",
      "resource": "https://www.youtube.com/watch?v=HN-F-OQe6j0",
      "title": "Defying Gravity - Kevin Hou, Google DeepMind",
      "author": "Kevin Hou, Google DeepMind",
      "last_modified": "2025-12-02T22:51:09Z",
      "analysis_file": "analysis/HN-F-OQe6j0.json"
    },
    {
      "id": "MLhAA9yguwM",
      "resource": "https://www.youtube.com/watch?v=MLhAA9yguwM",
      "title": "The 3 Pillars of Autonomy – Michele Catasta, Replit",
      "author": "Michele Catasta, Replit",
      "last_modified": "2025-12-22T16:30:06Z",
      "analysis_file": "analysis/MLhAA9yguwM.json"
    },
    {
      "id": "McknwOzbmyg",
      "resource": "https://www.youtube.com/watch?v=McknwOzbmyg",
      "title": "Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia",
      "author": "Jared Joselowitz, Ufonia",
      "last_modified": "2026-08-19T15:00:31Z",
      "analysis_file": "analysis/McknwOzbmyg.json"
    },
    {
      "id": "TeErpYBUIeM",
      "resource": "https://www.youtube.com/watch?v=TeErpYBUIeM",
      "title": "The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse",
      "author": "Marc Klingen, Langfuse",
      "last_modified": "2026-10-06T17:00:19Z",
      "analysis_file": "analysis/TeErpYBUIeM.json"
    },
    {
      "id": "U00AOI1eJUE",
      "resource": "https://www.youtube.com/watch?v=U00AOI1eJUE",
      "title": "Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz",
      "author": "Nimrod Hauser, Baz",
      "last_modified": "2026-04-08T00:45:06Z",
      "analysis_file": "analysis/U00AOI1eJUE.json"
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
      "id": "bI8WyG9YB0I",
      "resource": "https://www.youtube.com/watch?v=bI8WyG9YB0I",
      "title": "SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar",
      "author": "Killian Carlsen-Phelan, Sonar",
      "last_modified": "2026-10-11T19:00:11Z",
      "analysis_file": "analysis/bI8WyG9YB0I.json"
    },
    {
      "id": "dYh7TQkuYFE",
      "resource": "https://www.youtube.com/watch?v=dYh7TQkuYFE",
      "title": "I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore",
      "author": "Corey Gallon, Rexmore",
      "last_modified": "2026-10-13T12:00:08Z",
      "analysis_file": "analysis/dYh7TQkuYFE.json"
    },
    {
      "id": "fmZWvE7yDZo",
      "resource": "https://www.youtube.com/watch?v=fmZWvE7yDZo",
      "title": "UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft",
      "author": "Victor Dibia, Microsoft",
      "last_modified": "2025-07-21T19:11:17Z",
      "analysis_file": "analysis/fmZWvE7yDZo.json"
    },
    {
      "id": "iRcX54EO5g8",
      "resource": "https://www.youtube.com/watch?v=iRcX54EO5g8",
      "title": "Your agent is blindfolded — Johan Lajili, Poolside AI",
      "author": "Johan Lajili, Poolside AI",
      "last_modified": "2026-07-08T13:45:06Z",
      "analysis_file": "analysis/iRcX54EO5g8.json"
    },
    {
      "id": "m24UKZomm7k",
      "resource": "https://www.youtube.com/watch?v=m24UKZomm7k",
      "title": "Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft",
      "author": "Ornella Bahidika & Joel Allou, Microsoft",
      "last_modified": "2026-07-20T06:25:18Z",
      "analysis_file": "analysis/m24UKZomm7k.json"
    },
    {
      "id": "n97BCfyFIvw",
      "resource": "https://www.youtube.com/watch?v=n97BCfyFIvw",
      "title": "\"The engineer of the future is the person who chooses what is worth doing.\" — Addy Osmani, Anthropic",
      "author": "Addy Osmani, Anthropic",
      "last_modified": "2026-07-14T17:16:43Z",
      "analysis_file": "analysis/n97BCfyFIvw.json"
    },
    {
      "id": "oixzVKMAXG0",
      "resource": "https://www.youtube.com/watch?v=oixzVKMAXG0",
      "title": "Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway",
      "author": "Mahmoud Abdelwahab, Railway",
      "last_modified": "2026-10-12T15:00:19Z",
      "analysis_file": "analysis/oixzVKMAXG0.json"
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
      "id": "pSto5YaNGUo",
      "resource": "https://www.youtube.com/watch?v=pSto5YaNGUo",
      "title": "The Agentic AI Engineer - Benedikt Sanftl, Mutagent",
      "author": "Benedikt Sanftl, Mutagent",
      "last_modified": "2026-06-29T01:30:19Z",
      "analysis_file": "analysis/pSto5YaNGUo.json"
    },
    {
      "id": "so9l_MwS2yg",
      "resource": "https://www.youtube.com/watch?v=so9l_MwS2yg",
      "title": "Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS",
      "author": "Zack Proser, WorkOS",
      "last_modified": "2026-06-11T14:00:06Z",
      "analysis_file": "analysis/so9l_MwS2yg.json"
    },
    {
      "id": "u6q-byPWUuo",
      "resource": "https://www.youtube.com/watch?v=u6q-byPWUuo",
      "title": "From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge",
      "author": "Chaitanya Asawa, Abridge",
      "last_modified": "2026-08-19T14:00:06Z",
      "analysis_file": "analysis/u6q-byPWUuo.json"
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

# Verify completion against external artifacts rather than an agent's assertion

## What

Verify completion against external artifacts rather than an agent's assertion

Inspect actual environment state after meaningful steps to distinguish progress, completion and a stalled loop. Cheap state predicates should handle known cases before an uncertain semantic verifier is considered.

## Evidence

Source analysis [^2JX6JYyQG4Y]; no independently matched timestamped quote published.

Source analysis [^4VhbYlfC7Gs]; no independently matched timestamped quote published.

Source analysis [^AGkzpxMdPn8]; no independently matched timestamped quote published.

Source analysis [^AQv3qRCG6Gw]; no independently matched timestamped quote published.

> never saw it." Internal success is not external proof.
> — 13:37 [^BInpv7lGp1o]

Source analysis [^CLttOU7n6sI]; no independently matched timestamped quote published.

Source analysis [^HN-F-OQe6j0]; no independently matched timestamped quote published.

> that whenever a model tells us that a task has been completed, there is
> — 11:04 [^MLhAA9yguwM]

> Passing every test in simulation doesn't prove that Dora actually helps someone
> — 15:29 [^McknwOzbmyg]

Source analysis [^TeErpYBUIeM]; no independently matched timestamped quote published.

Source analysis [^U00AOI1eJUE]; no independently matched timestamped quote published.

Source analysis [^W76woOYHlvY]; no independently matched timestamped quote published.

Source analysis [^bI8WyG9YB0I]; no independently matched timestamped quote published.

Source analysis [^dYh7TQkuYFE]; no independently matched timestamped quote published.

Source analysis [^fmZWvE7yDZo]; no independently matched timestamped quote published.

> right now, it's an investment that pays off as soon as you start multiplying
> — 07:21 [^iRcX54EO5g8]

> ultimately it is the harness that decides. And so, for his A specifically,
> — 04:26 [^m24UKZomm7k]

Source analysis [^n97BCfyFIvw]; no independently matched timestamped quote published.

Source analysis [^oixzVKMAXG0]; no independently matched timestamped quote published.

> Analyze repository health by running get and file system scripts to find stale
> — 42:55 [^pFsfax19yOM]

> termination condition, right? So, when is an AI feature or an agent is good
> — 11:39 [^pSto5YaNGUo]

Source analysis [^so9l_MwS2yg]; no independently matched timestamped quote published.

> in a case like this, the generator and verifier gap is really small. If I had a
> — 16:05 [^u6q-byPWUuo]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2JX6JYyQG4Y]: [Perception Agents — Antje Barth, Amazon AGI Lab](https://www.youtube.com/watch?v=2JX6JYyQG4Y); publication: 2026-07-23T16:00:06Z; analysis: `analysis/2JX6JYyQG4Y.json`.
[^4VhbYlfC7Gs]: [Malleable Evals: Why Are We Evaluating Adaptive Systems with Static Tests? — Vincent Koc, OpenClaw](https://www.youtube.com/watch?v=4VhbYlfC7Gs); publication: 2026-05-12T16:00:06Z; analysis: `analysis/4VhbYlfC7Gs.json`.
[^AGkzpxMdPn8]: [Most Enterprise Agentic Projects Are Doomed, Here's Why — Jess Grogan-Avignon & Jack Wang, Accenture](https://www.youtube.com/watch?v=AGkzpxMdPn8); publication: 2026-05-28T21:00:02Z; analysis: `analysis/AGkzpxMdPn8.json`.
[^AQv3qRCG6Gw]: [Reinforcement Learning without Verifiable Rewards — Will Brown, Prime Intellect](https://www.youtube.com/watch?v=AQv3qRCG6Gw); publication: 2026-07-31T15:00:06Z; analysis: `analysis/AQv3qRCG6Gw.json`.
[^BInpv7lGp1o]: [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](https://www.youtube.com/watch?v=BInpv7lGp1o); publication: 2026-07-29T16:00:06Z; analysis: `analysis/BInpv7lGp1o.json`.
[^CLttOU7n6sI]: [Respect The Process - Andrew Dumit, Watershed Technology Inc.](https://www.youtube.com/watch?v=CLttOU7n6sI); publication: 2026-07-07T23:31:49Z; analysis: `analysis/CLttOU7n6sI.json`.
[^HN-F-OQe6j0]: [Defying Gravity - Kevin Hou, Google DeepMind](https://www.youtube.com/watch?v=HN-F-OQe6j0); publication: 2025-12-02T22:51:09Z; analysis: `analysis/HN-F-OQe6j0.json`.
[^MLhAA9yguwM]: [The 3 Pillars of Autonomy – Michele Catasta, Replit](https://www.youtube.com/watch?v=MLhAA9yguwM); publication: 2025-12-22T16:30:06Z; analysis: `analysis/MLhAA9yguwM.json`.
[^McknwOzbmyg]: [Shipping AI to a Million Patients Without an A/B Test — Jared Joselowitz, Ufonia](https://www.youtube.com/watch?v=McknwOzbmyg); publication: 2026-08-19T15:00:31Z; analysis: `analysis/McknwOzbmyg.json`.
[^TeErpYBUIeM]: [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](https://www.youtube.com/watch?v=TeErpYBUIeM); publication: 2026-10-06T17:00:19Z; analysis: `analysis/TeErpYBUIeM.json`.
[^U00AOI1eJUE]: [Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz](https://www.youtube.com/watch?v=U00AOI1eJUE); publication: 2026-04-08T00:45:06Z; analysis: `analysis/U00AOI1eJUE.json`.
[^W76woOYHlvY]: [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](https://www.youtube.com/watch?v=W76woOYHlvY); publication: 2026-05-02T21:00:06Z; analysis: `analysis/W76woOYHlvY.json`.
[^bI8WyG9YB0I]: [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](https://www.youtube.com/watch?v=bI8WyG9YB0I); publication: 2026-10-11T19:00:11Z; analysis: `analysis/bI8WyG9YB0I.json`.
[^dYh7TQkuYFE]: [I Believe Everything My Agents Tell Me: Three Levels of Review — Corey Gallon, Rexmore](https://www.youtube.com/watch?v=dYh7TQkuYFE); publication: 2026-10-13T12:00:08Z; analysis: `analysis/dYh7TQkuYFE.json`.
[^fmZWvE7yDZo]: [UX Design Principles for Semi Autonomous Multi Agent Systems — Victor Dibia, Microsoft](https://www.youtube.com/watch?v=fmZWvE7yDZo); publication: 2025-07-21T19:11:17Z; analysis: `analysis/fmZWvE7yDZo.json`.
[^iRcX54EO5g8]: [Your agent is blindfolded — Johan Lajili, Poolside AI](https://www.youtube.com/watch?v=iRcX54EO5g8); publication: 2026-07-08T13:45:06Z; analysis: `analysis/iRcX54EO5g8.json`.
[^m24UKZomm7k]: [Don't Let the LLM Drive - Ornella Bahidika & Joel Allou, Microsoft](https://www.youtube.com/watch?v=m24UKZomm7k); publication: 2026-07-20T06:25:18Z; analysis: `analysis/m24UKZomm7k.json`.
[^n97BCfyFIvw]: ["The engineer of the future is the person who chooses what is worth doing." — Addy Osmani, Anthropic](https://www.youtube.com/watch?v=n97BCfyFIvw); publication: 2026-07-14T17:16:43Z; analysis: `analysis/n97BCfyFIvw.json`.
[^oixzVKMAXG0]: [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=oixzVKMAXG0); publication: 2026-10-12T15:00:19Z; analysis: `analysis/oixzVKMAXG0.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^pSto5YaNGUo]: [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](https://www.youtube.com/watch?v=pSto5YaNGUo); publication: 2026-06-29T01:30:19Z; analysis: `analysis/pSto5YaNGUo.json`.
[^so9l_MwS2yg]: [Your Attention Is the Bottleneck, Not Your Agents — Zack Proser, WorkOS](https://www.youtube.com/watch?v=so9l_MwS2yg); publication: 2026-06-11T14:00:06Z; analysis: `analysis/so9l_MwS2yg.json`.
[^u6q-byPWUuo]: [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](https://www.youtube.com/watch?v=u6q-byPWUuo); publication: 2026-08-19T14:00:06Z; analysis: `analysis/u6q-byPWUuo.json`.
