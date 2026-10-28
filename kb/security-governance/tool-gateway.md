---
{
  "type": "technique",
  "id": "tool-gateway",
  "title": "Centralize tool authentication, policy and catalog vetting in a supported gateway",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-11T17:30:25Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1tpqdglI3T0",
      "resource": "https://www.youtube.com/watch?v=1tpqdglI3T0",
      "title": "Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog",
      "author": "Michael Forrester, Accenture & Whitney Lee, Datadog",
      "last_modified": "2026-10-11T17:30:25Z",
      "analysis_file": "analysis/1tpqdglI3T0.json"
    },
    {
      "id": "5qNXdLbEdew",
      "resource": "https://www.youtube.com/watch?v=5qNXdLbEdew",
      "title": "AI Platform Engineering: Patrick Debois",
      "author": null,
      "last_modified": "2024-12-31T17:20:37Z",
      "analysis_file": "analysis/5qNXdLbEdew.json"
    },
    {
      "id": "I3znWC3MEXM",
      "resource": "https://www.youtube.com/watch?v=I3znWC3MEXM",
      "title": "It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard",
      "author": "Kim Maida, Keycard",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/I3znWC3MEXM.json"
    },
    {
      "id": "Q81AzlA-VE8",
      "resource": "https://www.youtube.com/watch?v=Q81AzlA-VE8",
      "title": "What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg",
      "author": "Lei Zhang, Bloomberg",
      "last_modified": "2025-12-16T15:00:07Z",
      "analysis_file": "analysis/Q81AzlA-VE8.json"
    },
    {
      "id": "VXfRt_H-V08",
      "resource": "https://www.youtube.com/watch?v=VXfRt_H-V08",
      "title": "One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca",
      "author": "Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca",
      "last_modified": "2026-04-10T11:30:06Z",
      "analysis_file": "analysis/VXfRt_H-V08.json"
    },
    {
      "id": "WJjInLeaJjo",
      "resource": "https://www.youtube.com/watch?v=WJjInLeaJjo",
      "title": "Building Agents at Cloud Scale — Antje Barth, AWS",
      "author": "Antje Barth, AWS",
      "last_modified": "2025-08-02T18:15:06Z",
      "analysis_file": "analysis/WJjInLeaJjo.json"
    },
    {
      "id": "blW-lSd5CYQ",
      "resource": "https://www.youtube.com/watch?v=blW-lSd5CYQ",
      "title": "The rise of the agentic economy on the shoulders of MCP — Jan Curn, Apify",
      "author": "Jan Curn, Apify",
      "last_modified": "2025-07-18T18:59:57Z",
      "analysis_file": "analysis/blW-lSd5CYQ.json"
    },
    {
      "id": "vRFqbEzzDsI",
      "resource": "https://www.youtube.com/watch?v=vRFqbEzzDsI",
      "title": "Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza",
      "author": "Julián Duque & Anush Dsouza",
      "last_modified": "2025-06-27T09:38:08Z",
      "analysis_file": "analysis/vRFqbEzzDsI.json"
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

# Centralize tool authentication, policy and catalog vetting in a supported gateway

## What

Centralize tool authentication, policy and catalog vetting in a supported gateway

They decouple MCP servers from local stdio by deploying them as Lambda/streamable-HTTP services behind an MCP gateway.

## Evidence

Source analysis [^1tpqdglI3T0]; no independently matched timestamped quote published.

Source analysis [^5qNXdLbEdew]; no independently matched timestamped quote published.

Source analysis [^I3znWC3MEXM]; no independently matched timestamped quote published.

Source analysis [^Q81AzlA-VE8]; no independently matched timestamped quote published.

Source analysis [^VXfRt_H-V08]; no independently matched timestamped quote published.

Source analysis [^WJjInLeaJjo]; no independently matched timestamped quote published.

Source analysis [^blW-lSd5CYQ]; no independently matched timestamped quote published.

Source analysis [^vRFqbEzzDsI]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1tpqdglI3T0]: [Build a Platform and Watch It Burn — Michael Forrester, Accenture & Whitney Lee, Datadog](https://www.youtube.com/watch?v=1tpqdglI3T0); publication: 2026-10-11T17:30:25Z; analysis: `analysis/1tpqdglI3T0.json`.
[^5qNXdLbEdew]: [AI Platform Engineering: Patrick Debois](https://www.youtube.com/watch?v=5qNXdLbEdew); publication: 2024-12-31T17:20:37Z; analysis: `analysis/5qNXdLbEdew.json`.
[^I3znWC3MEXM]: [It's 10pm. Do You Know Where Your Agents Are? — Kim Maida, Keycard](https://www.youtube.com/watch?v=I3znWC3MEXM); publication: 2026-07-20T17:17:53Z; analysis: `analysis/I3znWC3MEXM.json`.
[^Q81AzlA-VE8]: [What We Learned Deploying AI within Bloomberg’s Engineering Organization – Lei Zhang, Bloomberg](https://www.youtube.com/watch?v=Q81AzlA-VE8); publication: 2025-12-16T15:00:07Z; analysis: `analysis/Q81AzlA-VE8.json`.
[^VXfRt_H-V08]: [One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca](https://www.youtube.com/watch?v=VXfRt_H-V08); publication: 2026-04-10T11:30:06Z; analysis: `analysis/VXfRt_H-V08.json`.
[^WJjInLeaJjo]: [Building Agents at Cloud Scale — Antje Barth, AWS](https://www.youtube.com/watch?v=WJjInLeaJjo); publication: 2025-08-02T18:15:06Z; analysis: `analysis/WJjInLeaJjo.json`.
[^blW-lSd5CYQ]: [The rise of the agentic economy on the shoulders of MCP — Jan Curn, Apify](https://www.youtube.com/watch?v=blW-lSd5CYQ); publication: 2025-07-18T18:59:57Z; analysis: `analysis/blW-lSd5CYQ.json`.
[^vRFqbEzzDsI]: [Building Agentic Applications w/ Heroku Managed Inference and Agents — Julián Duque & Anush Dsouza](https://www.youtube.com/watch?v=vRFqbEzzDsI); publication: 2025-06-27T09:38:08Z; analysis: `analysis/vRFqbEzzDsI.json`.
