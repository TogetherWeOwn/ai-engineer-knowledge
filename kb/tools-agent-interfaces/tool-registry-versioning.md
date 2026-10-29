---
{
  "type": "technique",
  "id": "tool-registry-versioning",
  "title": "Version the tool registry and invalidate derived discovery indexes after contract changes",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-06-28T15:15:15Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "n9rjuBuShko",
      "resource": "https://www.youtube.com/watch?v=n9rjuBuShko",
      "title": "Building LinkedIn's GenAI Platform — Xiaofeng Wang",
      "author": "Xiaofeng Wang",
      "last_modified": "2025-04-16T16:00:06Z",
      "analysis_file": "analysis/n9rjuBuShko.json"
    },
    {
      "id": "vh2VGuQ3zhY",
      "resource": "https://www.youtube.com/watch?v=vh2VGuQ3zhY",
      "title": "The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica",
      "author": "Sohail Shaikh & Ankush Rastogi, Prosodica",
      "last_modified": "2026-06-28T15:15:15Z",
      "analysis_file": "analysis/vh2VGuQ3zhY.json"
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

# Version the tool registry and invalidate derived discovery indexes after contract changes

## What

Version the tool registry and invalidate derived discovery indexes after contract changes

Keep authoritative names, schemas, ownership and versions in one catalog; derive cached indexes offline and rebuild when definitions change.

## Evidence

Source analysis [^n9rjuBuShko]; no independently matched timestamped quote published.

Source analysis [^vh2VGuQ3zhY]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^n9rjuBuShko]: [Building LinkedIn's GenAI Platform — Xiaofeng Wang](https://www.youtube.com/watch?v=n9rjuBuShko); publication: 2025-04-16T16:00:06Z; analysis: `analysis/n9rjuBuShko.json`.
[^vh2VGuQ3zhY]: [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](https://www.youtube.com/watch?v=vh2VGuQ3zhY); publication: 2026-06-28T15:15:15Z; analysis: `analysis/vh2VGuQ3zhY.json`.
