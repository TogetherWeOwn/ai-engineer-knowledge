---
{
  "type": "technique",
  "id": "multi-turn-scenarios",
  "title": "Evaluate clarification, resumption and stateful multi-turn behavior",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-09-26T16:30:29Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "OC04sP_QgTI",
      "resource": "https://www.youtube.com/watch?v=OC04sP_QgTI",
      "title": "Ensure AI Agents Work: Evaluation Frameworks for Scaling Success — Aparna Dhinkaran, CEO Arize",
      "author": "Aparna Dhinkaran, CEO Arize",
      "last_modified": "2025-04-23T16:00:06Z",
      "analysis_file": "analysis/OC04sP_QgTI.json"
    },
    {
      "id": "Qvp9vw4jJQ8",
      "resource": "https://www.youtube.com/watch?v=Qvp9vw4jJQ8",
      "title": "Break It 'Til You Make It: Building the Self-Improving Stack for AI Agents - Aparna Dhinakaran",
      "author": "Aparna Dhinakaran",
      "last_modified": "2025-06-10T17:30:11Z",
      "analysis_file": "analysis/Qvp9vw4jJQ8.json"
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
      "id": "fOtTHWeU6B8",
      "resource": "https://www.youtube.com/watch?v=fOtTHWeU6B8",
      "title": "How Zapier Builds AI Products and Features with the Help of Braintrust: Ankur Goyal & Olmo Maldonado",
      "author": null,
      "last_modified": "2024-11-07T20:11:02Z",
      "analysis_file": "analysis/fOtTHWeU6B8.json"
    },
    {
      "id": "iNkFlCiij0U",
      "resource": "https://www.youtube.com/watch?v=iNkFlCiij0U",
      "title": "The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI",
      "author": "Vincent Chen, Snorkel AI",
      "last_modified": "2026-06-04T16:00:06Z",
      "analysis_file": "analysis/iNkFlCiij0U.json"
    },
    {
      "id": "x4e5O9zN0TE",
      "resource": "https://www.youtube.com/watch?v=x4e5O9zN0TE",
      "title": "Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati",
      "author": "Erina Karati",
      "last_modified": "2026-09-26T16:30:29Z",
      "analysis_file": "analysis/x4e5O9zN0TE.json"
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

# Evaluate clarification, resumption and stateful multi-turn behavior

## What

Evaluate clarification, resumption and stateful multi-turn behavior

Single-prompt tests miss failures that appear only after ordered user messages, clarifications or interruptions.

## Evidence

> and so you don't want to be talking to an agent that forgets what you
> — 05:29 [^OC04sP_QgTI]

Source analysis [^Qvp9vw4jJQ8]; no independently matched timestamped quote published.

> certain questions in a particular order so that we can simulate multi-turn
> — 11:39 [^XyV6bSMyq-I]

> before but we're also testing steps we're also configuring Fields um all as
> — 09:15 [^fOtTHWeU6B8]

Source analysis [^iNkFlCiij0U]; no independently matched timestamped quote published.

> evaluating one answer. We were evaluating an entire run.
> — 09:15 [^x4e5O9zN0TE]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^OC04sP_QgTI]: [Ensure AI Agents Work: Evaluation Frameworks for Scaling Success — Aparna Dhinkaran, CEO Arize](https://www.youtube.com/watch?v=OC04sP_QgTI); publication: 2025-04-23T16:00:06Z; analysis: `analysis/OC04sP_QgTI.json`.
[^Qvp9vw4jJQ8]: [Break It 'Til You Make It: Building the Self-Improving Stack for AI Agents - Aparna Dhinakaran](https://www.youtube.com/watch?v=Qvp9vw4jJQ8); publication: 2025-06-10T17:30:11Z; analysis: `analysis/Qvp9vw4jJQ8.json`.
[^XyV6bSMyq-I]: [How We Built an Agent That Improves Itself — Zubin Aysola, Weights & Biases](https://www.youtube.com/watch?v=XyV6bSMyq-I); publication: 2026-09-26T16:00:08Z; analysis: `analysis/XyV6bSMyq-I.json`.
[^fOtTHWeU6B8]: [How Zapier Builds AI Products and Features with the Help of Braintrust: Ankur Goyal & Olmo Maldonado](https://www.youtube.com/watch?v=fOtTHWeU6B8); publication: 2024-11-07T20:11:02Z; analysis: `analysis/fOtTHWeU6B8.json`.
[^iNkFlCiij0U]: [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](https://www.youtube.com/watch?v=iNkFlCiij0U); publication: 2026-06-04T16:00:06Z; analysis: `analysis/iNkFlCiij0U.json`.
[^x4e5O9zN0TE]: [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](https://www.youtube.com/watch?v=x4e5O9zN0TE); publication: 2026-09-26T16:30:29Z; analysis: `analysis/x4e5O9zN0TE.json`.
