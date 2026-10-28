---
{
  "type": "technique",
  "id": "implicit-feedback-labels",
  "title": "Use downstream accepted, rejected and repaired outcomes as noisy labels",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-11T19:00:11Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2wgPHvW0mG8",
      "resource": "https://www.youtube.com/watch?v=2wgPHvW0mG8",
      "title": "One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio",
      "author": "Suchet Bargoti, Skydio",
      "last_modified": "2026-09-24T15:00:35Z",
      "analysis_file": "analysis/2wgPHvW0mG8.json"
    },
    {
      "id": "42q8OmAF_Gw",
      "resource": "https://www.youtube.com/watch?v=42q8OmAF_Gw",
      "title": "What It Actually Takes to Deploy GenAI Applications to Enterprises: Arjun Bansal and Trey Doig",
      "author": null,
      "last_modified": "2024-11-04T20:48:26Z",
      "analysis_file": "analysis/42q8OmAF_Gw.json"
    },
    {
      "id": "7Dtu2bilcFs",
      "resource": "https://www.youtube.com/watch?v=7Dtu2bilcFs",
      "title": "2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding",
      "author": "Steve Yegge & Gene Kim, Authors, Vibe Coding",
      "last_modified": "2025-12-06T16:30:06Z",
      "analysis_file": "analysis/7Dtu2bilcFs.json"
    },
    {
      "id": "A48uhxfxbsM",
      "resource": "https://www.youtube.com/watch?v=A48uhxfxbsM",
      "title": "Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2026-05-07T17:00:06Z",
      "analysis_file": "analysis/A48uhxfxbsM.json"
    },
    {
      "id": "B0fjR3yaZFU",
      "resource": "https://www.youtube.com/watch?v=B0fjR3yaZFU",
      "title": "How do you diffuse AI into the real world? — Varun Shenoy, Long Lake",
      "author": "Varun Shenoy, Long Lake",
      "last_modified": "2026-08-28T17:30:33Z",
      "analysis_file": "analysis/B0fjR3yaZFU.json"
    },
    {
      "id": "B8l81jhvHbI",
      "resource": "https://www.youtube.com/watch?v=B8l81jhvHbI",
      "title": "Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla",
      "author": "Ishita Daga, Tesla",
      "last_modified": "2026-07-20T06:25:12Z",
      "analysis_file": "analysis/B8l81jhvHbI.json"
    },
    {
      "id": "LzeC1AQ-U5o",
      "resource": "https://www.youtube.com/watch?v=LzeC1AQ-U5o",
      "title": "Building Blocks for LLM Systems & Products: Eugene Yan",
      "author": null,
      "last_modified": "2023-11-02T13:08:20Z",
      "analysis_file": "analysis/LzeC1AQ-U5o.json"
    },
    {
      "id": "RmJ4rTLV_x4",
      "resource": "https://www.youtube.com/watch?v=RmJ4rTLV_x4",
      "title": "Your Support Team Should Ship Code – Lisa Orr, Zapier",
      "author": "Lisa Orr, Zapier",
      "last_modified": "2025-12-16T17:00:06Z",
      "analysis_file": "analysis/RmJ4rTLV_x4.json"
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
      "id": "X1kp-ABIIxQ",
      "resource": "https://www.youtube.com/watch?v=X1kp-ABIIxQ",
      "title": "Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest",
      "author": "Dan Farrelly, CTO, Inngest",
      "last_modified": "2026-07-21T03:14:22Z",
      "analysis_file": "analysis/X1kp-ABIIxQ.json"
    },
    {
      "id": "_mi3alkqy4s",
      "resource": "https://www.youtube.com/watch?v=_mi3alkqy4s",
      "title": "The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-09-30T13:30:35Z",
      "analysis_file": "analysis/_mi3alkqy4s.json"
    },
    {
      "id": "aHhB3sjGjkI",
      "resource": "https://www.youtube.com/watch?v=aHhB3sjGjkI",
      "title": "Agents Building Agents - Alfonso Graziano, Nearform",
      "author": "Alfonso Graziano, Nearform",
      "last_modified": "2026-06-28T16:00:34Z",
      "analysis_file": "analysis/aHhB3sjGjkI.json"
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
      "id": "blrovBxxN9o",
      "resource": "https://www.youtube.com/watch?v=blrovBxxN9o",
      "title": "Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier",
      "author": "Rafal Willinski, Vitor Balocco, Zapier",
      "last_modified": "2025-06-30T17:15:06Z",
      "analysis_file": "analysis/blrovBxxN9o.json"
    },
    {
      "id": "eXA2tjRZIbY",
      "resource": "https://www.youtube.com/watch?v=eXA2tjRZIbY",
      "title": "The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI",
      "author": "Varun Krovvidi, Resolve AI",
      "last_modified": "2026-10-06T23:30:36Z",
      "analysis_file": "analysis/eXA2tjRZIbY.json"
    },
    {
      "id": "gvIAkmZUEZY",
      "resource": "https://www.youtube.com/watch?v=gvIAkmZUEZY",
      "title": "Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code",
      "author": "Beyang Liu, Amp Code",
      "last_modified": "2025-12-22T17:00:06Z",
      "analysis_file": "analysis/gvIAkmZUEZY.json"
    },
    {
      "id": "jJQoVkd5yLg",
      "resource": "https://www.youtube.com/watch?v=jJQoVkd5yLg",
      "title": "Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto",
      "author": "Abhi Arya, Reducto",
      "last_modified": "2026-10-08T17:00:23Z",
      "analysis_file": "analysis/jJQoVkd5yLg.json"
    },
    {
      "id": "mpzktdYTcdE",
      "resource": "https://www.youtube.com/watch?v=mpzktdYTcdE",
      "title": "E-Values Evaluating the Values of AI: Sheila Gulati and Nischal Nadhamuni",
      "author": null,
      "last_modified": "2024-12-31T17:25:58Z",
      "analysis_file": "analysis/mpzktdYTcdE.json"
    },
    {
      "id": "q4Tr-DknG2M",
      "resource": "https://www.youtube.com/watch?v=q4Tr-DknG2M",
      "title": "Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI",
      "author": "Lee Robinson, Cursor, SpaceXAI",
      "last_modified": "2026-07-15T20:13:51Z",
      "analysis_file": "analysis/q4Tr-DknG2M.json"
    },
    {
      "id": "u6q-byPWUuo",
      "resource": "https://www.youtube.com/watch?v=u6q-byPWUuo",
      "title": "From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge",
      "author": "Chaitanya Asawa, Abridge",
      "last_modified": "2026-08-19T14:00:06Z",
      "analysis_file": "analysis/u6q-byPWUuo.json"
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

# Use downstream accepted, rejected and repaired outcomes as noisy labels

## What

Use downstream accepted, rejected and repaired outcomes as noisy labels

Developer resolution decisions provide useful data for improving checks but are not themselves defect truth.

## Evidence

Source analysis [^2wgPHvW0mG8]; no independently matched timestamped quote published.

Source analysis [^42q8OmAF_Gw]; no independently matched timestamped quote published.

Source analysis [^7Dtu2bilcFs]; no independently matched timestamped quote published.

Source analysis [^A48uhxfxbsM]; no independently matched timestamped quote published.

Source analysis [^B0fjR3yaZFU]; no independently matched timestamped quote published.

Source analysis [^B8l81jhvHbI]; no independently matched timestamped quote published.

Source analysis [^LzeC1AQ-U5o]; no independently matched timestamped quote published.

> they can simply chat with the uh scout agent in gitlab that'll kick off another
> — 12:24 [^RmJ4rTLV_x4]

Source analysis [^TeErpYBUIeM]; no independently matched timestamped quote published.

> wait for additional events and attach them to the sessions that you're
> — 17:45 [^X1kp-ABIIxQ]

> calls it the resolution rate and it has driven it from 52% to over 70%. Um
> — 14:28 [^_mi3alkqy4s]

Source analysis [^aHhB3sjGjkI]; no independently matched timestamped quote published.

Source analysis [^bI8WyG9YB0I]; no independently matched timestamped quote published.

> So, if they do turn it on, that's actually really strong positive implicit
> — 04:51 [^blrovBxxN9o]

> days and go look at their last interaction with your product before
> — 06:07 [^blrovBxxN9o]

Source analysis [^eXA2tjRZIbY]; no independently matched timestamped quote published.

Source analysis [^gvIAkmZUEZY]; no independently matched timestamped quote published.

> behaving. Where humans overrode the agent, where
> — 13:25 [^jJQoVkd5yLg]

Source analysis [^mpzktdYTcdE]; no independently matched timestamped quote published.

> we want to zoom in on one specific part of that rollout, and ideally we can hint
> — 10:34 [^q4Tr-DknG2M]

> whether how you're editing the clinical note and your typical thumbs up, thumbs
> — 14:33 [^u6q-byPWUuo]

> judgment. Not just a score, but the reasoning and
> — 15:04 [^yqF6XhzbWBk]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2wgPHvW0mG8]: [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](https://www.youtube.com/watch?v=2wgPHvW0mG8); publication: 2026-09-24T15:00:35Z; analysis: `analysis/2wgPHvW0mG8.json`.
[^42q8OmAF_Gw]: [What It Actually Takes to Deploy GenAI Applications to Enterprises: Arjun Bansal and Trey Doig](https://www.youtube.com/watch?v=42q8OmAF_Gw); publication: 2024-11-04T20:48:26Z; analysis: `analysis/42q8OmAF_Gw.json`.
[^7Dtu2bilcFs]: [2026: The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding](https://www.youtube.com/watch?v=7Dtu2bilcFs); publication: 2025-12-06T16:30:06Z; analysis: `analysis/7Dtu2bilcFs.json`.
[^A48uhxfxbsM]: [Agent Optimization with Pydantic AI: GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=A48uhxfxbsM); publication: 2026-05-07T17:00:06Z; analysis: `analysis/A48uhxfxbsM.json`.
[^B0fjR3yaZFU]: [How do you diffuse AI into the real world? — Varun Shenoy, Long Lake](https://www.youtube.com/watch?v=B0fjR3yaZFU); publication: 2026-08-28T17:30:33Z; analysis: `analysis/B0fjR3yaZFU.json`.
[^B8l81jhvHbI]: [Enterprise Agents Have a Structure Problem - Ishita Daga, Tesla](https://www.youtube.com/watch?v=B8l81jhvHbI); publication: 2026-07-20T06:25:12Z; analysis: `analysis/B8l81jhvHbI.json`.
[^LzeC1AQ-U5o]: [Building Blocks for LLM Systems & Products: Eugene Yan](https://www.youtube.com/watch?v=LzeC1AQ-U5o); publication: 2023-11-02T13:08:20Z; analysis: `analysis/LzeC1AQ-U5o.json`.
[^RmJ4rTLV_x4]: [Your Support Team Should Ship Code – Lisa Orr, Zapier](https://www.youtube.com/watch?v=RmJ4rTLV_x4); publication: 2025-12-16T17:00:06Z; analysis: `analysis/RmJ4rTLV_x4.json`.
[^TeErpYBUIeM]: [The Self-Improving OSS Agent Stack — Marc Klingen, Langfuse](https://www.youtube.com/watch?v=TeErpYBUIeM); publication: 2026-10-06T17:00:19Z; analysis: `analysis/TeErpYBUIeM.json`.
[^X1kp-ABIIxQ]: [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ); publication: 2026-07-21T03:14:22Z; analysis: `analysis/X1kp-ABIIxQ.json`.
[^_mi3alkqy4s]: [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s); publication: 2026-09-30T13:30:35Z; analysis: `analysis/_mi3alkqy4s.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^bI8WyG9YB0I]: [SonarQube + OpenAI: Agentic Development — Killian Carlsen-Phelan, Sonar](https://www.youtube.com/watch?v=bI8WyG9YB0I); publication: 2026-10-11T19:00:11Z; analysis: `analysis/bI8WyG9YB0I.json`.
[^blrovBxxN9o]: [Turning Fails into Features: Zapier’s Hard-Won Eval Lessons — Rafal Willinski, Vitor Balocco, Zapier](https://www.youtube.com/watch?v=blrovBxxN9o); publication: 2025-06-30T17:15:06Z; analysis: `analysis/blrovBxxN9o.json`.
[^eXA2tjRZIbY]: [The 6 Pillars of an Agentic Harness for Production — Varun Krovvidi, Resolve AI](https://www.youtube.com/watch?v=eXA2tjRZIbY); publication: 2026-10-06T23:30:36Z; analysis: `analysis/eXA2tjRZIbY.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
[^jJQoVkd5yLg]: [Why We Deleted Our MCP Server and Rebuilt It — Abhi Arya, Reducto](https://www.youtube.com/watch?v=jJQoVkd5yLg); publication: 2026-10-08T17:00:23Z; analysis: `analysis/jJQoVkd5yLg.json`.
[^mpzktdYTcdE]: [E-Values Evaluating the Values of AI: Sheila Gulati and Nischal Nadhamuni](https://www.youtube.com/watch?v=mpzktdYTcdE); publication: 2024-12-31T17:25:58Z; analysis: `analysis/mpzktdYTcdE.json`.
[^q4Tr-DknG2M]: [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](https://www.youtube.com/watch?v=q4Tr-DknG2M); publication: 2026-07-15T20:13:51Z; analysis: `analysis/q4Tr-DknG2M.json`.
[^u6q-byPWUuo]: [From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge](https://www.youtube.com/watch?v=u6q-byPWUuo); publication: 2026-08-19T14:00:06Z; analysis: `analysis/u6q-byPWUuo.json`.
[^yqF6XhzbWBk]: [Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo](https://www.youtube.com/watch?v=yqF6XhzbWBk); publication: 2026-08-22T17:00:32Z; analysis: `analysis/yqF6XhzbWBk.json`.
