#!/usr/bin/env python3
"""Render claims/REGISTRY.md and claims/PROHIBITED.md from claims/registry.json (single source of truth)."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
reg = json.loads((ROOT / "claims/registry.json").read_text())
lines = [f"# UCompute claims registry\n", f"Generated from `claims/registry.json` by `scripts/render_claims.py`. Snapshot: **{reg['snapshot']}**, updated {reg['updated']}.\n",
         f"Source: {reg['source']}\n", f"**Rule:** {reg['rule']}\n", "| id | label | claim | qualifier (keep beside the claim) | evidence |", "|---|---|---|---|---|"]
for k, c in reg["claims"].items():
    lines.append(f"| `{k}` | {c['label']} | {c['text']} | {c['qualifier'] or '—'} | {c['evidence']} |")
lines += ["", "## Numbers", "", reg["numbers"]["rule"], "", "| figure | model | hardware | scope |", "|---|---|---|---|"]
for n in reg["numbers"]["allowed"]:
    lines.append(f"| {n['figure']} | {n['model']} | {n['hardware']} | {n['scope']} |")
lines += ["", "## How a new snapshot is adopted", "", "1. `scripts/sync_evidence.sh` refreshes `evidence/upstream/`.", "2. Diff `capability-snapshot.md` sections 8 and 9 against this registry; edit `claims/registry.json` (never a page first).", "3. `python3 scripts/render_claims.py && python3 scripts/claims_lint.py content --strict`.", "4. Re-lint every file in `content/ready` and `content/published`; withdraw or amend anything a changed claim no longer supports; log it in `journal/LOG.md`."]
(ROOT / "claims/REGISTRY.md").write_text("\n".join(lines) + "\n")
p = ["# Prohibited or premature phrases\n", "Mirrors capability snapshot section 9. `scripts/claims_lint.py` fails any content line matching these (case-insensitive) unless the line negates it. Say the registry claim instead.\n", "| pattern | why (snapshot section 9) |", "|---|---|"]
why = {"pool": "pooling and partitioning do not exist (Gate D); remote execution is not pooling", "distributed inference": "same", "cluster": "same", "join the ucompute network": "Swarm disabled, Gate F unverified", "earn credits": "no credits, billing, payments or payouts exist", "crypto": "never required, not implemented", "free forever": "no release; free is direction and not unlimited", "download": "no release record, no signed installers, no cohort open", "waitlist": "a sign-up needs its own owner authorization (spec 29.5)", "one-click install": "F-10-01 unverified", "supported on": "no platform is SUPPORTED", "runs on linux": "one CPU daemon in tests; Linux is PLANNED", "apple silicon": "only M2 on macOS 26.2 is experimental", "7b": "evidence covers models up to 0.5B (memory planning to 1.5B)", "faster": "all tok/s figures are path checks on tiny models", "never leaves your device": "the executing device sees the prompt; downloads use the internet", "works offline": "no offline test; first run downloads", "open protocol": "one implementation, experimental", "sdk": "SDKs are planned", "view on github": "source unpublished; the public repo holds only a LICENSE", "connect from anywhere": "same-network evidence only", "signed": "ad-hoc signed, not notarized; Windows unsigned", "automatic updates": "not started", "enterprise": "no paid service authorized", "™": "trademark clearance open", "users": "no cohort has started; test machines are not users", "screen": "no screen reader run yet", "mac.to.mac": "pairing failed on 2026-10-21, not repeated"}
for pat in reg["prohibited_patterns"]:
    w = next((v for k, v in why.items() if k in pat.lower()), "see snapshot section 9")
    p.append(f"| `{pat}` | {w} |")
p += ["", "## Identity patterns (never negatable)", "", "Any match anywhere in `content/` fails the lint: founder identity, affiliation, testers, machines, networks, private repositories, paths, IP addresses, private site addresses.", ""]
p += [f"- `{x}`" for x in reg["identity_patterns"]]
(ROOT / "claims/PROHIBITED.md").write_text("\n".join(p) + "\n")
print("rendered claims/REGISTRY.md and claims/PROHIBITED.md")
