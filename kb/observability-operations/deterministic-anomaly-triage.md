---
{
  "type": "technique",
  "id": "deterministic-anomaly-triage",
  "title": "Let deterministic detectors trigger bounded evidence-based agent investigations",
  "area": "observability-operations",
  "status": "stable",
  "valid_from": "2026-10-11T15:30:31Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KA5kPbdkK2E",
      "resource": "https://www.youtube.com/watch?v=KA5kPbdkK2E",
      "title": "How Lovable self-improves every hour — Benjamin Verbeek, Lovable",
      "author": "Benjamin Verbeek, Lovable",
      "last_modified": "2026-06-02T16:00:33Z",
      "analysis_file": "analysis/KA5kPbdkK2E.json"
    },
    {
      "id": "Q5IVm_CxN2w",
      "resource": "https://www.youtube.com/watch?v=Q5IVm_CxN2w",
      "title": "Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway",
      "author": "Mahmoud Abdelwahab, Railway",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/Q5IVm_CxN2w.json"
    },
    {
      "id": "X1kp-ABIIxQ",
      "resource": "https://www.youtube.com/watch?v=X1kp-ABIIxQ",
      "title": "Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest",
      "author": "Dan Farrelly, CTO, Inngest",
      "last_modified": "2026-07-21T03:14:22Z",
      "analysis_file": "analysis/X1kp-ABIIxQ.json"
    },
    {
      "id": "cZ5ZJy19KMo",
      "resource": "https://www.youtube.com/watch?v=cZ5ZJy19KMo",
      "title": "Mission-Critical Evals at Scale (Learnings from 100k medical decisions)",
      "author": null,
      "last_modified": "2025-02-22T19:00:06Z",
      "analysis_file": "analysis/cZ5ZJy19KMo.json"
    },
    {
      "id": "fnuNVFgLjHA",
      "resource": "https://www.youtube.com/watch?v=fnuNVFgLjHA",
      "title": "Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI",
      "author": "Fuad Ali, Arize AI",
      "last_modified": "2026-10-11T15:30:31Z",
      "analysis_file": "analysis/fnuNVFgLjHA.json"
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
      "id": "u6jJcIFDLE4",
      "resource": "https://www.youtube.com/watch?v=u6jJcIFDLE4",
      "title": "Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates",
      "author": "Subbiah Sethuraman and Abhilash Asokan, ZS Associates",
      "last_modified": "2026-07-23T05:00:02Z",
      "analysis_file": "analysis/u6jJcIFDLE4.json"
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

# Let deterministic detectors trigger bounded evidence-based agent investigations

## What

Let deterministic detectors trigger bounded evidence-based agent investigations

A cheap scheduled detector triggers targeted investigation only when measurements warrant it, separating routine health classification from open-ended root-cause analysis.

## Evidence

> spikes are? Why do we see spikes in the number of
> — 17:17 [^KA5kPbdkK2E]

> analyze a slice of time rather than just having a threshold being met because it
> — 04:33 [^Q5IVm_CxN2w]

> want to pull in even more context for them. So like at a high level we want to
> — 05:11 [^Q5IVm_CxN2w]

> And if it isn't healthy, maybe you just invoke a a triage agent that goes and
> — 13:39 [^X1kp-ABIIxQ]

> other methods such as confidence estimation using logic based methods and
> — 06:53 [^cZ5ZJy19KMo]

> know, a latency spike or a cost spike or anything like that. Um, you can then
> — 25:36 [^fnuNVFgLjHA]

Source analysis [^jHMiYtjoJfA]; no independently matched timestamped quote published.

> Everything happened before the agent even kick starts.
> — 07:30 [^u6jJcIFDLE4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Target verified waste rather than speculative fixes
- **Speed:** Shorter evidence-based incident diagnosis
- **Quality:** Explain actual behavior and outcomes
- **Reliability:** Detect silent failures and attribute changes
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KA5kPbdkK2E]: [How Lovable self-improves every hour — Benjamin Verbeek, Lovable](https://www.youtube.com/watch?v=KA5kPbdkK2E); publication: 2026-06-02T16:00:33Z; analysis: `analysis/KA5kPbdkK2E.json`.
[^Q5IVm_CxN2w]: [Infra that fixes itself, thanks to coding agents — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=Q5IVm_CxN2w); publication: 2025-11-24T20:16:36Z; analysis: `analysis/Q5IVm_CxN2w.json`.
[^X1kp-ABIIxQ]: [Your agent architecture has a half-life of 6 months — Dan Farrelly, CTO, Inngest](https://www.youtube.com/watch?v=X1kp-ABIIxQ); publication: 2026-07-21T03:14:22Z; analysis: `analysis/X1kp-ABIIxQ.json`.
[^cZ5ZJy19KMo]: [Mission-Critical Evals at Scale (Learnings from 100k medical decisions)](https://www.youtube.com/watch?v=cZ5ZJy19KMo); publication: 2025-02-22T19:00:06Z; analysis: `analysis/cZ5ZJy19KMo.json`.
[^fnuNVFgLjHA]: [Building Self-Learning Loops for Your Agent — Fuad Ali, Arize AI](https://www.youtube.com/watch?v=fnuNVFgLjHA); publication: 2026-10-11T15:30:31Z; analysis: `analysis/fnuNVFgLjHA.json`.
[^jHMiYtjoJfA]: [Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop](https://www.youtube.com/watch?v=jHMiYtjoJfA); publication: 2026-08-12T18:00:34Z; analysis: `analysis/jHMiYtjoJfA.json`.
[^u6jJcIFDLE4]: [Why We Killed Our Multi-Agent Pipeline — Subbiah Sethuraman and Abhilash Asokan, ZS Associates](https://www.youtube.com/watch?v=u6jJcIFDLE4); publication: 2026-07-23T05:00:02Z; analysis: `analysis/u6jJcIFDLE4.json`.
