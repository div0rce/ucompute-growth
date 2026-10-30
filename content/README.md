# Content pipeline

Stages: `drafts/` (anything, unlinted) → `ready/` (lint passes with `--strict`, claims declared, channel intent set) → `published/` (moved on publication with URL and date; `published/INDEX.md` lists every public URL).

Front matter for every piece:
```
---
id: 2026-10-30-pairing-explainer
title: ...
type: engineering-note | tutorial | explainer | comparison | search-page | community-answer | release-communication
audience: (an audience id from research/AUDIENCES.md)
channel_intent: (channel names from channels/REGISTRY.md; "website-handoff" when the Website workstream must publish it)
claims: [run-local, mesh-pair-choose]
status: draft | ready | published | withdrawn
sources: (URLs or evidence paths every factual statement rests on)
---
```
Rules: every product statement maps to a claim id and keeps its qualifier; numbers follow `claims/REGISTRY.md` → Numbers; no identity leaks; original diagrams only (ASCII or SVG drawn from the implementation, never decorative stock); cite external sources by URL; a comparison quotes a competitor's own documentation, never a third-party security claim about them; say "development build, October 2026" when describing behaviour.

`CALENDAR.md` is the distribution calendar: what goes where, when, and the evidence state it waits on.
