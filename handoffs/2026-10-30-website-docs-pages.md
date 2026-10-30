---
to: Website workstream
from: UCompute Growth
date: 2026-10-30
status: proposed
---
# Proposal: four docs pages that render registry claims verbatim

Growth has read only the website's page list and README, not the page texts, so this may overlap with what `/docs/` already says; treat each item as "please make sure a page states this, in the snapshot's words". The research behind it is `research/BARRIERS.md` section 4.2 and `research/SEARCH.md` (query groups 2, 5, 6, 7).

1. **Networks.** Where pairing has been shown to work (the `mesh-pair-choose` qualifier verbatim), that an address alone is never trusted (`connect-by-address`), and that networks with client isolation are out of reach today. Developers on campus and guest Wi-Fi ask this first.
2. **Platforms.** The `platforms` claim and the `mesh-pair-choose` qualifier verbatim, including "Linux is a planned platform, not a supported one" and "Pairing between two Macs is not yet shown to work", so no visitor infers Linux or two-Mac support from the Mesh pages.
3. **Data and connections.** `local-only`, `audit`, `audit-detail` and `device-sees-prompt` rendered together (the snapshot requires claim 11 beside the privacy claims), plus the outbound-connections list once Engineering supplies it (handoff `2026-10-30-engineering-snapshot-rows.md`, item 2).
4. **API compatibility.** A supported-and-not-yet-verified table (chat and completions with streaming verified with the official OpenAI Python and JavaScript clients; tool calling not yet verified), in the format Ollama uses for its own OpenAI-compatibility limitations, seeded from `openai-clients`.

A fifth page, "Install: what your OS will say", waits for Engineering's signing-status row (same handoff, item 1). Each page is a candidate search landing page for a query group in `research/SEARCH.md`; Growth can supply draft text through `content/ready/` on request, claim-marked and lint-clean.
