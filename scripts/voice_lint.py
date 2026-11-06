#!/usr/bin/env python3
"""Mechanical floor under charter/VOICE.md: catches marketing phrases and formula, cannot judge quality.
Lints the unpublished posts in content/ready/*-queue.md. bsky_post.py calls findings() before posting anything.
"""
import json, math, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BANNED = re.compile(
    r"\b(excited to|thrilled to|proud to|happy to announce|we're announcing|here's why|here is why|why this matters|"
    r"let's dive|dive in(to)?|deep dive|unlock\w*|game.?chang\w*|revolution\w*|seamless\w*|supercharg\w*|empower\w*|"
    r"leverag\w*|next.?gen\w*|cutting.?edge|world.?class|best.?in.?class|stay tuned|check (it |this )?out|learn more|"
    r"read more|in this (post|thread|note|article)|\U0001F9F5|the future of|more than just|not just .{1,40} but)\b", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐]")
LINK = re.compile(r"https?://")

def findings(text):
    out = []
    m = BANNED.search(text)
    if m: out.append(f"marketing phrase: {m.group(0)!r}")
    if EMOJI.search(text): out.append("emoji")
    if re.search(r"(^|\s)#[A-Za-z]", text): out.append("hashtag")
    if re.search(r"^\s*([-*•]|\d+\.)\s", text, re.M): out.append("list formatting")
    if re.match(r"\s*ucompute\b", text, re.I): out.append("opens with our own name")
    if re.match(r"\s*(how|what|why)\s+(\w+\s+){0,3}ucompute\b", text, re.I): out.append("article-summary opening")
    if text.rstrip().endswith((":", "→")): out.append("ends pointing at something")
    return out

def queue_findings(posts):
    """posts: [(id, body)] in order. Queue-level formula checks."""
    out = []
    links = sum(bool(LINK.search(b)) for _, b in posts)
    if links > math.ceil(len(posts) / 4): out.append(f"{links} of {len(posts)} posts carry links; the limit is one in four")
    firsts = [b.split()[0].lower() for _, b in posts if b.split()]
    out += [f"{posts[i][0]}: same first word as the post before" for i in range(1, len(firsts)) if firsts[i] == firsts[i - 1]]
    return out

def main():
    sys.path.insert(0, str(ROOT / "scripts"))
    from bsky_post import parse_queue, LEDGER
    done = {json.loads(l)["id"] for l in LEDGER.read_text().splitlines() if l.strip()} if LEDGER.exists() else set()
    bad, n = [], 0
    for f in sorted((ROOT / "content" / "ready").glob("*-queue.md")):
        posts = [(p, b) for p, _, b in parse_queue(f.read_text())[0] if p not in done or "x-queue" in f.name]
        n += len(posts)
        bad += [f"{f.name} {p}: {x}" for p, b in posts for x in findings(b)]
        bad += [f"{f.name} {x}" for x in queue_findings(posts)]
        if "x-queue" in f.name:
            bad += [f"{f.name} {p}: {len(b)} characters, X allows 280" for p, b in posts if len(b) > 280]
    print("\n".join(bad + [f"voice_lint: {n} unpublished posts, {len(bad)} findings"]))
    return 1 if bad else 0

def selftest():
    assert findings("We're excited to announce the next-gen thing") and findings("Great news #ai") and findings("UCompute now pairs")
    assert findings("How two UCompute devices pair") and findings("Shipping \U0001F680") and findings("Three ways:\n- one")
    assert findings("Details in the note:")
    assert not findings("We stopped reusing them: 0 failures in 43,000 requests. We still don't know why it closes them.")
    assert queue_findings([("a", "x https://a"), ("b", "y"), ("c", "z https://b"), ("d", "w")])
    assert queue_findings([("a", "We did"), ("b", "We also")]) and not queue_findings([("a", "We did"), ("b", "Then we")])
    print("voice_lint selftest: ok")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit(0)
    sys.exit(main())
