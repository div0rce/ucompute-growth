---
to: Website workstream
from: UCompute Growth
date: 2026-10-30
status: proposed
---
# Proposal: an "Engineering notes" section on the complete site, with a feed

**Ask.** Add a `/notes/` section to the complete site (the `preview` build; nothing on the frozen prelaunch page, D-023) that renders dated technical articles from Growth, plus `/notes/feed.xml` (RSS or Atom) and inclusion in `sitemap.xml` when the complete site launches. Articles are plain HTML pages in the existing page format with front matter, so `build.mjs`, `check.mjs` and the claim markers apply unchanged. Growth delivers each article as a file in `content/ready/` of the `ucompute-growth` repository with `{{claim:ID}}` markers matching `reference/claims.json`; the Website workstream copies it into `src/pages/notes/`, runs `npm test`, and deploys to preview. No automation touches the website repository.

**Why.** The site has one indexed URL. Developers find infrastructure projects through specific technical pages (how pairing works, why an RPC server stays on loopback, how memory fit is estimated), not through a prelaunch page. Every article is bounded by the capability snapshot and passes both the website checks and Growth's claims lint, so the section adds discoverability without adding claims.

**First three articles (ready in `content/ready/` as they pass lint):**
1. How two UCompute devices pair: the code, the keys, and the revoke (claims `mesh-pair-choose`, `transport`, `revocation`, `device-sees-prompt`, `local-only`).
2. Why llama.cpp's RPC server stays on loopback, and what UCompute puts around it (claims `engine`, `transport`, `planned`).
3. Before you load a model: how UCompute estimates whether a GGUF fits (claims `catalog-fit`, `platforms`).

**Measurement.** If the owner permits a first-party, cookie-free measure (Cloudflare Web Analytics server-side, or Pages request logs), Growth will use it; otherwise Google Search Console on the domain (owner-verified, free) is enough for search impressions. No third-party scripts, consistent with the site's rule.

**Not asked.** No change to the prelaunch page, no download or sign-up language, no repository links while the source is unpublished.
