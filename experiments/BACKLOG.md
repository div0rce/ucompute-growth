# Experiment backlog

Format: id · hypothesis · metric and threshold · method · cost · status · result · decision. An experiment counts only when its metric is measured, never when content is merely published.

| id | Hypothesis | Metric, threshold | Method | Status |
|---|---|---|---|---|
| X-01 | Developers searching for "run a model on my other computer" style queries will read a truthful technical page about authenticated pairing more than a generic product page | organic visits to the page in 30 days after indexing vs. the site's other pages (needs website analytics that respect the no-third-party rule, e.g. Cloudflare's server-side Web Analytics or Pages logs; proposal in handoffs) | publish via Website handoff; measure 30 days | blocked: no indexable pages, no analytics |
| X-02 | Honest limitation statements ("each request runs whole on one device") increase trust signals (saves, constructive replies) vs. hype in developer communities | ratio of constructive replies to total, saves/upvotes per view, qualitatively coded | A/B two post variants on an authorized channel, one week apart | blocked: no authorized channel |
| X-03 | A one-page "pairing and revocation" explainer answers a recurring real question (laptop uses desktop GPU safely) well enough that community members link it | number of inbound links/mentions in 60 days | publish, then watch referrers (GitHub referrers API, site analytics) | blocked: publication |
| X-04 | Positioning test: "nothing leaves your device until you allow it, per device" (default-deny) vs. "an audit log of every off-device request, without your prompts" headline (variants revised 2026-10-30 per the W44 competitor re-check; "choose where a request runs" is now a category sentence) | click-through on two variants of the same post | authorized channel A/B | blocked: channel |
| X-05 | Baseline drift: does the public repository get any organic traffic before publication? | 14-day views and uniques from `scripts/baseline.sh`, weekly | passive, running | running (baseline 2026-10-30: 6 views / 3 uniques, 27 clones / 21 uniques, mostly automated) |
| X-06 | A disclosed, automated Bluesky account posting at most one note link a day produces some discovery signal within 30 days, with no other distribution | any of: followers > 0 from accounts other than our own follows, a reply, a repost, or an exact-match mention; read from `bluesky_account` and `bsky` in the daily Actions file | passive; posts from the existing queue; read 2026-11-16 (14 days) and 2026-12-02 (30 days) | running since 2026-11-02 (baseline: 0 followers, 1 follow, post 1 pinned) |

## Decisions 2026-W44 (2026-10-30, cloud weekly)
All five retained; none abandoned (no result yet). X-04: variant A ("pair your own devices, choose where a request runs") to be replaced by a default-deny / audit headline before the test runs, because three 2026 competitors now use the routing sentence (`research/COMPETITORS.md`). X-05: second datapoint not taken; cloud runs cannot reach the sources (OWNER-ASKS 8).

## 2026-10-30 23:54 UTC: first publication
- X-03 started: the pairing explainer and five other notes are public at https://github.com/ucompute/notes. Metric: inbound mentions (exact-match Hacker News and Bluesky, `analytics/mentions.jsonl`) and stars/watchers/forks on `ucompute/notes` (`org_repos` in the daily `*.public.json`), read at 7 and 30 days (2026-11-07, 2026-11-30). Baseline at publication: 0 everywhere. No distribution beyond the organization yet, so a null result at 7 days is expected and says the channel alone does not create discovery.
- X-05 extended to the organization's repositories.


## Decisions 2026-W45 (2026-11-02, cloud weekly)
- **X-01 retain, still blocked, blocker changed.** Indexable pages now exist (notes site, 8 pages, sitemap, IndexNow). The remaining blocker is measurement: GitHub Pages gives no visit data, and the owner rule forbids third-party analytics on pages. A zero-cost, no-script option is search-console data for the notes site (impressions and clicks from the search engine itself); recorded as optional OWNER-ASKS 12.
- **X-02 and X-04 retain, deferred (not abandoned).** Bluesky is now AUTHORIZED, so a channel exists, but (a) Bluesky exposes no click-through, so X-04's metric must become likes+reposts+replies per post, and (b) at 0 followers neither test can separate variants. Run them only once the account has at least 50 followers; re-evaluate in W48.
- **X-03 running.** 7-day read due 2026-11-07 (daily run), 30-day read 2026-11-30. Baseline 0 everywhere.
- **X-05 retain, degraded.** No second traffic datapoint this week (traffic needs the owner's token in a local session).
- **X-06 new, running.** Cheapest available test of whether the one automated channel creates any discovery at all.
Nothing abandoned: no experiment has produced a result.
