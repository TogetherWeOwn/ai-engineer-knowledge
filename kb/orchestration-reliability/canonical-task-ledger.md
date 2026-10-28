---
{
  "type": "technique",
  "id": "canonical-task-ledger",
  "title": "Keep canonical append-only task and session state across interaction surfaces",
  "area": "orchestration-reliability",
  "status": "stable",
  "valid_from": "2026-10-07T20:00:04Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "1izYWsokr9s",
      "resource": "https://www.youtube.com/watch?v=1izYWsokr9s",
      "title": "Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal",
      "author": "Preeti Somal, Temporal",
      "last_modified": "2025-07-28T15:15:00Z",
      "analysis_file": "analysis/1izYWsokr9s.json"
    },
    {
      "id": "2wgPHvW0mG8",
      "resource": "https://www.youtube.com/watch?v=2wgPHvW0mG8",
      "title": "One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio",
      "author": "Suchet Bargoti, Skydio",
      "last_modified": "2026-09-24T15:00:35Z",
      "analysis_file": "analysis/2wgPHvW0mG8.json"
    },
    {
      "id": "HN-F-OQe6j0",
      "resource": "https://www.youtube.com/watch?v=HN-F-OQe6j0",
      "title": "Defying Gravity - Kevin Hou, Google DeepMind",
      "author": "Kevin Hou, Google DeepMind",
      "last_modified": "2025-12-02T22:51:09Z",
      "analysis_file": "analysis/HN-F-OQe6j0.json"
    },
    {
      "id": "JVuNPL5QO8Q",
      "resource": "https://www.youtube.com/watch?v=JVuNPL5QO8Q",
      "title": "Windsurf everywhere, doing everything, all at once - Kevin Hou, Windsurf",
      "author": "Kevin Hou, Windsurf",
      "last_modified": "2025-06-23T15:00:06Z",
      "analysis_file": "analysis/JVuNPL5QO8Q.json"
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
      "id": "QHBjufYK8TA",
      "resource": "https://www.youtube.com/watch?v=QHBjufYK8TA",
      "title": "The State of Model Routing — NVIDIA, Cognition, OpenRouter",
      "author": "NVIDIA, Cognition, OpenRouter",
      "last_modified": "2026-08-06T17:07:24Z",
      "analysis_file": "analysis/QHBjufYK8TA.json"
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
      "id": "UOcHfR3_tys",
      "resource": "https://www.youtube.com/watch?v=UOcHfR3_tys",
      "title": "Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band",
      "author": "Vlad Luzin, Band",
      "last_modified": "2026-09-30T13:00:33Z",
      "analysis_file": "analysis/UOcHfR3_tys.json"
    },
    {
      "id": "X6l4lpA0_NY",
      "resource": "https://www.youtube.com/watch?v=X6l4lpA0_NY",
      "title": "Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl",
      "author": "Dru Knox, Tessl",
      "last_modified": "2026-10-06T15:30:27Z",
      "analysis_file": "analysis/X6l4lpA0_NY.json"
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
      "id": "exiwa9QbQXI",
      "resource": "https://www.youtube.com/watch?v=exiwa9QbQXI",
      "title": "The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory",
      "author": "Davis Palmie, Factory",
      "last_modified": "2026-10-07T20:00:04Z",
      "analysis_file": "analysis/exiwa9QbQXI.json"
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
      "id": "ow1we5PzK-o",
      "resource": "https://www.youtube.com/watch?v=ow1we5PzK-o",
      "title": "The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory",
      "author": "Luke Alvoeiro, Factory",
      "last_modified": "2026-05-06T15:00:06Z",
      "analysis_file": "analysis/ow1we5PzK-o.json"
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

# Keep canonical append-only task and session state across interaction surfaces

## What

Keep canonical append-only task and session state across interaction surfaces

Slack/app/GitHub conversations attach to the same session and context instead of creating disconnected agents with duplicated histories.

## Evidence

Source analysis [^1izYWsokr9s]; no independently matched timestamped quote published.

Source analysis [^2wgPHvW0mG8]; no independently matched timestamped quote published.

Source analysis [^HN-F-OQe6j0]; no independently matched timestamped quote published.

Source analysis [^JVuNPL5QO8Q]; no independently matched timestamped quote published.

> exact same agent session. So, it's like the agent didn't forget what you did in
> — 04:00 [^OL7kfezynJM]

> which is um, one sub agent that continually has a running context. So
> — 18:44 [^QHBjufYK8TA]

Source analysis [^UG9IAdmi2Dg]; no independently matched timestamped quote published.

Source analysis [^UOcHfR3_tys]; no independently matched timestamped quote published.

> interface but now all of your touch points with the agent are legible. So we
> — 12:10 [^X6l4lpA0_NY]

Source analysis [^bVNNvWq6dKo]; no independently matched timestamped quote published.

> everything should share the same underlying harness and context.
> — 13:12 [^exiwa9QbQXI]

Source analysis [^mav15aW9lLM]; no independently matched timestamped quote published.

> state fragments across conversations without that coordinator and there's no
> — 03:02 [^ow1we5PzK-o]

> and it will give you like the entire trace of the task.
> — 17:43 [^yUmS-F9IX90]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Fewer full restarts and no-progress loops
- **Speed:** Less polling, contention and recovery delay
- **Quality:** Checkable intermediate and final outcomes
- **Reliability:** Bounded recoverable state transitions
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^1izYWsokr9s]: [Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal](https://www.youtube.com/watch?v=1izYWsokr9s); publication: 2025-07-28T15:15:00Z; analysis: `analysis/1izYWsokr9s.json`.
[^2wgPHvW0mG8]: [One Operator, Many Drones: Inside Skydio's Autonomy Stack — Suchet Bargoti, Skydio](https://www.youtube.com/watch?v=2wgPHvW0mG8); publication: 2026-09-24T15:00:35Z; analysis: `analysis/2wgPHvW0mG8.json`.
[^HN-F-OQe6j0]: [Defying Gravity - Kevin Hou, Google DeepMind](https://www.youtube.com/watch?v=HN-F-OQe6j0); publication: 2025-12-02T22:51:09Z; analysis: `analysis/HN-F-OQe6j0.json`.
[^JVuNPL5QO8Q]: [Windsurf everywhere, doing everything, all at once - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=JVuNPL5QO8Q); publication: 2025-06-23T15:00:06Z; analysis: `analysis/JVuNPL5QO8Q.json`.
[^OL7kfezynJM]: [Multiplayer agentic engineering — Arjun Singh, Superconductor](https://www.youtube.com/watch?v=OL7kfezynJM); publication: 2026-08-09T20:30:34Z; analysis: `analysis/OL7kfezynJM.json`.
[^QHBjufYK8TA]: [The State of Model Routing — NVIDIA, Cognition, OpenRouter](https://www.youtube.com/watch?v=QHBjufYK8TA); publication: 2026-08-06T17:07:24Z; analysis: `analysis/QHBjufYK8TA.json`.
[^UG9IAdmi2Dg]: [Building the platform for agent coordination — Tom Moor, Linear](https://www.youtube.com/watch?v=UG9IAdmi2Dg); publication: 2025-07-28T19:37:32Z; analysis: `analysis/UG9IAdmi2Dg.json`.
[^UOcHfR3_tys]: [Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band](https://www.youtube.com/watch?v=UOcHfR3_tys); publication: 2026-09-30T13:00:33Z; analysis: `analysis/UOcHfR3_tys.json`.
[^X6l4lpA0_NY]: [Harness Engineering: How to Build a Software Factory — Dru Knox, Tessl](https://www.youtube.com/watch?v=X6l4lpA0_NY); publication: 2026-10-06T15:30:27Z; analysis: `analysis/X6l4lpA0_NY.json`.
[^bVNNvWq6dKo]: [How Windsurf writes 90% of your code with an Agentic IDE - Kevin Hou, Windsurf](https://www.youtube.com/watch?v=bVNNvWq6dKo); publication: 2025-03-11T19:17:46Z; analysis: `analysis/bVNNvWq6dKo.json`.
[^exiwa9QbQXI]: [The Software Factory: From Bug Report to Production Code — Davis Palmie, Factory](https://www.youtube.com/watch?v=exiwa9QbQXI); publication: 2026-10-07T20:00:04Z; analysis: `analysis/exiwa9QbQXI.json`.
[^mav15aW9lLM]: [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard](https://www.youtube.com/watch?v=mav15aW9lLM); publication: 2026-08-19T18:30:15Z; analysis: `analysis/mav15aW9lLM.json`.
[^ow1we5PzK-o]: [The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory](https://www.youtube.com/watch?v=ow1we5PzK-o); publication: 2026-05-06T15:00:06Z; analysis: `analysis/ow1we5PzK-o.json`.
[^yUmS-F9IX90]: [Don't Build Slop (4 Levels of AI Agent Maturity) - Ara Khan, Cline](https://www.youtube.com/watch?v=yUmS-F9IX90); publication: 2026-05-19T15:00:06Z; analysis: `analysis/yUmS-F9IX90.json`.
