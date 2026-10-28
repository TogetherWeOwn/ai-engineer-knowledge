---
{
  "type": "technique",
  "id": "hard-vs-preference-rubrics",
  "title": "Separate hard correctness predicates from subjective preference judgments",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-22T07:00:28Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "IJXjTLPzvAU",
      "resource": "https://www.youtube.com/watch?v=IJXjTLPzvAU",
      "title": "The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen",
      "author": "Jacob E. Thomas, Results Gen",
      "last_modified": "2026-06-25T16:30:06Z",
      "analysis_file": "analysis/IJXjTLPzvAU.json"
    },
    {
      "id": "XyV6bSMyq-I",
      "resource": "https://www.youtube.com/watch?v=XyV6bSMyq-I",
      "title": "How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases",
      "author": "Zubin Aysola, Weights & Biases",
      "last_modified": "2026-09-26T16:00:08Z",
      "analysis_file": "analysis/XyV6bSMyq-I.json"
    },
    {
      "id": "_dTF3NpPzGo",
      "resource": "https://www.youtube.com/watch?v=_dTF3NpPzGo",
      "title": "Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI",
      "author": "Louis-François Bouchard, Towards AI",
      "last_modified": "2026-10-22T07:00:28Z",
      "analysis_file": "analysis/_dTF3NpPzGo.json"
    },
    {
      "id": "a4BV0gGmXgA",
      "resource": "https://www.youtube.com/watch?v=a4BV0gGmXgA",
      "title": "Five hard earned lessons about Evals — Ankur Goyal, Braintrust",
      "author": "Ankur Goyal, Braintrust",
      "last_modified": "2025-08-23T17:45:06Z",
      "analysis_file": "analysis/a4BV0gGmXgA.json"
    },
    {
      "id": "bDQn1w0idXs",
      "resource": "https://www.youtube.com/watch?v=bDQn1w0idXs",
      "title": "The AI Pivot: With Chris White of Prefect & Bryan Bischof of Hex",
      "author": null,
      "last_modified": "2023-11-07T19:45:58Z",
      "analysis_file": "analysis/bDQn1w0idXs.json"
    },
    {
      "id": "hkhDdcM5V94",
      "resource": "https://www.youtube.com/watch?v=hkhDdcM5V94",
      "title": "Building with Anthropic Claude: Prompt Workshop with Zack Witten",
      "author": null,
      "last_modified": "2024-08-17T15:24:49Z",
      "analysis_file": "analysis/hkhDdcM5V94.json"
    },
    {
      "id": "jvKf6zXrNO4",
      "resource": "https://www.youtube.com/watch?v=jvKf6zXrNO4",
      "title": "Prompt Engineering is Dead — Nir Gazit, Traceloop",
      "author": "Nir Gazit, Traceloop",
      "last_modified": "2025-06-27T09:34:55Z",
      "analysis_file": "analysis/jvKf6zXrNO4.json"
    },
    {
      "id": "qZj7sqmidqA",
      "resource": "https://www.youtube.com/watch?v=qZj7sqmidqA",
      "title": "From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-05T22:00:36Z",
      "analysis_file": "analysis/qZj7sqmidqA.json"
    },
    {
      "id": "vW8wLsb3Nnc",
      "resource": "https://www.youtube.com/watch?v=vW8wLsb3Nnc",
      "title": "POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent",
      "author": "Randall Hunt, Caylent",
      "last_modified": "2025-07-23T15:50:56Z",
      "analysis_file": "analysis/vW8wLsb3Nnc.json"
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

# Separate hard correctness predicates from subjective preference judgments

## What

Separate hard correctness predicates from subjective preference judgments

Use absolute pass/fail for required outcomes and a separate comparative axis for preferences such as when to ask questions.

## Evidence

Source analysis [^IJXjTLPzvAU]; no independently matched timestamped quote published.

> we pass a task or not and then relativistically where we can set styles
> — 10:18 [^XyV6bSMyq-I]

Source analysis [^_dTF3NpPzGo]; no independently matched timestamped quote published.

Source analysis [^a4BV0gGmXgA]; no independently matched timestamped quote published.

> you know human way boil it down to Binary yes or Nos and run your evals and
> — 29:26 [^bDQn1w0idXs]

> nice subject it's more likely to say that it's good in always like it's a
> — 1:21:58 [^hkhDdcM5V94]

Source analysis [^jvKf6zXrNO4]; no independently matched timestamped quote published.

> response should do, then stop. That is six evaluators, not one.
> — 1:19:25 [^qZj7sqmidqA]

Source analysis [^vW8wLsb3Nnc]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^IJXjTLPzvAU]: [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals - Jacob E. Thomas, Results Gen](https://www.youtube.com/watch?v=IJXjTLPzvAU); publication: 2026-06-25T16:30:06Z; analysis: `analysis/IJXjTLPzvAU.json`.
[^XyV6bSMyq-I]: [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](https://www.youtube.com/watch?v=XyV6bSMyq-I); publication: 2026-09-26T16:00:08Z; analysis: `analysis/XyV6bSMyq-I.json`.
[^_dTF3NpPzGo]: [Why AI Writing Still Reads Like Slop — Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=_dTF3NpPzGo); publication: 2026-10-22T07:00:28Z; analysis: `analysis/_dTF3NpPzGo.json`.
[^a4BV0gGmXgA]: [Five hard earned lessons about Evals — Ankur Goyal, Braintrust](https://www.youtube.com/watch?v=a4BV0gGmXgA); publication: 2025-08-23T17:45:06Z; analysis: `analysis/a4BV0gGmXgA.json`.
[^bDQn1w0idXs]: [The AI Pivot: With Chris White of Prefect & Bryan Bischof of Hex](https://www.youtube.com/watch?v=bDQn1w0idXs); publication: 2023-11-07T19:45:58Z; analysis: `analysis/bDQn1w0idXs.json`.
[^hkhDdcM5V94]: [Building with Anthropic Claude: Prompt Workshop with Zack Witten](https://www.youtube.com/watch?v=hkhDdcM5V94); publication: 2024-08-17T15:24:49Z; analysis: `analysis/hkhDdcM5V94.json`.
[^jvKf6zXrNO4]: [Prompt Engineering is Dead — Nir Gazit, Traceloop](https://www.youtube.com/watch?v=jvKf6zXrNO4); publication: 2025-06-27T09:34:55Z; analysis: `analysis/jvKf6zXrNO4.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^vW8wLsb3Nnc]: [POC to PROD: Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent](https://www.youtube.com/watch?v=vW8wLsb3Nnc); publication: 2025-07-23T15:50:56Z; analysis: `analysis/vW8wLsb3Nnc.json`.
