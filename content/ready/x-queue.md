---
id: x-queue
title: X queue (not live; no account exists)
type: social-post
audience: local-ai-developers, oss-infra
channel_intent: X through Buffer drafts, only after channels/REGISTRY.md marks X AUTHORIZED
claims: [no-release, transport, connect-by-address, catalog-fit, obs-keepalive, obs-soak-kills, obs-soak-miss, obs-dev-mac]
status: ready
review: PENDING
sources: evidence/upstream/ (see each claim and observation id); charter/VOICE.md
---

Written for X, not copied from Bluesky: shorter, and the number comes first. Limit 280 characters. Nothing here is published until the owner's grant is in the registry.

## Post 1 (pinned)

Open AI models on hardware you own, with work going only to devices you've paired. No release yet. Currently: soak tests and Wi-Fi surprises.

## Post 2

SIGKILL the engine every 50 cycles for 24 hours. 2,607 kills. Back within a second each time.

## Post 3

0.5% of burst requests dying with "connection closed before message completed". Cause: reusing idle connections to llama-server. After the fix, 0 in 43,000. Why the server closes them: still unknown.

## Post 4

A shared API key proves someone has the key. It can't say which machine is asking, and you can't revoke just one.

## Post 5

mDNS doesn't survive some campus Wi-Fi. Multicast gets dropped between clients, so two laptops on the same network never find each other.

## Post 6

Memory estimate vs measured peak: -4.6% to +8.9%, 14 model and context combinations, one M2 Mac. File size alone is a bad guess.

## Post 7

2 requests in 5.3 million: no answer, no error. That fails our soak. Best theory is our own test client timed out first. Unproven.

## Post 8

Dev machine is a MacBook Air with 8 GB. "Small model" means something very specific here.
