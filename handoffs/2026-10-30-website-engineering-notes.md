---
to: Website workstream
from: UCompute Growth
date: 2026-10-30
status: proposed
---
# Proposal: an "Engineering notes" section on the complete site, with a feed

**Ask.** Add a `/notes/` section to the complete site (the `preview` build; nothing on the frozen prelaunch page, D-023) that renders dated technical articles from Growth, plus `/notes/feed.xml` (RSS or Atom) and inclusion in `sitemap.xml` when the complete site launches. Articles are plain HTML pages in the existing page format with front matter, so `build.mjs`, `check.mjs` and the claim markers apply unchanged. Growth delivers each article as a file in `content/ready/` of the `ucompute-growth` repository with `{{claim:ID}}` markers matching `reference/claims.json`; the Website workstream copies it into `src/pages/notes/`, runs `npm test`, and deploys to preview. No automation touches the website repository.

**Why.** The site has one indexed URL. Developers find infrastructure projects through specific technical pages (how pairing works, why an RPC server stays on loopback, how memory fit is estimated), not through a prelaunch page. Every article is bounded by the capability snapshot and passes both the website checks and Growth's claims lint, so the section adds discoverability without adding claims.

**Five pieces are ready now** (`content/ready/` in the `ucompute-growth` repository; each passed a fact-check against the engineering evidence, a reader review, and the claims lint on 2026-10-30):
1. `2026-10-30-pairing-explainer`: How two UCompute devices pair: the six-digit code, the keys and the revoke (claims `mesh-pair-choose`, `transport`, `revocation`, `local-only`, `device-sees-prompt`, `audit`, `connect-by-address`, `platforms`, `no-release`, `license`).
2. `2026-10-31-loopback-rpc-vs-authenticated-transport`: llama.cpp's RPC backend is not a network transport, and what UCompute does instead (claims `engine`, `transport`, `mesh-pair-choose`, `planned`, `device-sees-prompt`, `no-release`, `license`).
3. `2026-11-01-memory-fit-explainer`: Before you load a model: how UCompute estimates whether a GGUF fits (claims `catalog-fit`, `engine`, `platforms`, `no-release`, `license`).
4. `2026-11-02-openai-client-base-url`: Point the official OpenAI Python and JavaScript clients at a local server (claims `openai-clients`, `run-local`, `local-only`, `device-sees-prompt`, `no-release`, `license`); fits `/docs/` as well as `/notes/`.
5. `2026-10-30-what-the-audit-log-records`: What UCompute's audit log records, and what it never records (claims `audit`, `audit-detail`, `local-only`, `device-sees-prompt`, `mesh-pair-choose`, `no-release`, `license`). `audit-detail` is a new Growth registry row for the mechanics (forbidden fields, size bound, rotation, security trail); the website claim map would need an equivalent row, with evidence ADR-0003 §9.11 and the observability crate's tests.

Each file's front matter (`claims:`, `sources:`) is source-side material and must not render; the claim ids map onto `reference/claims.json` rows of the same meaning (`mesh-pair-choose`, `transport`, `revocation`, `local-only`, `audit`, `device-sees-prompt`, `connect-by-address`, `platforms`, `license`, `no-release` exist there under the same or equivalent names; `engine`, `catalog-fit`, `openai-clients`, `planned` map to `engine`, `catalog`/`memory-fit`, `openai-clients`, `planned`). The website's own `check.mjs` stays the final gate.

**Measurement.** If the owner permits a first-party, cookie-free measure (Cloudflare Web Analytics server-side, or Pages request logs), Growth will use it; otherwise Google Search Console on the domain (owner-verified, free) is enough for search impressions. No third-party scripts, consistent with the site's rule.

**Not asked.** No change to the prelaunch page, no download or sign-up language, no repository links while the source is unpublished.
