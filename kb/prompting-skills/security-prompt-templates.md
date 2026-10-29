---
{
  "type": "technique",
  "id": "security-prompt-templates",
  "title": "Supply security-focused examples without treating prompts as the enforcement boundary",
  "area": "prompting-skills",
  "status": "stable",
  "valid_from": "2026-10-11T19:30:16Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "ZyC56eV8sVw",
      "resource": "https://www.youtube.com/watch?v=ZyC56eV8sVw",
      "title": "AI Security Engineer Foundations + Certificate — Javier Garza, Snyk",
      "author": "Javier Garza, Snyk",
      "last_modified": "2026-10-11T19:30:16Z",
      "analysis_file": "analysis/ZyC56eV8sVw.json"
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

# Supply security-focused examples without treating prompts as the enforcement boundary

## What

Supply security-focused examples without treating prompts as the enforcement boundary

Instead of 'build a login page', prompts enumerate required controls (rate limiting, parameterized queries, etc.) so generated code is secure by default.

## Evidence

Source analysis [^ZyC56eV8sVw]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Reuse proven procedures without instruction bloat
- **Speed:** Less repeated setup and clarification
- **Quality:** Consistent explicit task contracts
- **Reliability:** Versioned, testable procedure and authority boundaries
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^ZyC56eV8sVw]: [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](https://www.youtube.com/watch?v=ZyC56eV8sVw); publication: 2026-10-11T19:30:16Z; analysis: `analysis/ZyC56eV8sVw.json`.
