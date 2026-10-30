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
