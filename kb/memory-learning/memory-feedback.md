---
{
  "type": "technique",
  "id": "memory-feedback",
  "title": "Score recalled memories for usefulness and harmful influence",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-10-09T18:30:09Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "BIhiYL4U9_M",
      "resource": "https://www.youtube.com/watch?v=BIhiYL4U9_M",
      "title": "From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle",
      "author": "Anders Swanson, Oracle",
      "last_modified": "2026-10-09T18:30:09Z",
      "analysis_file": "analysis/BIhiYL4U9_M.json"
    },
    {
      "id": "Jx4ZFEAq6bY",
      "resource": "https://www.youtube.com/watch?v=Jx4ZFEAq6bY",
      "title": "User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch",
      "author": "Sonam Pankaj, StarlightSearch",
      "last_modified": "2026-06-28T17:00:20Z",
      "analysis_file": "analysis/Jx4ZFEAq6bY.json"
    },
    {
      "id": "KA5kPbdkK2E",
      "resource": "https://www.youtube.com/watch?v=KA5kPbdkK2E",
      "title": "How Lovable self-improves every hour — Benjamin Verbeek, Lovable",
      "author": "Benjamin Verbeek, Lovable",
      "last_modified": "2026-06-02T16:00:33Z",
      "analysis_file": "analysis/KA5kPbdkK2E.json"
    },
    {
      "id": "KGFyOtl5ktI",
      "resource": "https://www.youtube.com/watch?v=KGFyOtl5ktI",
      "title": "Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain",
      "author": "Jake Broekhuizen, LangChain",
      "last_modified": "2026-10-08T14:00:37Z",
      "analysis_file": "analysis/KGFyOtl5ktI.json"
    },
    {
      "id": "Qw_tC68KKes",
      "resource": "https://www.youtube.com/watch?v=Qw_tC68KKes",
      "title": "How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare",
      "author": "Justin Joyce, Cloudflare",
      "last_modified": "2026-08-26T16:30:09Z",
      "analysis_file": "analysis/Qw_tC68KKes.json"
    },
    {
      "id": "R3-anFK1YM8",
      "resource": "https://www.youtube.com/watch?v=R3-anFK1YM8",
      "title": "Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai",
      "author": "Stefania Druga, Sakana.ai",
      "last_modified": "2026-08-12T15:00:06Z",
      "analysis_file": "analysis/R3-anFK1YM8.json"
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
      "id": "s67bE2Ur3bY",
      "resource": "https://www.youtube.com/watch?v=s67bE2Ur3bY",
      "title": "Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi",
      "author": "Sai Krishna Rallabandi",
      "last_modified": "2026-07-29T22:58:19Z",
      "analysis_file": "analysis/s67bE2Ur3bY.json"
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

# Score recalled memories for usefulness and harmful influence

## What

Score recalled memories for usefulness and harmful influence

Record whether each retrieved memory was used, ignored, stale or harmful. Feed that back into ranking and into the memory lifecycle (validity window, last-used, conflict review), so memory stays accurate as the system changes, for example after a build-system switch.

## Evidence

Source analysis [^BIhiYL4U9_M]; no independently matched timestamped quote published.

> So, we act based on usefulness. Context is updated based on task. So, this is a
> — 06:26 [^Jx4ZFEAq6bY]

> do retrieve by semantic similarity to the current task weighted by whether
> — 05:21 [^Jx4ZFEAq6bY]

> noisy labels can make the utility noisy as well. And there is, uh,
> — 09:22 [^Jx4ZFEAq6bY]

> answer, it injects that context into the main agent.
> — 09:52 [^KA5kPbdkK2E]

> data actually should stay as history as referencable history. Some some might
> — 13:30 [^KGFyOtl5ktI]

Source analysis [^Qw_tC68KKes]; no independently matched timestamped quote published.

> ledger performed the best and it performed better than like just
> — 08:21 [^R3-anFK1YM8]

> that bad memory is expensive because it spends more token and it can send agent
> — 09:45 [^R3-anFK1YM8]

> your rules and standards and codify them and get analytics and statistics about
> — 16:18 [^s-aixZYJG4c]

Source analysis [^s67bE2Ur3bY]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^BIhiYL4U9_M]: [From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle](https://www.youtube.com/watch?v=BIhiYL4U9_M); publication: 2026-10-09T18:30:09Z; analysis: `analysis/BIhiYL4U9_M.json`.
[^Jx4ZFEAq6bY]: [User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch](https://www.youtube.com/watch?v=Jx4ZFEAq6bY); publication: 2026-06-28T17:00:20Z; analysis: `analysis/Jx4ZFEAq6bY.json`.
[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^KGFyOtl5ktI]: [Giving AI Agents Memory That Learns — Jake Broekhuizen, LangChain](https://www.youtube.com/watch?v=KGFyOtl5ktI); publication: 2026-10-08T14:00:37Z; analysis: `analysis/KGFyOtl5ktI.json`.
[^Qw_tC68KKes]: [How AI Agents Let GTM Teams Scale — Justin Joyce, Cloudflare](https://www.youtube.com/watch?v=Qw_tC68KKes); publication: 2026-08-26T16:30:09Z; analysis: `analysis/Qw_tC68KKes.json`.
[^R3-anFK1YM8]: [Memory Harnesses for Long-Running Research Agents — Stefania Druga, Sakana.ai](https://www.youtube.com/watch?v=R3-anFK1YM8); publication: 2026-08-12T15:00:06Z; analysis: `analysis/R3-anFK1YM8.json`.
[^s-aixZYJG4c]: [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=s-aixZYJG4c); publication: 2026-08-20T13:30:38Z; analysis: `analysis/s-aixZYJG4c.json`.
[^s67bE2Ur3bY]: [Wearing the Agent: From Group Chats to Glasses — Sai Krishna Rallabandi](https://www.youtube.com/watch?v=s67bE2Ur3bY); publication: 2026-07-29T22:58:19Z; analysis: `analysis/s67bE2Ur3bY.json`.
