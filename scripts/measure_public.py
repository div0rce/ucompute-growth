#!/usr/bin/env python3
"""Public, credential-free measurement for UCompute Growth. Runs in GitHub Actions daily.

Writes analytics/measurements/<UTC date>.public.json and appends new mentions to analytics/mentions.jsonl.
Sources (all public, no account): ucompute.org (status, sitemap URL count), GitHub REST (public repo and org
stats, repositories named like the project), Hacker News via Algolia (exact "ucompute", stories and
comments), Bluesky AppView search. A source that fails is recorded as {"error": ...}, never guessed.
Also: routine health. Exit 2 when no "cloud daily" log entry exists in the last 48 h, so GitHub emails the
workflow owner (the only alert channel that needs no setup).
ponytail: stdlib urllib, no retries; add backoff if a source flaps.
"""
import datetime as dt, json, os, pathlib, re, sys, urllib.request, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = {"User-Agent": "ucompute-growth-measure/1 (+https://ucompute.org)"}
FOUNDED = dt.date(2026, 10, 30)

def get(url, headers=None, raw=False):
    h = dict(UA, **(headers or {}))
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=20) as r:
        body = r.read()
        return r.status, (body.decode("utf-8", "replace") if raw else json.loads(body))

def safe(fn):
    try:
        return fn()
    except Exception as e:  # recorded, never guessed
        return {"error": f"{type(e).__name__}: {e}"[:300]}

def count_locs(xml):
    return len(re.findall(r"<loc>", xml))

def last_daily(log_text):
    """Latest date of a '## YYYY-MM-DD — cloud daily' heading, or None."""
    ds = re.findall(r"^## (\d{4}-\d{2}-\d{2}) [—-]+ cloud daily", log_text, re.M)
    return max((dt.date.fromisoformat(d) for d in ds), default=None)

def daily_overdue(log_text, today):
    last = last_daily(log_text) or FOUNDED
    return (today - last).days >= 2

def gh_headers():
    t = os.environ.get("GITHUB_TOKEN")
    return {"Authorization": f"Bearer {t}"} if t else {}

def site():
    s, _ = get("https://ucompute.org/", raw=True)
    _, sm = get("https://ucompute.org/sitemap.xml", raw=True)
    return {"http": s, "sitemap_urls": count_locs(sm)}

def notes_site():
    s, _ = get("https://ucompute.github.io/notes/", raw=True)
    _, sm = get("https://ucompute.github.io/notes/sitemap.xml", raw=True)
    return {"http": s, "sitemap_urls": count_locs(sm)}

def repo():
    _, d = get("https://api.github.com/repos/div0rce/ucompute", gh_headers())
    return {k: d.get(k) for k in ("stargazers_count", "subscribers_count", "forks_count", "open_issues_count", "pushed_at")}

def org():
    _, d = get("https://api.github.com/orgs/ucompute", gh_headers())
    return {k: d.get(k) for k in ("public_repos", "followers")}

def published():
    """Stars, watchers and forks of every public repository in the organization (published since 2026-10-31)."""
    _, repos = get("https://api.github.com/orgs/ucompute/repos?type=public&per_page=100", gh_headers())
    return {r["name"]: {"stars": r["stargazers_count"], "watchers": r["watchers_count"], "forks": r["forks_count"],
                        "pushed_at": r["pushed_at"]} for r in repos}

def name_repos():
    _, d = get("https://api.github.com/search/repositories?q=ucompute+in:name", gh_headers())
    return {"total": d.get("total_count"), "names": sorted(i["full_name"] for i in d.get("items", []))}

def hn():
    q = urllib.parse.urlencode({"query": "ucompute", "typoTolerance": "false", "hitsPerPage": 50})
    _, d = get(f"https://hn.algolia.com/api/v1/search_by_date?{q}")
    hits = [{"src": "hn", "id": h["objectID"], "at": h.get("created_at"),
             "url": f"https://news.ycombinator.com/item?id={h['objectID']}",
             "text": (h.get("title") or h.get("comment_text") or "")[:200]} for h in d.get("hits", [])]
    return {"count": d.get("nbHits"), "hits": hits}

def bsky():
    q = urllib.parse.urlencode({"q": "ucompute", "limit": 50})
    _, d = get(f"https://api.bsky.app/xrpc/app.bsky.feed.searchPosts?{q}")
    hits = [{"src": "bsky", "id": p["uri"], "at": p.get("indexedAt"), "url": p["uri"],
             "text": (p.get("record", {}).get("text") or "")[:200]} for p in d.get("posts", [])]
    return {"count": len(hits), "hits": hits}

def bluesky():
    """Public counts for @ucompute.org and engagement on every post in analytics/bluesky-posted.jsonl."""
    _, p = get("https://api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=ucompute.org")
    out = {k: p.get(k) for k in ("followersCount", "followsCount", "postsCount")}
    out["bot_label"] = any(l.get("val") == "bot" for l in p.get("labels", []))
    led = ROOT / "analytics" / "bluesky-posted.jsonl"
    uris = [json.loads(l)["uri"] for l in led.read_text().splitlines() if l.strip()] if led.exists() else []
    if uris:
        q = "&".join("uris=" + urllib.parse.quote(u, safe="") for u in uris[-25:])
        _, d = get(f"https://api.bsky.app/xrpc/app.bsky.feed.getPosts?{q}")
        out["posts"] = {x["uri"].rsplit("/", 1)[-1]: {k: x.get(k) for k in ("likeCount", "repostCount", "replyCount", "quoteCount")}
                        for x in d.get("posts", [])}
    return out

def main():
    today = dt.datetime.now(dt.timezone.utc).date()
    out = {"date": today.isoformat(), "source": "github-actions measure_public.py",
           "site": safe(site), "notes_site": safe(notes_site), "public_repo": safe(repo), "org": safe(org), "org_repos": safe(published), "bluesky_account": safe(bluesky),
           "repos_named_ucompute": safe(name_repos), "hn": safe(hn), "bsky": safe(bsky)}
    mdir = ROOT / "analytics" / "measurements"; mdir.mkdir(parents=True, exist_ok=True)
    mentions = ROOT / "analytics" / "mentions.jsonl"
    seen = {json.loads(l)["id"] for l in mentions.read_text().splitlines() if l.strip()} if mentions.exists() else set()
    new = [h for k in ("hn", "bsky") for h in out[k].get("hits", []) if h["id"] not in seen]
    if new:
        with mentions.open("a") as f:
            for h in new:
                f.write(json.dumps(h) + "\n")
    for k in ("hn", "bsky"):
        out[k].pop("hits", None)
    out["new_mentions"] = len(new)
    log = (ROOT / "journal" / "LOG.md").read_text()
    out["routine_health"] = {"last_cloud_daily": str(last_daily(log)), "overdue": daily_overdue(log, today)}
    (mdir / f"{today.isoformat()}.public.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))
    return 2 if out["routine_health"]["overdue"] else 0

def selftest():
    assert count_locs("<urlset><url><loc>a</loc></url><url><loc>b</loc></url></urlset>") == 2
    log = "## 2026-10-30 — local founding session\n## 2026-11-02 — cloud daily\n## 2026-11-01 — cloud daily\n"
    assert last_daily(log) == dt.date(2026, 11, 2)
    assert not daily_overdue(log, dt.date(2026, 11, 3)) and daily_overdue(log, dt.date(2026, 11, 4))
    assert daily_overdue("no entries", dt.date(2026, 11, 1)) and not daily_overdue("no entries", dt.date(2026, 10, 31))
    print("measure_public selftest: ok")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit(0)
    sys.exit(main())
