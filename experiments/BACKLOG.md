# Experiment backlog

Format: id · hypothesis · metric and threshold · method · cost · status · result · decision. An experiment counts only when its metric is measured, never when content is merely published.

| id | Hypothesis | Metric, threshold | Method | Status |
|---|---|---|---|---|
| X-01 | Developers searching for "run a model on my other computer" style queries will read a truthful technical page about authenticated pairing more than a generic product page | organic visits to the page in 30 days after indexing vs. the site's other pages (needs website analytics that respect the no-third-party rule, e.g. Cloudflare's server-side Web Analytics or Pages logs; proposal in handoffs) | publish via Website handoff; measure 30 days | blocked: no indexable pages, no analytics |
| X-02 | Honest limitation statements ("each request runs whole on one device") increase trust signals (saves, constructive replies) vs. hype in developer communities | ratio of constructive replies to total, saves/upvotes per view, qualitatively coded | A/B two post variants on an authorized channel, one week apart | blocked: no authorized channel |
| X-03 | A one-page "pairing and revocation" explainer answers a recurring real question (laptop uses desktop GPU safely) well enough that community members link it | number of inbound links/mentions in 60 days | publish, then watch referrers (GitHub referrers API, site analytics) | blocked: publication |
| X-04 | Positioning test: "nothing leaves your device until you allow it, per device" (default-deny) vs. "an audit log of every off-device request, without your prompts" headline (variants revised 2026-10-30 per the W44 competitor re-check; "choose where a request runs" is now a category sentence) | click-through on two variants of the same post | authorized channel A/B | blocked: channel |
| X-05 | Baseline drift: does the public repository get any organic traffic before publication? | 14-day views and uniques from `scripts/baseline.sh`, weekly | passive, running | running (baseline 2026-10-30: 6 views / 3 uniques, 27 clones / 21 uniques, mostly automated) |

## Decisions 2026-W44 (2026-10-30, cloud weekly)
All five retained; none abandoned (no result yet). X-04: variant A ("pair your own devices, choose where a request runs") to be replaced by a default-deny / audit headline before the test runs, because three 2026 competitors now use the routing sentence (`research/COMPETITORS.md`). X-05: second datapoint not taken; cloud runs cannot reach the sources (OWNER-ASKS 8).
