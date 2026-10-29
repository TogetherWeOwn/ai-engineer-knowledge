---
{
  "type": "technique",
  "id": "single-writer",
  "title": "Serialize writes at each mutable state boundary",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-18T08:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "9u6xvcNJaxc",
      "resource": "https://www.youtube.com/watch?v=9u6xvcNJaxc",
      "title": "The 4 Patterns of AI Native Development — Patrick Debois",
      "author": "Patrick Debois",
      "last_modified": "2025-06-04T07:21:01Z",
      "analysis_file": "analysis/9u6xvcNJaxc.json"
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
      "id": "KUEmEb71vzQ",
      "resource": "https://www.youtube.com/watch?v=KUEmEb71vzQ",
      "title": "Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI",
      "author": "Full Workshop, with Ilan Bigio of OpenAI",
      "last_modified": "2025-04-23T16:00:26Z",
      "analysis_file": "analysis/KUEmEb71vzQ.json"
    },
    {
      "id": "OD13PiXw60o",
      "resource": "https://www.youtube.com/watch?v=OD13PiXw60o",
      "title": "Building Multi agent Systems with Finite State Machines",
      "author": null,
      "last_modified": "2025-02-22T17:00:05Z",
      "analysis_file": "analysis/OD13PiXw60o.json"
    },
    {
      "id": "W-SX_srBa3Y",
      "resource": "https://www.youtube.com/watch?v=W-SX_srBa3Y",
      "title": "Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl",
      "author": "Michael Richman, Cmd+Ctrl",
      "last_modified": "2026-05-24T16:00:06Z",
      "analysis_file": "analysis/W-SX_srBa3Y.json"
    },
    {
      "id": "cI7zfqusmFU",
      "resource": "https://www.youtube.com/watch?v=cI7zfqusmFU",
      "title": "Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate",
      "author": "Giselle van Dongen, Restate",
      "last_modified": "2026-09-14T15:30:30Z",
      "analysis_file": "analysis/cI7zfqusmFU.json"
    },
    {
      "id": "obfPzbapMIM",
      "resource": "https://www.youtube.com/watch?v=obfPzbapMIM",
      "title": "Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse",
      "author": "Doneyli De Jesus & Annabell Schäfer, Langfuse",
      "last_modified": "2026-10-18T08:00:06Z",
      "analysis_file": "analysis/obfPzbapMIM.json"
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
      "id": "tUPPVhBBcoM",
      "resource": "https://www.youtube.com/watch?v=tUPPVhBBcoM",
      "title": "Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp",
      "author": "Zach Lloyd, Warp",
      "last_modified": "2026-09-27T17:30:36Z",
      "analysis_file": "analysis/tUPPVhBBcoM.json"
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

# Serialize writes at each mutable state boundary

## What

Serialize writes at each mutable state boundary

An actor/session key isolates state and queues concurrent mutations to prevent lost updates.

## Evidence

Source analysis [^9u6xvcNJaxc]; no independently matched timestamped quote published.

> and simple. One ordered commit path for one mutable state boundary.
> — 09:12 [^BInpv7lGp1o]

Source analysis [^KUEmEb71vzQ]; no independently matched timestamped quote published.

> parallelism because as I mentioned before the actor uh can only process one
> — 06:35 [^OD13PiXw60o]

Source analysis [^W-SX_srBa3Y]; no independently matched timestamped quote published.

> will guarantee that only one execution is running at a time. So a second
> — 11:15 [^cI7zfqusmFU]

> never did refund anything. So the tool was never called. It was never executed.
> — 02:42 [^obfPzbapMIM]

> run features serially. So there's only one worker or validator
> — 09:51 [^ow1we5PzK-o]

Source analysis [^tUPPVhBBcoM]; no independently matched timestamped quote published.

> can do it with Beads by queuing up enough enough work and having them claim
> — 18:16 [^yWS0udrIOc8]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^9u6xvcNJaxc]: [The 4 Patterns of AI Native Development — Patrick Debois](https://www.youtube.com/watch?v=9u6xvcNJaxc); publication: 2025-06-04T07:21:01Z; analysis: `analysis/9u6xvcNJaxc.json`.
[^BInpv7lGp1o]: [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](https://www.youtube.com/watch?v=BInpv7lGp1o); publication: 2026-07-29T16:00:06Z; analysis: `analysis/BInpv7lGp1o.json`.
[^KUEmEb71vzQ]: [Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI](https://www.youtube.com/watch?v=KUEmEb71vzQ); publication: 2025-04-23T16:00:26Z; analysis: `analysis/KUEmEb71vzQ.json`.
[^OD13PiXw60o]: [Building Multi agent Systems with Finite State Machines](https://www.youtube.com/watch?v=OD13PiXw60o); publication: 2025-02-22T17:00:05Z; analysis: `analysis/OD13PiXw60o.json`.
[^W-SX_srBa3Y]: [Let's Talk About FOMAT: Fear of Missing Agent Time — Michael Richman, Cmd+Ctrl](https://www.youtube.com/watch?v=W-SX_srBa3Y); publication: 2026-05-24T16:00:06Z; analysis: `analysis/W-SX_srBa3Y.json`.
[^cI7zfqusmFU]: [Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate](https://www.youtube.com/watch?v=cI7zfqusmFU); publication: 2026-09-14T15:30:30Z; analysis: `analysis/cI7zfqusmFU.json`.
[^obfPzbapMIM]: [Evals for High-Stakes AI Agents — Doneyli De Jesus & Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=obfPzbapMIM); publication: 2026-10-18T08:00:06Z; analysis: `analysis/obfPzbapMIM.json`.
[^ow1we5PzK-o]: [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](https://www.youtube.com/watch?v=ow1we5PzK-o); publication: 2026-05-06T15:00:06Z; analysis: `analysis/ow1we5PzK-o.json`.
[^tUPPVhBBcoM]: [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](https://www.youtube.com/watch?v=tUPPVhBBcoM); publication: 2026-09-27T17:30:36Z; analysis: `analysis/tUPPVhBBcoM.json`.
[^yWS0udrIOc8]: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/yWS0udrIOc8.json`.
