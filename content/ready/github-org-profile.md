---
id: github-org-profile
title: GitHub organization profile (ucompute/.github, profile/README.md) and organization description
type: profile
audience: all
channel_intent: GitHub organization ucompute (on the owner's grant)
claims: [run-local, mesh-pair-choose, no-release, license, local-only, audit, device-sees-prompt]
status: ready
sources: research/SEARCH.md 5.4 (disambiguation sentence), research/POSITIONING.md 1 (positioning), distribution/COMMUNITIES.md 9.1 and 11 (disclosure)
---

<!-- Organization description field (160 characters max): -->
<!-- Run small open AI models on your own computer; pair your own devices. In development, no public release. Apache-2.0, source not yet published. -->

# UCompute

UCompute (ucompute.org): run small open AI models on your own computer, and pair your own devices so one can run a request for another. Each request runs whole on one device. In development; no public release yet. UCompute's code is licensed under Apache-2.0. The source has not been published yet. Not related to the uCompute RP2040 boards, Universal Compute products or any token.

**What exists today, in development builds.** UCompute Run runs small open models on your own computer, with no account and no UCompute service. By default, your requests stay on your device. UCompute Mesh lets you pair your own devices with a short code and choose which one runs a request. Each request runs whole on one device; UCompute does not split a model across devices. A paired device still refuses off-device work until you allow it, and audit logs record each off-device request without the prompt or the response. The device that runs your request processes your prompt, so pair only devices you control or trust.

*Demonstrated on an Apple M2 Mac (macOS 26.2) and a Windows 11 laptop with an Intel Arc 140V GPU; both platforms are experimental; other platforms are not yet available, and most are planned. Downloading a model or the engine uses the internet.*

**Read:** [engineering notes](https://ucompute.github.io/notes/) (source: [ucompute/notes](https://github.com/ucompute/notes)): how pairing works, what the audit log records, how the memory-fit estimate works, and what llama.cpp's own README says about its RPC backend.

**Contact:** hello@ucompute.org. Please send anything security-related there rather than posting it publicly.

*Parts of this organization are maintained by UCompute's automated growth workstream, which writes from the project's engineering evidence and is reviewed in scheduled sessions, not in real time.*
