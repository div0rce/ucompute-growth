---
id: 2026-11-07-shared-api-key-is-not-device-trust
title: "A shared API key is not device trust: what local AI servers check, in their own words"
type: explainer
audience: multi-device-developers, local-ai-developers
channel_intent: github-org (notes site), website-handoff, later syndication with canonical link
claims: [no-release, mesh-pair-choose, transport, device-sees-prompt, local-only, revocation, audit, connect-by-address, platforms]
status: ready
review: independent fact-check (fresh subagent, scripts/prompts/factcheck.md) 2026-11-05, 15 findings (1 blocker, 4 major, 10 minor), all applied; LM Studio serve-on-network sentence quoted as rendered (source line 20 links 'authentication')
publish_after: 2026-11-07
sources: Ollama authentication docs https://github.com/ollama/ollama/blob/main/docs/api/authentication.mdx and FAQ https://github.com/ollama/ollama/blob/main/docs/faq.mdx (read 2026-11-05 via raw.githubusercontent.com, ollama/ollama main at a6d3325); llama.cpp server README https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md (read 2026-11-05 via raw.githubusercontent.com, ggml-org/llama.cpp master at 10d4846); Jan local API server docs https://github.com/janhq/jan/blob/main/docs/src/pages/docs/desktop/api-server.mdx (source of https://docs.jan.ai/desktop/api-server; read 2026-11-05 from a clone of janhq/jan at d7f72c4); LM Studio docs https://github.com/lmstudio-ai/docs files 1_developer/0_core/authentication.mdx and 1_developer/0_core/0_server/serve-on-network.mdx (sources of https://lmstudio.ai/docs/developer/core/authentication and .../server/serve-on-network; read 2026-11-05 from a clone at 8c7159b); exo issue https://github.com/exo-explore/exo/issues/1833 (quoted in research/raw/competitors-positioning.md, read 2026-10-30; github.com issue pages not reachable from this session on 2026-11-05); UCompute: claims/REGISTRY.md (no-release, mesh-pair-choose, transport, device-sees-prompt, local-only, revocation, audit, connect-by-address)
---

# A shared API key is not device trust: what local AI servers check, in their own words

*Written 5 November 2026. Every quotation below is from the project's own documentation as read that day (one, from exo, was read on 30 October 2026); documentation changes, so check the current page before relying on it. UCompute is in development. There is no public release or download yet.*

When you let a second computer use the model server on your desktop, the server has to decide, for every request, whether to answer. The five local AI servers quoted here make that decision in one of four ways. This note sets them side by side, quoting each project, and then says what each way can and cannot tell you. It does not rank the projects. Ollama, llama-server, Jan and LM Studio listen only on your own computer by default, and that is the safe starting point.

## The four answers

| What the server checks | Project and its own words |
|---|---|
| **Nothing; add your own in front** | Ollama: "The local API at `http://localhost:11434` does not require authentication." and "Ollama binds 127.0.0.1 port 11434 by default." and "Ollama runs an HTTP server and can be exposed using a proxy server such as Nginx." exo, in a reply from a project member closing an issue about unauthenticated endpoints (read 30 October 2026): "this is intended behaviour, exo's api is unauthorized" and "run exo behind a reverse proxy and provide your own authentication if you wish to expose it downstream." |
| **One shared key** | Jan: "If a key is configured, requests must include it in the `Authorization: Bearer YOUR_API_KEY` header." and "Jan refuses to start the server on `0.0.0.0` (or any address other than your own computer) without a key." |
| **A list of keys** | llama.cpp `llama-server`: `--api-key` is the "API key to use for authentication, multiple keys can be provided as a comma-separated list (default: none)"; `--api-key-file` reads "API keys, one per line". `/health` "is public (no API key check)". |
| **Named tokens with permissions** | LM Studio: "By default, LM Studio does not require authentication for API requests." When you turn it on, you create tokens: "Provide a name for the token and select the desired permissions." Its page on serving to the network says: "Any bind other than `127.0.0.1` exposes the server beyond `localhost`; we recommend enabling authentication." |

Ollama, llama-server, Jan and LM Studio each document `127.0.0.1` as the default; Jan and LM Studio also warn against leaving it without a key or token. The rows differ in what happens once you bind to something else.

## What a key tells the server, and what it does not

A bearer key answers one question: does this request carry a secret the server knows? That is worth having. It stops the casual case, a neighbour's laptop or a scanner that finds the port.

It does not answer other questions you may care about once more than one device uses the server:

- **Which device sent this?** With one shared key, every device that holds it looks the same to the server. If the key is in your laptop's shell profile, in a notebook on a lab machine and in a phone app, the server cannot tell those apart.
- **How do I stop one device?** With one shared key, you change the key and then give the new one to every device you still want. With a list of keys (llama-server) or named tokens (LM Studio), you can give each device its own and remove one (LM Studio's token list lets you delete a token; with llama-server you edit the list or key file and restart the server); that is the reason to prefer them, and to use one key per device rather than one key for all.
- **Who could read the key on the way?** The examples on these pages use `http://` URLs: `http://127.0.0.1:1337` (Jan), `http://localhost:1234` (LM Studio), `http://127.0.0.1:9931` (llama-server). Over plain HTTP, the key and the prompt cross the network as readable text to anything positioned to see the traffic. On loopback that path never leaves your computer; on Wi-Fi it does. llama-server documents `--ssl-key-file` and `--ssl-cert-file` and a build "with SSL support using OpenSSL 3"; for the others, check the current documentation, or keep the server on loopback and reach it through an SSH tunnel or a VPN overlay ([how those work](2026-11-04-other-computer-without-open-port.md)).
- **What was asked from where?** A key check accepts or refuses. Jan and llama-server document request and prompt logging for debugging; a per-device record of requests that leaves the prompt out is not something the pages quoted above describe.

None of this makes keys a bad idea. If you serve a model to other devices today, use a key, one per device where the server allows it, keep `/health`-style public endpoints in mind, and prefer a tunnel or overlay to an open port.

## A five-minute checklist for a server you already expose

1. Find out what it is listening on: the [sixty-second self-check](2026-11-03-what-0000-exposes.md) has the command for each operating system.
2. If it is not on `127.0.0.1`, turn on its key or token setting, using the wording on its own documentation page; Ollama and exo document none for their local API, so put a reverse proxy with authentication in front, as exo's reply suggests.
3. Give each device its own key where the server supports more than one (llama-server's comma-separated list or key file; LM Studio's named tokens).
4. Write down which key went where, so you can remove one without rotating all of them.
5. If the traffic crosses Wi-Fi as plain HTTP, move it into a tunnel or an overlay.

---

## How UCompute approaches the same question (development build, October 2026)

*This section describes UCompute. UCompute is in development. There is no public release or download yet.*

UCompute Mesh lets you pair your own devices with a short code and choose which one runs a request. Each request runs whole on one device; UCompute does not split a model across devices. (Tested with development builds between one Apple M2 Mac and one Windows 11 laptop (Intel Arc 140V) on the same Wi-Fi network or phone hotspot, and between that Mac and one Linux desktop computer (Ubuntu, processor only, a development build of the background program compiled and started by hand; no app or installer) on a home Wi-Fi network. Linux is a planned platform, not a supported one. Pairing between two Macs is not yet shown to work.)

**Who is on the other end.** Traffic between paired devices is encrypted and both ends are authenticated: QUIC with TLS 1.3 and device keys pinned at pairing. Your device will not send work to a device you have not paired. A device you have not paired cannot send you work; that was tested with several instances on one computer, not yet between two machines. Where a network blocks automatic discovery, as some campus Wi-Fi does, paired devices can still connect by address. An address alone is never trusted: the device must present the key it was paired with. Reconnecting by address was shown between one Mac and one Windows laptop on the same campus network, with development builds.

**The device that runs the request sees the prompt.** The device that runs your request processes your prompt. Pair only devices you control or trust.

**Whether anything leaves at all.** Your prompts and responses stay on your device unless you pair another device and choose to run a request there. Local-only mode refuses every off-device request. Downloading a model or the engine uses the internet.

**How to stop one device.** You can revoke a paired device at any time. In our two-machine tests (development builds, October 2026; a Mac paired with a Windows laptop and with a Linux desktop computer), its connection closed less than a tenth of a second after the revoke (between 0.002 s and 0.061 s in four runs), and its next request was refused.

**What was asked from where.** Audit logs record each off-device request without the prompt or the response. ([What the audit log records](2026-10-30-what-the-audit-log-records.md).)

### What this does not do

- It does not replace a key on a server you already run. UCompute's pairing applies only between UCompute devices; an Ollama, exo, llama-server, Jan or LM Studio server you expose keeps whatever check it has.
- It has not been shown across the internet. The evidence covers devices on the same local network only.
- No platform is declared supported yet. macOS 26.2 on Apple M2 and Windows 11 on an Intel Core Ultra 7 258V with Arc 140V are experimental; Linux, other GPUs and phones (as clients) are planned.

Corrections and private security reports: hello@ucompute.org.
