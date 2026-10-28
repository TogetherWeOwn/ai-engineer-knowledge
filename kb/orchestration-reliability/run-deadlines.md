---
{
  "type": "technique",
  "id": "run-deadlines",
  "title": "Bound run lifetime and require a terminal outcome",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-17T09:00:27Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-a2oTS9J67U",
      "resource": "https://www.youtube.com/watch?v=-a2oTS9J67U",
      "title": "The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale",
      "author": "Michele Grant, Leading at Scale",
      "last_modified": "2026-10-13T16:00:11Z",
      "analysis_file": "analysis/-a2oTS9J67U.json"
    },
    {
      "id": "5eJqXtevlXg",
      "resource": "https://www.youtube.com/watch?v=5eJqXtevlXg",
      "title": "Hacking Subagents Into Codex CLI — Brian John, Betterup",
      "author": "Brian John, Betterup",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/5eJqXtevlXg.json"
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
      "id": "RjfbvDXpFls",
      "resource": "https://www.youtube.com/watch?v=RjfbvDXpFls",
      "title": "Building pi in a World of Slop — Mario Zechner",
      "author": "Mario Zechner",
      "last_modified": "2026-04-16T22:58:06Z",
      "analysis_file": "analysis/RjfbvDXpFls.json"
    },
    {
      "id": "Ti-BmGU1_mQ",
      "resource": "https://www.youtube.com/watch?v=Ti-BmGU1_mQ",
      "title": "The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI",
      "author": "Eugene Cheah, Featherless AI",
      "last_modified": "2026-10-17T09:00:27Z",
      "analysis_file": "analysis/Ti-BmGU1_mQ.json"
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
      "id": "aeTb5BdmTTc",
      "resource": "https://www.youtube.com/watch?v=aeTb5BdmTTc",
      "title": "Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab",
      "author": "Aditya Khandelwal, Amazon AGI Lab",
      "last_modified": "2026-08-11T00:03:17Z",
      "analysis_file": "analysis/aeTb5BdmTTc.json"
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
      "id": "cQQbJqvZkpo",
      "resource": "https://www.youtube.com/watch?v=cQQbJqvZkpo",
      "title": "Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave",
      "author": "Sitanshu Gupta, CoreWeave",
      "last_modified": "2026-09-19T16:30:34Z",
      "analysis_file": "analysis/cQQbJqvZkpo.json"
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
      "id": "flf_IKnFYnE",
      "resource": "https://www.youtube.com/watch?v=flf_IKnFYnE",
      "title": "From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/flf_IKnFYnE.json"
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
      "id": "jc3kbZkuHTo",
      "resource": "https://www.youtube.com/watch?v=jc3kbZkuHTo",
      "title": "The Human Is an Async API — Melanie Warrick, Temporal",
      "author": "Melanie Warrick, Temporal",
      "last_modified": "2026-10-04T16:30:17Z",
      "analysis_file": "analysis/jc3kbZkuHTo.json"
    },
    {
      "id": "oVsEddfhdxc",
      "resource": "https://www.youtube.com/watch?v=oVsEddfhdxc",
      "title": "We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect",
      "author": "Elie Bakouch, Prime Intellect",
      "last_modified": "2026-09-26T17:30:10Z",
      "analysis_file": "analysis/oVsEddfhdxc.json"
    },
    {
      "id": "ro5HkZvzfiQ",
      "resource": "https://www.youtube.com/watch?v=ro5HkZvzfiQ",
      "title": "The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:",
      "author": "Almog Baku:",
      "last_modified": "2025-02-22T15:00:06Z",
      "analysis_file": "analysis/ro5HkZvzfiQ.json"
    },
    {
      "id": "zrZ1amZBSPw",
      "resource": "https://www.youtube.com/watch?v=zrZ1amZBSPw",
      "title": "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio",
      "author": "Kanish Manuja, Twilio",
      "last_modified": "2026-08-28T15:30:03Z",
      "analysis_file": "analysis/zrZ1amZBSPw.json"
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

# Bound run lifetime and require a terminal outcome

## What

Bound run lifetime and require a terminal outcome

A run waiting on an event that cannot arrive must end in a recorded terminal state (success, failure, timeout, cancel or max attempts), and recovery must not queue behind the stuck work.

## Evidence

Source analysis [^-a2oTS9J67U]; no independently matched timestamped quote published.

Source analysis [^5eJqXtevlXg]; no independently matched timestamped quote published.

> Runs needs deadlines and cancellation. A deadline bounds the weight. Watchdog
> — 10:45 [^BInpv7lGp1o]

> I embed uh issues and pull request texts into 3D space, so I see clusters of
> — 11:47 [^RjfbvDXpFls]

Source analysis [^Ti-BmGU1_mQ]; no independently matched timestamped quote published.

Source analysis [^W76woOYHlvY]; no independently matched timestamped quote published.

Source analysis [^aeTb5BdmTTc]; no independently matched timestamped quote published.

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

Source analysis [^cQQbJqvZkpo]; no independently matched timestamped quote published.

> that's when a hook triggers the agent and it will check that temp file to see
> — 06:06 [^cgimkNGNjvU]

> activities obviously have to run again from scratch. And so once that finishes
> — 20:16 [^flf_IKnFYnE]

Source analysis [^gvIAkmZUEZY]; no independently matched timestamped quote published.

Source analysis [^jc3kbZkuHTo]; no independently matched timestamped quote published.

Source analysis [^oVsEddfhdxc]; no independently matched timestamped quote published.

Source analysis [^ro5HkZvzfiQ]; no independently matched timestamped quote published.

> It's a lie. You should be tracking your P99 per model per route, not a gateway
> — 07:25 [^zrZ1amZBSPw]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-a2oTS9J67U]: [The Agent Works. Does Anyone Trust It? — Michele Grant, Leading at Scale](https://www.youtube.com/watch?v=-a2oTS9J67U); publication: 2026-10-13T16:00:11Z; analysis: `analysis/-a2oTS9J67U.json`.
[^5eJqXtevlXg]: [Hacking Subagents Into Codex CLI — Brian John, Betterup](https://www.youtube.com/watch?v=5eJqXtevlXg); publication: 2025-11-24T20:16:36Z; analysis: `analysis/5eJqXtevlXg.json`.
[^BInpv7lGp1o]: [The Model Was Right. The Harness Failed. — Vinoth Govindarajan, OpenAI](https://www.youtube.com/watch?v=BInpv7lGp1o); publication: 2026-07-29T16:00:06Z; analysis: `analysis/BInpv7lGp1o.json`.
[^RjfbvDXpFls]: [Building pi in a World of Slop — Mario Zechner](https://www.youtube.com/watch?v=RjfbvDXpFls); publication: 2026-04-16T22:58:06Z; analysis: `analysis/RjfbvDXpFls.json`.
[^Ti-BmGU1_mQ]: [The AI Bill Is Too Damn High: Tokenomics 101 — Eugene Cheah, Featherless AI](https://www.youtube.com/watch?v=Ti-BmGU1_mQ); publication: 2026-10-17T09:00:27Z; analysis: `analysis/Ti-BmGU1_mQ.json`.
[^W76woOYHlvY]: [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](https://www.youtube.com/watch?v=W76woOYHlvY); publication: 2026-05-02T21:00:06Z; analysis: `analysis/W76woOYHlvY.json`.
[^aeTb5BdmTTc]: [Agents, codebases, and teams — Aditya Khandelwal, Amazon AGI Lab](https://www.youtube.com/watch?v=aeTb5BdmTTc); publication: 2026-08-11T00:03:17Z; analysis: `analysis/aeTb5BdmTTc.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^cQQbJqvZkpo]: [Vertical Mobility: Inference from MVP to Trillion-Parameter Workloads — Sitanshu Gupta, CoreWeave](https://www.youtube.com/watch?v=cQQbJqvZkpo); publication: 2026-09-19T16:30:34Z; analysis: `analysis/cQQbJqvZkpo.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
[^flf_IKnFYnE]: [From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/flf_IKnFYnE.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
[^jc3kbZkuHTo]: [The Human Is an Async API — Melanie Warrick, Temporal](https://www.youtube.com/watch?v=jc3kbZkuHTo); publication: 2026-10-04T16:30:17Z; analysis: `analysis/jc3kbZkuHTo.json`.
[^oVsEddfhdxc]: [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](https://www.youtube.com/watch?v=oVsEddfhdxc); publication: 2026-09-26T17:30:10Z; analysis: `analysis/oVsEddfhdxc.json`.
[^ro5HkZvzfiQ]: [The LLM Triangle: Engineering Principles for Robust AI Applications - Almog Baku:](https://www.youtube.com/watch?v=ro5HkZvzfiQ); publication: 2025-02-22T15:00:06Z; analysis: `analysis/ro5HkZvzfiQ.json`.
[^zrZ1amZBSPw]: [Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons — Kanish Manuja, Twilio](https://www.youtube.com/watch?v=zrZ1amZBSPw); publication: 2026-08-28T15:30:03Z; analysis: `analysis/zrZ1amZBSPw.json`.
