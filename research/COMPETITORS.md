# Competitors (consolidated fact sheet)

Internal. Full profiles, complaints and the 45-source list: `research/raw/competitors-positioning.md` (2026-10-30, founding session). This file holds the current, re-checked facts and the positioning implications. Every fact is from a primary page fetched on the date shown; **unverified** marks anything that could not be re-read. Star counts are what the page showed and drift.

## Current facts (re-checked 2026-10-30, cloud weekly)

| Project | License | Stars | Latest release (releases page) | Distributed mode | Device auth / encryption (their words) | Revocation / removal documented |
|---|---|---|---|---|---|---|
| NVIDIA PAIR | Apache-2.0 | 1.7k | v1.0.0, 13 Oct (assets 2026-10-09); first release v0.1.0 on 26 Aug (corrects the earlier unverified "2026-09-03") | Whole request to one node: "PAIR routes each independent request to one node"; "does not pool GPU memory" | Six-digit PIN, then certificates and mutual TLS; "Cluster mTLS protects participating cluster channels only when identity and certificate material are present" | **Yes, as a UI step:** README "Remove it from another node, which any member can do from Settings → Cluster by removing that node from the list." No certificate revocation or rotation described |
| Mesh LLM | Apache-2.0 | 3.7k | v0.78.1, 05 Oct; rolling preview 30 Oct (the README's Windows section still cites v0.75/v0.76) | Route by default ("If one node can host the full model, it serves the model locally without stage traffic"); split mode available | "QUIC end-to-end encrypts traffic between Mesh nodes"; private meshes invite-token based | Partial: `mesh/docs/MESHES.md` tokens "can expire"; rotating an invite token is "just replacing the file's contents"; CLI has `auth rotate-node` / `auth rotate-owner` (certificate rotation). No node-removal procedure found |
| LM Studio LM Link | Proprietary | n/a | **unverified this run** (lmstudio.ai and tailscale.com outside the routine's allowed network domains) | Whole request to a remote device (Preview, per 2026-10-30 founding read) | End-to-end encrypted via Tailscale (founding read) | Only "disable this device" seen in a snippet (**unverified**). No GA announcement found (search snippets still say Preview, **unverified**) |
| exo | Apache-2.0 | 48.1k | v1.0.71, 23 Apr (year not shown) | Genuine partitioning | README mentions no authentication; maintainer: "exo's api is unauthorized" (#1833, founding read) | n/a (no pairing) |
| Ollama | MIT | 185.3k | v0.40.13, 28 Oct | None (cloud models instead) | "The local API at `http://localhost:11434` does not require authentication." (docs source on GitHub; docs.ollama.com unreachable this run) | n/a |
| llama.cpp RPC | MIT | 132.8k | b12002, 30 Oct (pre-release builds) | Genuine partitioning | RPC README: "the functionality is fragile and insecure."; "Never run the RPC server on an open network or in a sensitive environment!" | n/a |
| LocalAI | MIT | 50.1k | v4.12.1, 23 Oct (security-only patch) | Worker shard and federated routing (experimental) | Shared token over libp2p/EdgeVPN (founding read) | not re-checked |
| Jan | Apache-2.0 | 45.2k | v0.8.8, 28 Oct 2026 | None | Optional API key, 127.0.0.1 default (founding read) | n/a. Repository now opens at `janhq/jan` (redirect from `menloresearch/jan`; redirect itself not confirmed) |
| Petals, prima.cpp, distributed-llama | MIT | 10.7k / 125 / 3.1k (founding read) | not re-checked | Genuine partitioning | None documented | n/a |

Sources re-read this run: github.com/NVIDIA/Personal-AI-Router (README, /releases, /releases/tag/v0.1.0, SECURITY.md); github.com/Mesh-LLM/mesh-llm (README, /releases, mesh/docs/MESHES.md, mesh/docs/CLI.md); github.com/exo-explore/exo (+/releases); github.com/ollama/ollama (+/releases, docs/api/authentication.mdx); github.com/ggml-org/llama.cpp (+ tools/rpc/README.md, /releases); github.com/mudler/LocalAI (+/releases); github.com/janhq/jan (+/releases). Unreachable (`getaddrinfo ENOTFOUND`, outside allowed domains): lmstudio.ai, tailscale.com, docs.ollama.com, nvidia.com.

## What changed since the founding read (same day, earlier)
1. **PAIR documents node removal** in its README (any member, Settings → Cluster). "One-step per-device revoke" is therefore **no longer differentiated vs. PAIR**; it is parity as a capability. What PAIR still does not describe is what removal does cryptographically (no certificate revocation or rotation in README or SECURITY.md).
2. **Mesh LLM documents certificate rotation and expiring invite tokens.** Still no node-removal procedure.
3. PAIR reached 1.0.0 (13 Oct); its first public release was 26 Aug, not 3 Sep.
4. Mesh LLM is at v0.78.1; Jan moved to `janhq/jan`.

## UCompute properties: verdict as of 2026-10-30
| Property | Verdict |
|---|---|
| OpenAI-client compatibility, streaming, loopback-only API | Table stakes |
| Memory-fit before load; hash-verified downloads | Table stakes technically; reliability is the only possible opening, and only with public evidence |
| Whole request on one device | Category (PAIR, LM Link, Mesh LLM default). Say it as a limitation, not a headline |
| Authenticated pairing with pinned keys, TLS 1.3 over QUIC | Differentiated vs. partitioners; parity vs. PAIR, LM Link, Mesh LLM |
| Per-device revoke | **Parity with PAIR** (UI removal). Possible nuance only if UCompute's evidence states what revoke does to the pinned key and that a revoked device is refused (check `claims/registry.json` before saying anything) |
| Default local-only policy (nothing leaves a device until opted in per device) | Differentiated as a default (no page read describes one) |
| Audit log of off-device requests without prompt text | Differentiated (no page read documents one) |

## Implications (supersedes §5 of the raw file where they differ)
1. Lead with **default-deny off-device policy** and the **prompt-free audit log**; mention revoke as part of a complete trust lifecycle (pair → allow → audit → revoke), not as a unique feature.
2. Compare honestly against PAIR; never call any project insecure. Quote others only in their own words with links.
3. Everything is gated on shipping: every project above has a downloadable artifact; UCompute's public repository holds a LICENSE.

## Change record
- 2026-10-30 (cloud weekly): file created from the founding raw lens plus a same-day primary-source re-check; revoke verdict downgraded to parity vs. PAIR; release and repository facts updated.
