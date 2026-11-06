---
id: split-run-held
title: Held posts on the first two-machine run
type: social-post
audience: local-ai-developers, oss-infra
channel_intent: none until the gate below opens
claims: [planned]
status: draft
sources: evidence/upstream/engineering-evidence-pool-two-machine-2026-11-06.md
---

**Not publishable.** Gate: a `VERIFIED` ledger row and an updated Website `claims.json`, or the owner's explicit release of this run as a dated research post. Status 2026-11-06: the Core Lab has scored run-0820 (bytes, turns and placement PASS on all six runs, 4 of 4 denials typed, no canary found, timing has no verdict under D-033). That is a score, not a claim: F-03-01 is still IMPLEMENTED_UNVERIFIED and the remaining P1 steps are owed. Do not move these to a queue on your own judgment. Re-read the evidence before releasing any of them.

1. We predicted 16,921 bytes per token crossing the link. We measured 17,022. It's a strange feeling when the spreadsheet is right.
2. Same model, same prompt. All on Metal, or half the layers on an x86 CPU: the text matches for 135 characters, then goes its own way. Both are valid. Near-ties in the logits break differently on different hardware.
3. Every split load takes 36 to 86 seconds because it uploads weights the other machine already holds. A tensor cache looked like the fix. It isn't: for models this size it would skip nothing on one and a quarter on the other. The open question is why the tunnel does 42 Mbit/s on a 351 Mbit/s link.
4. First run of one model across two machines: 23 steps, 0 failures. Still owed: peak memory, a relay capture, nine failure cases and a quiet timing run. Promising, not done.
