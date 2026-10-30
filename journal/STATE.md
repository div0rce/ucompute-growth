# State

Updated: 2026-10-30 11:55 UTC (founding session, resumed again)

## Where things stand
- Workspace: private repo `ucompute-growth`, pushed. Charter, runbook, claims registry + lint, channel registry, owner asks, pipeline, experiments, analytics baseline exist.
- Evidence mirror: `evidence/upstream/` at engineering 29c0c8e (wp04/fix-pass), website ce71dc1 (stage-snapshot), snapshot 2026-10-23b draft 3.
- Product truth: development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031); no public release, source, channel or cohort.
- Content: four pieces REVIEWED and READY in `content/ready/` (2026-10-30); the website handoff lists them.
- Channels: none AUTHORIZED. Publication path today = Website handoff (`handoffs/2026-10-30-website-engineering-notes.md`).
- Weekly report: `analytics/weekly/2026-W44.md` (first report; strategy change: lead with default-deny + prompt-free audit; revoke is parity with NVIDIA PAIR, not "whole request on one device"). Competitor facts consolidated in `research/COMPETITORS.md`.
- Measurement from the cloud is blocked (ucompute.org outside the environment's allowed domains; public repo outside GitHub scope): OWNER-ASKS 8. Cloud runs write "not measured", never a guess.
- Lint: strict mode now exempts `INDEX.md`/`README.md` from the front-matter requirement (still pattern-checked); `content/ready content/published --strict` passes.
- Research: INTERRUPTED a second time (usage limit, 2026-10-30 11:50 UTC). Raw lens reports now in `research/raw/`: local-AI developers, multi-device developers, AI app builders, homelab/self-hosting, OSS infra and researchers, competitors (plus the cloud re-check). Still missing: `channels-platform-rules`, `search-demand`, `adoption-barriers`, the adversarial verification, and the synthesis files `research/POSITIONING.md`, `AUDIENCES.md`, `SEARCH.md`, `BARRIERS.md`, `distribution/COMMUNITIES.md`. A local session resumes with the Workflow tool (`scripts/workflows/research.js`, resume id wf_fc367b96-c01); the cloud daily does the same work directly, one lens per run, then the synthesis.
- Scheduling: two cloud routines created 2026-10-30 (ids below). Local evidence-sync task: blocked by permission (OWNER-ASKS 7).

## Routine ids
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (cron 0 13 * * * UTC, model claude-opus-5-5, source div0rce/ucompute-growth, no connectors) — https://claude.ai/code/routines/trig_018xkiTyQqoEVCLHrVgXYwWz
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (cron 0 14 * * 1 UTC, same config) — https://claude.ai/code/routines/trig_01Xxy1PgCyyTQAent7Ddfz2Q
- first runs: daily 2026-10-30 13:06 UTC, weekly 2026-11-02 14:05 UTC; verify with `RemoteTrigger list_runs` or the routine page, then record in LOG.md

## Next actions (ranked, for the daily runs)
0. **Cloud daily, today (2026-10-30) only:** the founding session resumed at 11:55 UTC and is finishing the research (three lenses, synthesis files, `distribution/COMMUNITIES.md`) and `content/community-answers.md` itself; do NOT write under `research/`, `distribution/` or `content/` today. Do: monitoring into `pipeline/OPPORTUNITIES.md`; measurement ("not measured" until OWNER-ASKS 8); routine-health note; log and push. From 2026-10-31 the normal list below applies.
1. From 2026-10-31: routine health check (a "cloud daily" entry per day in LOG.md; a missing one for 2 days is a failure to record and to put in OWNER-ASKS).
2. Channel check every run: publish from `content/ready/` only when `channels/REGISTRY.md` shows an AUTHORIZED row with the owner's words.
3. If the research synthesis exists (`research/POSITIONING.md`), re-read the four ready pieces against it and against `research/COMPETITORS.md` §Implications; adjust leads where they contradict (default-deny and prompt-free audit lead; revoke is parity; "whole request on one device" is a limitation statement), keep the lint clean, log the edits.
4. (merged into 0)
5. Next pieces after community answers (one per run, research-led): a search page per cluster in `research/SEARCH.md`; a Windows firewall consent explainer (claim `windows-firewall`); a "what the audit log records" note (claim `audit`).
6. Watch `evidence/upstream/` for the final capability snapshot and the Windows post-fix run (local sessions sync; cloud runs use the mirror).
7. Held drafts: source-publication announcement and release communication (only when the gates move).
8. Weekly report `analytics/weekly/2026-W45.md` on Monday 2026-11-02 (the scheduled weekly fire).
