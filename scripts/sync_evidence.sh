#!/usr/bin/env bash
# Mirror read-only evidence from the local engineering and website checkouts into evidence/upstream/.
# Reads only committed files (git show HEAD:path) so a mid-edit working tree is never copied.
# ponytail: paths are fixed to this Mac; the cloud routine uses the committed mirror instead.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$HERE/evidence/upstream"
ENG="${UCOMPUTE_ENG_REPO:-/Users/nasr/repos/ucompute}"
WEB="${UCOMPUTE_WEB_REPO:-/Users/nasr/repos/ucompute-website-work/website}"
mkdir -p "$OUT"
copy() { # repo path dest
  if git -C "$1" cat-file -e "HEAD:$2" 2>/dev/null; then
    git -C "$1" show "HEAD:$2" > "$OUT/$3"; echo "synced $3 (from $(git -C "$1" rev-parse --short HEAD))"
  else echo "missing $1:$2" >&2; fi
}
copy "$ENG" docs/DECISIONS.md engineering-DECISIONS.md
copy "$ENG" docs/BLOCKERS.md engineering-BLOCKERS.md
copy "$ENG" README.md engineering-README.md
latest="$(git -C "$ENG" ls-tree --name-only HEAD docs/capabilities/ | sort | tail -1)"
[ -n "$latest" ] && copy "$ENG" "$latest" "capability-snapshot.md"
copy "$WEB" reference/claims.json website-claims.json
copy "$WEB" reference/releases.json website-releases.json
copy "$WEB" docs/LAUNCH.md website-LAUNCH.md
{
  echo "# Upstream evidence sync"
  echo "synced_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "engineering_head: $(git -C "$ENG" rev-parse HEAD) ($(git -C "$ENG" branch --show-current))"
  echo "website_head: $(git -C "$WEB" rev-parse HEAD) ($(git -C "$WEB" branch --show-current))"
  echo "capability_snapshot: $latest"
} > "$OUT/SYNC.md"
# Privacy scrub check: the mirror must not carry personal identifiers into any public output.
# It stays private in this repo; the lint blocks these strings from content/.
cat "$OUT/SYNC.md"
