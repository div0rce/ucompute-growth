#!/usr/bin/env python3
"""Send the next queued X post to Buffer. Closed by default: does nothing until channels/REGISTRY.md marks X AUTHORIZED.

Design and evidence: distribution/X-INTEGRATION.md. Reuses bsky_post.py's queue, caps, claims lint and link checks and
voice_lint.py, so X passes the same gates as Bluesky. Queue: content/ready/x-queue.md. Ledger: analytics/x-posted.jsonl.

Default mode saves a Buffer draft and a person releases it, which keeps the account human-run. X_MODE=unattended
schedules it instead; that needs X's Automated label and a public link to a human-run account, so it also needs the
word "unattended" in the registry row. Credentials: BUFFER_API_KEY and BUFFER_X_CHANNEL_ID, held as repository
secrets by the owner and never printed. Never scripts X, never replies: X requires prior approval for AI-generated replies.
ponytail: publish status is not read back; add post(input:{id}) once a live key confirms the schema.
"""
import datetime as dt, json, os, pathlib, re, sys, urllib.request
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from bsky_post import caps_ok, heading_meta, link_ok, lint_ok, parse_queue, URL_RE
from voice_lint import findings as voice_findings

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "content" / "ready" / "x-queue.md"
LEDGER = ROOT / "analytics" / "x-posted.jsonl"
REGISTRY = ROOT / "channels" / "REGISTRY.md"
API = "https://api.buffer.com"
MAX_LEN = 280  # X's limit for accounts without a paid X plan
MUTATION = """mutation($input: CreatePostInput!) { createPost(input: $input) {
  ... on PostActionSuccess { post { id } } ... on MutationError { message } } }"""

def authorized(text, mode):
    row = next((l for l in text.splitlines() if l.startswith("| X ")), "")
    return "**AUTHORIZED**" in row and (mode != "unattended" or "unattended" in row)

def post_input(text, channel, mode, now):
    base = {"text": text, "channelId": channel, "schedulingType": "automatic", "mode": "customScheduled",
            "dueAt": (now + dt.timedelta(minutes=10)).isoformat().replace("+00:00", "Z")}
    return base if mode == "unattended" else {**base, "saveToDraft": True}

def send(key, variables):
    req = urllib.request.Request(API, data=json.dumps({"query": MUTATION, "variables": variables}).encode(),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())

def next_post(posts, done, ledger, now):
    """First post that is due and clears every gate, or a printable reason there is none."""
    for pid, heading, text in posts:
        if pid in done:
            continue
        if heading_meta(heading)[0] > now.date().isoformat():
            continue
        if not caps_ok(ledger, now, exempt="pinned" in heading):
            return None, "cap reached"
        if len(text) > MAX_LEN or voice_findings(text) or not lint_ok(text) or not all(link_ok(u) for u in URL_RE.findall(text)):
            print(f"x_post: {pid} held (length {len(text)}, voice {voice_findings(text)}, lint or link)"); continue
        return (pid, text), ""
    return None, "nothing due"

def main(send=send):
    mode = os.environ.get("X_MODE", "draft")
    if not authorized(REGISTRY.read_text(), mode):
        print(f"x_post: X is not AUTHORIZED for {mode} in channels/REGISTRY.md; nothing sent"); return 0
    key, channel = os.environ.get("BUFFER_API_KEY"), os.environ.get("BUFFER_X_CHANNEL_ID")
    if not (key and channel):
        print("x_post: BUFFER_API_KEY or BUFFER_X_CHANNEL_ID not set; nothing sent"); return 0
    ledger = [json.loads(l) for l in LEDGER.read_text().splitlines() if l.strip()] if LEDGER.exists() else []
    now = dt.datetime.now(dt.timezone.utc)
    item, why = next_post(parse_queue(QUEUE.read_text())[0], {e["id"] for e in ledger}, ledger, now)
    if not item:
        print(f"x_post: {why}"); return 0
    pid, text = item
    res = send(key, {"input": post_input(text, channel, mode, now)})
    out = (res.get("data") or {}).get("createPost") or {}
    if "post" not in out:  # Buffer reports failures in the body, not as an HTTP error
        print(f"x_post: {pid} refused: {out.get('message') or res.get('errors')}"); return 1
    with LEDGER.open("a") as f:
        f.write(json.dumps({"id": pid, "buffer_id": out["post"]["id"], "mode": mode, "at": now.isoformat()}) + "\n")
    print(f"x_post: {pid} sent to Buffer ({mode})"); return 0

def selftest():
    closed = "| X / Twitter | PREREQUISITE | x |\n"; open_ = "| X / Twitter | **AUTHORIZED** | drafts through Buffer |\n"
    assert not authorized(closed, "draft") and not authorized("", "draft")
    assert authorized(open_, "draft") and not authorized(open_, "unattended"), "unattended needs its own grant"
    assert authorized(open_.replace("drafts", "unattended posts"), "unattended")
    now = dt.datetime(2026, 11, 10, 12, tzinfo=dt.timezone.utc)
    d = post_input("hi", "chan", "draft", now)
    assert d["saveToDraft"] is True and d["channelId"] == "chan" and d["dueAt"] == "2026-11-10T12:10:00Z"
    assert "saveToDraft" not in post_input("hi", "chan", "unattended", now)
    assert next_post([("post-1", " (not before 2026-11-11)", "later")], set(), [], now) == (None, "nothing due")
    assert next_post([("post-1", "", "Soak test: 2,607 kills.")], set(), [], now)[0] == ("post-1", "Soak test: 2,607 kills.")
    assert next_post([("post-1", "", "x" * 281)], set(), [], now)[0] is None, "over 280 is held"
    assert next_post([("post-1", "", "We're excited to announce it")], set(), [], now)[0] is None, "voice gate applies"
    assert next_post([("post-1", "", "a")], {"post-1"}, [], now)[0] is None, "ledger prevents a repeat"
    print("x_post selftest: ok")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit(0)
    sys.exit(main())
