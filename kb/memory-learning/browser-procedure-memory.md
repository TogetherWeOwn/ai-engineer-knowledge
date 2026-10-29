---
{
  "type": "technique",
  "id": "browser-procedure-memory",
  "title": "Reuse versioned site-specific browser procedures instead of rediscovering every flow",
  "area": "memory-learning",
  "status": "stable",
  "valid_from": "2026-10-11T21:30:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "kZsf_Sfm7RU",
      "resource": "https://www.youtube.com/watch?v=kZsf_Sfm7RU",
      "title": "The Missing Layer After Launch - Raphael Kalandadze, Wandero AI",
      "author": "Raphael Kalandadze, Wandero AI",
      "last_modified": "2026-07-05T03:15:05Z",
      "analysis_file": "analysis/kZsf_Sfm7RU.json"
    },
    {
      "id": "p7gaxmCUiIU",
      "resource": "https://www.youtube.com/watch?v=p7gaxmCUiIU",
      "title": "Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase",
      "author": "Shubhankar Srivastava, Browserbase",
      "last_modified": "2026-10-11T21:30:05Z",
      "analysis_file": "analysis/p7gaxmCUiIU.json"
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

# Reuse versioned site-specific browser procedures instead of rediscovering every flow

## What

Reuse versioned site-specific browser procedures instead of rediscovering every flow

A compact map of the product's DOM and navigation avoids slow generic computer-use exploration.

## Evidence

> Uh and we try to build a specific skill that know our uh website, our DOM, how
> — 17:14 [^kZsf_Sfm7RU]

> all of these learnings? It says go straight to the shed schedule page. If
> — 13:45 [^p7gaxmCUiIU]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated investigation
- **Speed:** Faster reuse of relevant prior work
- **Quality:** More current, scoped lessons
- **Reliability:** Less stale, conflicting or unsupported recall
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^kZsf_Sfm7RU]: [The Missing Layer After Launch - Raphael Kalandadze, Wandero AI](https://www.youtube.com/watch?v=kZsf_Sfm7RU); publication: 2026-07-05T03:15:05Z; analysis: `analysis/kZsf_Sfm7RU.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
