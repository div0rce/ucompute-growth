# State

Updated: 2026-11-02 15:00 UTC (cloud weekly W45; report `analytics/weekly/2026-W45.md`)

## Where things stand
- Workspace: private repo `ucompute-growth`, pushed. Charter, runbook, claims registry (20 claims incl. `audit-detail`) + lint, channel registry, owner asks, pipeline, experiments, analytics baseline, handoffs.
- Evidence mirror: `evidence/upstream/` at engineering 29c0c8e (wp04/fix-pass), website ce71dc1 (stage-snapshot), snapshot 2026-10-23b draft 3.
- Product truth: development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031); no public release, source, channel or cohort.
- Research: COMPLETE for the founding milestone. Nine raw lenses in `research/raw/`; synthesis in `research/POSITIONING.md`, `AUDIENCES.md`, `COMPETITORS.md` (cloud re-check), `SEARCH.md`, `BARRIERS.md`; channel database `distribution/COMMUNITIES.md`. Positioning: default-deny off-device policy + prompt-free audit log lead; whole-request is a limitation statement; revoke is parity. Primary audience multi-device developers; secondary local-AI developers.
- Content (2026-11-02): eight notes published on the notes site; READY and scheduled: `2026-11-05-ucompute-and-nvidia-pair` (publish_after 2026-11-03) and `2026-11-06-windows-firewall-what-the-rule-covers` (publish_after 2026-11-04, fact-checked 2026-11-02). Historical: SIX pieces READY in `content/ready/` (pairing, RPC backend, memory fit, OpenAI base URL, audit log, and since the 2026-10-30 cloud daily the 0.0.0.0 exposure self-check `2026-11-03-what-0000-exposes`, self fact-checked; its Cisco, Elastic and LM Studio quotations were traced to `research/` by the founding session on 2026-10-30); `content/community-answers.md` READY (25 answers). All six aligned with `research/POSITIONING.md`. The website handoff lists the five pieces.
- Publish packages: `scripts/build_notes.py` (public notes repository), `content/ready/github-org-profile.md`, `content/ready/bluesky-first-posts.md`; one-step publish documented in `channels/REGISTRY.md`.
- **Published:** https://github.com/ucompute (profile), https://github.com/ucompute/notes (source) and the site https://ucompute.github.io/notes/ (six notes, sitemap, Atom feed; submitted to IndexNow, HTTP 200), 2026-10-30 23:54 UTC. Index: `content/published/INDEX.md`.
- Channels: GitHub organization AUTHORIZED (basis quoted in `channels/REGISTRY.md`); all others not yet. The GitHub organization `ucompute` exists (owner, 2026-10-30 16:56 UTC; this account is admin) and awaits the owner's grant line (OWNER-ASKS 3). First accounts to ask for: Bluesky (`@ucompute.org` handle), Fosstodon, dev.to organization (all need the project mailbox, OWNER-ASKS 2).
- Measurement: GitHub Actions `public-measurement` daily (site, public repo, org, name collisions, exact-match HN and Bluesky mentions); repository traffic only from local `scripts/baseline.sh`. Routines share the account's usage limit: both 2026-10-30 daily slots were rejected while the founding session ran.
- Scheduling: three cloud routines (ids below). Local evidence-sync task blocked by permission (OWNER-ASKS 7); local sessions run `./scripts/sync_evidence.sh` by hand.

## Routine ids
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (cron 0 13 * * * UTC, claude-opus-5-5, source div0rce/ucompute-growth, no connectors, idempotent) — https://claude.ai/code/routines/trig_018xkiTyQqoEVCLHrVgXYwWz
- daily retry: `trig_01Hr6VmMMhkG7RQZxahnrmRN` (cron 0 21 * * * UTC, same prompt) — https://claude.ai/code/routines/trig_01Hr6VmMMhkG7RQZxahnrmRN
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (cron 0 14 * * 1 UTC) — https://claude.ai/code/routines/trig_01Xxy1PgCyyTQAent7Ddfz2Q; verified end to end by a manual run on 2026-10-30 (W44 report).
- Health: first successful daily run 2026-10-30 ~23:45 UTC (pushed). Earlier 2026-10-30 slots were rate-limited. Next scheduled: 2026-10-31 13:07 UTC. Cloud sessions cannot reach ucompute.org, the public repo API, docs.ollama.com, lmstudio.ai, blogs.cisco.com or www.elastic.co; measurement no longer depends on that (GitHub Actions `public-measurement`, which also alerts the owner after 48 h without a cloud daily entry). For quotations from blocked hosts, use the research files that recorded them.

## Since the last rewrite
- 2026-10-31 00:52 UTC: seventh note live (https://ucompute.github.io/notes/2026-10-31-verify-a-gguf-download.html); claim `download-integrity` added; contact hello@ucompute.org on every note.
- 2026-11-01 cloud daily: ninth piece `2026-11-05-ucompute-and-nvidia-pair` ("UCompute Mesh and NVIDIA PAIR, fact by fact") READY after the independent fact-check (14 findings applied) and **queued** behind the eighth; access check still PUSH_DENIED (403). Routine health: daily ran on schedule (second clean scheduled run). No 2026-11-01 Actions measurement file yet at 13:40 UTC; next run confirms it landed.
- 2026-10-31 cloud daily: eighth piece `2026-11-04-other-computer-without-open-port` READY (independent fact-check applied) and **queued**: the cloud cannot push to `ucompute/notes` (PUSH_DENIED, 403, OWNER-ASKS 10). Routine health: daily ran on schedule today (first clean scheduled run).

- **Bluesky live** since 2026-11-02 03:02 UTC: @ucompute.org has the automation label and disclosure bio; post 1 is pinned; the `bluesky-post` Actions job posts one queued post a day (15:37 UTC, max 4 a week). When a note is published to the notes site, add a Bluesky post for it to `content/ready/bluesky-first-posts.md` (under 300 characters, claims-linted, link to the notes site page).

## Routine health (2026-11-02)
- Daily ran on schedule (13:30 UTC; third clean scheduled run). Cloud access to `ucompute/notes`: PUSH_OK. `public-measurement` scheduled runs land late (2026-11-01 at 13:34 UTC, not 06:17); judge a missing file only after 24 h.
- **Bluesky caution:** this cloud environment holds `BSKY_HANDLE`/`BSKY_APP_PASSWORD`. Never run `scripts/bsky_post.py` without `--selftest` (exact spelling) in a routine; posting belongs to the Actions job. See the 2026-11-02 cloud daily incident.

## Weekly W45 decisions (2026-11-02)
- Cadence: notes 2026-11-03 (PAIR) and 2026-11-04 (firewall) as scheduled; **from 2026-11-05 at most three new notes a week**. Every published note gets a Bluesky post in the queue the same day.
- Experiments: X-06 started (Bluesky discovery signal; reads 2026-11-16, 2026-12-02). X-02/X-04 deferred until Bluesky ≥ 50 followers (X-04 metric: likes+reposts+replies per post). X-01 blocked on measurement only (optional OWNER-ASKS 12: search console for the notes site).
- Channels: GitHub org and Bluesky stay AUTHORIZED; Fosstodon is the next account to request (OWNER-ASKS 3). fosstodon.org and dev.to unreachable from the cloud (ENOTFOUND).
- Routine health: daily entries on every day 10-30..11-02; healthy.

## Next actions (ranked, for the daily runs)
1. **2026-11-03: publish the PAIR comparison** (runbook 6; `build_notes.py` releases it by `publish_after`): first re-read PAIR's README and SECURITY.md via raw.githubusercontent.com and adjust quotes (the W45 competitor re-check in `research/COMPETITORS.md` lists what changed); then INDEX.md, the log, and a Bluesky post for it in `content/ready/bluesky-first-posts.md` (under 300 characters, lint clean).
2. **2026-11-04: publish the Windows firewall note** the same way, plus its Bluesky post.
3. **2026-11-05 onward: at most one new piece per run and three per week.** First check whether "What 'verified' means: SHA-256 before the engine opens the file" is already covered by the GGUF-download note; if so, pick from `research/BARRIERS.md` §4 or a research lens. Independent fact-check required.
4. **2026-11-07: read X-03** (7-day) from the Actions files; record in `experiments/BACKLOG.md`. Also confirm the `bluesky_account` block is in the daily file (X-06 baseline).
5. Measurement: confirm `analytics/measurements/2026-11-02.public.json` landed (late runs are normal); two missing days → failure and owner ask.
6. Local session only: llama.cpp advisories (OPPORTUNITIES, pruned summary) vs pinned b11609 → decide on a dated update to the RPC note.
7. Channel check every run: notes site and Bluesky are AUTHORIZED; everything else waits on OWNER-ASKS 3.
8. Handoffs: watch `evidence/upstream/` for answers. Candidate registry additions to request: pairing-code length; "pairing is separate from permission"; the Windows rule's exact scope (snapshot 3.3 row).
9. Held drafts: source-publication announcement and release communication (only when the gates move).
10. Next weekly: `analytics/weekly/2026-W46.md` on Monday 2026-11-09; re-check selfh.st 2026 survey results (not published as of 11-02).
0. Routine health: if two consecutive UTC days pass with no "cloud daily" entry in `journal/LOG.md`, record a failure here and in OWNER-ASKS ("check the routines at https://claude.ai/code/routines"), with the run log's error.
