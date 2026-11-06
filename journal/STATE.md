# State

Updated: 2026-11-06 13:30 UTC (cloud daily: checks only, nothing published; the local session of the same day set the state below)

## Where things stand
- **Function:** UCompute Growth & Community. Charter `charter/CHARTER.md`, voice `charter/VOICE.md` (binding on everything public), recovery `runbook/RUNBOOK.md`.
- **Product truth:** development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031). Snapshot still 2026-10-23b draft 3. P1's first generating run passed on 2026-11-06 (D-033), partial, not claimable: F-03-01 is IMPLEMENTED_UNVERIFIED, and the Core Lab's scoring and P1.4 to P1.8 are owed. Linux stays planned.
- **Channels:** AUTHORIZED: GitHub organization (profile, notes, Pages root) and Bluesky `@ucompute.org`. X is built and off (`distribution/X-INTEGRATION.md`, OWNER-ASKS 14). Assessment in `channels/REGISTRY.md`.
- **Public:** 11 notes at https://ucompute.github.io/notes/. Bluesky queue `content/ready/bluesky-queue.md`: dates are floors, not appointments. Live so far: five posts, the last a correction under post 4 (2026-11-06). New bio live. Bot label off by the owner's instruction of 2026-11-06, and the job keeps it off. `bluesky-post` is enabled again.
- **Funnel:** Discovery 0, Understanding 0, Qualified interest 0; Installation onward not reachable. Latest checkpoint: `analytics/weekly/2026-11-06-transition-checkpoint.md`.
- **Held:** `content/drafts/split-run-held.md`, refreshed after the lab scored run-0820. Only the owner releases these.
- **Experiments:** X-07 arm A evaluated negative, arm B running. X-03, X-05, X-06 running. X-01, X-02, X-04 waiting.
- **Reported by Program Control, 2026-11-06:** the owner chose security@ucompute.org but it is untested, so keep hello@ucompute.org on every page until Program Control says Engineering has recorded the end-to-end test. The owner also approved in principle preparing a 3-5 person developer cohort. DevEx defines it; Growth sends no invitations and does no recruiting or outreach for it until that gate opens, and no public text mentions it.
- **Coordination:** Program Control reads this repository. Open handoffs: Website link and claim review, docs pages (HO-005). If a P1 run is active, files only.

## Routine ids
- evidence sync: `trig_01FzksEYN8XDYZQiWZ1KHFnK` (12:30 UTC, claude-haiku-5-5, Bash only; the only routine with Engineering and Website sources; keep it without web tools)
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (13:00 UTC, idempotent)
- daily retry: `trig_01Hr6VmMMhkG7RQZxahnrmRN` (21:00 UTC)
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (Mondays 14:00 UTC)
- Health 2026-11-06: all ran on schedule through 11-06 (cloud daily 11-06 ran, access PUSH_OK; no evidence commit after 08:29 UTC; the 12:30 sync commits only real changes, and its run was not checked from here). Actions: `claims-lint`, `public-measurement`, `bluesky-post` active; `x-post` off.
- **Bluesky caution:** the cloud environment holds `BSKY_HANDLE` and `BSKY_APP_PASSWORD`. Never run `scripts/bsky_post.py` without `--selftest` in a routine; posting belongs to the Actions job.
- Hosts blocked from the cloud vary by run (github.com HTML, docs.jan.ai, lmstudio.ai, ucompute.github.io); use git clone and raw.githubusercontent.com.

## Next actions (ranked)
1. **2026-11-07 daily: read X-03 (7-day)** from the Actions files and record it in `experiments/BACKLOG.md`, null or not. This is the first pre-registered read. No new note is due; the 11-07 note went out on 2026-11-06, and post 14 links it later.
2. **2026-11-07 onward:** confirm the Actions job posted the new pin (post 10). Queue dates are floors. A new real development goes to the top, and a day with nothing due is fine.
3. **2026-11-09 weekly (W46):** checkpoint in the required five headings; reread the week's posts against `charter/VOICE.md`; first `research/ECOSYSTEM.md` (research only, no outreach).
4. **2026-11-13 and 2026-11-20: X-07 reads** (runbook section 7, each with a control). **2026-11-16: X-06 final read.** 2026-11-30: X-03 30-day read.
5. **Watch `evidence/upstream/`:** when F-03-01 turns VERIFIED and `claims.json` changes, update `mesh-pair-choose` and `planned`, every note that quotes them, and consider `content/drafts/split-run-held.md`. Until then those posts stay held unless the owner releases them.
6. **Look for new real material** in `engineering-PROGRESS.md` and the evidence mirror. Add `obs-` entries only from committed records.
7. **Owner decisions pending:** split-run release (`content/drafts/split-run-held.md`), OWNER-ASKS 12, 13, 14, 3, 5, 9. Don't re-ask.
8. **Local sessions only:** `./scripts/baseline.sh` for traffic; Bing and Brave readings by hand; push changes to the Pages root or `.github` (the cloud App reaches only `ucompute/notes`).
0. Routine health: if two consecutive UTC days pass with no "cloud daily" entry in `journal/LOG.md`, record a failure here and in OWNER-ASKS with the run log's error.
