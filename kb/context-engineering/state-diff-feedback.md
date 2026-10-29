---
{
  "type": "technique",
  "id": "state-diff-feedback",
  "title": "Return explicit observed state diffs after actions rather than only prose success claims",
  "area": "context-engineering",
  "status": "stable",
  "valid_from": "2026-06-28T15:30:40Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "JnubYCYunk8",
      "resource": "https://www.youtube.com/watch?v=JnubYCYunk8",
      "title": "Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI",
      "author": "Kushan Raj, Sarvam AI",
      "last_modified": "2026-06-28T15:30:40Z",
      "analysis_file": "analysis/JnubYCYunk8.json"
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

# Return explicit observed state diffs after actions rather than only prose success claims

## What

Return explicit observed state diffs after actions rather than only prose success claims

Tell the agent what newly appeared, what disappeared, and why a click failed, by tracking end-to-end page state across steps.

## Evidence

Source analysis [^JnubYCYunk8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less irrelevant or duplicated input
- **Speed:** Less context assembly and rereading
- **Quality:** Better preservation and use of decisive evidence
- **Reliability:** Detect missing, stale or transformed source material
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^JnubYCYunk8]: [Browser Agents Don't Need Better Models. They Need Better Eyes. - Kushan Raj, Sarvam AI](https://www.youtube.com/watch?v=JnubYCYunk8); publication: 2026-06-28T15:30:40Z; analysis: `analysis/JnubYCYunk8.json`.
