# Competitive positioning: local and multi-device LLM inference (as of 2026-10-30)

Lens: competitors-positioning. Internal strategy input for UCompute.

**Method.** 48 URLs were fetched and read directly (listed in §9). Every factual claim is cited inline to the page it came from. Anything marked **unverified** came only from a search-result snippet, a secondary write-up, or a page that could not be opened. Star counts, issue counts and version numbers are what each page showed on 2026-10-30 and will drift. Where a page gave no number, none is stated.

**Subject caveat.** UCompute is unreleased: the public repo holds only a LICENSE, the private alpha is behind access control, and the Mesh/Run behaviour described below was demonstrated on one Apple M2 Mac (macOS 26.2), one Windows 11 laptop (Intel Arc 140V) and a CPU-only Linux daemon. Every comparison here is "UCompute's development-build behaviour vs. a shipped product's public documentation". That asymmetry governs what can honestly be said in public.

---

## 1. Executive summary

1. **"Route the whole request to one of your own devices" is a crowded position in 2026, not an empty one.** Three shipped projects do what UCompute Mesh does and say so in nearly the same words. NVIDIA PAIR (Apache-2.0; Windows 11, Linux, macOS installers): "PAIR routes each independent request to one node" and "does not combine GPU memory, join GPUs into one larger GPU, or split a model or request across systems" ([PAIR README](https://github.com/NVIDIA/Personal-AI-Router), [NVIDIA build page](https://build.nvidia.com/rtx/pair.md)). LM Studio's LM Link (proprietary, Preview, built on Tailscale): "load remote models as if they were local" ([LM Link](https://lmstudio.ai/link)). Mesh LLM (Apache-2.0, 3.7k stars): "if one node can host the full model, it serves it locally without stage traffic", with partitioning available behind `--split` ([Mesh LLM README](https://github.com/Mesh-LLM/mesh-llm)).
2. **Against the partitioning projects, UCompute's trust model is genuinely differentiated.** exo, llama.cpp RPC, distributed-llama, prima.cpp and Petals document no authentication or encryption between devices, and two say so bluntly. An exo team member closed an unauthenticated-destructive-endpoint report as not planned with "this is intended behaviour, exo's api is unauthorized" ([exo #1833](https://github.com/exo-explore/exo/issues/1833)). llama.cpp's RPC README: "the functionality is fragile and insecure ... Never run the RPC server on an open network or in a sensitive environment!" ([RPC README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)).
3. **Against the 2026 routers, encrypted authenticated transport is table stakes; what remains differentiated is narrower.** PAIR: six-digit PIN, then traffic "designed to use certificates and mutual TLS after pairing" ([PAIR SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md)). LM Link: "always end-to-end encrypted, thanks to Tailscale" ([LM Link docs](https://lmstudio.ai/docs/lmlink)). Mesh LLM: QUIC "end-to-end encrypts traffic between Mesh nodes" ([Mesh LLM README](https://github.com/Mesh-LLM/mesh-llm)). None of the pages read documents (a) a one-step per-device revocation with a stated time bound, (b) an audit log of off-device requests that omits prompt text, or (c) a device that is paired yet refuses every off-device request until the owner opts in. Those three, plus "no account and no vendor backend in the pairing path", are UCompute's real differences in this tier.
4. **PAIR's own security policy is hedged in ways UCompute's claims are not.** PAIR's SECURITY.md says the PIN "is low entropy", "does not protect a node before pairing", that mTLS applies "only when identity and certificate material are present and the relevant workers use that transport", that "Discovery and node-information traffic can use plain HTTP", and it documents no removal or revocation procedure, listing "member removal" as an area "needing focused review and tests" ([PAIR SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md)). That is an honest document; it is also a concrete, citable gap.
5. **Two external facts give UCompute's least glamorous defaults real weight.** Censys found "10.6K high-confidence Ollama instances exposed to the Internet", 1.5K of which answered probe prompts ([Censys, 2025-09-24](https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys)); LeakIX counted 12,269 with "zero authentication" and noted the maintainers "have declined to add it, pointing users to reverse proxies instead" ([LeakIX, 2026-02-23](https://blog.leakix.net/2026/02/ollama-exposed/)); Ollama's own docs confirm "The local API at `http://localhost:11434` does not require authentication" ([Ollama auth](https://docs.ollama.com/api/authentication)) and the 2023 request for built-in auth was closed "not planned" ([Ollama #849](https://github.com/ollama/ollama/issues/849)). A May 2026 heap over-read in Ollama's GGUF loader (CVE-2026-7482, "Bleeding Llama", fixed in 0.17.1) was exploitable "without authentication" via "three unauthenticated API calls" and could expose prompts and environment variables ([SecurityWeek](https://www.securityweek.com/critical-bug-could-expose-300000-ollama-deployments-to-information-theft/)).
6. **Where competitors are clearly ahead:** pooling and partitioning (exo tensor-parallel with RDMA over Thunderbolt 5; Mesh LLM split mode; llama.cpp RPC; distributed-llama; prima.cpp; Petals), model range and modality (Ollama, LocalAI, LM Studio), platform coverage (Ollama, LM Studio, Jan, PAIR, Mesh LLM all ship Windows/macOS/Linux), mobile (LM Studio's Locally iPhone/iPad app; prima.cpp on Android/HarmonyOS), NAT traversal (LM Link via Tailscale; Mesh LLM via iroh relays; LocalAI via libp2p DHT), richer API surface (Anthropic Messages and OpenAI Responses endpoints on exo, LocalAI, PAIR, Ollama, LM Studio, llama-server), and maturity (Ollama 185.3k stars, llama.cpp 132.8k, LocalAI 50.1k, exo 48.1k, Jan 45.2k).
7. **Memory-fit before load and OpenAI-client compatibility are table stakes.** llama-server ships `--fit` "default: 'on'" to "adjust unset arguments to fit in device memory" ([server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)); Ollama queues requests "until the new model can be loaded" and unloads idle models ([Ollama FAQ](https://docs.ollama.com/faq)). Every competitor read exposes an OpenAI-compatible `/v1` endpoint.

---

## 2. Landscape map

| Project | One-line positioning (quoted) | License | Platforms | Distributed mode | Auth / encryption between devices | Discovery / pairing | Stars shown |
|---|---|---|---|---|---|---|---|
| exo | "Run frontier AI locally" | Apache-2.0 | macOS app (Apple Silicon, macOS 15.1+); Linux CPU-only from source; no Windows | Genuine partitioning (pipeline + tensor) | None documented; API "unauthorized" by design | Automatic, "no manual configuration"; no pairing step; version-namespaced | 48.1k |
| Ollama | "Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models" | MIT | macOS, Windows, Linux, Docker | None (cloud models are the remote story) | Local API "does not require authentication" | n/a | 185.3k |
| LM Studio + LM Link | "run Llama, DeepSeek, Qwen, Phi, and other LLMs locally"; LM Link: "load remote models as if they were local" | Proprietary | Apple Silicon Mac (macOS 14+), Windows x64/ARM, Linux x64/ARM64 AppImage; iPhone/iPad via Locally | Whole-request remote (LM Link, Preview) | End-to-end encrypted via Tailscale; account-based | Account sign-in; "Add a remote machine"; device list goes to LM Studio servers | n/a (closed source) |
| llama.cpp (llama-server, RPC) | "LLM inference in C/C++" | MIT | Everything (CPU, Metal, CUDA, HIP, Vulkan, SYCL, ...) | Genuine partitioning via RPC backend | None; "fragile and insecure"; "Never run ... on an open network" | Manual `--rpc host:port` list | 132.8k |
| Petals | "Run LLMs at home, BitTorrent-style" | MIT | Linux, WSL, Docker, macOS M1/M2 | Genuine partitioning across a public swarm | None documented; "Your data will be processed with the help of other people in the public swarm" | Public swarm / private swarm wiki | 10.7k; last commit Aug 2024 |
| prima.cpp | "Fast 30-70B LLM Inference on Heterogeneous and Low-Resource Home Clusters" | MIT | Linux, macOS, Android/HarmonyOS via Termux; no Windows | Genuine partitioning (piped-ring) | None documented; advises disabling firewall | Manual `--master`/`--next` IPs, ZeroMQ ports 9000/10000 | GitHub repo 404; Gitee mirror 23 |
| distributed-llama | "Connect home devices into a powerful cluster to accelerate LLM inference" | MIT | Linux, macOS, Windows; ARM and x86_64 AVX2; Raspberry Pi | Genuine partitioning (tensor parallel, 2^n nodes) | None documented | Manual `--workers ip:port` | 3.1k |
| LocalAI | "LocalAI is the open-source AI engine" | MIT | macOS DMG, Linux, Docker/podman; Windows not on README | Both: federated (whole request to one worker) and worker/sharded (llama.cpp RPC) | Shared token over libp2p/EdgeVPN; "secure and private"; protocol not documented | Auto via DHT (default) or mDNS; anyone with token joins | 50.1k |
| Jan | "an open source alternative to ChatGPT that runs 100% offline on your computer" | Apache-2.0 | Windows, macOS, Linux (.deb, AppImage, Flathub, MS Store) | None | Local API: optional bearer token, off by default | n/a | 45.2k |
| NVIDIA PAIR (2026) | "a local inference router for a group of compatible computers on the same network" | Apache-2.0 | Windows 11, Linux, macOS 13+ (x64, arm64); installers for all three | Whole-request remote only | Six-digit PIN, then "designed to use certificates and mutual TLS" | mDNS (UDP 5353) or add by IP; PIN + invitation modal | 1.7k |
| Mesh LLM (2026) | "Distributed AI/LLM for the people. Share compute privately or publicly" | Apache-2.0 | macOS, Linux, Windows (CPU, CUDA, ROCm, Vulkan, Metal) | Both: whole-model-on-one-node by default, `--split` for stages | QUIC end-to-end encryption; invite token for private meshes | Invite token `--join`; public meshes via Nostr; iroh relays | 3.7k |

Sources for each row are in the per-competitor profiles below.

---

## 3. Per-competitor profiles

Format: positioning / license / platforms / distributed mode / auth and encryption between devices / discovery and pairing UX / API / community signals / channels / recurring complaints.

### 3.1 exo (exo-explore/exo)

- **Positioning:** "Run frontier AI locally." "exo connects all your devices into an AI cluster." [README](https://github.com/exo-explore/exo)
- **License:** Apache-2.0, confirmed from the LICENSE file ("Apache License, Version 2.0, January 2004"; copyright Exo Technologies Ltd, 2025). [LICENSE](https://github.com/exo-explore/exo/blob/main/LICENSE). A vendor comparison table lists exo as GPL-3.0; that conflicts with the LICENSE file and is treated as wrong or stale. [SharedLLM blog](https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html)
- **Platforms:** macOS app requires "a Mac with Apple silicon and macOS Sequoia 15.1 or later"; RDMA over Thunderbolt requires macOS Tahoe 26.2+; source builds on macOS and Linux; "Currently, exo runs on CPU on Linux. GPU support for Linux platforms is under development." No Windows. [README](https://github.com/exo-explore/exo)
- **Distributed mode:** Genuine partitioning. "Topology-Aware Auto Parallel ... figures out the best way to split your model across all available devices"; tensor parallelism "up to 1.8x speedup on 2 devices and 3.2x speedup on 4 devices" (project's own numbers, measurement not described). [README](https://github.com/exo-explore/exo)
- **Auth / encryption between devices:** Not described in the README. The only security note is that `trust_remote_code` "must be explicitly enabled (default is false) for security". [README](https://github.com/exo-explore/exo). On the HTTP API the position is explicit: issue #1833 ("Unauthenticated Remote Instance Termination", opened 2026-04-02, reporting that `GET /state` and `DELETE /instance/{id}` have "no authentication middleware, no API key, no bearer token, no session cookie") was closed the same day as not planned by a "Member" with: "this is intended behaviour, exo's api is unauthorized" and "run exo behind a reverse proxy and provide your own authentication if you wish to expose it downstream." [exo #1833](https://github.com/exo-explore/exo/issues/1833)
- **Discovery / pairing UX:** "Devices running exo automatically discover each other - no manual configuration." No pairing step; cluster names isolate groups. Discovery is namespaced by version: "Nodes connect only when they share a discovery namespace. The namespace defaults to the exo version, so devices running different versions of exo never connect." Until PR #2419 (merged 2026-10-13) users got no explanation because the other node's Hellos were dropped at trace level. [README](https://github.com/exo-explore/exo), [PR #2419](https://github.com/exo-explore/exo/pull/2419)
- **API:** OpenAI Chat Completions, Claude Messages, OpenAI Responses and Ollama APIs (`/v1/chat/completions`, `/v1/messages`, `/v1/responses`, `/ollama/api/*`). [README](https://github.com/exo-explore/exo)
- **Community signals:** 48.1k stars, 3.6k forks, 208 open issues, 225 open PRs, 2,462 commits. Discord and X linked; Discord member count not readable on the page (**unverified**). [README](https://github.com/exo-explore/exo)
- **Recurring complaints:** Discovery is the dominant theme. The README itself lists: devices on different exo versions won't join; "Guest Wi-Fi and some office networks may block device discovery"; RDMA ports may fail to discover if macOS build numbers differ; on Mac Studio one TB5 port can't be used. [README](https://github.com/exo-explore/exo). Issue titles from search (**not opened; unverified**): "[BUG] not seeing the MAC minis and MAC Studios - NO FIREWALL" (#1534), "Two Ubuntu nodes on same LAN fail to discover each other" (#2271), "[BUG] DGX Spark does not find other nodes" (#1682), "Fix Local Network permissions in MacOS App" (#952), "VLAN discovery" (#711), "manual discovery" (#724), Tailscale/ZeroTier conflicts (#879).

### 3.2 Ollama

- **Positioning:** "Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models." "Start building with open models." [README](https://github.com/ollama/ollama)
- **License:** MIT. [README](https://github.com/ollama/ollama)
- **Platforms:** macOS, Windows, Linux (install scripts and manual installers), Docker image. [README](https://github.com/ollama/ollama)
- **Distributed mode:** None on the pages read. The remote story is cloud models: `ollama signin`, `OLLAMA_API_KEY`; disable with `disable_ollama_cloud` in `~/.ollama/server.json` or `OLLAMA_NO_CLOUD=1`, which "removes access to cloud models and web search". Cloud use requires an "Ollama Public Key". [FAQ](https://docs.ollama.com/faq), [auth](https://docs.ollama.com/api/authentication)
- **Auth / encryption:** "The local API at `http://localhost:11434` does not require authentication." [auth](https://docs.ollama.com/api/authentication). Binds "127.0.0.1 port 11434 by default"; exposing is `OLLAMA_HOST="0.0.0.0:11434"`. The FAQ's only exposure guidance is an Nginx proxy example that forwards requests and sets the Host header; it configures no authentication. Model pulls are HTTPS-only: "Ollama does not use HTTP for model pulls, only HTTPS." [FAQ](https://docs.ollama.com/faq). The 2023 request "How to secure the API with api key" (#849) drew the maintainer answer "The solution to this for the time being would be to add an authenticating proxy in front of Ollama" and was closed as not planned on 2023-10-25; follow-up comments asking why auth can't be built in carry 97 and 47 thumbs-up. [Ollama #849](https://github.com/ollama/ollama/issues/849)
- **Consequences in the wild:** Censys (2025-09-24): "We find 10.6K high-confidence Ollama instances exposed to the Internet"; "Of these 10.6K public hosts, 1.5K respond to at least one of these prompts"; "approximately 10,600 services ... across 1,229 autonomous systems"; more than a quarter on non-default ports. [Censys](https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys). LeakIX (2026-02-23): 12,269 instances "with zero authentication"; `/api/tags`, `/api/generate`, `/api/chat`, `/api/pull`, `/api/push` all open; ~1,000 estimated still vulnerable to CVE-2024-37032; "Ollama 'ships with no authentication,' and ... the maintainers have declined to add it, pointing users to reverse proxies instead"; "no warning when binding to 0.0.0.0"; "Ollama doesn't log requests by default". [LeakIX](https://blog.leakix.net/2026/02/ollama-exposed/). SecurityWeek (2026-05-05): CVE-2026-7482 "Bleeding Llama", heap out-of-bounds read in the GGUF loader, CVSS 9.3, exploitable "remotely without authentication" with "only three unauthenticated API calls", can expose prompts, messages and environment variables; fixed in 0.17.1; Cyera's figure of "approximately 300,000 Ollama servers currently exposed" is quoted. [SecurityWeek](https://www.securityweek.com/critical-bug-could-expose-300000-ollama-deployments-to-information-theft/). Note the counts (10.6K, 12.3K, 300K) come from different scanners and filters and are not comparable.
- **Discovery / pairing:** n/a.
- **API:** "Ollama supports a subset of the OpenAI API": `/v1/chat/completions`, `/v1/completions`, `/v1/models`, `/v1/embeddings`, `/v1/responses` (non-stateful only), `/v1/audio/*`. Local base URL `http://localhost:11434/v1/`, api_key "required but ignored". Unsupported: logprobs, image URLs, `tool_choice`, `logit_bias`, `n`; context size needs a Modelfile `num_ctx`. [OpenAI compat](https://docs.ollama.com/api/openai-compatibility)
- **Download verification:** The pull API streams `StatusEvent`s with a `digest` field, "Content digest associated with the status, if applicable"; the page gives no example digest and makes no verification statement; `insecure: true` allows "downloading over insecure connections". [pull API](https://docs.ollama.com/api/pull). That Ollama blobs are SHA-256 content-addressed is **unverified** from the pages read.
- **Memory behaviour:** `OLLAMA_MAX_LOADED_MODELS` loads models "provided they fit in available memory" (default 3 × GPUs); when memory is insufficient "all new requests will be queued until the new model can be loaded"; idle models are unloaded to make room; default keep-alive 5 minutes. [FAQ](https://docs.ollama.com/faq)
- **Community signals:** 185.3k stars. Discord, X, Reddit linked; member counts not readable (**unverified**). [README](https://github.com/ollama/ollama)
- **Recurring complaints:** (a) no built-in auth (above, primary). (b) Cloud blurring local: FAQ states cloud prompts are processed by Ollama but "not stored or logged" and "never used for training" ([FAQ](https://docs.ollama.com/faq)); third-party commentary that cloud models share the same localhost port and CLI so users may not notice data leaving the machine, and an April 2026 issue (#15453) alleging a high cloud failure rate, are **unverified** (search snippets only).

### 3.3 LM Studio (including LM Link, llmster and Locally)

- **Positioning:** "run Llama, DeepSeek, Qwen, Phi, and other LLMs locally"; "Serve local models on OpenAI-like endpoints, locally and on the network"; "LM Studio can operate entirely offline". Runtimes: llama.cpp on Mac/Windows/Linux, MLX on Apple Silicon. "llmster is the headless version of LM Studio, no desktop app required." [docs/app](https://lmstudio.ai/docs/app). Note: on 2026-10-30 the root `lmstudio.ai` served a page for "Bionic ... LM Studio's agent for open models", with a Windows x64 download and an account sign-up; it stated "cloud services are Zero Data Retention (ZDR) across the board". [lmstudio.ai](https://lmstudio.ai/)
- **License:** Proprietary. Terms (version dated August 23, 2026) grant a "non-exclusive, non-transferable license to use the Software solely for Your personal and / or internal business purposes"; "the Software and its structure, organization, and source code constitute valuable trade secrets"; no modification, derivative works, sublicensing, SaaS or service-bureau use; "Paid Features" may carry fees. [terms](https://lmstudio.ai/terms). Tailscale's post says LM Studio "is free for personal use and for work, with enterprise plans offering advanced features". [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access)
- **Platforms:** macOS: "Apple Silicon (M1/M2/M3/M4)", "macOS 14.0 or newer is required", "Intel-based Macs are currently not supported", "16GB+ RAM recommended". Windows: x64 and ARM (Snapdragon X Elite), "AVX2 instruction set support is required (for x64)", 16GB RAM and 4GB VRAM recommended. Linux: x64 and ARM64 AppImage, Ubuntu 20.04+. [system requirements](https://lmstudio.ai/docs/app/system-requirements). Mobile: "Locally" is "LM Studio's mobile app" for iPhone and iPad; "LM Link on iPhone and iPad" announced 2026-06-04. [Locally post](https://lmstudio.ai/blog/locally-lm-link)
- **Distributed mode:** Whole-request remote only. LM Link: "Link your machines, and then load remote models as if they were local." Remote models appear in the model loader; chats stay local; any tool pointed at `localhost:1234` (Codex, Claude Code, OpenCode named) can use remote models. "LM Link is in Preview. We are rolling out access in batches." "Free for the duration of the Preview period"; free and paid plans at GA, free tier with device and user limits. [LM Link](https://lmstudio.ai/link)
- **Auth / encryption between devices:** Links are "custom made, end-to-end encrypted networks intended for loading and serving LLMs across devices you own"; "All communication and data transfer between devices is always end-to-end encrypted, thanks to Tailscale." [LM Link docs](https://lmstudio.ai/docs/lmlink). "Your devices are never exposed to the public internet"; "runs entirely in userspace"; apart from the device list, "which goes to LM Studio's servers for discovery and connection", data stays between devices; coexists with an existing Tailscale VPN. [LM Link](https://lmstudio.ai/link). Tailscale (2026-02-25): "built on tsnet"; devices authenticate then "establish an end-to-end encrypted connection"; prompts and responses are "never seen, either by Tailscale or LM Studio's backend service"; the backend handles "device discovery, keep-alives, and configuration data". [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access). Local server: "By default, the LM Studio API server does **not** require authentication"; token auth can be enabled in server settings and sent as `Authorization: Bearer`. [REST quickstart](https://lmstudio.ai/docs/developer/rest/quickstart)
- **Discovery / pairing UX:** Account-based. "In the desktop app, choose 'Add a remote machine'" or "run `lms login`, then `lms link enable`". [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access). Access requires requesting a Link at `lmstudio.ai/lm-link/request`. [LM Link](https://lmstudio.ai/link). **Per-device removal or revocation is not described on any page read**; the docs list sub-pages "Add a Device" and "Set a preferred device" whose contents were not fetched. [LM Link docs](https://lmstudio.ai/docs/lmlink)
- **API:** OpenAI-compatible `GET /v1/models`, `POST /v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`, plus `/v1/decisions`; official clients work via `OpenAI(base_url="http://localhost:1234/v1")`. [OpenAI compat](https://lmstudio.ai/docs/developer/openai-compat)
- **Community signals:** Closed source, so no star count. Discord at `discord.gg/lmstudio` (member count not shown, **unverified**); public bug tracker on GitHub. [OpenAI compat](https://lmstudio.ai/docs/developer/openai-compat)
- **Recurring complaints:** (a) LM Link is gated and account-bound: a March 2026 bug ("LM Link works only from one account from the same client PC", #1648) showed the connector living in a per-user `.lmstudio` folder; resolved only after "several LM Studio updates on both machines" with no root cause named. [bug tracker #1648](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/1648). A widely shared post objecting to having to "apply to use 'LM Link' and hope they get me off the waitlist" to reach local models on a home network, and a competitor page describing a February 2026 r/LocalLLaMA thread objecting to mandatory sign-in, are **unverified** (snippets only). (b) Closed source and proprietary terms (primary, above). (c) No official "model loading guardrails" page was found; the memory-protection behaviour of the app is **unverified**.

### 3.4 llama.cpp (llama-server and the RPC backend)

- **Positioning:** "LLM inference in C/C++"; "LLM (and VLM) inference with minimal setup"; "Apple silicon is a first-class citizen". [README](https://github.com/ggml-org/llama.cpp)
- **License:** MIT. [README](https://github.com/ggml-org/llama.cpp)
- **Platforms / backends:** plain C/C++, AVX/AVX2/AVX512/AMX, RISC-V, Metal, CUDA, HIP, MUSA, Vulkan, SYCL, OpenCL, WebGPU, CANN, Hexagon, zDNN, ZenDNN, OpenVINO (in progress); CPU+GPU hybrid for models larger than VRAM. [README](https://github.com/ggml-org/llama.cpp)
- **Distributed mode:** Genuine partitioning via RPC. `ggml-rpc-server` exposes a host's devices over TCP (or RDMA: RoCEv2 on Linux, RDMA over Thunderbolt 5 on Apple Silicon with macOS 26.2+); llama.cpp "distributes model weights and the KV cache across all available devices" proportional to memory; `--tensor-split` overrides. Optional on-disk cache at `$HOME/.cache/llama.cpp/rpc`. [RPC README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- **Auth / encryption between devices:** None. "This example and the RPC backend are currently in a proof-of-concept development stage. As such, the functionality is fragile and insecure. Never run the RPC server on an open network or in a sensitive environment!" No authentication, encryption or access control is mentioned. [RPC README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- **Discovery / pairing UX:** Manual: `--rpc host:port,host:port`; server port via `-p` (default `127.0.0.1:50052`). [RPC README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- **llama-server:** "Fast, lightweight, pure C/C++ HTTP server based on httplib, nlohmann::json and llama.cpp." OpenAI-compatible chat completions, responses and embeddings. `--api-key KEY` "(default: none)", `--api-key-file`; `/health` is public. `--host` default `127.0.0.1`, `--port` default `9931`. TLS via `--ssl-key-file`/`--ssl-cert-file` when built with `-DLLAMA_OPENSSL=ON`. By default the server reflects any `Origin` with credentials allowed. `--tools`/`--agent` expose file read/write and should not be enabled "in untrusted environments". For public deployment: set an API key and use a reverse proxy. Model download: `-hf <user>/<model>[:quant]` (default Q4_K_M), `--model-url`; no integrity-verification statement on the page. Memory fit: `--fit [on|off]` "whether to adjust unset arguments to fit in device memory ... default: 'on'", `--fit-target` (1024 MiB margin), `--fit-ctx` (min 4096); router mode `--models-memory-margin` unloads LRU models. [server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- **Community signals:** 132.8k stars, 875 watchers, 25.0k forks, 757 open issues, 1.8k open PRs. GitHub Discussions and Issues; no Discord or Slack listed. [README](https://github.com/ggml-org/llama.cpp)
- **Recurring complaints:** Not sampled from the issue tracker in this pass (**unverified**). The RPC README's own warning is the salient user-facing caveat.

### 3.5 Petals (bigscience-workshop/petals)

- **Positioning:** "Run LLMs at home, BitTorrent-style. Fine-tuning and inference up to 10x faster than offloading." [README](https://github.com/bigscience-workshop/petals)
- **License:** MIT. [README](https://github.com/bigscience-workshop/petals)
- **Platforms:** Linux (Anaconda/pip, NVIDIA; AMD via wiki), Windows via WSL, Docker (NVIDIA), macOS M1/M2 via Homebrew/pip. [README](https://github.com/bigscience-workshop/petals)
- **Distributed mode:** Genuine partitioning across a volunteer swarm: load one part of a model and connect to peers hosting the rest; "up to 6 tokens/sec for Llama 2 (70B)". [README](https://github.com/bigscience-workshop/petals)
- **Auth / encryption between devices:** None documented. "Your data will be processed with the help of other people in the public swarm"; for sensitive data, run a private swarm; "Hosting a server does not allow others to run custom code on your computer." [README](https://github.com/bigscience-workshop/petals)
- **Discovery / pairing UX:** Public swarm monitor at health.petals.dev; private swarms via wiki. [README](https://github.com/bigscience-workshop/petals)
- **Community signals:** 10.7k stars, 649 forks, 94 open issues, 522 commits; Discord linked. [README](https://github.com/bigscience-workshop/petals)
- **Maintenance status:** The five most recent commits on `main` are dated 2024-08-25 and 2024-07-24. [commits](https://github.com/bigscience-workshop/petals/commits/main). Issue #633 "Is this project dead?" (opened 2026-09-04: "the demo bot fails, and there is no recent changes") is open with no maintainer reply. [issue #633](https://github.com/bigscience-workshop/petals/issues/633). A vendor blog calls it "in maintenance mode" with a "currently broken" status widget. [SharedLLM blog](https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html)
- **Recurring complaints:** Project inactivity (primary, above); public-swarm privacy (primary, README); health site timing out (#624, **unverified**, snippet).

### 3.6 prima.cpp

- **Positioning:** "Fast 30-70B LLM Inference on Heterogeneous and Low-Resource Home Clusters"; a "distributed implementation" of llama.cpp. [Gitee](https://gitee.com/zonghang-li/prima.cpp). Paper: "a distributed inference system that runs 70B-scale models on everyday home devices"; "15× faster than llama.cpp on 70B models" (authors' own benchmark). [arXiv](https://arxiv.org/html/2504.08791v1)
- **Repository status:** `github.com/Lizonghang/prima.cpp` returned HTTP 404 on 2026-10-30. The paper abstract now points to "https://gitee.com/zonghang-li/prima.cpp". [HF paper page](https://huggingface.co/papers/2504.08791), [Gitee](https://gitee.com/zonghang-li/prima.cpp). A GitHub fork (`async0x42/prima.cpp`) carries the README. [fork](https://github.com/async0x42/prima.cpp). The reason for the GitHub 404 is **unverified** (a snippet attributed it to an account block).
- **License:** MIT (license text credits "The ggml authors" and "the prima.cpp authors"). [Gitee](https://gitee.com/zonghang-li/prima.cpp), [fork](https://github.com/async0x42/prima.cpp)
- **Platforms:** "macOS, Linux, Android, HarmonyOS, etc." (Android/HarmonyOS via Termux); Windows: "Not yet—but it's on the roadmap." GPUs: "Now prima.cpp supports only CUDA-based GPUs"; Metal appears in build notes; Vulkan on roadmap. [Gitee](https://gitee.com/zonghang-li/prima.cpp). Test cluster: Mac M1, Linux laptop with RTX 3070, Linux desktop with RTX 2080 Ti, Mate40Pro phone. [arXiv](https://arxiv.org/html/2504.08791v1)
- **Distributed mode:** Genuine partitioning: piped-ring parallelism with prefetching, mmap-managed weights, Halda layer-assignment scheduler. [arXiv](https://arxiv.org/html/2504.08791v1)
- **Auth / encryption between devices:** None documented. Setup advice is to "disable the firewall to prevent the ports needed (e.g., 9000, 10000) been blocked." [fork](https://github.com/async0x42/prima.cpp), [Gitee](https://gitee.com/zonghang-li/prima.cpp)
- **Discovery / pairing UX:** Manual ring: `--world`, `--rank`, `--master 192.168.1.2 --next 192.168.1.3`; ZeroMQ on ports 9000 (data) and 10000 (signal). [Gitee](https://gitee.com/zonghang-li/prima.cpp)
- **API:** Examples use `llama-cli`; server example binds 127.0.0.1 with no auth documented. [Gitee](https://gitee.com/zonghang-li/prima.cpp)
- **Community signals:** Gitee shows 23 stars, 10 forks, 4,234 commits. GitHub star count unavailable (404). [Gitee](https://gitee.com/zonghang-li/prima.cpp)
- **Recurring complaints / limitations:** "each device is assigned at least one model layer" (inefficient for small models); Termux required on phones; "70B models remain much slower than those on the cloud"; "Token latency is heavily affected by memory competition." [fork](https://github.com/async0x42/prima.cpp), [arXiv](https://arxiv.org/html/2504.08791v1)

### 3.7 distributed-llama (b4rtaz/distributed-llama)

- **Positioning:** "Connect home devices into a powerful cluster to accelerate LLM inference. More devices means faster inference." [README](https://github.com/b4rtaz/distributed-llama)
- **License:** MIT. [README](https://github.com/b4rtaz/distributed-llama)
- **Platforms:** "Supports Linux, macOS, and Windows"; "Optimized for ARM and x86_64 AVX2 CPUs"; Raspberry Pi guide; Vulkan experimental. [README](https://github.com/b4rtaz/distributed-llama), [docs dir](https://github.com/b4rtaz/distributed-llama/tree/main/docs)
- **Distributed mode:** Genuine partitioning (tensor parallelism). Root node loads weights and syncs state; workers process slices; "You can run Distributed Llama only on 1, 2, 4... 2^n nodes"; max nodes = model's KV heads. [README](https://github.com/b4rtaz/distributed-llama)
- **Auth / encryption between devices:** Not mentioned. [README](https://github.com/b4rtaz/distributed-llama)
- **Discovery / pairing UX:** Manual: workers listen with `--host`/`--port`; root lists `--workers 10.0.0.1:9999 10.0.0.2:9999`. [README](https://github.com/b4rtaz/distributed-llama)
- **API:** `dllama-api` runs an API server; OpenAI compatibility **unverified** (no API doc found in `docs/`). [README](https://github.com/b4rtaz/distributed-llama), [docs dir](https://github.com/b4rtaz/distributed-llama/tree/main/docs)
- **Community signals:** 3.1k stars, 257 forks; Discord badge; Discussions tab. [README](https://github.com/b4rtaz/distributed-llama)
- **Recurring complaints / limitations:** power-of-two node count; KV-head ceiling (#70); only q40/q80 or f32/f32 quantization combinations. [README](https://github.com/b4rtaz/distributed-llama)

### 3.8 LocalAI (mudler/LocalAI) and its P2P/federation

- **Positioning:** "LocalAI is the open-source AI engine"; "any model - LLMs, vision, voice, image, video - on any hardware"; "Drop-in API compatibility: OpenAI, Anthropic, and ElevenLabs APIs across every backend"; also a drop-in Ollama API. [README](https://github.com/mudler/LocalAI)
- **License:** MIT. [README](https://github.com/mudler/LocalAI)
- **Platforms:** macOS DMG ("not signed by Apple", quarantine removal required), Linux, Docker/podman; NVIDIA, AMD ROCm, Intel SYCL, Apple Metal, Vulkan, Jetson, CPU-only. Windows not on the README. [README](https://github.com/mudler/LocalAI)
- **Distributed mode:** Both kinds, "experimental" with "tech preview quality". Federated: requests "routed to a single worker node in the network based on the load balancer's decision" (whole-request remote). Worker/sharding: "The weights are split proportional to the memory when running into worker mode", built on llama.cpp RPC (PR #6829), llama.cpp-compatible models only; "Only a single model is supported currently"; "additional workers cannot be added once inference has begun." [distribute docs](https://localai.io/docs/features/distribute/)
- **Auth / encryption between devices:** Shared token: "Nodes are automatically discovered and connect via p2p by using a shared token which makes sure the communication is secure and private." Built on go-libp2p and EdgeVPN. The encryption protocol and key handling are not described; anyone holding the token can join; "Listing publishes its token, so anyone who sees the list can use the swarm's workers." Without P2P, plain `LLAMACPP_GRPC_SERVERS="address1:port,address2:port"` (inherits RPC's lack of auth). [distribute docs](https://localai.io/docs/features/distribute/)
- **Discovery / pairing UX:** Automatic via DHT by default; `LOCALAI_P2P_DISABLE_DHT=true` makes it "local only (mDNS)". Token copied from WebUI or `curl http://localhost:8000/p2p/token`. Containers need host networking. [distribute docs](https://localai.io/docs/features/distribute/)
- **Community signals:** 50.1k stars, 4.6k forks; Discord and X. [README](https://github.com/mudler/LocalAI)
- **Recurring complaints:** No 2026 P2P-specific issues surfaced in search (**unverified**); the docs' own "tech preview", single-model and no-late-join limits are the stated caveats.

### 3.9 Jan (janhq/jan)

- **Positioning:** "Jan is an open source alternative to ChatGPT that runs 100% offline on your computer." [README](https://github.com/janhq/jan)
- **License:** Apache-2.0, confirmed from the LICENSE file ("Licensed under the Apache License, Version 2.0"; "Copyright 2025 Menlo Research"). [LICENSE](https://github.com/janhq/jan/blob/dev/LICENSE). A secondary guide's "AGPLv3" claim conflicts with this and is treated as wrong.
- **Platforms:** Windows (.exe, Microsoft Store), macOS 13.6+ (universal .dmg), Linux (.deb, AppImage, Flathub, Arm64 guide). Engine: bundled llama.cpp (CPU, Vulkan, Metal, CUDA 12/13, ROCm) and MLX on Apple Silicon. [README](https://github.com/janhq/jan), [API server docs](https://docs.jan.ai/desktop/api-server)
- **Distributed mode:** None. "Cloud Integration" means hosted providers (OpenAI, Anthropic, Mistral, Groq). [README](https://github.com/janhq/jan)
- **Auth / encryption:** Local server at `http://127.0.0.1:1337/v1`; host `127.0.0.1` by default ("only accessible from your own computer"), `0.0.0.0` available ("Use this with caution"); optional API key sent as `Authorization: Bearer`, and leaving it empty is "not recommended when binding to `0.0.0.0`"; CORS on by default; Trusted Hosts allowlist. Bundled llama.cpp "does not load models on Intel Macs as of v0.8.5". [API server docs](https://docs.jan.ai/desktop/api-server)
- **API:** "built-in, OpenAI-compatible API server that runs entirely on your computer." [API server docs](https://docs.jan.ai/desktop/api-server)
- **Community signals:** 45.2k stars, 3.1k forks; Discord (`#🆘|jan-help`). [README](https://github.com/janhq/jan)
- **Recurring complaints:** GPU detection regressions by release (0.7.3, 0.7.5, 0.7.9) across NVIDIA, AMD and Flatpak, and model-load failures — issue titles #6999, #8053, #7341, #8005, #7553, #7786 from search (**not opened; unverified**). README memory guidance (8GB for 3B, 16GB for 7B, 32GB for 13B) is the only fit guidance on the pages read. [README](https://github.com/janhq/jan)

### 3.10 2026 newcomers that pair personal devices

#### 3.10.1 NVIDIA PAIR (Personal AI Router)

- **Positioning:** "a local inference router for a group of compatible computers on the same network"; "Router that virtually distributes inference across connected devices in the home." [README](https://github.com/NVIDIA/Personal-AI-Router)
- **License:** Apache-2.0. [README](https://github.com/NVIDIA/Personal-AI-Router)
- **Platforms:** Windows 11, Linux, macOS 13+ (Apple Silicon or Intel); x64 and arm64; `.exe`, `.deb`, `.dmg` installers; "Windows on ARM is experimental"; mixed-OS clusters supported. Hardware table: RTX Spark, DGX Spark, GeForce RTX 20-series+, RTX PRO Turing+, Mac. [README](https://github.com/NVIDIA/Personal-AI-Router), [build page](https://build.nvidia.com/rtx/pair.md)
- **Distributed mode:** Whole-request remote only. "PAIR routes each independent request to one node." "It does not combine GPU memory, join GPUs into one larger GPU, or split a model or request across systems." Engines: Ollama, LM Studio, llama.cpp (v1.0.0 added managed llama.cpp). [README](https://github.com/NVIDIA/Personal-AI-Router), [build page](https://build.nvidia.com/rtx/pair.md)
- **Auth / encryption between devices:** "The cluster manager uses a six-digit PIN to bootstrap trust." "The six-digit PIN is low entropy" and should not be treated as "a durable credential or as strong proof of physical presence." "The PIN does not protect a node before pairing." "Cluster-scoped peer traffic and promoted proxy ingress are designed to use certificates and mutual TLS after pairing", but only "when identity and certificate material are present and the relevant workers use that transport." "Discovery and node-information traffic can use plain HTTP." mTLS "does not automatically protect loopback HTTP, plain discovery metadata, node-information HTTP", Electron IPC or third-party engine APIs. Local proxies "accept requests only from the local system" (remote requests get 403). Logging policy: prompts, messages, chunks and response bodies "should not be written to logs". [SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md), [getting started](https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx), [build page](https://build.nvidia.com/rtx/pair.md)
- **Revocation:** Not documented. SECURITY.md says only to "remove members that are no longer authorized" and lists "member removal" as an area "needing focused review and tests"; certificate revocation and rotation are not described; the getting-started page "doesn't say how to remove a paired node". [SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md), [getting started](https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx)
- **Discovery / pairing UX:** mDNS on UDP 5353; node-to-node TCP 14318–14323; "Add node" → pick a discovered system → inviting system shows a six-digit PIN → invited system accepts a "Cluster invitation" modal and enters the PIN. If discovery fails "you can add it by IP address." "Only pair systems while both devices and the local network are trusted." [getting started](https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx)
- **API:** Ollama-compatible (11434), OpenAI-compatible (1234), llama.cpp (8080) proxies, plus Anthropic Messages API; engines are moved to higher ports. [getting started](https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx), [README](https://github.com/NVIDIA/Personal-AI-Router)
- **Community signals:** 1.7k stars, 287 forks, 25 watchers; Issues and Discussions; no Discord listed. [README](https://github.com/NVIDIA/Personal-AI-Router). Announcement date (reported as 2026-09-03) is **unverified** (secondary sources only).
- **Limitations (roadmap gaps):** no request queuing, no cross-engine routing for OpenAI-compatible requests, no launch on startup, no requester-only clients; "Run only one PAIR interface per system"; GPU-memory display "can understate available memory on Windows systems with unified memory". [README](https://github.com/NVIDIA/Personal-AI-Router), [build page](https://build.nvidia.com/rtx/pair.md)

#### 3.10.2 Mesh LLM (Mesh-LLM/mesh-llm)

- **Positioning:** "Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat." Self-described "experimental distributed-systems software." [README](https://github.com/Mesh-LLM/mesh-llm)
- **License:** Apache-2.0. [README](https://github.com/Mesh-LLM/mesh-llm)
- **Platforms:** macOS bundles (Homebrew for Apple Silicon), Linux and Windows builds for CPU, CUDA, ROCm, Vulkan; Linux ARM64; `mesh-llm.exe` "not code-signed yet"; native Windows CUDA has three open bugs. [README](https://github.com/Mesh-LLM/mesh-llm)
- **Distributed mode:** Both. Default: "if one node can host the full model, it serves it locally without stage traffic." `--split`: coordinator assigns contiguous layer ranges across stages. Experimental Mixture-of-Agents gateway (`model: "mesh"`). [README](https://github.com/Mesh-LLM/mesh-llm)
- **Auth / encryption between devices:** QUIC "end-to-end encrypts traffic between Mesh nodes," including requests, responses and split-model activations; iroh relays "forward packets without reading their payload". Private meshes are invite-token based (`--join <token>`); owner-control lane `mesh-llm-control/1`; identity data in `~/.mesh-llm`. Per-device revocation not described. [README](https://github.com/Mesh-LLM/mesh-llm)
- **Discovery / pairing UX:** Invite token for private meshes; published meshes advertise via Nostr; Windows firewall guide opens UDP 5353. [README](https://github.com/Mesh-LLM/mesh-llm)
- **API:** OpenAI-compatible at `http://localhost:9337/v1`; web console on 3131. [README](https://github.com/Mesh-LLM/mesh-llm)
- **Community signals:** 3.7k stars, 476 forks, 2,927 commits; v0.75.1 stable, v0.76.0-rc8 prerelease; Discussions, Issues, Community Forum; sponsored by spiral.xyz. [README](https://github.com/Mesh-LLM/mesh-llm)

#### 3.10.3 SharedLLM (vendor-described; repo not reachable)

- The author's own comparison post (2026-04-11) describes SharedLLM as "community-owned, privacy-first, AGPL-3.0, built on llama.cpp's RPC backend so you can bring any GGUF", with "coordinator + mesh" topology, workers vouched "via HMAC cluster secret", no encryption-in-transit claim, "no public reference coordinator yet", alpha v0.1.0, and a known "upstream llama.cpp RPC assertion on certain tensor shapes". [SharedLLM blog](https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html). The linked repo `github.com/MHASK/sharedllm` returned 404 on 2026-10-30, so stars, platforms and current status are **unverified**.

#### 3.10.4 Kalavai (kalavai-net/kalavai-client)

- "Aggregates compute from spare GPU capacity"; Apache-2.0; 223 stars; seed node requires arm64/amd64 Linux with Docker and root; workers "Linux and Windows; amd64 / ARM"; engines vLLM, llama.cpp, Ray; "Kalavai is at an early stage of its development"; joining mechanism not described on the README; Discord, Substack, Discussions. [README](https://github.com/kalavai-net/kalavai-client). Enterprise/pool-oriented rather than personal-device pairing.

#### 3.10.5 Not verified

- DRIFT-LLM (hivemind-based, "weights are spread over the cluster") appeared in search; the repo URL returned 404 and nothing is cited from it (**unverified**).

---

## 4. UCompute's claimed properties: differentiated vs. table stakes

Scope reminder: these are UCompute development-build properties verified on named hardware only. "Differentiated" means no competitor page read documents an equivalent; it does not mean competitors lack it.

| UCompute property | vs. partitioning projects (exo, RPC, distributed-llama, prima.cpp, Petals) | vs. 2026 routers (PAIR, LM Link, Mesh LLM) | Verdict |
|---|---|---|---|
| Authenticated pairing by short code, QUIC + TLS 1.3, device keys pinned at pairing | **Differentiated.** None documents device auth or encryption; exo's API is "unauthorized" by design ([#1833](https://github.com/exo-explore/exo/issues/1833)); RPC is "fragile and insecure" ([RPC README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)); prima.cpp says disable the firewall ([Gitee](https://gitee.com/zonghang-li/prima.cpp)). | **Table stakes with a twist.** All three encrypt. PAIR: PIN then mTLS "designed to", hedged ([SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md)). LM Link: Tailscale E2E, but requires an account and the device list goes to LM Studio's servers ([LM Link](https://lmstudio.ai/link), [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access)). Mesh LLM: QUIC E2E, invite token ([README](https://github.com/Mesh-LLM/mesh-llm)). The twist: no account, no vendor backend, per-device pinned keys rather than a shared token or PIN. | Differentiated vs. tier 1; a specific sub-difference vs. tier 2 |
| One-step revocation (connection closed <0.1 s in tests) | n/a (no auth to revoke) | **Differentiated on paper.** PAIR documents no removal/revocation procedure and flags member removal as needing review ([SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md), [getting started](https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx)). LM Link's add/remove pages were not read; nothing on the pages read describes per-device revocation. Mesh LLM README does not describe it. LocalAI's shared token implies rotating it for everyone, though the page does not say ([distribute docs](https://localai.io/docs/features/distribute/)). | Differentiated, pending reading LM Link's device-management pages |
| Default local-only policy (paired device still refuses every off-device request until opted in) | **Differentiated** in the sense that these projects have no per-device serve/refuse switch at all. | **Partially differentiated.** "Bind to localhost by default" is universal: Ollama 127.0.0.1 ([FAQ](https://docs.ollama.com/faq)), llama-server 127.0.0.1 ([server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)), Jan 127.0.0.1 ([Jan docs](https://docs.jan.ai/desktop/api-server)), PAIR proxies accept "only from the local system" ([build page](https://build.nvidia.com/rtx/pair.md)). What is not documented elsewhere: a device that is already paired yet serves nothing until the owner flips it. | Differentiated only in the "paired but closed" semantics; "localhost by default" is table stakes |
| Audit log of off-device requests without prompt text | Not present in any. | **Differentiated, narrow.** PAIR has a policy that prompts "should not be written to logs" but documents no audit log ([SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md)). LeakIX notes "Ollama doesn't log requests by default" ([LeakIX](https://blog.leakix.net/2026/02/ollama-exposed/)). | Differentiated, narrow |
| Memory-fit check before load | exo places by memory (its core feature) ([README](https://github.com/exo-explore/exo)). | **Table stakes / competitors ahead.** llama-server `--fit` is on by default and auto-adjusts to fit ([server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)); Ollama queues and evicts ([FAQ](https://docs.ollama.com/faq)); PAIR gives memory guidance and shows GPU memory ([build page](https://build.nvidia.com/rtx/pair.md)). | Table stakes; UCompute's "refuse rather than adjust" is a UX choice, not a gap |
| SHA-256-verified downloads with license shown before download | Not documented by any. | **Mostly hygiene.** Ollama pulls are HTTPS-only with a `digest` field, but no verification statement on the pages read ([FAQ](https://docs.ollama.com/faq), [pull API](https://docs.ollama.com/api/pull)); llama-server `-hf` has no integrity statement ([server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)). Showing the model license pre-download is not documented by any competitor page read. | Weakly differentiated; do not lead with it |
| Local OpenAI-compatible API (official clients by changing base URL) | exo supports OpenAI, Claude Messages, Responses and Ollama APIs ([README](https://github.com/exo-explore/exo)). | **Table stakes; competitors ahead.** Ollama ([OpenAI compat](https://docs.ollama.com/api/openai-compatibility)), LM Studio ([OpenAI compat](https://lmstudio.ai/docs/developer/openai-compat)), llama-server, Jan ([Jan docs](https://docs.jan.ai/desktop/api-server)), LocalAI (OpenAI + Anthropic + ElevenLabs) ([README](https://github.com/mudler/LocalAI)), PAIR (OpenAI + Ollama + Anthropic) ([README](https://github.com/NVIDIA/Personal-AI-Router)), Mesh LLM ([README](https://github.com/Mesh-LLM/mesh-llm)). Several add Responses and Anthropic Messages endpoints UCompute has not claimed. | Table stakes |

Net: the defensible, evidence-backed differences are the **trust-model bundle** (pinned per-device keys with no account or vendor backend; one-step revocation; paired-but-closed default; prompt-free audit log). Everything else UCompute has is either universal or done more fully by someone else.

---

## 5. Where competitors are ahead (and by how much, from their own pages)

- **Pooling / partitioning.** exo: pipeline and tensor sharding, RDMA over Thunderbolt 5 ([README](https://github.com/exo-explore/exo)). Mesh LLM: `--split` layer stages over encrypted QUIC ([README](https://github.com/Mesh-LLM/mesh-llm)). llama.cpp RPC: weights and KV cache across devices, RDMA on Linux and macOS ([RPC README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)). distributed-llama, prima.cpp, Petals, LocalAI worker mode. UCompute has design only.
- **Model range and modality.** Ollama's catalog; LocalAI "LLMs, vision, voice, image, video" ([README](https://github.com/mudler/LocalAI)); LM Studio GGUF + MLX ([docs/app](https://lmstudio.ai/docs/app)). UCompute: small open GGUF via one pinned llama.cpp build.
- **Platforms and distribution.** Ollama, LM Studio, Jan, PAIR, Mesh LLM all ship Windows/macOS/Linux builds today; PAIR ships `.exe`/`.deb`/`.dmg` ([README](https://github.com/NVIDIA/Personal-AI-Router)). UCompute: no supported platform yet.
- **Mobile.** LM Studio's Locally on iPhone/iPad over LM Link ([Locally post](https://lmstudio.ai/blog/locally-lm-link)); prima.cpp on Android/HarmonyOS ([Gitee](https://gitee.com/zonghang-li/prima.cpp)). UCompute: not built.
- **Off-LAN reach / NAT traversal.** LM Link works "regardless of what network they're on" via Tailscale ([Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access)); Mesh LLM uses iroh relays ([README](https://github.com/Mesh-LLM/mesh-llm)); LocalAI DHT ([distribute docs](https://localai.io/docs/features/distribute/)). UCompute: LAN only, connect-by-address fallback; relay not built.
- **API surface.** Responses API (Ollama, LM Studio, llama-server, exo), Anthropic Messages (exo, LocalAI, PAIR), tool calling (llama-server `--tools`, LM Studio) — UCompute has not verified tool calling.
- **Maturity and community.** Ollama 185.3k, llama.cpp 132.8k, LocalAI 50.1k, exo 48.1k, Jan 45.2k, Petals 10.7k, Mesh LLM 3.7k, distributed-llama 3.1k, PAIR 1.7k ([sources in §3](#3-per-competitor-profiles)). UCompute: no public code.
- **Auto-update, signed installers.** exo macOS app auto-updates ([README](https://github.com/exo-explore/exo)); PAIR ships installers; LocalAI's DMG is unsigned and Mesh LLM's `.exe` is unsigned (both self-reported). UCompute: no auto-update.

---

## 6. Positioning implications (evidence-constrained)

1. **Do not position Mesh as novel.** PAIR, LM Link and Mesh LLM already own "one request, one of your devices" with shipped installers and larger communities. A claim of novelty is checkable and false.
2. **The honest contrast is the trust model, stated as specifics, not superlatives.** "Pinned per-device keys, no account, no vendor backend in the pairing path, one-step revocation, paired-but-closed by default, audit log with no prompt text" — each is absent from the competitor pages read, and each can be demonstrated rather than asserted. PAIR's SECURITY.md provides the vocabulary for the comparison and is itself candid about the gaps.
3. **The Ollama exposure record is the market's own argument for default-closed behaviour**, but it should be cited as Censys/LeakIX/SecurityWeek findings about an unauthenticated local server being bound to 0.0.0.0, not as a claim that UCompute is "more secure". Note the three counts are not comparable and say so.
4. **Concede the rest explicitly.** No pooling, narrow model range, no supported platform, LAN-only, no mobile. Developers in this space read READMEs and SECURITY.md files; the competitors' own candour (RPC's warning, PAIR's hedges, Mesh LLM's "experimental") sets the tone UCompute should match.
5. **LM Link's account gate is a live irritant** (waitlist, sign-in, device list on vendor servers, per-user connector bug) and UCompute's account-free pairing is a direct, evidence-backed answer to it — but the strongest primary evidence read is LM Studio's own pages and one closed bug; the social-media and Reddit reactions are unverified and should not be quoted.

---

## 7. Unverified items and open questions

- Discord member counts for exo, Ollama, LM Studio, LocalAI, Jan, distributed-llama: not readable on any page fetched.
- NVIDIA PAIR announcement date (reported 2026-09-03) and the Neowin claim of "mTLS and generated certificates after users have given approval": secondary only; PAIR's own SECURITY.md is more hedged.
- LM Link per-device removal/revocation: the "Add a Device" sub-page was not read; absence of documentation is not absence of the feature.
- LM Studio "model loading guardrails": no official page found.
- Ollama blob digests being SHA-256: not stated on the pages read.
- distributed-llama `dllama-api` OpenAI compatibility: no doc found.
- prima.cpp GitHub 404 cause; prima.cpp GitHub star count.
- SharedLLM and DRIFT-LLM repos: 404.
- All GitHub issue titles cited from search for exo, Jan and Ollama (#15453) were not opened.
- Secondary exposure figures (SentinelLABS/Censys 175,000 in January 2026; CSA 31% of 5,200; Cyera 300,000) are quoted from snippets or via SecurityWeek, not from the original reports.

---

## 8. Table of record: raw numbers as shown on 2026-10-30

| Project | Stars | Forks | Open issues | Other |
|---|---|---|---|---|
| Ollama | 185.3k | — | — | — |
| llama.cpp | 132.8k | 25.0k | 757 | 1.8k open PRs |
| LocalAI | 50.1k | 4.6k | — | — |
| exo | 48.1k | 3.6k | 208 | 225 open PRs, 2,462 commits |
| Jan | 45.2k | 3.1k | — | — |
| Petals | 10.7k | 649 | 94 | last commit 2024-08-25 |
| Mesh LLM | 3.7k | 476 | — | 2,927 commits; v0.75.1 |
| distributed-llama | 3.1k | 257 | — | — |
| NVIDIA PAIR | 1.7k | 287 | — | v1.0.0 |
| Kalavai | 223 | 8 | — | — |
| prima.cpp (Gitee) | 23 | 10 | 1 | GitHub 404 |

---

## 9. Sources

### Read directly (48)

exo
- https://github.com/exo-explore/exo
- https://github.com/exo-explore/exo/blob/main/LICENSE
- https://github.com/exo-explore/exo/pull/2419
- https://github.com/exo-explore/exo/issues/1833

Ollama
- https://github.com/ollama/ollama
- https://docs.ollama.com/faq
- https://docs.ollama.com/api/openai-compatibility
- https://docs.ollama.com/api/pull
- https://docs.ollama.com/api/authentication
- https://github.com/ollama/ollama/issues/849
- https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys
- https://blog.leakix.net/2026/02/ollama-exposed/
- https://www.securityweek.com/critical-bug-could-expose-300000-ollama-deployments-to-information-theft/

LM Studio / LM Link
- https://lmstudio.ai/
- https://lmstudio.ai/docs/app
- https://lmstudio.ai/docs/app/system-requirements
- https://lmstudio.ai/terms
- https://lmstudio.ai/link
- https://lmstudio.ai/docs/lmlink
- https://lmstudio.ai/docs/developer/openai-compat
- https://lmstudio.ai/docs/developer/rest/quickstart
- https://lmstudio.ai/blog/locally-lm-link
- https://tailscale.com/blog/lm-link-remote-llm-access
- https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/1648

llama.cpp
- https://github.com/ggml-org/llama.cpp
- https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md
- https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md

Petals
- https://github.com/bigscience-workshop/petals
- https://github.com/bigscience-workshop/petals/issues/633
- https://github.com/bigscience-workshop/petals/commits/main

prima.cpp
- https://arxiv.org/html/2504.08791v1
- https://huggingface.co/papers/2504.08791
- https://gitee.com/zonghang-li/prima.cpp
- https://github.com/async0x42/prima.cpp (fork of the original)

distributed-llama
- https://github.com/b4rtaz/distributed-llama
- https://github.com/b4rtaz/distributed-llama/tree/main/docs

LocalAI
- https://github.com/mudler/LocalAI
- https://localai.io/docs/features/distribute/

Jan
- https://github.com/janhq/jan
- https://github.com/janhq/jan/blob/dev/LICENSE
- https://docs.jan.ai/desktop/api-server

Newcomers and adjacent
- https://github.com/NVIDIA/Personal-AI-Router
- https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md
- https://github.com/NVIDIA/Personal-AI-Router/blob/main/docs/getting-started.mdx
- https://build.nvidia.com/rtx/pair.md
- https://github.com/Mesh-LLM/mesh-llm
- https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html
- https://github.com/kalavai-net/kalavai-client

### Attempted, not reachable (404 or moved)
- https://github.com/Lizonghang/prima.cpp (404)
- https://lmstudio.ai/docs/link (404; the live page is /docs/lmlink)
- https://localai.io/features/distribute/ (moved to /docs/features/distribute/)
- https://github.com/b4rtaz/distributed-llama/blob/main/docs/HOW_TO_RUN_API.md (404)
- https://github.com/MHASK/sharedllm (404)
- https://github.com/ApexDevelopment/DRIFT-LLM (404)

### Seen only as search-result snippets (not cited as fact)
exo issues #1534, #2271, #1682, #952, #879, #711, #724, #1043; Jan issues #6999, #8053, #7341, #8005, #7553, #7786; Ollama issues #1053, #15453; LM Studio bug tracker #2087; Neowin, aiweekly, MindStudio and other PAIR write-ups; Private LLM comparison page; humla.team; Cyera and CSA research notes; SentinelLABS/Censys January 2026 figure; Theo (t3.gg) post on X.
