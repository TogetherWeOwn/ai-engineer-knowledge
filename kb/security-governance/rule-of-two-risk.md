---
{
  "type": "technique",
  "id": "rule-of-two-risk",
  "title": "Detect dangerous combinations of untrusted input, sensitive data and outbound authority",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2025-11-24T20:16:36Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "5eJqXtevlXg",
      "resource": "https://www.youtube.com/watch?v=5eJqXtevlXg",
      "title": "Hacking Subagents Into Codex CLI — Brian John, Betterup",
      "author": "Brian John, Betterup",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/5eJqXtevlXg.json"
    },
    {
      "id": "YpY83-kA7Bo",
      "resource": "https://www.youtube.com/watch?v=YpY83-kA7Bo",
      "title": "2025 in LLMs so far, illustrated by Pelicans on Bicycles — Simon Willison",
      "author": "Simon Willison",
      "last_modified": "2025-07-09T16:00:06Z",
      "analysis_file": "analysis/YpY83-kA7Bo.json"
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

# Detect dangerous combinations of untrusted input, sensitive data and outbound authority

## What

Detect dangerous combinations of untrusted input, sensitive data and outbound authority

Classifies an agent by three axes — untrusted input, access to sensitive data/systems, ability to change state or communicate externally — and argues you should not have all three at once.

## Evidence

Source analysis [^5eJqXtevlXg]; no independently matched timestamped quote published.

Source analysis [^YpY83-kA7Bo]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^5eJqXtevlXg]: [Hacking Subagents Into Codex CLI — Brian John, Betterup](https://www.youtube.com/watch?v=5eJqXtevlXg); publication: 2025-11-24T20:16:36Z; analysis: `analysis/5eJqXtevlXg.json`.
[^YpY83-kA7Bo]: [2025 in LLMs so far, illustrated by Pelicans on Bicycles — Simon Willison](https://www.youtube.com/watch?v=YpY83-kA7Bo); publication: 2025-07-09T16:00:06Z; analysis: `analysis/YpY83-kA7Bo.json`.
