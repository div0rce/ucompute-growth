# Activity and decision log

Append-only, newest at the bottom. Each entry: date (UTC), who (local session / cloud daily / cloud weekly / evidence-sync), what was done, evidence, decisions, failures.

## 2026-10-30 — local founding session
- Inspected environment: GitHub authenticated (repo scope), no scheduled tasks, no UCompute-branded accounts, live site = frozen prelaunch page with one URL and no analytics, public repo holds LICENSE + superseded handoff. Evidence read read-only from engineering (snapshot 2026-10-23b draft 3, DECISIONS D-019..D-031, BLOCKERS, competitive matrix, research gaps), Core Lab (README, AUDIT) and Website (README, DEPLOYMENT, LAUNCH, claims.json).
- Created private repository `ucompute-growth`; wrote CLAUDE.md, charter, runbook, claims registry (19 claims, 102 prohibited patterns, 21 identity patterns) with lint and self-test, channel registry, owner asks, pipeline, experiment backlog, analytics definitions, two handoffs.
- Baseline measured (`analytics/measurements/2026-10-30.json`).
- Launched the research workflow (9 lenses, adversarial verification, synthesis, critic) writing to `research/`.
- **Failure:** creating the local scheduled task `ucompute-growth-evidence-sync` was refused by the permission classifier (`mcp__scheduled-tasks__create_scheduled_task` denied). Recorded as owner ask 7; not retried. Cloud routines are the primary mechanism; local sessions run `scripts/sync_evidence.sh` by hand.
- **Decision:** no public channel is authorized today; the pipeline targets readiness, and the first publication path is a Website handoff (engineering-notes proposal).
- Cloud routines created through the routines API: daily `trig_018xkiTyQqoEVCLHrVgXYwWz` (13:00 UTC), weekly `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (Mondays 14:00 UTC); model claude-opus-5-5 (chosen over the default for claim accuracy); auto-attached connectors (Airtable, Higgsfield, Docs, Remote) removed for least privilege. First daily run expected 2026-10-30 13:06 UTC.
- 06:10 UTC: session usage limit reached. Both background workflows stopped. Saved: 3 of 9 research lens reports (`research/raw/`), four unreviewed drafts, the workflow scripts (`scripts/workflows/`). Not done: six research lenses, claim verification, synthesis files, communities database, draft review, community-answers bank. Next actions re-ranked in STATE.md; the cloud daily run (first fire 2026-10-30 13:06 UTC) picks them up.

## 2026-10-30 — cloud weekly (2026-W44)
- Fired Friday 2026-10-30 11:00 UTC (recorded schedule: Mondays 14:00 UTC; mismatch noted in OWNER-ASKS 8). Recovered from STATE/LOG/OWNER-ASKS; `git pull` already up to date.
- Wrote `analytics/weekly/2026-W44.md` (first weekly report). Published: nothing, no channel authorized. No previous week to compare.
- **Failure (measurement):** `curl https://ucompute.org/` → `curl: (56) CONNECT tunnel failed, response 403`; WebFetch → `getaddrinfo ENOTFOUND ucompute.org` (host outside the routine environment's allowed domains). Public repository stats unreadable: session GitHub scope is `ucompute-growth` only; `gh api` → HTTP 403 "GitHub access to this repository is not enabled for this session". No measurement file written for this run; nothing estimated. Added OWNER-ASKS 8.
- Competitor refresh from primary sources (`research/COMPETITORS.md`, new): PAIR 1.0.0 (13 Oct), first release 26 Aug (corrects unverified 3 Sep); PAIR README now documents node removal → revoke downgraded from differentiated to parity; Mesh LLM v0.78.1 with cert rotation and expiring tokens; Ollama v0.40.13, llama.cpp b12002, LocalAI v4.12.1, Jan v0.8.8 (repo now `janhq/jan`), exo v1.0.71. LM Link unverifiable this run (lmstudio.ai, tailscale.com ENOTFOUND).
- **Decision (strategy):** lead with default-deny off-device policy and the prompt-free audit log; "whole request on one device" becomes a limitation statement; revoke presented as part of the trust lifecycle, never as unique. X-04 variants to be revised. All experiments retained, none abandoned.
- Channels: no status change (no grant; platform-rules lens not yet run). `distribution/COMMUNITIES.md`, `research/POSITIONING.md`, `research/AUDIENCES.md` still unwritten (5 of 9 research lenses missing; 4 exist, not 3 as previously logged).
- Lint: strict mode flagged `content/published/INDEX.md` (no front matter); exempted INDEX.md/README.md from the front-matter requirement only (still pattern-checked). Strict lint and self-test pass.
- Routine health: the daily routine's first fire (13:06 UTC today) is after this run; no "cloud daily" entry yet is expected, not a failure.
- Calendar re-dated for W45 (draft review slipped); opportunities log gained three dated entries.
