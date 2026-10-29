---
{
  "type": "technique",
  "id": "cost-per-success",
  "title": "Normalize cost, latency and retries by successful comparable outcomes",
  "area": "evaluation-measurement",
  "status": "stable",
  "valid_from": "2026-10-20T23:00:22Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "2Wtq2GvUicw",
      "resource": "https://www.youtube.com/watch?v=2Wtq2GvUicw",
      "title": "LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella",
      "author": null,
      "last_modified": "2025-02-08T21:32:17Z",
      "analysis_file": "analysis/2Wtq2GvUicw.json"
    },
    {
      "id": "3axY1wz2OvA",
      "resource": "https://www.youtube.com/watch?v=3axY1wz2OvA",
      "title": "Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis",
      "author": "Oliver Kennon, SemiAnalysis",
      "last_modified": "2026-10-20T23:00:22Z",
      "analysis_file": "analysis/3axY1wz2OvA.json"
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
      "id": "CoEIs6Xm8m8",
      "resource": "https://www.youtube.com/watch?v=CoEIs6Xm8m8",
      "title": "Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline",
      "author": "Saoud Rizwan, Cline",
      "last_modified": "2026-08-07T23:26:51Z",
      "analysis_file": "analysis/CoEIs6Xm8m8.json"
    },
    {
      "id": "HS5a8VIKsvA",
      "resource": "https://www.youtube.com/watch?v=HS5a8VIKsvA",
      "title": "Navigating AI’s Frontier in 2025 - Grace Isford, Lux Capital",
      "author": "Grace Isford, Lux Capital",
      "last_modified": "2025-03-13T17:06:55Z",
      "analysis_file": "analysis/HS5a8VIKsvA.json"
    },
    {
      "id": "PXj0p_mW9nI",
      "resource": "https://www.youtube.com/watch?v=PXj0p_mW9nI",
      "title": "Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic",
      "author": "Katelyn Lesse & Angela Jiang, Anthropic",
      "last_modified": "2026-09-14T14:00:06Z",
      "analysis_file": "analysis/PXj0p_mW9nI.json"
    },
    {
      "id": "Rx8f05JI_WA",
      "resource": "https://www.youtube.com/watch?v=Rx8f05JI_WA",
      "title": "SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI",
      "author": "Rishi Desai, Abundant AI",
      "last_modified": "2026-07-07T03:45:51Z",
      "analysis_file": "analysis/Rx8f05JI_WA.json"
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
      "id": "Th5e4h-oVmc",
      "resource": "https://www.youtube.com/watch?v=Th5e4h-oVmc",
      "title": "Real AI Agents Need Planning, Not Just Prompting - Yuval Belfer",
      "author": "Yuval Belfer",
      "last_modified": "2025-06-03T22:22:27Z",
      "analysis_file": "analysis/Th5e4h-oVmc.json"
    },
    {
      "id": "U7ZYBCcdJPg",
      "resource": "https://www.youtube.com/watch?v=U7ZYBCcdJPg",
      "title": "Tokens Are the Cheap Part — Steve Jamison, Jellyfish",
      "author": "Steve Jamison, Jellyfish",
      "last_modified": "2026-10-13T17:00:19Z",
      "analysis_file": "analysis/U7ZYBCcdJPg.json"
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
      "id": "_B4Pv9ttFgY",
      "resource": "https://www.youtube.com/watch?v=_B4Pv9ttFgY",
      "title": "Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google",
      "author": "Michael Hablich, Google",
      "last_modified": "2026-06-05T17:00:06Z",
      "analysis_file": "analysis/_B4Pv9ttFgY.json"
    },
    {
      "id": "_naLJOqVOEI",
      "resource": "https://www.youtube.com/watch?v=_naLJOqVOEI",
      "title": "Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI",
      "author": "FriendliAI",
      "last_modified": "2026-10-11T19:30:05Z",
      "analysis_file": "analysis/_naLJOqVOEI.json"
    },
    {
      "id": "bZISsg7H7DA",
      "resource": "https://www.youtube.com/watch?v=bZISsg7H7DA",
      "title": "Your Agents Need a Save Button - Hamza Tahir, ZenML",
      "author": "Hamza Tahir, ZenML",
      "last_modified": "2026-07-18T07:00:06Z",
      "analysis_file": "analysis/bZISsg7H7DA.json"
    },
    {
      "id": "d5EltXhbcfA",
      "resource": "https://www.youtube.com/watch?v=d5EltXhbcfA",
      "title": "Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil",
      "author": "Sayash Kapoor, AI Snake Oil",
      "last_modified": "2025-04-17T16:00:06Z",
      "analysis_file": "analysis/d5EltXhbcfA.json"
    },
    {
      "id": "dvft0Gp9sEE",
      "resource": "https://www.youtube.com/watch?v=dvft0Gp9sEE",
      "title": "Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo",
      "author": "Charlie Guo",
      "last_modified": "2025-06-03T07:00:07Z",
      "analysis_file": "analysis/dvft0Gp9sEE.json"
    },
    {
      "id": "gWLVu9OGvBg",
      "resource": "https://www.youtube.com/watch?v=gWLVu9OGvBg",
      "title": "Understanding AI Stakes to Break Production Code: Philip Rathle",
      "author": null,
      "last_modified": "2024-12-31T17:17:42Z",
      "analysis_file": "analysis/gWLVu9OGvBg.json"
    },
    {
      "id": "hqHC6Z_lXyo",
      "resource": "https://www.youtube.com/watch?v=hqHC6Z_lXyo",
      "title": "20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna",
      "author": "Bertrand Charpentier, Pruna",
      "last_modified": "2026-06-01T17:00:06Z",
      "analysis_file": "analysis/hqHC6Z_lXyo.json"
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
      "id": "k2ClBT4aqAg",
      "resource": "https://www.youtube.com/watch?v=k2ClBT4aqAg",
      "title": "We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman",
      "author": "Kamalakannan Nandagopal, Postman",
      "last_modified": "2026-10-08T21:30:19Z",
      "analysis_file": "analysis/k2ClBT4aqAg.json"
    },
    {
      "id": "kPL-6-9MVyA",
      "resource": "https://www.youtube.com/watch?v=kPL-6-9MVyA",
      "title": "RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG",
      "author": "Douwe Kiela, creator of RAG",
      "last_modified": "2025-04-10T19:47:37Z",
      "analysis_file": "analysis/kPL-6-9MVyA.json"
    },
    {
      "id": "kTnfJszFxCg",
      "resource": "https://www.youtube.com/watch?v=kTnfJszFxCg",
      "title": "3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph",
      "author": "Harrison Chase, LangChain/LangGraph",
      "last_modified": "2025-07-23T15:51:25Z",
      "analysis_file": "analysis/kTnfJszFxCg.json"
    },
    {
      "id": "sRpqPgKeXNk",
      "resource": "https://www.youtube.com/watch?v=sRpqPgKeXNk",
      "title": "Trends Across the AI Frontier — George Cameron, ArtificialAnalysis.ai",
      "author": "George Cameron, ArtificialAnalysis.ai",
      "last_modified": "2025-07-08T16:00:06Z",
      "analysis_file": "analysis/sRpqPgKeXNk.json"
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

# Normalize cost, latency and retries by successful comparable outcomes

## What

Normalize cost, latency and retries by successful comparable outcomes

A cheaper call is false economy if it lowers resolution quality and creates retries or downstream repair work.

## Evidence

Source analysis [^2Wtq2GvUicw]; no independently matched timestamped quote published.

Source analysis [^3axY1wz2OvA]; no independently matched timestamped quote published.

Source analysis [^7c9FSUVcXR0]; no independently matched timestamped quote published.

Source analysis [^CoEIs6Xm8m8]; no independently matched timestamped quote published.

Source analysis [^HS5a8VIKsvA]; no independently matched timestamped quote published.

Source analysis [^PXj0p_mW9nI]; no independently matched timestamped quote published.

> So, the model isn't just the full picture. The agent scaffold makes a huge
> — 07:38 [^Rx8f05JI_WA]

> again. And as a result, all of those LLM calls piled up and made it a lot more
> — 16:40 [^T3SS931wU0I]

Source analysis [^Th5e4h-oVmc]; no independently matched timestamped quote published.

> More tokens leads to more PRs, which leads to a lower cost of delivery.
> — 08:42 [^U7ZYBCcdJPg]

> and costs more than one of the bigger models because it just used so many
> — 06:25 [^YIxzNZDDy1A]

Source analysis [^Yk87oUPVaxU]; no independently matched timestamped quote published.

Source analysis [^_B4Pv9ttFgY]; no independently matched timestamped quote published.

Source analysis [^_naLJOqVOEI]; no independently matched timestamped quote published.

> the day you have to look at the value created, right? So it's a trade-off
> — 14:18 [^bZISsg7H7DA]

> mentioned earlier um you can have multiple agents which are evaluated with
> — 09:59 [^d5EltXhbcfA]

Source analysis [^dvft0Gp9sEE]; no independently matched timestamped quote published.

Source analysis [^gWLVu9OGvBg]; no independently matched timestamped quote published.

Source analysis [^hqHC6Z_lXyo]; no independently matched timestamped quote published.

Source analysis [^iNkFlCiij0U]; no independently matched timestamped quote published.

> and we also measured the exact amount of tokens it took for each of these runs.
> — 07:45 [^k2ClBT4aqAg]

Source analysis [^kPL-6-9MVyA]; no independently matched timestamped quote published.

> opposite for the cost when it's wrong. And of course, like this needs to be
> — 02:45 [^kTnfJszFxCg]

> you to think this way but you're paying for the cost per token but then you're
> — 11:51 [^sRpqPgKeXNk]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Stop spending on non-informative checks or comparisons
- **Speed:** Faster diagnosis using existing evidence
- **Quality:** Outcome-valid rather than proxy-only judgments
- **Reliability:** Detect uncertainty, bias, drift and invalid scoring
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^2Wtq2GvUicw]: [LLM Quality Optimization Bootcamp: Thierry Moreau and Pedro Torruella](https://www.youtube.com/watch?v=2Wtq2GvUicw); publication: 2025-02-08T21:32:17Z; analysis: `analysis/2Wtq2GvUicw.json`.
[^3axY1wz2OvA]: [Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis](https://www.youtube.com/watch?v=3axY1wz2OvA); publication: 2026-10-20T23:00:22Z; analysis: `analysis/3axY1wz2OvA.json`.
[^7c9FSUVcXR0]: [Operating Distributed Inference Systems at Scale — Nishant Gupta & Naman Ahuja, Meta](https://www.youtube.com/watch?v=7c9FSUVcXR0); publication: 2026-09-19T15:00:10Z; analysis: `analysis/7c9FSUVcXR0.json`.
[^CoEIs6Xm8m8]: [Open Source Is Dead. Long Live Open Source. — Saoud Rizwan, Cline](https://www.youtube.com/watch?v=CoEIs6Xm8m8); publication: 2026-08-07T23:26:51Z; analysis: `analysis/CoEIs6Xm8m8.json`.
[^HS5a8VIKsvA]: [Navigating AI’s Frontier in 2025 - Grace Isford, Lux Capital](https://www.youtube.com/watch?v=HS5a8VIKsvA); publication: 2025-03-13T17:06:55Z; analysis: `analysis/HS5a8VIKsvA.json`.
[^PXj0p_mW9nI]: [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](https://www.youtube.com/watch?v=PXj0p_mW9nI); publication: 2026-09-14T14:00:06Z; analysis: `analysis/PXj0p_mW9nI.json`.
[^Rx8f05JI_WA]: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA); publication: 2026-07-07T03:45:51Z; analysis: `analysis/Rx8f05JI_WA.json`.
[^T3SS931wU0I]: [Agentic Search vs Vector Search for Coding Agents: We Ran the Eval — Braintrust](https://www.youtube.com/watch?v=T3SS931wU0I); publication: 2026-10-05T15:30:36Z; analysis: `analysis/T3SS931wU0I.json`.
[^Th5e4h-oVmc]: [Real AI Agents Need Planning, Not Just Prompting - Yuval Belfer](https://www.youtube.com/watch?v=Th5e4h-oVmc); publication: 2025-06-03T22:22:27Z; analysis: `analysis/Th5e4h-oVmc.json`.
[^U7ZYBCcdJPg]: [Tokens Are the Cheap Part — Steve Jamison, Jellyfish](https://www.youtube.com/watch?v=U7ZYBCcdJPg); publication: 2026-10-13T17:00:19Z; analysis: `analysis/U7ZYBCcdJPg.json`.
[^YIxzNZDDy1A]: [From Zero to Leaderboard: Agent Evaluation — Wolfram Ravenwolf, Weights & Biases](https://www.youtube.com/watch?v=YIxzNZDDy1A); publication: 2026-10-11T17:00:18Z; analysis: `analysis/YIxzNZDDy1A.json`.
[^Yk87oUPVaxU]: [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](https://www.youtube.com/watch?v=Yk87oUPVaxU); publication: 2026-07-26T18:10:56Z; analysis: `analysis/Yk87oUPVaxU.json`.
[^_B4Pv9ttFgY]: [Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google](https://www.youtube.com/watch?v=_B4Pv9ttFgY); publication: 2026-06-05T17:00:06Z; analysis: `analysis/_B4Pv9ttFgY.json`.
[^_naLJOqVOEI]: [Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI](https://www.youtube.com/watch?v=_naLJOqVOEI); publication: 2026-10-11T19:30:05Z; analysis: `analysis/_naLJOqVOEI.json`.
[^bZISsg7H7DA]: [Your Agents Need a Save Button - Hamza Tahir, ZenML](https://www.youtube.com/watch?v=bZISsg7H7DA); publication: 2026-07-18T07:00:06Z; analysis: `analysis/bZISsg7H7DA.json`.
[^d5EltXhbcfA]: [Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil](https://www.youtube.com/watch?v=d5EltXhbcfA); publication: 2025-04-17T16:00:06Z; analysis: `analysis/d5EltXhbcfA.json`.
[^dvft0Gp9sEE]: [Analyzing 10,000 Sales Calls With AI In 2 Weeks — Charlie Guo](https://www.youtube.com/watch?v=dvft0Gp9sEE); publication: 2025-06-03T07:00:07Z; analysis: `analysis/dvft0Gp9sEE.json`.
[^gWLVu9OGvBg]: [Understanding AI Stakes to Break Production Code: Philip Rathle](https://www.youtube.com/watch?v=gWLVu9OGvBg); publication: 2024-12-31T17:17:42Z; analysis: `analysis/gWLVu9OGvBg.json`.
[^hqHC6Z_lXyo]: [20 days of compute vs 7 hours: rethinking what state-of-the-art means — Bertrand Charpentier, Pruna](https://www.youtube.com/watch?v=hqHC6Z_lXyo); publication: 2026-06-01T17:00:06Z; analysis: `analysis/hqHC6Z_lXyo.json`.
[^iNkFlCiij0U]: [The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI](https://www.youtube.com/watch?v=iNkFlCiij0U); publication: 2026-06-04T16:00:06Z; analysis: `analysis/iNkFlCiij0U.json`.
[^k2ClBT4aqAg]: [We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman](https://www.youtube.com/watch?v=k2ClBT4aqAg); publication: 2026-10-08T21:30:19Z; analysis: `analysis/k2ClBT4aqAg.json`.
[^kPL-6-9MVyA]: [RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG](https://www.youtube.com/watch?v=kPL-6-9MVyA); publication: 2025-04-10T19:47:37Z; analysis: `analysis/kPL-6-9MVyA.json`.
[^kTnfJszFxCg]: [3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph](https://www.youtube.com/watch?v=kTnfJszFxCg); publication: 2025-07-23T15:51:25Z; analysis: `analysis/kTnfJszFxCg.json`.
[^sRpqPgKeXNk]: [Trends Across the AI Frontier — George Cameron, ArtificialAnalysis.ai](https://www.youtube.com/watch?v=sRpqPgKeXNk); publication: 2025-07-08T16:00:06Z; analysis: `analysis/sRpqPgKeXNk.json`.
