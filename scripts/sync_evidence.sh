#!/usr/bin/env bash
# Mirror read-only evidence into evidence/upstream/. Reads committed files at a named ref (git show), never a working
# tree, and never fetches inside another team's checkout: the cloud evidence routine fetches in its own clones.
# Website: its approved ref, not the checkout's HEAD (Program Control C-5, HO-004). Engineering: the claims rule is a
# VERIFIED ledger row, so REQUIREMENTS.csv is mirrored with the records that explain it.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$HERE/evidence/upstream"
ENG="${UCOMPUTE_ENG_REPO:-/Users/nasr/repos/ucompute}"
WEB="${UCOMPUTE_WEB_REPO:-/Users/nasr/repos/ucompute-website-work/website}"
ENG_REF="${UCOMPUTE_ENG_REF:-HEAD}"
WEB_REF="${UCOMPUTE_WEB_REF:-origin/stage-snapshot}"
mkdir -p "$OUT"
copy() { # repo ref path dest
  if git -C "$1" cat-file -e "$2:$3" 2>/dev/null; then
    git -C "$1" show "$2:$3" > "$OUT/$4"; echo "synced $4 (from $2 $(git -C "$1" rev-parse --short "$2"))"
  else echo "missing $1 $2:$3" >&2; fi
}
copy "$ENG" "$ENG_REF" docs/DECISIONS.md engineering-DECISIONS.md
copy "$ENG" "$ENG_REF" docs/BLOCKERS.md engineering-BLOCKERS.md
copy "$ENG" "$ENG_REF" docs/REQUIREMENTS.csv engineering-REQUIREMENTS.csv
copy "$ENG" "$ENG_REF" docs/decisions/ADR-0003-peer-transport-and-pairing.md engineering-ADR-0003.md
copy "$ENG" "$ENG_REF" README.md engineering-README.md
latest="$(git -C "$ENG" ls-tree --name-only "$ENG_REF" docs/capabilities/ | sort | tail -1)"
[ -n "$latest" ] && copy "$ENG" "$ENG_REF" "$latest" "capability-snapshot.md"
copy "$WEB" "$WEB_REF" reference/claims.json website-claims.json
copy "$WEB" "$WEB_REF" reference/releases.json website-releases.json
copy "$WEB" "$WEB_REF" docs/LAUNCH.md website-LAUNCH.md
{
  echo "# Upstream evidence sync"
  echo "synced_at: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "engineering_ref: $ENG_REF $(git -C "$ENG" rev-parse "$ENG_REF")"
  echo "website_ref: $WEB_REF $(git -C "$WEB" rev-parse "$WEB_REF")"
  echo "capability_snapshot: $latest"
} > "$OUT/SYNC.md"
cat "$OUT/SYNC.md"
