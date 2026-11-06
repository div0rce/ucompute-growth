---
id: bluesky-queue
title: Bluesky profile and queue (@ucompute.org)
type: social-post
audience: multi-device-developers, local-ai-developers, oss-infra
channel_intent: Bluesky @ucompute.org (owner's grant)
claims: [no-release, run-local, mesh-pair-choose, connect-by-address, catalog-fit, planned, split-design, pairing-code, obs-keepalive, obs-soak-kills, obs-soak-miss, obs-wifi-drop, obs-dev-mac, obs-spake2]
status: ready
review: independent fact-check 2026-11-06, 16 findings applied. Re-check "last run" (post 15) and the crate version (post 21) on their posting dates
sources: evidence/upstream/ (see each claim and observation id); charter/VOICE.md
---

Voice: `charter/VOICE.md`. Published posts are in `analytics/bluesky-posted.jsonl`. Dates are floors, not appointments: anything real and new goes on top. Heading tokens: `pinned`, `reply to post-N`, `not before YYYY-MM-DD`.

## Profile

Display name: UCompute
Bio (256 characters max): Open models on hardware you own, and your own devices handing work to each other. In development, no public release yet. Learning more about Wi-Fi than we planned to. Notes: ucompute.github.io/notes
Settings: Account → Automation label OFF (owner's instruction, 2026-11-06). Never say or imply a human is at the keyboard.

## Post 9 (reply to post-4; correction)

Correction to the post above: "does not use RPC" was too broad. Mesh requests don't. Our work on splitting one model between two devices does, with both ends on loopback and the bytes inside the paired connection. That's a design under test, not a feature.

## Post 10 (pinned; not before 2026-11-07)

We're building UCompute: open models on hardware you own, and your own devices handing work to each other. There's no public release yet. For now it's mostly soak tests, Wi-Fi surprises and writing down what broke.

## Post 11 (not before 2026-11-10)

About 0.5% of burst requests died with "connection closed before message completed". Our client was reusing idle connections that llama-server had already closed. We stopped reusing them: 0 failures in 43,000 admitted requests on one test machine. We still don't know why it closes them.

## Post 12 (not before 2026-11-11)

A shared API key tells a server someone has the key. It can't say which machine is asking, and you can't take it back from just one of them.

## Post 13 (not before 2026-11-13)

Some campus Wi-Fi drops multicast between clients, so mDNS never finds the laptop sitting next to you. That's why paired devices can also connect by plain address. An address alone is never trusted: the device still has to present the key it was paired with.

## Post 14 (not before 2026-11-14)

Wrote down how five local AI servers decide whether to answer a request. Four different answers, in their own words.
https://ucompute.github.io/notes/2026-11-07-shared-api-key-is-not-device-trust.html

## Post 15 (not before 2026-11-17)

Our 24-hour soak SIGKILLs the engine every 50 cycles, on purpose. Last run, one test machine, tiny test model: 2,607 kills, back within a second each time.

## Post 16 (not before 2026-11-18)

In an earlier soak, two requests out of 5.3 million got no answer and no error within our test client's 120 seconds. That fails a soak by our own rule. Best theory: the client gave up before the daemon's own timeout could fire. Still a theory.

## Post 17 (not before 2026-11-20)

llama.cpp's RPC README says the functionality is "fragile and insecure", right at the top. More projects should write docs like that.

## Post 18 (not before 2026-11-24)

One of our test machines dropped off the network more than once overnight without rebooting. Most likely Ubuntu's default Wi-Fi power saving. We turned it off. The fallback plan is a cable, which is also the fallback plan for most things.

## Post 19 (not before 2026-11-25)

A lot of this gets built and tested on a MacBook Air with 8 GB of memory. Good for keeping "small model" honest. Bad for running a release build and a model at the same time.

## Post 20 (not before 2026-11-27)

File size is a bad guess at whether a model fits. Weights are only part of it. Our estimate lands between -4.6% and +8.9% of measured peak, on one M2 Mac with small models, and the low end is the one that hurts.

## Post 21 (not before 2026-12-01)

The SPAKE2 crate in our pairing flow is three years old, unaudited, and says itself it's probably not constant-time. We took it because the secret lives 120 seconds and long-term trust sits on TLS 1.3 and pinned keys. Still on the list to revisit.

## Rules for this account
- Ceilings, not targets: one post a day and four a week. Corrections and the pinned post don't count against the week.
- Reply only to mentions and to replies on our own posts. Never search-and-reply.
- Any reply about privacy says that the device running a request processes the prompt.
