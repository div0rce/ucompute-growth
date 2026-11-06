# Measurement

Principles: real, authorized, privacy-conscious; never infer conversions from views; every number has a source and a date. Raw daily files live in `measurements/YYYY-MM-DD.json` (written by `scripts/baseline.sh`); weekly checkpoints in `weekly/YYYY-Www.md` (format in `runbook/RUNBOOK.md` section 3).

## Funnel and metric definitions
Only evidence-supported outcomes count. Zero is a result. Views never count as conversions.

| Stage | What counts | Source today | Reading 2026-11-06 |
|---|---|---|---|
| Discovery | A developer who is not us reaches a UCompute page: search appearance, referrers, exact-match mentions | Search readings (runbook section 7), GitHub traffic (local token), `analytics/mentions.jsonl`. GitHub Pages gives no visit data | 0: no note in Bing, Brave or the WebSearch tool; `ucompute/notes` 0 views in 14 days; 0 mentions by others |
| Understanding | Evidence someone read and engaged: questions, corrections, constructive replies | Bluesky replies, `hello@ucompute.org` (owner's mailbox; Growth cannot read it) | 0 replies; mailbox unknown to Growth |
| Qualified interest | A deliberate opt-in by a developer: star, watch, fork, follow, feed subscriber if measurable | GitHub API, Bluesky API | 0 stars, watchers, forks, org followers; 0 Bluesky followers |
| Installation | A public install | None: no public release (gate) | Not reachable |
| First workload | A person runs a model | None: no telemetry by design; consented tester reports only | Not reachable |
| Repeat usage | A person comes back | Same | Not reachable |
| Integration | An independent project integrates or cites UCompute | GitHub code search, community reports | 0 known |
| Advocacy | Someone recommends UCompute unprompted | Mentions | 0 |

Traffic on the notes site itself cannot be seen: no third-party analytics on pages (owner rule). Search-console data is the only clean route (OWNER-ASKS 12).

## Baseline (2026-10-30)
See `measurements/2026-10-30.json`: public repository 0 stars, 0 watchers, 0 forks; 14-day views 6 (3 unique); 14-day clones 27 (21 unique, largely automated mirrors and the project's own operations); ucompute.org reachable, one indexed URL; no analytics. Search presence: to be recorded by the research synthesis (`research/SEARCH.md`).
