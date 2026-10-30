# Channel registry

The single source of truth for where Growth may publish. A channel is **AUTHORIZED** only when the owner's written grant is quoted in its row (date, exact words). Everything else is preparation. `distribution/COMMUNITIES.md` holds the full community database with platform rules; this file holds decisions.

Status vocabulary: AUTHORIZED · PREREQUISITE (owner action needed; listed in `journal/OWNER-ASKS.md`) · HANDOFF (another workstream owns the surface; proposal in `handoffs/`) · HUMAN_ONLY (platform rules forbid automated operation) · WHEN_SOURCE_PUBLIC (useful only after the owner publishes the source) · REJECTED.

| Channel | Status | Why / what it takes | First use |
|---|---|---|---|
| ucompute.org (public prelaunch page) | HANDOFF | Owned by the Website workstream; the live page is frozen by owner decision D-023. Growth proposes pages through `handoffs/` only | Proposal: an "Engineering notes" section with an RSS feed, behind the same claims checks (`handoffs/2026-10-30-website-engineering-notes.md`) |
| GitHub public repository (`ucompute`) | HANDOFF | Source publication is an owner decision (engineering B-007/D-028). Growth never pushes there. Content must not link it while it holds only a LICENSE | After publication: README quality, Discussions, issue templates, good-first-issue labelling, release notes |
| GitHub organization `ucompute` | PREREQUISITE | The login `ucompute` returned not-found on 2026-10-30 (free at that moment). Only the owner may create accounts. A UCompute-branded org separates the public identity from the founder's handle | Owner creates the org and invites the growth operator's token; Growth then proposes moving public surfaces under it (engineering decides) |
| UCompute contact mailbox (e.g. hello@ucompute.org via Cloudflare Email Routing, free) | PREREQUISITE | Needed before any community post can carry a contact; the owner holds the Cloudflare zone | Owner configures routing to an inbox they control |
| Hacker News (Show HN) | HUMAN_ONLY | HN guidelines expect a person to post and answer; Show HN requires something people can try, which does not exist publicly yet. Growth drafts the post and answers; the owner (or a future human maintainer) submits | After a public source or release |
| Reddit (r/LocalLLaMA, r/selfhosted, r/homelab) | PREREQUISITE + rules check | Needs a UCompute-branded account the owner creates; subreddit self-promotion rules apply (quoted in `distribution/COMMUNITIES.md` once researched); automation must be disclosed | Useful answers to real questions first; no project posts until something is usable |
| Bluesky (`@ucompute.org` as a domain handle) | PREREQUISITE | Account creation is an owner action; the domain handle proves the project identity. Bluesky allows labelled automated accounts; API is free | Engineering notes, evidence-dated updates |
| Mastodon (a FOSS-friendly instance) | PREREQUISITE | Owner creates the account; instance rules on bots and project accounts must be quoted first | Same as Bluesky |
| X / Twitter | REJECTED for now | Free API write access is limited and automation rules are strict; low fit for $0 budget | Revisit if the owner wants it |
| LinkedIn company page | REJECTED for now | Requires a personal profile as admin (identity exposure) | — |
| dev.to / Hashnode (organization or project account) | PREREQUISITE | Owner creates the account; both allow canonical URLs, so articles can live on ucompute.org first and syndicate | Republish engineering notes with canonical links |
| Newsletter | REJECTED for now | Collecting emails needs its own owner authorization (spec 29.5) and a provider; nothing to announce yet | Revisit at public release |
| Discord / forum | REJECTED for now | The Community page says none exists and will not pretend otherwise; a server without a usable product is empty | Revisit at public release |
| Product Hunt | REJECTED for now | Nothing publicly usable | Revisit at public release |
| Claude.ai artifacts | REJECTED as a public channel | Private by default, not a developer channel | — |

## Weekly review 2026-W44 (2026-10-30, cloud weekly)
No status changed: no owner grant exists, so nothing is AUTHORIZED. No platform rules were re-read this week (the `channels-platform-rules` research lens has not run yet; it is next week's first research item), so no rule-based status change is justified. Evidence that did arrive (competitor and audience research in `research/raw/`) confirms the ranking of the PREREQUISITE channels: the multi-device and local-AI audiences are found in r/LocalLLaMA, r/selfhosted, Hacker News comment threads and dev.to write-ups, which keeps Reddit, dev.to/Hashnode and HN (human-submitted) as the highest-fit channels once something is publicly usable. The ucompute.org HANDOFF remains the only publication path. `distribution/COMMUNITIES.md` does not exist yet; it is written after the platform-rules lens.

## Publishing procedure (when a channel is AUTHORIZED)
1. The piece sits in `content/ready/` with `claims:` front matter and passes `python3 scripts/claims_lint.py content/ready --strict`.
2. Check the channel's rule row in `distribution/COMMUNITIES.md` (frequency, disclosure, format).
3. Publish; record the URL, timestamp, channel and piece id in `content/published/INDEX.md` and `journal/LOG.md`; move the file to `content/published/`.
4. Schedule the measurement check in `analytics/` (7 and 30 days).
