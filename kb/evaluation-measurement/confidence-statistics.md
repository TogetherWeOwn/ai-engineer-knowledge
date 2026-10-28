---
{
  "type": "technique",
  "id": "confidence-statistics",
  "title": "Report sample size, confidence intervals and detectable error rates",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-14T15:00:14Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "8g1N_a3h9H0",
      "resource": "https://www.youtube.com/watch?v=8g1N_a3h9H0",
      "title": "How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival",
      "author": "Alvin Pane, OutRival",
      "last_modified": "2026-10-14T15:00:14Z",
      "analysis_file": "analysis/8g1N_a3h9H0.json"
    },
    {
      "id": "AN65uc645mE",
      "resource": "https://www.youtube.com/watch?v=AN65uc645mE",
      "title": "200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI",
      "author": "Vivek Muppalla, Hippocratic AI",
      "last_modified": "2026-08-19T16:00:06Z",
      "analysis_file": "analysis/AN65uc645mE.json"
    },
    {
      "id": "CTLa_p6iOiY",
      "resource": "https://www.youtube.com/watch?v=CTLa_p6iOiY",
      "title": "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs",
      "author": "Pierluca D'Oro, Programma Labs",
      "last_modified": "2026-08-14T14:30:31Z",
      "analysis_file": "analysis/CTLa_p6iOiY.json"
    },
    {
      "id": "RhfqQKe22ZA",
      "resource": "https://www.youtube.com/watch?v=RhfqQKe22ZA",
      "title": "Why Agent Hype can fall short of reality – Joel Becker, METR",
      "author": "Joel Becker, METR",
      "last_modified": "2025-12-24T16:30:06Z",
      "analysis_file": "analysis/RhfqQKe22ZA.json"
    },
    {
      "id": "WXy8Yy9xGss",
      "resource": "https://www.youtube.com/watch?v=WXy8Yy9xGss",
      "title": "CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed",
      "author": "Nathan Sobo, Zed",
      "last_modified": "2025-06-27T09:22:37Z",
      "analysis_file": "analysis/WXy8Yy9xGss.json"
    },
    {
      "id": "Xfl50508LZM",
      "resource": "https://www.youtube.com/watch?v=Xfl50508LZM",
      "title": "Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize",
      "author": "Laurie Voss, Arize",
      "last_modified": "2026-05-14T18:00:06Z",
      "analysis_file": "analysis/Xfl50508LZM.json"
    },
    {
      "id": "YnNF55QV0zs",
      "resource": "https://www.youtube.com/watch?v=YnNF55QV0zs",
      "title": "Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai",
      "author": "Ishan Anand, InsightSciences.ai",
      "last_modified": "2026-07-29T20:15:35Z",
      "analysis_file": "analysis/YnNF55QV0zs.json"
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
      "id": "oVsEddfhdxc",
      "resource": "https://www.youtube.com/watch?v=oVsEddfhdxc",
      "title": "We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect",
      "author": "Elie Bakouch, Prime Intellect",
      "last_modified": "2026-09-26T17:30:10Z",
      "analysis_file": "analysis/oVsEddfhdxc.json"
    },
    {
      "id": "wHhlvcQgi9M",
      "resource": "https://www.youtube.com/watch?v=wHhlvcQgi9M",
      "title": "7 Habits of Highly Effective Generative AI Evaluations - Justin Muller",
      "author": "Justin Muller",
      "last_modified": "2025-06-03T22:22:29Z",
      "analysis_file": "analysis/wHhlvcQgi9M.json"
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

# Report sample size, confidence intervals and detectable error rates

## What

Report sample size, confidence intervals and detectable error rates

A study’s point estimate does not automatically generalize across model generations, task mixes or workers.

## Evidence

Source analysis [^8g1N_a3h9H0]; no independently matched timestamped quote published.

Source analysis [^AN65uc645mE]; no independently matched timestamped quote published.

Source analysis [^CTLa_p6iOiY]; no independently matched timestamped quote published.

> in nature possibility is, you know, this is a small study. You shouldn't you
> — 18:00 [^RhfqQKe22ZA]

> 100% of these 200 examples to pass or this test should like literally fail the
> — 06:08 [^WXy8Yy9xGss]

Source analysis [^Xfl50508LZM]; no independently matched timestamped quote published.

Source analysis [^YnNF55QV0zs]; no independently matched timestamped quote published.

Source analysis [^iNkFlCiij0U]; no independently matched timestamped quote published.

Source analysis [^oVsEddfhdxc]; no independently matched timestamped quote published.

Source analysis [^wHhlvcQgi9M]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^8g1N_a3h9H0]: [How to Actually Tokenmaxx and Save Millions — Alvin Pane, OutRival](https://www.youtube.com/watch?v=8g1N_a3h9H0); publication: 2026-10-14T15:00:14Z; analysis: `analysis/8g1N_a3h9H0.json`.
[^AN65uc645mE]: [200 Million Patient Interactions Later — Vivek Muppalla, Hippocratic AI](https://www.youtube.com/watch?v=AN65uc645mE); publication: 2026-08-19T16:00:06Z; analysis: `analysis/AN65uc645mE.json`.
[^CTLa_p6iOiY]: [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](https://www.youtube.com/watch?v=CTLa_p6iOiY); publication: 2026-08-14T14:30:31Z; analysis: `analysis/CTLa_p6iOiY.json`.
[^RhfqQKe22ZA]: [Why Agent Hype can fall short of reality – Joel Becker, METR](https://www.youtube.com/watch?v=RhfqQKe22ZA); publication: 2025-12-24T16:30:06Z; analysis: `analysis/RhfqQKe22ZA.json`.
[^WXy8Yy9xGss]: [CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed](https://www.youtube.com/watch?v=WXy8Yy9xGss); publication: 2025-06-27T09:22:37Z; analysis: `analysis/WXy8Yy9xGss.json`.
[^Xfl50508LZM]: [Ship Real Agents: Hands-On Evals for Agentic Applications — Laurie Voss, Arize](https://www.youtube.com/watch?v=Xfl50508LZM); publication: 2026-05-14T18:00:06Z; analysis: `analysis/Xfl50508LZM.json`.
[^YnNF55QV0zs]: [Persona Engineering: A Field Guide to AI Synthetic Personas — Ishan Anand, InsightSciences.ai](https://www.youtube.com/watch?v=YnNF55QV0zs); publication: 2026-07-29T20:15:35Z; analysis: `analysis/YnNF55QV0zs.json`.
[^iNkFlCiij0U]: [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](https://www.youtube.com/watch?v=iNkFlCiij0U); publication: 2026-06-04T16:00:06Z; analysis: `analysis/iNkFlCiij0U.json`.
[^oVsEddfhdxc]: [We Let Claude Code and Codex Race Human Researchers — Elie Bakouch, Prime Intellect](https://www.youtube.com/watch?v=oVsEddfhdxc); publication: 2026-09-26T17:30:10Z; analysis: `analysis/oVsEddfhdxc.json`.
[^wHhlvcQgi9M]: [7 Habits of Highly Effective Generative AI Evaluations - Justin Muller](https://www.youtube.com/watch?v=wHhlvcQgi9M); publication: 2025-06-03T22:22:29Z; analysis: `analysis/wHhlvcQgi9M.json`.
