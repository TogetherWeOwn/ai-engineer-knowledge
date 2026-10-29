---
{
  "type": "technique",
  "id": "security-findings-lifecycle",
  "title": "Track security exposure until verified remediation rather than aging it away",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-08-12T18:00:34Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
    },
    {
      "id": "WqZq8L-v9pA",
      "resource": "https://www.youtube.com/watch?v=WqZq8L-v9pA",
      "title": "What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish",
      "author": "Nick Arcolano, Jellyfish",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/WqZq8L-v9pA.json"
    },
    {
      "id": "jHMiYtjoJfA",
      "resource": "https://www.youtube.com/watch?v=jHMiYtjoJfA",
      "title": "Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop",
      "author": "Ben Hylak, Raindrop",
      "last_modified": "2026-08-12T18:00:34Z",
      "analysis_file": "analysis/jHMiYtjoJfA.json"
    },
    {
      "id": "wjk0ulMAkbc",
      "resource": "https://www.youtube.com/watch?v=wjk0ulMAkbc",
      "title": "Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer",
      "author": null,
      "last_modified": "2026-04-21T14:00:06Z",
      "analysis_file": "analysis/wjk0ulMAkbc.json"
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

# Track security exposure until verified remediation rather than aging it away

## What

Track security exposure until verified remediation rather than aging it away

Unlike ordinary low-impact bugs, dormant vulnerabilities can accumulate risk without visible user complaints.

## Evidence

> would go through commit by commit and it would create a vulnerability patch and
> — 56:23 [^MhHEGMFCEB0]

Source analysis [^WqZq8L-v9pA]; no independently matched timestamped quote published.

Source analysis [^jHMiYtjoJfA]; no independently matched timestamped quote published.

Source analysis [^wjk0ulMAkbc]; no independently matched timestamped quote published.

> The problem compounds over time. Yeah?
> — 06:15 [^yWS0udrIOc8]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^WqZq8L-v9pA]: [What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish](https://www.youtube.com/watch?v=WqZq8L-v9pA); publication: 2025-11-24T20:16:36Z; analysis: `analysis/WqZq8L-v9pA.json`.
[^jHMiYtjoJfA]: [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](https://www.youtube.com/watch?v=jHMiYtjoJfA); publication: 2026-08-12T18:00:34Z; analysis: `analysis/jHMiYtjoJfA.json`.
[^wjk0ulMAkbc]: [Taste & Craft: A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @The Pragmatic Engineer](https://www.youtube.com/watch?v=wjk0ulMAkbc); publication: 2026-04-21T14:00:06Z; analysis: `analysis/wjk0ulMAkbc.json`.
[^yWS0udrIOc8]: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/yWS0udrIOc8.json`.
