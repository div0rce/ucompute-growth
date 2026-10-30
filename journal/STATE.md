# State

Updated: 2026-10-30 UTC (cloud weekly 2026-W44)

## Where things stand
- Workspace: private repo `ucompute-growth`, pushed. Charter, runbook, claims registry + lint, channel registry, owner asks, pipeline, experiments, analytics baseline exist.
- Evidence mirror: `evidence/upstream/` at engineering 29c0c8e (wp04/fix-pass), website ce71dc1 (stage-snapshot), snapshot 2026-10-23b draft 3.
- Product truth: development builds only; private alpha 0.1.1 candidate 2 behind access control (D-031); no public release, source, channel or cohort.
- Channels: none AUTHORIZED. Publication path today = Website handoff (`handoffs/2026-10-30-website-engineering-notes.md`).
- Weekly report: `analytics/weekly/2026-W44.md` (first report; strategy change: lead with default-deny + prompt-free audit; revoke is parity with NVIDIA PAIR, not "whole request on one device"). Competitor facts consolidated in `research/COMPETITORS.md`.
- Measurement from the cloud is blocked (ucompute.org outside the environment's allowed domains; public repo outside GitHub scope): OWNER-ASKS 8. Cloud runs write "not measured", never a guess.
- Lint: strict mode now exempts `INDEX.md`/`README.md` from the front-matter requirement (still pattern-checked); `content/ready content/published --strict` passes.
- Research: INTERRUPTED (usage limit, 2026-10-30 06:10 UTC). 4 of 9 lens reports landed (the founding note said 3; `audience-ai-app-builders` also exists) in `research/raw/` (local-AI developers, multi-device developers, competitors); 5 lenses (`channels-platform-rules`, `adoption-barriers`, `search-demand`, `audience-homelab-selfhosting`, `audience-oss-infra-and-researchers`), the adversarial verification, `research/POSITIONING.md`, `AUDIENCES.md`, `SEARCH.md`, `BARRIERS.md` and `distribution/COMMUNITIES.md` do not exist yet. The workflow scripts are saved in `scripts/workflows/research.js` and `draft-review.js`; a local Claude Code session re-runs them with the Workflow tool (resume ids: research wf_fc367b96-c01, review wf_c2a9b28e-210). A cloud daily run without the Workflow tool does the same work directly: one lens per run from the LENSES list in `scripts/workflows/research.js`, written to `research/raw/<key>.md`, then the synthesis files once all nine exist.
- Scheduling: two cloud routines created 2026-10-30 (ids below). Local evidence-sync task: blocked by permission (OWNER-ASKS 7).

## Routine ids
- daily: `trig_018xkiTyQqoEVCLHrVgXYwWz` (cron 0 13 * * * UTC, model claude-opus-5-5, source div0rce/ucompute-growth, no connectors) — https://claude.ai/code/routines/trig_018xkiTyQqoEVCLHrVgXYwWz
- weekly: `trig_01Xxy1PgCyyTQAent7Ddfz2Q` (cron 0 14 * * 1 UTC, same config) — https://claude.ai/code/routines/trig_01Xxy1PgCyyTQAent7Ddfz2Q
- first runs: daily 2026-10-30 13:06 UTC, weekly 2026-11-02 14:05 UTC; verify with `RemoteTrigger list_runs` or the routine page, then record in LOG.md

## Next actions (ranked, for the daily runs)
0. Routine health: the first cloud daily run was due 2026-10-30 13:06 UTC. The next run checks `journal/LOG.md` for a "cloud daily" entry; if there is none by 2026-11-01, record a failure in LOG and OWNER-ASKS ("check the daily routine at https://claude.ai/code/routines").
1. Review the four drafts in `content/drafts/` (fact-check against `evidence/upstream/` + `claims/registry.json`, reader review, fixes, strict lint) and move each to `content/ready/`; pairing explainer first, leading with default-deny and the prompt-free audit, revoke as part of the trust lifecycle (2026-W44 strategy change; do not call revoke unique). One or two per run, quality first.
2. Finish the research, one lens per run: `channels-platform-rules` → `adoption-barriers` → `search-demand` → `audience-homelab-selfhosting` → `audience-oss-infra-and-researchers` (prompts in `scripts/workflows/research.js`, output `research/raw/<key>.md`). Then write `research/AUDIENCES.md`, `research/POSITIONING.md` (start from `research/COMPETITORS.md` §Implications) and `distribution/COMMUNITIES.md`.
3. Write `content/community-answers.md` from the four raw research files (open ports, sleep, discovery, "why not Ollama / LM Link / PAIR"), each answer with claim ids.
4. Revise experiment X-04's variants (replace the "choose where a request runs" headline with a default-deny/audit headline).
5. Watch `evidence/upstream/` for the final capability snapshot and the Windows post-fix run (local sessions sync; cloud runs use the mirror).
6. Held drafts: source-publication announcement and release communication (only when the gates move).
7. Next weekly report: `analytics/weekly/2026-W45.md` on Monday 2026-11-09 (or the next weekly fire); compare against this week's table, which has no cloud datapoints until OWNER-ASKS 8 is done.
