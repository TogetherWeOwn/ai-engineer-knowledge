---
{
  "type": "technique",
  "id": "visual-verification",
  "title": "Verify rendered UI with screenshots and scoped visual comparisons",
  "area": "testing-ci",
  "status": "stable",
  "valid_from": "2026-10-11T21:30:05Z",
  "valid_to": null,
  "superseded_by": null,
  "sources": [
    {
      "id": "9arM9b7JgOo",
      "resource": "https://www.youtube.com/watch?v=9arM9b7JgOo",
      "title": "Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat",
      "author": "Jeffrey Lee-Chan, Snapchat",
      "last_modified": "2026-07-11T14:45:18Z",
      "analysis_file": "analysis/9arM9b7JgOo.json"
    },
    {
      "id": "XLEYtv3cMlw",
      "resource": "https://www.youtube.com/watch?v=XLEYtv3cMlw",
      "title": "Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait",
      "author": "Sina Shahandeh, Radicait",
      "last_modified": "2026-07-18T23:30:06Z",
      "analysis_file": "analysis/XLEYtv3cMlw.json"
    },
    {
      "id": "_KFbT6eph5A",
      "resource": "https://www.youtube.com/watch?v=_KFbT6eph5A",
      "title": "Using AI to Build an Infinite Game: Jeff Schomay",
      "author": null,
      "last_modified": "2024-02-01T17:41:28Z",
      "analysis_file": "analysis/_KFbT6eph5A.json"
    },
    {
      "id": "p7gaxmCUiIU",
      "resource": "https://www.youtube.com/watch?v=p7gaxmCUiIU",
      "title": "Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase",
      "author": "Shubhankar Srivastava, Browserbase",
      "last_modified": "2026-10-11T21:30:05Z",
      "analysis_file": "analysis/p7gaxmCUiIU.json"
    },
    {
      "id": "r0AG44qYKsI",
      "resource": "https://www.youtube.com/watch?v=r0AG44qYKsI",
      "title": "This video was edited with AI agent. But how?",
      "author": null,
      "last_modified": "2025-02-22T20:00:06Z",
      "analysis_file": "analysis/r0AG44qYKsI.json"
    },
    {
      "id": "tUPPVhBBcoM",
      "resource": "https://www.youtube.com/watch?v=tUPPVhBBcoM",
      "title": "Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp",
      "author": "Zach Lloyd, Warp",
      "last_modified": "2026-09-27T17:30:36Z",
      "analysis_file": "analysis/tUPPVhBBcoM.json"
    },
    {
      "id": "v3u8xc0zLec",
      "resource": "https://www.youtube.com/watch?v=v3u8xc0zLec",
      "title": "Proactive Agents – Kath Korevec, Google Labs",
      "author": "Kath Korevec, Google Labs",
      "last_modified": "2025-12-13T04:44:20Z",
      "analysis_file": "analysis/v3u8xc0zLec.json"
    },
    {
      "id": "wpOA-UXynoM",
      "resource": "https://www.youtube.com/watch?v=wpOA-UXynoM",
      "title": "How Forward Deployed Engineering is done at Factory — Eno Reyes",
      "author": "Eno Reyes",
      "last_modified": "2026-07-28T22:00:06Z",
      "analysis_file": "analysis/wpOA-UXynoM.json"
    },
    {
      "id": "xLUQOqjudtA",
      "resource": "https://www.youtube.com/watch?v=xLUQOqjudtA",
      "title": "Tolan: Voice-First AI Companion — Paula Dozsa, Tolan",
      "author": "Paula Dozsa, Tolan",
      "last_modified": "2026-09-15T14:30:14Z",
      "analysis_file": "analysis/xLUQOqjudtA.json"
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

# Verify rendered UI with screenshots and scoped visual comparisons

## What

Verify rendered UI with screenshots and scoped visual comparisons

A replay makes the completed UI state inspectable rather than accepting a teacher/doer’s pass declaration.

## Evidence

> okay, like which problems truly needed that human or not.
> — 06:41 [^9arM9b7JgOo]

> very well because they're just not simply trained on scientific images and
> — 17:32 [^XLEYtv3cMlw]

Source analysis [^_KFbT6eph5A]; no independently matched timestamped quote published.

> sort of watch the entire replay to see if that is accurate. Uh, it was able to
> — 17:11 [^p7gaxmCUiIU]

Source analysis [^r0AG44qYKsI]; no independently matched timestamped quote published.

> producing videos and screenshots. CI/CD still use it obviously. Uh and then
> — 11:41 [^tUPPVhBBcoM]

Source analysis [^v3u8xc0zLec]; no independently matched timestamped quote published.

> based harness. Uh Things like flickering are really hard to catch in a verif- in
> — 19:13 [^wpOA-UXynoM]

> it against snapshots until it's pixel perfect. And then we have separate
> — 10:54 [^xLUQOqjudtA]

## How to apply (generic)

Test the smallest supported intervention on representative tasks. Compare against a baseline, check correctness and failure cases, and retain a rollback before wider use.

## Expected effect

- **Cost:** Catch failures before expensive review and reruns
- **Speed:** Faster scoped feedback and shorter CI critical paths
- **Quality:** Stronger behavioral and negative-case coverage
- **Reliability:** Repeatable regression and recovery evidence
- **Certainty:** Expected directions, not measured local gains; savings across clusters overlap and must not be added.

[^9arM9b7JgOo]: [Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat](https://www.youtube.com/watch?v=9arM9b7JgOo); publication: 2026-07-11T14:45:18Z; analysis: `analysis/9arM9b7JgOo.json`.
[^XLEYtv3cMlw]: [Autonomous Agents for Scientific Tasks - Sina Shahandeh, Radicait](https://www.youtube.com/watch?v=XLEYtv3cMlw); publication: 2026-07-18T23:30:06Z; analysis: `analysis/XLEYtv3cMlw.json`.
[^_KFbT6eph5A]: [Using AI to Build an Infinite Game: Jeff Schomay](https://www.youtube.com/watch?v=_KFbT6eph5A); publication: 2024-02-01T17:41:28Z; analysis: `analysis/_KFbT6eph5A.json`.
[^p7gaxmCUiIU]: [Hill-Climbing Skills: Improve Agents Without Changing the Model — Shubhankar Srivastava, Browserbase](https://www.youtube.com/watch?v=p7gaxmCUiIU); publication: 2026-10-11T21:30:05Z; analysis: `analysis/p7gaxmCUiIU.json`.
[^r0AG44qYKsI]: [This video was edited with AI agent. But how?](https://www.youtube.com/watch?v=r0AG44qYKsI); publication: 2025-02-22T20:00:06Z; analysis: `analysis/r0AG44qYKsI.json`.
[^tUPPVhBBcoM]: [Software Engineering Is Becoming Factory Engineering — Zach Lloyd, Warp](https://www.youtube.com/watch?v=tUPPVhBBcoM); publication: 2026-09-27T17:30:36Z; analysis: `analysis/tUPPVhBBcoM.json`.
[^v3u8xc0zLec]: [Proactive Agents – Kath Korevec, Google Labs](https://www.youtube.com/watch?v=v3u8xc0zLec); publication: 2025-12-13T04:44:20Z; analysis: `analysis/v3u8xc0zLec.json`.
[^wpOA-UXynoM]: [How Forward Deployed Engineering is done at Factory — Eno Reyes](https://www.youtube.com/watch?v=wpOA-UXynoM); publication: 2026-07-28T22:00:06Z; analysis: `analysis/wpOA-UXynoM.json`.
[^xLUQOqjudtA]: [Tolan: Voice-First AI Companion — Paula Dozsa, Tolan](https://www.youtube.com/watch?v=xLUQOqjudtA); publication: 2026-09-15T14:30:14Z; analysis: `analysis/xLUQOqjudtA.json`.
