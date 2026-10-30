#!/usr/bin/env bash
# Record the measurable, authorized baseline into analytics/measurements/YYYY-MM-DD.json.
# Sources: GitHub API for the public repository (traffic needs push access), live site reachability, sitemap size.
# ponytail: curl + gh + jq only; add a parser when a second data source exists.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$HERE/analytics/measurements"; mkdir -p "$OUT"
DAY="$(date -u +%Y-%m-%d)"; F="$OUT/$DAY.json"
REPO="div0rce/ucompute"
repo_json="$(gh api "repos/$REPO" --jq '{stars:.stargazers_count,watchers:.subscribers_count,forks:.forks_count,open_issues:.open_issues_count}' 2>/dev/null || echo '{}')"
views="$(gh api "repos/$REPO/traffic/views" --jq '{count:.count,uniques:.uniques}' 2>/dev/null || echo '{}')"
clones="$(gh api "repos/$REPO/traffic/clones" --jq '{count:.count,uniques:.uniques}' 2>/dev/null || echo '{}')"
referrers="$(gh api "repos/$REPO/traffic/popular/referrers" 2>/dev/null || echo '[]')"
site_code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 https://ucompute.org/ || echo 0)"
sitemap_urls="$(curl -s --max-time 20 https://ucompute.org/sitemap.xml | grep -c '<loc>' || echo 0)"
jq -n --arg day "$DAY" --argjson repo "$repo_json" --argjson views "$views" --argjson clones "$clones" \
  --argjson referrers "$referrers" --arg site "$site_code" --arg urls "$sitemap_urls" \
  '{date:$day, public_repo:{name:"div0rce/ucompute", stats:$repo, views_14d:$views, clones_14d:$clones, referrers:$referrers},
    site:{"ucompute.org_http":$site, sitemap_urls:($urls|tonumber)},
    notes:"Public repo holds only LICENSE and a superseded handoff; the site is the frozen prelaunch page with no analytics (owner rule). Clone counts include bots and the project itself."}' > "$F"
cat "$F"
