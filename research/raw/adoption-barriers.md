# Adoption Barriers for Local-AI Developer Tools, 2025–2026

**Lens:** adoption barriers, from real user reports (GitHub issues, Hacker News threads, vendor docs, audits).
**Prepared for:** UCompute internal strategy repository.
**Research date:** 2026-10-30.
**Method:** WebSearch (extended mode for niche facts) to locate candidate pages, then WebFetch to read each primary page. Every factual claim below carries the URL that was actually read. Items that could not be confirmed from a page read in this session are marked **unverified**. Pages seen only as search-result snippets are listed separately at the end and are not used as evidence. No statistics were invented; where a source gives a number, the number is attributed to that source.

**UCompute baseline used for the "what UCompute can honestly say" sections** (from the project brief, not from any public page): Apache-2.0; source not yet published (public repo holds only a LICENSE); no public release or download; in development builds it runs small open GGUF models through a pinned llama.cpp engine behind a local OpenAI-compatible API; shows size, license and a memory-fit verdict before a download; verifies downloads by SHA-256; "UCompute Mesh" pairs the user's own devices on one local network with a short code and routes a WHOLE request to one chosen device over QUIC + TLS 1.3 with pinned device keys, one-step revocation, default local-only policy, an audit log without prompt text, connect-by-address where mDNS is blocked, and a Windows firewall consent step that adds a rule only for its own program on private networks. macOS builds are ad-hoc signed and not notarized; Windows builds are unsigned; no Linux package; no auto-update; no relay/NAT; no partitioning, scheduler, open network, cloud, credits, SDKs or mobile.

---

## 1. Funnel model and ranking

Funnel stages used throughout: **discovery → install → first workload → second device → repeat use**.

Ranking criterion: how much of the funnel a barrier blocks for a UCompute-shaped product (local engine + own-device routing), weighted by (a) the share of users who hit it, (b) whether it occurs before any value is delivered, and (c) whether UCompute's current build makes it worse or better than incumbents. The rank is this report's judgment; the evidence under each barrier is what it rests on.

| Rank | Barrier | Funnel stage hit | Why ranked here | UCompute today |
|---|---|---|---|---|
| 1 | Unsigned / un-notarized installers (macOS Gatekeeper, Windows SmartScreen and Smart App Control) | install | Hits 100% of installs, before any value; macOS has removed the Control-click bypass; Smart App Control offers no per-app bypass | Worse than every signed incumbent (ad-hoc macOS, unsigned Windows) |
| 2 | "Why not just Ollama" — now "why not Ollama + NVIDIA PAIR" | discovery | PAIR (Sept 2026) ships the same whole-request-routing design with signed installers and three-OS pairing; the objection now has a concrete, free, Apache-2.0 answer | Differentiators exist (pinned keys, revocation, audit log, pre-download fit verdict) but nothing is downloadable |
| 3 | Memory, quantization and model-selection confusion | first workload | Every user chooses a model; incumbents check fit after download or with wrong estimates; wrong defaults make models "feel dumb" | Strongest honest position: size + license + fit verdict before download |
| 4 | First-run download size, time and reliability | first workload | Multi-GB pulls stall, reset, or lack resume on common connections; year-old open issues | SHA-256 verification is real; resume behaviour is unverified |
| 5 | Discovery and firewall failures on home and campus networks | second device | mDNS silently fails on home LANs, is blocked by campus client isolation; Windows firewall drops SYNs | Connect-by-address and scoped firewall consent are real; client-isolated networks remain unsolvable without a relay |
| 6 | Trust in privacy / telemetry claims | discovery, install | The privacy-first audience verifies claims by reading source or sniffing traffic; LM Studio's default-on analytics is the cautionary case | Source unpublished, so "verify it yourself" is not yet possible |
| 7 | Mixed-OS pairing and version drift | second device, repeat use | exo has no native Windows; version mismatches made peers invisible with no message until Oct 2026 | macOS + Windows builds exist; no Linux; no auto-update means drift risk |
| 8 | Linux packaging | install | Smaller but developer-dense segment; curl-pipe-sh and AppImage both generate reliability issues | No Linux package at all: zero conversion for that segment |
| 9 | Laptop sleep breaking servers | repeat use | Suspend/resume breaks GPU inference on Linux (open since 2024) and stops servers on macOS | Nothing in current evidence addresses it |
| 10 | Unauthenticated LAN exposure | second device, repeat use | Ollama's auth-less API has been found exposed at scale; the fear transfers to any tool that opens a port | An advantage area: default local-only, pinned keys, TLS 1.3, revocation |

---

## 2. Barriers in detail

### Barrier 1 — Unsigned / un-notarized installers (install gate)

**What users report**

- Apple's developer notice (2024-08-06) states that in macOS Sequoia users "can no longer Control-click to override Gatekeeper" for software that is not signed correctly or notarized; they must go to System Settings > Privacy & Security and review the software before allowing it. Apple's recommendation is to submit Developer-ID-signed software for notarization. https://developer.apple.com/news/?id=saqachfa
- A desktop-app PR (flexkit, merged 2026-10-20) documents the practical consequence for unsigned Electron builds: without a Developer ID the app has no bundle signature, and Gatekeeper reports it as "damaged and can't be opened" with no way to allow it. Ad-hoc signing changes the result to the standard blocked-app dialog, which offers "Open Anyway" in System Settings — but the app is still not notarized and is still blocked on first launch; ad-hoc signing "only changes the message and the available workaround." https://github.com/flexkit-io/flexkit/pull/196
- On Windows, the LiteRT-LM issue (opened 2025-08-22, still open and marked stale on 2026-10-25) reports SmartScreen blocking the pre-built binary with "Microsoft Defender SmartScreen prevented an unrecognized app from starting," publisher "Unknown"; the user asked for a signed binary or safe bypass instructions "so new users can try LiteRT-LM without building from source." No signing response from maintainers appears in the thread. https://github.com/google-ai-edge/LiteRT-LM/issues/476
- The agent-orchestrator issue (2026-08-26, closed via a signing PR on 2026-08-30) argues unsigned binaries "build reputation slowly or never" so the SmartScreen warning persists; the author's own (unverified) estimate is a "large first-run drop-off at about 10k users." A follow-up on 2026-10-20 reports Windows **Smart App Control** blocking the official installer outright (Get-AuthenticodeSignature: NotSigned), i.e., a hard block rather than a prompt. https://github.com/OrchestratorInc/agent-orchestrator/issues/4502
- Microsoft's Smart App Control page: if the cloud service cannot confidently judge an app, SAC checks for a valid signature and, if the app is unsigned, will "consider it untrusted and block it." "There is currently no way to bypass Smart App Control protection for individual apps"; the only options are to turn SAC off or ask the developer to sign. https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003
- Even a funded, multi-OS competitor ships unsigned on Windows: the Mesh LLM README states "mesh-llm.exe is not code-signed yet, so SmartScreen may warn." https://github.com/Mesh-LLM/mesh-llm

**How incumbents mitigate**

- NVIDIA PAIR: "Released installers are signed. Self-built versions are unsigned and don't check the update feed." Installers: Windows .exe, Linux .deb, macOS .dmg. https://github.com/NVIDIA/Personal-AI-Router
- Mesh LLM: signed-release attestation for provenance, but the Windows binary is explicitly not code-signed; the third-party review calls Windows "pilot-grade" because the guide "still documents installer/runtime workarounds and unsigned executables." https://github.com/Mesh-LLM/mesh-llm , https://wavect.io/blog/mesh-llm-distributed-inference-multiple-computers/
- Ollama, LM Studio, Jan signing/notarization status: **unverified** in this research (no page read in this session states it).

**What UCompute can honestly say or do now**

- It can say its macOS build is ad-hoc signed, which per the flexkit PR means the user sees the "Open Anyway" path rather than the dead-end "damaged" dialog. It cannot say the app is trusted by Gatekeeper, and it must document the System Settings > Privacy & Security step (Apple's Sequoia change makes Control-click insufficient).
- It cannot honestly tell Windows users the install is frictionless: an unsigned .exe will trigger SmartScreen and is blocked outright on Smart App Control machines with no per-app bypass.
- Honest copy today: "development builds; expect an OS warning; here is exactly what it says and why." Anything more requires Developer ID + notarization on macOS and Authenticode (EV or Azure Trusted Signing, as the agent-orchestrator issue proposes) on Windows.

---

### Barrier 2 — "Why not just Ollama" (and now "why not Ollama + PAIR")

**What users report**

- HN thread on "The local LLM ecosystem doesn't need Ollama" (page shows only "6 months ago", so approx. April 2026): defenders say Ollama "just worked" with one command and a browsable, curated model list; "ollama solved the UX problem"; "It's not the GUI, it's the curated model hosting platform"; "Stop pretending like HF is in any way beginner friendly." Critics cite llama.cpp attribution, hashed-blob storage lock-in ("I just want control over the damn files"), the move toward cloud monetization, and casual users believing distilled models were "DeepSeek." https://news.ycombinator.com/item?id=47788385
- A second HN thread (approx. same period): "Ollama solved the UX problem for most people wanting local LLMs… One command runs a model, even on AMD ROCm." Rebuttals point to llama-server's GUI and OpenAI-compatible API, Hugging Face one-liners, LM Studio, KoboldCpp; counter-rebuttals report "unknown model architecture" errors from stale llama.cpp builds and say llama.cpp "moves fast" and is unsuitable for casual users. https://news.ycombinator.com/item?id=47789569
- A third HN thread (approx. March–April 2026): "There is virtually no reason to use Ollama over LM Studio or the myriad of other…" with conflicting informal speed numbers (one M4 Mac mini test found Ollama ~25% faster than LM Studio; another AMD/Vulkan test found the reverse) and a complaint that LM Studio "messes up tool calls." The thread treats Ollama's API as the integration standard: "Ollama's API is easy to plug into other tools." https://news.ycombinator.com/item?id=47624999
- The strongest version of the objection for a mesh product comes from exo's user base, summarized (secondary source, 2026-04-02): "if a model fits on one machine, Exo adds complexity without any benefit"; "None of these clustering solutions are fully baked"; "you'll get sick of it and quit using it in 10 minutes." https://www.lobsterpack.com/blog/exo-distributed-ai-cluster-macs/

**The new incumbent for UCompute's exact design: NVIDIA PAIR**

- Announced 2026-09-03 at IFA as a free, open-source beta for Windows, macOS and Linux. https://blogs.nvidia.com/blog/local-ai-ifa-next-gen-agents-nv-pair-rtx-spark/
- Design: "Each request runs on a single node from start to finish"; it "does not merge GPUs or pool VRAM," "does not shard a model or split one request across machines." Discovery by mDNS plus add-by-IP; pairing approved by the user; node-to-node traffic secured with mTLS using generated certificates; supported engines Ollama and LM Studio; supported devices RTX 20-series+, RTX PRO (Turing+), DGX Spark, Apple M4+. https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
- README: Apache-2.0; Windows/Linux/macOS nodes "can be paired with each other"; engines Ollama, LM Studio and llama.cpp; six-digit PIN pairing from Settings → Cluster; signed releases; the Windows installer adds the needed firewall rules. https://github.com/NVIDIA/Personal-AI-Router
- Getting-started docs: the PIN "is a temporary bootstrap code rather than a strong credential. Pair systems only on trusted devices and networks"; endpoints accept requests only from the local machine (others get 403, with no option to expose a network endpoint); "Updates are manual and per machine… All cluster nodes should run the same version"; requires UDP 5353 plus TCP 14318–14323 between nodes. https://docs.nvidia.com/local-ai/nvpair/getting-started/

**How incumbents mitigate the objection**

- Ollama: curated library, one-command pull/run, de-facto API standard (HN threads above).
- LM Studio: GUI, curated models, credits llama.cpp (HN 47789569).
- PAIR: rides on Ollama/LM Studio rather than replacing them, so the objection does not apply to it.
- Mesh LLM: positions on model splitting and pooled capacity, with an explicit admission that "Pooled capacity does not guarantee pooled speed" (68 tok/s solo → 21 tok/s on two nodes → 12–13 on three, in the project's own example). https://wavect.io/blog/mesh-llm-distributed-inference-multiple-computers/

**What UCompute can honestly say or do now**

- It can say what it is not: not pooling, not splitting — the same honest framing PAIR uses, and the one the exo-user complaints vindicate.
- It can name concrete differences from PAIR as stated facts, without claiming superiority: UCompute pairs with pinned device keys and one-step revocation (PAIR docs describe the PIN as a temporary bootstrap, not a strong credential); UCompute keeps an audit log without prompt text (PAIR docs read in this session do not mention an audit log — **unverified** whether PAIR has one); UCompute runs its own pinned llama.cpp engine rather than requiring Ollama/LM Studio.
- It cannot say it is easier than Ollama, faster, or more compatible: there is no public release to compare, and PAIR's hardware floor (RTX 20+/M4+) versus UCompute's is **unverified**.
- A caution from the HN threads: a *pinned* llama.cpp engine is exactly the configuration that produced "unknown model architecture" errors for users on stale builds (HN 47789569). UCompute should expect to be asked how fast the pin moves.

---

### Barrier 3 — Memory, quantization and model-selection confusion (first workload)

**What users report**

- Ollama issue #10920 (2025-05-30): a user on a 16 GB Arm board downloaded a ~132 GB model for about four hours, then `ollama run` failed with "model requires more system memory (164.8 GiB) than is available (13.4 GiB)." The user asked for the check to happen before download; the maintainer replied the size is on the model page and that Ollama "cannot know the model's intended use" (a download might be for an air-gapped server), and that "other clients may offer more safeguards." Closed as completed on 2025-07-03 with no pre-download check shown. https://github.com/ollama/ollama/issues/10920
- LM Studio's pre-load guardrail produces false positives: lms #499 (2026-03-10) — "Model loading was stopped due to insufficient system resources," estimate ~22.92 GB, while the same setup in llama.cpp used closer to 11.5 GB, and "Load anyway" in the GUI worked; the CLI/REST path has no "load anyway." Still open. https://github.com/lmstudio-ai/lms/issues/499
- lmstudio-bug-tracker #1471 (2026-02-03): on an AMD Ryzen AI Max+ 395 UMA system with 96 GiB allocated to the GPU, the guardrail reads system MemAvailable (~22 GiB) and blocks a 15.89 GB model while sysfs reports ~103 GB VRAM. Open, no maintainer response. https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/1471
- lmstudio-bug-tracker #651 (2025-05-10): on a 128 GB M3 MacBook, models over ~70 GB are marked "Likely too large" even after raising the GPU wired limit; the reporter believes the app caps near 64 GB. Open, no responses. https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/651
- Defaults make models "feel dumb": HN "Why your local LLM feels dumber than it is" (approx. late August 2026) — Ollama's small default context "made a lot of people think local LLMs are dumb as rocks"; "tons of people misunderstand what they're using" (which quant); KV-cache quantization and chat-template parsing bugs add to it; "I spent hours on it." https://news.ycombinator.com/item?id=49402232
- Ollama's FAQ confirms the default: "By default, Ollama uses a context window size of 4096 tokens." https://docs.ollama.com/faq.md
- Changing the default caused its own breakage: Ollama #14073 (2026-02-04, closed 2026-06-09) — 0.15.5 set defaults by VRAM tier (<24 GiB: 4,096; 24–48 GiB: 32,768; ≥48 GiB: 262,144); users with 52 GB VRAM saw models spill to CPU and Ollama become unresponsive, others saw "model requires more system memory" on 70B models and a 500 error loading a 1B model on a 96 GB GPU. A contributor's position: "no default fits all hardware." https://github.com/ollama/ollama/issues/14073

**How incumbents mitigate**

- LM Studio: compatibility indicator plus model-loading guardrails with Relaxed/Balanced/Custom/Off modes and a GUI "Load anyway" (per the issues above); estimates are often wrong on UMA and high-memory Apple hardware.
- Ollama: lists model size on the model page; checks fit only at load time, after download (maintainer position in #10920).
- PAIR: "Each engine and model must fit the machine's hardware"; routing eligibility requires "the exact model is present" on the node. https://github.com/NVIDIA/Personal-AI-Router , https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/

**What UCompute can honestly say or do now**

- This is UCompute's clearest honest claim: it shows size, license and a memory-fit verdict *before* the download — exactly the behaviour requested and declined in Ollama #10920.
- It must also be honest about the failure mode the LM Studio issues expose: a fit verdict is an estimate, and estimates are wrong on UMA systems, on high-memory Macs, and whenever context length is large. The verdict should state its assumptions (context length, KV cache) and allow an override; otherwise UCompute inherits LM Studio's false-positive complaints.
- It cannot yet claim the verdict is accurate: there is no public build and no third-party test.

---

### Barrier 4 — First-run download size, time and reliability (first workload)

**What users report**

- Ollama #8484 (opened 2025-01-19; ~30 thumbs-up; comments through September 2026): large-model pulls stall and progress resets even after 60–95%. A user traced it to a hard-coded 5-second no-data stall timeout in `server/download.go` ("stalled; retrying"). Quotes: "Can't believe this is still not fixed. It is not because a connection stalls for 5s that it is dead!" (Sep 2026); "This issue has been open for over a year without a mitigation" (Jan 2026); "Please re-open ticket." Workarounds include shell loops that kill and restart the pull, `OLLAMA_EXPERIMENT=client2`, and downloading the blob manually with a download manager. https://github.com/ollama/ollama/issues/8484
- Ollama #12507 (2025-10-05, closed as completed 2025-10-09): request to save download progress; maintainers say completed chunks are kept "until the server is restarted" and `OLLAMA_NOPRUNE=1` keeps them across restarts. Post-closure comments (Apr and Jul 2026) report downloads that "start from scratch every time." https://github.com/ollama/ollama/issues/12507
- Ollama #12478 (2025-10-02, open, no maintainer response): the Linux install script itself fails on slow or unstable connections ("max retries exceeded," TLS/curl errors); a contributor swapped in aria2c with resume to cope. https://github.com/ollama/ollama/issues/12478

**How incumbents mitigate**

- Ollama: parallel chunked downloader with chunk retention and env-var knobs (above); no official fix shown in #8484.
- PAIR: "PAIR downloads models during setup"; llama.cpp downloads require exact `owner/repository:quantization` IDs. https://docs.nvidia.com/local-ai/nvpair/getting-started/
- Mesh LLM: each peer downloads only its assigned layer fragments. https://github.com/Mesh-LLM/mesh-llm

**What UCompute can honestly say or do now**

- It can say downloads are verified by SHA-256 (a stated capability); this addresses corruption but not stalls or resume.
- Whether UCompute resumes interrupted downloads, how it handles stalls, or what its first-run download size is: **unverified** — not in the brief and not publicly testable.
- The "small open GGUF models" positioning is itself a mitigation: smaller first-run payloads shorten the time-to-first-token that #8484 users lose. The honest statement is about scope ("small models"), not about downloader quality.

---

### Barrier 5 — Discovery and firewall failures on home and campus networks (second device)

**What users report**

- exo #950 (2025-12-21): two Mac Studios on the same subnet, firewall disabled, Thunderbolt 5 link — libp2p mDNS advertised nothing, nodes never found each other; no manual peer flag was available. Maintainer: "Can't repro." Closed as not planned the same day. https://github.com/exo-explore/exo/issues/950
- exo #2271 (2026-08-20, open): two Ubuntu nodes on one wired /24 LAN, ping works, UFW opened, UDP test passes — each node elects itself master and never sees the other, with no error even at DEBUG. Manual peering is impossible: the code raises "Bootstrap peers has been temporarily removed." A community member suspects multicast/IGMP snooping. https://github.com/exo-explore/exo/issues/2271
- exo #952 (2025-12-21, open): the macOS app loses discovery after every reboot until Local Network permission is revoked and re-granted; one cluster dropped to one node after ~20 minutes. https://github.com/exo-explore/exo/issues/952
- exo PR #2419 (merged 2026-10-13): nodes on different exo versions silently dropped each other's Hello messages ("dropped: different namespace" at trace level) "so users got no explanation"; the fix logs a rate-limited notice that another exo "can't join the cluster" and all devices need the same version. https://github.com/exo-explore/exo/pull/2419
- Campus networks: flux #127 (2026-10-08) — on eduroam/university/guest/corporate Wi-Fi with client isolation, devices "can't see each other, so they can't pair"; proposes pairing by explicit IP/host with the same TLS link and verification key; notes the approach "won't help where client isolation also blocks unicast," in which case "a VPN or relay is the only option." https://github.com/bjarneo/flux/issues/127
- Windows firewall: Ollama #6571 (2024-08-30) — `OLLAMA_HOST=0.0.0.0` set, other PCs time out after ~21 s; maintainer: "This looks like a firewall issue" (SYN packets dropped); resolved by the user adjusting the firewall. https://github.com/ollama/ollama/issues/6571
- exo #606 (Windows tracking, open): "Windows-to-Windows discovery was the most common failure"; WSL's NAT keeps nodes off the LAN; opening UDP 49152–65535 and firewall rules gave mixed results. https://github.com/exo-explore/exo/issues/606

**How incumbents mitigate**

- PAIR: mDNS plus "add it by IP address" when discovery fails; the Windows installer adds firewall rules; Linux users with restrictive firewalls must open UDP 5353 and TCP 14318–14323 manually; docs tell users to "Confirm all systems are on the same local network." https://docs.nvidia.com/local-ai/nvpair/getting-started/
- Mesh LLM: Nostr-based public discovery with relays, invite tokens for private meshes, and a LAN-only mDNS mode that avoids relays; firewall ports 3131, 9337 and UDP 5353 documented for WSL2. https://github.com/Mesh-LLM/mesh-llm , https://wavect.io/blog/mesh-llm-distributed-inference-multiple-computers/
- LM Studio: "Serve on Local Network" toggle / `lms server start --bind 0.0.0.0` with a warning and an authentication recommendation; no firewall guidance on that page. https://lmstudio.ai/docs/developer/core/server/serve-on-network
- Ollama FAQ: binds 127.0.0.1:11434 by default; LAN exposure via `OLLAMA_HOST`; no authentication section. https://docs.ollama.com/faq.md
- exo: no manual peering at the time of #950/#2271; version-mismatch notice added only in Oct 2026.

**What UCompute can honestly say or do now**

- It can say it has connect-by-address for networks where mDNS is blocked, and that its Windows firewall step asks consent and adds a rule only for its own program on private-profile networks — the same two mitigations PAIR documents, with a narrower rule scope.
- It can say its pairing is a short code plus pinned device keys, so a device found by typed address is authenticated the same way as one found by mDNS (the trust argument made in flux #127).
- It cannot claim to work on client-isolated campus networks: without relay/NAT traversal (explicitly not built), unicast-blocked networks are out of reach, as flux #127 states. The honest line is "same local network, and if your network isolates clients, pairing will not work."
- It should expect the exo pattern: silent failures with "network confirmed working" and demand for diagnostics. Nothing in the brief says UCompute surfaces a reason when a peer cannot be reached; **unverified**.

---

### Barrier 6 — Trust in telemetry and privacy claims (discovery / install)

**What users report**

- Ollama #2567 (2024-02-17): user observed periodic outbound traffic and asked what telemetry exists; maintainer: the only outgoing call is the auto-update check carrying OS and architecture, and "Ollama does not track any of your data or input." A later commenter (Oct 2024) said self-reports cannot be trusted and users should monitor outgoing connections themselves. https://github.com/ollama/ollama/issues/2567
- Independent audit (local-llm.net, 2026-04-08, fresh installs on Ubuntu 24.04 with Wireshark/mitmproxy): Ollama — registry downloads expose IP, optional update check, no network requests during local inference, newer cloud features send prompts to ollama.com unless disabled; LM Studio — analytics "on by default" including app version, OS, GPU type and model names (no prompt content), opt-out in Settings > Privacy, and "because the license is proprietary, the claims can't be verified from the full source"; Jan — "no telemetry, analytics, or crash reporting in the source or traffic"; GPT4All — opt-in prompt at first launch. The author's thesis: "telemetry should always be opt-in." https://www.local-llm.net/blog/local-ai-privacy-audit/
- Jan's own privacy page: "You'll choose tracking preferences at first launch"; "Zero data collection until you say so"; analytics on PostHog EU limited to active users and retention under a random ID; changeable anytime in Settings; local models "keep everything at home." https://docs.jan.ai/desktop/privacy
- The HN "doesn't need Ollama" thread shows the trust slope: cloud features and a closed GUI are read as "steps away from the local, open-source roots." https://news.ycombinator.com/item?id=47788385

**How incumbents mitigate**

- Jan: opt-in at first launch, named provider, documented scope (above).
- Ollama: FAQ documents a local-only mode (`OLLAMA_NO_CLOUD=1` / `disable_ollama_cloud`) and states local use does not send prompts to ollama.com. https://docs.ollama.com/faq.md
- PAIR: "prompts and responses are intended to stay on the local network when all clients, model sources, engines, and nodes are local"; update checks contact a release feed; no telemetry statement found on the README (**unverified** whether PAIR collects any). https://github.com/NVIDIA/Personal-AI-Router
- LM Studio: opt-out setting, but default-on (audit above).

**What UCompute can honestly say or do now**

- It can state design intent: default local-only policy, audit log that excludes prompt text, Apache-2.0 license.
- It cannot yet say "verify it yourself": the source is unpublished and there is no build to sniff. In this audience, that is the whole test (Ollama #2567's "monitor outgoing connections"; the audit's "can't be verified from the full source" verdict on LM Studio). Until source and a build exist, privacy claims are assertions, and should be labelled as such.
- Whether UCompute performs any update check or outbound call at all: **unverified** (no auto-update is built, which removes one common outbound call, but model downloads necessarily contact a host).

---

### Barrier 7 — Mixed-OS pairing and version drift (second device / repeat use)

**What users report**

- exo #455 (2024-11-13): adding a Windows 11 laptop to a Mac cluster crashed on `add_signal_handler` (NotImplementedError); WSL2 attempts failed on networking and later on an ELF header error; closed as duplicate of the Windows tracking issue on 2025-12-18. https://github.com/exo-explore/exo/issues/455
- exo #606 (open): "Windows support is a longshot, but we are keeping an eye on it"; native Windows unsupported because tinygrad dropped Windows; a Mac and a WSL node discovered each other in one report; a community fork using llama-server runs across RTX 4090/5090 but "non-primary nodes run only the RPC server and must route prompts to the primary node." https://github.com/exo-explore/exo/issues/606
- Version drift as silent failure: exo PR #2419 (above). PAIR docs: "Updates are manual and per machine. PAIR doesn't update peers or engines. All cluster nodes should run the same version." https://docs.nvidia.com/local-ai/nvpair/getting-started/
- Secondary: exo "breaks between updates" (Lobster Pack summary of Reddit threads). https://www.lobsterpack.com/blog/exo-distributed-ai-cluster-macs/

**How incumbents mitigate**

- PAIR: Windows, Linux and macOS nodes can be paired with each other; signed releases notify of new versions and install only on approval. https://github.com/NVIDIA/Personal-AI-Router
- Mesh LLM: macOS, Linux (x64 and ARM64) and Windows bundles, with Windows flagged as blocked out-of-the-box as of v0.76.0-rc8 and WSL2 offered as an alternative. https://github.com/Mesh-LLM/mesh-llm
- exo: Windows not supported; Thunderbolt/RDMA Mac clusters are its focus (#606).

**What UCompute can honestly say or do now**

- It can say development builds exist for macOS and Windows and that Mesh is designed to pair them. Whether macOS↔Windows pairing has been exercised and works in the current build is **unverified** by anything public.
- It cannot offer Linux nodes (no package), and it has no auto-update, so the PAIR/exo version-mismatch failure mode applies in full. At minimum it should tell the user when a peer's version differs — the fix exo only shipped on 2026-10-13.

---

### Barrier 8 — Linux packaging (install)

**What users report**

- Ollama's official Linux path is `curl … | sh`, a manual `.tar.zst` extract, or a hand-written systemd unit; amd64 and ARM64; updates by re-running the script or re-extracting; no distro packages mentioned on the page. https://docs.ollama.com/linux
- The script fails on unreliable connections (Ollama #12478, open, no maintainer response). https://github.com/ollama/ollama/issues/12478
- LM Studio's AppImage crashes on launch on Xubuntu 24.04 with a Chromium SUID sandbox error; the workaround `--no-sandbox` "is not ideal for security reasons"; open since 2025-09-09, confirmed again Jan 2026, no maintainer response. https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/991
- Ollama on Linux also needs CUDA or ROCm v7 installed separately, and the docs advise AMD's latest `amdgpu` driver over the kernel-bundled one. https://docs.ollama.com/linux

**How incumbents mitigate**

- PAIR: `.deb` for Debian/Ubuntu via `sudo apt install ./NVPAIR-Setup-*.deb`; "Other Linux distributions require building from source"; headless archive with a terminal UI. https://docs.nvidia.com/local-ai/nvpair/getting-started/ , https://github.com/NVIDIA/Personal-AI-Router
- Mesh LLM: `curl | bash`, Homebrew formula (Apple Silicon), Ubuntu and Arch packages, OCI images, checksums and SBOMs from a packaging repo. https://github.com/Mesh-LLM/mesh-llm
- Jan: `.deb` and AppImage (seen in search results only; **unverified** by a page read).

**What UCompute can honestly say or do now**

- Nothing: there is no Linux package. The honest statement is "macOS and Windows development builds only." Given Linux is where Ollama's headless/server users live (the systemd path above), this excludes a developer-dense segment entirely until a `.deb`/tarball exists.

---

### Barrier 9 — Laptop sleep breaking servers (repeat use)

**What users report**

- Ollama #5464 (2024-07-03, **still open**, labels bug/nvidia): after Linux suspend/resume Ollama loses CUDA and falls back to CPU ("cuda driver library init failure: 999"); reloading `nvidia_uvm` fixes PyTorch but not Ollama; only an Ollama service restart restores GPU mode; `NVreg_PreserveVideoMemoryAllocations=1` helps some users; a systemd sleep-inhibitor approach was proposed but not implemented; the maintainer invited community contributions in Sept 2024. https://github.com/ollama/ollama/issues/5464
- Ollama #10053 (2025-03-30, closed as duplicate of #5464): same symptom on Debian 12; "Restarting the ollama server doesn't resolve this issue," only a full reboot, and it returns after the next sleep. https://github.com/ollama/ollama/issues/10053
- macOS (vendor blog, June 2026 — a keep-awake app seller, so product claims are promotional): Ollama is "an ordinary background process" with no sleep exemption; idle sleep is blocked by `caffeinate`, but lid-close sleep needs `pmset -a disablesleep 1` or clamshell mode with external display and power; menu-bar keep-awake apps share caffeinate's limit. https://lidrun.com/blog/keep-ollama-running-on-macbook

**How incumbents mitigate**

- Ollama: documented workarounds in the GPU docs, no shipped fix (#5464).
- PAIR: node eligibility requires the node be "online and ready" and routes around unavailable nodes; adapts "as devices join or leave the network." https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/ , https://blogs.nvidia.com/blog/local-ai-ifa-next-gen-agents-nv-pair-rtx-spark/
- LM Studio: `llmster` daemon for headless service operation (seen in search results only; **unverified** by a page read).

**What UCompute can honestly say or do now**

- Nothing in the brief addresses sleep. A mesh of laptops makes this worse: the "second device" is often a MacBook that will sleep mid-request. UCompute cannot honestly claim resilience here. The minimum honest behaviour is a clear error when a chosen device goes away, which is **unverified**.

---

### Barrier 10 — Unauthenticated LAN exposure (second device / repeat use)

**What users report**

- Cisco Talos (2025-09-01): a Shodan query found 1,139 publicly exposed Ollama endpoints; 214 (about 18.8%) were "actively hosting and responding with live models"; the rest were reachable through unauthenticated interfaces with no model loaded. Root causes named: misconfiguration, default settings, weak or absent authentication, insufficient network isolation; Ollama's "deployment defaults and documentation don't strongly emphasize security." https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
- Ollama's FAQ has no authentication section; exposure is via `OLLAMA_HOST`. https://docs.ollama.com/faq.md
- The privacy audit: Ollama's "API port has no built-in authentication, so anyone on the network can reach it"; "Ollama needs authentication." https://www.local-llm.net/blog/local-ai-privacy-audit/

**How incumbents mitigate**

- LM Studio: warns that any non-127.0.0.1 bind exposes the server and recommends enabling authentication. https://lmstudio.ai/docs/developer/core/server/serve-on-network
- PAIR: mTLS between nodes with generated certificates; endpoints accept requests only from the local machine (403 otherwise). https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/ , https://docs.nvidia.com/local-ai/nvpair/getting-started/
- Mesh LLM: QUIC end-to-end encryption, owner keys, allowlists, API bound to loopback by default. https://github.com/Mesh-LLM/mesh-llm

**What UCompute can honestly say or do now**

- This is an advantage area. It can state: default local-only policy; QUIC + TLS 1.3 with pinned device keys; one-step revocation; audit log without prompt text; Windows firewall rule scoped to its own program and private networks. These are the properties the Cisco report and the audit say Ollama lacks.
- It should not claim it "cannot be exposed": that is a property of the build and of user configuration, neither of which is public or audited.

---

## 3. Three barriers where UCompute's existing evidence gives it something honest to say

1. **Memory/quant/model confusion (Barrier 3).** Pre-download size + license + memory-fit verdict is precisely what Ollama #10920 asked for and the maintainer declined ("other clients may offer more safeguards"). Honest caveat: estimates fail on UMA and large-memory Macs (LM Studio #1471, #651, lms #499), so the verdict must show its assumptions and permit override.
2. **Discovery fallback and firewall consent (Barrier 5).** Connect-by-address where mDNS is blocked, and a Windows firewall rule added only for its own program on private networks, match PAIR's documented mitigations (add by IP; installer-added rules) and beat exo's state in #950/#2271 (no manual peering at all). Honest limit: client-isolated campus networks need a relay (flux #127), which UCompute does not have.
3. **LAN exposure safety (Barrier 10).** Default local-only, pinned device keys, TLS 1.3, one-step revocation and a prompt-free audit log address the exact gap documented by Cisco and the privacy audit for Ollama, and go beyond PAIR's "temporary bootstrap" PIN as described in NVIDIA's own docs. Honest limit: unaudited and unpublished.

(Also honest, smaller: SHA-256 verification of downloads, and GGUF-based models rather than a proprietary blob store — the latter a live complaint in the HN threads; UCompute's on-disk layout is **unverified**.)

## 4. Three barriers UCompute cannot address yet

1. **The install gate (Barrier 1).** Ad-hoc-signed macOS and unsigned Windows builds are blocked by Gatekeeper (Sequoia removed Control-click) and SmartScreen, and hard-blocked by Smart App Control with no per-app bypass. Every signed incumbent (PAIR confirmed) clears this; UCompute cannot until it has Developer ID + notarization and Authenticode signing. No Linux package compounds it.
2. **"Verify it yourself" trust (Barrier 6).** With no published source and no downloadable build, UCompute's privacy and audit-log properties cannot be checked by the audience that checks (Ollama #2567; the local-llm.net audit method). Claims must be labelled as design intent.
3. **Repeat-use resilience: sleep, version drift, no auto-update (Barriers 7 and 9).** Nothing addresses a peer laptop sleeping mid-request (Ollama #5464 open since 2024), and no auto-update means the exo version-mismatch failure (#2419) and PAIR's "all nodes should run the same version" burden apply in full.

## 5. Decision-relevant facts (with URLs read)

1. Apple (2024-08-06): macOS Sequoia users "can no longer Control-click to override Gatekeeper"; unnotarized software must be allowed via System Settings > Privacy & Security. https://developer.apple.com/news/?id=saqachfa
2. Microsoft: Smart App Control blocks unsigned apps and "there is currently no way to bypass Smart App Control protection for individual apps." https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003
3. NVIDIA PAIR (beta announced 2026-09-03): Apache-2.0, signed installers for Windows/.deb/macOS, three-OS pairing, six-digit PIN described as "a temporary bootstrap code rather than a strong credential," mDNS + add-by-IP, mTLS, whole-request routing with no pooling or splitting, endpoints local-only, manual per-machine updates, requires UDP 5353 + TCP 14318–14323. https://docs.nvidia.com/local-ai/nvpair/getting-started/ , https://github.com/NVIDIA/Personal-AI-Router , https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
4. Ollama #10920: a 16 GB device downloaded ~132 GB over ~4 hours before the memory check failed; maintainer declined a pre-download check. https://github.com/ollama/ollama/issues/10920 — and Ollama #8484: download stalls/resets tied to a hard-coded 5-second stall timeout, ~30 thumbs-up, complaints through Sept 2026. https://github.com/ollama/ollama/issues/8484
5. Cisco Talos (2025-09-01): 1,139 exposed Ollama endpoints, 214 responding with live models, attributed to absent authentication and defaults. https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
6. Privacy audit (2026-04-08): LM Studio analytics on by default (version, OS, GPU, model names; no prompts); Jan none found; Ollama update check only during local use. https://www.local-llm.net/blog/local-ai-privacy-audit/
7. exo PR #2419 (merged 2026-10-13): peers on different versions were silently invisible to each other until this fix. https://github.com/exo-explore/exo/pull/2419

## 6. Gaps and unverified items

- Signing/notarization status of Ollama, LM Studio and Jan installers: not read in this session.
- Whether PAIR collects telemetry or keeps an audit log: not stated on pages read.
- UCompute specifics not in the brief and not publicly testable: download resume/stall handling; first-run payload size; accuracy of the memory-fit verdict; whether macOS↔Windows pairing has been exercised; whether a peer-unreachable or version-mismatch reason is surfaced; behaviour when a peer sleeps; on-disk model layout; any outbound calls besides model downloads.
- No first-hand Reddit threads were read (search returned secondary summaries only); Reddit-sourced sentiment is cited only via the Lobster Pack summary and marked secondary.
- Quantified install drop-off from SmartScreen: only one user's own estimate exists (agent-orchestrator #4502), unverified.

---

## Sources (every URL read in this session)

Installers / OS gates
- https://developer.apple.com/news/?id=saqachfa
- https://github.com/flexkit-io/flexkit/pull/196
- https://github.com/google-ai-edge/LiteRT-LM/issues/476
- https://github.com/OrchestratorInc/agent-orchestrator/issues/4502
- https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003
- https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/991
- https://docs.ollama.com/linux
- https://github.com/ollama/ollama/issues/12478

Model selection / memory / quantization / defaults
- https://github.com/ollama/ollama/issues/10920
- https://github.com/lmstudio-ai/lms/issues/499
- https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/1471
- https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/651
- https://github.com/ollama/ollama/issues/14073
- https://news.ycombinator.com/item?id=49402232
- https://docs.ollama.com/faq.md

Downloads
- https://github.com/ollama/ollama/issues/8484
- https://github.com/ollama/ollama/issues/12507

Privacy / telemetry / exposure
- https://github.com/ollama/ollama/issues/2567
- https://www.local-llm.net/blog/local-ai-privacy-audit/
- https://docs.jan.ai/desktop/privacy
- https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
- https://lmstudio.ai/docs/developer/core/server/serve-on-network

Discovery / firewall / mixed-OS / version drift
- https://github.com/exo-explore/exo/issues/950
- https://github.com/exo-explore/exo/issues/2271
- https://github.com/exo-explore/exo/issues/952
- https://github.com/exo-explore/exo/pull/2419
- https://github.com/exo-explore/exo/issues/455
- https://github.com/exo-explore/exo/issues/606
- https://github.com/bjarneo/flux/issues/127
- https://github.com/ollama/ollama/issues/6571

Sleep
- https://github.com/ollama/ollama/issues/5464
- https://github.com/ollama/ollama/issues/10053
- https://lidrun.com/blog/keep-ollama-running-on-macbook (vendor blog)

"Why not Ollama" / incumbents
- https://news.ycombinator.com/item?id=47788385
- https://news.ycombinator.com/item?id=47789569
- https://news.ycombinator.com/item?id=47624999
- https://www.lobsterpack.com/blog/exo-distributed-ai-cluster-macs/ (secondary)
- https://blogs.nvidia.com/blog/local-ai-ifa-next-gen-agents-nv-pair-rtx-spark/
- https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
- https://github.com/NVIDIA/Personal-AI-Router
- https://docs.nvidia.com/local-ai/nvpair/getting-started/
- https://github.com/Mesh-LLM/mesh-llm
- https://wavect.io/blog/mesh-llm-distributed-inference-multiple-computers/

Attempted but not read (fetch failed; not used as evidence)
- https://www.nvidia.com/en-us/ai-on-rtx/personal-ai-router/ (HTTP 504)
- https://github.com/ollama/ollama/blob/main/docs/linux.md (HTTP 404; docs.ollama.com/linux used instead)

Surfaced in search results only — NOT read, NOT used as evidence (listed for follow-up)
- Ollama downloads: issues #8406, #9300, #8632, #14136, #14868; PR #8831
- Ollama install script: issues #12343, #11732, #10101, #12609
- Ollama LAN binding: issues #1431, #8304, #703, #3581, #5008
- Ollama memory errors: issues #7423, #8667, #10256, #7942, #15650
- Ollama sleep: issues #3489, #6647, #10204
- Ollama context truncation in agent tools: NousResearch/hermes-agent #43900, openclaw/openclaw #4028 and #24068
- exo discovery: issues #1788, #1682, #1305, #520
- LM Studio guardrails/AppImage: lmstudio-bug-tracker #2543, #2017, #1038, #120, #358, #624, #903; lms #217, #201
- HN: items 44805232, 39125838, 39309375
- Jan download/packaging pages; Petronella and vdf.ai Jan write-ups; Ollama exposure counts from Intruder/GreyNoise/cybernews (unverified figures)
