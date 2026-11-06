# Experiment backlog

Format: id · hypothesis · metric and threshold · method · cost · status · result · decision. An experiment counts only when its metric is measured, never when content is merely published.

| id | Hypothesis | Metric, threshold | Method | Status |
|---|---|---|---|---|
| X-01 | Developers searching for "run a model on my other computer" style queries will read a truthful technical page about authenticated pairing more than a generic product page | organic visits to the page in 30 days after indexing vs. the site's other pages (needs website analytics that respect the no-third-party rule, e.g. Cloudflare's server-side Web Analytics or Pages logs; proposal in handoffs) | publish via Website handoff; measure 30 days | blocked: pages exist but are not in search (X-07), and there is no visit data (OWNER-ASKS 12) |
| X-02 | Honest limitation statements ("each request runs whole on one device") increase trust signals (saves, constructive replies) vs. hype in developer communities | ratio of constructive replies to total, saves/upvotes per view, qualitatively coded | A/B two post variants on an authorized channel, one week apart | deferred: Bluesky at 0 followers cannot separate variants; re-evaluate at 50 followers |
| X-03 | A one-page "pairing and revocation" explainer answers a recurring real question (laptop uses desktop GPU safely) well enough that community members link it | number of inbound links/mentions in 60 days | publish, then watch referrers (GitHub referrers API, site analytics) | running since 2026-10-30; 7-day read 2026-11-07, 30-day read 2026-11-30 |
| X-04 | Positioning test: "nothing leaves your device until you allow it, per device" (default-deny) vs. "an audit log of every off-device request, without your prompts" headline (variants revised 2026-10-30 per the W44 competitor re-check; "choose where a request runs" is now a category sentence) | click-through on two variants of the same post | authorized channel A/B | deferred: same as X-02 |
| X-05 | Baseline drift: does the public repository get any organic traffic before publication? | 14-day views and uniques from `scripts/baseline.sh`, weekly | passive, running | running (baseline 2026-10-30: 6 views / 3 uniques, 27 clones / 21 uniques, mostly automated) |
| X-06 | A disclosed, automated Bluesky account posting at most one note link a day produces some discovery signal within 30 days, with no other distribution | any of: followers > 0 from accounts other than our own follows, a reply, a repost, or an exact-match mention; read from `bluesky_account` and `bsky` in the daily Actions file | passive; posts from the existing queue; read 2026-11-16 (14 days) and 2026-12-02 (30 days) | running since 2026-11-02 (baseline: 0 followers, 1 follow, post 1 pinned) |
| X-07 | The notes are absent from search because crawlers lack host-level signals and distinct page metadata, not only because the site is new | Distinct note URLs found by `site:ucompute.github.io` on Bing, Brave and the WebSearch tool, each with a passing same-day control. Success: at least 1 note on at least 1 engine by 2026-11-20. Strong: at least 3 notes, or one note returned for its exact title | Arm A evaluated 2026-11-06; arm B changed 2026-11-06, read 2026-11-13 and 2026-11-20 (runbook section 7) | arm A **evaluated: negative**; arm B running |

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

## 2026-11-06: X-07, search discoverability
**Registered late, and labelled so.** Arm A was not pre-registered. The sitemap and IndexNow were shipped on 2026-10-31 as routine setup, and the W45 review recorded "indexable pages now exist" without checking. It is written up here because it is a real distribution action on an authorized channel with a measurable outcome. Arm B is pre-registered above, before any reading.

**Arm A: sitemap and IndexNow alone.** Executed 2026-10-31 00:05 UTC (IndexNow HTTP 200; later URLs through the daily `--new-only` job). Read 2026-11-06 about 08:15 UTC, T+6 days.

| Method | Control (`ollama.readthedocs.io`) | `ucompute.github.io` |
|---|---|---|
| Bing result page, `site:` | 22 matches | 0 |
| Brave result page, `site:` | 127 matches | 0 |
| WebSearch tool, domain filter | 10 results | 0 |
| WebSearch tool, exact note title | not applicable | note not returned |
| Mojeek, Yandex, DuckDuckGo | refused or challenged the client | not measured |
| Google | not measured | not measured |

Result: **0 of 10 published notes found on three methods with passing controls.** Supporting evidence: `ucompute/notes` 0 views and no referrers in 14 days; 112 clones (48 unique), which are our routines, Pages and bots.

Decision: a sitemap and IndexNow do not create discovery for a new `github.io` project site within six days. Content is not the current constraint, so the cap of three new notes a week stands and no new search-page content is justified until a note appears. The W45 line "indexable pages now exist" was an unchecked assumption and is corrected: a page is discoverable only when an engine returns it. A caveat on strength: six days is short, and a null here does not prove the notes will stay absent.

**Arm B: host signals and page metadata.** All live 2026-11-06 by about 08:35 UTC and verified with curl:
1. New root site `ucompute/ucompute.github.io` with `robots.txt` carrying `Sitemap: https://ucompute.github.io/notes/sitemap.xml` (before: root 404, no robots.txt, so a crawler probing the host learned nothing).
2. A distinct meta description on every note (before: one sentence on every page).
3. `ucompute/notes` homepage points to the notes site (before: ucompute.org).
4. IndexNow resubmission of all 11 URLs, HTTP 200.

Limits, stated now: there is no control arm, so the site simply getting older could produce the same result; attribution to any single change will not be possible. If arm B succeeds, the learning is "the combination was enough", no more. If it fails at T+14, the next move is an inbound link and search-console data (OWNER-ASKS 12 and 13), not more metadata.

Cost: $0.

## 2026-11-06: interim reads
- **X-05, second datapoint.** 14 days to 2026-11-06: public repository 0 views, 8 clones; `ucompute/notes` 0 views, 112 clones (48 unique); `.github` 0 views, 41 clones (28 unique); referrers none. No organic traffic. Decision: retain, read weekly from local sessions only.
- **X-06, interim, T+4 days (final read 2026-11-16).** 4 posts, 0 followers, 0 replies, 0 reposts, 0 quotes, 1 like on post 1 from an unrelated account, within minutes of posting. A like is not in the metric, so nothing qualifies so far. Exact-match count corrected: the 2 earlier "mentions" were our own posts; the measurement now excludes our account and the log was cleaned.
- **X-03.** Read tomorrow, as registered.
