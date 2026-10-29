---
{
  "type": "technique",
  "id": "policy-valid-recovery",
  "title": "Treat denials as boundaries and offer a permitted recovery path",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-19T23:00:08Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1lgFGaHoGq8",
      "resource": "https://www.youtube.com/watch?v=1lgFGaHoGq8",
      "title": "AI’s Jurassic Park Period — Aaron Stanley, dbt Labs",
      "author": "Aaron Stanley, dbt Labs",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/1lgFGaHoGq8.json"
    },
    {
      "id": "Btk8wDUVs74",
      "resource": "https://www.youtube.com/watch?v=Btk8wDUVs74",
      "title": "From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com",
      "author": "Omri Bruchim & Tomer Ast, monday.com",
      "last_modified": "2026-07-22T23:00:11Z",
      "analysis_file": "analysis/Btk8wDUVs74.json"
    },
    {
      "id": "Cc0_nyxROBA",
      "resource": "https://www.youtube.com/watch?v=Cc0_nyxROBA",
      "title": "From RL to IRL — Gaurav Mishra, Amazon AGI Lab",
      "author": "Gaurav Mishra, Amazon AGI Lab",
      "last_modified": "2026-08-14T16:00:06Z",
      "analysis_file": "analysis/Cc0_nyxROBA.json"
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
      "id": "_4Ph2dhmUFI",
      "resource": "https://www.youtube.com/watch?v=_4Ph2dhmUFI",
      "title": "How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase",
      "author": "Evan Kormos, Coinbase",
      "last_modified": "2026-10-19T23:00:08Z",
      "analysis_file": "analysis/_4Ph2dhmUFI.json"
    },
    {
      "id": "_cVfz88_j7A",
      "resource": "https://www.youtube.com/watch?v=_cVfz88_j7A",
      "title": "Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs",
      "author": "Anant Shankhdhar, Risa Labs",
      "last_modified": "2026-07-20T06:24:47Z",
      "analysis_file": "analysis/_cVfz88_j7A.json"
    },
    {
      "id": "il1c1a2FufU",
      "resource": "https://www.youtube.com/watch?v=il1c1a2FufU",
      "title": "Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex",
      "author": null,
      "last_modified": "2026-07-24T15:00:06Z",
      "analysis_file": "analysis/il1c1a2FufU.json"
    },
    {
      "id": "o_hhkJtlbSs",
      "resource": "https://www.youtube.com/watch?v=o_hhkJtlbSs",
      "title": "Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2025-07-25T23:10:11Z",
      "analysis_file": "analysis/o_hhkJtlbSs.json"
    },
    {
      "id": "vJukHCIv7Ck",
      "resource": "https://www.youtube.com/watch?v=vJukHCIv7Ck",
      "title": "Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS",
      "author": "Elizabeth Fuentes, AWS",
      "last_modified": "2026-07-11T21:45:00Z",
      "analysis_file": "analysis/vJukHCIv7Ck.json"
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

# Treat denials as boundaries and offer a permitted recovery path

## What

Treat denials as boundaries and offer a permitted recovery path

## Evidence

Source analysis [^1lgFGaHoGq8]; no independently matched timestamped quote published.

Source analysis [^Btk8wDUVs74]; no independently matched timestamped quote published.

Source analysis [^Cc0_nyxROBA]; no independently matched timestamped quote published.

> going to say if I receive six, I can steer the booking for two rooms. So you
> — 45:53 [^YXiLj4tJt5A]

Source analysis [^_4Ph2dhmUFI]; no independently matched timestamped quote published.

> break during the run time. For this, we have a self-healing loop
> — 05:18 [^_cVfz88_j7A]

> about, right? These are like real security issues. And again, um,
> — 54:37 [^il1c1a2FufU]

> though, just throw away that work. Start fresh with a new prompt based on uh what
> — 10:06 [^o_hhkJtlbSs]

> and that's it. So, use hook for hard constraints.
> — 51:05 [^vJukHCIv7Ck]

Source analysis [^vh2VGuQ3zhY]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1lgFGaHoGq8]: [AI’s Jurassic Park Period — Aaron Stanley, dbt Labs](https://www.youtube.com/watch?v=1lgFGaHoGq8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/1lgFGaHoGq8.json`.
[^Btk8wDUVs74]: [From Systems of Record to Systems of Context — Omri Bruchim & Tomer Ast, monday.com](https://www.youtube.com/watch?v=Btk8wDUVs74); publication: 2026-07-22T23:00:11Z; analysis: `analysis/Btk8wDUVs74.json`.
[^Cc0_nyxROBA]: [From RL to IRL — Gaurav Mishra, Amazon AGI Lab](https://www.youtube.com/watch?v=Cc0_nyxROBA); publication: 2026-08-14T16:00:06Z; analysis: `analysis/Cc0_nyxROBA.json`.
[^YXiLj4tJt5A]: [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](https://www.youtube.com/watch?v=YXiLj4tJt5A); publication: 2026-10-11T15:00:05Z; analysis: `analysis/YXiLj4tJt5A.json`.
[^_4Ph2dhmUFI]: [How to Know When an AI Agent Can Work Unsupervised — Evan Kormos, Coinbase](https://www.youtube.com/watch?v=_4Ph2dhmUFI); publication: 2026-10-19T23:00:08Z; analysis: `analysis/_4Ph2dhmUFI.json`.
[^_cVfz88_j7A]: [Can Oncology Workflows Run Without Human Touch? - Anant Shankhdhar, Risa Labs](https://www.youtube.com/watch?v=_cVfz88_j7A); publication: 2026-07-20T06:24:47Z; analysis: `analysis/_cVfz88_j7A.json`.
[^il1c1a2FufU]: [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](https://www.youtube.com/watch?v=il1c1a2FufU); publication: 2026-07-24T15:00:06Z; analysis: `analysis/il1c1a2FufU.json`.
[^o_hhkJtlbSs]: [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=o_hhkJtlbSs); publication: 2025-07-25T23:10:11Z; analysis: `analysis/o_hhkJtlbSs.json`.
[^vJukHCIv7Ck]: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns - Elizabeth Fuentes, AWS](https://www.youtube.com/watch?v=vJukHCIv7Ck); publication: 2026-07-11T21:45:00Z; analysis: `analysis/vJukHCIv7Ck.json`.
[^vh2VGuQ3zhY]: [The 100-Tool Agent Is a Trap - Sohail Shaikh & Ankush Rastogi, Prosodica](https://www.youtube.com/watch?v=vh2VGuQ3zhY); publication: 2026-06-28T15:15:15Z; analysis: `analysis/vh2VGuQ3zhY.json`.
