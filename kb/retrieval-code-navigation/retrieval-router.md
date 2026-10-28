---
{
  "type": "technique",
  "id": "retrieval-router",
  "title": "Choose exact, lexical, semantic, graph or filtered retrieval according to the question",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-09-26T14:30:38Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KcVkq5L-0f0",
      "resource": "https://www.youtube.com/watch?v=KcVkq5L-0f0",
      "title": "Your agents lack context: Here's how to fix \"You're absolutely right!\" — Brandon Waselnuk, Unblocked",
      "author": "Brandon Waselnuk, Unblocked",
      "last_modified": "2026-09-09T14:30:12Z",
      "analysis_file": "analysis/KcVkq5L-0f0.json"
    },
    {
      "id": "O84lhGc1OOI",
      "resource": "https://www.youtube.com/watch?v=O84lhGc1OOI",
      "title": "If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread",
      "author": "Benjamin Clavié, Mixedbread",
      "last_modified": "2026-09-16T15:00:39Z",
      "analysis_file": "analysis/O84lhGc1OOI.json"
    },
    {
      "id": "V_5bn4q-vAI",
      "resource": "https://www.youtube.com/watch?v=V_5bn4q-vAI",
      "title": "How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth",
      "author": "Christopher Burns, Inth",
      "last_modified": "2026-08-26T15:30:07Z",
      "analysis_file": "analysis/V_5bn4q-vAI.json"
    },
    {
      "id": "bVNNvWq6dKo",
      "resource": "https://www.youtube.com/watch?v=bVNNvWq6dKo",
      "title": "How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf",
      "author": "Kevin Hou, Windsurf",
      "last_modified": "2025-03-11T19:17:46Z",
      "analysis_file": "analysis/bVNNvWq6dKo.json"
    },
    {
      "id": "gsedOXz8FX4",
      "resource": "https://www.youtube.com/watch?v=gsedOXz8FX4",
      "title": "Memory Masterclass: Make Your AI Agents Remember What They Do! — Mark Bain, AIUS",
      "author": "Mark Bain, AIUS",
      "last_modified": "2025-06-27T09:51:20Z",
      "analysis_file": "analysis/gsedOXz8FX4.json"
    },
    {
      "id": "gvIAkmZUEZY",
      "resource": "https://www.youtube.com/watch?v=gvIAkmZUEZY",
      "title": "Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code",
      "author": "Beyang Liu, Amp Code",
      "last_modified": "2025-12-22T17:00:06Z",
      "analysis_file": "analysis/gvIAkmZUEZY.json"
    },
    {
      "id": "hd7TOvmyAxU",
      "resource": "https://www.youtube.com/watch?v=hd7TOvmyAxU",
      "title": "An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases",
      "author": "Tim Sweeney, Weights & Biases",
      "last_modified": "2026-09-26T14:30:38Z",
      "analysis_file": "analysis/hd7TOvmyAxU.json"
    },
    {
      "id": "hxFpUcvWPcU",
      "resource": "https://www.youtube.com/watch?v=hxFpUcvWPcU",
      "title": "How to build Enterprise Aware Agents - Chau Tran, Glean",
      "author": "Chau Tran, Glean",
      "last_modified": "2025-07-24T09:22:32Z",
      "analysis_file": "analysis/hxFpUcvWPcU.json"
    },
    {
      "id": "ynJyIKwjonM",
      "resource": "https://www.youtube.com/watch?v=ynJyIKwjonM",
      "title": "Agentic Search for Context Engineering — Leonie Monigatti, Elastic",
      "author": "Leonie Monigatti, Elastic",
      "last_modified": "2026-05-08T13:00:06Z",
      "analysis_file": "analysis/ynJyIKwjonM.json"
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

# Choose exact, lexical, semantic, graph or filtered retrieval according to the question

## What

Choose exact, lexical, semantic, graph or filtered retrieval according to the question

Semantic nearest neighbors can miss exact acronyms; grep cannot efficiently cover arbitrary semantic variations.

## Evidence

> provide a link quickly, unfurl it, get that document back and move along. So,
> — 08:39 [^KcVkq5L-0f0]

> primitive. PM25 is a primitive and semantic search is a primitive and all
> — 16:44 [^O84lhGc1OOI]

Source analysis [^V_5bn4q-vAI]; no independently matched timestamped quote published.

Source analysis [^bVNNvWq6dKo]; no independently matched timestamped quote published.

Source analysis [^gsedOXz8FX4]; no independently matched timestamped quote published.

> fetch context beyond the codebase. So from libraries and frameworks that you
> — 08:50 [^gvIAkmZUEZY]

> agent context about your business domain, the underlying uh primitives
> — 20:04 [^hd7TOvmyAxU]

> accomplish a new task we'll find the most similar task in the training data
> — 13:39 [^hxFpUcvWPcU]

> it knows for exact matches you probably still want to use grap. And for um more
> — 42:56 [^ynJyIKwjonM]

> you need, then you would actually might want to have a second round of search,
> — 03:37 [^ynJyIKwjonM]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KcVkq5L-0f0]: [Your agents lack context: Here's how to fix "You're absolutely right!" — Brandon Waselnuk, Unblocked](https://www.youtube.com/watch?v=KcVkq5L-0f0); publication: 2026-09-09T14:30:12Z; analysis: `analysis/KcVkq5L-0f0.json`.
[^O84lhGc1OOI]: [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI); publication: 2026-09-16T15:00:39Z; analysis: `analysis/O84lhGc1OOI.json`.
[^V_5bn4q-vAI]: [How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth](https://www.youtube.com/watch?v=V_5bn4q-vAI); publication: 2026-08-26T15:30:07Z; analysis: `analysis/V_5bn4q-vAI.json`.
[^bVNNvWq6dKo]: [How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=bVNNvWq6dKo); publication: 2025-03-11T19:17:46Z; analysis: `analysis/bVNNvWq6dKo.json`.
[^gsedOXz8FX4]: [Memory Masterclass: Make Your AI Agents Remember What They Do! — Mark Bain, AIUS](https://www.youtube.com/watch?v=gsedOXz8FX4); publication: 2025-06-27T09:51:20Z; analysis: `analysis/gsedOXz8FX4.json`.
[^gvIAkmZUEZY]: [Amp Code: Next Generation AI Coding – Beyang Liu, Amp Code](https://www.youtube.com/watch?v=gvIAkmZUEZY); publication: 2025-12-22T17:00:06Z; analysis: `analysis/gvIAkmZUEZY.json`.
[^hd7TOvmyAxU]: [An AI Research Agent That Runs Your Experiments — Tim Sweeney, Weights & Biases](https://www.youtube.com/watch?v=hd7TOvmyAxU); publication: 2026-09-26T14:30:38Z; analysis: `analysis/hd7TOvmyAxU.json`.
[^hxFpUcvWPcU]: [How to build Enterprise Aware Agents - Chau Tran, Glean](https://www.youtube.com/watch?v=hxFpUcvWPcU); publication: 2025-07-24T09:22:32Z; analysis: `analysis/hxFpUcvWPcU.json`.
[^ynJyIKwjonM]: [Agentic Search for Context Engineering — Leonie Monigatti, Elastic](https://www.youtube.com/watch?v=ynJyIKwjonM); publication: 2026-05-08T13:00:06Z; analysis: `analysis/ynJyIKwjonM.json`.
