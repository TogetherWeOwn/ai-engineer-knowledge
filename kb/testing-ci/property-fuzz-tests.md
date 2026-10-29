---
{
  "type": "technique",
  "id": "property-fuzz-tests",
  "title": "Use property-based tests and bounded fuzzing for invariants",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-12T05:36:31Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "IddXPepIAS4",
      "resource": "https://www.youtube.com/watch?v=IddXPepIAS4",
      "title": "Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS",
      "author": "Erik Hanchett, AWS",
      "last_modified": "2026-06-28T17:30:24Z",
      "analysis_file": "analysis/IddXPepIAS4.json"
    },
    {
      "id": "KhYifX22yhE",
      "resource": "https://www.youtube.com/watch?v=KhYifX22yhE",
      "title": "The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside",
      "author": "Marah Abdin & Robert McHardy, poolside",
      "last_modified": "2026-07-26T01:00:06Z",
      "analysis_file": "analysis/KhYifX22yhE.json"
    },
    {
      "id": "OMGPvW8TBHc",
      "resource": "https://www.youtube.com/watch?v=OMGPvW8TBHc",
      "title": "Fuzzing in the GenAI Era — Leonard Tang, Haize Labs",
      "author": "Leonard Tang, Haize Labs",
      "last_modified": "2025-08-22T15:00:05Z",
      "analysis_file": "analysis/OMGPvW8TBHc.json"
    },
    {
      "id": "VktrqzQgytY",
      "resource": "https://www.youtube.com/watch?v=VktrqzQgytY",
      "title": "CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner",
      "author": "Hugo Santos and Madison Faulkner",
      "last_modified": "2026-05-13T13:00:06Z",
      "analysis_file": "analysis/VktrqzQgytY.json"
    },
    {
      "id": "_mi3alkqy4s",
      "resource": "https://www.youtube.com/watch?v=_mi3alkqy4s",
      "title": "The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-09-30T13:30:35Z",
      "analysis_file": "analysis/_mi3alkqy4s.json"
    },
    {
      "id": "k72eLcYpVys",
      "resource": "https://www.youtube.com/watch?v=k72eLcYpVys",
      "title": "1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS",
      "author": "Kevin Orellana, AWS",
      "last_modified": "2026-10-12T05:36:31Z",
      "analysis_file": "analysis/k72eLcYpVys.json"
    },
    {
      "id": "sDMGWK4wZ_w",
      "resource": "https://www.youtube.com/watch?v=sDMGWK4wZ_w",
      "title": "Training Taste — Thais Castello Branco, Taste Labs",
      "author": "Thais Castello Branco, Taste Labs",
      "last_modified": "2026-09-10T16:00:20Z",
      "analysis_file": "analysis/sDMGWK4wZ_w.json"
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

# Use property-based tests and bounded fuzzing for invariants

## What

Use property-based tests and bounded fuzzing for invariants

Passing interface tests does not prove assertions such as unsafe-memory validity or authorization invariants.

## Evidence

Source analysis [^IddXPepIAS4]; no independently matched timestamped quote published.

Source analysis [^KhYifX22yhE]; no independently matched timestamped quote published.

> anything and we exhaust our search budget, that that means you're
> — 06:41 [^OMGPvW8TBHc]

> application. And we use that as a signal to help guide the next round of search,
> — 06:31 [^OMGPvW8TBHc]

> to flip. Uh we can use various forms of tree search and MCTS. We can search over
> — 16:00 [^OMGPvW8TBHc]

Source analysis [^VktrqzQgytY]; no independently matched timestamped quote published.

> assertions that the test suite was never designed to look for. So they took
> — 17:15 [^_mi3alkqy4s]

> locally, but also fuzzy test it with a wide set of domain tests um remotely.
> — 14:50 [^k72eLcYpVys]

Source analysis [^sDMGWK4wZ_w]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^IddXPepIAS4]: [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](https://www.youtube.com/watch?v=IddXPepIAS4); publication: 2026-06-28T17:30:24Z; analysis: `analysis/IddXPepIAS4.json`.
[^KhYifX22yhE]: [The Messy Reality of Scale: Synthetic Data and Pre-Training — Marah Abdin & Robert McHardy, poolside](https://www.youtube.com/watch?v=KhYifX22yhE); publication: 2026-07-26T01:00:06Z; analysis: `analysis/KhYifX22yhE.json`.
[^OMGPvW8TBHc]: [Fuzzing in the GenAI Era — Leonard Tang, Haize Labs](https://www.youtube.com/watch?v=OMGPvW8TBHc); publication: 2025-08-22T15:00:05Z; analysis: `analysis/OMGPvW8TBHc.json`.
[^VktrqzQgytY]: [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](https://www.youtube.com/watch?v=VktrqzQgytY); publication: 2026-05-13T13:00:06Z; analysis: `analysis/VktrqzQgytY.json`.
[^_mi3alkqy4s]: [The Death of the Code Review: What the Data Actually Says — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=_mi3alkqy4s); publication: 2026-09-30T13:30:35Z; analysis: `analysis/_mi3alkqy4s.json`.
[^k72eLcYpVys]: [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](https://www.youtube.com/watch?v=k72eLcYpVys); publication: 2026-10-12T05:36:31Z; analysis: `analysis/k72eLcYpVys.json`.
[^sDMGWK4wZ_w]: [Training Taste — Thais Castello Branco, Taste Labs](https://www.youtube.com/watch?v=sDMGWK4wZ_w); publication: 2026-09-10T16:00:20Z; analysis: `analysis/sDMGWK4wZ_w.json`.
