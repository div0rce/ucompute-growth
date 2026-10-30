# State

Updated: 2026-10-30 (founding session, in progress)

## Where things stand
- Workspace: private repo `ucompute-growth`, pushed. Charter, runbook, claims registry + lint, channel registry, owner asks, pipeline, experiments, analytics baseline exist.
- Evidence mirror: `evidence/upstream/` at engineering 29c0c8e (wp04/fix-pass), website ce71dc1 (stage-snapshot), snapshot 2026-10-23b draft 3.
- Product truth: development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031); no public release, source, channel or cohort.
- Channels: none AUTHORIZED. Publication path today = Website handoff (`handoffs/2026-10-30-website-engineering-notes.md`).
- Research: workflow running; outputs land in `research/` and `distribution/COMMUNITIES.md`.
- Scheduling: two cloud routines created 2026-10-30 (ids below). Local evidence-sync task: blocked by permission (OWNER-ASKS 7).

## Routine ids
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (cron 0 13 * * * UTC, model claude-opus-5-5, source div0rce/ucompute-growth, no connectors) — https://claude.ai/code/routines/trig_018xkiTyQqoEVCLHrVgXYwWz
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (cron 0 14 * * 1 UTC, same config) — https://claude.ai/code/routines/trig_01Xxy1PgCyyTQAent7Ddfz2Q
- first runs: daily 2026-10-30 13:06 UTC, weekly 2026-11-02 14:05 UTC; verify with `RemoteTrigger list_runs` or the routine page, then record in LOG.md

## Next actions (ranked)
1. Finish the research synthesis review; fix anything the critic flagged; commit.
2. Draft and lint the first three engineering notes (`content/CALENDAR.md`), move to `content/ready/`.
3. Write `content/community-answers.md` from the research (truthful answers to the recurring questions).
4. Weekly report skeleton for 2026-W44 on Monday 2026-11-02.
5. Watch `evidence/upstream/` for the final capability snapshot (draft 3 → final) and the Windows post-fix run; update claims when it lands.
6. Held drafts: source-publication announcement and release communication (write when the gates move, not before).
