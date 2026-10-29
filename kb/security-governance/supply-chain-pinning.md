---
{
  "type": "technique",
  "id": "supply-chain-pinning",
  "title": "Pin and review dependencies, skills and external tool definitions",
  "area": "security-governance",
  "status": "stable",
  "valid_from": "2026-10-11T20:30:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "9WiBJRO84yY",
      "resource": "https://www.youtube.com/watch?v=9WiBJRO84yY",
      "title": "Building on the Codex Harness — Dominik Kundel, OpenAI",
      "author": "Dominik Kundel, OpenAI",
      "last_modified": "2026-10-09T15:30:04Z",
      "analysis_file": "analysis/9WiBJRO84yY.json"
    },
    {
      "id": "CD6R4Wf3jnY",
      "resource": "https://www.youtube.com/watch?v=CD6R4Wf3jnY",
      "title": "Gateways are All You Need — Karan Sampath, Anthropic",
      "author": "Karan Sampath, Anthropic",
      "last_modified": "2026-04-27T21:00:06Z",
      "analysis_file": "analysis/CD6R4Wf3jnY.json"
    },
    {
      "id": "FCi4jT86gSw",
      "resource": "https://www.youtube.com/watch?v=FCi4jT86gSw",
      "title": "MCP Is Not Good Yet — David Cramer, Sentry",
      "author": "David Cramer, Sentry",
      "last_modified": "2025-07-03T16:00:06Z",
      "analysis_file": "analysis/FCi4jT86gSw.json"
    },
    {
      "id": "GVbPiq3Pet0",
      "resource": "https://www.youtube.com/watch?v=GVbPiq3Pet0",
      "title": "Building security around ML: Dr. Andrew Davis",
      "author": null,
      "last_modified": "2025-02-08T21:31:25Z",
      "analysis_file": "analysis/GVbPiq3Pet0.json"
    },
    {
      "id": "JRTAtZ5iBkU",
      "resource": "https://www.youtube.com/watch?v=JRTAtZ5iBkU",
      "title": "HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori",
      "author": "Amol Kapoor, Nori",
      "last_modified": "2026-06-28T18:30:30Z",
      "analysis_file": "analysis/JRTAtZ5iBkU.json"
    },
    {
      "id": "KhRjivBSwiw",
      "resource": "https://www.youtube.com/watch?v=KhRjivBSwiw",
      "title": "The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef",
      "author": "Yoni Michael & Brandon Callender, Typedef",
      "last_modified": "2026-10-11T12:30:23Z",
      "analysis_file": "analysis/KhRjivBSwiw.json"
    },
    {
      "id": "LC3-P7v3yoI",
      "resource": "https://www.youtube.com/watch?v=LC3-P7v3yoI",
      "title": "Skills are the New SDKs - Elvin Aghammadzada, DataRobot",
      "author": "Elvin Aghammadzada, DataRobot",
      "last_modified": "2026-07-20T06:24:53Z",
      "analysis_file": "analysis/LC3-P7v3yoI.json"
    },
    {
      "id": "M05vON8i0aI",
      "resource": "https://www.youtube.com/watch?v=M05vON8i0aI",
      "title": "AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack",
      "author": "Imad Touil, QuantumBlack",
      "last_modified": "2026-08-28T18:30:04Z",
      "analysis_file": "analysis/M05vON8i0aI.json"
    },
    {
      "id": "MhHEGMFCEB0",
      "resource": "https://www.youtube.com/watch?v=MhHEGMFCEB0",
      "title": "OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman",
      "author": "Vaibhav Srivastav & Katia Gil Guzman",
      "last_modified": "2026-04-29T16:00:06Z",
      "analysis_file": "analysis/MhHEGMFCEB0.json"
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
      "id": "RjfbvDXpFls",
      "resource": "https://www.youtube.com/watch?v=RjfbvDXpFls",
      "title": "Building pi in a World of Slop — Mario Zechner",
      "author": "Mario Zechner",
      "last_modified": "2026-04-16T22:58:06Z",
      "analysis_file": "analysis/RjfbvDXpFls.json"
    },
    {
      "id": "XZ0boOjtbNo",
      "resource": "https://www.youtube.com/watch?v=XZ0boOjtbNo",
      "title": "AI Didn’t Kill the Web, It Moved in! — Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)",
      "author": "Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)",
      "last_modified": "2026-04-10T00:24:17Z",
      "analysis_file": "analysis/XZ0boOjtbNo.json"
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
      "id": "ZyC56eV8sVw",
      "resource": "https://www.youtube.com/watch?v=ZyC56eV8sVw",
      "title": "AI Security Engineer Foundations + Certificate — Javier Garza, Snyk",
      "author": "Javier Garza, Snyk",
      "last_modified": "2026-10-11T19:30:16Z",
      "analysis_file": "analysis/ZyC56eV8sVw.json"
    },
    {
      "id": "_Zcw_sVF6hU",
      "resource": "https://www.youtube.com/watch?v=_Zcw_sVF6hU",
      "title": "The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "author": "Armin Ronacher & Cristina Poncela Cubeiro, Earendil",
      "last_modified": "2026-04-18T10:30:06Z",
      "analysis_file": "analysis/_Zcw_sVF6hU.json"
    },
    {
      "id": "aV_vgUSatqs",
      "resource": "https://www.youtube.com/watch?v=aV_vgUSatqs",
      "title": "Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal",
      "author": "Mark Lummus & Navinkumar Patil, PayPal",
      "last_modified": "2026-10-11T20:30:04Z",
      "analysis_file": "analysis/aV_vgUSatqs.json"
    },
    {
      "id": "bSG9wUYaHWU",
      "resource": "https://www.youtube.com/watch?v=bSG9wUYaHWU",
      "title": "Context Is the New Code — Patrick Debois, Tessl",
      "author": "Patrick Debois, Tessl",
      "last_modified": "2026-05-03T14:00:06Z",
      "analysis_file": "analysis/bSG9wUYaHWU.json"
    },
    {
      "id": "c35YoMdnI78",
      "resource": "https://www.youtube.com/watch?v=c35YoMdnI78",
      "title": "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "author": "Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents",
      "last_modified": "2026-07-17T21:00:06Z",
      "analysis_file": "analysis/c35YoMdnI78.json"
    },
    {
      "id": "cgimkNGNjvU",
      "resource": "https://www.youtube.com/watch?v=cgimkNGNjvU",
      "title": "Agentic Development Security — Ezra Tanzer, Snyk",
      "author": "Ezra Tanzer, Snyk",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/cgimkNGNjvU.json"
    },
    {
      "id": "i1uPAN6uW4s",
      "resource": "https://www.youtube.com/watch?v=i1uPAN6uW4s",
      "title": "Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,",
      "author": "Harald Kirshner,",
      "last_modified": "2025-06-27T10:15:59Z",
      "analysis_file": "analysis/i1uPAN6uW4s.json"
    },
    {
      "id": "iKQ78wyJEXU",
      "resource": "https://www.youtube.com/watch?v=iKQ78wyJEXU",
      "title": "We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank",
      "author": "Lucas Palma, Nubank",
      "last_modified": "2026-07-29T22:00:06Z",
      "analysis_file": "analysis/iKQ78wyJEXU.json"
    },
    {
      "id": "jdeMJJ_oNYg",
      "resource": "https://www.youtube.com/watch?v=jdeMJJ_oNYg",
      "title": "LLM Safeguards: Security Privacy Compliance Anti Hallucination: Daniel Whitenack",
      "author": null,
      "last_modified": "2024-12-31T17:28:40Z",
      "analysis_file": "analysis/jdeMJJ_oNYg.json"
    },
    {
      "id": "p-2MT8KYZqU",
      "resource": "https://www.youtube.com/watch?v=p-2MT8KYZqU",
      "title": "AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk",
      "author": "Micah Silverman, Snyk",
      "last_modified": "2026-10-11T13:30:04Z",
      "analysis_file": "analysis/p-2MT8KYZqU.json"
    },
    {
      "id": "sJ2jc7leKBk",
      "resource": "https://www.youtube.com/watch?v=sJ2jc7leKBk",
      "title": "I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)",
      "author": "Radek Sienkiewicz (@velvetshark-com)",
      "last_modified": "2026-05-02T22:00:06Z",
      "analysis_file": "analysis/sJ2jc7leKBk.json"
    },
    {
      "id": "tHJSZ1-ZqcA",
      "resource": "https://www.youtube.com/watch?v=tHJSZ1-ZqcA",
      "title": "The Agent Awakens: Collaborative Development with Copilot - Christopher Harrison, GitHub",
      "author": "Christopher Harrison, GitHub",
      "last_modified": "2025-06-27T10:11:01Z",
      "analysis_file": "analysis/tHJSZ1-ZqcA.json"
    },
    {
      "id": "u-o0sW9nwmk",
      "resource": "https://www.youtube.com/watch?v=u-o0sW9nwmk",
      "title": "From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer",
      "author": "Rafal Wilinski, Runlayer",
      "last_modified": "2026-10-07T14:00:10Z",
      "analysis_file": "analysis/u-o0sW9nwmk.json"
    },
    {
      "id": "utTqdQpe39A",
      "resource": "https://www.youtube.com/watch?v=utTqdQpe39A",
      "title": "GitHub's AI Powered Security Platform: Sarah Khalife",
      "author": null,
      "last_modified": "2025-02-08T21:31:24Z",
      "analysis_file": "analysis/utTqdQpe39A.json"
    },
    {
      "id": "w7IMuYsBNr8",
      "resource": "https://www.youtube.com/watch?v=w7IMuYsBNr8",
      "title": "OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)",
      "author": "Fouad Matin (Codex, Agent Robustness)",
      "last_modified": "2025-07-30T15:00:06Z",
      "analysis_file": "analysis/w7IMuYsBNr8.json"
    },
    {
      "id": "x4e5O9zN0TE",
      "resource": "https://www.youtube.com/watch?v=x4e5O9zN0TE",
      "title": "Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati",
      "author": "Erina Karati",
      "last_modified": "2026-09-26T16:30:29Z",
      "analysis_file": "analysis/x4e5O9zN0TE.json"
    },
    {
      "id": "yWS0udrIOc8",
      "resource": "https://www.youtube.com/watch?v=yWS0udrIOc8",
      "title": "Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town",
      "author": "Steve Yegge, Gas Town",
      "last_modified": "2026-07-20T17:17:53Z",
      "analysis_file": "analysis/yWS0udrIOc8.json"
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

# Pin and review dependencies, skills and external tool definitions

## What

Pin and review dependencies, skills and external tool definitions

Give each skill one responsibility and explicit inputs/outputs/dependencies so combined procedures do not duplicate or contradict each other.

## Evidence

Source analysis [^9WiBJRO84yY]; no independently matched timestamped quote published.

Source analysis [^CD6R4Wf3jnY]; no independently matched timestamped quote published.

Source analysis [^FCi4jT86gSw]; no independently matched timestamped quote published.

Source analysis [^GVbPiq3Pet0]; no independently matched timestamped quote published.

Source analysis [^JRTAtZ5iBkU]; no independently matched timestamped quote published.

> computed once and then on every commit, it's refreshed atomically, right? So,
> — 14:31 [^KhRjivBSwiw]

> the graph in the same form as rip grab, right? You take the same tool structure
> — 1:01:13 [^KhRjivBSwiw]

> actually the LM generated skills hurts the performance of LM in a sense that it
> — 24:48 [^LC3-P7v3yoI]

> verification control. Just like how NPM was scary 10 years ago in a sense that
> — 25:42 [^LC3-P7v3yoI]

Source analysis [^M05vON8i0aI]; no independently matched timestamped quote published.

Source analysis [^MhHEGMFCEB0]; no independently matched timestamped quote published.

> importantly the tools need to be co-designed with the agents like the
> — 16:13 [^O84lhGc1OOI]

> And you can then bundle all of that up and put it on NPM or on GitHub because I
> — 08:49 [^RjfbvDXpFls]

Source analysis [^XZ0boOjtbNo]; no independently matched timestamped quote published.

> cloud formation is a infrastructure as a code using CDK. So you can explore the
> — 56:32 [^YXiLj4tJt5A]

Source analysis [^ZyC56eV8sVw]; no independently matched timestamped quote published.

> dependency I actually want to have in this code base? Like, do I like the
> — 15:41 [^_Zcw_sVF6hU]

Source analysis [^aV_vgUSatqs]; no independently matched timestamped quote published.

> kind of pieces of context, and then we are able to install pieces of context
> — 14:35 [^bSG9wUYaHWU]

> a loop or other prompting. You need to own your supply chain.
> — 59:18 [^c35YoMdnI78]

> because of AI, but this is because of NPM supply chain attacks. This has been
> — 46:04 [^c35YoMdnI78]

> configured, it will connect to them, retrieve the tool descriptions, analyze
> — 07:43 [^cgimkNGNjvU]

> introduced issues are the only thing that's being surfaced to that agent
> — 06:22 [^cgimkNGNjvU]

> memory. So, even if you remove a malicious skill, they can still persist.
> — 07:18 [^cgimkNGNjvU]

Source analysis [^i1uPAN6uW4s]; no independently matched timestamped quote published.

Source analysis [^iKQ78wyJEXU]; no independently matched timestamped quote published.

Source analysis [^jdeMJJ_oNYg]; no independently matched timestamped quote published.

Source analysis [^p-2MT8KYZqU]; no independently matched timestamped quote published.

Source analysis [^sJ2jc7leKBk]; no independently matched timestamped quote published.

Source analysis [^tHJSZ1-ZqcA]; no independently matched timestamped quote published.

> series of checks like whether it's not containing some kind of prompt injection
> — 15:35 [^u-o0sW9nwmk]

Source analysis [^utTqdQpe39A]; no independently matched timestamped quote published.

Source analysis [^w7IMuYsBNr8]; no independently matched timestamped quote published.

> event and if it crosses a threshold, it will store that specific memory uh in a
> — 04:14 [^x4e5O9zN0TE]

> looks right, but what it downloaded was a backdoor.
> — 03:54 [^yWS0udrIOc8]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Avoid incident recovery and unauthorized side-effect cost
- **Speed:** Reduce unsafe improvisation and repeated denials
- **Quality:** Preserve authorized task correctness
- **Reliability:** Contain credential, data and execution blast radius
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^9WiBJRO84yY]: [Building on the Codex Harness — Dominik Kundel, OpenAI](https://www.youtube.com/watch?v=9WiBJRO84yY); publication: 2026-10-09T15:30:04Z; analysis: `analysis/9WiBJRO84yY.json`.
[^CD6R4Wf3jnY]: [Gateways are All You Need — Karan Sampath, Anthropic](https://www.youtube.com/watch?v=CD6R4Wf3jnY); publication: 2026-04-27T21:00:06Z; analysis: `analysis/CD6R4Wf3jnY.json`.
[^FCi4jT86gSw]: [MCP Is Not Good Yet — David Cramer, Sentry](https://www.youtube.com/watch?v=FCi4jT86gSw); publication: 2025-07-03T16:00:06Z; analysis: `analysis/FCi4jT86gSw.json`.
[^GVbPiq3Pet0]: [Building security around ML: Dr. Andrew Davis](https://www.youtube.com/watch?v=GVbPiq3Pet0); publication: 2025-02-08T21:31:25Z; analysis: `analysis/GVbPiq3Pet0.json`.
[^JRTAtZ5iBkU]: [HTML is All You Need (for Agents to Make Graphics) - Amol Kapoor, Nori](https://www.youtube.com/watch?v=JRTAtZ5iBkU); publication: 2026-06-28T18:30:30Z; analysis: `analysis/JRTAtZ5iBkU.json`.
[^KhRjivBSwiw]: [The Data Context Layer for Agents — Yoni Michael & Brandon Callender, Typedef](https://www.youtube.com/watch?v=KhRjivBSwiw); publication: 2026-10-11T12:30:23Z; analysis: `analysis/KhRjivBSwiw.json`.
[^LC3-P7v3yoI]: [Skills are the New SDKs - Elvin Aghammadzada, DataRobot](https://www.youtube.com/watch?v=LC3-P7v3yoI); publication: 2026-07-20T06:24:53Z; analysis: `analysis/LC3-P7v3yoI.json`.
[^M05vON8i0aI]: [AI-Native Organisations Run on Skills: How to Structure and Scale Them — Imad Touil, QuantumBlack](https://www.youtube.com/watch?v=M05vON8i0aI); publication: 2026-08-28T18:30:04Z; analysis: `analysis/M05vON8i0aI.json`.
[^MhHEGMFCEB0]: [OpenAI Codex Masterclass  — Vaibhav Srivastav & Katia Gil Guzman](https://www.youtube.com/watch?v=MhHEGMFCEB0); publication: 2026-04-29T16:00:06Z; analysis: `analysis/MhHEGMFCEB0.json`.
[^O84lhGc1OOI]: [If we want them to do Knowledge Work, design them as Knowledge Agents — Benjamin Clavié, Mixedbread](https://www.youtube.com/watch?v=O84lhGc1OOI); publication: 2026-09-16T15:00:39Z; analysis: `analysis/O84lhGc1OOI.json`.
[^RjfbvDXpFls]: [Building pi in a World of Slop — Mario Zechner](https://www.youtube.com/watch?v=RjfbvDXpFls); publication: 2026-04-16T22:58:06Z; analysis: `analysis/RjfbvDXpFls.json`.
[^XZ0boOjtbNo]: [AI Didn’t Kill the Web, It Moved in! — Olivier Leplus (AWS) & Yohan Lasorsa (Microsoft)](https://www.youtube.com/watch?v=XZ0boOjtbNo); publication: 2026-04-10T00:24:17Z; analysis: `analysis/XZ0boOjtbNo.json`.
[^YXiLj4tJt5A]: [Agent Speedrun — Elizabeth Fuentes Leone & Sandhya Subramani, AWS](https://www.youtube.com/watch?v=YXiLj4tJt5A); publication: 2026-10-11T15:00:05Z; analysis: `analysis/YXiLj4tJt5A.json`.
[^ZyC56eV8sVw]: [AI Security Engineer Foundations + Certificate — Javier Garza, Snyk](https://www.youtube.com/watch?v=ZyC56eV8sVw); publication: 2026-10-11T19:30:16Z; analysis: `analysis/ZyC56eV8sVw.json`.
[^_Zcw_sVF6hU]: [The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil](https://www.youtube.com/watch?v=_Zcw_sVF6hU); publication: 2026-04-18T10:30:06Z; analysis: `analysis/_Zcw_sVF6hU.json`.
[^aV_vgUSatqs]: [Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal](https://www.youtube.com/watch?v=aV_vgUSatqs); publication: 2026-10-11T20:30:04Z; analysis: `analysis/aV_vgUSatqs.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^cgimkNGNjvU]: [Agentic Development Security — Ezra Tanzer, Snyk](https://www.youtube.com/watch?v=cgimkNGNjvU); publication: 2026-07-20T17:17:53Z; analysis: `analysis/cgimkNGNjvU.json`.
[^i1uPAN6uW4s]: [Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments - Harald Kirshner,](https://www.youtube.com/watch?v=i1uPAN6uW4s); publication: 2025-06-27T10:15:59Z; analysis: `analysis/i1uPAN6uW4s.json`.
[^iKQ78wyJEXU]: [We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank](https://www.youtube.com/watch?v=iKQ78wyJEXU); publication: 2026-07-29T22:00:06Z; analysis: `analysis/iKQ78wyJEXU.json`.
[^jdeMJJ_oNYg]: [LLM Safeguards: Security Privacy Compliance Anti Hallucination: Daniel Whitenack](https://www.youtube.com/watch?v=jdeMJJ_oNYg); publication: 2024-12-31T17:28:40Z; analysis: `analysis/jdeMJJ_oNYg.json`.
[^p-2MT8KYZqU]: [AI Security Engineer Foundations + Certificate — Micah Silverman, Snyk](https://www.youtube.com/watch?v=p-2MT8KYZqU); publication: 2026-10-11T13:30:04Z; analysis: `analysis/p-2MT8KYZqU.json`.
[^sJ2jc7leKBk]: [I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)](https://www.youtube.com/watch?v=sJ2jc7leKBk); publication: 2026-05-02T22:00:06Z; analysis: `analysis/sJ2jc7leKBk.json`.
[^tHJSZ1-ZqcA]: [The Agent Awakens: Collaborative Development with Copilot - Christopher Harrison, GitHub](https://www.youtube.com/watch?v=tHJSZ1-ZqcA); publication: 2025-06-27T10:11:01Z; analysis: `analysis/tHJSZ1-ZqcA.json`.
[^u-o0sW9nwmk]: [From 36% to 100%: How Self-Improving Agents Write Their Own Skills — Rafal Wilinski, Runlayer](https://www.youtube.com/watch?v=u-o0sW9nwmk); publication: 2026-10-07T14:00:10Z; analysis: `analysis/u-o0sW9nwmk.json`.
[^utTqdQpe39A]: [GitHub's AI Powered Security Platform: Sarah Khalife](https://www.youtube.com/watch?v=utTqdQpe39A); publication: 2025-02-08T21:31:24Z; analysis: `analysis/utTqdQpe39A.json`.
[^w7IMuYsBNr8]: [OpenAI on Securing Code-Executing AI Agents — Fouad Matin (Codex, Agent Robustness)](https://www.youtube.com/watch?v=w7IMuYsBNr8); publication: 2025-07-30T15:00:06Z; analysis: `analysis/w7IMuYsBNr8.json`.
[^x4e5O9zN0TE]: [Long-Horizon Agents Need Experiments, Not Just Prompts — Erina Karati](https://www.youtube.com/watch?v=x4e5O9zN0TE); publication: 2026-09-26T16:30:29Z; analysis: `analysis/x4e5O9zN0TE.json`.
[^yWS0udrIOc8]: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain — Steve Yegge, Gas Town](https://www.youtube.com/watch?v=yWS0udrIOc8); publication: 2026-07-20T17:17:53Z; analysis: `analysis/yWS0udrIOc8.json`.
