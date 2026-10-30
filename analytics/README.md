# Measurement

Principles: real, authorized, privacy-conscious; never infer conversions from views; every number has a source and a date. Raw daily files live in `measurements/YYYY-MM-DD.json` (written by `scripts/baseline.sh`); weekly reports in `weekly/YYYY-Www.md`.

## Funnel and metric definitions
| Stage | Metric | Source available today | Source when gates open |
|---|---|---|---|
| Discovery | search impressions and clicks for ucompute.org; referrers to the public repository | GitHub referrers API (empty); no site analytics (the site injects none by owner rule) | Google Search Console (owner verifies the domain, free); Cloudflare Web Analytics server-side or Pages request logs if the owner allows a first-party, cookie-free measure |
| Understanding | time-on-page is not measured; use qualitative signals: questions asked, replies | none | authorized channel replies |
| Interest | stars, watchers, forks; opt-in interest only if the owner authorizes a sign-up | GitHub API (0/0/0 on 2026-10-30) | same plus authorized sign-up |
| Installation | downloads of a public release | none (private alpha behind access control; counts never published) | release asset download counts (GitHub releases API) or Pages logs |
| First workload | not measurable without telemetry; the product has none by design | — | tester feedback only, with consent |
| Second device | same | — | same |
| Repeat use | same | — | same |
| Developer integration | independent projects citing or integrating UCompute | GitHub code search for the project name (noise today) | same, plus community reports |

## Baseline (2026-10-30)
See `measurements/2026-10-30.json`: public repository 0 stars, 0 watchers, 0 forks; 14-day views 6 (3 unique); 14-day clones 27 (21 unique, largely automated mirrors and the project's own operations); ucompute.org reachable, one indexed URL; no analytics. Search presence: to be recorded by the research synthesis (`research/SEARCH.md`).
