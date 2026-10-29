---
{
  "type": "technique",
  "id": "execution-control-separation",
  "title": "Separate worker execution resources from durable orchestration and control-plane state",
  "area": "sandbox-compute",
  "status": "stable",
  "valid_from": "2026-10-20T19:00:34Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1izYWsokr9s",
      "resource": "https://www.youtube.com/watch?v=1izYWsokr9s",
      "title": "Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal",
      "author": "Preeti Somal, Temporal",
      "last_modified": "2025-07-28T15:15:00Z",
      "analysis_file": "analysis/1izYWsokr9s.json"
    },
    {
      "id": "7c9FSUVcXR0",
      "resource": "https://www.youtube.com/watch?v=7c9FSUVcXR0",
      "title": "Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta",
      "author": "Nishant Gupta & Naman Ahuja, Meta",
      "last_modified": "2026-09-19T15:00:10Z",
      "analysis_file": "analysis/7c9FSUVcXR0.json"
    },
    {
      "id": "_-oIuRH4oGA",
      "resource": "https://www.youtube.com/watch?v=_-oIuRH4oGA",
      "title": "How agents broke app-level infrastructure - Evan Boyle",
      "author": "Evan Boyle",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/_-oIuRH4oGA.json"
    },
    {
      "id": "adfw3xJBx1o",
      "resource": "https://www.youtube.com/watch?v=adfw3xJBx1o",
      "title": "A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo",
      "author": "Felipe Felisola Caso & Francesco Galletta, Monzo",
      "last_modified": "2026-10-20T19:00:34Z",
      "analysis_file": "analysis/adfw3xJBx1o.json"
    },
    {
      "id": "k8cnVCMYmNc",
      "resource": "https://www.youtube.com/watch?v=k8cnVCMYmNc",
      "title": "OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal",
      "author": "Cornelia Davis, Temporal",
      "last_modified": "2026-01-12T19:30:06Z",
      "analysis_file": "analysis/k8cnVCMYmNc.json"
    },
    {
      "id": "uFPAtKIN-FQ",
      "resource": "https://www.youtube.com/watch?v=uFPAtKIN-FQ",
      "title": "Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri",
      "author": null,
      "last_modified": "2025-06-11T16:57:37Z",
      "analysis_file": "analysis/uFPAtKIN-FQ.json"
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

# Separate worker execution resources from durable orchestration and control-plane state

## What

Separate worker execution resources from durable orchestration and control-plane state

Persist pending work and let independent workers pull bounded activities instead of tying every workflow to one long-lived monolithic process.

## Evidence

Source analysis [^1izYWsokr9s]; no independently matched timestamped quote published.

Source analysis [^7c9FSUVcXR0]; no independently matched timestamped quote published.

Source analysis [^_-oIuRH4oGA]; no independently matched timestamped quote published.

Source analysis [^adfw3xJBx1o]; no independently matched timestamped quote published.

> are just pulling other things off of the queue.
> — 52:09 [^k8cnVCMYmNc]

Source analysis [^uFPAtKIN-FQ]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reduce avoidable idle and duplicated compute
- **Speed:** Reduce measured execution/queue bottlenecks
- **Quality:** Reproducible command and environment evidence
- **Reliability:** Isolation, cleanup and recovery guarantees
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1izYWsokr9s]: [Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal](https://www.youtube.com/watch?v=1izYWsokr9s); publication: 2025-07-28T15:15:00Z; analysis: `analysis/1izYWsokr9s.json`.
[^7c9FSUVcXR0]: [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](https://www.youtube.com/watch?v=7c9FSUVcXR0); publication: 2026-09-19T15:00:10Z; analysis: `analysis/7c9FSUVcXR0.json`.
[^_-oIuRH4oGA]: [How agents broke app-level infrastructure - Evan Boyle](https://www.youtube.com/watch?v=_-oIuRH4oGA); publication: 2025-06-03T22:22:28Z; analysis: `analysis/_-oIuRH4oGA.json`.
[^adfw3xJBx1o]: [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](https://www.youtube.com/watch?v=adfw3xJBx1o); publication: 2026-10-20T19:00:34Z; analysis: `analysis/adfw3xJBx1o.json`.
[^k8cnVCMYmNc]: [OpenAI + @Temporalio : Building Durable, Production Ready Agents - Cornelia Davis, Temporal](https://www.youtube.com/watch?v=k8cnVCMYmNc); publication: 2026-01-12T19:30:06Z; analysis: `analysis/k8cnVCMYmNc.json`.
[^uFPAtKIN-FQ]: [Exposing Agents as MCP servers with mcp-agent: Sarmad Qadri](https://www.youtube.com/watch?v=uFPAtKIN-FQ); publication: 2025-06-11T16:57:37Z; analysis: `analysis/uFPAtKIN-FQ.json`.
