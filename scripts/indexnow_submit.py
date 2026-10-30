#!/usr/bin/env python3
"""Submit every URL in the notes site's sitemap to IndexNow (Bing, Yandex, Seznam, Naver share submissions).

Run after each publish to ucompute/notes. Free, no account: ownership is proven by the key file the build ships
at https://ucompute.github.io/notes/<key>.txt. Prints the HTTP status (200 or 202 = accepted).
ponytail: whole sitemap every time; it is a handful of URLs.
"""
import json, re, sys, urllib.request, urllib.error, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_notes import INDEXNOW_KEY, SITE

def main():
    sm = urllib.request.urlopen(SITE + "sitemap.xml", timeout=20).read().decode()
    urls = re.findall(r"<loc>([^<]+)</loc>", sm)
    body = json.dumps({"host": "ucompute.github.io", "key": INDEXNOW_KEY,
                       "keyLocation": f"{SITE}{INDEXNOW_KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        status = urllib.request.urlopen(req, timeout=30).status
    except urllib.error.HTTPError as e:
        status = e.code
    print(f"indexnow: HTTP {status} for {len(urls)} URLs")
    return 0 if status in (200, 202) else 1

if __name__ == "__main__":
    sys.exit(main())
