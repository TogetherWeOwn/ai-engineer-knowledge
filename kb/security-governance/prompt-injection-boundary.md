---
{
  "type": "technique",
  "id": "prompt-injection-boundary",
  "title": "Treat retrieved content and tool results as untrusted data, not authority",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-11T13:30:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "FCi4jT86gSw",
      "resource": "https://www.youtube.com/watch?v=FCi4jT86gSw",
      "title": "MCP Is Not Good Yet — David Cramer, Sentry",
      "author": "David Cramer, Sentry",
      "last_modified": "2025-07-03T16:00:06Z",
      "analysis_file": "analysis/FCi4jT86gSw.json"
    },
    {
      "id": "GVbPiq3Pet0",
      "resource": "https://www.youtube.com/watch?v=GVbPiq3Pet0",
      "title": "Building security around ML: Dr. Andrew Davis",
      "author": null,
      "last_modified": "2025-02-08T21:31:25Z",
      "analysis_file": "analysis/GVbPiq3Pet0.json"
    },
    {
      "id": "L4I7WgiEquo",
      "resource": "https://www.youtube.com/watch?v=L4I7WgiEquo",
      "title": "AI in GTM at Notion — Flora Liu",
      "author": "Flora Liu",
      "last_modified": "2026-08-26T14:00:05Z",
      "analysis_file": "analysis/L4I7WgiEquo.json"
    },
    {
      "id": "NdrSPm6NCdk",
      "resource": "https://www.youtube.com/watch?v=NdrSPm6NCdk",
      "title": "Evals in AI: A Deep Dive — Tejas Kumar, IBM",
      "author": "Tejas Kumar, IBM",
      "last_modified": "2026-10-05T17:00:22Z",
      "analysis_file": "analysis/NdrSPm6NCdk.json"
    },
    {
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "YZHPEkfy2kc",
      "resource": "https://www.youtube.com/watch?v=YZHPEkfy2kc",
      "title": "$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpintero",
      "author": "Diego Carpintero",
      "last_modified": "2026-04-16T11:00:07Z",
      "analysis_file": "analysis/YZHPEkfy2kc.json"
    },
    {
      "id": "_B4Pv9ttFgY",
      "resource": "https://www.youtube.com/watch?v=_B4Pv9ttFgY",
      "title": "Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google",
      "author": "Michael Hablich, Google",
      "last_modified": "2026-06-05T17:00:06Z",
      "analysis_file": "analysis/_B4Pv9ttFgY.json"
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
      "id": "jdeMJJ_oNYg",
      "resource": "https://www.youtube.com/watch?v=jdeMJJ_oNYg",
      "title": "LLM Safeguards: Security Privacy Compliance Anti Hallucination: Daniel Whitenack",
      "author": null,
      "last_modified": "2024-12-31T17:28:40Z",
      "analysis_file": "analysis/jdeMJJ_oNYg.json"
    },
    {
      "id": "p-2MT8KYZqU",
      "resource": "https://www.youtube.com/watch?v=p-2MT8KYZqU",
      "title": "AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk",
      "author": "Micah Silverman, Snyk",
      "last_modified": "2026-10-11T13:30:04Z",
      "analysis_file": "analysis/p-2MT8KYZqU.json"
    },
    {
      "id": "yWS0udrIOc8",
      "resource": "https://www.youtube.com/watch?v=yWS0udrIOc8",
      "title": "Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town",
      "author": "Steve Yegge, Gas Town",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/yWS0udrIOc8.json"
    },
    {
      "id": "zMiSRliEzv4",
      "resource": "https://www.youtube.com/watch?v=zMiSRliEzv4",
      "title": "Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog",
      "author": "Joshua Snyder, PostHog",
      "last_modified": "2026-06-10T13:00:17Z",
      "analysis_file": "analysis/zMiSRliEzv4.json"
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

# Treat retrieved content and tool results as untrusted data, not authority

## What

Treat retrieved content and tool results as untrusted data, not authority

Separate tool-returned content from executable instructions so embedded commands cannot acquire the caller’s authority.

## Evidence

Source analysis [^FCi4jT86gSw]; no independently matched timestamped quote published.

Source analysis [^GVbPiq3Pet0]; no independently matched timestamped quote published.

Source analysis [^L4I7WgiEquo]; no independently matched timestamped quote published.

> supposed to treat all tool call results as um non-instructional. It's just data,
> — 04:31 [^NdrSPm6NCdk]

> connecting this agent that has shell access and you're doing web fetch that's
> — 28:03 [^RFKCzGlAU6Q]

Source analysis [^YZHPEkfy2kc]; no independently matched timestamped quote published.

> uh make sure that they have the domain allow list and don't prompt injection
> — 20:55 [^_B4Pv9ttFgY]

> readme it has a huge caveat uh, which is this action is not hardened against
> — 20:50 [^_mi3alkqy4s]

Source analysis [^jdeMJJ_oNYg]; no independently matched timestamped quote published.

Source analysis [^p-2MT8KYZqU]; no independently matched timestamped quote published.

> Um I mean, I don't have any good answers
> — 21:36 [^yWS0udrIOc8]

> classifier that's going to check is this trying to do something bad?
> — 04:25 [^zMiSRliEzv4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^FCi4jT86gSw]: [MCP Is Not Good Yet — David Cramer, Sentry](https://www.youtube.com/watch?v=FCi4jT86gSw); publication: 2025-07-03T16:00:06Z; analysis: `analysis/FCi4jT86gSw.json`.
[^GVbPiq3Pet0]: [Building security around ML: Dr. Andrew Davis](https://www.youtube.com/watch?v=GVbPiq3Pet0); publication: 2025-02-08T21:31:25Z; analysis: `analysis/GVbPiq3Pet0.json`.
[^L4I7WgiEquo]: [AI in GTM at Notion — Flora Liu](https://www.youtube.com/watch?v=L4I7WgiEquo); publication: 2026-08-26T14:00:05Z; analysis: `analysis/L4I7WgiEquo.json`.
[^NdrSPm6NCdk]: [Evals in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=NdrSPm6NCdk); publication: 2026-10-05T17:00:22Z; analysis: `analysis/NdrSPm6NCdk.json`.
[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^YZHPEkfy2kc]: [$1 AI Guardrails: The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpintero](https://www.youtube.com/watch?v=YZHPEkfy2kc); publication: 2026-04-16T11:00:07Z; analysis: `analysis/YZHPEkfy2kc.json`.
[^_B4Pv9ttFgY]: [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](https://www.youtube.com/watch?v=_B4Pv9ttFgY); publication: 2026-06-05T17:00:06Z; analysis: `analysis/_B4Pv9ttFgY.json`.
[^_mi3alkqy4s]: [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s); publication: 2026-09-30T13:30:35Z; analysis: `analysis/_mi3alkqy4s.json`.
[^jdeMJJ_oNYg]: [LLM Safeguards: Security Privacy Compliance Anti Hallucination: Daniel Whitenack](https://www.youtube.com/watch?v=jdeMJJ_oNYg); publication: 2024-12-31T17:28:40Z; analysis: `analysis/jdeMJJ_oNYg.json`.
[^p-2MT8KYZqU]: [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](https://www.youtube.com/watch?v=p-2MT8KYZqU); publication: 2026-10-11T13:30:04Z; analysis: `analysis/p-2MT8KYZqU.json`.
[^yWS0udrIOc8]: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/yWS0udrIOc8.json`.
[^zMiSRliEzv4]: [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](https://www.youtube.com/watch?v=zMiSRliEzv4); publication: 2026-06-10T13:00:17Z; analysis: `analysis/zMiSRliEzv4.json`.
