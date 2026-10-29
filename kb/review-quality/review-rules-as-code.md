---
{
  "type": "technique",
  "id": "review-rules-as-code",
  "title": "Convert repeatable conventions into lint, tests and governed rule assets",
  "area": "review-quality",
  "status": "stable",
  "valid_from": "2026-10-11T16:00:29Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-AKPRSYccJc",
      "resource": "https://www.youtube.com/watch?v=-AKPRSYccJc",
      "title": "How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI",
      "author": "Nnenna Ndukwe, Qodo AI",
      "last_modified": "2026-10-11T16:00:29Z",
      "analysis_file": "analysis/-AKPRSYccJc.json"
    },
    {
      "id": "7GMKdpLsxwU",
      "resource": "https://www.youtube.com/watch?v=7GMKdpLsxwU",
      "title": "The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI",
      "author": "Hassan El Mghari, Together AI",
      "last_modified": "2026-08-21T15:00:06Z",
      "analysis_file": "analysis/7GMKdpLsxwU.json"
    },
    {
      "id": "E3KbFLAGD6A",
      "resource": "https://www.youtube.com/watch?v=E3KbFLAGD6A",
      "title": "Stop Prompting — Greg Pstrucha, Sentry",
      "author": "Greg Pstrucha, Sentry",
      "last_modified": "2026-10-09T14:00:20Z",
      "analysis_file": "analysis/E3KbFLAGD6A.json"
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
      "id": "kWOQS3XPZ10",
      "resource": "https://www.youtube.com/watch?v=kWOQS3XPZ10",
      "title": "Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode",
      "author": "Ahmad Awais, CommandCode",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/kWOQS3XPZ10.json"
    },
    {
      "id": "pSqpC7fFLZA",
      "resource": "https://www.youtube.com/watch?v=pSqpC7fFLZA",
      "title": "The Robots are coming for your job, and that's okay - Elmer Thomas and Maria Bermudez",
      "author": "Elmer Thomas and Maria Bermudez",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/pSqpC7fFLZA.json"
    },
    {
      "id": "rgjF5o2Qjsc",
      "resource": "https://www.youtube.com/watch?v=rgjF5o2Qjsc",
      "title": "The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo",
      "author": "Itamar Friedman, Qodo",
      "last_modified": "2025-12-11T21:58:59Z",
      "analysis_file": "analysis/rgjF5o2Qjsc.json"
    },
    {
      "id": "s-aixZYJG4c",
      "resource": "https://www.youtube.com/watch?v=s-aixZYJG4c",
      "title": "The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo",
      "author": "Itamar Friedman, Qodo",
      "last_modified": "2026-08-20T13:30:38Z",
      "analysis_file": "analysis/s-aixZYJG4c.json"
    },
    {
      "id": "wEc9aG7cRQc",
      "resource": "https://www.youtube.com/watch?v=wEc9aG7cRQc",
      "title": "Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog",
      "author": "Diane Lin, Datadog",
      "last_modified": "2026-07-20T06:25:22Z",
      "analysis_file": "analysis/wEc9aG7cRQc.json"
    },
    {
      "id": "whue9_YquGA",
      "resource": "https://www.youtube.com/watch?v=whue9_YquGA",
      "title": "Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation",
      "author": "Angie Jones, Agentic AI Foundation",
      "last_modified": "2026-06-28T19:00:10Z",
      "analysis_file": "analysis/whue9_YquGA.json"
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

# Convert repeatable conventions into lint, tests and governed rule assets

## What

Convert repeatable conventions into lint, tests and governed rule assets

Agents have no memory and repeat the same elementary mistakes, and compaction erases corrections. Writing a linter is now cheap because the agent writes it. So, on a schedule, mine past transcripts and review comments for repeated feedback and codify the deterministic ones as lint rules, e.g. design-system component use, OpenAPI decorators, or skill code blocks that must type-check. Expect whack-a-mole: the agent first dodged the rule by deleting the code blocks, then the backticks.

## Evidence

Source analysis [^-AKPRSYccJc]; no independently matched timestamped quote published.

Source analysis [^7GMKdpLsxwU]; no independently matched timestamped quote published.

Source analysis [^E3KbFLAGD6A]; no independently matched timestamped quote published.

> model to not do as unknown as X. It found that never is a bottom type. So
> — 39:41 [^Wmp2Tku2PrI]

> example would be no bare catch rules. Great.
> — 12:44 [^_Zcw_sVF6hU]

Source analysis [^kWOQS3XPZ10]; no independently matched timestamped quote published.

Source analysis [^pSqpC7fFLZA]; no independently matched timestamped quote published.

Source analysis [^rgjF5o2Qjsc]; no independently matched timestamped quote published.

> adding more rules for blocking and more rules for
> — 17:01 [^s-aixZYJG4c]

Source analysis [^wEc9aG7cRQc]; no independently matched timestamped quote published.

> repeatable workflows like slash commands and later agent skills,
> — 09:23 [^whue9_YquGA]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer redundant or low-value review rounds
- **Speed:** Shorter evidence-backed review/repair cycles
- **Quality:** Better focus on actionable defects rather than cosmetic scores
- **Reliability:** Independent, revision-bound verification
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-AKPRSYccJc]: [How to Build Quality Gates into Agentic Coding Workflows — Nnenna Ndukwe, Qodo AI](https://www.youtube.com/watch?v=-AKPRSYccJc); publication: 2026-10-11T16:00:29Z; analysis: `analysis/-AKPRSYccJc.json`.
[^7GMKdpLsxwU]: [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](https://www.youtube.com/watch?v=7GMKdpLsxwU); publication: 2026-08-21T15:00:06Z; analysis: `analysis/7GMKdpLsxwU.json`.
[^E3KbFLAGD6A]: [Stop Prompting — Greg Pstrucha, Sentry](https://www.youtube.com/watch?v=E3KbFLAGD6A); publication: 2026-10-09T14:00:20Z; analysis: `analysis/E3KbFLAGD6A.json`.
[^Wmp2Tku2PrI]: [Vibe Engineering Effect Apps — Michael Arnaldi, Effectful](https://www.youtube.com/watch?v=Wmp2Tku2PrI); publication: 2026-05-07T15:00:06Z; analysis: `analysis/Wmp2Tku2PrI.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^kWOQS3XPZ10]: [Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode](https://www.youtube.com/watch?v=kWOQS3XPZ10); publication: 2025-11-24T20:16:36Z; analysis: `analysis/kWOQS3XPZ10.json`.
[^pSqpC7fFLZA]: [The Robots are coming for your job, and that's okay - Elmer Thomas and Maria Bermudez](https://www.youtube.com/watch?v=pSqpC7fFLZA); publication: 2025-06-03T22:22:29Z; analysis: `analysis/pSqpC7fFLZA.json`.
[^rgjF5o2Qjsc]: [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=rgjF5o2Qjsc); publication: 2025-12-11T21:58:59Z; analysis: `analysis/rgjF5o2Qjsc.json`.
[^s-aixZYJG4c]: [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=s-aixZYJG4c); publication: 2026-08-20T13:30:38Z; analysis: `analysis/s-aixZYJG4c.json`.
[^wEc9aG7cRQc]: [Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog](https://www.youtube.com/watch?v=wEc9aG7cRQc); publication: 2026-07-20T06:25:22Z; analysis: `analysis/wEc9aG7cRQc.json`.
[^whue9_YquGA]: [Building an Autonomous Engineering Org - Angie Jones, Agentic AI Foundation](https://www.youtube.com/watch?v=whue9_YquGA); publication: 2026-06-28T19:00:10Z; analysis: `analysis/whue9_YquGA.json`.
