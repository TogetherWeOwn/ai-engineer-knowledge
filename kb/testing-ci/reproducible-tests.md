---
{
  "type": "technique",
  "id": "reproducible-tests",
  "title": "Pin test inputs, dependencies and environments for reproducible replay",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-21T19:01:02Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "42Bz0TUfeOQ",
      "resource": "https://www.youtube.com/watch?v=42Bz0TUfeOQ",
      "title": "The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize",
      "author": "Debugging Voice Agents, Arize",
      "last_modified": "2026-10-05T21:30:33Z",
      "analysis_file": "analysis/42Bz0TUfeOQ.json"
    },
    {
      "id": "5Bn0xro2ol8",
      "resource": "https://www.youtube.com/watch?v=5Bn0xro2ol8",
      "title": "How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma",
      "author": "Eyal Blum, Figma",
      "last_modified": "2026-08-28T17:00:33Z",
      "analysis_file": "analysis/5Bn0xro2ol8.json"
    },
    {
      "id": "CTLa_p6iOiY",
      "resource": "https://www.youtube.com/watch?v=CTLa_p6iOiY",
      "title": "Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs",
      "author": "Pierluca D'Oro, Programma Labs",
      "last_modified": "2026-08-14T14:30:31Z",
      "analysis_file": "analysis/CTLa_p6iOiY.json"
    },
    {
      "id": "Cz4v1WHVyZc",
      "resource": "https://www.youtube.com/watch?v=Cz4v1WHVyZc",
      "title": "HTML Is All Agents Need — James Russo, HeyGen",
      "author": "James Russo, HeyGen",
      "last_modified": "2026-07-21T18:54:01Z",
      "analysis_file": "analysis/Cz4v1WHVyZc.json"
    },
    {
      "id": "Dc3qOA9WOnE",
      "resource": "https://www.youtube.com/watch?v=Dc3qOA9WOnE",
      "title": "Vibes won't cut it — Chris Kelly, Augment Code",
      "author": "Chris Kelly, Augment Code",
      "last_modified": "2025-08-03T04:32:17Z",
      "analysis_file": "analysis/Dc3qOA9WOnE.json"
    },
    {
      "id": "DqtmZE6Hl0g",
      "resource": "https://www.youtube.com/watch?v=DqtmZE6Hl0g",
      "title": "The Prompt is the Platform - Dominik Tornow, Resonate HQ",
      "author": "Dominik Tornow, Resonate HQ",
      "last_modified": "2026-06-29T01:00:36Z",
      "analysis_file": "analysis/DqtmZE6Hl0g.json"
    },
    {
      "id": "GqoNrUz8hEU",
      "resource": "https://www.youtube.com/watch?v=GqoNrUz8hEU",
      "title": "Bringing agents onto the world wide web — Paul Klein IV, Browserbase",
      "author": "Paul Klein IV, Browserbase",
      "last_modified": "2026-08-14T15:00:31Z",
      "analysis_file": "analysis/GqoNrUz8hEU.json"
    },
    {
      "id": "H7vFrcNWXzs",
      "resource": "https://www.youtube.com/watch?v=H7vFrcNWXzs",
      "title": "Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition",
      "author": "Jonathan Kelley, Dioxus Labs & Cognition",
      "last_modified": "2026-09-11T20:00:06Z",
      "analysis_file": "analysis/H7vFrcNWXzs.json"
    },
    {
      "id": "HLTa7Vcs4X0",
      "resource": "https://www.youtube.com/watch?v=HLTa7Vcs4X0",
      "title": "Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous",
      "author": "Gabriel Spencer-Harper, Meticulous",
      "last_modified": "2026-10-02T21:30:22Z",
      "analysis_file": "analysis/HLTa7Vcs4X0.json"
    },
    {
      "id": "I8fs4omN1no",
      "resource": "https://www.youtube.com/watch?v=I8fs4omN1no",
      "title": "Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline",
      "author": "Nik Pash, Cline",
      "last_modified": "2025-12-12T15:00:06Z",
      "analysis_file": "analysis/I8fs4omN1no.json"
    },
    {
      "id": "KMR_RBoCa4M",
      "resource": "https://www.youtube.com/watch?v=KMR_RBoCa4M",
      "title": "SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)",
      "author": "Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)",
      "last_modified": "2026-07-29T19:00:06Z",
      "analysis_file": "analysis/KMR_RBoCa4M.json"
    },
    {
      "id": "L8OoYeDI_ls",
      "resource": "https://www.youtube.com/watch?v=L8OoYeDI_ls",
      "title": "Evals Are Not Unit Tests — Ido Pesok, Vercel v0",
      "author": "Ido Pesok, Vercel v0",
      "last_modified": "2025-08-06T16:14:42Z",
      "analysis_file": "analysis/L8OoYeDI_ls.json"
    },
    {
      "id": "Lc8zRh9muoY",
      "resource": "https://www.youtube.com/watch?v=Lc8zRh9muoY",
      "title": "Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft",
      "author": "Tisha Chawla & Susheem Koul, Microsoft",
      "last_modified": "2026-06-29T00:00:39Z",
      "analysis_file": "analysis/Lc8zRh9muoY.json"
    },
    {
      "id": "O-CBZ3JtRvo",
      "resource": "https://www.youtube.com/watch?v=O-CBZ3JtRvo",
      "title": "Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face",
      "author": "Uri Rolls, Arithmetic & Thom Wolf, Hugging Face",
      "last_modified": "2026-07-24T05:19:15Z",
      "analysis_file": "analysis/O-CBZ3JtRvo.json"
    },
    {
      "id": "ON5LIT0M4do",
      "resource": "https://www.youtube.com/watch?v=ON5LIT0M4do",
      "title": "Feedback Loops are All You Need — Mehedi Hassan, Granola",
      "author": "Mehedi Hassan, Granola",
      "last_modified": "2026-05-10T18:00:06Z",
      "analysis_file": "analysis/ON5LIT0M4do.json"
    },
    {
      "id": "Rx8f05JI_WA",
      "resource": "https://www.youtube.com/watch?v=Rx8f05JI_WA",
      "title": "SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI",
      "author": "Rishi Desai, Abundant AI",
      "last_modified": "2026-07-07T03:45:51Z",
      "analysis_file": "analysis/Rx8f05JI_WA.json"
    },
    {
      "id": "SQMCtZX3trg",
      "resource": "https://www.youtube.com/watch?v=SQMCtZX3trg",
      "title": "The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)",
      "author": "Paul Bakaus, Renaissance Geek (Impeccable)",
      "last_modified": "2026-09-21T19:00:10Z",
      "analysis_file": "analysis/SQMCtZX3trg.json"
    },
    {
      "id": "SbcQYbrvAfI",
      "resource": "https://www.youtube.com/watch?v=SbcQYbrvAfI",
      "title": "Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize",
      "author": "SallyAnn DeLucia & Fuad Ali, Arize",
      "last_modified": "2026-01-06T17:30:06Z",
      "analysis_file": "analysis/SbcQYbrvAfI.json"
    },
    {
      "id": "Uv0nAf_7tyU",
      "resource": "https://www.youtube.com/watch?v=Uv0nAf_7tyU",
      "title": "Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic",
      "author": "Anthropic",
      "last_modified": "2026-10-12T05:44:00Z",
      "analysis_file": "analysis/Uv0nAf_7tyU.json"
    },
    {
      "id": "X6NShR2ccOg",
      "resource": "https://www.youtube.com/watch?v=X6NShR2ccOg",
      "title": "Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML",
      "author": "Alessandro Cappelli, Adaptive ML",
      "last_modified": "2026-05-12T17:00:06Z",
      "analysis_file": "analysis/X6NShR2ccOg.json"
    },
    {
      "id": "Yk87oUPVaxU",
      "resource": "https://www.youtube.com/watch?v=Yk87oUPVaxU",
      "title": "DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve",
      "author": "James Shi, Datacurve",
      "last_modified": "2026-07-26T18:10:56Z",
      "analysis_file": "analysis/Yk87oUPVaxU.json"
    },
    {
      "id": "ZFxh7sqbUZo",
      "resource": "https://www.youtube.com/watch?v=ZFxh7sqbUZo",
      "title": "Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd",
      "author": "Prof. David Brumley, Bugcrowd",
      "last_modified": "2026-08-01T00:30:06Z",
      "analysis_file": "analysis/ZFxh7sqbUZo.json"
    },
    {
      "id": "ZdheJTfLu-s",
      "resource": "https://www.youtube.com/watch?v=ZdheJTfLu-s",
      "title": "Shipping complex AI applications — Braintrust & Trainline",
      "author": "Braintrust & Trainline",
      "last_modified": "2026-05-01T14:00:06Z",
      "analysis_file": "analysis/ZdheJTfLu-s.json"
    },
    {
      "id": "_IzZWeuTx7I",
      "resource": "https://www.youtube.com/watch?v=_IzZWeuTx7I",
      "title": "RL Environments at Scale – Will Brown, Prime Intellect",
      "author": "Will Brown, Prime Intellect",
      "last_modified": "2025-12-09T15:53:42Z",
      "analysis_file": "analysis/_IzZWeuTx7I.json"
    },
    {
      "id": "bU5gDVyu_28",
      "resource": "https://www.youtube.com/watch?v=bU5gDVyu_28",
      "title": "Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One",
      "author": "Max Kanat-Alexander, Capital One",
      "last_modified": "2026-10-21T19:01:02Z",
      "analysis_file": "analysis/bU5gDVyu_28.json"
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
      "id": "bZISsg7H7DA",
      "resource": "https://www.youtube.com/watch?v=bZISsg7H7DA",
      "title": "Your Agents Need a Save Button - Hamza Tahir, ZenML",
      "author": "Hamza Tahir, ZenML",
      "last_modified": "2026-07-18T07:00:06Z",
      "analysis_file": "analysis/bZISsg7H7DA.json"
    },
    {
      "id": "d5EltXhbcfA",
      "resource": "https://www.youtube.com/watch?v=d5EltXhbcfA",
      "title": "Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil",
      "author": "Sayash Kapoor, AI Snake Oil",
      "last_modified": "2025-04-17T16:00:06Z",
      "analysis_file": "analysis/d5EltXhbcfA.json"
    },
    {
      "id": "exiwa9QbQXI",
      "resource": "https://www.youtube.com/watch?v=exiwa9QbQXI",
      "title": "The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory",
      "author": "Davis Palmie, Factory",
      "last_modified": "2026-10-07T20:00:04Z",
      "analysis_file": "analysis/exiwa9QbQXI.json"
    },
    {
      "id": "fiXjTif1nS4",
      "resource": "https://www.youtube.com/watch?v=fiXjTif1nS4",
      "title": "Best Practices for Evaluating Large Language Model Applications with llmeval: Niklas Nielsen",
      "author": null,
      "last_modified": "2025-02-05T11:18:34Z",
      "analysis_file": "analysis/fiXjTif1nS4.json"
    },
    {
      "id": "flf_IKnFYnE",
      "resource": "https://www.youtube.com/watch?v=flf_IKnFYnE",
      "title": "From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic",
      "author": "Samuel Colvin, Pydantic",
      "last_modified": "2025-11-24T20:16:36Z",
      "analysis_file": "analysis/flf_IKnFYnE.json"
    },
    {
      "id": "imFedndyXYQ",
      "resource": "https://www.youtube.com/watch?v=imFedndyXYQ",
      "title": "Using LLMs to Secure Source Code — Eugene Yan, Anthropic",
      "author": "Eugene Yan, Anthropic",
      "last_modified": "2026-07-17T21:27:20Z",
      "analysis_file": "analysis/imFedndyXYQ.json"
    },
    {
      "id": "k72eLcYpVys",
      "resource": "https://www.youtube.com/watch?v=k72eLcYpVys",
      "title": "1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS",
      "author": "Kevin Orellana, AWS",
      "last_modified": "2026-10-12T05:36:31Z",
      "analysis_file": "analysis/k72eLcYpVys.json"
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
      "id": "kmV-qg4uoNI",
      "resource": "https://www.youtube.com/watch?v=kmV-qg4uoNI",
      "title": "Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel",
      "author": "Peter Wielander, Vercel",
      "last_modified": "2026-01-06T16:00:07Z",
      "analysis_file": "analysis/kmV-qg4uoNI.json"
    },
    {
      "id": "l0FLhNqBOic",
      "resource": "https://www.youtube.com/watch?v=l0FLhNqBOic",
      "title": "AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents",
      "author": "Vasuman Moza, Varick Agents",
      "last_modified": "2026-07-28T21:00:06Z",
      "analysis_file": "analysis/l0FLhNqBOic.json"
    },
    {
      "id": "l1-D89bAuOA",
      "resource": "https://www.youtube.com/watch?v=l1-D89bAuOA",
      "title": "Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google",
      "author": "Ashok Chandrasekar & Jason Kramberger, Google",
      "last_modified": "2026-09-19T16:00:07Z",
      "analysis_file": "analysis/l1-D89bAuOA.json"
    },
    {
      "id": "mav15aW9lLM",
      "resource": "https://www.youtube.com/watch?v=mav15aW9lLM",
      "title": "Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard",
      "author": "Christopher Lovejoy & Saul Howard",
      "last_modified": "2026-08-19T18:30:15Z",
      "analysis_file": "analysis/mav15aW9lLM.json"
    },
    {
      "id": "qStB9GbppMU",
      "resource": "https://www.youtube.com/watch?v=qStB9GbppMU",
      "title": "1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI",
      "author": "Sumanyu Sharma, Hamming AI",
      "last_modified": "2026-09-15T15:00:06Z",
      "analysis_file": "analysis/qStB9GbppMU.json"
    },
    {
      "id": "qZj7sqmidqA",
      "resource": "https://www.youtube.com/watch?v=qZj7sqmidqA",
      "title": "From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI",
      "author": "Laurie Voss, Arize AI",
      "last_modified": "2026-10-05T22:00:36Z",
      "analysis_file": "analysis/qZj7sqmidqA.json"
    },
    {
      "id": "qqXdLf3wy1E",
      "resource": "https://www.youtube.com/watch?v=qqXdLf3wy1E",
      "title": "Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant",
      "author": "Jesse Hu, Abundant",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qqXdLf3wy1E.json"
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
      "id": "sn79oS4MZFI",
      "resource": "https://www.youtube.com/watch?v=sn79oS4MZFI",
      "title": "Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason",
      "author": "Dan Mason",
      "last_modified": "2025-06-22T16:00:06Z",
      "analysis_file": "analysis/sn79oS4MZFI.json"
    },
    {
      "id": "tHN44yJoeS8",
      "resource": "https://www.youtube.com/watch?v=tHN44yJoeS8",
      "title": "Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor",
      "author": "Naman Jain, Cursor",
      "last_modified": "2025-12-15T17:18:09Z",
      "analysis_file": "analysis/tHN44yJoeS8.json"
    },
    {
      "id": "y2Drx0SDZLo",
      "resource": "https://www.youtube.com/watch?v=y2Drx0SDZLo",
      "title": "Agent Evals: Finally, With The Map",
      "author": null,
      "last_modified": "2025-02-22T19:00:31Z",
      "analysis_file": "analysis/y2Drx0SDZLo.json"
    },
    {
      "id": "yUmS-F9IX90",
      "resource": "https://www.youtube.com/watch?v=yUmS-F9IX90",
      "title": "Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline",
      "author": "Ara Khan, Cline",
      "last_modified": "2026-05-19T15:00:06Z",
      "analysis_file": "analysis/yUmS-F9IX90.json"
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

# Pin test inputs, dependencies and environments for reproducible replay

## What

Pin test inputs, dependencies and environments for reproducible replay

A repeatable environment prevents hidden machine state from turning an agent task into setup debugging.

## Evidence

Source analysis [^42Bz0TUfeOQ]; no independently matched timestamped quote published.

Source analysis [^5Bn0xro2ol8]; no independently matched timestamped quote published.

Source analysis [^CTLa_p6iOiY]; no independently matched timestamped quote published.

Source analysis [^Cz4v1WHVyZc]; no independently matched timestamped quote published.

Source analysis [^Dc3qOA9WOnE]; no independently matched timestamped quote published.

Source analysis [^DqtmZE6Hl0g]; no independently matched timestamped quote published.

Source analysis [^GqoNrUz8hEU]; no independently matched timestamped quote published.

Source analysis [^H7vFrcNWXzs]; no independently matched timestamped quote published.

Source analysis [^HLTa7Vcs4X0]; no independently matched timestamped quote published.

Source analysis [^I8fs4omN1no]; no independently matched timestamped quote published.

Source analysis [^KMR_RBoCa4M]; no independently matched timestamped quote published.

> 5% that can fail on us. So let's improve it.
> — 04:47 [^L8OoYeDI_ls]

> to draw a very clear distinction here. There are two ways of testing AI agents,
> — 12:18 [^Lc8zRh9muoY]

Source analysis [^O-CBZ3JtRvo]; no independently matched timestamped quote published.

Source analysis [^ON5LIT0M4do]; no independently matched timestamped quote published.

> reference solutions. And then we work together to standardize them into
> — 05:38 [^Rx8f05JI_WA]

Source analysis [^SQMCtZX3trg]; no independently matched timestamped quote published.

Source analysis [^SbcQYbrvAfI]; no independently matched timestamped quote published.

> restrict it to specific domains or MCPS? you can define what packages you want
> — 14:21 [^Uv0nAf_7tyU]

Source analysis [^X6NShR2ccOg]; no independently matched timestamped quote published.

Source analysis [^Yk87oUPVaxU]; no independently matched timestamped quote published.

Source analysis [^ZFxh7sqbUZo]; no independently matched timestamped quote published.

Source analysis [^ZdheJTfLu-s]; no independently matched timestamped quote published.

Source analysis [^_IzZWeuTx7I]; no independently matched timestamped quote published.

Source analysis [^bU5gDVyu_28]; no independently matched timestamped quote published.

Source analysis [^bVNNvWq6dKo]; no independently matched timestamped quote published.

> lookup policy. And I'm mocking it with another function
> — 08:13 [^bZISsg7H7DA]

> providing the agent with the code and the data needed to reproduce it so as
> — 05:01 [^d5EltXhbcfA]

> thinking about agents these agents need to take actions in the real world they
> — 07:50 [^d5EltXhbcfA]

Source analysis [^exiwa9QbQXI]; no independently matched timestamped quote published.

Source analysis [^fiXjTif1nS4]; no independently matched timestamped quote published.

Source analysis [^flf_IKnFYnE]; no independently matched timestamped quote published.

Source analysis [^imFedndyXYQ]; no independently matched timestamped quote published.

> might not match what you have in a remote sandbox.
> — 12:34 [^k72eLcYpVys]

> following our research process. And so, having these good rubrics that become
> — 18:25 [^kiqubc5b5Yo]

> deterministic. So it can be rerun um in a in a uh deterministic fashion and
> — 12:33 [^kmV-qg4uoNI]

Source analysis [^l0FLhNqBOic]; no independently matched timestamped quote published.

Source analysis [^l1-D89bAuOA]; no independently matched timestamped quote published.

Source analysis [^mav15aW9lLM]; no independently matched timestamped quote published.

Source analysis [^qStB9GbppMU]; no independently matched timestamped quote published.

> task could be some subcomponent of what your agent did. So if we were running an
> — 1:36:03 [^qZj7sqmidqA]

Source analysis [^qqXdLf3wy1E]; no independently matched timestamped quote published.

> start cursor dev tool frontend start um and that is abstracting everything away
> — 51:43 [^rnDm57Py54A]

> handle time or I have to replace all the time stamps. Um, we ended up sort of
> — 1:36:07 [^sn79oS4MZFI]

> drastic models would sometimes completely hijack the infra where uh
> — 10:59 [^tHN44yJoeS8]

> keep in mind is the offline versus online testing so what are the things
> — 09:06 [^y2Drx0SDZLo]

> that can actually be just measured separately uh using more traditional
> — 10:16 [^y2Drx0SDZLo]

> common set up that like so many other people can share and so many people can
> — 15:41 [^yUmS-F9IX90]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^42Bz0TUfeOQ]: [The Transcript Looked Fine. The Call Wasn't. — Debugging Voice Agents, Arize](https://www.youtube.com/watch?v=42Bz0TUfeOQ); publication: 2026-10-05T21:30:33Z; analysis: `analysis/42Bz0TUfeOQ.json`.
[^5Bn0xro2ol8]: [How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) — Eyal Blum, Figma](https://www.youtube.com/watch?v=5Bn0xro2ol8); publication: 2026-08-28T17:00:33Z; analysis: `analysis/5Bn0xro2ol8.json`.
[^CTLa_p6iOiY]: [Computer Use at the Edge of the Statistical Precipice — Pierluca D'Oro, Programma Labs](https://www.youtube.com/watch?v=CTLa_p6iOiY); publication: 2026-08-14T14:30:31Z; analysis: `analysis/CTLa_p6iOiY.json`.
[^Cz4v1WHVyZc]: [HTML Is All Agents Need — James Russo, HeyGen](https://www.youtube.com/watch?v=Cz4v1WHVyZc); publication: 2026-07-21T18:54:01Z; analysis: `analysis/Cz4v1WHVyZc.json`.
[^Dc3qOA9WOnE]: [Vibes won't cut it — Chris Kelly, Augment Code](https://www.youtube.com/watch?v=Dc3qOA9WOnE); publication: 2025-08-03T04:32:17Z; analysis: `analysis/Dc3qOA9WOnE.json`.
[^DqtmZE6Hl0g]: [The Prompt is the Platform - Dominik Tornow, Resonate HQ](https://www.youtube.com/watch?v=DqtmZE6Hl0g); publication: 2026-06-29T01:00:36Z; analysis: `analysis/DqtmZE6Hl0g.json`.
[^GqoNrUz8hEU]: [Bringing agents onto the world wide web — Paul Klein IV, Browserbase](https://www.youtube.com/watch?v=GqoNrUz8hEU); publication: 2026-08-14T15:00:31Z; analysis: `analysis/GqoNrUz8hEU.json`.
[^H7vFrcNWXzs]: [Building ambitious software — Jonathan Kelley, Dioxus Labs & Cognition](https://www.youtube.com/watch?v=H7vFrcNWXzs); publication: 2026-09-11T20:00:06Z; analysis: `analysis/H7vFrcNWXzs.json`.
[^HLTa7Vcs4X0]: [Why AI Didn't Actually Make You Ship Faster — Gabriel Spencer-Harper, Meticulous](https://www.youtube.com/watch?v=HLTa7Vcs4X0); publication: 2026-10-02T21:30:22Z; analysis: `analysis/HLTa7Vcs4X0.json`.
[^I8fs4omN1no]: [Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline](https://www.youtube.com/watch?v=I8fs4omN1no); publication: 2025-12-12T15:00:06Z; analysis: `analysis/I8fs4omN1no.json`.
[^KMR_RBoCa4M]: [SimulationMaxxing: How we ship agents 20× faster — Aman Gupta (Nubank) + Shreya Rajpal (Snowglobe)](https://www.youtube.com/watch?v=KMR_RBoCa4M); publication: 2026-07-29T19:00:06Z; analysis: `analysis/KMR_RBoCa4M.json`.
[^L8OoYeDI_ls]: [Evals Are Not Unit Tests — Ido Pesok, Vercel v0](https://www.youtube.com/watch?v=L8OoYeDI_ls); publication: 2025-08-06T16:14:42Z; analysis: `analysis/L8OoYeDI_ls.json`.
[^Lc8zRh9muoY]: [Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft](https://www.youtube.com/watch?v=Lc8zRh9muoY); publication: 2026-06-29T00:00:39Z; analysis: `analysis/Lc8zRh9muoY.json`.
[^O-CBZ3JtRvo]: [Training Frontier Models to Out-Think Hackers — Uri Rolls, Arithmetic & Thom Wolf, Hugging Face](https://www.youtube.com/watch?v=O-CBZ3JtRvo); publication: 2026-07-24T05:19:15Z; analysis: `analysis/O-CBZ3JtRvo.json`.
[^ON5LIT0M4do]: [Feedback Loops are All You Need — Mehedi Hassan, Granola](https://www.youtube.com/watch?v=ON5LIT0M4do); publication: 2026-05-10T18:00:06Z; analysis: `analysis/ON5LIT0M4do.json`.
[^Rx8f05JI_WA]: [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale - Rishi Desai, Abundant AI](https://www.youtube.com/watch?v=Rx8f05JI_WA); publication: 2026-07-07T03:45:51Z; analysis: `analysis/Rx8f05JI_WA.json`.
[^SQMCtZX3trg]: [The Dark Arts of Skill Engineering — Paul Bakaus, Renaissance Geek (Impeccable)](https://www.youtube.com/watch?v=SQMCtZX3trg); publication: 2026-09-21T19:00:10Z; analysis: `analysis/SQMCtZX3trg.json`.
[^SbcQYbrvAfI]: [Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize](https://www.youtube.com/watch?v=SbcQYbrvAfI); publication: 2026-01-06T17:30:06Z; analysis: `analysis/SbcQYbrvAfI.json`.
[^Uv0nAf_7tyU]: [Decoupling the Brain from the Hands: Claude Managed Agents (Part 1 of 4) — Anthropic](https://www.youtube.com/watch?v=Uv0nAf_7tyU); publication: 2026-10-12T05:44:00Z; analysis: `analysis/Uv0nAf_7tyU.json`.
[^X6NShR2ccOg]: [Lessons from Trillion Token Deployments at Fortune 500s — Alessandro Cappelli, Adaptive ML](https://www.youtube.com/watch?v=X6NShR2ccOg); publication: 2026-05-12T17:00:06Z; analysis: `analysis/X6NShR2ccOg.json`.
[^Yk87oUPVaxU]: [DeepSWE: A Contamination-Resistant Coding Benchmark — James Shi, Datacurve](https://www.youtube.com/watch?v=Yk87oUPVaxU); publication: 2026-07-26T18:10:56Z; analysis: `analysis/Yk87oUPVaxU.json`.
[^ZFxh7sqbUZo]: [Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd](https://www.youtube.com/watch?v=ZFxh7sqbUZo); publication: 2026-08-01T00:30:06Z; analysis: `analysis/ZFxh7sqbUZo.json`.
[^ZdheJTfLu-s]: [Shipping complex AI applications — Braintrust & Trainline](https://www.youtube.com/watch?v=ZdheJTfLu-s); publication: 2026-05-01T14:00:06Z; analysis: `analysis/ZdheJTfLu-s.json`.
[^_IzZWeuTx7I]: [RL Environments at Scale – Will Brown, Prime Intellect](https://www.youtube.com/watch?v=_IzZWeuTx7I); publication: 2025-12-09T15:53:42Z; analysis: `analysis/_IzZWeuTx7I.json`.
[^bU5gDVyu_28]: [Does Code Quality Still Matter? It Depends on This — Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=bU5gDVyu_28); publication: 2026-10-21T19:01:02Z; analysis: `analysis/bU5gDVyu_28.json`.
[^bVNNvWq6dKo]: [How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=bVNNvWq6dKo); publication: 2025-03-11T19:17:46Z; analysis: `analysis/bVNNvWq6dKo.json`.
[^bZISsg7H7DA]: [Your Agents Need a Save Button - Hamza Tahir, ZenML](https://www.youtube.com/watch?v=bZISsg7H7DA); publication: 2026-07-18T07:00:06Z; analysis: `analysis/bZISsg7H7DA.json`.
[^d5EltXhbcfA]: [Building and evaluating AI Agents — Sayash Kapoor, AI Snake Oil](https://www.youtube.com/watch?v=d5EltXhbcfA); publication: 2025-04-17T16:00:06Z; analysis: `analysis/d5EltXhbcfA.json`.
[^exiwa9QbQXI]: [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](https://www.youtube.com/watch?v=exiwa9QbQXI); publication: 2026-10-07T20:00:04Z; analysis: `analysis/exiwa9QbQXI.json`.
[^fiXjTif1nS4]: [Best Practices for Evaluating Large Language Model Applications with llmeval: Niklas Nielsen](https://www.youtube.com/watch?v=fiXjTif1nS4); publication: 2025-02-05T11:18:34Z; analysis: `analysis/fiXjTif1nS4.json`.
[^flf_IKnFYnE]: [From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic](https://www.youtube.com/watch?v=flf_IKnFYnE); publication: 2025-11-24T20:16:36Z; analysis: `analysis/flf_IKnFYnE.json`.
[^imFedndyXYQ]: [Using LLMs to Secure Source Code — Eugene Yan, Anthropic](https://www.youtube.com/watch?v=imFedndyXYQ); publication: 2026-07-17T21:27:20Z; analysis: `analysis/imFedndyXYQ.json`.
[^k72eLcYpVys]: [1,000 Agent Tasks in a Sandbox: What Breaks When LLMs Run Code — Kevin Orellana, AWS](https://www.youtube.com/watch?v=k72eLcYpVys); publication: 2026-10-12T05:36:31Z; analysis: `analysis/k72eLcYpVys.json`.
[^kiqubc5b5Yo]: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo); publication: 2026-07-29T17:06:26Z; analysis: `analysis/kiqubc5b5Yo.json`.
[^kmV-qg4uoNI]: [Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel](https://www.youtube.com/watch?v=kmV-qg4uoNI); publication: 2026-01-06T16:00:07Z; analysis: `analysis/kmV-qg4uoNI.json`.
[^l0FLhNqBOic]: [AI tools for Forward Deployed Engineering — Vasuman Moza, Varick Agents](https://www.youtube.com/watch?v=l0FLhNqBOic); publication: 2026-07-28T21:00:06Z; analysis: `analysis/l0FLhNqBOic.json`.
[^l1-D89bAuOA]: [Are LLM Performance Benchmarks Reliable? — Ashok Chandrasekar & Jason Kramberger, Google](https://www.youtube.com/watch?v=l1-D89bAuOA); publication: 2026-09-19T16:00:07Z; analysis: `analysis/l1-D89bAuOA.json`.
[^mav15aW9lLM]: [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](https://www.youtube.com/watch?v=mav15aW9lLM); publication: 2026-08-19T18:30:15Z; analysis: `analysis/mav15aW9lLM.json`.
[^qStB9GbppMU]: [1 Trillion Phone Calls/yr, 10% Error rate: The Crisis in Voice AI — Sumanyu Sharma, Hamming AI](https://www.youtube.com/watch?v=qStB9GbppMU); publication: 2026-09-15T15:00:06Z; analysis: `analysis/qStB9GbppMU.json`.
[^qZj7sqmidqA]: [From Vibes to Production: Evaluating and Shipping AI Agents That Work 101 — Laurie Voss, Arize AI](https://www.youtube.com/watch?v=qZj7sqmidqA); publication: 2026-10-05T22:00:36Z; analysis: `analysis/qZj7sqmidqA.json`.
[^qqXdLf3wy1E]: [Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant](https://www.youtube.com/watch?v=qqXdLf3wy1E); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qqXdLf3wy1E.json`.
[^rnDm57Py54A]: [Building your own software factory — Eric Zakariasson, Cursor](https://www.youtube.com/watch?v=rnDm57Py54A); publication: 2026-04-28T18:00:06Z; analysis: `analysis/rnDm57Py54A.json`.
[^sn79oS4MZFI]: [Case Study + Deep Dive: Telemedicine Support Agents with LangGraph/MCP - Dan Mason](https://www.youtube.com/watch?v=sn79oS4MZFI); publication: 2025-06-22T16:00:06Z; analysis: `analysis/sn79oS4MZFI.json`.
[^tHN44yJoeS8]: [Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor](https://www.youtube.com/watch?v=tHN44yJoeS8); publication: 2025-12-15T17:18:09Z; analysis: `analysis/tHN44yJoeS8.json`.
[^y2Drx0SDZLo]: [Agent Evals: Finally, With The Map](https://www.youtube.com/watch?v=y2Drx0SDZLo); publication: 2025-02-22T19:00:31Z; analysis: `analysis/y2Drx0SDZLo.json`.
[^yUmS-F9IX90]: [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](https://www.youtube.com/watch?v=yUmS-F9IX90); publication: 2026-05-19T15:00:06Z; analysis: `analysis/yUmS-F9IX90.json`.
