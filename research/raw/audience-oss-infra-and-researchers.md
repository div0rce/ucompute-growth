# Audience research: open-source infrastructure enthusiasts and distributed/edge-inference researchers

Lens: `audience-oss-infra-and-researchers`
Date of research: 2026-10-30
Status of UCompute at time of writing (from brief, not independently verified): Apache-2.0 project, source not yet published (public repo holds only a LICENSE), no public release, private alpha on macOS Apple Silicon for an owner-managed cohort. UCompute Mesh routes a WHOLE request to ONE device; it does NOT partition or pool models.

Conventions used in this report:
- Every factual claim carries a URL that was actually read (WebFetch) unless marked **[search-only]** (seen only in a search-result snippet) or **[unverified]** (could not be confirmed from a primary page).
- Numbers quoted from GitHub pages (stars, issues) are as rendered on 2026-10-30 and drift daily.
- Nothing here is a statistic I invented; where a source gave no number, I say so.

---

## 1. Executive summary

1. **This audience is small, technical, and already skeptical of "run AI across your devices" claims.** The exo launch thread on Hacker News (July 2024, ~439 points, 151 comments) asked, on day one, for tokens/sec benchmarks, a security model, and a LICENSE file, and multiple commenters argued that shipping activations over a home network would be memory-bandwidth-bound and slow (https://news.ycombinator.com/item?id=40973339). Two years later the same objections recur in the Ollama distributed-inference thread, where one user measured gpt-oss:120b dropping from 42.2 to 34.1 tok/s when split across two DGX Sparks on a 200 Gb/s link (https://github.com/ollama/ollama/issues/4643).

2. **The 2025-2026 consensus among honest practitioners is that distribution adds capacity, not single-request speed, unless you have RDMA-class interconnect.** Apple's own MLX research post (15 Oct 2026) says pipeline parallelism "does not speed up decode" and that tensor parallelism "depends on very low-latency interconnect" (https://machinelearning.apple.com/research/mlx-distributed-inference). An independent MLX tool documented a 0.8B model running 2.7x *slower* when sharded across two Macs (https://mlx-optiq.com/docs/cluster). Jeff Geerling's four-Mac-Studio RDMA cluster post concluded he "cannot justify the cost" for most home users (https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/). **UCompute's decision not to partition is defensible to this audience if it is stated as a measured engineering position rather than a gap.**

3. **Security of home-LAN inference daemons is the live, under-served conversation, and it is exactly where UCompute's verified design sits.** llama.cpp's RPC README calls the feature "fragile and insecure" and says "Never run the RPC server on an open network" (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md); its SECURITY.md says "Do not use the RPC backend" in untrusted environments (https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md); a Critical CVSS 9.8 unauthenticated RCE in the RPC backend (CVE-2026-34159) was published 26 March 2026 with no patched version listed (https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw). Cisco Talos found 1,139 unauthenticated Ollama servers via Shodan (Sep 2025) (https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama) and LeakIX found 12,269 (Feb 2026) (https://blog.leakix.net/2026/02/ollama-exposed/). Authenticated transport with pinned device keys, local-only-by-default, sub-0.1 s revocation, and audit logs without prompt text are precisely the properties these sources say are missing.

4. **The research frontier (2025-2026) has moved to (a) heterogeneity-aware scheduling and (b) integrity/privacy against untrusted peers.** prima.cpp (ICLR 2026) frames scheduling as an ILP over CPU/GPU/disk/OS heterogeneity (https://arxiv.org/abs/2504.08791, https://mlanthology.org/iclr/2026/li2026iclr-prima/); Parallax (Sep 2025) does two-phase scheduling over volunteer GPUs (https://arxiv.org/abs/2509.26182); a July 2026 paper proposes canary inputs to detect tampering nodes in layer-split pipelines (https://arxiv.org/abs/2607.19490); a Feb 2026 paper quantifies token-recovery from leaked activations in split inference (~59% at a 2-layer split) (https://arxiv.org/abs/2602.16760). UCompute avoids both problem classes by design (no activations leave a device; no untrusted peers), and should say so explicitly.

5. **Distribution channels that reach this audience at $0:** arXiv cs.DC/cs.CR (36 new cs.DC submissions on 30 Oct 2026 alone, several on LLM serving: https://arxiv.org/list/cs.DC/recent); Hacker News with its Show HN rules (must be something people can try; no soliciting upvotes: https://news.ycombinator.com/showhn.html); project Discords (exo, Petals, distributed-llama links verified in their READMEs); EleutherAI's community (200+ monthly active members, 150+ community researchers: https://www.eleuther.ai/community/); newsletters that pick up technical reports with primary links, notably Import AI (https://jack-clark.net/2025/04/21/import-ai-409-...) and Latent Space's AI News, which reads r/LocalLLaMA daily and tracks ~544 X accounts (https://latent.space/p/ainews-top-local-models-list-april/).

6. **Timing constraint:** nothing in this audience's channels works before source is published. Show HN requires something runnable. The exo HN thread shows an unlicensed/unpublished project is immediately challenged. UCompute already has a LICENSE but no code; a "technical report first, code on release day" sequence is the only path that does not burn credibility.

---

## 2. The landscape this audience tracks (verified facts, project by project)

### 2.1 exo (exo labs)
- README: "Run frontier AI locally." Automatic discovery; topology-aware pipeline or tensor parallelism; claims up to 1.8x speedup on 2 devices and 3.2x on 4; OpenAI Chat Completions, Claude Messages, OpenAI Responses and Ollama-compatible endpoints; MLX backend; macOS Apple Silicon GPU, Linux CPU-only (GPU "under development"); day-0 RDMA over Thunderbolt 5 requiring macOS 26.2 and `rdma_ctl enable` from Recovery; all devices must run the same exo version; `trust_remote_code` disabled by default. ~48.1k stars, 208 open issues, 225 open PRs as rendered. Discord `discord.gg/TJ4P57arEm`, X `@exolabs`. (https://github.com/exo-explore/exo)
- License is Apache-2.0, "Copyright 2025 Exo Technologies Ltd" (https://github.com/exo-explore/exo/blob/main/LICENSE). Note: a vendor comparison lists exo as GPL-3.0; that is wrong per the LICENSE file (https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html). This audience catches such errors.
- Launch reception on HN (16 Jul 2024, ~439 points, 151 comments): objections were platform support (MLX-only at launch), per-hop latency ("50 nodes at 40 ms each would take about 2 seconds per token"), memory-bandwidth bound, "two MacBook Pros ran at the same speed as one," no security section in README (maintainer: assumes trusted LAN), no LICENSE (maintainer added one). Praise: clear explanation that activation size, not parameter count, sets network traffic; maintainer responsiveness. Questions: comparison to Petals, training support, Raspberry Pi, crowdsourced clusters. (https://news.ycombinator.com/item?id=40973339)
- Independent field test (Jeff Geerling, 18 Dec 2025): four M3 Ultra Mac Studios, 1.5 TB unified memory, "just shy of $40,000"; exo 1.0 was the only tool with RDMA; Qwen3 235B ~32 tok/s on the full cluster; Kimi K2 Thinking ~30 tok/s; HPL over Thunderbolt TCP crashed and rebooted two Macs; exo "sometimes failed to load models"; llama.cpp RPC "scales but is inefficient, so its performance drops as nodes are added"; author notes the exo developers "went silent for a period"; verdict: "cannot justify the cost," cluster management "painful." (https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/)

### 2.2 prima.cpp (OpenCPIL / Zonghang Li et al.)
- arXiv 2504.08791, v1 7 Apr 2025, v2 26 Sep 2025, v3 4 Jul 2026. Pipelined-ring parallelism (PRP) overlapping disk I/O with compute and communication; Halda, a heterogeneity-aware scheduler. Claims: 70B at 674 ms/token TPOT on four consumer devices with <6% memory pressure; 32B with speculative decoding at 26 tok/s; 5-17x lower TPOT than llama.cpp, exo and dllama. Authors: Zonghang Li, Tao Li, Wenjiao Feng, Rongxing Xiao, Jianshu She, Hong Huang, Mohsen Guizani, Hongfang Yu, Qirong Ho, Wei Xiang, Xue Liu. Code: github.com/OpenCPIL/prima.cpp. (https://arxiv.org/abs/2504.08791)
- Accepted at ICLR 2026 (https://mlanthology.org/iclr/2026/li2026iclr-prima/). Affiliation: lead author at MBZUAI, co-authors at UESTC, City University of Hong Kong, La Trobe **[search-only]**.
- Official repo: distributed implementation of llama.cpp; macOS, Linux, Android and HarmonyOS via Termux; CUDA only (no Vulkan/AMD); no Windows yet; README claims "15x faster" than llama.cpp in its tests; QwQ-32B ~11 tok/s, Llama-3-70B ~1.5 tok/s on author hardware; MIT; 125 stars, 21 forks, 2 open issues as rendered; no Discord listed. (https://github.com/OpenCPIL/prima.cpp). Earlier repos existed under Gitee `zonghang-li` and GitHub `Lizonghang`; whether they hold a larger star count is **[unverified]**.
- The paper's own HTML cites llama.cpp, exo, distributed-llama, MLC-LLM, kTransformers, AirLLM and PocketPal AI as related work (https://arxiv.org/html/2504.08791, reached via https://huggingface.co/papers/2504.08791 which redirected and showed no upvote count).
- No Hacker News thread for prima.cpp surfaced in search **[unverified]**. Takeaway: an ICLR paper with a 5-17x claim over exo has ~125 stars on its official repo versus exo's ~48k. Academic credibility and adoption are different currencies in this space.

### 2.3 llama.cpp RPC backend (ggml-org)
- README: RPC backend offloads to `ggml-rpc-server` instances over TCP; labelled proof-of-concept, "fragile and insecure"; "Never run the RPC server on an open network or in a sensitive environment!"; no authentication; weights and KV cache split by available memory; RDMA negotiated at handshake (Linux RoCEv2 via libibverbs; macOS Thunderbolt 5 on Apple silicon, macOS 26.2+); no benchmarks in README. (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
- SECURITY.md: "Do not use the RPC backend, ggml-rpc-server and llama-server functionality" in untrusted environments; recommends sandboxing untrusted models and verifying weights against a known-good hash; private disclosure program currently disabled, fixes as public PRs; reports need a working PoC and "cannot be written exclusively by AI." (https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md)
- Advisories page (first page, 10 shown): 3 relate to RPC: GHSA-wcr5-566p-9cwj (write-what-where in `rpc_server::set_tensor`, Critical, Aug 2024), GHSA-5vm9-p64x-gqw9 (arbitrary read in `get_tensor`, Moderate, Aug 2024), GHSA-j8rj-fmpv-wcxw (unauthenticated RCE via GRAPH_COMPUTE buffer=0 bypass, Critical, 26 Mar 2026). (https://github.com/ggml-org/llama.cpp/security/advisories)
- GHSA-j8rj-fmpv-wcxw / CVE-2026-34159: CVSS 3.1 9.8; affects b7991 and earlier; "Patched version: none listed"; root cause shared with CVE-2024-42478/42479 which were patched only in GET_TENSOR/SET_TENSOR handlers; bug dates to the RPC merge in May 2024; reporter las7 says CERT/CC closed the case so it was filed directly. (https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw)
- Exploitation write-up (6 Feb 2025): heap overflow in `ggml_backend_cpu_buffer_cpy_tensor` from attacker-controlled tensor dimensions, chained to RCE via forged buffer/backend structures; author's takeaway: layered checks added after earlier GHSAs did not eliminate risk because a size calculation trusted attacker-controlled dimensions. (https://retr0.blog/blog/llama-rpc-rce)
- **Relevance to UCompute:** UCompute pins llama.cpp b11609 and never exposes an RPC server; a whole request runs on one device over an authenticated QUIC/TLS 1.3 channel. That is a direct answer to the single most-cited security weakness in this ecosystem.

### 2.4 distributed-llama (b4rtaz)
- Tensor parallelism over Ethernet; root node plus 2^n - 1 workers; max nodes equals the model's KV-head count; Linux/macOS/Windows; ARM and x86_64 AVX2; experimental Vulkan; Q40/Q80 or F32 only; MIT; ~3.1k stars, 257 forks, 46 open issues, 417 commits; latest news item 16 Sep 2025 (Qwen 3 MoE on Vulkan); Discord via n4no.com invite; benchmarks live in GitHub Discussions not README. (https://github.com/b4rtaz/distributed-llama)

### 2.5 Petals (BigScience workshop)
- "BitTorrent-style" public swarm; ~6 tok/s Llama 2 70B, ~4 tok/s Falcon 180B single-batch; Llama 3.1 up to 405B, Mixtral 8x22B, Falcon, BLOOM; data "processed by other participants in the public swarm," private swarm recommended for sensitive data; hosting "does not let others run custom code on your computer"; MIT; 522 commits, 94 open issues, 20 open PRs; two Discords (usage: discord.gg/KdThf2bWVU; hosting: discord.gg/X7DgtxgMhc). No deprecation notice shown. (https://github.com/bigscience-workshop/petals)
- health.petals.dev refused the connection on 2026-10-30 (single attempt, `ECONNREFUSED`). A vendor comparison dated 11 Apr 2026 also describes Petals as "in maintenance mode" with a broken network-status widget (https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html). Treat Petals as the reference citation for "public volunteer swarm," not as a live competitor.

### 2.6 MLX distributed (Apple)
- Apple ML Research post, 15 Oct 2026: macOS 26.2 added a low-latency RDMA driver over Thunderbolt 5; MLX v0.30.1+ uses it via the `jaccl` backend launched with `mlx.launch`; measured with `mlx_lm.benchmark` at batch size 1: Qwen 3.8 27B dense BF16 12.46 tok/s on one M3 Ultra, 19.69 on one M5 Ultra, 50.89 on four M5 Ultras (tensor parallel); Mistral Medium 3.5 128B FP8 4.95 / 7.70 / 23.37; an 816B-total MoE at 36.73 tok/s on four M5 Ultras. Caveats stated by Apple: "pipeline parallelism does not speed up decode"; two-machine tensor parallel was slower than two-machine pipeline for a 65k-token prefill; "dense architectures scale better across multiple computers"; results are one configuration, 128-token generation, quantized. (https://machinelearning.apple.com/research/mlx-distributed-inference)
- Independent corroboration: Qwen3.5-0.8B ran 5.0 ms/token on one Mac and 13.4 ms/token across two (2.7x worse); a 42.8 GiB model that did not fit on one Mac decoded at 20.5 tok/s split versus 4.9 tok/s streaming experts from SSD. Recommendation: "Don't shard a model that already fits on one Mac." (https://mlx-optiq.com/docs/cluster)
- Awni Hannun (MLX lead): GitHub `awni`, X `@awnihannun`, org `ml-explore` (https://github.com/awni). Georgi Gerganov (llama.cpp): GitHub `ggerganov`, X `@ggerganov`, 20.9k GitHub followers, employer shown as Hugging Face, org `ggml-org` (https://github.com/ggerganov).

### 2.7 Mesh LLM (Michael Neale / Block) - the closest recent analogue to UCompute Mesh
- README: pools GPUs and memory across machines behind one OpenAI-compatible endpoint at `localhost:9337/v1`; a request runs locally, is routed to a peer with the model loaded, or is split across nodes; "QUIC end-to-end encrypts traffic between Mesh nodes"; iroh relays forward encrypted packets without reading payload; separate control lane for owner configuration; private meshes via invite tokens, public via Nostr discovery; `--local-model-only` mode; self-described as "experimental distributed-systems software"; Apache-2.0; ~3.7k stars, 476 forks; no benchmarks in README; if a model does not fit, startup fails rather than silently falling back to distributed serving. (https://github.com/Mesh-LLM/mesh-llm)
- iroh launch post, 11 Jul 2026: each node's iroh endpoint is its identity and only network surface; three ALPNs (`mesh-llm/1`, `mesh-llm-control/1`, `skippy-stage/2`); 40+ model catalog; ~18 MB install; no benchmarks. (https://www.iroh.computer/blog/mesh-llm)
- Block engineering, 27 Jul 2026 ("Buzz"): "Prompts and data sent to another machine are visible to that machine's owner, so ... Share compute with people you trust"; results from other machines "are not verified"; public mesh is "best-effort, with no guarantees"; distributed inference is "advanced and challenging, with throughput depending heavily on the network." (https://engineering.block.xyz/blog/buzz-sharing-compute-powered-by-meshllm)
- HN reception: reached the front page in July 2026; point counts differ between secondary sources (179 vs 277) **[search-only, unverified]**; main criticism reported was "how slow is network-distributed inference" **[search-only]**.
- **Why this matters for UCompute:** Mesh LLM shows this audience will accept a QUIC-encrypted, OpenAI-compatible, route-whole-request design and will reward honest "experimental" labelling. Its gaps (no benchmarks, trust-your-peers privacy, unverified results) are the exact places UCompute can be more rigorous: measured revocation, pinned keys at pairing, local-only default, audit logs without prompt text.

### 2.8 Parallax (Gradient)
- arXiv 2509.26182, 30 Sep 2025: decentralized serving over volunteer GPUs; two-phase scheduler (model allocation across heterogeneous GPUs under memory and bandwidth constraints; request-time pipeline selection); evaluated on "real volunteer nodes"; code at github.com/GradientHQ/parallax; license not stated on the abstract page. (https://arxiv.org/abs/2509.26182). Vendor-reported 5.3x lower inter-token latency vs Petals **[search-only, unverified]**.

### 2.9 Prime Intellect / Nous Psyche (decentralized training, adjacent audience)
- INTELLECT-2, 11 May 2025: 32B model trained with fully asynchronous RL across a permissionless, heterogeneous pool; PRIME-RL (FSDP2 trainer, vLLM inference); TOPLOC (locality-sensitive hashing to verify inference outputs across different GPU hardware); SHARDCAST (HTTP tree broadcast of weights); invalid rollouts cause nodes to be removed from the pool; model, code and data open-sourced. (https://www.primeintellect.ai/blog/intellect-2-release)
- Import AI 409 (21 Apr 2025) covered the run as a "prediction confirmed," with 18 contributors on the live dashboard at the time, and framed its importance as policy: decentralized compute challenges the assumption that frontier compute must be centralized. The newsletter selects research/technical reports with primary links and milestones that test prior predictions. (https://jack-clark.net/2025/04/21/import-ai-409-huawei-trains-a-model-on-8000-ascend-chips-32b-decentralized-training-run-and-the-era-of-experience-and-superintelligence/)
- Psyche (Nous): "distributed training of transformer-based AI models over the internet" for "untrusted parties"; Apache-2.0; 976 stars, 133 forks; details deferred to docs.psyche.network. (https://github.com/PsycheFoundation/psyche)
- Position paper "Will LLMs Scaling Hit the Wall? Breaking Barriers via Distributed Resources on Massive Edge Devices," arXiv 2503.08223, v1 11 Mar 2025, v3 9 Apr 2026, cs.DC: argues edge devices can break the data and compute concentration barriers; abstract gives no quantitative edge-compute figures. (https://arxiv.org/abs/2503.08223)
- **Caution for UCompute:** this is the sub-community most likely to read "compute-credit economy" as a token play. A critical piece claims INTELLECT-3 was trained on a conventional 512-GPU cluster despite decentralized branding **[search-only, unverified]**. Keep UCompute's credit economy strictly labelled "direction" and never lead with it here.

### 2.10 BOINC-style volunteer computing
- No BOINC project doing LLM inference was found in 2025-2026 searches **[search-only; absence not proven]**. A 2026 paper (WWW.Serve) cites BOINC and Petals as background **[search-only]**. Treat "BOINC for LLMs" as an analogy this audience understands, not as a live competitor set.

### 2.11 Exposure of unauthenticated local LLM servers (the practical security backdrop)
- Cisco Talos, 1 Sep 2025: Shodan-based; 1,139 Ollama instances answering unauthenticated test prompts; 214 (~18.8%) actively serving models; US 36.6%, China 22.5%, Germany 8.9%; recommends API-key/OAuth2 auth with RBAC, network isolation, rate limiting, audit logging; "never expose LLM servers publicly without it." (https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama)
- LeakIX, 23 Feb 2026: 12,269 Ollama instances reachable with no authentication; top hosts AWS 1,686, Hetzner 1,004, OVH 773; ~1,000 on versions vulnerable to CVE-2024-37032 (unauthenticated RCE as root via path traversal); recommends bind to 127.0.0.1, auth proxy, firewall, proxy-side logging because "Ollama does not log requests by default"; argues secure defaults are the maintainers' responsibility. Vendor source, advocacy tone. (https://blog.leakix.net/2026/02/ollama-exposed/)
- **UCompute mapping:** local-only mode that refuses every off-device request by default, pairing with a short code, pinned device keys, and audit logs of off-device requests are the controls both reports ask for.

---

## 3. Where the discussion happens

| Venue | Evidence | What works there |
|---|---|---|
| **arXiv cs.DC / cs.CR / cs.LG** | 36 new cs.DC submissions on 30 Oct 2026; same-day titles include FlatCake (KV-cache storage for LLM serving), PDScope (memory-bound MoE inference), an energy accounting of speculative decoding (https://arxiv.org/list/cs.DC/recent). Key home-cluster papers: 2504.08791 (ICLR 2026), 2509.26182, 2607.19490 (cs.CR), 2602.16760 (cs.CR), 2503.08223. | Short technical reports with code links. Security papers now land in cs.CR, which is where a threat-model write-up would be read. |
| **Hacker News** | exo launch: ~439 pts/151 comments (https://news.ycombinator.com/item?id=40973339). "Local LLM inference - impressive but too hard to work with" (21 Apr 2025): 84 pts/58 comments; commenters valued MLX/GGUF/unified-memory awareness, criticised single-model tests, debated cloud vs local (https://news.ycombinator.com/item?id=43753890). Show HN rules: must be something people can run; no sign-up walls; "Don't ask friends to upvote or comment" (https://news.ycombinator.com/showhn.html). | One Show HN on the day code is public and runnable. Author must be present in the thread with numbers. |
| **GitHub issue threads as forums** | ollama/ollama#4643 (opened 26 May 2024, still open with a comment on 18 Oct 2026; original post 61 thumbs-up; no maintainer stance; users report 1 Gbps Ethernet making splitting slower than a smaller local model) (https://github.com/ollama/ollama/issues/4643). | Data-bearing comments only. This thread is literally where people who want multi-machine Ollama congregate. |
| **Project Discords** | exo `discord.gg/TJ4P57arEm` (https://github.com/exo-explore/exo); Petals usage `discord.gg/KdThf2bWVU` and hosting `discord.gg/X7DgtxgMhc` (https://github.com/bigscience-workshop/petals); distributed-llama via n4no.com (https://github.com/b4rtaz/distributed-llama). EleutherAI: 200+ monthly active, 150+ community researchers, 30+ countries, reading groups, SOAR internship (https://www.eleuther.ai/community/); its Discord invite page shows ~39.9k members **[search-only]**. Nous Research Discord ~147k members **[search-only]**. | Ask and answer technical questions; do not announce. Other projects' Discords are not UCompute's marketing channel. |
| **Reddit r/LocalLLaMA** | Latent Space's editor reads r/LocalLLaMA and r/localLLM "almost daily" and its recap covers 12 subreddits (https://latent.space/p/ainews-top-local-models-list-april/). Member count: Reddit blocked from this environment; a third-party stats page showed empty data and flagged the subreddit as quarantined **[unverified]**. | Benchmarks-with-hardware posts. The subreddit's self-promotion rules were not readable from here **[unverified]**; assume strict. |
| **X / Twitter** | Verified handles: `@exolabs` (https://github.com/exo-explore/exo), `@ggerganov` (https://github.com/ggerganov), `@awnihannun` (https://github.com/awni), `@PrimeIntellect` and `@jackclarkSF` **[search-only]**. Latent Space monitors ~544 X accounts for its recap (https://latent.space/p/ainews-top-local-models-list-april/). Follower counts for these accounts: **[unverified]**. | Reply with measurements to ggerganov/awni-adjacent threads; don't broadcast. |
| **Bluesky** | 142+ machine-learning starter packs listed as of Oct 2026, but none specific to LLM infrastructure or open-source AI systems (https://blueskystarterpack.com/machine-learning). Platform DAU figures **[search-only, unverified]**. | Low priority for this audience; academic ML presence exists but infra/local-inference community has not visibly formed there. |
| **Newsletters** | Import AI: picks technical reports with primary links, decentralization/compute-access themes, milestones against prior predictions (https://jack-clark.net/2025/04/21/import-ai-409-...). Latent Space AI News: ranks local models by "what people are actually recommending," sources Reddit + X, Discord access was cut off on the day of that issue (https://latent.space/p/ainews-top-local-models-list-april/). Interconnects, SemiAnalysis, Ahead of AI: coverage of home-device inference **[unverified]**, none surfaced in searches. | A technical report with a reproducible benchmark and a protocol spec is the artefact these pick up. |
| **Academic groups** | prima.cpp: MBZUAI lead with UESTC / CityU HK / La Trobe co-authors **[search-only]**, published ICLR 2026 (https://mlanthology.org/iclr/2026/li2026iclr-prima/). Parallax: Gradient (https://arxiv.org/abs/2509.26182). Integrity paper: Cihangiroglu and Nocera (https://arxiv.org/abs/2607.19490). Apple MLX team (https://machinelearning.apple.com/research/mlx-distributed-inference). | Cite them correctly in UCompute's own write-ups; invite reproduction on UCompute's named hardware. |
| **Independent benchmarkers / YouTube** | Jeff Geerling (Apple-loaned hardware, publishes failures and cost) (https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/). | The gold standard for credibility; only reachable once there is a runnable build. |

---

## 4. What this audience values in a new project (evidence-backed)

1. **Measured tokens/sec and TTFT on named hardware, with the losing cases included.** Requested on day one of exo's HN thread (https://news.ycombinator.com/item?id=40973339); Apple publishes its own two-machine-slower-than-pipeline case (https://machinelearning.apple.com/research/mlx-distributed-inference); mlx-optiq publishes a 2.7x regression (https://mlx-optiq.com/docs/cluster); Geerling publishes crashes and cost (https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/).
2. **An explicit threat model and trust boundary.** exo was asked for one at launch and said "assumes trusted devices on a local network" (https://news.ycombinator.com/item?id=40973339). llama.cpp states its RPC trust boundary bluntly (https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md). Block states "Share compute with people you trust" and that results are not verified (https://engineering.block.xyz/blog/buzz-sharing-compute-powered-by-meshllm). The research literature now formalises attacker models: a tampering node altering layer outputs (https://arxiv.org/abs/2607.19490); an untrusted server inverting activations (https://arxiv.org/abs/2602.16760).
3. **A license and a real repo before any claims.** exo added a LICENSE in response to the HN thread (https://news.ycombinator.com/item?id=40973339). Show HN excludes "sign-up pages" and things that cannot be tried (https://news.ycombinator.com/showhn.html).
4. **Honest "experimental" labelling.** llama.cpp: "proof-of-concept ... fragile and insecure" (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md). Mesh LLM: "experimental distributed-systems software" (https://github.com/Mesh-LLM/mesh-llm). prima.cpp lists no Windows, no Vulkan/AMD (https://github.com/OpenCPIL/prima.cpp).
5. **Protocol-level specifics.** Mesh LLM's iroh post lists ALPNs and stream types (https://www.iroh.computer/blog/mesh-llm); llama.cpp RPC README documents handshake-negotiated RDMA fallback to TCP (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md); INTELLECT-2 names TOPLOC/SHARDCAST and how invalid nodes are evicted (https://www.primeintellect.ai/blog/intellect-2-release).
6. **Reproducibility and pre-registration.** The integrity paper fixed "metrics and success criteria before experiments ran" across 408 configurations (https://arxiv.org/abs/2607.19490). ICLR acceptance for prima.cpp (https://mlanthology.org/iclr/2026/li2026iclr-prima/).
7. **Secure defaults, not documentation.** LeakIX argues the gap between "local-first" positioning and 12,269 exposed servers is the maintainers' responsibility (https://blog.leakix.net/2026/02/ollama-exposed/); Cisco asks for auth plus audit logging (https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama).
8. **Skepticism of VC/token framing.** The vendor comparison flags exo's "VC-backed" governance as a risk (https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html); Import AI frames decentralized compute as a policy question, not a product (https://jack-clark.net/2025/04/21/import-ai-409-...).

---

## 5. Papers and posts that define the 2025-2026 conversation

| Date | Item | Why it matters to UCompute |
|---|---|---|
| 11 Mar 2025 (v3 9 Apr 2026) | "Will LLMs Scaling Hit the Wall?" position paper, arXiv 2503.08223 | The thesis that edge devices matter; UCompute's "Compute better. Together." direction sits here, but the paper is about training. |
| 7 Apr 2025 -> ICLR 2026 | prima.cpp, arXiv 2504.08791 | The reference design for heterogeneous home-cluster partitioning. If UCompute ever partitions, this is the bar; until then, cite it as why you don't. |
| 21 Apr 2025 | Import AI 409 on INTELLECT-2 | How a top newsletter frames decentralized compute (policy, prediction-tracking). |
| 11 May 2025 | INTELLECT-2 release (TOPLOC verification, node eviction) | The verification vocabulary this audience expects when "untrusted compute" is mentioned. |
| 1 Sep 2025 | Cisco Talos: 1,139 exposed Ollama servers | Practical security backdrop; auth + audit logging asked for. |
| 30 Sep 2025 | Parallax, arXiv 2509.26182 | Volunteer-GPU scheduling; shows the "swarm" end of the spectrum UCompute explicitly has not built. |
| 18 Dec 2025 | Geerling: 1.5 TB VRAM Mac Studio cluster | Most-read independent test of exo + RDMA; honest failures and cost. |
| 18 Feb 2026 | Split inference privacy, arXiv 2602.16760 | Quantifies activation leakage (~59% tokens recoverable at 2-layer split). UCompute leaks no activations because requests are not split. |
| 23 Feb 2026 | LeakIX: 12,269 exposed Ollama instances | "Local-first" vs reality; secure defaults as maintainer duty. |
| 26 Mar 2026 | CVE-2026-34159, llama.cpp RPC unauthenticated RCE, CVSS 9.8, no patch listed | The single strongest argument for UCompute's authenticated, non-RPC architecture. |
| 11 Jul 2026 | Mesh LLM on iroh (QUIC, route-whole-request option, Apache-2.0) | Closest analogue; demonstrates demand and the credibility of experimental labelling. |
| 21 Jul 2026 | Integrity under malicious nodes, arXiv 2607.19490 (canaries, AUROC 1.0 across 408 configs) | Current security research framing for layer-split pipelines. |
| 27 Jul 2026 | Block "Buzz" post | A corporate adopter telling users to "share compute with people you trust." |
| 15 Oct 2026 | Apple MLX distributed inference post | Authoritative statement that pipeline parallel does not speed decode and tensor parallel needs RDMA-class links. |

---

## 6. What technical content from UCompute would earn credibility here (given no partitioning)

Each item is tied to something UCompute has verified in development builds. Nothing below requires claiming features that do not exist.

### 6.1 Publish a threat model and a protocol note for UCompute Mesh (highest leverage)
- Contents: pairing with a short code; device keys pinned at pairing; QUIC + TLS 1.3; what the audit log records (off-device requests, no prompt text); local-only mode refusing every off-device request by default; revocation closing the connection in under 0.1 s in tests (state the test setup); connect-by-address fallback when mDNS is blocked.
- Why it lands: llama.cpp documents the absence of exactly these controls (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md, https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md); CVE-2026-34159 shows the consequence (https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw); Cisco and LeakIX ask for auth and audit logging (https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama, https://blog.leakix.net/2026/02/ollama-exposed/); Mesh LLM shows the format this audience reads (ALPNs, stream types) (https://www.iroh.computer/blog/mesh-llm).
- Format: a `SECURITY.md` with explicit in/out-of-scope (model llama.cpp's), plus a short `docs/threat-model.md`. Consider an arXiv cs.CR technical note later; cs.CR is where 2607.19490 and 2602.16760 landed.

### 6.2 Write "Why UCompute routes whole requests and does not split models (yet)"
- Cite the measured evidence: Apple's "pipeline parallelism does not speed up decode" (https://machinelearning.apple.com/research/mlx-distributed-inference); the 2.7x regression for models that fit on one device (https://mlx-optiq.com/docs/cluster); 42.2 -> 34.1 tok/s on a 200 Gb/s link (https://github.com/ollama/ollama/issues/4643); Geerling's cost and instability (https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/).
- State the corollary honestly: whole-request routing cannot run a model larger than the largest single device. Point to prima.cpp (https://arxiv.org/abs/2504.08791) as the state of the art for the problem UCompute is deferring, and say partitioning is "design only."
- Security bonus: no activations leave a device, so the activation-inversion and layer-tampering attack classes (https://arxiv.org/abs/2602.16760, https://arxiv.org/abs/2607.19490) do not apply. Say this precisely, not as a marketing line.

### 6.3 Ship a reproducible benchmark harness, not a benchmark blog
- Pinned llama.cpp b11609; named devices (Apple M2 / macOS 26.2; Windows 11 / Intel Arc 140V); memory-fit check outcome; tokens/sec, TTFT, and the routing decision for each request; raw JSON published. Include the cases where routing to another device was slower than local.
- Why: every credible source in this space publishes the losing case (Apple, mlx-optiq, Geerling); vendor-only numbers are discounted (the search results repeatedly flagged exo's 1.8x/3.2x as vendor claims; the sharedllm comparison was caught mis-stating exo's license).

### 6.4 Document the download integrity path
- SHA-256 verified downloads with license display answers llama.cpp's SECURITY.md advice to "match a known-good hash" and to treat model trust as non-binary (https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md). A short doc on how UCompute pins hashes and shows licenses is cheap and credible.

### 6.5 Engage where the data is asked for, with data only
- ollama/ollama#4643 is a live, two-year thread of people wanting multi-machine Ollama (https://github.com/ollama/ollama/issues/4643). A single comment with measured whole-request routing numbers, once public, is legitimate; a product plug is not.
- HN: one Show HN on the day the repo has runnable code (rules: https://news.ycombinator.com/showhn.html). Be present; answer the bandwidth/latency objection with the "we don't split" write-up ready.
- Discords of exo/Petals/distributed-llama: ask questions as a peer; never announce.

### 6.6 What not to do with this audience
- Do not publish before source. The repo currently holding only a LICENSE will be the first comment.
- Do not lead with "Compute better. Together." or the compute-credit economy; label direction as direction and keep it out of technical posts. The decentralized-training sub-community is primed to read credits as a token play (see 2.9).
- Do not use secondary benchmark numbers for competitors (e.g., the 5.3x Parallax-vs-Petals figure is vendor-reported and unverified here).
- Do not say "supported" for any platform; say "verified on" with the exact machine, matching the brief.

---

## 7. Opportunities (ranked)

1. Threat model + protocol note for Mesh (6.1): directly answers the ecosystem's loudest documented weakness; zero cost; publishable before source as a design doc, but credibility is higher with code.
2. "Why we don't split" post (6.2): converts the biggest perceived gap into the most defensible position, backed by Apple's own numbers.
3. Reproducible benchmark harness (6.3): the artefact Import AI / Latent Space / Geerling-type reviewers can actually use.
4. cs.CR/cs.DC technical note on device-granular routing with pinned-key pairing: enters the arXiv feed this audience reads; cheap once 6.1-6.3 exist.
5. Single Show HN on release day with the author in-thread.
6. Data-only participation in ollama#4643 and similar threads once a runnable build exists.

## 8. Risks

1. **Premature exposure.** HN and r/LocalLLaMA punish repos with no code; exo was pressed for LICENSE and benchmarks within hours (https://news.ycombinator.com/item?id=40973339).
2. **"Not pooling" read as "not interesting."** Mitigated only by the measured-evidence framing in 6.2; without it, the audience files UCompute under "Ollama with a remote."
3. **Security claims invite security scrutiny.** llama.cpp's RPC history shows that even layered checks got bypassed (https://retr0.blog/blog/llama-rpc-rce; https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw). A published threat model must come with a SECURITY.md and disclosure path.
4. **Pinned engine drift.** b11609 will age; the audience tracks llama.cpp advisories (3 RPC-related GHSAs on the first advisories page: https://github.com/ggml-org/llama.cpp/security/advisories). Document the update policy.
5. **Credit-economy association.** Decentralized-compute readers are alert to token framing (see 2.9 cautions); any "direction" language leaking into technical docs costs trust.
6. **Small, slow audience.** prima.cpp has an ICLR paper and ~125 stars on its official repo (https://github.com/OpenCPIL/prima.cpp). Academic credibility here does not convert to adoption quickly; this lens is for credibility and inbound contributors, not volume.

---

## 9. Verification gaps (explicitly unverified)

- r/LocalLLaMA member count and self-promotion rules (Reddit unreachable from this environment).
- Discord member counts for EleutherAI (~39.9k) and Nous (~147k): search snippets only.
- Mesh LLM's HN point count (179 vs 277 in different secondary sources).
- Follower counts for `@ggerganov`, `@awnihannun`, `@exolabs`, `@PrimeIntellect`.
- prima.cpp author affiliations beyond the arXiv author list; whether older prima.cpp repos hold more stars.
- Parallax license and its vendor-reported 5.3x figure.
- INTELLECT-3 training-infrastructure critique.
- Petals public swarm liveness (health page refused connection once on 2026-10-30; one attempt).
- Any Interconnects / SemiAnalysis / Ahead of AI coverage of home-device inference.
- Existence of any BOINC LLM-inference project.

---

## Sources (every URL read directly)

1. https://github.com/exo-explore/exo
2. https://github.com/exo-explore/exo/blob/main/LICENSE
3. https://news.ycombinator.com/item?id=40973339
4. https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/
5. https://arxiv.org/abs/2504.08791
6. https://arxiv.org/html/2504.08791 (reached via https://huggingface.co/papers/2504.08791)
7. https://github.com/OpenCPIL/prima.cpp
8. https://mlanthology.org/iclr/2026/li2026iclr-prima/
9. https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md
10. https://github.com/ggml-org/llama.cpp/blob/master/SECURITY.md
11. https://github.com/ggml-org/llama.cpp/security/advisories
12. https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw
13. https://retr0.blog/blog/llama-rpc-rce
14. https://github.com/b4rtaz/distributed-llama
15. https://github.com/bigscience-workshop/petals
16. https://health.petals.dev/ (connection refused on 2026-10-30)
17. https://machinelearning.apple.com/research/mlx-distributed-inference
18. https://mlx-optiq.com/docs/cluster
19. https://github.com/awni
20. https://github.com/ggerganov
21. https://github.com/Mesh-LLM/mesh-llm
22. https://www.iroh.computer/blog/mesh-llm
23. https://engineering.block.xyz/blog/buzz-sharing-compute-powered-by-meshllm
24. https://arxiv.org/abs/2509.26182
25. https://www.primeintellect.ai/blog/intellect-2-release
26. https://github.com/PsycheFoundation/psyche
27. https://arxiv.org/abs/2503.08223
28. https://arxiv.org/abs/2607.19490
29. https://arxiv.org/abs/2602.16760
30. https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
31. https://blog.leakix.net/2026/02/ollama-exposed/
32. https://sharedllm.org/blog/sharedllm-vs-petals-vs-exo.html
33. https://github.com/ollama/ollama/issues/4643
34. https://news.ycombinator.com/item?id=43753890
35. https://news.ycombinator.com/showhn.html
36. https://www.eleuther.ai/community/
37. https://blueskystarterpack.com/machine-learning
38. https://jack-clark.net/2025/04/21/import-ai-409-huawei-trains-a-model-on-8000-ascend-chips-32b-decentralized-training-run-and-the-era-of-experience-and-superintelligence/
39. https://latent.space/p/ainews-top-local-models-list-april/
40. https://arxiv.org/list/cs.DC/recent

Search-only (seen in result snippets, not read; cited above as [search-only]): discord.com/invite/2kpBev9nCd (EleutherAI), discord.com/invite/nousresearch, x.com/PrimeIntellect, x.com/jackclarkSF, gradient.network/parallax.pdf, implicator.ai INTELLECT-3 critique, arxiv.org/pdf/2603.20661 (WWW.Serve), arxiv.org/html/2509.24257 (VeriLLM), subredditstats.com/r/LocalLLaMA (empty data).
