---
{
  "type": "technique",
  "id": "work-actionability",
  "title": "Classify incoming work as fixable-now, deferred, intended or unsupported before admission",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-10-05T20:00:35Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "RmJ4rTLV_x4",
      "resource": "https://www.youtube.com/watch?v=RmJ4rTLV_x4",
      "title": "Your Support Team Should Ship Code – Lisa Orr, Zapier",
      "author": "Lisa Orr, Zapier",
      "last_modified": "2025-12-16T17:00:06Z",
      "analysis_file": "analysis/RmJ4rTLV_x4.json"
    },
    {
      "id": "YYH0DMQr30A",
      "resource": "https://www.youtube.com/watch?v=YYH0DMQr30A",
      "title": "Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel",
      "author": "Kobie Crawdord, Snorkel",
      "last_modified": "2026-06-02T17:00:39Z",
      "analysis_file": "analysis/YYH0DMQr30A.json"
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
      "id": "s0hFne6EeOI",
      "resource": "https://www.youtube.com/watch?v=s0hFne6EeOI",
      "title": "Build the Right Thing: Product Engineering (Part 2) — Kent C. Dodds, EpicProduct.engineer",
      "author": "Kent C. Dodds, EpicProduct.engineer",
      "last_modified": "2026-10-05T20:00:35Z",
      "analysis_file": "analysis/s0hFne6EeOI.json"
    },
    {
      "id": "zMiSRliEzv4",
      "resource": "https://www.youtube.com/watch?v=zMiSRliEzv4",
      "title": "Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog",
      "author": "Joshua Snyder, PostHog",
      "last_modified": "2026-06-10T13:00:17Z",
      "analysis_file": "analysis/zMiSRliEzv4.json"
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

# Classify incoming work as fixable-now, deferred, intended or unsupported before admission

## What

Classify incoming work as fixable-now, deferred, intended or unsupported before admission

Not every reported problem warrants code or a golden failure case; validate purpose and false positives first.

## Evidence

> next assess its fixability. Not every issue that comes from support
> — 10:18 [^RmJ4rTLV_x4]

> the tests don't match with the the requested task set up.
> — 14:54 [^YYH0DMQr30A]

> validation, then we prioritize and we understand what we want to fix now, fix
> — 25:28 [^aHhB3sjGjkI]

Source analysis [^s0hFne6EeOI]; no independently matched timestamped quote published.

> back into the pool to keep gathering more evidence.
> — 09:08 [^zMiSRliEzv4]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^RmJ4rTLV_x4]: [Your Support Team Should Ship Code – Lisa Orr, Zapier](https://www.youtube.com/watch?v=RmJ4rTLV_x4); publication: 2025-12-16T17:00:06Z; analysis: `analysis/RmJ4rTLV_x4.json`.
[^YYH0DMQr30A]: [Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel](https://www.youtube.com/watch?v=YYH0DMQr30A); publication: 2026-06-02T17:00:39Z; analysis: `analysis/YYH0DMQr30A.json`.
[^aHhB3sjGjkI]: [Agents Building Agents - Alfonso Graziano, Nearform](https://www.youtube.com/watch?v=aHhB3sjGjkI); publication: 2026-06-28T16:00:34Z; analysis: `analysis/aHhB3sjGjkI.json`.
[^s0hFne6EeOI]: [Build the Right Thing: Product Engineering (Part 2) — Kent C. Dodds, EpicProduct.engineer](https://www.youtube.com/watch?v=s0hFne6EeOI); publication: 2026-10-05T20:00:35Z; analysis: `analysis/s0hFne6EeOI.json`.
[^zMiSRliEzv4]: [Self Driving Products: Product Signals to Pull Requests — Joshua Snyder, PostHog](https://www.youtube.com/watch?v=zMiSRliEzv4); publication: 2026-06-10T13:00:17Z; analysis: `analysis/zMiSRliEzv4.json`.
