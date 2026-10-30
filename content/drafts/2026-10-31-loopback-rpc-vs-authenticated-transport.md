---
id: 2026-10-31-loopback-rpc-vs-authenticated-transport
title: Why llama.cpp's RPC server stays on loopback, and what UCompute puts around it
type: comparison
audience: local-ai-developers, oss-infra
channel_intent: website-handoff (Engineering notes), later syndication with canonical link
claims: [engine, transport, mesh-pair-choose, planned, device-sees-prompt, no-release, license]
status: draft
sources: https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md (read 2026-10-30); https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md (read 2026-10-30); engineering docs/security/THREAT_MODEL.md section 3 (secure defaults SD-03, SD-07, SD-13); ADR-0002 (supervised engine); capability snapshot 2026-10-23b sections 5, 8 and 9
---

# Why llama.cpp's RPC server stays on loopback, and what UCompute puts around it

*Development build, October 2026. UCompute is in development; there is no public release or download yet.*

llama.cpp is the engine UCompute runs models with: a pinned release of its server, downloaded on first use and verified against its published hash. UCompute does not write its own inference kernels. This note is about one specific part of llama.cpp, the RPC backend, because people who want to use a second computer's GPU from their laptop keep arriving at it, and because the llama.cpp project itself is unusually clear about what it is for.

## What the RPC backend is

The RPC backend lets a llama.cpp process on one host use the accelerator devices of another host over TCP. You start `ggml-rpc-server` on the remote machine, and on the main machine you pass `--rpc host:port` to `llama-cli` or `llama-server`. Model weights and the KV cache are then split across the local and remote devices, by default in proportion to each device's available memory. This is genuine model partitioning: layers live on the remote device and activations cross the wire during each token.

## What its authors say about it

The RPC README, as of 30 October 2026, says three things that matter:

> "This example and the RPC backend are currently in a proof-of-concept development stage."
>
> "As such, the functionality is fragile and insecure."
>
> "Never run the RPC server on an open network or in a sensitive environment!"

The project's security policy adds, under "Untrusted environments or networks":

> "Do not use the RPC backend, ggml-rpc-server and llama-server functionality"

and

> "Encrypt your data if sending it over the network."

That is not a criticism of llama.cpp. The RPC protocol is a plain TCP wire format for moving tensors and compute commands between two processes that trust each other completely. It has no authentication, no encryption and no notion of which device is allowed to talk to which. Its authors say so, and they are right to.

## The trap for the two-computer setup

The trap is that the same command that makes the RPC backend work on a trusted lab network also works on a home network, a shared flat, a dorm, or an office. A port that accepts tensor uploads and compute commands from any source on the network is a large attack surface, and putting it on the LAN is exactly what the README tells you not to do. Wrapping it in a VPN helps with eavesdropping but still leaves every device inside that VPN able to drive the server.

## What UCompute does today

UCompute treats the engine as an untrusted-by-network local process and the network as a separate, authenticated layer:

- **Engine ports never leave the machine.** UCompute runs llama.cpp's server as a supervised child process bound to loopback, with a random per-process API key, and never exposes that port. This is a stated secure default, not a configuration option.
- **The only path between devices is authenticated and encrypted.** Traffic between paired devices is encrypted and both ends are authenticated: QUIC with TLS 1.3 and device keys pinned at pairing. Your device will not send work to a device you have not paired. There is no plaintext peer transport and no downgrade negotiation.
- **A request runs whole on one device.** UCompute Mesh lets you pair your own devices with a short code and choose which one runs a request. Each request runs whole on one device; UCompute does not split a model across devices. In other words, UCompute does not use the RPC backend today at all. What crosses the network is a request to a paired device, which runs it entirely on its own engine and streams the result back.
- **The device that runs your request processes your prompt. Pair only devices you control or trust.** Encryption protects the traffic from observers on the network, not from the endpoint.

## Planned, with no date

Planned, with no date: running one model across several devices, an opt-in open network (UCompute Swarm), compute credits and an optional managed service (UCompute Cloud). None of these exists today. The engineering design that has been written for splitting one model between two devices keeps both ends of the RPC connection on loopback and carries the bytes only inside the same authenticated connection that pairing established, with policy checks on both devices. It is a design, not a feature, and this note will be updated only when evidence exists.

## If you want to use the RPC backend anyway

Read the README's warning again and take it literally: an isolated network segment that only your two machines can reach, no port forwarding, and an understanding that whoever can reach the port can run arbitrary compute on that machine. The llama.cpp project's own guidance is the right source for its own tool.

## Where this has run

Tested with development builds between one Apple M2 Mac and one Windows 11 laptop (Intel Arc 140V) on the same Wi-Fi network or phone hotspot, and between that Mac and one Linux desktop computer (Ubuntu, processor only, a development build of the background program compiled and started by hand; no app or installer) on a home Wi-Fi network. Linux is a planned platform, not a supported one. Pairing between two Macs is not yet shown to work. The check that captured traffic carries no readable prompt text ran on one computer.

UCompute's code is licensed under Apache-2.0. The source has not been published yet. llama.cpp is MIT-licensed; quotations above are from its repository and are attributed to its authors.
