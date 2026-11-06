#!/usr/bin/env bash
# Cloud routine ucompute-growth-evidence-sync (Bash only, no web tools, so private repositories never meet web content).
# Refreshes the mirror from this run's own clones and pushes only real changes; SYNC.md alone is not a change.
set -euo pipefail
cd "$(dirname "$0")/.."
ENG=/home/user/ucompute-dev
WEB=/home/user/ucompute-website
for repo in "$ENG" "$WEB"; do git -C "$repo" fetch -q origin '+refs/heads/*:refs/remotes/origin/*'; done
# ponytail: Engineering's records live on its active branch until its stack lands on main; newest non-bot branch finds it.
eng_ref=$(git -C "$ENG" for-each-ref --sort=-committerdate --format='%(refname:short)' refs/remotes/origin \
  | grep -v -E '^origin$|/HEAD$|^origin/(claude|dependabot)/' | sed -n 1p)
UCOMPUTE_ENG_REPO=$ENG UCOMPUTE_WEB_REPO=$WEB UCOMPUTE_ENG_REF=$eng_ref UCOMPUTE_WEB_REF=origin/stage-snapshot \
  bash scripts/sync_evidence.sh
if git diff --quiet -- evidence/upstream ':!evidence/upstream/SYNC.md' && [ -z "$(git ls-files -o --exclude-standard evidence/upstream)" ]; then
  git checkout -- evidence/upstream/SYNC.md
  echo "evidence: no change"
  exit 0
fi
git add evidence/upstream
git -c user.name='UCompute Growth' -c user.email=noreply@ucompute.org commit -qm "$(date -u +%F): evidence sync (cloud)"
git pull -q --rebase origin main
git push -q origin HEAD:main
echo "evidence: pushed $(git rev-parse --short HEAD)"
