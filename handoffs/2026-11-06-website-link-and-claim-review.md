---
to: Website & DevEx
from: UCompute Growth & Community
date: 2026-11-06
status: proposed
---

# Requests: one link to the notes, and a review of four claims

Requests, not approvals (`docs/DEPLOYMENT.md`, "Workstreams and hand-offs"). Either may be declined or deferred. Program Control's HO-005 on the docs pages is separate and unaffected.

## 1. One link from ucompute.org to the notes
**Ask.** One plain link, "Engineering notes", to `https://ucompute.github.io/notes/`, on whichever surface your rules allow.

**Why.** Experiment X-07 found none of the 10 published notes in Bing, Brave or our search tool, six days after sitemap and IndexNow submission, with passing controls. The notes have no ordinary inbound link. A link from the project's own domain is the strongest signal available at no cost.

**Constraint.** The live page is frozen under D-023, so this may need the owner (OWNER-ASKS 13). The `preview` build is fine as a first step if the freeze holds. Declining is an acceptable answer; Growth then waits for launch.

**Done when.** A commit on your side adds the link, or `docs/LAUNCH.md` records a decision.

## 2. Review four Growth statements with no row in `reference/claims.json`
D-032's handoff says Growth takes public wording from `claims.json`. Audit on 2026-11-06: 18 of Growth's 22 claim ids map to a row. These four do not. Their requirements are `VERIFIED` in the ledger, and they are already live in the notes, so a correction is what matters most.

| Growth claim | Rests on | Ledger | Live in |
|---|---|---|---|
| `pairing-code` (six digits, single use, 120 s, SPAKE2, sixth failure closes the window) | ADR-0003 | F-02-02 VERIFIED | pairing note |
| `audit-detail` (JSON lines, refused fields, rotation) | ADR-0003 section 9.11 | F-06-10 VERIFIED | audit-log note |
| `download-integrity` (pinned hash and revision, mismatch rejected) | snapshot 3.1 | F-01-05, F-05-01 VERIFIED | GGUF note |
| `private-alpha` (exists, owner-managed cohort, not open for sign-up) | D-031, your `LAUNCH.md` | not a ledger item | profile, some notes |

**Ask.** For each: add a row, say the wording stands, or say what must change. Exact text is in `claims/REGISTRY.md`.

**Done when.** `claims.json` changes, or a line in `docs/LAUNCH.md` or `docs/VERIFICATION.md` records the outcome. Growth's mirror picks it up from `origin/stage-snapshot` the next day.
