# Distribution calendar

Two channels are AUTHORIZED (`channels/REGISTRY.md`): the GitHub organization's notes site and Bluesky `@ucompute.org`. This file plans experiments and reads, not posts: nothing here is a quota, and caps are ceilings (`charter/VOICE.md`). Everything else stays readiness-only. The table below is the historical readiness record; the current week's plan is the last section.

| Target state | Piece (content/ id) | Audience | Waits on | Ready by |
|---|---|---|---|---|
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-10-30-pairing-explainer` (how two devices pair: code, keys, revocation) | multi-device developers; OSS infra | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-10-31-loopback-rpc-vs-authenticated-transport` (llama.cpp's RPC backend is not a network transport, and what UCompute does instead) | local-AI developers; OSS infra | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-11-01-memory-fit-explainer` (how UCompute estimates whether a GGUF fits before loading) | local-AI developers; AI app builders | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-11-02-openai-client-base-url` (point the official OpenAI clients at a local server) | AI app builders | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-10-30-what-the-audit-log-records` (what the audit log records and never records) | multi-device developers; homelab; OSS infra | nothing: fact-checked, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-11-03-what-0000-exposes` (what binding a local AI server to 0.0.0.0 exposes; OS-by-OS self-check) | local-AI developers; multi-device developers | nothing: self fact-checked, lint clean, in `content/ready/`; Cisco/Elastic/LM Studio quotes to be re-read by a local session (hosts blocked from the cloud) | done |
| **READY 2026-10-30** (internal bank; used only in AUTHORIZED channels) | `community-answers.md` (25 answers in 9 themes, quotations traced to `research/raw/`) | all | nothing: lint clean, reviewed | done |
| Drafted, held | Source-publication announcement | all | owner publishes the source (engineering B-007) | draft within 24 h of the decision |
| Drafted, held | Public release communication | all | website LAUNCH.md gates | draft within 24 h |
| Weekly | `analytics/weekly/` report | owner (internal) | — | every Monday |

## Week 2026-W45 (2026-11-02 to 2026-11-08), set by the 2026-W44 weekly review
Dates slipped because the founding session's draft review was interrupted. One piece reviewed and promoted per daily run, in the order above; one research lens per daily run after that. Publication remains zero until a channel is AUTHORIZED.

## Published 2026-10-30 23:54 UTC
The six ready notes and the organization profile are public (`content/published/INDEX.md`). Bluesky posts in `content/ready/bluesky-first-posts.md` now have live link targets and wait only for the account (owner).
- 2026-10-31 00:52 UTC: published `2026-10-31-verify-a-gguf-download` (search query group 7: verifying model downloads). Next in the queue (`research/SEARCH.md` §4, `research/BARRIERS.md` §4.1): "Use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi"; "How UCompute compares with NVIDIA PAIR, fact by fact"; "Windows firewall consent: what UCompute asks and what the rule covers". One a day at most, each with the independent fact-check.
- 2026-10-31 13:40 UTC (cloud daily): `2026-11-04-other-computer-without-open-port` ("Running a prompt on your other computer without opening a port to everyone on the Wi-Fi", SEARCH.md rank 2) READY after the independent fact-check. **Queued for the notes site**: the cloud push to `ucompute/notes` was refused (403, OWNER-ASKS 10); the next local session or the first cloud run with PUSH_OK publishes it. Next in the queue: "How UCompute compares with NVIDIA PAIR, fact by fact" (short-code pairing is parity, see OPPORTUNITIES 2026-10-31); "Windows firewall consent: what UCompute asks and what the rule covers".
- 2026-11-01 13:40 UTC (cloud daily): `2026-11-05-ucompute-and-nvidia-pair` ("UCompute Mesh and NVIDIA PAIR, fact by fact") READY after the independent fact-check (14 findings applied). **Queued** behind `2026-11-04-other-computer-without-open-port` (notes push still 403, OWNER-ASKS 10). Publish order when access works: 11-04 piece first, PAIR piece the next day (one note a day). Next to write: "Windows firewall consent: what UCompute asks and what the rule covers".
- 2026-11-02 13:30 UTC (cloud daily): `2026-11-06-windows-firewall-what-the-rule-covers` ("Windows firewall prompts for local AI servers: what a rule covers, and how to read yours", BARRIERS.md §6 item 6) READY after the independent fact-check (18 findings, 2 major, all applied); `publish_after: 2026-11-04`. Publish order: PAIR comparison 2026-11-03, firewall note 2026-11-04 (cloud push to `ucompute/notes` is PUSH_OK). Bluesky post 6 (links the other-computer note) queued. Next to write: a research lens or "What 'verified' means: SHA-256 before the engine opens the file" only if the GGUF-download note does not already cover it; otherwise BARRIERS.md §9 "what happens when a paired device cannot be reached" once the evidence answers it.

## Week 2026-W45 plan (2026-11-02 to 2026-11-08), set by the W45 weekly review
| Date (UTC) | Notes site | Bluesky (Actions job, 15:37 UTC, cap-dependent) | Other |
|---|---|---|---|
| Mon 11-02 | — (note 8 went out 01:55) | none expected (post 1 went out 03:02, 1/day cap) | weekly report |
| Tue 11-03 | **DONE 13:16 UTC** `2026-11-05-ucompute-and-nvidia-pair` (PAIR README/SECURITY.md re-read; 24 quotes matched, one stray period fixed) | post 2 (Actions 15:37) | Bluesky post 7 queued for the PAIR note |
| Wed 11-04 | **DONE 13:20 UTC** `2026-11-06-windows-firewall-what-the-rule-covers` (notes commit a901fb5; `build_notes.py` TYPES gained `tutorial`, which had silently excluded it) | next queued post (post 3) | Bluesky post 8 queued for the firewall note |
| Thu 11-05 | none scheduled | next queued post (likely the 4th in 7 days; then the weekly cap holds until 11-09) | **DONE**: `2026-11-07-shared-api-key-is-not-device-trust` READY (independent fact-check, 15 findings applied), `publish_after` 2026-11-07 |
| Fri 11-06 – Sun 11-08 | at most one more note in the week (new cadence: max three new notes a week after 11-04) | cap holds | **Sat 11-07: X-03 7-day read**; 11-07 run publishes the shared-API-key note (W45 new note 1 of 3) and queues its Bluesky post |

Cadence change (W45 strategy): ten notes are live or scheduled by 11-04 with zero measured audience; from 11-05 the daily runs write at most three new notes a week and spend the freed capacity on accuracy maintenance (llama.cpp advisory check for the RPC note), a Bluesky post for every published note, and the measurement asks.

## Campaign: "Can a developer find this?" (2026-11-06 to 2026-11-20)
Set by the transition checkpoint. Goal: move Discovery off zero. Measured by X-07, not by what is published.

| Date (UTC) | Notes site | Bluesky | Experiments and research |
|---|---|---|---|
| Fri 11-06 | **DONE** rebuild with descriptions; root site live; shared-API-key note published | correction posted | X-07 arm A evaluated, arm B started |
| Sat 11-07 | none due | new pinned post | **X-03 7-day read** |
| Mon 11-09 | none required | queue dates are floors; expect two or three posts a week | W46 checkpoint; first `research/ECOSYSTEM.md` |
| Fri 11-13 | — | — | **X-07 T+7 read** |
| Mon 11-16 | — | — | **X-06 final read**, W47 checkpoint |
| Fri 11-20 | — | — | **X-07 T+14 read and decision** |
