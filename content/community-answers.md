---
id: community-answers
title: Community answers: what developers ask about UCompute, answered from the evidence
type: community-answer
audience: all
channel_intent: any AUTHORIZED channel; adapt per thread; never paste verbatim across threads
claims: [no-release, run-local, engine, mesh-pair-choose, license, planned, private-alpha, transport, local-only, audit, audit-detail, device-sees-prompt, openai-clients, connect-by-address, platforms, revocation, windows-firewall, catalog-fit, demo-2026-10-19]
status: ready
sources: claims/REGISTRY.md (snapshot 2026-10-23b draft 3, updated 2026-10-30); claims/PROHIBITED.md; content/README.md; research/POSITIONING.md sections 1 to 6; research/AUDIENCES.md section 3; research/BARRIERS.md section 2; research/SEARCH.md sections 2 and 5.4; research/COMPETITORS.md; the five pieces in content/ready/ (pairing explainer, audit-log note, RPC comparison, memory-fit explainer, OpenAI base-URL page). Every competitor quotation carries the URL its research file read it from on 2026-10-30.
---

# Community answers

Internal bank, written 2026-10-30. Truthful, ready-to-adapt answers to the questions developers actually ask, for use in forum threads, issues and replies once a channel is AUTHORIZED in `channels/REGISTRY.md`. On 2026-10-30 no channel is authorized and nothing here may be posted.

## How to use this bank

- Post only in an AUTHORIZED channel, under that channel's rules. Hacker News bans generated text and automated posting; dev.to bars AI-assisted posts that promote the author's own project; Lobsters treats text without meaningful human authorship as spam. An automated account does not post there at all.
- The first line of any reply is the status: "Development build, October 2026. UCompute is in development; there is no public release or download yet."
- Adapt every answer to the thread. Answer the question that was asked, cut what does not apply, keep the qualifier beside every claim, and never paste the same text into two threads.
- The five ready notes are referenced by title because they have no public URL yet (website handoff pending). Add the link only when the site publishes them.
- Competitors are quoted only in their own documented words, with the URL. Never call a project insecure. Never say UCompute is faster, safer, more private or stronger than anything.
- Write "UCompute Mesh" as two words, never "Mesh" alone, with "each request runs whole on one device" in the same or the next sentence; the word collides with Mesh LLM and other projects.
- Disclosure line, required whenever the account posting is automated: "This reply was written by UCompute's automated growth account from the project's published evidence; it is not a human maintainer."
- Run `python3 scripts/claims_lint.py content/community-answers.md --strict` after any edit.

## Theme 1. What UCompute is and is not

### Q1. What is UCompute, in one paragraph?

**Answer.** Status first: UCompute is in development; there is no public release or download yet. UCompute Run runs small open models on your own computer, with no account and no UCompute service; by default your requests stay on your device (demonstrated on one Apple M2 Mac, macOS 26.2, and one Windows 11 laptop with an Intel Arc 140V GPU, both experimental; downloading a model or the engine uses the internet). Models run through a pinned release of llama.cpp (MIT), verified against a pinned SHA-256 hash; UCompute writes no inference kernels of its own. UCompute Mesh lets you pair your own devices with a short code and choose which one runs a request. Each request runs whole on one device (development builds, one Mac with one Windows laptop and with one Linux desktop; Linux is planned, not supported). The code is Apache-2.0; the source has not been published yet. [claims: no-release, run-local, engine, mesh-pair-choose, license]

### Q2. Can I combine two machines to run a larger model?

**Answer.** No. Each request runs whole on one device you choose and does not pool memory. If a model does not fit the device you pick, it will not run there. That is a limitation, stated plainly: whole-request routing cannot run a model larger than the chosen device. Running one model across several devices is planned, with no date, and is not a feature. If partitioning is what you need now, llama.cpp's RPC backend and exo do that; see the note 'What llama.cpp's own README says about its RPC backend, and what UCompute does instead' for the trade-offs in the llama.cpp project's own words. The reason for whole requests is an engineering position resting on others' measurements, not a speed claim: Apple's MLX team writes that pipeline parallelism "does not speed up decode" (https://machinelearning.apple.com/research/mlx-distributed-inference). [claims: mesh-pair-choose, planned]

### Q3. Is it released? Where is the download, and where is the code?

**Answer.** Nowhere yet. UCompute is in development; there is no public release or download yet. UCompute's code is licensed under Apache-2.0; the source has not been published yet (both sentences travel together). A private alpha build for macOS on Apple Silicon exists for an owner-managed cohort; it is not a public release and is not open for sign-up, so there is no link to give and no list to join. This account does not hand out builds in threads, name testers or their number, or give dates: the only wording for anything unbuilt is "planned, with no date". Until the registry changes, the honest answer to "when" is that no date exists, and the honest answer to "where is the code" is that a LICENSE is what exists publicly today. [claims: no-release, license, private-alpha]

## Theme 2. Using a second computer on the LAN safely

### Q4. How do I use my desktop's GPU from my laptop without binding the server to 0.0.0.0 and opening the port to everyone on the Wi-Fi?

**Answer.** Limits first: both machines run UCompute development builds on the same local network; no relay, no NAT traversal; the model must fit the desktop. UCompute Mesh lets you pair your own devices with a short code and choose which one runs a request; each request runs whole on one device. Traffic between paired devices is encrypted and both ends are authenticated: QUIC with TLS 1.3 and device keys pinned at pairing. Your device will not send work to a device you have not paired, and the paired desktop still refuses off-device requests until you allow it. Each off-device request is logged without the prompt or the response. Your app keeps talking to the local API on your own laptop. The desktop processes your prompt, so pair only devices you control or trust. Tested between one Apple M2 Mac and one Windows 11 laptop (Intel Arc 140V); two Macs are not yet shown to pair. See the note 'How two UCompute devices pair, allow, audit and revoke: the six-digit code and the pinned keys'. [claims: mesh-pair-choose, transport, local-only, audit, device-sees-prompt]

### Q5. Can a device on my network that I did not pair send prompts to my machine, or read answers?

**Answer.** Qualifier first: "A device you have not paired cannot send you work" has been tested with several instances on one computer, not yet between two machines; the check that captured traffic carries no readable prompt text also ran on one computer. What is built: traffic between paired devices is encrypted and both ends are authenticated, QUIC with TLS 1.3 and device keys pinned at pairing; if a key is not pinned, the handshake fails before any application data moves. Pairing alone grants no permission: local-only mode refuses every off-device request, and a paired device serves work only after you turn serving on. Peer networking is off by default and nothing listens beyond loopback until you turn it on. A refused connection is written to the audit log as a structured line with the other device's id, never the content. [claims: transport, local-only, audit-detail, device-sees-prompt]

### Q6. My two devices cannot see each other on campus or guest Wi-Fi. And can I reach my desktop from outside my network, or from my phone?

**Answer.** Outside the network: no. The evidence covers two devices on the same local network; there is no relay, no NAT traversal and no phone client (phones as clients are planned). If you use Tailscale for the away case, keep using it; UCompute makes no claim there. On the same network with discovery blocked: where a network blocks automatic discovery, as some campus Wi-Fi does, paired devices can still connect by address. An address alone is never trusted: the device must present the key it was paired with. That was shown between one Mac and one Windows laptop on one campus network, with development builds. Where client isolation also blocks direct traffic between devices, pairing will not work; that is the same limit flux #127 states for its own design (https://github.com/bjarneo/flux/issues/127). [claims: connect-by-address, platforms, mesh-pair-choose]

### Q7. How do I remove a device, and what does revoke actually do?

**Answer.** You can revoke a paired device at any time. In our two-machine tests, its connection closed less than a tenth of a second after the revoke (between 0.002 s and 0.061 s in four runs), and its next request was refused. Mechanically, a revocation is a signed record: every open connection to the revoked device closes, its key is refused inside the next TLS handshake, and because UCompute issues no session tickets there is no cached session to come back with. The revocation is also copied to a separately rotated security trail, so a flood of requests cannot rotate it away. Parity, stated as parity: NVIDIA PAIR documents removing a node from another node's settings page, which any member can do (https://github.com/NVIDIA/Personal-AI-Router); UCompute's specific is the measured close and the refusal inside the handshake. See the note 'How two UCompute devices pair, allow, audit and revoke: the six-digit code and the pinned keys'. [claims: revocation, audit-detail]

### Q8. What does Windows ask me when I pair?

**Answer.** Scope first: shown in October 2026 on one Windows 11 laptop with a development build; later builds have not been re-checked. On Windows, UCompute asks before it lets your paired devices reach it through the firewall, and the rule it adds covers only its own program, on private networks. Windows asks for administrator approval for that rule. Nothing is opened for other programs. For comparison in its own words, NVIDIA PAIR's getting-started page says its Windows installer adds firewall rules and that Linux users open the ports by hand (https://docs.nvidia.com/local-ai/nvpair/getting-started/). Whether UCompute shows a reason when a paired device cannot be reached through a firewall is unverified, so this account does not describe that case. [claims: windows-firewall]

### Q9. What happens when the strong machine sleeps mid-request, or when the two devices run different versions?

**Answer.** Honest answer: neither is covered by the evidence. No registry row describes what the requesting device shows when the chosen device stops answering (sleep, lid close, network loss), whether an in-flight request is reported as failed, or whether a version mismatch between two paired UCompute devices is detected and shown. There is no auto-update. These are open questions for Engineering, recorded in the project's barriers research, and this account does not guess at them. For context in other projects' own words: NVIDIA PAIR says "Updates are manual and per machine" and that all nodes should run the same version (https://docs.nvidia.com/local-ai/nvpair/getting-started/); exo's PR #2419 added a notice after peers on different versions silently dropped each other (https://github.com/exo-explore/exo/pull/2419). [claims: no-release; no registry row covers sleep or version drift]

## Theme 3. Privacy and what the executing device sees

### Q10. Do my prompts leave my machine, and what outbound connections does it make?

**Answer.** Your prompts and responses stay on your device unless you pair another device and choose to run a request there; local-only mode refuses every off-device request. Downloading a model or the engine uses the internet: the pinned llama.cpp release is fetched on first use and verified against a pinned SHA-256 hash, and model files are fetched when you start a download and checked against a pinned SHA-256 hash. There is no account and no UCompute service. The local API listens on 127.0.0.1:8192 by default. What this account cannot give you yet is a complete enumerated list of every outbound host, or a statement about update checks: the registry has no row for that, so the connections page is held until Engineering confirms the list. The device that runs your request processes your prompt; pair only devices you control or trust. [claims: local-only, run-local, engine, catalog-fit, device-sees-prompt]

### Q11. If I run a prompt on my other machine, does that machine see it? Does the encryption hide it?

**Answer.** Yes, it sees it. The device that runs your request processes your prompt. Pair only devices you control or trust. Encryption protects the traffic from observers on the network, not from the endpoint: traffic between paired devices is encrypted and both ends are authenticated (QUIC with TLS 1.3, device keys pinned at pairing), and the check that captured traffic carries no readable prompt text ran on one computer. So UCompute uses no privacy absolutes about prompts: downloads use the internet, and the executing device reads what it runs. What is built is a policy with a default: your prompts and responses stay on your device unless you pair another device and choose to run a request there. Mesh LLM's maintainers at Block state the same property of their own design: prompts "sent to another machine are visible to that machine's owner" (https://engineering.block.xyz/blog/buzz-sharing-compute-powered-by-meshllm). [claims: device-sees-prompt, transport, local-only]

## Theme 4. The audit log

### Q12. Is the audit log going to contain my prompts? What is in it?

**Answer.** No. Audit logs record each off-device request without the prompt or the response. The trail is a file of JSON lines (`logs/audit.jsonl`) with a UTC timestamp, an event kind, the other device's id and structured fields: ids, sizes, reasons, durations. The writer refuses fields named prompt, content, messages, api_key, private_key or pkcs8 and any string over 2 KiB. The sent line is written before the request leaves the device; if it cannot be written, nothing is sent. The file rotates at 8 MiB with three rotated files kept; owner actions and revocations are copied to a separately rotated security trail; refused-connection lines are capped at 20 per minute. Local-only work writes no line. Scope: mechanics held by automated tests on one computer (development build, October 2026); absence of prompt text checked in the two-machine runs; on Windows, second-account access is untested. See the note 'What UCompute's audit log records, and what it never records'. [claims: audit, audit-detail, local-only]

## Theme 5. Memory fit and downloads

### Q13. Which model and quant fits my memory, and how does UCompute decide?

**Answer.** Limits first: the estimate is calibrated for Apple Silicon Macs on one engine release and on models up to 1.5 billion parameters; nothing larger has been measured; Windows uses the macOS figures as a placeholder; demonstrated on one Apple M2 Mac (macOS 26.2), experimental. Before you download a model, UCompute shows its size, its license and whether it fits in your computer's memory. Before the download it knows only the file size, so that verdict is a lower bound: weights plus the engine's fixed baseline. After the download, the full estimate adds KV cache (context capped at 4,096 tokens), compute buffers and tokenizer tables against the memory free at that moment, keeps ten percent spare, and runs again before every load. Across 14 combinations on that Mac, stories260K to qwen2.5-1.5b, the estimate landed between 4.6 % below and 8.9 % above the measured peak (llama.cpp b11609). Whether a "does not fit" verdict can be overridden is unverified. See the note 'Before you load a model: how UCompute estimates whether a GGUF fits'. [claims: catalog-fit, engine, platforms]

### Q14. Are downloads verified, and against what?

**Answer.** Every model download is checked against a SHA-256 hash pinned in UCompute's catalog, after the download and before the engine opens the file. The engine itself is a pinned release of llama.cpp (MIT), downloaded on first use and verified against a pinned SHA-256 hash; UCompute refuses to start it if the archive's hash does not match. Demonstrated on an Apple M2 Mac (macOS 26.2); the platform is experimental. A hash check proves the bytes you received match the pinned value; it does not prove who published the model or that the model is safe to run. Unverified, so not claimed: whether files already on disk are re-hashed before every load, what you see on a mismatch, and whether interrupted downloads resume. With any other tool, `shasum -a 256`, `Get-FileHash` or `sha256sum` compares a file against a publisher's hash. [claims: catalog-fit, engine]

## Theme 6. OpenAI-client compatibility

### Q15. What is the base URL, the port and the API key?

**Answer.** `ucompute serve` starts the local API on `127.0.0.1:8192`; the OpenAI routes are under `/v1`, so the base URL is `http://127.0.0.1:8192/v1`. By default only programs on the same computer can reach it; it does not listen on your network address unless you configure it to. UCompute's local API works with the official OpenAI Python and JavaScript client libraries; only the base URL changes. Demonstrated on an Apple M2 Mac (macOS 26.2); the platform is experimental. Chat and completions with streaming; tool calling is not yet verified. The client libraries require a non-empty API key string even when a server ignores it, so pass a placeholder and never commit a real cloud key. Model ids come from `GET /v1/models` on your server, not from cloud model names. The server also serves an OpenAPI 3.1 document at `/openapi.json`. See the note 'Point the official OpenAI Python and JavaScript clients at a local server'. [claims: openai-clients, run-local]

### Q16. Tool calling, `/v1/responses`, embeddings: which are verified and which are not?

**Answer.** Tool calling is not yet verified; chat and completions with streaming are verified with the official OpenAI Python and JavaScript clients (demonstrated on an Apple M2 Mac, macOS 26.2, experimental). Whether `/v1/responses` or an embeddings endpoint exists is unverified, and this account does not guess; it is an open question for Engineering. The same goes for which request fields are honoured, ignored or rejected, the default context window and how many concurrent requests the server takes. If you are wiring the OpenAI Agents SDK, Codex or a framework that needs the Responses API, do not expect it to work until an answer is published. On a development build, the OpenAPI 3.1 document at `/openapi.json` lists the routes and the request fields each one reads; that document, not this reply, is the authoritative check. [claims: openai-clients]

## Theme 7. Platforms and release status

### Q17. Is there a Linux build, a Docker image or a phone app?

**Answer.** No, no and no. No platform is declared supported yet. macOS 26.2 on Apple M2 and Windows 11 on an Intel Core Ultra 7 258V with Arc 140V are experimental; Linux, other GPUs and phones (as clients) are planned. What exists for Linux: in the two-machine tests, one Linux desktop (Ubuntu, processor only) ran a development build of the background program compiled and started by hand, with no app or installer; Linux is a planned platform, not a supported one. There is no package, no container image, no GPU path on Linux and no mobile client. The homelab pattern of a Linux GPU box serving clients is exactly the one UCompute cannot serve today, and this account says so rather than hedging. [claims: platforms, mesh-pair-choose, no-release]

### Q18. Does it run on my Mac or my GPU? What does "supported" mean here?

**Answer.** Nothing is supported; two machines are demonstrated. No platform is declared supported yet. macOS 26.2 on Apple M2 and Windows 11 on an Intel Core Ultra 7 258V with Arc 140V are experimental; Linux, other GPUs and phones (as clients) are planned. UCompute says "demonstrated on" with the machine named instead of "supported", and it does not extend a result from one chip to a family: other Apple chips, other macOS versions and other GPUs have not been tested. The engine is llama.cpp, which has backends for many devices, but which of them UCompute's builds enable on other hardware is not something the evidence covers. Memory-fit estimates are calibrated for Apple Silicon Macs, on the M2 that was measured. If your hardware is not one of the two machines above, the truthful answer is "not tested". [claims: platforms, run-local, catalog-fit]

## Theme 8. Comparisons

### Q19. Why not Ollama?

**Answer.** For one machine, Ollama does what UCompute Run does and ships on macOS, Windows, Linux and Docker; UCompute has no public release. In Ollama's own words: "Ollama binds 127.0.0.1 port 11434 by default. Change the bind address with the `OLLAMA_HOST` environment variable" (https://docs.ollama.com/faq); "The local API at `http://localhost:11434` does not require authentication" (https://docs.ollama.com/api/authentication); on built-in auth, the maintainers said "add an authenticating proxy in front of Ollama" (https://github.com/ollama/ollama/issues/849). UCompute's documented differences, as facts: the path to a second device is pairing, not an open port; off-device requests go only to a device you paired, over QUIC with TLS 1.3 and pinned keys, and a paired device still refuses them until allowed; each off-device request is logged without prompt text; size, license and memory-fit are shown before a download; the engine is a pinned llama.cpp release, named and credited. No speed comparison exists. [claims: transport, local-only, audit, catalog-fit, engine, no-release]

### Q20. Why not LM Studio's LM Link?

**Answer.** Status first for both: LM Link is "in Preview" per its own page; UCompute has no public release. In LM Studio's words: "Link your machines, and then load remote models as if they were local" (https://lmstudio.ai/link); "All communication and data transfer between devices is always end-to-end encrypted, thanks to Tailscale" (https://lmstudio.ai/docs/lmlink); "The LM Studio Hub is only used to facilitate discovery" (https://lmstudio.ai/docs/lmlink/basics/faq). LM Link is ahead on shipped platforms, reach across networks through Tailscale, and iPhone and iPad through Locally. Where UCompute differs, as facts: no account and no vendor server in the pairing path; pairing is a short code between two devices on one local network, with device keys pinned at pairing; same network only and no relay, which is a limitation; Apache-2.0, source not yet published. Per-device removal in LM Link is unverified from the pages read, so no comparison is made on revoke. [claims: mesh-pair-choose, transport, license, no-release]

### Q21. Why not NVIDIA PAIR?

**Answer.** PAIR is the closest comparable, and it is shipped: v1.0.0 with installers for Windows, Linux and macOS, using Ollama, LM Studio or llama.cpp as the engine; UCompute has no public release. In PAIR's own words: "a local inference router for a group of compatible computers on the same network"; "PAIR routes each independent request to one node" (https://github.com/NVIDIA/Personal-AI-Router). Parity, stated as parity: whole request to one device; PIN-based pairing; encrypted authenticated transport; per-device removal; add-by-address when discovery fails; a Windows firewall step. Differences as facts, not a ranking: device keys pinned at pairing, with the handshake failing before application data if a key is not pinned; revoke measured at 0.002 s to 0.061 s in four runs, next request refused; a paired device refuses off-device work until allowed; a documented audit log with the fields it refuses; a pinned llama.cpp run by UCompute itself rather than another runner. PAIR's own SECURITY.md says "The six-digit PIN is low entropy" (https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md): quote it and stop. [claims: mesh-pair-choose, transport, revocation, local-only, audit-detail, engine, windows-firewall, connect-by-address]

### Q22. Why not Mesh LLM?

**Answer.** Different target. In Mesh LLM's own words: "Share compute privately or publicly to power your agents and chat"; "experimental distributed-systems software"; "If one node can host the full model, it serves the model locally without stage traffic"; "QUIC end-to-end encrypts traffic between Mesh nodes" (https://github.com/Mesh-LLM/mesh-llm). It is ahead on shipped builds for macOS, Linux and Windows, a split mode, relays through iroh beyond the local network, public meshes and certificate rotation. UCompute Mesh is narrower: your own devices only, one local network, no public mesh, no relay; each request runs whole on one device; per-device keys pinned at pairing instead of a shared invite token; an audit log of each off-device request without the prompt or the response. Both projects say the same about running elsewhere: Block's engineers write that prompts "sent to another machine are visible to that machine's owner" (https://engineering.block.xyz/blog/buzz-sharing-compute-powered-by-meshllm); UCompute says the device that runs your request processes your prompt. [claims: mesh-pair-choose, transport, audit, device-sees-prompt]

### Q23. Why not exo?

**Answer.** exo solves a different problem. In its own words: "Run frontier AI locally"; it "figures out the best way to split your model across all available devices"; "Guest Wi-Fi and some office networks may block device discovery" (https://github.com/exo-explore/exo); on authentication, a maintainer wrote "this is intended behaviour, exo's api is unauthorized" (https://github.com/exo-explore/exo/issues/1833). If you need one model spread over several machines, exo does that and UCompute does not: each request runs whole on one device, so it cannot run a model larger than the device you choose. What UCompute adds for the two-devices-you-own case: pairing is authenticated with device keys pinned at pairing, and where discovery is blocked, paired devices connect by address with the key still required. The whole-request choice rests on others' measurements, not a speed claim: Apple's MLX team writes that pipeline parallelism "does not speed up decode" (https://machinelearning.apple.com/research/mlx-distributed-inference). [claims: mesh-pair-choose, transport, connect-by-address]

### Q24. Why not llama-server or llama.cpp's RPC backend? Is UCompute just a wrapper?

**Answer.** Partly yes, and it says so: UCompute runs models through a pinned release of llama.cpp (MIT), verified against a pinned SHA-256 hash; UCompute does not write its own inference kernels. For one machine, llama-server does what UCompute Run does and more (`--api-key`, `--fit` on by default, Responses routes, a web UI; https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md). UCompute's distinct part is the paired-device policy layer and the pre-download fit verdict. On RPC, the llama.cpp authors' own words: "the functionality is fragile and insecure. Never run the RPC server on an open network or in a sensitive environment!" (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md). UCompute never exposes an RPC server; its engine runs on loopback with a per-process key, and what crosses the network is a whole request to a paired device over QUIC with TLS 1.3 and pinned keys. RPC can run a model larger than one machine; UCompute cannot. See the note 'What llama.cpp's own README says about its RPC backend, and what UCompute does instead'. [claims: engine, transport, mesh-pair-choose]

## Theme 9. The name

### Q25. Is this the uCompute RP2040 project? Or Universal Compute? Or a token?

**Answer.** No. UCompute (ucompute.org) runs small open AI models on your own computer and pairs your own devices so one can run a request for another; each request runs whole on one device. It is in development with no public release yet; Apache-2.0, source not yet published. It is not related to the uCompute RP2040 boards and rover on GitHub (https://github.com/JPMichon/RP2040_uCompute), not to Extreme Networks' Universal Compute Platform, and not to any token or coin, including Universal Basic Compute. The "credits" in UCompute's stated direction do not exist, are not a token, and do not belong in a technical thread. If a thread is about the RP2040 hardware, this account posts this disambiguation only when asked directly, and nothing else. [claims: run-local, mesh-pair-choose, no-release, license, planned]

## Reusable block: the one two-machine run that may be described

Use this exact text, unchanged, whenever a thread asks what has actually run between two machines:

> In a test on 19 October 2026 (UTC), development builds of the desktop app on a MacBook Air (Apple M2, macOS 26.2) and a Windows 11 laptop (Intel Core Ultra 7 258V, Arc 140V) were paired through their own windows on one phone hotspot, and the Windows app ran a prompt on the Mac (the Mac's permission for the laptop to run prompts was set through the Mac's local API, not its window). A request in the other direction, sent through the Mac's local API rather than its app window, ran on the laptop's GPU. Each request ran whole on one device; no model was split. The test model was a 15-million-parameter fixture, so speeds from it are not performance figures.

[claims: demo-2026-10-19]

## Never answer

Decline plainly, state the status line, and stop. Do not improvise around any of these.

- Download links, builds or files: there is no public release or download; never link, send or describe the private alpha file or how to get it.
- Release dates: no date exists for anything; the only wording for unbuilt work is "planned, with no date".
- Benchmarks or speed: never give tokens-per-second figures beyond the registry's path check rows, never answer "how fast" with a number outside them, and never say faster, safer, more private or stronger than any project.
- Pooling, partitioning or running one model across devices as something UCompute does: it does not; the planned work is undated.
- Pricing, credits, payments, compute credits or UCompute Cloud: never discuss cost or a managed service; none of it exists, and direction is never raised in a technical thread.
- Tester counts or the cohort: never name testers, their number, or describe the cohort as open.
- People: never name a founder, maintainer, tester, affiliation, machine or network; the project speaks as UCompute.
- What a revoked device is told: never describe it.
- Signing or notarization status of any build, the installer dialog, admin rights or launch-at-login: no registry row covers them.
- Anything the research marks unverified: `/v1/responses`, embeddings, accepted request fields, sleep and reconnection behaviour, version-mismatch handling, download resume, the complete outbound-connection list, pairing between two Macs.
