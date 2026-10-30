# Competitive positioning: local and multi-device LLM inference (as of 2026-10-30)

Lens: competitors-positioning. Internal strategy input for UCompute.

Method: 45 URLs fetched directly (see Sources). Facts are cited inline to the page they came from. Anything marked **unverified** came from a search-result snippet or a secondary write-up, or could not be confirmed on a primary page. Star counts, issue counts and version numbers are what the page showed on 2026-10-30 and will drift. No statistics are invented; where a page gave no number, none is stated.

A note on the subject: UCompute is unreleased (public repo holds only a LICENSE; private alpha behind access control; macOS Apple Silicon build, M2 and one Windows 11 Intel Arc laptop demonstrated, Linux CPU daemon in tests). Every comparison below is "UCompute's development-build behaviour vs. a shipped product's documentation". That asymmetry matters for how any of this may be said publicly.

---

## 1. Executive summary

1. **"Route the whole request to one of your own devices" is no longer a lonely position.** Three 2026 products do exactly what UCompute Mesh does and say so in almost the same words: NVIDIA PAIR (Apache-2.0, Win/Linux/macOS installers, "routes each independent request to one node ... does **not** pool GPU memory"), LM Studio's LM Link (Preview, Tailscale-based, "use models on remote machines as if they were local"), and Mesh LLM's default routing mode ("If one node can host the full model, it serves the model locally without stage traffic"). [PAIR README](https://github.com/NVIDIA/Personal-AI-Router), [LM Link](https://lmstudio.ai/link), [Mesh LLM README](https://github.com/Mesh-LLM/mesh-llm).
2. **Against the partitioning projects (exo, llama.cpp RPC, distributed-llama, prima.cpp, Petals), UCompute's security posture is genuinely differentiated**: those projects document no authentication or encryption between devices, and two of them say so bluntly. exo's maintainer closed an unauthenticated-endpoint report with "this is intended behaviour, exo's api is unauthorized" ([exo #1833](https://github.com/exo-explore/exo/issues/1833)); llama.cpp's RPC README calls itself "fragile and insecure" and says "Never run the RPC server on an open network or in a sensitive environment!" ([rpc README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)).
3. **Against the 2026 routers (PAIR, LM Link, Mesh LLM), authenticated encrypted transport is table stakes.** PAIR uses a six-digit PIN then "mutual TLS restricted to nodes in the cluster"; LM Link is "end-to-end encrypted, thanks to Tailscale"; Mesh LLM says "QUIC end-to-end encrypts traffic between Mesh nodes". What none of them documents on the pages read: a one-step per-device revocation procedure, an audit log of off-device requests, or a default that refuses every off-device request until the user opts in. Those three are UCompute's narrowest real differences. [PAIR overview](https://docs.nvidia.com/local-ai/nvpair), [PAIR SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md), [LM Link docs](https://lmstudio.ai/docs/lmlink), [Mesh LLM README](https://github.com/Mesh-LLM/mesh-llm).
4. **Where competitors are clearly ahead**: pooling/partitioning (exo tensor-parallel with RDMA over Thunderbolt 5; Mesh LLM split mode; llama.cpp RPC; distributed-llama; prima.cpp), model range and multimodality (Ollama, LM Studio, LocalAI), platform coverage (Ollama/LM Studio/Jan ship Win/Mac/Linux; PAIR ships signed installers for all three), mobile (LM Studio's Locally iPhone/iPad app), NAT traversal/relays (LM Link via Tailscale, Mesh LLM via iroh relays), and sheer maturity (Ollama 185.3k stars, llama.cpp 132.8k, LocalAI 50.1k, exo 48.1k, Jan 45.2k).
5. **Two external facts strengthen UCompute's two least glamorous features.** Censys found "10.6K high-confidence Ollama instances exposed to the Internet" with 1.5K answering prompts, because people bind an unauthenticated local server to 0.0.0.0 ([Censys](https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys), [Ollama auth docs](https://docs.ollama.com/api/authentication)). And a live llama.cpp RPC issue reports cache files "truncated on disk-full are later served as valid cache hits → silent weight corruption" ([llama.cpp RPC issues](https://github.com/ggml-org/llama.cpp/issues?q=is%3Aissue+is%3Aopen+rpc)), which is the failure mode hash-verified artifacts exist to prevent.

---

## 2. Per-competitor profiles

Format per project: positioning / license / platforms / distributed mode / auth and encryption between devices / discovery and pairing UX / community signals / channels / recurring complaints.

### 2.1 exo (exo-explore/exo)

- **Positioning:** "Run frontier AI locally." "Maintained by exo labs." Splits models across devices: "exo figures out the best way to split your model across all available devices." [README](https://github.com/exo-explore/exo)
- **License:** Apache-2.0 (the archived predecessor repo was GPL-3.0; **unverified**, from a search snippet). [README](https://github.com/exo-explore/exo)
- **Platforms:** macOS app needs "a Mac with Apple silicon and macOS Sequoia 15.1 or later"; source builds on macOS and Linux; "exo currently runs on CPU" on Linux, Linux GPU "under development". No Windows. MLX is the backend. RDMA over Thunderbolt 5 requires macOS 26.2+. [README](https://github.com/exo-explore/exo)
- **Distributed mode:** Genuine partitioning (pipeline and tensor sharding; README claims up to 1.8x on 2 devices and 3.2x on 4 devices; these are the project's own numbers). [README](https://github.com/exo-explore/exo)
- **Auth/encryption between devices:** Not mentioned in the README. On the HTTP API, the maintainer's position is explicit: issue #1833 ("Unauthenticated Remote Instance Termination", opened 2026-04-02) was closed the same day as not planned with "this is intended behaviour, exo's api is unauthorized", recommending a reverse proxy if exposed. [exo #1833](https://github.com/exo-explore/exo/issues/1833). This became CVE-2026-50759 (CVSS 7.5, CWE-306, affecting 1.0.69) per SentinelOne's database, whose page notes its own content is AI-generated; treat the CVE details as **secondary**. [SentinelOne](https://www.sentinelone.com/vulnerability-database/cve-2026-50759/). A separate secondary write-up describes an earlier RCE path via TRUST_REMOTE_CODE defaulting to true and the API exposed on all interfaces, patched for the remote-code default only; **secondary**, no CVE named. [EnterpriseSecurityTech](https://www.enterprisesecuritytech.com/post/unauthenticated-rce-in-exo-raises-alarms-about-security-in-open-source-ai-infrastructure)
- **Discovery/pairing UX:** "automatically discover each other - no manual configuration"; cluster names isolate groups on one network; Zenoh namespace setting referenced. No pairing step. [README](https://github.com/exo-explore/exo)
- **API:** "Compatible with OpenAI Chat Completions API, Claude Messages API, OpenAI Responses API, and Ollama API." [README](https://github.com/exo-explore/exo)
- **Community signals:** 48.1k stars, 3.6k forks, 208 open issues, 2,462 commits. Discord and X linked; Discord member count not readable on the page (**unverified**). [README](https://github.com/exo-explore/exo)
- **Recurring complaints (first page of open issues):** discovery/networking ("Two Ubuntu nodes on the same LAN fail to discover each other", master/worker IP disagreement, "Election restarts every ~5 s"), Thunderbolt not being used when available, Linux CPU "pinned to a single thread", "Memory leak in macOS app requiring periodic restarts", "EXO.app stuck at ~105–110% CPU", "Path traversal in DELETE /download/...", and an open "Project maintenance status and roadmap?" question. [exo issues](https://github.com/exo-explore/exo/issues)

### 2.2 Ollama

- **Positioning:** "Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models." Local or "in the cloud". [README](https://github.com/ollama/ollama)
- **License:** MIT. [README](https://github.com/ollama/ollama)
- **Platforms:** macOS, Windows, Linux, Docker. [README](https://github.com/ollama/ollama)
- **Distributed mode:** None on the pages read. Cloud models are the "remote" story: `ollama signin`, `OLLAMA_API_KEY`, `OLLAMA_NO_CLOUD=1` to disable. [FAQ](https://docs.ollama.com/faq), [auth](https://docs.ollama.com/api/authentication)
- **Auth/encryption:** Local API "does not require authentication". Binds "127.0.0.1 port 11434 by default"; exposing is a one-line `OLLAMA_HOST=0.0.0.0:11434`. The FAQ offers only a proxy (Nginx, ngrok, Cloudflare Tunnel) as the way to expose it; no API-key guidance for local. [auth](https://docs.ollama.com/api/authentication), [FAQ](https://docs.ollama.com/faq). Consequence: Censys (2025-09-24) found "10.6K high-confidence Ollama instances exposed to the Internet", 1.5K responding to prompts, "approximately 10,600 services ... across 1,229 autonomous systems", >25% on non-default ports. [Censys](https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys)
- **Discovery/pairing:** n/a.
- **API:** "Ollama supports a subset of the OpenAI API": `/v1/chat/completions`, `/v1/completions`, `/v1/models`, `/v1/embeddings`, `/v1/responses` (stateless), audio endpoints. "The client requires an API key value, but Ollama ignores it." [OpenAI compat](https://docs.ollama.com/api/openai-compatibility)
- **Privacy statement:** "Ollama runs locally. We don't see your prompts or data when you run locally." Cloud: "do not store or log that content and never train on it." [FAQ](https://docs.ollama.com/faq)
- **Community signals:** 185.3k stars, 18.7k forks, 2,614 open issues. Discord, X, r/ollama. [README](https://github.com/ollama/ollama), [issues](https://github.com/ollama/ollama/issues)
- **Recurring complaints:** OpenAI-compat edge cases (`/v1/models` returns `"data": null`, reasoning dropped on content-parts arrays), memory estimation ("Memory estimate for Gemma 4 E-series ... is 3-4x actual VRAM, causing needless evictions"), scheduler eviction order, GPU detection in the UI, AMD card support, pull/resume failures, intermittent 500s from the embedded llama-server. [issues](https://github.com/ollama/ollama/issues)

### 2.3 LM Studio (including LM Link and llmster)

- **Positioning:** "run Llama, DeepSeek, Qwen, Phi, and other LLMs locally"; "Serve local models on OpenAI-like endpoints, locally and on the network." Runtimes: llama.cpp (GGUF) on all three OSes, MLX on Apple Silicon. [docs](https://lmstudio.ai/docs/app)
- **License:** Proprietary. Terms grant a "non-exclusive, non-transferable license to use the Software solely for Your personal and / or internal business purposes"; source is treated as trade secrets; some features "may be offered for a fee". [terms](https://lmstudio.ai/terms)
- **Platforms:** "Apple Silicon Macs, x64/ARM64 Windows PCs, and x64 Linux PCs." Headless "llmster". iPhone/iPad via the Locally app (first LM Link on iPhone release post dated 2026-06-04). [docs](https://lmstudio.ai/docs/app), [Locally post](https://lmstudio.ai/blog/locally-lm-link)
- **Distributed mode:** Whole-request remote (LM Link, Preview). "load and use models on remote machines as if they were local"; "Chats stay on your local device, while heavy model processing runs on the more powerful remote device." No model splitting. [LM Link](https://lmstudio.ai/link)
- **Auth/encryption:** Links are "end-to-end encrypted networks intended for loading and serving LLMs across devices you own", "made possible in partnership with Tailscale"; "All communication and data transfer between devices is always end-to-end encrypted, thanks to Tailscale." Devices "are not exposed to the public internet, and no ports are opened." Backend sees "your device list, used for discovery and connection". Tailscale's own post: built on tsnet; "they automatically discover each other and establish an end-to-end encrypted connection"; traffic "is never seen, either by Tailscale or LM Studio's backend service." [LM Link docs](https://lmstudio.ai/docs/lmlink), [LM Link](https://lmstudio.ai/link), [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access). Local server: "By default, the LM Studio API server does not require authentication"; token auth can be enabled in server settings. [REST quickstart](https://lmstudio.ai/docs/developer/rest/quickstart)
- **Discovery/pairing UX:** Requires an LM Studio account (`lms login`, then `lms link enable`; **CLI pages seen only as search snippets, unverified**). Access "rolling out in batches" via a "Create your Link" form; "Free during Preview", with free and paid plans at GA. Per-device removal/revocation: not documented on any page read; the only documented control is disabling the current device (**unverified**, snippet). [LM Link](https://lmstudio.ai/link), [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access)
- **Community signals:** Bug tracker shows 2,018 open issues. Discord linked (member count not shown). [bug tracker](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues), [docs](https://lmstudio.ai/docs/app)
- **Recurring complaints:** model loading/downloads ("believes partial download is complete after restart"), Metal/CUDA init failures, CUDA regressions on eGPU, "LM Link: peers show online but stay 'disconnected', remote models never appear", bundled Node.js EOL CVE, Linux headless pinned issue (#218), Windows-specific bugs. [bug tracker](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues)

### 2.4 llama.cpp (llama-server and the RPC backend)

- **Positioning:** "LLM inference in C/C++". [README](https://github.com/ggml-org/llama.cpp)
- **License:** MIT. [README](https://github.com/ggml-org/llama.cpp)
- **Platforms/backends:** CPU (ARM NEON/Accelerate, AVX/AVX2/AVX512/AMX, RISC-V), Metal, CUDA, HIP, Vulkan, SYCL, OpenCL, MUSA, CANN, WebGPU, Hexagon, zDNN, VirtGPU, ZenDNN, RPC. Direct HF download: `llama cli -hf ...`. [README](https://github.com/ggml-org/llama.cpp)
- **Distributed mode:** Genuine partitioning via RPC: "distributes model weights and the KV cache across all available devices -- both local and remote -- in proportion to each device's available memory", `--tensor-split` to override; RDMA over Thunderbolt 5 (macOS 26.2+) and RoCEv2 (Linux). Self-described "proof of concept", "fragile and insecure". [rpc README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- **Auth/encryption (RPC):** None. "Never run the RPC server on an open network or in a sensitive environment!" [rpc README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- **Auth/encryption (llama-server):** `--host` defaults to `127.0.0.1`; `--api-key` / `--api-key-file` (default: none); TLS via `--ssl-key-file`/`--ssl-cert-file` with `-DLLAMA_OPENSSL=ON`; default CORS reflects any Origin with credentials; `--tools`/`--agent`/MCP flagged "do not enable in untrusted environments"; public deployments told to set an API key and use a reverse proxy. OpenAI-compatible chat/responses/embeddings routes plus Anthropic Messages. [server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- **Discovery/pairing UX:** Manual `--rpc host:port,host:port`. [rpc README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- **Community signals:** 132.8k stars, 24.9k forks. No Discord listed; GitHub Discussions. [README](https://github.com/ggml-org/llama.cpp)
- **Recurring complaints (RPC-related open issues):** memory-safety crashes ("heap OOB write via op_params/ne mismatch in 6 ops (pre-auth validation bypass)", "oversized ne aborts ggml-rpc-server"), "cache files truncated on disk-full are later served as valid cache hits → silent weight corruption / garbage output", output degeneration with two workers after long prompts, half-open connections on SIGTERM, 25-30% speculative-decode regression over RPC. [RPC issues](https://github.com/ggml-org/llama.cpp/issues?q=is%3Aissue+is%3Aopen+rpc)

### 2.5 Petals

- **Positioning:** "Run LLMs at home, BitTorrent-style." "You load a small part of the model, then join a network of people serving the other parts." [README](https://github.com/bigscience-workshop/petals)
- **License:** MIT. [README](https://github.com/bigscience-workshop/petals)
- **Platforms:** Linux/Anaconda (NVIDIA), Windows via WSL, Docker, macOS M1/M2, AMD via wiki. [README](https://github.com/bigscience-workshop/petals)
- **Distributed mode:** Genuine partitioning across a public volunteer swarm (or a private swarm). [README](https://github.com/bigscience-workshop/petals)
- **Auth/encryption:** Transport is "standard TCP and QUIC communication via the libp2p framework"; no encryption or authentication described. Privacy posture is the opposite of UCompute's: "Your data will be processed with the help of other people in the public swarm"; peers "serving model layers" could "recover input data and model outputs" and "modify the outputs in a malicious way"; "please do not use the public swarm for processing sensitive data"; "Petals lets other peers know your IP address." [README](https://github.com/bigscience-workshop/petals), [security wiki](https://github.com/bigscience-workshop/petals/wiki/Security,-privacy,-and-AI-safety)
- **Discovery/pairing:** DHT-based public swarm; private swarm via wiki guide. [README](https://github.com/bigscience-workshop/petals)
- **Community signals:** 10.7k stars, 650 forks, 94 open issues, 522 commits; Discord linked. [README](https://github.com/bigscience-workshop/petals)
- **Status:** health.petals.dev refused connection on 2026-10-30; chat.petals.dev loads but lists one model (Stable Beluga 2, 70B) and reports "We're out of capacity". Effectively dormant; **maintenance status unverified**. [chat.petals.dev](https://chat.petals.dev)

### 2.6 prima.cpp

- **Positioning:** "[Official] Prima.cpp: Scale Your Local AI Beyond One Device." "a distributed implementation of llama.cpp" for 30-70B models on home clusters; ICLR 2026 paper. [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp), [arXiv](https://arxiv.org/html/2504.08791v1)
- **Repo status:** The original https://github.com/Lizonghang/prima.cpp returns 404 as of 2026-10-30. A third-party index shows it at 997 stars with "Last Commit: 1 year ago" and license "not explicitly stated in the README" (**secondary**). The repo now labelled official is OpenCPIL/prima.cpp: MIT, 125 stars, 21 forks, 2 open issues, version 1.0.2 Docker image. The account-block explanation for the move came from an anonymous forum comment (**unverified**). [SourcePulse](https://www.sourcepulse.org/projects/2358052), [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp)
- **Platforms:** "Currently, prima.cpp can run on Linux, macOS, Android and HarmonyOS (via Termux)." Windows planned. "Now prima.cpp supports only CUDA-based GPUs." [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp)
- **Distributed mode:** Genuine partitioning (piped-ring parallelism; layer windows assigned by the Halda scheduler). [arXiv](https://arxiv.org/html/2504.08791v1)
- **Auth/encryption:** Not mentioned anywhere read; README's networking advice is to disable firewalls or change ports. [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp)
- **Discovery/pairing UX:** Fully manual ring: `--world 4 --rank 0 --master 192.168.1.2 --next 192.168.1.3`; ports 9000/10000. No discovery. [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp)
- **API:** `llama-server` with `/v1/chat/completions` and `/v1/cancel`; clients use `http://localhost:8080/v1`. [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp)
- **Community:** No Discord/forum listed. [OpenCPIL README](https://github.com/OpenCPIL/prima.cpp)

### 2.7 distributed-llama (b4rtaz)

- **Positioning:** "Connect home devices into a powerful cluster to accelerate LLM inference." "tensor parallelism and high-speed synchronization over Ethernet." [README](https://github.com/b4rtaz/distributed-llama)
- **License:** MIT. [README](https://github.com/b4rtaz/distributed-llama)
- **Platforms:** "Supports Linux, macOS, and Windows. Optimized for ARM and x86_64 AVX2 CPUs." Raspberry Pi guide; Vulkan experimental. [README](https://github.com/b4rtaz/distributed-llama)
- **Distributed mode:** Genuine partitioning (tensor parallel). "You can run Distributed Llama only on 1, 2, 4... 2^n nodes"; max nodes = KV heads. Only q40/q80 or f32. [README](https://github.com/b4rtaz/distributed-llama)
- **Auth/encryption:** Not mentioned. [README](https://github.com/b4rtaz/distributed-llama)
- **Discovery/pairing UX:** Manual `--workers ip:port ...`. [README](https://github.com/b4rtaz/distributed-llama)
- **API:** `dllama-api` exists; OpenAI compatibility not stated on the README and the API doc URL 404'd (**unverified**). [README](https://github.com/b4rtaz/distributed-llama)
- **Community signals:** 3.1k stars, 257 forks, 46 open issues; Discord badge. [README](https://github.com/b4rtaz/distributed-llama), [issues](https://github.com/b4rtaz/distributed-llama/issues)
- **Recurring complaints:** GPU support (AMD, CUDA, "GPU slower than CPU"), model conversion/tokenizer failures, new-model requests (Gemma 4, Qwen3-Coder), MoE on 8 nodes, multiple workers per machine. [issues](https://github.com/b4rtaz/distributed-llama/issues)

### 2.8 LocalAI (P2P / federated)

- **Positioning:** "LocalAI is the open-source AI engine." "Drop-in API compatibility: OpenAI, Anthropic, and ElevenLabs APIs across every backend." [README](https://github.com/mudler/LocalAI)
- **License:** MIT. [README](https://github.com/mudler/LocalAI)
- **Platforms:** Docker images (CPU, CUDA 12/13, ROCm, oneAPI, Vulkan, Jetson); macOS DMG; launcher for macOS and Linux. Latest release shown: 4.11.0 (October 2026). [README](https://github.com/mudler/LocalAI)
- **Distributed mode:** Both. "Worker mode" shards weights across llama.cpp RPC workers ("proportional to the memory", built on llama.cpp PR #6829). "Federated mode" load-balances requests across full nodes. Feature is "experimental"/"tech preview quality"; "Only a single model is supported currently"; workers cannot be added after inference starts. [distribute docs](https://localai.io/docs/features/distribute/)
- **Auth/encryption:** go-libp2p via EdgeVPN; a shared token ("`--p2p` generates a shared token") is the only access control; page says the token keeps communication "secure and private" but documents no cipher or key pinning; the public Explorer lists swarm tokens, and anyone with a token can join. [distribute docs](https://localai.io/docs/features/distribute/). Server side: "API key auth, user quotas, role-based access"; an August 2026 note mentions deny-by-default auth. [README](https://github.com/mudler/LocalAI)
- **Discovery/pairing UX:** DHT by default; `LOCALAI_P2P_DISABLE_DHT=true` for mDNS local-only. [distribute docs](https://localai.io/docs/features/distribute/)
- **Community signals:** 50.1k stars, 4.6k forks, 104 open issues; Discord. [README](https://github.com/mudler/LocalAI), [issues](https://github.com/mudler/LocalAI/issues)
- **Recurring complaints:** API behaviour (reasoning field, Open Responses, MCP), backend install/load failures, gallery template/404 problems, container permissions. None of the 25 visible open issues concern P2P/federated, which suggests low usage of that mode rather than its robustness (**inference, not verified**). [issues](https://github.com/mudler/LocalAI/issues)

### 2.9 Jan (menloresearch/jan)

- **Positioning:** "Jan is an open source alternative to ChatGPT that runs 100% offline on your computer." "Privacy First: Everything runs locally when you want it to." [README](https://github.com/menloresearch/jan)
- **License:** Apache-2.0. [README](https://github.com/menloresearch/jan)
- **Platforms:** Windows 10+ (NVIDIA/AMD/Intel Arc), macOS 13.6+, Linux (.deb, AppImage). Bundled llama.cpp. [README](https://github.com/menloresearch/jan)
- **Distributed mode:** None. Connects to cloud providers (OpenAI, Anthropic, Mistral, Groq...). An open idea issue asks for "Jan server and client in local network". [README](https://github.com/menloresearch/jan), [issues](https://github.com/menloresearch/jan/issues)
- **Auth/encryption (local server):** Host `127.0.0.1`, port 1337, OpenAI-compatible `/v1`. API key optional: "Leave the field empty to disable authentication (not recommended when binding to `0.0.0.0`)." Trusted Hosts list; CORS on by default. [api-server docs](https://docs.jan.ai/desktop/api-server)
- **Community signals:** 45.2k stars, 3.1k forks, 399 open issues; Discord "where the community lives". [README](https://github.com/menloresearch/jan), [issues](https://github.com/menloresearch/jan/issues)
- **Recurring complaints:** GPU/hardware detection (Pascal crash on every load in 0.8.8, AMD RX 580 Linux startup exit, "Will run on CPU" mislabel on Apple Silicon), local API server UX (port-in-use message, Trusted Hosts edits lost), Linux AppImage issues, Windows installer signing. [issues](https://github.com/menloresearch/jan/issues)

### 2.10 2026 newcomers that pair personal devices

#### NVIDIA PAIR (Personal AI Router)

- **Positioning:** "Router that virtually distributes inference across connected devices in the home." "turns several machines on your local network into one place to send inference requests." [README](https://github.com/NVIDIA/Personal-AI-Router), [overview](https://docs.nvidia.com/local-ai/nvpair)
- **License:** Apache-2.0. [README](https://github.com/NVIDIA/Personal-AI-Router)
- **Platforms:** Windows 11, Linux (.deb), macOS; x64 and arm64; Windows on ARM "experimental". Entry machine "does not need a GPU or an engine of its own." Engines: Ollama, LM Studio, llama.cpp ("PAIR installs and starts Ollama, LM Studio, or llama.cpp for you"). [README](https://github.com/NVIDIA/Personal-AI-Router), [getting started](https://docs.nvidia.com/local-ai/nvpair/getting-started/)
- **Distributed mode:** Whole-request remote, stated emphatically: "PAIR routes each independent request to one node." It "does **not** pool GPU memory, combine GPUs into a larger logical GPU, shard one model across machines, or split an in-flight inference request between nodes." Routing by "engine availability, model availability, and current workload". [README](https://github.com/NVIDIA/Personal-AI-Router)
- **Auth/encryption:** Six-digit PIN bootstrap, then certificates: "node-to-node traffic runs over mutual TLS restricted to nodes in the cluster"; "Discovery is deliberately not a trust decision." Caveats in their own words: "The PIN is a temporary bootstrap code, not a durable high-entropy credential"; "Cluster mTLS protects participating cluster channels only when identity and certificate material are present"; it "does not automatically protect loopback HTTP, plain discovery metadata, node-information HTTP, Electron IPC, third-party engine APIs"; local broker "has no per-message bearer token". Proxy "serves plaintext HTTP to loopback only". Logging: "Prompts, messages, chunks, and response bodies should not be written to logs" (a prohibition, not an audit feature). Revocation: no procedure documented, only "remove members that are no longer authorized". [overview](https://docs.nvidia.com/local-ai/nvpair), [getting started](https://docs.nvidia.com/local-ai/nvpair/getting-started/), [SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md)
- **Discovery/pairing UX:** mDNS on 5353/udp, fallback "add the system by IP address"; invite + PIN modal; ports 14318-14323. [getting started](https://docs.nvidia.com/local-ai/nvpair/getting-started/)
- **API:** "local proxy endpoints for Ollama-compatible, OpenAI-compatible, and Anthropic Messages API requests." [README](https://github.com/NVIDIA/Personal-AI-Router)
- **Community signals:** 1.7k stars, 287 forks, 41 open issues, 51 open PRs. No Discord; GitHub Discussions, NVIDIA developer forum. Release date not on pages read; a search snippet says open-sourced 2026-09-03 (**unverified**). [README](https://github.com/NVIDIA/Personal-AI-Router)

#### Mesh LLM (Mesh-LLM/mesh-llm, built on iroh)

- **Positioning:** "Distributed AI/LLM for the people. Share compute privately or publicly to power your agents and chat." [README](https://github.com/Mesh-LLM/mesh-llm)
- **License:** Apache-2.0. [README](https://github.com/Mesh-LLM/mesh-llm)
- **Platforms:** macOS (Metal), Linux and Windows (CPU, CUDA, ROCm, Vulkan). ~18 MB binary; mobile app "coming" (iroh post, 2026-07-11). [README](https://github.com/Mesh-LLM/mesh-llm), [iroh blog](https://www.iroh.computer/blog/mesh-llm)
- **Distributed mode:** Both. Default is routing: "If one node can host the full model, it serves the model locally without stage traffic." Split mode: "The coordinator plans contiguous layer ranges" across nodes. [README](https://github.com/Mesh-LLM/mesh-llm)
- **Auth/encryption:** "QUIC end-to-end encrypts traffic between Mesh nodes"; each iroh endpoint "is the node's identity, a public key, and its only network surface"; relays "forward encrypted packets without reading their payload"; two project-run relays for NAT fallback. Private meshes are "invite-token based"; revocation/rotation not documented on pages read (docs/MESHES.md 404'd; **unverified**). Public mesh privacy toward the serving node is not addressed. "Mesh LLM is experimental distributed-systems software." [README](https://github.com/Mesh-LLM/mesh-llm), [iroh blog](https://www.iroh.computer/blog/mesh-llm)
- **Discovery/pairing UX:** `mesh-llm serve --auto` joins "the best discovered public mesh" (Nostr discovery); private: `--join <token>`. API on `http://localhost:9337/v1`, loopback by default (`--listen-all` to change). [README](https://github.com/Mesh-LLM/mesh-llm)
- **Community signals:** 3.7k stars, 476 forks, 117 open issues; latest stable v0.75.1, prerelease v0.76.0-rc8. No Discord link. [README](https://github.com/Mesh-LLM/mesh-llm)

---

## 3. Comparison matrix

| Project | License | Platforms (shipped) | Distributed mode | Device auth / encryption documented | Pairing UX | Stars (2026-10-30) |
|---|---|---|---|---|---|---|
| exo | Apache-2.0 | macOS app (Apple Silicon); Linux CPU source | Genuine partitioning | None; API "unauthorized" by design | Auto-discovery, no pairing | 48.1k |
| Ollama | MIT | macOS, Win, Linux, Docker | None (cloud models instead) | Local API no auth; 127.0.0.1 default | n/a | 185.3k |
| LM Studio / LM Link | Proprietary | macOS, Win, Linux; iOS via Locally | Whole-request remote (Preview) | E2E encrypted via Tailscale; account-based | Account sign-in, batches | n/a (bug tracker: 2,018 open) |
| llama.cpp RPC | MIT | Any backend | Genuine partitioning | None; "fragile and insecure" | Manual host:port | 132.8k |
| Petals | MIT | Linux, WSL, Docker, macOS | Genuine partitioning (public swarm) | None; peers can read data | DHT swarm | 10.7k |
| prima.cpp | MIT (OpenCPIL) | Linux, macOS, Android, HarmonyOS; CUDA only | Genuine partitioning | None mentioned | Manual ring (--master/--next) | 125 (official), 997 (old, stale) |
| distributed-llama | MIT | Linux, macOS, Win; CPU-first | Genuine partitioning (2^n nodes) | None mentioned | Manual ip:port | 3.1k |
| LocalAI P2P | MIT | Docker, macOS DMG | Both (worker shard / federated route) | Shared token via libp2p/EdgeVPN; cipher undocumented | Token; DHT or mDNS | 50.1k |
| Jan | Apache-2.0 | Win, macOS, Linux | None | Optional API key; 127.0.0.1 default | n/a | 45.2k |
| NVIDIA PAIR | Apache-2.0 | Win 11, Linux, macOS installers | Whole-request remote | PIN then mTLS; PIN "low entropy" by own admission | mDNS + PIN invite | 1.7k |
| Mesh LLM | Apache-2.0 | macOS, Linux, Win | Both (route default / split) | iroh QUIC E2E; invite tokens | `--auto` public or `--join token` | 3.7k |
| **UCompute (dev build)** | Apache-2.0 | none shipped; macOS AS alpha, Win 11 + Linux CPU demonstrated | Whole-request remote | QUIC + TLS 1.3, keys pinned at pairing | Short code; address fallback | repo holds only LICENSE |

---

## 4. UCompute properties: differentiated or table stakes?

Judged only against what the pages above document. "Differentiated" means no competitor read documents it; "parity" means the 2026 routers document an equivalent; "table stakes" means most of the field has it.

| UCompute property | Verdict | Evidence |
|---|---|---|
| OpenAI-client compatibility (change base URL) | **Table stakes** | Ollama, llama-server, LM Studio, Jan, LocalAI, exo, PAIR, Mesh LLM, prima.cpp all expose `/v1`. Ollama even documents "required but ignored" API key. [Ollama](https://docs.ollama.com/api/openai-compatibility), [llama-server](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), [PAIR](https://github.com/NVIDIA/Personal-AI-Router), [Mesh LLM](https://github.com/Mesh-LLM/mesh-llm) |
| Streaming, cancellation | **Table stakes** | Universal; prima.cpp even exposes `/v1/cancel`. [prima.cpp](https://github.com/OpenCPIL/prima.cpp) |
| Loopback-only local API by default | **Table stakes** | Ollama 127.0.0.1, llama-server 127.0.0.1, Jan 127.0.0.1, LM Studio localhost:1234, Mesh LLM loopback, PAIR plaintext "to loopback only". [Ollama FAQ](https://docs.ollama.com/faq), [Jan](https://docs.jan.ai/desktop/api-server), [PAIR](https://docs.nvidia.com/local-ai/nvpair/getting-started/) |
| Memory-fit check before load | **Table stakes, with a quality opening** | Ollama has memory estimation (issue: "3-4x actual VRAM, causing needless evictions"); LM Studio has "AutoFit ... guardrails" (issue: "loads context larger than VRAM ... ignores guardrails"); exo has an `allowMemoryOverride` toggle. Everyone has it; several have it wrong. [Ollama issues](https://github.com/ollama/ollama/issues), [LM Studio tracker](https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues), [exo issues](https://github.com/exo-explore/exo/issues) |
| SHA-256 verified downloads with license shown | **Likely table stakes technically, under-communicated by everyone** | No page read advertises hash verification or license display to the user. Registry-based pulls (Ollama, HF) are content-addressed in practice but that was not verified on the pages read (**unverified**). The llama.cpp RPC cache-corruption issue shows the failure mode is real. [RPC issues](https://github.com/ggml-org/llama.cpp/issues?q=is%3Aissue+is%3Aopen+rpc) |
| Whole request runs on one device (no pooling) | **Parity with 2026 routers; differentiated vs. partitioners** | PAIR says it in bold; LM Link and Mesh LLM default routing do the same. This is a category now, not a position. [PAIR](https://github.com/NVIDIA/Personal-AI-Router), [LM Link](https://lmstudio.ai/link), [Mesh LLM](https://github.com/Mesh-LLM/mesh-llm) |
| Authenticated pairing, device keys pinned, TLS 1.3 over QUIC | **Differentiated vs. exo / llama.cpp RPC / distributed-llama / prima.cpp / Petals; parity vs. PAIR (mTLS), LM Link (Tailscale), Mesh LLM (iroh QUIC)** | The partitioners document nothing; exo's maintainer: "exo's api is unauthorized". Among routers, the nuance is control-plane dependence: LM Link needs an LM Studio account and sends the device list to its backend; Mesh LLM's public mode uses project-run relays; PAIR's PIN is "not a strong authenticator" by its own doc. A short-code pairing with no account and no vendor server is a defensible sub-position, if it can be said without implying the others are insecure. [exo #1833](https://github.com/exo-explore/exo/issues/1833), [LM Link](https://lmstudio.ai/link), [PAIR overview](https://docs.nvidia.com/local-ai/nvpair), [Mesh LLM](https://github.com/Mesh-LLM/mesh-llm) |
| One-step revocation of a device | **Differentiated (narrowly)** | PAIR's SECURITY.md has no revocation procedure ("remove members that are no longer authorized" only). LM Link documents only disabling the current device (**unverified**, snippet). Mesh LLM token rotation undocumented (**unverified**). Nobody read documents a per-device revoke. The "<0.1 s" figure is a dev-build measurement on specific hardware; usable as a design goal, not a benchmark claim. [PAIR SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md) |
| Default local-only policy (refuse all off-device requests until opted in) | **Differentiated as a policy default** | Others default to loopback binding (table stakes) but, once paired, route automatically: PAIR by workload, exo by auto-cluster, LocalAI federated by load-balance. An explicit "nothing leaves this device until you say so, per device" default is a stance none of the pages read describes. Closest analogue: PAIR's "Discovery is deliberately not a trust decision." [PAIR README](https://github.com/NVIDIA/Personal-AI-Router), [exo](https://github.com/exo-explore/exo), [LocalAI](https://localai.io/docs/features/distribute/) |
| Audit log of off-device requests without prompt text | **Differentiated** | No competitor read documents an audit log. PAIR has the inverse statement (prompts "should not be written to logs") but no audit feature. Niche appeal; strongest with privacy-conscious developers and anyone who has read the Censys or Petals pages. [PAIR SECURITY.md](https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md), [Petals wiki](https://github.com/bigscience-workshop/petals/wiki/Security,-privacy,-and-AI-safety) |
| Pinned llama.cpp engine build (b11609) | **Neutral** | Ollama, LM Studio, Jan, LocalAI all embed llama.cpp; pinning is normal engineering, not positioning. |

### Where competitors are ahead (do not contest these)

- **Pooling / partitioning:** exo (tensor parallel, RDMA over TB5), llama.cpp RPC, Mesh LLM split mode, distributed-llama, prima.cpp, LocalAI worker mode. UCompute has design only. [exo](https://github.com/exo-explore/exo), [rpc README](https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md), [Mesh LLM](https://github.com/Mesh-LLM/mesh-llm)
- **Model range and modality:** Ollama's library and audio endpoints; LM Studio's MLX + GGUF; LocalAI's vision/voice/image/video. UCompute: small GGUF only. [Ollama compat](https://docs.ollama.com/api/openai-compatibility), [LocalAI](https://github.com/mudler/LocalAI)
- **Platforms and installers:** PAIR ships Win/Linux/macOS; Ollama/LM Studio/Jan ship all three; LM Studio ships iOS. UCompute: no public build. [PAIR getting started](https://docs.nvidia.com/local-ai/nvpair/getting-started/), [Jan](https://github.com/menloresearch/jan), [Locally](https://lmstudio.ai/blog/locally-lm-link)
- **Off-LAN access / NAT traversal:** LM Link (Tailscale), Mesh LLM (iroh relays). UCompute: LAN-only, no relay. [Tailscale](https://tailscale.com/blog/lm-link-remote-llm-access), [iroh blog](https://www.iroh.computer/blog/mesh-llm)
- **Maturity and community:** star counts above; every mature project has a Discord. UCompute has none.
- **Tool calling:** llama-server, Ollama, LM Studio document it; UCompute has not verified it.

---

## 5. Implications for positioning (evidence-backed, not aspirational)

1. **Do not lead with "runs the whole request on one device".** NVIDIA owns that sentence now, with installers. Lead instead with the three things no router documents: per-device revoke, default-deny off-device policy, prompt-free audit. These are small, concrete, and verifiable in a demo.
2. **The honest comparison target is PAIR, not exo.** Same license, same non-pooling model, same LAN scope. PAIR's own SECURITY.md lists what its mTLS does not protect and calls its PIN low-entropy; UCompute can describe its own trust model with the same candour and let readers compare. Never claim PAIR is insecure; its doc is more candid than most.
3. **exo is the wrong enemy and the right cautionary tale.** It has 48.1k stars and real partitioning. Its maintainers chose an unauthenticated API by design and the issue tracker shows discovery pain on plain LANs. UCompute's address-fallback pairing and pinned keys speak directly to the "Two Ubuntu nodes on the same LAN fail to discover each other" and "exo's api is unauthorized" threads, without naming anyone.
4. **The Censys number is the best third-party argument for default-deny**, and it is about Ollama, the most popular tool in the space. Cite it as a category problem, not as an attack on Ollama.
5. **Hash verification and memory-fit are not differentiators; reliability of them might be.** Ollama's and LM Studio's trackers show both features misfiring. Only claim this once there is public evidence UCompute's versions hold up on more than two machines.
6. **Everything above is gated on shipping.** Every competitor profiled has a downloadable artifact; UCompute's public repo has a LICENSE. Positioning text written before source is public will be read against that fact.

---

## Sources

Fetched and read directly on 2026-10-30:

1. https://github.com/exo-explore/exo
2. https://github.com/exo-explore/exo/issues
3. https://github.com/exo-explore/exo/issues/1833
4. https://github.com/ollama/ollama
5. https://github.com/ollama/ollama/issues
6. https://docs.ollama.com/api/openai-compatibility
7. https://docs.ollama.com/faq
8. https://docs.ollama.com/api/authentication
9. https://github.com/ggml-org/llama.cpp
10. https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md
11. https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
12. https://github.com/ggml-org/llama.cpp/issues?q=is%3Aissue+is%3Aopen+rpc
13. https://github.com/bigscience-workshop/petals
14. https://github.com/bigscience-workshop/petals/wiki/Security,-privacy,-and-AI-safety
15. https://chat.petals.dev
16. https://health.petals.dev (connection refused on 2026-10-30)
17. https://github.com/Lizonghang/prima.cpp (HTTP 404 on 2026-10-30)
18. https://www.sourcepulse.org/projects/2358052 (third-party index; secondary)
19. https://arxiv.org/html/2504.08791v1
20. https://github.com/OpenCPIL/prima.cpp
21. https://github.com/b4rtaz/distributed-llama
22. https://github.com/b4rtaz/distributed-llama/issues
23. https://github.com/mudler/LocalAI
24. https://github.com/mudler/LocalAI/issues
25. https://localai.io/docs/features/distribute/
26. https://github.com/menloresearch/jan
27. https://github.com/menloresearch/jan/issues
28. https://docs.jan.ai/desktop/api-server
29. https://lmstudio.ai/docs/app
30. https://lmstudio.ai/link
31. https://lmstudio.ai/blog/locally-lm-link
32. https://lmstudio.ai/terms
33. https://lmstudio.ai/docs/developer/rest/quickstart
34. https://lmstudio.ai/docs/lmlink
35. https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues
36. https://tailscale.com/blog/lm-link-remote-llm-access
37. https://github.com/NVIDIA/Personal-AI-Router
38. https://github.com/NVIDIA/Personal-AI-Router/blob/main/SECURITY.md
39. https://docs.nvidia.com/local-ai/nvpair/getting-started/
40. https://docs.nvidia.com/local-ai/nvpair
41. https://github.com/Mesh-LLM/mesh-llm
42. https://www.iroh.computer/blog/mesh-llm
43. https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys
44. https://www.sentinelone.com/vulnerability-database/cve-2026-50759/ (secondary; page states its content is AI-generated)
45. https://www.enterprisesecuritytech.com/post/unauthenticated-rce-in-exo-raises-alarms-about-security-in-open-source-ai-infrastructure (secondary)

Seen only as search-result snippets, not read (claims from these are marked unverified above): lmstudio.ai/docs/cli/link/link-disable, lmstudio.ai/docs/cli/link/link-enable, github.com/advisories/ghsa-qr8q-72gc-wm4f, github.com/exo-explore/ex-exo, huggingface.co/papers/2504.08791 (forum comment on repo move), third-party PAIR and Mesh LLM blog coverage.

Not reachable: github.com/Mesh-LLM/mesh-llm/blob/main/docs/MESHES.md (404), github.com/b4rtaz/distributed-llama/blob/main/docs/API.md (404), explorer.localai.io (HTTP 521), nvd.nist.gov detail page for CVE-2026-50759 (returned home page).
