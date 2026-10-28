---
{
  "type": "technique",
  "id": "acceptance-specification",
  "title": "Define behavior and acceptance criteria before delegating",
  "area": "planning-work-supply",
  "status": "stable",
  "valid_from": "2026-10-20T23:00:22Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "-CnA2lGfymY",
      "resource": "https://www.youtube.com/watch?v=-CnA2lGfymY",
      "title": "\"I've never seen anything scarier than an LLM with tool calls.\" — Erik Meijer aka @HeadinTheBox",
      "author": "Erik Meijer aka @HeadinTheBox",
      "last_modified": "2026-07-13T19:25:09Z",
      "analysis_file": "analysis/-CnA2lGfymY.json"
    },
    {
      "id": "-npY6XjM8CQ",
      "resource": "https://www.youtube.com/watch?v=-npY6XjM8CQ",
      "title": "When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI",
      "author": "Nick Heiner, Surge AI",
      "last_modified": "2026-08-02T16:30:06Z",
      "analysis_file": "analysis/-npY6XjM8CQ.json"
    },
    {
      "id": "0I07YAuF8xA",
      "resource": "https://www.youtube.com/watch?v=0I07YAuF8xA",
      "title": "From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto",
      "author": "Adit Abraham, Reducto",
      "last_modified": "2026-09-23T14:30:11Z",
      "analysis_file": "analysis/0I07YAuF8xA.json"
    },
    {
      "id": "0ML7ZLMdcl4",
      "resource": "https://www.youtube.com/watch?v=0ML7ZLMdcl4",
      "title": "AI Engineering at Jane Street - John Crepezzi",
      "author": "John Crepezzi",
      "last_modified": "2025-03-28T15:04:44Z",
      "analysis_file": "analysis/0ML7ZLMdcl4.json"
    },
    {
      "id": "1P1hJ36rxM0",
      "resource": "https://www.youtube.com/watch?v=1P1hJ36rxM0",
      "title": "\"Software engineering is not about writing code\" — Benoit Schillings, Google DeepMind VP of Research",
      "author": "Benoit Schillings, Google DeepMind VP of Research",
      "last_modified": "2026-07-17T15:24:44Z",
      "analysis_file": "analysis/1P1hJ36rxM0.json"
    },
    {
      "id": "1nOTQsfe1RU",
      "resource": "https://www.youtube.com/watch?v=1nOTQsfe1RU",
      "title": "\"Data readiness\" is a Myth: Reliable AI with an Agentic Semantic Layer — Anushrut Gupta, PromptQL",
      "author": "Anushrut Gupta, PromptQL",
      "last_modified": "2025-06-27T09:40:39Z",
      "analysis_file": "analysis/1nOTQsfe1RU.json"
    },
    {
      "id": "3axY1wz2OvA",
      "resource": "https://www.youtube.com/watch?v=3axY1wz2OvA",
      "title": "Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis",
      "author": "Oliver Kennon, SemiAnalysis",
      "last_modified": "2026-10-20T23:00:22Z",
      "analysis_file": "analysis/3axY1wz2OvA.json"
    },
    {
      "id": "3hXJI2q0Jz8",
      "resource": "https://www.youtube.com/watch?v=3hXJI2q0Jz8",
      "title": "Recursive Coding Agents - Raymond Weitekamp, OpenProse",
      "author": "Raymond Weitekamp, OpenProse",
      "last_modified": "2026-06-25T21:00:06Z",
      "analysis_file": "analysis/3hXJI2q0Jz8.json"
    },
    {
      "id": "6NIr_cYPglk",
      "resource": "https://www.youtube.com/watch?v=6NIr_cYPglk",
      "title": "To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball",
      "author": "Forrest Brazeal, Matt Ball",
      "last_modified": "2025-06-27T10:46:59Z",
      "analysis_file": "analysis/6NIr_cYPglk.json"
    },
    {
      "id": "6bmM45jkMDY",
      "resource": "https://www.youtube.com/watch?v=6bmM45jkMDY",
      "title": "You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs",
      "author": "Balázs Horváth, VisualLabs",
      "last_modified": "2026-06-29T02:30:20Z",
      "analysis_file": "analysis/6bmM45jkMDY.json"
    },
    {
      "id": "7GMKdpLsxwU",
      "resource": "https://www.youtube.com/watch?v=7GMKdpLsxwU",
      "title": "The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI",
      "author": "Hassan El Mghari, Together AI",
      "last_modified": "2026-08-21T15:00:06Z",
      "analysis_file": "analysis/7GMKdpLsxwU.json"
    },
    {
      "id": "7vn4WpqNpck",
      "resource": "https://www.youtube.com/watch?v=7vn4WpqNpck",
      "title": "Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs",
      "author": "Denys Linkov, Wisedocs",
      "last_modified": "2026-08-08T19:00:06Z",
      "analysis_file": "analysis/7vn4WpqNpck.json"
    },
    {
      "id": "7wu2hsRfvV0",
      "resource": "https://www.youtube.com/watch?v=7wu2hsRfvV0",
      "title": "How Forward Deployed Engineering is done at Decagon — Sunny Rekhi",
      "author": "Sunny Rekhi",
      "last_modified": "2026-07-28T17:00:35Z",
      "analysis_file": "analysis/7wu2hsRfvV0.json"
    },
    {
      "id": "89aQ7T6cMwA",
      "resource": "https://www.youtube.com/watch?v=89aQ7T6cMwA",
      "title": "How to Fail at AI Strategy: Hamel Husain & Greg Ceccarelli",
      "author": null,
      "last_modified": "2025-04-13T16:19:16Z",
      "analysis_file": "analysis/89aQ7T6cMwA.json"
    },
    {
      "id": "8rABwKRsec4",
      "resource": "https://www.youtube.com/watch?v=8rABwKRsec4",
      "title": "The New Code — Sean Grove, OpenAI",
      "author": "Sean Grove, OpenAI",
      "last_modified": "2025-07-11T16:00:06Z",
      "analysis_file": "analysis/8rABwKRsec4.json"
    },
    {
      "id": "ClWD8OEYgp8",
      "resource": "https://www.youtube.com/watch?v=ClWD8OEYgp8",
      "title": "Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub",
      "author": "Maggie Appleton, GitHub",
      "last_modified": "2026-04-26T15:00:06Z",
      "analysis_file": "analysis/ClWD8OEYgp8.json"
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
      "id": "EAfP8pDs7h4",
      "resource": "https://www.youtube.com/watch?v=EAfP8pDs7h4",
      "title": "[Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments",
      "author": null,
      "last_modified": "2025-06-27T10:19:00Z",
      "analysis_file": "analysis/EAfP8pDs7h4.json"
    },
    {
      "id": "EUHx5ooJHuQ",
      "resource": "https://www.youtube.com/watch?v=EUHx5ooJHuQ",
      "title": "How Coding Agents change Software Development Forever - Hailong Zhang",
      "author": "Hailong Zhang",
      "last_modified": "2025-02-22T16:00:06Z",
      "analysis_file": "analysis/EUHx5ooJHuQ.json"
    },
    {
      "id": "H6MrR5NbTZA",
      "resource": "https://www.youtube.com/watch?v=H6MrR5NbTZA",
      "title": "Don’t get one-shotted: Use AI to test, review, merge, and deploy code — Tomas Reimers, Graphite",
      "author": "Tomas Reimers, Graphite",
      "last_modified": "2025-06-27T10:25:04Z",
      "analysis_file": "analysis/H6MrR5NbTZA.json"
    },
    {
      "id": "IddXPepIAS4",
      "resource": "https://www.youtube.com/watch?v=IddXPepIAS4",
      "title": "Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS",
      "author": "Erik Hanchett, AWS",
      "last_modified": "2026-06-28T17:30:24Z",
      "analysis_file": "analysis/IddXPepIAS4.json"
    },
    {
      "id": "Lue8K2jqfKk",
      "resource": "https://www.youtube.com/watch?v=Lue8K2jqfKk",
      "title": "Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic",
      "author": "Boris Cherny, Anthropic",
      "last_modified": "2025-07-04T16:00:06Z",
      "analysis_file": "analysis/Lue8K2jqfKk.json"
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
      "id": "N4vCBM5YbN0",
      "resource": "https://www.youtube.com/watch?v=N4vCBM5YbN0",
      "title": "Building Code First AI Agents with Azure AI Agent Service — Cedric Vidal, Microsoft",
      "author": "Cedric Vidal, Microsoft",
      "last_modified": "2025-06-27T10:03:21Z",
      "analysis_file": "analysis/N4vCBM5YbN0.json"
    },
    {
      "id": "OA-Mc60Rboo",
      "resource": "https://www.youtube.com/watch?v=OA-Mc60Rboo",
      "title": "Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA",
      "author": "Lakshya A. Agrawal, GEPA",
      "last_modified": "2026-09-26T17:00:06Z",
      "analysis_file": "analysis/OA-Mc60Rboo.json"
    },
    {
      "id": "OL7kfezynJM",
      "resource": "https://www.youtube.com/watch?v=OL7kfezynJM",
      "title": "Multiplayer agentic engineering — Arjun Singh, Superconductor",
      "author": "Arjun Singh, Superconductor",
      "last_modified": "2026-08-09T20:30:34Z",
      "analysis_file": "analysis/OL7kfezynJM.json"
    },
    {
      "id": "PXj0p_mW9nI",
      "resource": "https://www.youtube.com/watch?v=PXj0p_mW9nI",
      "title": "Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic",
      "author": "Katelyn Lesse & Angela Jiang, Anthropic",
      "last_modified": "2026-09-14T14:00:06Z",
      "analysis_file": "analysis/PXj0p_mW9nI.json"
    },
    {
      "id": "PwCSYy-oGsM",
      "resource": "https://www.youtube.com/watch?v=PwCSYy-oGsM",
      "title": "Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI",
      "author": "Druid AI",
      "last_modified": "2026-10-12T00:00:10Z",
      "analysis_file": "analysis/PwCSYy-oGsM.json"
    },
    {
      "id": "RkVILz06y08",
      "resource": "https://www.youtube.com/watch?v=RkVILz06y08",
      "title": "Real world MCPs in GitHub Copilot Agent Mode — Jon Peck, Microsoft",
      "author": "Jon Peck, Microsoft",
      "last_modified": "2025-07-19T07:00:21Z",
      "analysis_file": "analysis/RkVILz06y08.json"
    },
    {
      "id": "SZStlIhyTCY",
      "resource": "https://www.youtube.com/watch?v=SZStlIhyTCY",
      "title": "Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company",
      "author": "Martin Harrysson & Natasha Maniar, McKinsey & Company",
      "last_modified": "2025-12-12T17:00:06Z",
      "analysis_file": "analysis/SZStlIhyTCY.json"
    },
    {
      "id": "Sjfz1TqxzEs",
      "resource": "https://www.youtube.com/watch?v=Sjfz1TqxzEs",
      "title": "Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics",
      "author": "Jason Ma, Dyna Robotics",
      "last_modified": "2026-09-24T14:30:12Z",
      "analysis_file": "analysis/Sjfz1TqxzEs.json"
    },
    {
      "id": "T0HhO4YtTfE",
      "resource": "https://www.youtube.com/watch?v=T0HhO4YtTfE",
      "title": "AI System Design: From Idea to Production - Apoorva Joshi, MongoDB",
      "author": "Apoorva Joshi, MongoDB",
      "last_modified": "2026-06-28T20:30:21Z",
      "analysis_file": "analysis/T0HhO4YtTfE.json"
    },
    {
      "id": "UG9IAdmi2Dg",
      "resource": "https://www.youtube.com/watch?v=UG9IAdmi2Dg",
      "title": "Building the platform for agent coordination — Tom Moor, Linear",
      "author": "Tom Moor, Linear",
      "last_modified": "2025-07-28T19:37:32Z",
      "analysis_file": "analysis/UG9IAdmi2Dg.json"
    },
    {
      "id": "VMemhtlsoNk",
      "resource": "https://www.youtube.com/watch?v=VMemhtlsoNk",
      "title": "Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF",
      "author": "Mike Spitz, PFF",
      "last_modified": "2026-05-15T17:00:06Z",
      "analysis_file": "analysis/VMemhtlsoNk.json"
    },
    {
      "id": "VktrqzQgytY",
      "resource": "https://www.youtube.com/watch?v=VktrqzQgytY",
      "title": "CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner",
      "author": "Hugo Santos and Madison Faulkner",
      "last_modified": "2026-05-13T13:00:06Z",
      "analysis_file": "analysis/VktrqzQgytY.json"
    },
    {
      "id": "W76woOYHlvY",
      "resource": "https://www.youtube.com/watch?v=W76woOYHlvY",
      "title": "Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban",
      "author": "Louis Knight-Webb, Vibe Kanban",
      "last_modified": "2026-05-02T21:00:06Z",
      "analysis_file": "analysis/W76woOYHlvY.json"
    },
    {
      "id": "XqF-IFHBCkM",
      "resource": "https://www.youtube.com/watch?v=XqF-IFHBCkM",
      "title": "Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel",
      "author": "Sonar & McKinsey Panel",
      "last_modified": "2026-10-07T15:30:19Z",
      "analysis_file": "analysis/XqF-IFHBCkM.json"
    },
    {
      "id": "YYH0DMQr30A",
      "resource": "https://www.youtube.com/watch?v=YYH0DMQr30A",
      "title": "Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel",
      "author": "Kobie Crawdord, Snorkel",
      "last_modified": "2026-06-02T17:00:39Z",
      "analysis_file": "analysis/YYH0DMQr30A.json"
    },
    {
      "id": "YZQsWVeN3rE",
      "resource": "https://www.youtube.com/watch?v=YZQsWVeN3rE",
      "title": "Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech",
      "author": "Alex Bauer, Upside.tech",
      "last_modified": "2026-07-11T00:57:36Z",
      "analysis_file": "analysis/YZQsWVeN3rE.json"
    },
    {
      "id": "YgEv7IQzGdM",
      "resource": "https://www.youtube.com/watch?v=YgEv7IQzGdM",
      "title": "How to Kill the Code Review — Ankit Jain, Aviator",
      "author": "Ankit Jain, Aviator",
      "last_modified": "2026-08-17T20:00:08Z",
      "analysis_file": "analysis/YgEv7IQzGdM.json"
    },
    {
      "id": "Zniw5c9_jx8",
      "resource": "https://www.youtube.com/watch?v=Zniw5c9_jx8",
      "title": "Mentoring the Machine — Eric Hou, Augment Code",
      "author": "Eric Hou, Augment Code",
      "last_modified": "2025-07-24T15:01:06Z",
      "analysis_file": "analysis/Zniw5c9_jx8.json"
    },
    {
      "id": "_ehJyfHg1Vk",
      "resource": "https://www.youtube.com/watch?v=_ehJyfHg1Vk",
      "title": "The Era of Compound Engineering — Kieran Klaassen, Every/Cora",
      "author": "Kieran Klaassen, Every/Cora",
      "last_modified": "2026-08-20T15:00:06Z",
      "analysis_file": "analysis/_ehJyfHg1Vk.json"
    },
    {
      "id": "a4BV0gGmXgA",
      "resource": "https://www.youtube.com/watch?v=a4BV0gGmXgA",
      "title": "Five hard earned lessons about Evals — Ankur Goyal, Braintrust",
      "author": "Ankur Goyal, Braintrust",
      "last_modified": "2025-08-23T17:45:06Z",
      "analysis_file": "analysis/a4BV0gGmXgA.json"
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
      "id": "atwSCxWFVMg",
      "resource": "https://www.youtube.com/watch?v=atwSCxWFVMg",
      "title": "GPT Web App Generator - 10,000 apps created in a month: Matija Sosic",
      "author": "10,000 apps created in a month: Matija Sosic",
      "last_modified": "2024-01-26T20:51:42Z",
      "analysis_file": "analysis/atwSCxWFVMg.json"
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
      "id": "bdHaOXZOhcM",
      "resource": "https://www.youtube.com/watch?v=bdHaOXZOhcM",
      "title": "Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company",
      "author": "Hursh Agrawal, The Browser Company",
      "last_modified": "2026-08-20T14:00:21Z",
      "analysis_file": "analysis/bdHaOXZOhcM.json"
    },
    {
      "id": "bjNYEc908oQ",
      "resource": "https://www.youtube.com/watch?v=bjNYEc908oQ",
      "title": "Building Reliable Agentic Systems: Eno Reyes",
      "author": null,
      "last_modified": "2024-08-20T13:44:51Z",
      "analysis_file": "analysis/bjNYEc908oQ.json"
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
      "id": "cCRO3ChaYhM",
      "resource": "https://www.youtube.com/watch?v=cCRO3ChaYhM",
      "title": "Platforms for Humans and Machines: Engineering for the Age of Agents — Juan Herreros Elorza",
      "author": "Juan Herreros Elorza",
      "last_modified": "2026-04-08T09:30:06Z",
      "analysis_file": "analysis/cCRO3ChaYhM.json"
    },
    {
      "id": "eIoohUmYpGI",
      "resource": "https://www.youtube.com/watch?v=eIoohUmYpGI",
      "title": "The Infinite Software Crisis – Jake Nations, Netflix",
      "author": "Jake Nations, Netflix",
      "last_modified": "2025-12-20T17:00:06Z",
      "analysis_file": "analysis/eIoohUmYpGI.json"
    },
    {
      "id": "eJOjdjO45Sc",
      "resource": "https://www.youtube.com/watch?v=eJOjdjO45Sc",
      "title": "How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind",
      "author": "Mukund Sridhar & Aarush Selvan, Google DeepMind",
      "last_modified": "2025-03-26T19:41:41Z",
      "analysis_file": "analysis/eJOjdjO45Sc.json"
    },
    {
      "id": "eOxOzcw70f0",
      "resource": "https://www.youtube.com/watch?v=eOxOzcw70f0",
      "title": "Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison",
      "author": "Harald Kirschner, Christopher Harrison",
      "last_modified": "2025-08-03T04:30:57Z",
      "analysis_file": "analysis/eOxOzcw70f0.json"
    },
    {
      "id": "h403btjldDQ",
      "resource": "https://www.youtube.com/watch?v=h403btjldDQ",
      "title": "Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa",
      "author": "Dotta Bippa",
      "last_modified": "2026-04-15T21:59:05Z",
      "analysis_file": "analysis/h403btjldDQ.json"
    },
    {
      "id": "iheWKg2Tkrk",
      "resource": "https://www.youtube.com/watch?v=iheWKg2Tkrk",
      "title": "Ship Production Software in Minutes, Not Months — Eno Reyes, Factory",
      "author": "Eno Reyes, Factory",
      "last_modified": "2025-07-25T23:11:00Z",
      "analysis_file": "analysis/iheWKg2Tkrk.json"
    },
    {
      "id": "jWq-aZIU0kM",
      "resource": "https://www.youtube.com/watch?v=jWq-aZIU0kM",
      "title": "Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i",
      "author": "Ali Khial, G2i",
      "last_modified": "2026-07-31T16:00:06Z",
      "analysis_file": "analysis/jWq-aZIU0kM.json"
    },
    {
      "id": "kRkcNOsRyYg",
      "resource": "https://www.youtube.com/watch?v=kRkcNOsRyYg",
      "title": "AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j",
      "author": "Zach Blumenfeld, Neo4j",
      "last_modified": "2026-07-23T07:00:23Z",
      "analysis_file": "analysis/kRkcNOsRyYg.json"
    },
    {
      "id": "khVX_BUnEwU",
      "resource": "https://www.youtube.com/watch?v=khVX_BUnEwU",
      "title": "Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital",
      "author": "Yohei Nakajima, Untapped Capital",
      "last_modified": "2026-07-22T20:00:06Z",
      "analysis_file": "analysis/khVX_BUnEwU.json"
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
      "id": "mOf-PP4mVjA",
      "resource": "https://www.youtube.com/watch?v=mOf-PP4mVjA",
      "title": "Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs",
      "author": "James Le, TwelveLabs",
      "last_modified": "2026-07-23T02:00:03Z",
      "analysis_file": "analysis/mOf-PP4mVjA.json"
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
      "id": "pFsfax19yOM",
      "resource": "https://www.youtube.com/watch?v=pFsfax19yOM",
      "title": "Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser",
      "author": "Nick Nisi and Zack Proser",
      "last_modified": "2026-05-06T17:00:06Z",
      "analysis_file": "analysis/pFsfax19yOM.json"
    },
    {
      "id": "pSto5YaNGUo",
      "resource": "https://www.youtube.com/watch?v=pSto5YaNGUo",
      "title": "The Agentic AI Engineer - Benedikt Sanftl, Mutagent",
      "author": "Benedikt Sanftl, Mutagent",
      "last_modified": "2026-06-29T01:30:19Z",
      "analysis_file": "analysis/pSto5YaNGUo.json"
    },
    {
      "id": "pzmbleiOfCM",
      "resource": "https://www.youtube.com/watch?v=pzmbleiOfCM",
      "title": "Voice Agents: the good, the bad, and the ugly",
      "author": null,
      "last_modified": "2025-02-22T20:00:06Z",
      "analysis_file": "analysis/pzmbleiOfCM.json"
    },
    {
      "id": "q-WOjZhOMCA",
      "resource": "https://www.youtube.com/watch?v=q-WOjZhOMCA",
      "title": "IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork",
      "author": "Sarthak Aggarwal, Decawork",
      "last_modified": "2026-08-20T14:30:38Z",
      "analysis_file": "analysis/q-WOjZhOMCA.json"
    },
    {
      "id": "qLqttdO33UM",
      "resource": "https://www.youtube.com/watch?v=qLqttdO33UM",
      "title": "Vision: Zero Bugs — Johann Schleier-Smith, Temporal",
      "author": "Johann Schleier-Smith, Temporal",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/qLqttdO33UM.json"
    },
    {
      "id": "qdmxApz3EJI",
      "resource": "https://www.youtube.com/watch?v=qdmxApz3EJI",
      "title": "On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks",
      "author": "Omar Khattab, DSPy & Databricks",
      "last_modified": "2025-08-06T16:15:49Z",
      "analysis_file": "analysis/qdmxApz3EJI.json"
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
      "id": "rT2Del5pwg4",
      "resource": "https://www.youtube.com/watch?v=rT2Del5pwg4",
      "title": "Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One",
      "author": "Max Kanat-Alexander, Capital One",
      "last_modified": "2025-12-23T17:30:28Z",
      "analysis_file": "analysis/rT2Del5pwg4.json"
    },
    {
      "id": "rcsliSIy_YU",
      "resource": "https://www.youtube.com/watch?v=rcsliSIy_YU",
      "title": "Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands",
      "author": "Robert Brennan, OpenHands",
      "last_modified": "2026-01-08T16:30:23Z",
      "analysis_file": "analysis/rcsliSIy_YU.json"
    },
    {
      "id": "rgjF5o2Qjsc",
      "resource": "https://www.youtube.com/watch?v=rgjF5o2Qjsc",
      "title": "The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo",
      "author": "Itamar Friedman, Qodo",
      "last_modified": "2025-12-11T21:58:59Z",
      "analysis_file": "analysis/rgjF5o2Qjsc.json"
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
      "id": "v4F1gFy-hqg",
      "resource": "https://www.youtube.com/watch?v=v4F1gFy-hqg",
      "title": "\"Software Fundamentals Matter More Than Ever\" — Matt Pocock",
      "author": "Matt Pocock",
      "last_modified": "2026-04-23T15:15:06Z",
      "analysis_file": "analysis/v4F1gFy-hqg.json"
    },
    {
      "id": "vGCJ7diEtrw",
      "resource": "https://www.youtube.com/watch?v=vGCJ7diEtrw",
      "title": "What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory",
      "author": "Tereza Tížková, Factory",
      "last_modified": "2026-09-27T15:00:02Z",
      "analysis_file": "analysis/vGCJ7diEtrw.json"
    },
    {
      "id": "x_1EumTaXeE",
      "resource": "https://www.youtube.com/watch?v=x_1EumTaXeE",
      "title": "Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue",
      "author": "Josh Albrecht, Imbue",
      "last_modified": "2025-07-25T23:10:37Z",
      "analysis_file": "analysis/x_1EumTaXeE.json"
    },
    {
      "id": "zMXKhhwiCIc",
      "resource": "https://www.youtube.com/watch?v=zMXKhhwiCIc",
      "title": "Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage",
      "author": "Alex Gavrilescu, Funstage",
      "last_modified": "2025-11-24T20:16:38Z",
      "analysis_file": "analysis/zMXKhhwiCIc.json"
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

# Define behavior and acceptance criteria before delegating

## What

Define behavior and acceptance criteria before delegating

Clear success criteria let an agent verify that its result satisfies the requested work instead of stopping at a plausible artifact.

## Evidence

Source analysis [^-CnA2lGfymY]; no independently matched timestamped quote published.

Source analysis [^-npY6XjM8CQ]; no independently matched timestamped quote published.

Source analysis [^0I07YAuF8xA]; no independently matched timestamped quote published.

Source analysis [^0ML7ZLMdcl4]; no independently matched timestamped quote published.

Source analysis [^1P1hJ36rxM0]; no independently matched timestamped quote published.

Source analysis [^1nOTQsfe1RU]; no independently matched timestamped quote published.

Source analysis [^3axY1wz2OvA]; no independently matched timestamped quote published.

Source analysis [^3hXJI2q0Jz8]; no independently matched timestamped quote published.

Source analysis [^6NIr_cYPglk]; no independently matched timestamped quote published.

Source analysis [^6bmM45jkMDY]; no independently matched timestamped quote published.

Source analysis [^7GMKdpLsxwU]; no independently matched timestamped quote published.

Source analysis [^7vn4WpqNpck]; no independently matched timestamped quote published.

Source analysis [^7wu2hsRfvV0]; no independently matched timestamped quote published.

Source analysis [^89aQ7T6cMwA]; no independently matched timestamped quote published.

Source analysis [^8rABwKRsec4]; no independently matched timestamped quote published.

Source analysis [^ClWD8OEYgp8]; no independently matched timestamped quote published.

Source analysis [^DqtmZE6Hl0g]; no independently matched timestamped quote published.

Source analysis [^EAfP8pDs7h4]; no independently matched timestamped quote published.

> unit test is a problem, but software engineering is not a problem.
> — 06:10 [^EUHx5ooJHuQ]

Source analysis [^H6MrR5NbTZA]; no independently matched timestamped quote published.

Source analysis [^IddXPepIAS4]; no independently matched timestamped quote published.

Source analysis [^Lue8K2jqfKk]; no independently matched timestamped quote published.

> working with agents to make a really, really detailed plan. So, I think
> — 09:21 [^MGzymaYBiss]

Source analysis [^N4vCBM5YbN0]; no independently matched timestamped quote published.

> instead update a prompt where a single natural language update can give a very
> — 03:40 [^OA-Mc60Rboo]

> the agent has clear criteria to evaluate whether it did a good job on the work
> — 07:36 [^OL7kfezynJM]

> And if it scored anything less than 100% on that kind of task, we would actually
> — 07:50 [^PXj0p_mW9nI]

Source analysis [^PwCSYy-oGsM]; no independently matched timestamped quote published.

> textbased diraph diagramming. But that readme is intended to be very complete
> — 02:14 [^RkVILz06y08]

Source analysis [^SZStlIhyTCY]; no independently matched timestamped quote published.

Source analysis [^Sjfz1TqxzEs]; no independently matched timestamped quote published.

Source analysis [^T0HhO4YtTfE]; no independently matched timestamped quote published.

Source analysis [^UG9IAdmi2Dg]; no independently matched timestamped quote published.

Source analysis [^VMemhtlsoNk]; no independently matched timestamped quote published.

Source analysis [^VktrqzQgytY]; no independently matched timestamped quote published.

Source analysis [^W76woOYHlvY]; no independently matched timestamped quote published.

Source analysis [^XqF-IFHBCkM]; no independently matched timestamped quote published.

Source analysis [^YYH0DMQr30A]; no independently matched timestamped quote published.

> agents why you want them to do something, and they will do it a lot
> — 08:59 [^YZQsWVeN3rE]

> and then you verify. But, there's no feedback loop.
> — 04:55 [^YgEv7IQzGdM]

Source analysis [^Zniw5c9_jx8]; no independently matched timestamped quote published.

> and it comes back with very sharp questions. I always like the questions.
> — 12:35 [^_ehJyfHg1Vk]

> they're like a spec or like a PRD for your AI application. And if you think
> — 03:41 [^a4BV0gGmXgA]

Source analysis [^am_oeAoUhew]; no independently matched timestamped quote published.

Source analysis [^atwSCxWFVMg]; no independently matched timestamped quote published.

> which then gets broken down by the agent into a planning mode into step by step
> — 05:54 [^bSG9wUYaHWU]

> like hey write the tests first so they capture what you do. This is really
> — 09:05 [^bdHaOXZOhcM]

> kind of hard-coded logic uh you know ultimately all of this is about error
> — 06:38 [^bjNYEc908oQ]

> desired end state and feed in the current state of the world and have an
> — 08:14 [^c35YoMdnI78]

> the agent, this is how you know you have succeeded at the task.
> — 11:26 [^cCRO3ChaYhM]

> tokens became 2,000 words of specification. And then to take it even
> — 10:47 [^eIoohUmYpGI]

Source analysis [^eJOjdjO45Sc]; no independently matched timestamped quote published.

Source analysis [^eOxOzcw70f0]; no independently matched timestamped quote published.

Source analysis [^h403btjldDQ]; no independently matched timestamped quote published.

Source analysis [^iheWKg2Tkrk]; no independently matched timestamped quote published.

Source analysis [^jWq-aZIU0kM]; no independently matched timestamped quote published.

Source analysis [^kRkcNOsRyYg]; no independently matched timestamped quote published.

> simulated games against three reference agents and then if the win rate
> — 13:47 [^khVX_BUnEwU]

> the config config and submit the job and not have to worry about like doing
> — 08:09 [^kiqubc5b5Yo]

Source analysis [^mOf-PP4mVjA]; no independently matched timestamped quote published.

Source analysis [^ojJXgXLUQFc]; no independently matched timestamped quote published.

> confidence score. It's based on the problem clarity, it has a 20. Goal
> — 1:01:43 [^pFsfax19yOM]

> isolated from the implementation details. So once you decide to
> — 09:32 [^pSto5YaNGUo]

Source analysis [^pzmbleiOfCM]; no independently matched timestamped quote published.

Source analysis [^q-WOjZhOMCA]; no independently matched timestamped quote published.

Source analysis [^qLqttdO33UM]; no independently matched timestamped quote published.

Source analysis [^qdmxApz3EJI]; no independently matched timestamped quote published.

Source analysis [^qqXdLf3wy1E]; no independently matched timestamped quote published.

> is making each individual response fast. You don't actually want to shorten the
> — 11:13 [^rT2Del5pwg4]

Source analysis [^rcsliSIy_YU]; no independently matched timestamped quote published.

> your spec to your to your code uh uh make tests which are executable specs
> — 17:45 [^rgjF5o2Qjsc]

> like latency is a big concern for acceptance rates. So if you look at
> — 15:53 [^tHN44yJoeS8]

> about the module changes and the interfaces inside those modules, how
> — 16:50 [^v4F1gFy-hqg]

> that's written before any code is done. And first type is scrutiny validator.
> — 13:49 [^vGCJ7diEtrw]

> the AI agent to first make a plan without writing any code at all. Then
> — 05:30 [^x_1EumTaXeE]

> run unit test they should also uh check if the acceptance criteria as are met
> — 12:08 [^zMXKhhwiCIc]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer duplicate or misdirected runs
- **Speed:** Less blocked work and handoff delay
- **Quality:** More verifiable customer-relevant scope
- **Reliability:** Explicit ownership, dependencies and stop conditions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^-CnA2lGfymY]: ["I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox](https://www.youtube.com/watch?v=-CnA2lGfymY); publication: 2026-07-13T19:25:09Z; analysis: `analysis/-CnA2lGfymY.json`.
[^-npY6XjM8CQ]: [When Will The Benchmaxxing Plague End? — Nick Heiner, Surge AI](https://www.youtube.com/watch?v=-npY6XjM8CQ); publication: 2026-08-02T16:30:06Z; analysis: `analysis/-npY6XjM8CQ.json`.
[^0I07YAuF8xA]: [From Ingestion to Agents: How AI Teams Build on Document Intelligence — Adit Abraham, Reducto](https://www.youtube.com/watch?v=0I07YAuF8xA); publication: 2026-09-23T14:30:11Z; analysis: `analysis/0I07YAuF8xA.json`.
[^0ML7ZLMdcl4]: [AI Engineering at Jane Street - John Crepezzi](https://www.youtube.com/watch?v=0ML7ZLMdcl4); publication: 2025-03-28T15:04:44Z; analysis: `analysis/0ML7ZLMdcl4.json`.
[^1P1hJ36rxM0]: ["Software engineering is not about writing code" — Benoit Schillings, Google DeepMind VP of Research](https://www.youtube.com/watch?v=1P1hJ36rxM0); publication: 2026-07-17T15:24:44Z; analysis: `analysis/1P1hJ36rxM0.json`.
[^1nOTQsfe1RU]: ["Data readiness" is a Myth: Reliable AI with an Agentic Semantic Layer — Anushrut Gupta, PromptQL](https://www.youtube.com/watch?v=1nOTQsfe1RU); publication: 2025-06-27T09:40:39Z; analysis: `analysis/1nOTQsfe1RU.json`.
[^3axY1wz2OvA]: [Same GPU, 50% More Output: Why the Operator Matters — Oliver Kennon, SemiAnalysis](https://www.youtube.com/watch?v=3axY1wz2OvA); publication: 2026-10-20T23:00:22Z; analysis: `analysis/3axY1wz2OvA.json`.
[^3hXJI2q0Jz8]: [Recursive Coding Agents - Raymond Weitekamp, OpenProse](https://www.youtube.com/watch?v=3hXJI2q0Jz8); publication: 2026-06-25T21:00:06Z; analysis: `analysis/3hXJI2q0Jz8.json`.
[^6NIr_cYPglk]: [To the moon! Navigating deep context in legacy code with Augment Agent — Forrest Brazeal, Matt Ball](https://www.youtube.com/watch?v=6NIr_cYPglk); publication: 2025-06-27T10:46:59Z; analysis: `analysis/6NIr_cYPglk.json`.
[^6bmM45jkMDY]: [You Can't Prompt the Room: The Last Skill AI Won't Replace - Balázs Horváth, VisualLabs](https://www.youtube.com/watch?v=6bmM45jkMDY); publication: 2026-06-29T02:30:20Z; analysis: `analysis/6bmM45jkMDY.json`.
[^7GMKdpLsxwU]: [The Missing Layer: Design Taste in AI Agents — Hassan El Mghari, Together AI](https://www.youtube.com/watch?v=7GMKdpLsxwU); publication: 2026-08-21T15:00:06Z; analysis: `analysis/7GMKdpLsxwU.json`.
[^7vn4WpqNpck]: [Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs](https://www.youtube.com/watch?v=7vn4WpqNpck); publication: 2026-08-08T19:00:06Z; analysis: `analysis/7vn4WpqNpck.json`.
[^7wu2hsRfvV0]: [How Forward Deployed Engineering is done at Decagon — Sunny Rekhi](https://www.youtube.com/watch?v=7wu2hsRfvV0); publication: 2026-07-28T17:00:35Z; analysis: `analysis/7wu2hsRfvV0.json`.
[^89aQ7T6cMwA]: [How to Fail at AI Strategy: Hamel Husain & Greg Ceccarelli](https://www.youtube.com/watch?v=89aQ7T6cMwA); publication: 2025-04-13T16:19:16Z; analysis: `analysis/89aQ7T6cMwA.json`.
[^8rABwKRsec4]: [The New Code — Sean Grove, OpenAI](https://www.youtube.com/watch?v=8rABwKRsec4); publication: 2025-07-11T16:00:06Z; analysis: `analysis/8rABwKRsec4.json`.
[^ClWD8OEYgp8]: [Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub](https://www.youtube.com/watch?v=ClWD8OEYgp8); publication: 2026-04-26T15:00:06Z; analysis: `analysis/ClWD8OEYgp8.json`.
[^DqtmZE6Hl0g]: [The Prompt is the Platform - Dominik Tornow, Resonate HQ](https://www.youtube.com/watch?v=DqtmZE6Hl0g); publication: 2026-06-29T01:00:36Z; analysis: `analysis/DqtmZE6Hl0g.json`.
[^EAfP8pDs7h4]: [[Full Workshop] Vibe Coding at Scale: Customizing AI Assistants for Enterprise Environments](https://www.youtube.com/watch?v=EAfP8pDs7h4); publication: 2025-06-27T10:19:00Z; analysis: `analysis/EAfP8pDs7h4.json`.
[^EUHx5ooJHuQ]: [How Coding Agents change Software Development Forever - Hailong Zhang](https://www.youtube.com/watch?v=EUHx5ooJHuQ); publication: 2025-02-22T16:00:06Z; analysis: `analysis/EUHx5ooJHuQ.json`.
[^H6MrR5NbTZA]: [Don’t get one-shotted: Use AI to test, review, merge, and deploy code — Tomas Reimers, Graphite](https://www.youtube.com/watch?v=H6MrR5NbTZA); publication: 2025-06-27T10:25:04Z; analysis: `analysis/H6MrR5NbTZA.json`.
[^IddXPepIAS4]: [Using Spec-Driven Development for Production Workflows - Erik Hanchett, AWS](https://www.youtube.com/watch?v=IddXPepIAS4); publication: 2026-06-28T17:30:24Z; analysis: `analysis/IddXPepIAS4.json`.
[^Lue8K2jqfKk]: [Claude Code & the evolution of agentic coding — Boris Cherny, Anthropic](https://www.youtube.com/watch?v=Lue8K2jqfKk); publication: 2025-07-04T16:00:06Z; analysis: `analysis/Lue8K2jqfKk.json`.
[^MGzymaYBiss]: [Dispatch from the Future: building an AI-native Company – Dan Shipper, Every, AI & I](https://www.youtube.com/watch?v=MGzymaYBiss); publication: 2025-12-18T18:00:06Z; analysis: `analysis/MGzymaYBiss.json`.
[^N4vCBM5YbN0]: [Building Code First AI Agents with Azure AI Agent Service — Cedric Vidal, Microsoft](https://www.youtube.com/watch?v=N4vCBM5YbN0); publication: 2025-06-27T10:03:21Z; analysis: `analysis/N4vCBM5YbN0.json`.
[^OA-Mc60Rboo]: [Beating RL With Reflection: GEPA and Optimize Anything — Lakshya A. Agrawal, GEPA](https://www.youtube.com/watch?v=OA-Mc60Rboo); publication: 2026-09-26T17:00:06Z; analysis: `analysis/OA-Mc60Rboo.json`.
[^OL7kfezynJM]: [Multiplayer agentic engineering — Arjun Singh, Superconductor](https://www.youtube.com/watch?v=OL7kfezynJM); publication: 2026-08-09T20:30:34Z; analysis: `analysis/OL7kfezynJM.json`.
[^PXj0p_mW9nI]: [Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic](https://www.youtube.com/watch?v=PXj0p_mW9nI); publication: 2026-09-14T14:00:06Z; analysis: `analysis/PXj0p_mW9nI.json`.
[^PwCSYy-oGsM]: [Containment Is Lying to You: Measuring AI Agents Like Employees — Druid AI](https://www.youtube.com/watch?v=PwCSYy-oGsM); publication: 2026-10-12T00:00:10Z; analysis: `analysis/PwCSYy-oGsM.json`.
[^RkVILz06y08]: [Real world MCPs in GitHub Copilot Agent Mode — Jon Peck, Microsoft](https://www.youtube.com/watch?v=RkVILz06y08); publication: 2025-07-19T07:00:21Z; analysis: `analysis/RkVILz06y08.json`.
[^SZStlIhyTCY]: [Moving away from Agile: What's Next – Martin Harrysson & Natasha Maniar, McKinsey & Company](https://www.youtube.com/watch?v=SZStlIhyTCY); publication: 2025-12-12T17:00:06Z; analysis: `analysis/SZStlIhyTCY.json`.
[^Sjfz1TqxzEs]: [Robot Demos Are Easy. Reliability Is Hard — Jason Ma, Dyna Robotics](https://www.youtube.com/watch?v=Sjfz1TqxzEs); publication: 2026-09-24T14:30:12Z; analysis: `analysis/Sjfz1TqxzEs.json`.
[^T0HhO4YtTfE]: [AI System Design: From Idea to Production - Apoorva Joshi, MongoDB](https://www.youtube.com/watch?v=T0HhO4YtTfE); publication: 2026-06-28T20:30:21Z; analysis: `analysis/T0HhO4YtTfE.json`.
[^UG9IAdmi2Dg]: [Building the platform for agent coordination — Tom Moor, Linear](https://www.youtube.com/watch?v=UG9IAdmi2Dg); publication: 2025-07-28T19:37:32Z; analysis: `analysis/UG9IAdmi2Dg.json`.
[^VMemhtlsoNk]: [Agents Don't Do Standups: Building the Post-Engineer Engineering Org — Mike Spitz, PFF](https://www.youtube.com/watch?v=VMemhtlsoNk); publication: 2026-05-15T17:00:06Z; analysis: `analysis/VMemhtlsoNk.json`.
[^VktrqzQgytY]: [CI/CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner](https://www.youtube.com/watch?v=VktrqzQgytY); publication: 2026-05-13T13:00:06Z; analysis: `analysis/VktrqzQgytY.json`.
[^W76woOYHlvY]: [Software Engineering Is Becoming Plan and Review — Louis Knight-Webb, Vibe Kanban](https://www.youtube.com/watch?v=W76woOYHlvY); publication: 2026-05-02T21:00:06Z; analysis: `analysis/W76woOYHlvY.json`.
[^XqF-IFHBCkM]: [Redesigning How Software Gets Built With AI Agents — Sonar & McKinsey Panel](https://www.youtube.com/watch?v=XqF-IFHBCkM); publication: 2026-10-07T15:30:19Z; analysis: `analysis/XqF-IFHBCkM.json`.
[^YYH0DMQr30A]: [Task Fidelity Scaling Laws — Kobie Crawdord, Snorkel](https://www.youtube.com/watch?v=YYH0DMQr30A); publication: 2026-06-02T17:00:39Z; analysis: `analysis/YYH0DMQr30A.json`.
[^YZQsWVeN3rE]: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers — Alex Bauer, Upside.tech](https://www.youtube.com/watch?v=YZQsWVeN3rE); publication: 2026-07-11T00:57:36Z; analysis: `analysis/YZQsWVeN3rE.json`.
[^YgEv7IQzGdM]: [How to Kill the Code Review — Ankit Jain, Aviator](https://www.youtube.com/watch?v=YgEv7IQzGdM); publication: 2026-08-17T20:00:08Z; analysis: `analysis/YgEv7IQzGdM.json`.
[^Zniw5c9_jx8]: [Mentoring the Machine — Eric Hou, Augment Code](https://www.youtube.com/watch?v=Zniw5c9_jx8); publication: 2025-07-24T15:01:06Z; analysis: `analysis/Zniw5c9_jx8.json`.
[^_ehJyfHg1Vk]: [The Era of Compound Engineering — Kieran Klaassen, Every/Cora](https://www.youtube.com/watch?v=_ehJyfHg1Vk); publication: 2026-08-20T15:00:06Z; analysis: `analysis/_ehJyfHg1Vk.json`.
[^a4BV0gGmXgA]: [Five hard earned lessons about Evals — Ankur Goyal, Braintrust](https://www.youtube.com/watch?v=a4BV0gGmXgA); publication: 2025-08-23T17:45:06Z; analysis: `analysis/a4BV0gGmXgA.json`.
[^am_oeAoUhew]: [Harness Engineering: How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI](https://www.youtube.com/watch?v=am_oeAoUhew); publication: 2026-04-17T00:29:28Z; analysis: `analysis/am_oeAoUhew.json`.
[^atwSCxWFVMg]: [GPT Web App Generator - 10,000 apps created in a month: Matija Sosic](https://www.youtube.com/watch?v=atwSCxWFVMg); publication: 2024-01-26T20:51:42Z; analysis: `analysis/atwSCxWFVMg.json`.
[^bSG9wUYaHWU]: [Context Is the New Code — Patrick Debois, Tessl](https://www.youtube.com/watch?v=bSG9wUYaHWU); publication: 2026-05-03T14:00:06Z; analysis: `analysis/bSG9wUYaHWU.json`.
[^bdHaOXZOhcM]: [Prototyping as Leadership: How a CTO Ships with AI Agents — Hursh Agrawal, The Browser Company](https://www.youtube.com/watch?v=bdHaOXZOhcM); publication: 2026-08-20T14:00:21Z; analysis: `analysis/bdHaOXZOhcM.json`.
[^bjNYEc908oQ]: [Building Reliable Agentic Systems: Eno Reyes](https://www.youtube.com/watch?v=bjNYEc908oQ); publication: 2024-08-20T13:44:51Z; analysis: `analysis/bjNYEc908oQ.json`.
[^c35YoMdnI78]: [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](https://www.youtube.com/watch?v=c35YoMdnI78); publication: 2026-07-17T21:00:06Z; analysis: `analysis/c35YoMdnI78.json`.
[^cCRO3ChaYhM]: [Platforms for Humans and Machines: Engineering for the Age of Agents — Juan Herreros Elorza](https://www.youtube.com/watch?v=cCRO3ChaYhM); publication: 2026-04-08T09:30:06Z; analysis: `analysis/cCRO3ChaYhM.json`.
[^eIoohUmYpGI]: [The Infinite Software Crisis – Jake Nations, Netflix](https://www.youtube.com/watch?v=eIoohUmYpGI); publication: 2025-12-20T17:00:06Z; analysis: `analysis/eIoohUmYpGI.json`.
[^eJOjdjO45Sc]: [How Deep Research Works - Mukund Sridhar & Aarush Selvan, Google DeepMind](https://www.youtube.com/watch?v=eJOjdjO45Sc); publication: 2025-03-26T19:41:41Z; analysis: `analysis/eJOjdjO45Sc.json`.
[^eOxOzcw70f0]: [Real World Development with GitHub Copilot and VS Code — Harald Kirschner, Christopher Harrison](https://www.youtube.com/watch?v=eOxOzcw70f0); publication: 2025-08-03T04:30:57Z; analysis: `analysis/eOxOzcw70f0.json`.
[^h403btjldDQ]: [Paperclip: Open Source Human Control Plane for AI Labor — Dotta Bippa](https://www.youtube.com/watch?v=h403btjldDQ); publication: 2026-04-15T21:59:05Z; analysis: `analysis/h403btjldDQ.json`.
[^iheWKg2Tkrk]: [Ship Production Software in Minutes, Not Months — Eno Reyes, Factory](https://www.youtube.com/watch?v=iheWKg2Tkrk); publication: 2025-07-25T23:11:00Z; analysis: `analysis/iheWKg2Tkrk.json`.
[^jWq-aZIU0kM]: [Benchmarks: The Good, the Bad, and the Ugly — Ali Khial, G2i](https://www.youtube.com/watch?v=jWq-aZIU0kM); publication: 2026-07-31T16:00:06Z; analysis: `analysis/jWq-aZIU0kM.json`.
[^kRkcNOsRyYg]: [AI on Your Lakehouse: Context Comes in Shapes, Not Queries — Zach Blumenfeld, Neo4j](https://www.youtube.com/watch?v=kRkcNOsRyYg); publication: 2026-07-23T07:00:23Z; analysis: `analysis/kRkcNOsRyYg.json`.
[^khVX_BUnEwU]: [Active Graph Agent Runtime (BabyAGI 4) — Yohei Nakajima, Untapped Capital](https://www.youtube.com/watch?v=khVX_BUnEwU); publication: 2026-07-22T20:00:06Z; analysis: `analysis/khVX_BUnEwU.json`.
[^kiqubc5b5Yo]: [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains — Brendan Rappazzo](https://www.youtube.com/watch?v=kiqubc5b5Yo); publication: 2026-07-29T17:06:26Z; analysis: `analysis/kiqubc5b5Yo.json`.
[^mOf-PP4mVjA]: [Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs](https://www.youtube.com/watch?v=mOf-PP4mVjA); publication: 2026-07-23T02:00:03Z; analysis: `analysis/mOf-PP4mVjA.json`.
[^ojJXgXLUQFc]: [The SDLC You Build Yourself — Andy Wong, Andrei Bocan & Shane Wolf, Atlassian](https://www.youtube.com/watch?v=ojJXgXLUQFc); publication: 2026-10-11T14:30:40Z; analysis: `analysis/ojJXgXLUQFc.json`.
[^pFsfax19yOM]: [Full Walkthrough: Writing & Using Skills — Nick Nisi and Zack Proser](https://www.youtube.com/watch?v=pFsfax19yOM); publication: 2026-05-06T17:00:06Z; analysis: `analysis/pFsfax19yOM.json`.
[^pSto5YaNGUo]: [The Agentic AI Engineer - Benedikt Sanftl, Mutagent](https://www.youtube.com/watch?v=pSto5YaNGUo); publication: 2026-06-29T01:30:19Z; analysis: `analysis/pSto5YaNGUo.json`.
[^pzmbleiOfCM]: [Voice Agents: the good, the bad, and the ugly](https://www.youtube.com/watch?v=pzmbleiOfCM); publication: 2025-02-22T20:00:06Z; analysis: `analysis/pzmbleiOfCM.json`.
[^q-WOjZhOMCA]: [IT Admin for the AI Workforce — Sarthak Aggarwal, Decawork](https://www.youtube.com/watch?v=q-WOjZhOMCA); publication: 2026-08-20T14:30:38Z; analysis: `analysis/q-WOjZhOMCA.json`.
[^qLqttdO33UM]: [Vision: Zero Bugs — Johann Schleier-Smith, Temporal](https://www.youtube.com/watch?v=qLqttdO33UM); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qLqttdO33UM.json`.
[^qdmxApz3EJI]: [On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks](https://www.youtube.com/watch?v=qdmxApz3EJI); publication: 2025-08-06T16:15:49Z; analysis: `analysis/qdmxApz3EJI.json`.
[^qqXdLf3wy1E]: [Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant](https://www.youtube.com/watch?v=qqXdLf3wy1E); publication: 2025-11-24T20:16:38Z; analysis: `analysis/qqXdLf3wy1E.json`.
[^rT2Del5pwg4]: [Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One](https://www.youtube.com/watch?v=rT2Del5pwg4); publication: 2025-12-23T17:30:28Z; analysis: `analysis/rT2Del5pwg4.json`.
[^rcsliSIy_YU]: [Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands](https://www.youtube.com/watch?v=rcsliSIy_YU); publication: 2026-01-08T16:30:23Z; analysis: `analysis/rcsliSIy_YU.json`.
[^rgjF5o2Qjsc]: [The State of AI Code Quality: Hype vs Reality — Itamar Friedman, Qodo](https://www.youtube.com/watch?v=rgjF5o2Qjsc); publication: 2025-12-11T21:58:59Z; analysis: `analysis/rgjF5o2Qjsc.json`.
[^tHN44yJoeS8]: [Coding Evals: From Code Snippets to Codebases – Naman Jain, Cursor](https://www.youtube.com/watch?v=tHN44yJoeS8); publication: 2025-12-15T17:18:09Z; analysis: `analysis/tHN44yJoeS8.json`.
[^v4F1gFy-hqg]: ["Software Fundamentals Matter More Than Ever" — Matt Pocock](https://www.youtube.com/watch?v=v4F1gFy-hqg); publication: 2026-04-23T15:15:06Z; analysis: `analysis/v4F1gFy-hqg.json`.
[^vGCJ7diEtrw]: [What It Actually Takes to Build a Software Factory — Tereza Tížková, Factory](https://www.youtube.com/watch?v=vGCJ7diEtrw); publication: 2026-09-27T15:00:02Z; analysis: `analysis/vGCJ7diEtrw.json`.
[^x_1EumTaXeE]: [Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue](https://www.youtube.com/watch?v=x_1EumTaXeE); publication: 2025-07-25T23:10:37Z; analysis: `analysis/x_1EumTaXeE.json`.
[^zMXKhhwiCIc]: [Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage](https://www.youtube.com/watch?v=zMXKhhwiCIc); publication: 2025-11-24T20:16:38Z; analysis: `analysis/zMXKhhwiCIc.json`.
