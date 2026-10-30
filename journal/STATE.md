# State

Updated: 2026-10-30 11:40 UTC (founding session, resumed)

## Where things stand
- Workspace: private repo `ucompute-growth`, pushed. Charter, runbook, claims registry + lint, channel registry, owner asks, pipeline, experiments, analytics baseline exist.
- Evidence mirror: `evidence/upstream/` at engineering 29c0c8e (wp04/fix-pass), website ce71dc1 (stage-snapshot), snapshot 2026-10-23b draft 3.
- Product truth: development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031); no public release, source, channel or cohort.
- Content: four pieces REVIEWED and READY in `content/ready/` (2026-10-30); the website handoff lists them.
- Channels: none AUTHORIZED. Publication path today = Website handoff (`handoffs/2026-10-30-website-engineering-notes.md`).
- Weekly report: `analytics/weekly/2026-W44.md` (first report; strategy change: lead with default-deny + prompt-free audit; revoke is parity with NVIDIA PAIR, not "whole request on one device"). Competitor facts consolidated in `research/COMPETITORS.md`.
- Measurement from the cloud is blocked (ucompute.org outside the environment's allowed domains; public repo outside GitHub scope): OWNER-ASKS 8. Cloud runs write "not measured", never a guess.
- Lint: strict mode now exempts `INDEX.md`/`README.md` from the front-matter requirement (still pattern-checked); `content/ready content/published --strict` passes.
- Research: RUNNING AGAIN in the founding session (resumed 11:01 UTC; expect `research/POSITIONING.md`, `AUDIENCES.md`, `SEARCH.md`, `BARRIERS.md`, `distribution/COMMUNITIES.md` and the five missing raw lenses by about 13:00 UTC). Earlier note kept for history: INTERRUPTED (usage limit, 2026-10-30 06:10 UTC). 4 of 9 lens reports landed (the founding note said 3; `audience-ai-app-builders` also exists) in `research/raw/` (local-AI developers, multi-device developers, competitors); 5 lenses (`channels-platform-rules`, `adoption-barriers`, `search-demand`, `audience-homelab-selfhosting`, `audience-oss-infra-and-researchers`), the adversarial verification, `research/POSITIONING.md`, `AUDIENCES.md`, `SEARCH.md`, `BARRIERS.md` and `distribution/COMMUNITIES.md` do not exist yet. The workflow scripts are saved in `scripts/workflows/research.js` and `draft-review.js`; a local Claude Code session re-runs them with the Workflow tool (resume ids: research wf_fc367b96-c01, review wf_c2a9b28e-210). A cloud daily run without the Workflow tool does the same work directly: one lens per run from the LENSES list in `scripts/workflows/research.js`, written to `research/raw/<key>.md`, then the synthesis files once all nine exist.
- Scheduling: two cloud routines created 2026-10-30 (ids below). Local evidence-sync task: blocked by permission (OWNER-ASKS 7).

## Routine ids
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (cron 0 13 * * * UTC, model claude-opus-5-5, source div0rce/ucompute-growth, no connectors) — https://claude.ai/code/routines/trig_018xkiTyQqoEVCLHrVgXYwWz
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (cron 0 14 * * 1 UTC, same config) — https://claude.ai/code/routines/trig_01Xxy1PgCyyTQAent7Ddfz2Q
- first runs: daily 2026-10-30 13:06 UTC, weekly 2026-11-02 14:05 UTC; verify with `RemoteTrigger list_runs` or the routine page, then record in LOG.md

## Next actions (ranked, for the daily runs)
0. **Today (2026-10-30) only, cloud daily:** the founding session is still running the research workflow and will commit the synthesis files; do NOT start a research lens or rewrite `research/*` today (it would collide). Do instead: (a) first version of `content/community-answers.md` from the four raw research files, each answer with claim ids, strict lint; (b) monitoring into `pipeline/OPPORTUNITIES.md`; (c) measurement (expect "not measured" until OWNER-ASKS 8); (d) log and push.
1. From 2026-10-31: routine health check (a "cloud daily" entry per day in LOG.md; a missing one for 2 days is a failure to record and to put in OWNER-ASKS).
2. Channel check every run: publish from `content/ready/` only when `channels/REGISTRY.md` shows an AUTHORIZED row with the owner's words.
3. If the research synthesis exists (`research/POSITIONING.md`), re-read the four ready pieces against it and against `research/COMPETITORS.md` §Implications; adjust leads where they contradict (default-deny and prompt-free audit lead; revoke is parity; "whole request on one device" is a limitation statement), keep the lint clean, log the edits.
4. If `research/POSITIONING.md` does not exist by 2026-11-01, run the missing lenses yourself, one per run, in the order `channels-platform-rules` → `adoption-barriers` → `search-demand` → `audience-homelab-selfhosting` → `audience-oss-infra-and-researchers` (prompts in `scripts/workflows/research.js`), then the synthesis files.
5. Next pieces after community answers (one per run, research-led): a search page per cluster in `research/SEARCH.md`; a Windows firewall consent explainer (claim `windows-firewall`); a "what the audit log records" note (claim `audit`).
6. Watch `evidence/upstream/` for the final capability snapshot and the Windows post-fix run (local sessions sync; cloud runs use the mirror).
7. Held drafts: source-publication announcement and release communication (only when the gates move).
8. Weekly report `analytics/weekly/2026-W45.md` on Monday 2026-11-02 (the scheduled weekly fire).
