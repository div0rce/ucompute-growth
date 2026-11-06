#!/usr/bin/env python3
"""Post the next queued UCompute post to Bluesky. Runs daily in GitHub Actions.

Queue: the "## Post N ..." sections of content/ready/bluesky-queue.md, in file order. Heading tokens: "pinned" pins the
post, "reply to post-N" threads it under that ledger entry, "not before YYYY-MM-DD" is a floor, not an appointment.
Ledger: analytics/bluesky-posted.jsonl (one JSON line per post).
Before posting: the account's profile carries the queue's bio and no "bot" self-label (owner's instruction, 2026-11-06;
Bluesky's label is voluntary); caps hold
(one post per UTC day, four per rolling 7 days; corrections and the pinned post skip the weekly cap); the text is at
most 300 characters; every link, if there is one, answers HTTP 200; the text passes the claims and voice lints. Credentials: BSKY_HANDLE and BSKY_APP_PASSWORD from the environment
(an app password stored as a repository secret by the owner; never printed). Without them it exits 0 with a notice.
ponytail: stdlib urllib; no thumbnail upload for link cards.
"""
import datetime as dt, json, os, pathlib, re, subprocess, sys, tempfile, urllib.request, urllib.error
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from voice_lint import findings as voice_findings

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "content" / "ready" / "bluesky-queue.md"
LEDGER = ROOT / "analytics" / "bluesky-posted.jsonl"
PDS = "https://bsky.social/xrpc/"
URL_RE = re.compile(r"https?://[^\s)]+")
DAY_CAP, WEEK_CAP, MAX_LEN = 1, 4, 300

def parse_queue(text):
    """[(post_id, heading, body)] from '## Post N (...)' sections; bio from the 'Bio (...):' line."""
    posts = [(f"post-{n}", h.strip(), b.strip())
             for n, h, b in re.findall(r"^## Post (\d+)([^\n]*)\n\n(.*?)(?=\n## |\Z)", text, re.S | re.M)]
    bio = re.search(r"^Bio \(256 characters max\): (.+)$", text, re.M)
    return posts, (bio.group(1).strip() if bio else None)

def facets(text):
    out, b = [], text.encode("utf-8")
    for m in URL_RE.finditer(text):
        start = len(text[:m.start()].encode("utf-8")); end = start + len(m.group(0).encode("utf-8"))
        assert b[start:end].decode() == m.group(0)
        out.append({"index": {"byteStart": start, "byteEnd": end},
                    "features": [{"$type": "app.bsky.richtext.facet#link", "uri": m.group(0)}]})
    return out

def heading_meta(heading):
    """(not_before, reply_to_post_id) from a queue heading."""
    nb = re.search(r"not before (\d{4}-\d{2}-\d{2})", heading)
    rp = re.search(r"reply to (post-\d+)", heading)
    return (nb.group(1) if nb else ""), (rp.group(1) if rp else None)

def caps_ok(ledger, now, exempt=False):
    ts = [dt.datetime.fromisoformat(e["at"]) for e in ledger]
    today = sum(1 for t in ts if t.date() == now.date())
    week = sum(1 for t in ts if now - t < dt.timedelta(days=7))
    return today < DAY_CAP and (exempt or week < WEEK_CAP)

def call(method, body=None, token=None, get=False):
    url = PDS + method
    if get and body:
        url += "?" + "&".join(f"{k}={v}" for k, v in body.items())
    req = urllib.request.Request(url, data=None if get else json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json",
                                          **({"Authorization": f"Bearer {token}"} if token else {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def link_ok(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "ucompute-growth"}), timeout=20) as r:
            return r.status == 200
    except Exception:
        return False

def page_title(u):
    try:
        html = urllib.request.urlopen(u, timeout=20).read().decode("utf-8", "replace")
        m = re.search(r"<title>([^<]+)</title>", html)
        return (m.group(1).split(" | ")[0].strip() if m else u)[:300]
    except Exception:
        return u

def lint_ok(text):
    with tempfile.TemporaryDirectory() as d:
        f = pathlib.Path(d) / "post.md"; f.write_text(text)
        return subprocess.run([sys.executable, str(ROOT / "scripts" / "claims_lint.py"), str(f)],
                              capture_output=True).returncode == 0

def without_bot(vals):
    return {"labels": {"$type": "com.atproto.label.defs#selfLabels", "values": [{"val": v} for v in vals if v != "bot"]}}

def ensure_profile(token, did, bio):
    rec = call("com.atproto.repo.getRecord", {"repo": did, "collection": "app.bsky.actor.profile", "rkey": "self"}, token, get=True)
    value, cid = rec["value"], rec.get("cid")
    vals = [l.get("val") for l in (value.get("labels") or {}).get("values", [])]
    changed = False
    if bio and value.get("description") != bio:
        value["description"] = bio; changed = True
    if "bot" in vals:
        value.update(without_bot(vals)) if len(vals) > 1 else value.pop("labels", None)
        changed = True
    if changed:
        call("com.atproto.repo.putRecord", {"repo": did, "collection": "app.bsky.actor.profile", "rkey": "self",
                                            "record": value, "swapRecord": cid}, token)
    return value, changed

def main():
    handle, pw = os.environ.get("BSKY_HANDLE"), os.environ.get("BSKY_APP_PASSWORD")
    if not (handle and pw):
        print("bsky_post: BSKY_HANDLE or BSKY_APP_PASSWORD not set; nothing posted (OWNER-ASKS 11)"); return 0
    posts, bio = parse_queue(QUEUE.read_text())
    ledger = [json.loads(l) for l in LEDGER.read_text().splitlines() if l.strip()] if LEDGER.exists() else []
    done = {e["id"] for e in ledger}
    sess = call("com.atproto.server.createSession", {"identifier": handle, "password": pw})
    token, did = sess["accessJwt"], sess["did"]
    _, changed = ensure_profile(token, did, bio)
    print(f"bsky_post: profile {'updated (bio, labels)' if changed else 'unchanged'}")
    now = dt.datetime.now(dt.timezone.utc)
    for pid, heading, text in posts:
        if pid in done:
            continue
        not_before, reply_to = heading_meta(heading)
        if not_before > now.date().isoformat():
            continue
        if not caps_ok(ledger, now, exempt=bool(reply_to) or "pinned" in heading):
            print("bsky_post: cap reached (1/day, 4/week); nothing posted"); return 0
        links = URL_RE.findall(text)
        if len(text) > MAX_LEN or voice_findings(text) or not lint_ok(text) or not all(link_ok(u) for u in links):
            print(f"bsky_post: {pid} held (length {len(text)}, voice {voice_findings(text)}, lint or a link not live yet)"); continue
        rec = {"$type": "app.bsky.feed.post", "text": text, "createdAt": now.isoformat().replace("+00:00", "Z"),
               "langs": ["en"]}
        if reply_to:
            parent = next(e for e in ledger if e["id"] == reply_to)
            ref = {"uri": parent["uri"], "cid": parent["cid"]}
            rec["reply"] = {"root": ref, "parent": ref}
        if links:
            rec["facets"] = facets(text)
            rec["embed"] = {"$type": "app.bsky.embed.external",
                            "external": {"uri": links[-1], "title": page_title(links[-1]), "description": ""}}
        res = call("com.atproto.repo.createRecord", {"repo": did, "collection": "app.bsky.feed.post", "record": rec}, token)
        if "pinned" in heading:
            prof = call("com.atproto.repo.getRecord", {"repo": did, "collection": "app.bsky.actor.profile", "rkey": "self"}, token, get=True)
            prof["value"]["pinnedPost"] = {"uri": res["uri"], "cid": res["cid"]}
            call("com.atproto.repo.putRecord", {"repo": did, "collection": "app.bsky.actor.profile", "rkey": "self",
                                                "record": prof["value"], "swapRecord": prof.get("cid")}, token)
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER.open("a") as f:
            f.write(json.dumps({"id": pid, "uri": res["uri"], "cid": res["cid"], "at": now.isoformat(),
                                "url": f"https://bsky.app/profile/{handle}/post/{res['uri'].rsplit('/', 1)[-1]}"}) + "\n")
        print(f"bsky_post: posted {pid} -> https://bsky.app/profile/{handle}/post/{res['uri'].rsplit('/', 1)[-1]}")
        return 0
    print("bsky_post: nothing due"); return 0

def selftest():
    t = "Résumé check https://ucompute.github.io/notes/x.html done"
    f = facets(t)[0]["index"]
    assert t.encode()[f["byteStart"]:f["byteEnd"]].decode() == "https://ucompute.github.io/notes/x.html"
    q = "Bio (256 characters max): hello bio\n\n## Post 1 (pinned; x)\n\nfirst\n\n## Post 2 (day 2)\n\nsecond\nhttps://a.b/c\n\n## Rules\n- r"
    posts, bio = parse_queue(q)
    assert bio == "hello bio" and [p[0] for p in posts] == ["post-1", "post-2"] and posts[1][2].endswith("https://a.b/c")
    now = dt.datetime(2026, 11, 2, 12, tzinfo=dt.timezone.utc)
    assert caps_ok([], now)
    assert not caps_ok([{"at": "2026-11-02T01:00:00+00:00"}], now)
    week = [{"at": f"2026-10-{d}T10:00:00+00:00"} for d in (28, 29, 30, 31)]
    assert not caps_ok(week, now) and caps_ok(week[1:], now)
    assert heading_meta(" (pinned; not before 2026-11-07)") == ("2026-11-07", None)
    assert heading_meta(" (reply to post-4; correction)") == ("", "post-4")
    assert caps_ok(week[1:], now) and not caps_ok(week, now) and caps_ok(week, now, exempt=True)
    assert not caps_ok([{"at": "2026-11-02T01:00:00+00:00"}], now, exempt=True), "exempt skips the week, never the day"
    assert without_bot(["bot", "x"])["labels"]["values"] == [{"val": "x"}]
    print("bsky_post selftest: ok")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit(0)
    sys.exit(main())
