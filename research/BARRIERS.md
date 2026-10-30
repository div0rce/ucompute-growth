# Adoption barriers across the funnel (synthesis)

Internal. Research date: **2026-10-30**. Raw lens: `research/raw/adoption-barriers.md` (every URL there was read in that session; items from search snippets are excluded or marked **unverified**). Supporting lenses: `research/raw/audience-multi-device-developers.md`, `research/raw/audience-local-ai-developers.md`, `research/COMPETITORS.md`.

## 0. How to read this file

- Funnel: **discovery → install → first workload → second device → repeat use → integration**. "Integration" (pointing an app, agent or editor at the local API and keeping it working) is added here because the audience lenses show it is where developers judge a runner after the first prompt works.
- The rank is this file's judgment of how much of the funnel each barrier blocks for a product shaped like UCompute (local engine plus own-device routing), weighted by share of users who hit it, whether it occurs before any value is delivered, and whether UCompute's current build changes it. Evidence under each barrier is what the judgment rests on.
- Incumbent mitigations are quoted or closely paraphrased from their own documentation, with the URL. This file does not say UCompute is stronger, safer or faster than any of them; it says what each documents, and what UCompute's registry lets Growth say.
- "What Growth can say" maps to claim ids in `claims/REGISTRY.md`; the qualifier travels with the claim. Phrases in `claims/PROHIBITED.md` do not appear in public copy.
- UCompute build facts that are **not** in the registry (signing status, download resume, sleep behaviour, update checks, mismatch messages) come from the project brief in the raw lens and are marked **unverified** here; Growth cannot publish them until a registry row exists.

## 1. Ranked barriers

| Rank | Barrier | Stage | Why here | What UCompute's evidence gives Growth |
|---|---|---|---|---|
| 1 | Unsigned or un-notarized installers (Gatekeeper, SmartScreen, Smart App Control) | install | Hits every install before any value; macOS removed the Control-click bypass; Smart App Control has no per-app bypass | Nothing public: `no-release`, `private-alpha` only; signing status has no registry row (**unverified**) |
| 2 | "Why not Ollama", now "why not Ollama plus NVIDIA PAIR" | discovery | PAIR documents the same whole-request design with signed installers and three-OS pairing | Documented differences, stated as facts: `local-only` default, `audit`, `transport`, `revocation`, `engine`, `catalog-fit` |
| 3 | Memory, quantization and model-selection confusion | first workload | Every user chooses a model; incumbents check fit after download or estimate wrongly on some hardware | Strongest position: `catalog-fit` with its calibration numbers and limits |
| 4 | First-run download size, time and reliability | first workload | Multi-GB pulls stall or reset; year-old open issues | `catalog-fit` (SHA-256), `engine` (archive verified); resume and stall handling **unverified** |
| 5 | Discovery and firewall failures on home and campus networks | second device | mDNS fails silently; client isolation blocks pairing; Windows firewall drops connections | `connect-by-address`, `windows-firewall`; client-isolated networks out of reach; two Macs not yet shown to pair |
| 6 | Trust in privacy and telemetry claims | discovery, install | The audience verifies by reading source or capturing traffic | `local-only`, `audit`, `audit-detail`, `device-sees-prompt`, `license` (source not published, so "check it yourself" is not available) |
| 7 | Mixed-OS pairing and version drift | second device, repeat use | Peers on different versions were silently invisible in exo until Oct 2026; PAIR requires same-version nodes | `mesh-pair-choose` (Mac to Windows, Mac to Linux dev daemon), `demo-2026-10-19`, `platforms`; no auto-update; mismatch message **unverified** |
| 8 | Strict OpenAI-API compatibility and the tool-call field | integration | Agents and SDKs break on one wrong field; the audience tests it first | `openai-clients` with its qualifier ("tool calling is not yet verified") |
| 9 | Linux packaging | install | Developer-dense segment; incumbents ship `.deb`, tarballs, scripts | Nothing: `platforms` (Linux planned); `mesh-pair-choose` qualifier describes the hand-started dev daemon |
| 10 | Laptop sleep breaking servers and peers | repeat use | Open since 2024 in Ollama; a mesh of laptops makes the second device a sleeping MacBook | Nothing; behaviour when a peer sleeps **unverified** |
| 11 | Unauthenticated LAN exposure | second device, repeat use | Auth-less local APIs found exposed at scale; fear transfers to any tool that opens a port | Documented properties: `local-only`, `transport`, `revocation`, `audit`, `windows-firewall` |

Discovery also carries a brand-findability barrier (no result for "UCompute" or "ucompute.org" surfaced from the domain; several name collisions). It is handled in `research/SEARCH.md` §5 and not ranked again here.

## 2. Barriers in detail

### B1. Unsigned or un-notarized installers (install)

**Evidence.**
- Apple developer notice (2024-08-06): in macOS Sequoia users "can no longer Control-click to override Gatekeeper" for software that is not signed correctly or notarized; the path is System Settings > Privacy & Security. https://developer.apple.com/news/?id=saqachfa
- flexkit PR #196 (merged 2026-10-20): an unsigned Electron app is reported as "damaged and can't be opened" with no way to allow it; ad-hoc signing changes that to the standard blocked-app dialog with "Open Anyway" in System Settings, and "only changes the message and the available workaround". https://github.com/flexkit-io/flexkit/pull/196
- LiteRT-LM issue #476 (opened 2025-08-22, open, stale 2026-10-25): SmartScreen "prevented an unrecognized app from starting", publisher "Unknown". https://github.com/google-ai-edge/LiteRT-LM/issues/476
- agent-orchestrator issue #4502 (2026-08-26, closed by a signing PR): unsigned binaries "build reputation slowly or never"; a 2026-10-20 follow-up reports Smart App Control blocking the installer outright. The "10k users" drop-off figure in that issue is one author's estimate, **unverified**. https://github.com/OrchestratorInc/agent-orchestrator/issues/4502
- Microsoft, Smart App Control: an unsigned app it cannot judge is considered "untrusted" and blocked; "There is currently no way to bypass Smart App Control protection for individual apps". https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003
- Jan issue #224 (2023): "Apple cannot check it for malicious software"; closed after "Our app is notarized" (2023-10-06). https://github.com/janhq/jan/issues/224
- Community norm: the `xattr` bypass is accepted only with a published checksum; installers that ask for admin rights or set launch-at-login are called out (HN 36802582, https://news.ycombinator.com/item?id=36802582).

**How incumbents mitigate (their words).**
- NVIDIA PAIR: "Released installers are signed. Self-built versions are unsigned and don't check the update feed." Windows .exe, Linux .deb, macOS .dmg. https://github.com/NVIDIA/Personal-AI-Router
- Mesh LLM: "mesh-llm.exe is not code-signed yet, so SmartScreen may warn." https://github.com/Mesh-LLM/mesh-llm
- Ollama, LM Studio, Jan current signing status: **unverified** (no page read states it; Jan notarized in 2023 per issue #224).

**What Growth can say.** Only `no-release` ("UCompute is in development. There is no public release or download yet.") and `private-alpha` (a macOS build exists for an owner-managed cohort; never name testers, number, file or describe it as open). Growth cannot describe the alpha's signing status, the dialog a tester sees or the workaround: no registry row covers it, and `signed (installer|app|build)`, `notarized`, `verified installer` are prohibited until a release record exists.

**Who owns it.** Engineering and the owner (Developer ID plus notarization on macOS; Authenticode on Windows; a published SHA-256 for the app alongside the models' hashes). Growth's only move is the handoff.

### B2. "Why not Ollama", now "why not Ollama plus PAIR" (discovery)

**Evidence.**
- HN, "The local LLM ecosystem doesn't need Ollama" (approx. Apr 2026): "ollama solved the UX problem"; "It's not the GUI, it's the curated model hosting platform"; critics cite blob storage ("I just want control over the damn files"), llama.cpp attribution and cloud monetization. https://news.ycombinator.com/item?id=47788385
- HN 47789569: rebuttals point to llama-server's GUI and API; counter-rebuttals report "unknown model architecture" errors from stale llama.cpp builds. https://news.ycombinator.com/item?id=47789569
- HN 47624999: "Ollama's API is easy to plug into other tools"; conflicting informal speed anecdotes. https://news.ycombinator.com/item?id=47624999
- exo users (secondary, 2026-04-02): "if a model fits on one machine, Exo adds complexity without any benefit"; "None of these clustering solutions are fully baked". https://www.lobsterpack.com/blog/exo-distributed-ai-cluster-macs/
- PAIR, the direct comparable: "Each request runs on a single node from start to finish"; "does not merge GPUs or pool VRAM"; mDNS plus add-by-IP; mTLS with generated certificates; engines Ollama and LM Studio (README adds llama.cpp); Apache-2.0; signed releases; the PIN "is a temporary bootstrap code rather than a strong credential. Pair systems only on trusted devices and networks"; endpoints accept requests only from the local machine; "Updates are manual and per machine". https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/, https://github.com/NVIDIA/Personal-AI-Router, https://docs.nvidia.com/local-ai/nvpair/getting-started/. First release v0.1.0 on 26 Aug 2026, v1.0.0 on 13 Oct 2026 (`research/COMPETITORS.md`).

**How incumbents mitigate (their words).** Ollama: curated library, one-command pull and run, de-facto API (HN threads). LM Studio: GUI, curated models, credits llama.cpp (HN 47789569). PAIR: rides on Ollama and LM Studio rather than replacing them. Mesh LLM: positions on pooled capacity and states "Pooled capacity does not guarantee pooled speed" with its own example figures. https://wavect.io/blog/mesh-llm-distributed-inference-multiple-computers/

**What Growth can say.** What UCompute is not: each request runs whole on one device; no model is split (`mesh-pair-choose`), stated as a limitation, not a headline (`research/COMPETITORS.md` §Implications). Documented differences as facts, side by side with PAIR's quoted docs and without a verdict: device keys pinned at pairing (`transport`); revoke with the measured close times (`revocation`; parity with PAIR's documented UI removal, so present it as part of the lifecycle pair → allow → audit → revoke); audit lines for off-device requests without prompt or response (`audit`; whether PAIR keeps one is **unverified**); local-only as the default policy (`local-only`); UCompute runs a pinned llama.cpp release itself rather than requiring another runner (`engine`); size, license and fit before download (`catalog-fit`). Growth cannot say easier, faster or more compatible: there is no public build to compare, and the hardware floors differ (PAIR's documented floor is RTX 20-series or Apple M4 and later; UCompute's demonstrated hardware is one M2 Mac and one Arc 140V laptop, `platforms`).

**Expect this question.** "How fast does the llama.cpp pin move?" The HN complaint about stale builds applies to any pinned engine; the registry says nothing about the update cadence (**unverified**).

### B3. Memory, quantization and model-selection confusion (first workload)

**Evidence.**
- Ollama #10920 (2025-05-30): a 16 GB device downloaded about 132 GB over about four hours before "model requires more system memory (164.8 GiB) than is available (13.4 GiB)"; the maintainer declined a pre-download check ("other clients may offer more safeguards"); closed 2025-07-03. https://github.com/ollama/ollama/issues/10920
- lms #499 (2026-03-10, open): LM Studio's guardrail estimated about 22.92 GB where llama.cpp used about 11.5 GB; the CLI and REST paths have no "Load anyway". https://github.com/lmstudio-ai/lms/issues/499
- lmstudio-bug-tracker #1471 (2026-02-03, open): on a UMA system with 96 GiB assigned to the GPU, the guardrail read system MemAvailable (about 22 GiB) and blocked a 15.89 GB model. https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/1471
- lmstudio-bug-tracker #651 (2025-05-10, open): on a 128 GB Mac, models over about 70 GB marked "Likely too large". https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/651
- HN, "Why your local LLM feels dumber than it is" (approx. Aug 2026): small default context "made a lot of people think local LLMs are dumb as rocks". https://news.ycombinator.com/item?id=49402232
- Ollama FAQ: "By default, Ollama uses a context window size of 4096 tokens." https://docs.ollama.com/faq.md. Ollama #14073: VRAM-tiered defaults in 0.15.5 caused spills and failures; a contributor: "no default fits all hardware". https://github.com/ollama/ollama/issues/14073

**How incumbents mitigate (their words).** LM Studio: compatibility indicator and loading guardrails (Relaxed / Balanced / Custom / Off) with a GUI "Load anyway" (per the issues). Ollama: size on the model page; fit checked at load time. PAIR: "Each engine and model must fit the machine's hardware". https://github.com/NVIDIA/Personal-AI-Router

**What Growth can say.** `catalog-fit`: "Before you download a model, UCompute shows its size, its license and whether it fits in your computer's memory. Every download is checked against a pinned SHA-256 hash." with its qualifier (Apple M2, macOS 26.2, experimental; estimates calibrated for Apple Silicon Macs) and the registry number (estimate within -4.6 % to +8.9 % of measured over 14 combinations, stories260K to qwen2.5-1.5b, calibrated for llama.cpp b11609 on Apple Silicon). The ready piece `2026-11-01-memory-fit-explainer` already states the limits (pre-download verdict is a lower bound; nothing above 1.5 B measured). Growth must present the verdict as an estimate with stated assumptions, so UCompute does not inherit the LM Studio false-positive complaints. Whether the user can override a "does not fit" verdict, and how the estimate behaves on Windows or UMA hardware: **unverified**.

### B4. First-run download size, time and reliability (first workload)

**Evidence.**
- Ollama #8484 (opened 2025-01-19; comments through Sep 2026): pulls stall and reset after 60 to 95 %; traced by a user to a hard-coded 5-second stall timeout; "This issue has been open for over a year without a mitigation". https://github.com/ollama/ollama/issues/8484
- Ollama #12507 (2025-10-05): completed chunks kept "until the server is restarted"; `OLLAMA_NOPRUNE=1` keeps them across restarts; later comments report downloads that "start from scratch every time". https://github.com/ollama/ollama/issues/12507
- Ollama #12478 (2025-10-02, open): the Linux install script fails on slow connections. https://github.com/ollama/ollama/issues/12478

**How incumbents mitigate (their words).** Ollama: parallel chunked downloader, chunk retention, environment knobs (above). PAIR: "PAIR downloads models during setup". https://docs.nvidia.com/local-ai/nvpair/getting-started/. Mesh LLM: each peer downloads only its assigned layer fragments. https://github.com/Mesh-LLM/mesh-llm

**What Growth can say.** Downloads are checked against a pinned SHA-256 hash (`catalog-fit`); the engine is a pinned llama.cpp release downloaded on first use and verified against its published hash (`engine`); "Downloading a model or the engine uses the internet" (`run-local` qualifier). The scope statement "small open models" is honest and relevant (smaller first payloads), but it is a scope, not a downloader quality claim. Resume, stall handling, first-run payload size and what the user sees on a hash mismatch: **unverified**; Engineering ask.

### B5. Discovery and firewall failures on home and campus networks (second device)

**Evidence.**
- exo #950 (2025-12-21): two Mac Studios on one subnet never found each other; no manual peer flag; closed "Can't repro". https://github.com/exo-explore/exo/issues/950
- exo #2271 (2026-08-20, open): two Ubuntu nodes on one wired LAN each elect themselves master; "Bootstrap peers has been temporarily removed". https://github.com/exo-explore/exo/issues/2271
- exo #952 (open): macOS discovery lost after every reboot until Local Network permission is re-granted. https://github.com/exo-explore/exo/issues/952
- flux #127 (2026-10-08): on eduroam, university, guest and corporate Wi-Fi with client isolation, devices "can't see each other, so they can't pair"; proposes pairing by explicit address with the same verification key; where isolation also blocks unicast, "a VPN or relay is the only option". https://github.com/bjarneo/flux/issues/127
- Ollama #6571 (2024-08-30): other PCs time out after about 21 s; maintainer: "This looks like a firewall issue". https://github.com/ollama/ollama/issues/6571
- exo #606 (open): "Windows-to-Windows discovery was the most common failure"; WSL NAT keeps nodes off the LAN. https://github.com/exo-explore/exo/issues/606

**How incumbents mitigate (their words).** PAIR: mDNS plus "add it by IP address"; the Windows installer adds firewall rules; Linux users open UDP 5353 and TCP 14318 to 14323 by hand; "Confirm all systems are on the same local network". https://docs.nvidia.com/local-ai/nvpair/getting-started/. Mesh LLM: Nostr-based public discovery with relays, invite tokens for private meshes, a LAN-only mDNS mode; documented ports for WSL2. https://github.com/Mesh-LLM/mesh-llm. LM Studio: "Serve on Local Network" toggle with a warning and an authentication recommendation; no firewall guidance on that page. https://lmstudio.ai/docs/developer/core/server/serve-on-network. Ollama FAQ: loopback by default; LAN exposure via `OLLAMA_HOST`. https://docs.ollama.com/faq.md

**What Growth can say.** `connect-by-address`: "Where a network blocks automatic discovery, as some campus Wi-Fi does, paired devices can still connect by address. An address alone is never trusted: the device must present the key it was paired with." (shown between one Mac and one Windows laptop on one campus network, development builds). `windows-firewall`: UCompute asks before letting paired devices through the firewall, and the rule covers only its own program on private networks (one Windows 11 laptop, October 2026; later builds not re-checked; Windows asks for administrator approval). `mesh-pair-choose` qualifier, verbatim: same Wi-Fi network or phone hotspot; Linux was a hand-compiled development daemon; "Pairing between two Macs is not yet shown to work." Growth cannot say pairing works on client-isolated networks (no relay or NAT traversal; `connect from anywhere`, `remote access` and `works across the internet` are prohibited). Whether a reason is shown when a peer cannot be reached: **unverified**.

### B6. Trust in privacy and telemetry claims (discovery, install)

**Evidence.**
- Ollama #2567 (2024-02-17): user saw periodic outbound traffic; maintainer: only the update check, carrying OS and architecture; a later commenter: self-reports cannot be trusted, monitor outgoing connections yourself. https://github.com/ollama/ollama/issues/2567
- Ollama #14279 (2026-02-16, closed Jun 2026 without a direct answer): cloud model data-retention question; "If this wasn't an issue it would be clear in the docs." https://github.com/ollama/ollama/issues/14279
- local-llm.net audit (2026-04-08): LM Studio analytics "on by default" (version, OS, GPU, model names; no prompts), opt-out in settings, and "because the license is proprietary, the claims can't be verified from the full source"; Jan: none found; Ollama: update check only during local use. Method claimed, captures not published; per-tool claims **unverified**. https://www.local-llm.net/blog/local-ai-privacy-audit/
- Jan privacy page: "You'll choose tracking preferences at first launch"; "Zero data collection until you say so". https://docs.jan.ai/desktop/privacy
- HN 47788385: cloud features and a closed GUI read as "steps away from the local, open-source roots".

**How incumbents mitigate (their words).** Jan: opt-in at first launch, named provider, documented scope. Ollama FAQ: "We don't see your prompts or data when you run locally"; `OLLAMA_NO_CLOUD=1`. https://docs.ollama.com/faq.md. PAIR: "prompts and responses are intended to stay on the local network when all clients, model sources, engines, and nodes are local"; update checks contact a release feed; telemetry statement not found (**unverified**). https://github.com/NVIDIA/Personal-AI-Router. LM Studio: opt-out setting (audit above).

**What Growth can say.** `local-only`: prompts and responses stay on the device unless the user pairs another device and chooses to run a request there; local-only mode refuses every off-device request; downloads use the internet. `audit` and `audit-detail`: what is recorded and the refused field names. `device-sees-prompt`, required beside any of the above. `license`: Apache-2.0 and "The source has not been published yet", both sentences together. Growth must label these as documented behaviour of development builds, never as something the reader can verify today, and never use `never leaves your device`, `end-to-end private`, `works offline`, `air-gapped` or `zero-knowledge`. A full list of outbound connections and whether any update check runs: **unverified**; Engineering ask (also the blocker for the cluster-6 page in `research/SEARCH.md`).

### B7. Mixed-OS pairing and version drift (second device, repeat use)

**Evidence.**
- exo #455 (2024-11-13): adding a Windows laptop to a Mac cluster crashed; closed as duplicate of the Windows tracking issue. https://github.com/exo-explore/exo/issues/455
- exo #606 (open): "Windows support is a longshot". https://github.com/exo-explore/exo/issues/606
- exo PR #2419 (merged 2026-10-13): peers on different versions silently dropped each other's Hello "so users got no explanation"; the fix logs a notice that all devices need the same version. https://github.com/exo-explore/exo/pull/2419
- PAIR: "Updates are manual and per machine. PAIR doesn't update peers or engines. All cluster nodes should run the same version." https://docs.nvidia.com/local-ai/nvpair/getting-started/

**How incumbents mitigate (their words).** PAIR: Windows, Linux and macOS nodes "can be paired with each other"; signed releases notify of new versions and install only on approval. https://github.com/NVIDIA/Personal-AI-Router. Mesh LLM: macOS, Linux (x64 and ARM64) and Windows bundles, Windows flagged as blocked out of the box in one release, WSL2 offered. https://github.com/Mesh-LLM/mesh-llm. exo: Windows not supported.

**What Growth can say.** `mesh-pair-choose` with its full qualifier (Mac to Windows; Mac to a hand-started Linux daemon; two Macs not yet shown). `demo-2026-10-19`, exact text only. `platforms`: no platform is declared supported; macOS 26.2 on M2 and Windows 11 on the named laptop are experimental; Linux, other GPUs and phones planned. Growth cannot mention updates at all (`automatic updates` prohibited; not started). Whether a version mismatch between two UCompute devices is reported to the user: **unverified**; Engineering ask.

### B8. Strict OpenAI-API compatibility and the tool-call field (integration)

**Evidence.**
- llama.cpp #20198 (2026-03-07): `tool_calls` arguments returned as a JSON object instead of a string crashed the official `openai` Python SDK with a `TypeError` and broke several agent frameworks; reverted the next day. https://github.com/ggml-org/llama.cpp/issues/20198
- Ollama, "OpenAI compatibility": `api_key` "required but ignored"; limitations listed (no `tool_choice`, no `n`, no logprobs; context size not settable through the OpenAI API). https://docs.ollama.com/openai
- HN 47788385: an OpenAI-compatible API is "needed for tools and agents". Audience lens: "Strictness matters more than breadth"; this audience "has been burned by that exact field and will test it first" (`research/raw/audience-local-ai-developers.md` §3.4).
- Long-running compatibility threads seen only as titles (`/v1/responses` support; KV cache truncation on `/v1/chat/completions`): **unverified**.

**How incumbents mitigate (their words).** Ollama: a documented list of supported endpoints and limitations (above). llama.cpp server: "OpenAI API compatible chat completions, responses, and embeddings routes" (README). LM Studio: "Use chat, responses, embeddings, and other familiar OpenAI-style endpoints." https://lmstudio.ai/docs/app/api

**What Growth can say.** `openai-clients`, verbatim with qualifier: "UCompute's local API works with the official OpenAI Python and JavaScript client libraries; only the base URL changes. Demonstrated on an Apple M2 Mac (macOS 26.2); the platform is experimental. Chat and completions with streaming; tool calling is not yet verified." The ready piece `2026-11-02-openai-client-base-url` already does this. Growth cannot write `full openai api compatibility`, `python and typescript sdks` (SDKs are planned) or describe tool or function calling as working. Which other request fields are accepted or ignored: **unverified**; Engineering ask (a documented limitations list like Ollama's would let Growth write a docs page).

### B9. Linux packaging (install)

**Evidence.**
- Ollama Linux docs: `curl … | sh`, manual `.tar.zst`, hand-written systemd unit; CUDA or ROCm installed separately. https://docs.ollama.com/linux
- Ollama #12478 (open): the install script fails on unreliable connections. https://github.com/ollama/ollama/issues/12478
- lmstudio-bug-tracker #991 (open since 2025-09-09): AppImage crashes on launch on Xubuntu 24.04; the `--no-sandbox` workaround "is not ideal for security reasons". https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/991
- HN 36802582 (2023): "Surprised to see no Linux support" as an immediate reaction to a new local-AI tool.

**How incumbents mitigate (their words).** PAIR: `.deb` for Debian and Ubuntu; "Other Linux distributions require building from source"; a headless archive with a terminal UI. https://docs.nvidia.com/local-ai/nvpair/getting-started/. Mesh LLM: `curl | bash`, Homebrew, Ubuntu and Arch packages, OCI images, checksums and SBOMs. https://github.com/Mesh-LLM/mesh-llm. Jan: `.deb` and AppImage (**unverified**, seen in search only).

**What Growth can say.** `platforms`: Linux is planned. `mesh-pair-choose` qualifier: one Linux desktop computer ran a development build of the background program compiled and started by hand, processor only; "Linux is a planned platform, not a supported one." Nothing else; `runs on linux`, `linux (version|app)`, `works on ubuntu` are prohibited. Engineering and owner decision.

### B10. Laptop sleep breaking servers and peers (repeat use)

**Evidence.**
- Ollama #5464 (2024-07-03, open): after Linux suspend and resume, CUDA init fails and inference falls back to CPU; only a service restart restores GPU mode. https://github.com/ollama/ollama/issues/5464
- Ollama #10053 (2025-03-30, duplicate): same on Debian 12; only a full reboot helps. https://github.com/ollama/ollama/issues/10053
- lidrun.com (vendor blog, Jun 2026; promotional): on macOS, lid-close sleep stops a background server unless `pmset -a disablesleep 1` or clamshell mode is used. https://lidrun.com/blog/keep-ollama-running-on-macbook
- Multi-device lens §4.3: "the strong machine sleeps (and the VPN doesn't come back)"; Windows GPU PCs that sleep when idle (open-webui discussion #28601).

**How incumbents mitigate (their words).** Ollama: documented workarounds, no shipped fix (#5464). PAIR: node eligibility requires the node to be "online and ready"; routes around unavailable nodes; adapts "as devices join or leave the network". https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/. LM Studio: a headless daemon (`llmster`) (**unverified**, seen in search only).

**What Growth can say.** Nothing. No registry row touches sleep, wake, reconnection or what happens to an in-flight request when the chosen device goes away. Engineering ask: what the requesting device shows when the paired device stops answering.

### B11. Unauthenticated LAN exposure (second device, repeat use)

**Evidence.**
- Cisco Talos (2025-09-01): 1,139 exposed Ollama endpoints, 214 serving live models; causes named: misconfiguration, default settings, weak or absent authentication, insufficient isolation. https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
- Ollama docs: "The local API at `http://localhost:11434` does not require authentication." https://docs.ollama.com/api/authentication
- local-llm.net audit: "Ollama needs authentication" (**unverified** methodology). https://www.local-llm.net/blog/local-ai-privacy-audit/
- Elastic prebuilt rule "Ollama API Accessed from External Network", mitigation "setting OLLAMA_HOST=127.0.0.1:11434 or applying firewall rules". https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/cross-platform/initial_access_ollama_api_external_access

**How incumbents mitigate (their words).** LM Studio: "Any bind other than `127.0.0.1` exposes the server beyond `localhost`"; "we recommend enabling authentication". https://lmstudio.ai/docs/developer/core/server/serve-on-network. PAIR: mTLS between nodes with generated certificates; endpoints accept requests only from the local machine. https://docs.nvidia.com/local-ai/nvpair/getting-started/. Mesh LLM: "QUIC end-to-end encrypts traffic between Mesh nodes"; owner keys and allowlists; API bound to loopback by default. https://github.com/Mesh-LLM/mesh-llm. llama.cpp server: `--api-key` (default none); "set an API key, put the server behind a reverse proxy" for public deployments. https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md

**What Growth can say.** `local-only`; `transport` with both qualifiers (the no-readable-prompt capture ran on one computer; "A device you have not paired cannot send you work" tested with several instances on one computer); `revocation`; `audit`; `windows-firewall`; `device-sees-prompt` beside all of it. Growth must not say UCompute "cannot be exposed" or compare safety; it states the defaults UCompute documents next to the defaults the others document.

## 3. What Growth cannot address (leave to Engineering or the owner)

| Item | Why Growth cannot move it | Barriers |
|---|---|---|
| Unsigned builds (ad-hoc macOS, unsigned Windows per the brief; **unverified** against `evidence/upstream/`) | Signing is a release action; no registry row; prohibited vocabulary until a release record exists | B1 |
| No public release | `no-release`; release gates belong to the owner and website LAUNCH.md | B1, B2, B6 |
| No Linux package | `platforms`; a hand-started daemon is not a package | B9, B7 |
| No published source | `license` second sentence; publication is engineering B-007 and an owner decision | B2, B6 |
| No auto-update, no version-mismatch message (**unverified**) | Engineering scope | B7 |
| Download resume and stall handling (**unverified**) | Engineering scope | B4 |
| Peer-sleep behaviour (**unverified**) | Engineering scope | B10 |
| Relay or NAT traversal for client-isolated networks | Not built; `planned` does not list it | B5 |
| Tool-call verification and a documented limitations list | Engineering verification | B8 |

## 4. Proposals (one sentence each)

### 4.1 Content pieces (Growth writes; `content/drafts` → `ready`)
1. **What binding a local AI server to 0.0.0.0 exposes, and a 60-second self-check** (B11; `run-local`, `local-only`, `openai-clients`, `transport`, `mesh-pair-choose`, `device-sees-prompt`).
2. **Use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi** (B2, B5, B11; `mesh-pair-choose`, `transport`, `local-only`, `audit`, `revocation`, `connect-by-address`, `windows-firewall`, `catalog-fit`, `demo-2026-10-19`).
3. **Why a shared API key is not device trust**, a four-pattern table in each project's own words (B11; `transport`, `revocation`, `audit`, `audit-detail`, `local-only`).
4. **What "verified" means in UCompute: SHA-256 against a pinned hash** (B4; `catalog-fit`, `engine`), omitting re-hash-on-load and mismatch UX until Engineering answers.
5. **How UCompute compares with NVIDIA PAIR, fact by fact**, each row a quote with a link and a registry claim, no verdict column (B2; `mesh-pair-choose`, `transport`, `revocation`, `audit`, `local-only`, `engine`, `catalog-fit`, `platforms`).
6. **Windows firewall consent: what UCompute asks and what the rule covers** (B5; `windows-firewall`, `local-only`).
7. **Every network connection UCompute makes, and why**, drafted now and held until the Engineering confirmation in 4.3.2 (B6; `local-only`, `run-local`, `engine`, `catalog-fit`, `planned`).
8. **What the memory-fit verdict assumes and when it will be wrong**, an addendum to the memory-fit explainer covering UMA and non-Mac hardware once measured (B3; `catalog-fit`, `platforms`).

### 4.2 Docs proposals for the Website workstream (to be written as `handoffs/YYYY-MM-DD-website-*.md`)
1. **An "Install: what your OS will say" page**, blank until Engineering supplies a registry row for signing status, so that the first thing a tester reads is the exact Gatekeeper and SmartScreen text and the sanctioned steps (B1).
2. **A "Networks" docs page** stating in registry words where pairing has been shown to work, that an address alone is never trusted, and that client-isolated networks are out of reach today (B5; `mesh-pair-choose`, `connect-by-address`).
3. **An "API compatibility" docs page** with a supported-and-not-yet-verified table mirroring Ollama's limitations format, seeded with `openai-clients` and its qualifier (B8).
4. **A "Platforms" docs page** that renders `platforms` and the `mesh-pair-choose` qualifier verbatim, including "Linux is a planned platform, not a supported one" and "Pairing between two Macs is not yet shown to work" (B7, B9).
5. **A "Data and connections" docs page** that renders `local-only`, `audit`, `audit-detail` and `device-sees-prompt` and links the connections manifest once Engineering confirms it (B6).

### 4.3 Asks to Engineering (to be written as `handoffs/YYYY-MM-DD-engineering-*.md`)
1. **Sign and notarize the macOS build with a Developer ID and sign the Windows build with Authenticode, publish the app's SHA-256 beside the model hashes, and add a snapshot row stating the current signing status so Growth can describe it** (B1).
2. **Confirm the complete list of outbound connections a development build can make (engine archive host, model hosts, paired devices, anything else) and whether any update check runs, as a snapshot row** (B6, cluster 6 in `research/SEARCH.md`).
3. **State whether interrupted model or engine downloads resume, how stalls are handled, and what the user sees on a SHA-256 mismatch** (B4).
4. **State whether files already on disk are re-hashed before load** (B4, SEARCH cluster 7).
5. **State what the requesting device shows when the chosen device stops answering (sleep, lid close, network loss) and whether an in-flight request is reported as failed** (B10).
6. **State whether a version mismatch between two paired UCompute devices is detected and shown, given no auto-update** (B7).
7. **State whether a "does not fit" verdict can be overridden and how the estimate behaves on the Windows laptop and on unified-memory hardware** (B3).
8. **Verify tool calling against the official OpenAI clients or publish the list of request fields that are accepted, ignored or rejected** (B8).
9. **State whether a reason is surfaced when a paired device cannot be reached (discovery blocked, firewall, isolation)** (B5).
10. **Repeat the two-Mac pairing attempt and record the result in the snapshot, so the registry qualifier can change in either direction** (B5, B7).

## 5. Unverified items (do not publish)
Signing status of Ollama, LM Studio and Jan installers; whether PAIR collects telemetry or keeps an audit log; PAIR's hardware floor relative to UCompute's; the 175,000-host figure (primary report not read); the "10k users" drop-off estimate; local-llm.net's per-tool traffic findings; Jan's `.deb` and AppImage and LM Studio's `llmster` (search snippets only); every UCompute build fact listed in §3 that has no registry row.

## 6. Sources
Every URL cited above was read on 2026-10-30 in the raw lens unless marked **unverified**; the complete list, including pages that failed to fetch and titles surfaced only in search, is in `research/raw/adoption-barriers.md` §Sources.
