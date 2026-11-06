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

**Not publishable.** Gate: a `VERIFIED` ledger row (F-03-01 is IMPLEMENTED_UNVERIFIED) and an updated Website `claims.json`, or the owner's explicit release of this run as a dated research post. The Core Lab has not finished scoring, and P1.4, P1.5, P1.6, P1.7 and P1.8 are owed. Do not move these to a queue on your own judgment.

1. We predicted 16,921 bytes per token crossing the link. We measured 17,022. It's a strange feeling when the spreadsheet is right.
2. Same model, same prompt. All on Metal, or half the layers on an x86 CPU: the text matches for 135 characters, then goes its own way. Both are valid. Near-ties in the logits break differently on different hardware.
3. Loading half of a small model over home Wi-Fi moves 190 MB and takes about 40 seconds, every load. Caching that has become a very attractive idea.
4. First run of one model across two machines: 23 steps, 0 failures. Still owed: peak memory, a relay capture, nine failure cases and a quiet timing run. Promising, not done.
