# State

Updated: 2026-10-30 23:50 UTC (founding session, day one closed)

## Where things stand
- Workspace: private repo `ucompute-growth`, pushed. Charter, runbook, claims registry (20 claims incl. `audit-detail`) + lint, channel registry, owner asks, pipeline, experiments, analytics baseline, handoffs.
- Evidence mirror: `evidence/upstream/` at engineering 29c0c8e (wp04/fix-pass), website ce71dc1 (stage-snapshot), snapshot 2026-10-23b draft 3.
- Product truth: development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031); no public release, source, channel or cohort.
- Research: COMPLETE for the founding milestone. Nine raw lenses in `research/raw/`; synthesis in `research/POSITIONING.md`, `AUDIENCES.md`, `COMPETITORS.md` (cloud re-check), `SEARCH.md`, `BARRIERS.md`; channel database `distribution/COMMUNITIES.md`. Positioning: default-deny off-device policy + prompt-free audit log lead; whole-request is a limitation statement; revoke is parity. Primary audience multi-device developers; secondary local-AI developers.
- Content: FIVE pieces reviewed and READY in `content/ready/` (pairing, RPC backend, memory fit, OpenAI base URL, audit log); `content/community-answers.md` READY (25 answers). All six aligned with `research/POSITIONING.md`. The website handoff lists the five pieces.
- Channels: none AUTHORIZED. The GitHub organization `ucompute` exists (owner, 2026-10-30 16:56 UTC; this account is admin) and awaits the owner's grant line (OWNER-ASKS 3). First accounts to ask for: Bluesky (`@ucompute.org` handle), Fosstodon, dev.to organization (all need the project mailbox, OWNER-ASKS 2).
- Measurement from the cloud is blocked (OWNER-ASKS 8); local `scripts/baseline.sh` works. Routines share the account's usage limit: both 2026-10-30 daily slots were rejected while the founding session ran.
- Scheduling: three cloud routines (ids below). Local evidence-sync task blocked by permission (OWNER-ASKS 7); local sessions run `./scripts/sync_evidence.sh` by hand.

## Routine ids
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (cron 0 13 * * * UTC, claude-opus-5-5, source div0rce/ucompute-growth, no connectors, idempotent) — https://claude.ai/code/routines/trig_018xkiTyQqoEVCLHrVgXYwWz
- daily retry: `trig_01Hr6VmMMhkG7RQZxahnrmRN` (cron 0 21 * * * UTC, same prompt) — https://claude.ai/code/routines/trig_01Hr6VmMMhkG7RQZxahnrmRN
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (cron 0 14 * * 1 UTC) — https://claude.ai/code/routines/trig_01Xxy1PgCyyTQAent7Ddfz2Q; verified end to end by a manual run on 2026-10-30 (W44 report).
- Health: no successful scheduled daily run yet (both 2026-10-30 slots rate-limited). First unattended test: 2026-10-31 13:07 UTC.

## Next actions (ranked, for the daily runs)
0. Routine health: if `journal/LOG.md` has no "cloud daily" entry by 2026-11-01 21:30 UTC, record a failure here and in OWNER-ASKS ("check the routines at https://claude.ai/code/routines"), with the run log's error.
1. Channel check every run: publish from `content/ready/` only when `channels/REGISTRY.md` shows an AUTHORIZED row quoting the owner's words. When the GitHub organization is granted: draft the organization profile README (disambiguation wording in `research/SEARCH.md` §5.4; claims-clean; lint) into `content/ready/`, then publish per the registry procedure.
2. Owner grants: when a grant line arrives (GitHub org, Bluesky, Fosstodon, dev.to), record it verbatim in `channels/REGISTRY.md`, then publish per the procedure. For the GitHub org, first draft the profile README (disambiguation wording in `research/SEARCH.md` §5.4).
3. Next pieces, one per run, from `research/SEARCH.md` §4 and `research/BARRIERS.md` §4.1, in this order: (a) "What binding a local AI server to 0.0.0.0 exposes, and a sixty-second self-check" (claims `local-only`, `transport`, `device-sees-prompt`; quote exposure counts with their scanner and filter, never as a UCompute comparison); (b) "What 'verified' means: SHA-256 before the engine opens the file" (`catalog-fit`, `engine`); (c) "Windows: the firewall consent step" (`windows-firewall`, `platforms`). Each: draft → fact-check against `evidence/upstream/` and the engineering sources named in the registry → lint → ready.
4. Handoffs written 2026-10-30 (engineering snapshot rows; website docs pages). Next: watch `evidence/upstream/` for answers; when a snapshot answers an item, add the claim to the registry and revise the affected pieces.
5. Experiments: X-04 variants are revised; X-02 and X-04 stay blocked on a channel. Record in `experiments/BACKLOG.md` anything learned.
6. Monitoring into `pipeline/OPPORTUNITIES.md`; measurement ("not measured" from the cloud until OWNER-ASKS 8).
7. Watch `evidence/upstream/` for the final capability snapshot and the Windows post-fix run (local sessions sync; cloud runs use the mirror).
8. Held drafts: source-publication announcement and release communication (only when the gates move).
9. Weekly report `analytics/weekly/2026-W45.md` on Monday 2026-11-02 14:05 UTC.
