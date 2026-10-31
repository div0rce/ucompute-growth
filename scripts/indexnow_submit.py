#!/usr/bin/env python3
"""Submit every URL in the notes site's sitemap to IndexNow (Bing, Yandex, Seznam, Naver share submissions).

Runs daily in GitHub Actions with --new-only: submits only sitemap URLs not yet listed in
analytics/indexnow-submitted.txt, then records them. Free, no account: ownership is proven by the key file the
build ships at https://ucompute.github.io/notes/<key>.txt. Prints the HTTP status (200 or 202 = accepted).
"""
import json, re, sys, urllib.request, urllib.error, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_notes import INDEXNOW_KEY, SITE

LEDGER = pathlib.Path(__file__).resolve().parent.parent / "analytics" / "indexnow-submitted.txt"

def main():
    sm = urllib.request.urlopen(SITE + "sitemap.xml", timeout=20).read().decode()
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
    done = set(LEDGER.read_text().split()) if LEDGER.exists() else set()
    if "--new-only" in sys.argv:
        urls = [u for u in urls if u not in done]
        if not urls:
            print("indexnow: nothing new"); return 0
    body = json.dumps({"host": "ucompute.github.io", "key": INDEXNOW_KEY,
                       "keyLocation": f"{SITE}{INDEXNOW_KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        status = urllib.request.urlopen(req, timeout=30).status
    except urllib.error.HTTPError as e:
        status = e.code
    print(f"indexnow: HTTP {status} for {len(urls)} URLs")
    if status in (200, 202):
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text("\n".join(sorted(done | set(urls))) + "\n")
        return 0
    return 1

if __name__ == "__main__":
    sys.exit(main())
