---
{
  "type": "technique",
  "id": "cross-repo-learning",
  "title": "Reuse proven sibling-repository patterns with provenance",
  "area": "retrieval-code-navigation",
  "status": "stable",
  "valid_from": "2026-10-12T15:00:19Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "MGzymaYBiss",
      "resource": "https://www.youtube.com/watch?v=MGzymaYBiss",
      "title": "Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I",
      "author": "Dan Shipper, Every, AI & I",
      "last_modified": "2025-12-18T18:00:06Z",
      "analysis_file": "analysis/MGzymaYBiss.json"
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
      "id": "ZRM_TfEZcIo",
      "resource": "https://www.youtube.com/watch?v=ZRM_TfEZcIo",
      "title": "Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "author": "Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI",
      "last_modified": "2026-06-26T14:00:07Z",
      "analysis_file": "analysis/ZRM_TfEZcIo.json"
    },
    {
      "id": "am_oeAoUhew",
      "resource": "https://www.youtube.com/watch?v=am_oeAoUhew",
      "title": "Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI",
      "author": "Ryan Lopopolo, OpenAI",
      "last_modified": "2026-04-17T00:29:28Z",
      "analysis_file": "analysis/am_oeAoUhew.json"
    },
    {
      "id": "jVjt-2g8NMY",
      "resource": "https://www.youtube.com/watch?v=jVjt-2g8NMY",
      "title": "A Genius With Amnesia - Victor Savkin, Nx",
      "author": "Victor Savkin, Nx",
      "last_modified": "2026-06-26T01:15:06Z",
      "analysis_file": "analysis/jVjt-2g8NMY.json"
    },
    {
      "id": "kiqubc5b5Yo",
      "resource": "https://www.youtube.com/watch?v=kiqubc5b5Yo",
      "title": "Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo",
      "author": "Brendan Rappazzo",
      "last_modified": "2026-07-29T17:06:26Z",
      "analysis_file": "analysis/kiqubc5b5Yo.json"
    },
    {
      "id": "oixzVKMAXG0",
      "resource": "https://www.youtube.com/watch?v=oixzVKMAXG0",
      "title": "Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway",
      "author": "Mahmoud Abdelwahab, Railway",
      "last_modified": "2026-10-12T15:00:19Z",
      "analysis_file": "analysis/oixzVKMAXG0.json"
    },
    {
      "id": "ojJXgXLUQFc",
      "resource": "https://www.youtube.com/watch?v=ojJXgXLUQFc",
      "title": "The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian",
      "author": "Andy Wong, Andrei Bocan & Shane Wolf, Atlassian",
      "last_modified": "2026-10-11T14:30:40Z",
      "analysis_file": "analysis/ojJXgXLUQFc.json"
    },
    {
      "id": "rnDm57Py54A",
      "resource": "https://www.youtube.com/watch?v=rnDm57Py54A",
      "title": "Building your own software factory — Eric Zakariasson, Cursor",
      "author": "Eric Zakariasson, Cursor",
      "last_modified": "2026-04-28T18:00:06Z",
      "analysis_file": "analysis/rnDm57Py54A.json"
    },
    {
      "id": "s-aixZYJG4c",
      "resource": "https://www.youtube.com/watch?v=s-aixZYJG4c",
      "title": "The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo",
      "author": "Itamar Friedman, Qodo",
      "last_modified": "2026-08-20T13:30:38Z",
      "analysis_file": "analysis/s-aixZYJG4c.json"
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

# Reuse proven sibling-repository patterns with provenance

## What

Reuse proven sibling-repository patterns with provenance

An agent can transfer the design process from a reference implementation into a different target stack.

## Evidence

> the hard part there is obviously figuring out the boundaries between the
> — 1:32:10 [^KhRjivBSwiw]

> And the reason is because it makes it AI makes it much easier to translate
> — 14:46 [^MGzymaYBiss]

> need to re-implement and re-implement it yourself in your own tech stack and your
> — 11:51 [^MGzymaYBiss]

> to do right you can do it with under 100 developer hours because they're just
> — 05:04 [^Ve-akpov78Q]

Source analysis [^ZRM_TfEZcIo]; no independently matched timestamped quote published.

> you should have one way to like do a bounded concurrency helper. You should
> — 35:31 [^am_oeAoUhew]

> I can make it replicate the approach used in the session by an engineer I
> — 17:19 [^jVjt-2g8NMY]

> bonds could really transfer well to like muni bonds, and that kind of translation
> — 01:54 [^kiqubc5b5Yo]

Source analysis [^oixzVKMAXG0]; no independently matched timestamped quote published.

Source analysis [^ojJXgXLUQFc]; no independently matched timestamped quote published.

> point the agent to like existing references and just asking this to
> — 06:06 [^rnDm57Py54A]

> contract between two uh piece of your software, but also links to history of
> — 13:22 [^s-aixZYJG4c]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Less repeated discovery and overfetch
- **Speed:** Faster file/evidence location
- **Quality:** Higher relevant-evidence coverage
- **Reliability:** Versioned, reproducible retrieval with explicit misses
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^MGzymaYBiss]: [Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I](https://www.youtube.com/watch?v=MGzymaYBiss); publication: 2025-12-18T18:00:06Z; analysis: `analysis/MGzymaYBiss.json`.
[^Ve-akpov78Q]: [Code Generation and Maintenance at Scale: Morgante Pell](https://www.youtube.com/watch?v=Ve-akpov78Q); publication: 2024-10-17T18:52:20Z; analysis: `analysis/Ve-akpov78Q.json`.
[^ZRM_TfEZcIo]: [Turn 10,994 Notes Into Memory - Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI](https://www.youtube.com/watch?v=ZRM_TfEZcIo); publication: 2026-06-26T14:00:07Z; analysis: `analysis/ZRM_TfEZcIo.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^jVjt-2g8NMY]: [A Genius With Amnesia - Victor Savkin, Nx](https://www.youtube.com/watch?v=jVjt-2g8NMY); publication: 2026-06-26T01:15:06Z; analysis: `analysis/jVjt-2g8NMY.json`.
[^kiqubc5b5Yo]: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo); publication: 2026-07-29T17:06:26Z; analysis: `analysis/kiqubc5b5Yo.json`.
[^oixzVKMAXG0]: [Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway](https://www.youtube.com/watch?v=oixzVKMAXG0); publication: 2026-10-12T15:00:19Z; analysis: `analysis/oixzVKMAXG0.json`.
[^ojJXgXLUQFc]: [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](https://www.youtube.com/watch?v=ojJXgXLUQFc); publication: 2026-10-11T14:30:40Z; analysis: `analysis/ojJXgXLUQFc.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
[^s-aixZYJG4c]: [The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=s-aixZYJG4c); publication: 2026-08-20T13:30:38Z; analysis: `analysis/s-aixZYJG4c.json`.
