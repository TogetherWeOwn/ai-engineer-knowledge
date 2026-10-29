---
{
  "type": "technique",
  "id": "staging-gate",
  "title": "Require isolated staging evidence before production promotion",
  "area": "delivery-release",
  "status": "stable",
  "valid_from": "2026-10-22T09:00:12Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "9arM9b7JgOo",
      "resource": "https://www.youtube.com/watch?v=9arM9b7JgOo",
      "title": "Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat",
      "author": "Jeffrey Lee-Chan, Snapchat",
      "last_modified": "2026-07-11T14:45:18Z",
      "analysis_file": "analysis/9arM9b7JgOo.json"
    },
    {
      "id": "YXiLj4tJt5A",
      "resource": "https://www.youtube.com/watch?v=YXiLj4tJt5A",
      "title": "Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS",
      "author": "Elizabeth Fuentes Leone & Sandhya Subramani, AWS",
      "last_modified": "2026-10-11T15:00:05Z",
      "analysis_file": "analysis/YXiLj4tJt5A.json"
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
      "id": "iUWwcG-C8OU",
      "resource": "https://www.youtube.com/watch?v=iUWwcG-C8OU",
      "title": "Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS",
      "author": "Garrett Galow, WorkOS",
      "last_modified": "2026-06-11T18:00:06Z",
      "analysis_file": "analysis/iUWwcG-C8OU.json"
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
      "id": "mMw3arwQsL0",
      "resource": "https://www.youtube.com/watch?v=mMw3arwQsL0",
      "title": "1,368 AI Failures and What They Teach About Evals — Vishal Srivastava & Tanmay Sah, New York Life",
      "author": "Vishal Srivastava & Tanmay Sah, New York Life",
      "last_modified": "2026-10-22T09:00:12Z",
      "analysis_file": "analysis/mMw3arwQsL0.json"
    },
    {
      "id": "wJwTlvb_TSo",
      "resource": "https://www.youtube.com/watch?v=wJwTlvb_TSo",
      "title": "WTF do people use Open Models for??",
      "author": null,
      "last_modified": "2025-02-22T20:00:06Z",
      "analysis_file": "analysis/wJwTlvb_TSo.json"
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

# Require isolated staging evidence before production promotion

## What

Require isolated staging evidence before production promotion

The same agent implementation can be exercised locally and packaged behind an explicit runtime entry point, reducing notebook-to-production divergence.

## Evidence

Source analysis [^9arM9b7JgOo]; no independently matched timestamped quote published.

> are going to be able to test the agent before to putting it in in AWS. And
> — 49:30 [^YXiLj4tJt5A]

Source analysis [^adfw3xJBx1o]; no independently matched timestamped quote published.

Source analysis [^iUWwcG-C8OU]; no independently matched timestamped quote published.

Source analysis [^kPL-6-9MVyA]; no independently matched timestamped quote published.

> controls that we have in deployment are more critically associated with harm,
> — 09:03 [^mMw3arwQsL0]

Source analysis [^wJwTlvb_TSo]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid failed cutover and repeated integration work
- **Speed:** Shorter safe automated promotion
- **Quality:** Release the actual tested artifact
- **Reliability:** Staging, provenance and rollback contain regressions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^9arM9b7JgOo]: [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo); publication: 2026-07-11T14:45:18Z; analysis: `analysis/9arM9b7JgOo.json`.
[^YXiLj4tJt5A]: [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](https://www.youtube.com/watch?v=YXiLj4tJt5A); publication: 2026-10-11T15:00:05Z; analysis: `analysis/YXiLj4tJt5A.json`.
[^adfw3xJBx1o]: [A Bank Built Its Own Coding Agent. It Took Off — Felippe Felisola Caso & Francesco Galletta, Monzo](https://www.youtube.com/watch?v=adfw3xJBx1o); publication: 2026-10-20T19:00:34Z; analysis: `analysis/adfw3xJBx1o.json`.
[^iUWwcG-C8OU]: [Why Can't Anyone Answer Questions About the Business? — Garrett Galow, WorkOS](https://www.youtube.com/watch?v=iUWwcG-C8OU); publication: 2026-06-11T18:00:06Z; analysis: `analysis/iUWwcG-C8OU.json`.
[^kPL-6-9MVyA]: [RAG Agents in Prod: 10 Lessons We Learned — Douwe Kiela, creator of RAG](https://www.youtube.com/watch?v=kPL-6-9MVyA); publication: 2025-04-10T19:47:37Z; analysis: `analysis/kPL-6-9MVyA.json`.
[^mMw3arwQsL0]: [1,368 AI Failures and What They Teach About Evals — Vishal Srivastava & Tanmay Sah, New York Life](https://www.youtube.com/watch?v=mMw3arwQsL0); publication: 2026-10-22T09:00:12Z; analysis: `analysis/mMw3arwQsL0.json`.
[^wJwTlvb_TSo]: [WTF do people use Open Models for??](https://www.youtube.com/watch?v=wJwTlvb_TSo); publication: 2025-02-22T20:00:06Z; analysis: `analysis/wJwTlvb_TSo.json`.
