---
{
  "type": "technique",
  "id": "targeted-edits",
  "title": "Make small structural or exact-match edits rather than rewriting whole files",
  "area": "tools-agent-interfaces",
  "status": "stable",
  "valid_from": "2026-08-10T16:00:06Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "RFKCzGlAU6Q",
      "resource": "https://www.youtube.com/watch?v=RFKCzGlAU6Q",
      "title": "How Claude Code Works - Jared Zoneraich, PromptLayer",
      "author": "Jared Zoneraich, PromptLayer",
      "last_modified": "2025-12-26T22:04:34Z",
      "analysis_file": "analysis/RFKCzGlAU6Q.json"
    },
    {
      "id": "Ve-akpov78Q",
      "resource": "https://www.youtube.com/watch?v=Ve-akpov78Q",
      "title": "Code Generation and Maintenance at Scale: Morgante Pell",
      "author": null,
      "last_modified": "2024-10-17T18:52:20Z",
      "analysis_file": "analysis/Ve-akpov78Q.json"
    },
    {
      "id": "WXy8Yy9xGss",
      "resource": "https://www.youtube.com/watch?v=WXy8Yy9xGss",
      "title": "CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed",
      "author": "Nathan Sobo, Zed",
      "last_modified": "2025-06-27T09:22:37Z",
      "analysis_file": "analysis/WXy8Yy9xGss.json"
    },
    {
      "id": "XNtkiQJ49Ps",
      "resource": "https://www.youtube.com/watch?v=XNtkiQJ49Ps",
      "title": "Agents need more than a chat - Jacob Lauritzen, CTO Legora",
      "author": "Jacob Lauritzen, CTO Legora",
      "last_modified": "2026-04-22T15:15:06Z",
      "analysis_file": "analysis/XNtkiQJ49Ps.json"
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
      "id": "shRR1e2HXMk",
      "resource": "https://www.youtube.com/watch?v=shRR1e2HXMk",
      "title": "How Codex Works — Dominik Kundel, OpenAI",
      "author": "Dominik Kundel, OpenAI",
      "last_modified": "2026-08-10T16:00:06Z",
      "analysis_file": "analysis/shRR1e2HXMk.json"
    },
    {
      "id": "w7IMuYsBNr8",
      "resource": "https://www.youtube.com/watch?v=w7IMuYsBNr8",
      "title": "OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)",
      "author": "Fouad Matin (Codex, Agent Robustness)",
      "last_modified": "2025-07-30T15:00:06Z",
      "analysis_file": "analysis/w7IMuYsBNr8.json"
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

# Make small structural or exact-match edits rather than rewriting whole files

## What

Make small structural or exact-match edits rather than rewriting whole files

A before/after code representation avoids fragile line-number arithmetic and can ignore irrelevant syntactic detail, but approximate application must be constrained to a unique authorized target.

## Evidence

> edit is it's using diffs and it's not rewriting files most of the time. uh way
> — 14:06 [^RFKCzGlAU6Q]

> being just a before snippet and this is something you might have like in a
> — 17:37 [^Ve-akpov78Q]

> gets more expensive so you really don't want to Output entire large files as
> — 16:45 [^Ve-akpov78Q]

> do this dynamic programming that gets us an approximate match really saved a lot
> — 07:26 [^WXy8Yy9xGss]

> some cases would just have an empty old text tag which like if you're doing old
> — 08:25 [^WXy8Yy9xGss]

> You can highlight clause three and it will only change clause three. You can
> — 12:06 [^XNtkiQJ49Ps]

> find and replace type editor or a diff based editor to allow the LLM to just
> — 05:08 [^o_hhkJtlbSs]

> patch tool to do file editing, which means that they're used to using that to
> — 10:23 [^shRR1e2HXMk]

Source analysis [^w7IMuYsBNr8]; no independently matched timestamped quote published.

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer model-owned steps and malformed calls
- **Speed:** Shorter reliable tool chains
- **Quality:** Clearer contracts and evidence
- **Reliability:** Fail-loud errors and recoverable execution
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^RFKCzGlAU6Q]: [How Claude Code Works - Jared Zoneraich, PromptLayer](https://www.youtube.com/watch?v=RFKCzGlAU6Q); publication: 2025-12-26T22:04:34Z; analysis: `analysis/RFKCzGlAU6Q.json`.
[^Ve-akpov78Q]: [Code Generation and Maintenance at Scale: Morgante Pell](https://www.youtube.com/watch?v=Ve-akpov78Q); publication: 2024-10-17T18:52:20Z; analysis: `analysis/Ve-akpov78Q.json`.
[^WXy8Yy9xGss]: [CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed](https://www.youtube.com/watch?v=WXy8Yy9xGss); publication: 2025-06-27T09:22:37Z; analysis: `analysis/WXy8Yy9xGss.json`.
[^XNtkiQJ49Ps]: [Agents need more than a chat - Jacob Lauritzen, CTO Legora](https://www.youtube.com/watch?v=XNtkiQJ49Ps); publication: 2026-04-22T15:15:06Z; analysis: `analysis/XNtkiQJ49Ps.json`.
[^o_hhkJtlbSs]: [Software Development Agents: What Works and What Doesn't - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=o_hhkJtlbSs); publication: 2025-07-25T23:10:11Z; analysis: `analysis/o_hhkJtlbSs.json`.
[^shRR1e2HXMk]: [How Codex Works — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=shRR1e2HXMk); publication: 2026-08-10T16:00:06Z; analysis: `analysis/shRR1e2HXMk.json`.
[^w7IMuYsBNr8]: [OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)](https://www.youtube.com/watch?v=w7IMuYsBNr8); publication: 2025-07-30T15:00:06Z; analysis: `analysis/w7IMuYsBNr8.json`.
