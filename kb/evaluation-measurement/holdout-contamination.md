---
{
  "type": "technique",
  "id": "holdout-contamination",
  "title": "Use leakage-resistant held-out and time-split validation",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-20T09:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-npY6XjM8CQ",
      "resource": "https://www.youtube.com/watch?v=-npY6XjM8CQ",
      "title": "When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI",
      "author": "Nick Heiner, Surge AI",
      "last_modified": "2026-08-02T16:30:06Z",
      "analysis_file": "analysis/-npY6XjM8CQ.json"
    },
    {
      "id": "2Wtq2GvUicw",
      "resource": "https://www.youtube.com/watch?v=2Wtq2GvUicw",
      "title": "LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella",
      "author": null,
      "last_modified": "2025-02-08T21:32:17Z",
      "analysis_file": "analysis/2Wtq2GvUicw.json"
    },
    {
      "id": "3ZMUiFaQ3qg",
      "resource": "https://www.youtube.com/watch?v=3ZMUiFaQ3qg",
      "title": "Verifiable Environments for AI in Biology — Kenny Workman, LatchBio",
      "author": "Kenny Workman, LatchBio",
      "last_modified": "2026-07-31T20:00:35Z",
      "analysis_file": "analysis/3ZMUiFaQ3qg.json"
    },
    {
      "id": "Bz1HFxQA1o8",
      "resource": "https://www.youtube.com/watch?v=Bz1HFxQA1o8",
      "title": "Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco",
      "author": "Al Chen, Cisco",
      "last_modified": "2026-10-20T09:00:06Z",
      "analysis_file": "analysis/Bz1HFxQA1o8.json"
    },
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "L4dUFimVDKU",
      "resource": "https://www.youtube.com/watch?v=L4dUFimVDKU",
      "title": "Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa",
      "author": "Ryan Ahern, Exa",
      "last_modified": "2026-10-19T07:00:39Z",
      "analysis_file": "analysis/L4dUFimVDKU.json"
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
      "id": "OA-Mc60Rboo",
      "resource": "https://www.youtube.com/watch?v=OA-Mc60Rboo",
      "title": "Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA",
      "author": "Lakshya A. Agrawal, GEPA",
      "last_modified": "2026-09-26T17:00:06Z",
      "analysis_file": "analysis/OA-Mc60Rboo.json"
    },
    {
      "id": "QuuIywMG4s8",
      "resource": "https://www.youtube.com/watch?v=QuuIywMG4s8",
      "title": "Evals Are Broken, Use Them Anyway — Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-06-06T16:00:00Z",
      "analysis_file": "analysis/QuuIywMG4s8.json"
    },
    {
      "id": "SHMCGrNJJGc",
      "resource": "https://www.youtube.com/watch?v=SHMCGrNJJGc",
      "title": "How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-17T19:00:23Z",
      "analysis_file": "analysis/SHMCGrNJJGc.json"
    },
    {
      "id": "T3SS931wU0I",
      "resource": "https://www.youtube.com/watch?v=T3SS931wU0I",
      "title": "Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust",
      "author": "Braintrust",
      "last_modified": "2026-10-05T15:30:36Z",
      "analysis_file": "analysis/T3SS931wU0I.json"
    },
    {
      "id": "TyPpSRXGhbc",
      "resource": "https://www.youtube.com/watch?v=TyPpSRXGhbc",
      "title": "Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI",
      "author": "Charles Dickens, Snorkel AI",
      "last_modified": "2026-10-10T00:30:10Z",
      "analysis_file": "analysis/TyPpSRXGhbc.json"
    },
    {
      "id": "X4dEHRzBLmc",
      "resource": "https://www.youtube.com/watch?v=X4dEHRzBLmc",
      "title": "Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI",
      "author": "Mahmoud Mabrouk, Agenta AI",
      "last_modified": "2026-04-10T10:00:06Z",
      "analysis_file": "analysis/X4dEHRzBLmc.json"
    },
    {
      "id": "YIxzNZDDy1A",
      "resource": "https://www.youtube.com/watch?v=YIxzNZDDy1A",
      "title": "From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases",
      "author": "Wolfram Ravenwolf, Weights & Biases",
      "last_modified": "2026-10-11T17:00:18Z",
      "analysis_file": "analysis/YIxzNZDDy1A.json"
    },
    {
      "id": "Yk87oUPVaxU",
      "resource": "https://www.youtube.com/watch?v=Yk87oUPVaxU",
      "title": "DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve",
      "author": "James Shi, Datacurve",
      "last_modified": "2026-07-26T18:10:56Z",
      "analysis_file": "analysis/Yk87oUPVaxU.json"
    },
    {
      "id": "Ywl4LsvHKzU",
      "resource": "https://www.youtube.com/watch?v=Ywl4LsvHKzU",
      "title": "RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot",
      "author": "Yuval Belfer and Niv Granot",
      "last_modified": "2025-06-03T22:22:28Z",
      "analysis_file": "analysis/Ywl4LsvHKzU.json"
    },
    {
      "id": "aHhB3sjGjkI",
      "resource": "https://www.youtube.com/watch?v=aHhB3sjGjkI",
      "title": "Agents Building Agents - Alfonso Graziano, Nearform",
      "author": "Alfonso Graziano, Nearform",
      "last_modified": "2026-06-28T16:00:34Z",
      "analysis_file": "analysis/aHhB3sjGjkI.json"
    },
    {
      "id": "b2GqTDWtg6s",
      "resource": "https://www.youtube.com/watch?v=b2GqTDWtg6s",
      "title": "Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering",
      "author": "Anju Kambadur, Bloomberg Head of AI Engineering",
      "last_modified": "2025-04-01T15:06:35Z",
      "analysis_file": "analysis/b2GqTDWtg6s.json"
    },
    {
      "id": "eAXxdtNlK04",
      "resource": "https://www.youtube.com/watch?v=eAXxdtNlK04",
      "title": "Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse",
      "author": "Annabell Schäfer, Langfuse",
      "last_modified": "2026-07-18T20:15:06Z",
      "analysis_file": "analysis/eAXxdtNlK04.json"
    },
    {
      "id": "iCj_ATyThvc",
      "resource": "https://www.youtube.com/watch?v=iCj_ATyThvc",
      "title": "How Autoresearch is changing ML research — Zhengyao Jiang, Weco",
      "author": "Zhengyao Jiang, Weco",
      "last_modified": "2026-07-16T18:08:16Z",
      "analysis_file": "analysis/iCj_ATyThvc.json"
    },
    {
      "id": "jRCpXUjz4CI",
      "resource": "https://www.youtube.com/watch?v=jRCpXUjz4CI",
      "title": "Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute",
      "author": "Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute",
      "last_modified": "2026-07-24T16:00:06Z",
      "analysis_file": "analysis/jRCpXUjz4CI.json"
    },
    {
      "id": "jWq-aZIU0kM",
      "resource": "https://www.youtube.com/watch?v=jWq-aZIU0kM",
      "title": "Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i",
      "author": "Ali Khial, G2i",
      "last_modified": "2026-07-31T16:00:06Z",
      "analysis_file": "analysis/jWq-aZIU0kM.json"
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
      "id": "kiqubc5b5Yo",
      "resource": "https://www.youtube.com/watch?v=kiqubc5b5Yo",
      "title": "Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo",
      "author": "Brendan Rappazzo",
      "last_modified": "2026-07-29T17:06:26Z",
      "analysis_file": "analysis/kiqubc5b5Yo.json"
    },
    {
      "id": "mYSRn6PC1mc",
      "resource": "https://www.youtube.com/watch?v=mYSRn6PC1mc",
      "title": "Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi",
      "author": "Louis-François Bouchard, Paul Iusztin, Samridhi",
      "last_modified": "2026-04-20T18:45:16Z",
      "analysis_file": "analysis/mYSRn6PC1mc.json"
    },
    {
      "id": "pP_dSNz_EdQ",
      "resource": "https://www.youtube.com/watch?v=pP_dSNz_EdQ",
      "title": "The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize",
      "author": "Aparna Dhinakaran, Arize",
      "last_modified": "2025-12-23T17:00:06Z",
      "analysis_file": "analysis/pP_dSNz_EdQ.json"
    },
    {
      "id": "q4Tr-DknG2M",
      "resource": "https://www.youtube.com/watch?v=q4Tr-DknG2M",
      "title": "Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI",
      "author": "Lee Robinson, Cursor, SpaceXAI",
      "last_modified": "2026-07-15T20:13:51Z",
      "analysis_file": "analysis/q4Tr-DknG2M.json"
    },
    {
      "id": "wcUJWP6WpGM",
      "resource": "https://www.youtube.com/watch?v=wcUJWP6WpGM",
      "title": "SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius",
      "author": "Ibragim Badertdinov, Nebius",
      "last_modified": "2026-06-04T14:00:06Z",
      "analysis_file": "analysis/wcUJWP6WpGM.json"
    },
    {
      "id": "xLxhT2ZI7UM",
      "resource": "https://www.youtube.com/watch?v=xLxhT2ZI7UM",
      "title": "Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase",
      "author": "Browserbase",
      "last_modified": "2026-10-05T23:30:05Z",
      "analysis_file": "analysis/xLxhT2ZI7UM.json"
    },
    {
      "id": "xyL2Ltkh-SA",
      "resource": "https://www.youtube.com/watch?v=xyL2Ltkh-SA",
      "title": "How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads",
      "author": "Preetika Bhateja & Daniel Bump, YouTube Ads",
      "last_modified": "2026-07-24T21:00:00Z",
      "analysis_file": "analysis/xyL2Ltkh-SA.json"
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

# Use leakage-resistant held-out and time-split validation

## What

Use leakage-resistant held-out and time-split validation

Use newer real tasks to reduce memorized-solution contamination and exercise repository navigation, tests and multi-turn tool use instead of synthetic long-context concatenation.

## Evidence

Source analysis [^-npY6XjM8CQ]; no independently matched timestamped quote published.

Source analysis [^2Wtq2GvUicw]; no independently matched timestamped quote published.

Source analysis [^3ZMUiFaQ3qg]; no independently matched timestamped quote published.

Source analysis [^Bz1HFxQA1o8]; no independently matched timestamped quote published.

> will very happily cheat and use git to go back to main and try to figure out
> — 1:19:40 [^KhRjivBSwiw]

Source analysis [^L4dUFimVDKU]; no independently matched timestamped quote published.

> This is the important part. The LM has no idea what I said because I want to
> — 38:25 [^NdrSPm6NCdk]

> generalization mode. So there you can do prompt optimization agent architecture
> — 17:24 [^OA-Mc60Rboo]

> And then zone three is the danger zone where it's like you're straight up
> — 16:39 [^QuuIywMG4s8]

> split this up split your evaluators into as many dimensions as you are testing.
> — 1:24:10 [^SHMCGrNJJGc]

> what we also had to do is use the disallowed tools flag to prevent Claude
> — 13:02 [^T3SS931wU0I]

Source analysis [^TyPpSRXGhbc]; no independently matched timestamped quote published.

> there is a little bit of redundancies but there are no redundancies between
> — 24:16 [^X4dEHRzBLmc]

> where a model went out and looked up the solution for the benchmark because
> — 20:50 [^YIxzNZDDy1A]

> have every task authored uh from scratch uh rather than being mined. Um aside
> — 08:41 [^Yk87oUPVaxU]

Source analysis [^Ywl4LsvHKzU]; no independently matched timestamped quote published.

> golden data sets or the scorers just to let the evals pass is not a good
> — 12:40 [^aHhB3sjGjkI]

Source analysis [^b2GqTDWtg6s]; no independently matched timestamped quote published.

Source analysis [^eAXxdtNlK04]; no independently matched timestamped quote published.

Source analysis [^iCj_ATyThvc]; no independently matched timestamped quote published.

> into your repo. And overfitting looks like reward hacking or also just uh
> — 06:32 [^jRCpXUjz4CI]

Source analysis [^jWq-aZIU0kM]; no independently matched timestamped quote published.

> split it into train test uh sets or train test evo sets and then run them
> — 12:55 [^jvKf6zXrNO4]

> private leaderboard, like held-out validation, how's the model performing.
> — 16:27 [^kiqubc5b5Yo]

> but we could have just used any any any other model that gets the job done and
> — 1:44:05 [^mYSRn6PC1mc]

> more because here on online traces, as you can see, it kind of failed.
> — 1:54:17 [^mYSRn6PC1mc]

> then we did kind of a diff comparing you know the old world. So just for you just
> — 08:06 [^pP_dSNz_EdQ]

Source analysis [^q4Tr-DknG2M]; no independently matched timestamped quote published.

> every month we collect only fresh problems from the previous month and
> — 02:33 [^wcUJWP6WpGM]

> that, we remove all the future Git history because previous Git history
> — 11:40 [^wcUJWP6WpGM]

Source analysis [^xLxhT2ZI7UM]; no independently matched timestamped quote published.

> if you have a test set, use it sparingly and also refresh it with prod data.
> — 12:54 [^xyL2Ltkh-SA]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-npY6XjM8CQ]: [When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI](https://www.youtube.com/watch?v=-npY6XjM8CQ); publication: 2026-08-02T16:30:06Z; analysis: `analysis/-npY6XjM8CQ.json`.
[^2Wtq2GvUicw]: [LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella](https://www.youtube.com/watch?v=2Wtq2GvUicw); publication: 2025-02-08T21:32:17Z; analysis: `analysis/2Wtq2GvUicw.json`.
[^3ZMUiFaQ3qg]: [Verifiable Environments for AI in Biology — Kenny Workman, LatchBio](https://www.youtube.com/watch?v=3ZMUiFaQ3qg); publication: 2026-07-31T20:00:35Z; analysis: `analysis/3ZMUiFaQ3qg.json`.
[^Bz1HFxQA1o8]: [Shipping AI Into 5 Major Banks Without a 12-Month Compliance Wait — Al Chen, Cisco](https://www.youtube.com/watch?v=Bz1HFxQA1o8); publication: 2026-10-20T09:00:06Z; analysis: `analysis/Bz1HFxQA1o8.json`.
[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^L4dUFimVDKU]: [Backtest Your Agent Against Yesterday's Web — Ryan Ahern, Exa](https://www.youtube.com/watch?v=L4dUFimVDKU); publication: 2026-10-19T07:00:39Z; analysis: `analysis/L4dUFimVDKU.json`.
[^NdrSPm6NCdk]: [Evals in AI: A Deep Dive — Tejas Kumar, IBM](https://www.youtube.com/watch?v=NdrSPm6NCdk); publication: 2026-10-05T17:00:22Z; analysis: `analysis/NdrSPm6NCdk.json`.
[^OA-Mc60Rboo]: [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo); publication: 2026-09-26T17:00:06Z; analysis: `analysis/OA-Mc60Rboo.json`.
[^QuuIywMG4s8]: [Evals Are Broken, Use Them Anyway — Ara Khan, Cline](https://www.youtube.com/watch?v=QuuIywMG4s8); publication: 2026-06-06T16:00:00Z; analysis: `analysis/QuuIywMG4s8.json`.
[^SHMCGrNJJGc]: [How to Know If Your AI Agent Is Any Good: Evals With Phoenix & Claude — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=SHMCGrNJJGc); publication: 2026-10-17T19:00:23Z; analysis: `analysis/SHMCGrNJJGc.json`.
[^T3SS931wU0I]: [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](https://www.youtube.com/watch?v=T3SS931wU0I); publication: 2026-10-05T15:30:36Z; analysis: `analysis/T3SS931wU0I.json`.
[^TyPpSRXGhbc]: [Small Models, Big Results: Training a Finance Agent for Under $500 — Charles Dickens, Snorkel AI](https://www.youtube.com/watch?v=TyPpSRXGhbc); publication: 2026-10-10T00:30:10Z; analysis: `analysis/TyPpSRXGhbc.json`.
[^X4dEHRzBLmc]: [Judge the Judge: Building LLM Evaluators That Actually Work with GEPA — Mahmoud Mabrouk, Agenta AI](https://www.youtube.com/watch?v=X4dEHRzBLmc); publication: 2026-04-10T10:00:06Z; analysis: `analysis/X4dEHRzBLmc.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^Yk87oUPVaxU]: [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](https://www.youtube.com/watch?v=Yk87oUPVaxU); publication: 2026-07-26T18:10:56Z; analysis: `analysis/Yk87oUPVaxU.json`.
[^Ywl4LsvHKzU]: [RAG Evaluation Is Broken! Here's Why (And How to Fix It) - Yuval Belfer and Niv Granot](https://www.youtube.com/watch?v=Ywl4LsvHKzU); publication: 2025-06-03T22:22:28Z; analysis: `analysis/Ywl4LsvHKzU.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^b2GqTDWtg6s]: [Scaling Agents for Gen AI Products - Anju Kambadur, Bloomberg Head of AI Engineering](https://www.youtube.com/watch?v=b2GqTDWtg6s); publication: 2025-04-01T15:06:35Z; analysis: `analysis/b2GqTDWtg6s.json`.
[^eAXxdtNlK04]: [Stop Burning Tokens: Why self-improvement needs domain expertise first - Annabell Schäfer, Langfuse](https://www.youtube.com/watch?v=eAXxdtNlK04); publication: 2026-07-18T20:15:06Z; analysis: `analysis/eAXxdtNlK04.json`.
[^iCj_ATyThvc]: [How Autoresearch is changing ML research — Zhengyao Jiang, Weco](https://www.youtube.com/watch?v=iCj_ATyThvc); publication: 2026-07-16T18:08:16Z; analysis: `analysis/iCj_ATyThvc.json`.
[^jRCpXUjz4CI]: [Everything Is a Rollout — Alex Shaw + Ryan Marten, Terminal-Bench, Harbor, Laude Institute](https://www.youtube.com/watch?v=jRCpXUjz4CI); publication: 2026-07-24T16:00:06Z; analysis: `analysis/jRCpXUjz4CI.json`.
[^jWq-aZIU0kM]: [Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](https://www.youtube.com/watch?v=jWq-aZIU0kM); publication: 2026-07-31T16:00:06Z; analysis: `analysis/jWq-aZIU0kM.json`.
[^jvKf6zXrNO4]: [Prompt Engineering is Dead — Nir Gazit, Traceloop](https://www.youtube.com/watch?v=jvKf6zXrNO4); publication: 2025-06-27T09:34:55Z; analysis: `analysis/jvKf6zXrNO4.json`.
[^kiqubc5b5Yo]: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo); publication: 2026-07-29T17:06:26Z; analysis: `analysis/kiqubc5b5Yo.json`.
[^mYSRn6PC1mc]: [Full Workshop: Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi](https://www.youtube.com/watch?v=mYSRn6PC1mc); publication: 2026-04-20T18:45:16Z; analysis: `analysis/mYSRn6PC1mc.json`.
[^pP_dSNz_EdQ]: [The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize](https://www.youtube.com/watch?v=pP_dSNz_EdQ); publication: 2025-12-23T17:00:06Z; analysis: `analysis/pP_dSNz_EdQ.json`.
[^q4Tr-DknG2M]: [Recursive Model Improvement — Lee Robinson, Cursor, SpaceXAI](https://www.youtube.com/watch?v=q4Tr-DknG2M); publication: 2026-07-15T20:13:51Z; analysis: `analysis/q4Tr-DknG2M.json`.
[^wcUJWP6WpGM]: [SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius](https://www.youtube.com/watch?v=wcUJWP6WpGM); publication: 2026-06-04T14:00:06Z; analysis: `analysis/wcUJWP6WpGM.json`.
[^xLxhT2ZI7UM]: [Your LLM Judge Is a Confident Liar: Building Better Verifiers — Browserbase](https://www.youtube.com/watch?v=xLxhT2ZI7UM); publication: 2026-10-05T23:30:05Z; analysis: `analysis/xLxhT2ZI7UM.json`.
[^xyL2Ltkh-SA]: [How Evals and Prompts Shape Agent Behavior — Preetika Bhateja & Daniel Bump, YouTube Ads](https://www.youtube.com/watch?v=xyL2Ltkh-SA); publication: 2026-07-24T21:00:00Z; analysis: `analysis/xyL2Ltkh-SA.json`.
