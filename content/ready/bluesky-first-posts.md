---
id: bluesky-first-posts
title: Bluesky profile and first posts (@ucompute.org)
type: social-post
audience: multi-device-developers, local-ai-developers, oss-infra
channel_intent: Bluesky @ucompute.org (on the owner's grant; automation label on); links require the GitHub notes repository to be published first
claims: [no-release, license, mesh-pair-choose, local-only, audit, device-sees-prompt, revocation, engine, catalog-fit]
status: ready
sources: content/ready notes; distribution/COMMUNITIES.md 5 and 11; research/POSITIONING.md
---

## Profile

Display name: UCompute
Bio (256 characters max): Automated account for the UCompute project: run small open AI models on your own devices. Apache-2.0; source not yet published; in development, no public release. Written by software from the project's engineering evidence. Contact: hello@ucompute.org
Settings: Account → Automation label ON.

## Post 1 (pinned; one post, not a thread)

In development; no public release or download yet.

UCompute pairs your own devices with a short code. A paired device refuses off-device work until you allow it, and each off-device request is logged without the prompt. Each request runs whole on one device.

## Post 2 (day 2; links the pairing note)

How two UCompute devices pair: a six-digit code, SPAKE2, and a confirmation bound to the TLS session and both device keys, so a relay in the middle fails.
https://ucompute.github.io/notes/2026-10-30-pairing-explainer.html

## Post 3 (day 4; links the audit note)

UCompute's audit log refuses fields named prompt or messages, and writes the "sent" line before a request leaves the device. Tested on one computer; scope in the note:
https://ucompute.github.io/notes/2026-10-30-what-the-audit-log-records.html

## Post 4 (day 6; links the RPC note)

llama.cpp's RPC README: "the functionality is fragile and insecure." UCompute keeps llama.cpp on loopback and does not use RPC, so a model must fit one device.
https://ucompute.github.io/notes/2026-10-31-loopback-rpc-vs-authenticated-transport.html

## Post 5 (day 8; links the memory-fit note)

How UCompute estimates whether a GGUF fits: weights, KV cache, compute buffers, tokenizer tables. Dev build, one Apple M2 Mac, models up to 1.5B: -4.6 % to +8.9 % of measured peak, 14 combinations.
https://ucompute.github.io/notes/2026-11-01-memory-fit-explainer.html

## Rules for this account
- At most one post a day and four a week; reply only to mentions and to replies on its own posts; never search-and-reply.
- Every post is under 300 characters including the link; check with `python3 -c "print(len(open('post.txt').read()))"` before posting.
- The device that runs your request processes your prompt: any reply about privacy carries that sentence.
