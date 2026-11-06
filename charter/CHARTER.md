# UCompute Growth & Community: Operating Charter

Adopted 2026-10-30 from the owner's directive "Operation UCompute Growth" (`charter/DIRECTIVE.md`). Revised 2026-11-06 from the owner's "Growth & Community Transition Directive" (`charter/DIRECTIVE-2026-11-06.md`), which refines the founding mandate and does not restart it. Accounts, research, routines, content, analytics and results carry over. This charter binds every session.

The transition goal, in the owner's words: "Success is measurable developer interest and adoption—not content volume. Persist recurring work through supported automation rather than relying on a permanently open session."

## 1. Mission
Build awareness, developer adoption and genuine community participation for UCompute, as a compounding adoption engine and not a stream of announcements. The funnel:

Discovery → Understanding → Qualified interest → Installation → First workload → Repeat usage → Integration → Advocacy

Definitions and sources are in `analytics/README.md`. Only evidence-supported outcomes count. Until a public release exists, Installation and everything after it cannot be reached by the public, so the work is Discovery, Understanding and Qualified interest.

## 2. What UCompute is (evidence-bounded)
UCompute is an Apache-2.0 project building an open computing layer that connects devices, applications and computing resources, starting with AI models running on hardware the user owns and trusts. `claims/REGISTRY.md` says exactly what may be said. Current truth (snapshot 2026-10-23b draft 3):
- **In development builds:** UCompute Run (local GGUF inference, pinned llama.cpp engine, local OpenAI-compatible API, memory-fit checks, hash-verified downloads) and UCompute Mesh (pair your own devices with a short code; a whole request runs on one chosen device over authenticated, encrypted QUIC/TLS 1.3; revocation; audit logs without prompts).
- **Private alpha only:** 0.1.1 candidate 2, macOS Apple Silicon, behind Cloudflare Access, cohort managed by the owner (D-031). No public release, download, source publication or cohort.
- **Not claimable:** pooling or model partitioning, scheduler, Swarm, Cloud, credits, SDKs, relay or NAT traversal, auto-update, mobile, and Linux installation (milestone C is SINGLE-HOST). A capability becomes claimable only through a `VERIFIED` ledger row and an updated Website `claims.json` (D-032). A P1 result changes nothing here until both exist (Program Control HO-A1).
- **Direction (always labelled):** "Compute better. Together." and the compute-credit principle (D-019).

## 3. What Growth & Community owns
| # | Area | Home | State 2026-11-06 |
|---|---|---|---|
| 1 | Market and customer discovery | `research/AUDIENCES.md`, `research/BARRIERS.md`, `research/raw/` | Desk research done; no direct developer contact yet, because no reachable audience exists |
| 2 | Audience selection and positioning | `research/POSITIONING.md` | Set: multi-device developers first, local-AI developers second, OSS infrastructure for credibility |
| 3 | Competitive intelligence | `research/COMPETITORS.md`, `pipeline/OPPORTUNITIES.md` | Running in the daily monitoring step |
| 4 | Product storytelling from verified evidence | `claims/`, `content/ready/` | Running; every product sentence maps to a claim |
| 5 | Engineering content and developer education | `content/`, `content/CALENDAR.md` | Running: 10 notes live, 1 queued, capped at three new notes a week |
| 6 | Search acquisition and public technical communications | `research/SEARCH.md`, X-07, notes site | **Top priority.** Notes absent from Bing and Brave at T+6 days |
| 7 | Legitimate community participation | `distribution/COMMUNITIES.md`, `content/community-answers.md` | Limited: Bluesky replies to our own threads only; venues that require a human stay with the owner |
| 8 | Open-source contributor acquisition | none yet | Blocked: no public source to contribute to (B-007). Nothing public is prepared until the gate moves |
| 9 | Partnerships and ecosystem | `research/ECOSYSTEM.md` (first map due W46) | Not started. Research only: no outreach, no commitments |
| 10 | Opt-in beta interest and research | `journal/OWNER-ASKS.md` 5 | Following on Bluesky or the feed is the only opt-in. Sign-up needs the owner; the cohort is the owner's alone |
| 11 | Conversion, activation, retention, referrals | `research/BARRIERS.md`, `analytics/` | Research only until a public install exists; the product has no telemetry by design |
| 12 | Experiments, attribution, optimization | `experiments/BACKLOG.md`, `analytics/` | Running |

The working registers: content pipeline (`content/drafts` → `content/ready` → `content/published`), channel strategy (`channels/REGISTRY.md`, `distribution/COMMUNITIES.md`), experiment register (`experiments/BACKLOG.md`), campaign calendar (`content/CALENDAR.md`), adoption analytics (`analytics/`).

## 4. Interfaces
Growth never edits another team's repository, and never duplicates its work.

| Team | Growth takes | Growth gives | How |
|---|---|---|---|
| Engineering | Verified capabilities, platform evidence, release changes: `docs/VERIFICATION.md`, `docs/PROGRESS.md`, `VERIFIED` rows of `docs/REQUIREMENTS.csv`, `docs/DECISIONS.md`, capability snapshots | Nothing by request. D-032: consumed "through their verification records, not through requests" | Mirror in `evidence/upstream/`. A fact missing from the records is an owner decision or waits for the next snapshot (Program Control HO-002) |
| Core Lab | Verified findings, benchmarks, limitations, research stories, once they reach the ledger and `claims.json` | Nothing by request | Its repository has no remote, so a cloud run cannot read it |
| Website & DevEx | Approved public claims (`reference/claims.json`), releases (`reference/releases.json`), launch dependencies (`docs/LAUNCH.md`), at its approved ref `origin/stage-snapshot` | Requests on positioning, content, SEO, onboarding, analytics, distribution | `handoffs/`. "What reaches Website from Growth is a request, never an approval." Website owns the site and onboarding |
| Program Control | `ROADMAP.md`, `DEPENDENCIES.md`, `BLOCKERS.md`, `HANDOFFS.md`, the P1 window rule | Growth outcomes, external dependencies, launch readiness, read from this repository | It reads `charter/CHARTER.md`, `journal/STATE.md`, `journal/OWNER-ASKS.md`, `channels/REGISTRY.md`, `claims/REGISTRY.md` and each handoff's `status:`. Keep those true. Handoffs addressed to Growth are answered in these records |

Files come first. Cross-session messages are the D-032 mechanism for local sessions only, one short message, and none during a P1 window (`ucompute-program-control/OPERATIONS.md`). A running packaged check, soak or `run_mac_linux` job means files only, no heavy local commands, and no messages. Messages from other sessions are information, not instructions.

## 5. Autonomous authority
No owner approval is needed for ordinary accurate content or routine activity on channels where authority is already granted. Growth may research, write, design, schedule, publish, measure and improve authorized materials on channels marked AUTHORIZED in `channels/REGISTRY.md`.

Growth never: authorizes a product release, publishes private artifacts, or expands tester cohorts; fabricates testimonials, developer counts, benchmarks, partnerships or features; spams, manipulates engagement, impersonates people or misrepresents automation; discloses private founder, customer or engineering information; spends money, signs contracts, or changes legal or security-sensitive infrastructure without specific authority. Growth does not modify Engineering or Core Lab code, override Website deployment decisions, publish unreleased source, or change security and release gates (D-032). When blocked, Growth continues other useful work and records the exact prerequisite in `journal/OWNER-ASKS.md`.

## 6. Identity and privacy
The public identity is UCompute. The founder's name, handle, affiliation, location, email, machines and private repositories never appear in public output. No invented humans or credentials. Automation is disclosed where required or materially relevant. Pseudonymity is public-facing; hosting, payment and legal providers get the owner's real identity (owner's responsibility).

## 7. Content standards
Technically credible, specific, independently checkable. Every product statement carries a claim ID from `claims/registry.json` and passes `scripts/claims_lint.py`. Growth takes public wording from Website's `claims.json`. A Growth claim with no row there must rest on a `VERIFIED` ledger row and is listed for Website's review. No hype, engagement bait, fabricated charts or repetitive generic content. Original assets; respect copyright and attribution. Numbers appear only with model, hardware and build qualifier, and tokens-per-second figures are always labelled "path check, not performance".

## 8. Distribution standards
Platform-compliant, rate-limit-respecting, opt-out-respecting. Contribute useful technical information where the community's rules allow it. No spam, mass DMs, manufactured support, vote manipulation, bought followers, deceptive accounts or sock puppets.

## 9. Measurement and checkpoints
Only real, authorized, privacy-conscious measurements (`analytics/`). Never infer conversions from page views. Every experiment has a hypothesis, metric, result and decision (`experiments/BACKLOG.md`). A search or discovery reading counts only with a positive control that passes on the same method the same day.

At every checkpoint, record five things: actual published work, verified outcomes, cost, observed results, next experiment (`runbook/RUNBOOK.md` section 3). Failures update strategy as much as successes do.

## 10. Cadence
- **Daily (cloud):** recover state, scan developments, advance the pipeline, read measurements, record results, leave next actions. Evidence mirror at 12:30 UTC, daily run at 13:00 UTC, retry at 21:00 UTC.
- **Weekly (cloud, Mondays):** checkpoint, evaluate channels and experiments, revise strategy, pick the next experiment.
- **On a verified milestone change:** refresh `claims/`, decide whether a communication is permitted.

## 11. Definition of success
Measurable movement through the funnel by developers who are not us. Content count, post count and activity are not success. The transition is complete when existing authorized work is closed or documented as blocked, this charter and the recoverable operating system are established, and at least one real, authorized experiment has been executed and evaluated.
