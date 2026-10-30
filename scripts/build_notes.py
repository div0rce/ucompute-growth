#!/usr/bin/env python3
"""Render content/ready engineering notes into a publishable tree for the public `ucompute/notes` repository.

Output: dist/notes/README.md (index), dist/notes/<id>.md (front matter stripped, a provenance footer added),
dist/notes/feed.xml (Atom). Only pieces with type engineering-note, explainer, comparison or search-page are
included; the community-answers bank and anything not status: ready are excluded. The output is linted again
with the strict claims lint before the script succeeds, so a failing piece blocks the whole package.
ponytail: string templates, no markdown or XML library; Atom needs only escaped titles and absolute links.
"""
import html, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "content" / "ready", ROOT / "dist" / "notes"
BASE = "https://github.com/ucompute/notes/blob/main/"
SITE = "https://ucompute.github.io/notes/"
# IndexNow ownership key (public by design: it proves control of the site, grants nothing else).
INDEXNOW_KEY = "b1d8674aecd8b2fc96497ccb3c2cd26e"
TYPES = {"engineering-note", "explainer", "comparison", "search-page"}
FRONT = re.compile(r"^---\n(.*?)\n---\n", re.S)
FOOTER = ("\n---\n\n*Published by the UCompute project. This note was drafted and checked by UCompute's automated "
          "growth workstream against the project's engineering evidence. Please do not post suspected security problems "
          "publicly; a private reporting route will be listed here when it exists. UCompute is in development. There is no "
          "public release or download yet.*\n")

def parse(text):
    m = FRONT.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); meta[k.strip()] = v.strip()
    return meta, text[m.end():]

def pieces():
    for f in sorted(SRC.glob("*.md")):
        meta, body = parse(f.read_text())
        if meta.get("status") == "ready" and meta.get("type") in TYPES:
            yield meta, body.strip() + "\n"

def build():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*"):
        old.unlink()
    items = list(pieces())
    for meta, body in items:
        (OUT / f"{meta['id']}.md").write_text(body + FOOTER)
    idx = ["# UCompute engineering notes", "",
           "Technical notes from the UCompute project: how its development builds work, what has been tested and where, "
           "and what does not exist yet. UCompute is in development. There is no public release or download yet. "
           "UCompute's code is licensed under Apache-2.0. The source has not been published yet.", "",
           "Not related to the uCompute RP2040 boards, Universal Compute products or any token.", ""]
    idx += [f"- [{m['title']}]({m['id']}.md)" for m, _ in items]
    idx += ["", "Feed: [feed.xml](feed.xml). Each note states the hardware and builds it rests on; numbers are never performance claims."]
    (OUT / "README.md").write_text("\n".join(idx) + "\n")
    (OUT / "_config.yml").write_text(
        "title: UCompute engineering notes\n"
        "description: Technical notes from the UCompute project. In development; no public release. "
        "Apache-2.0; source not yet published.\n"
        "url: https://ucompute.github.io\nbaseurl: /notes\n"
        "plugins:\n  - jekyll-sitemap\n  - jekyll-relative-links\n  - jekyll-optional-front-matter\n  - jekyll-titles-from-headings\n"
        "include: [" + INDEXNOW_KEY + ".txt]\n")
    (OUT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY + "\n")
    entries = "".join(
        f"<entry><title>{html.escape(m['title'])}</title><id>{SITE}{m['id']}.html</id>"
        f"<link href=\"{SITE}{m['id']}.html\"/><updated>{m['id'][:10]}T00:00:00Z</updated></entry>\n" for m, _ in items)
    newest = max((m["id"][:10] for m, _ in items), default="2026-10-30")
    (OUT / "feed.xml").write_text(
        "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<feed xmlns=\"http://www.w3.org/2005/Atom\">"
        f"<title>UCompute engineering notes</title><id>{SITE}</id><link href=\"{SITE}\"/><updated>{newest}T00:00:00Z</updated>\n{entries}</feed>\n")
    return items

def main():
    items = build()
    lint = subprocess.run([sys.executable, str(ROOT / "scripts" / "claims_lint.py"), str(OUT)], capture_output=True, text=True)
    print(lint.stdout.strip())
    if lint.returncode:
        print("build_notes: lint failed; nothing is publishable", file=sys.stderr); return 1
    print(f"build_notes: {len(items)} notes -> {OUT.relative_to(ROOT)}")
    return 0

def selftest():
    meta, body = parse("---\nid: x\ntitle: T: sub\nstatus: ready\n---\n# H\n")
    assert meta == {"id": "x", "title": "T: sub", "status": "ready"} and body == "# H\n"
    assert parse("no front\n") == ({}, "no front\n")
    print("build_notes selftest: ok")

if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest(); sys.exit(0)
    sys.exit(main())
