# Search demand and content gaps (synthesis)

Internal. Research date: **2026-10-30**. Raw lens: `research/raw/search-demand.md` (48 pages read, ~90 surfaced only as titles). Query language cross-checked against `research/raw/audience-multi-device-developers.md` and `research/raw/audience-local-ai-developers.md`.

## 0. Read this first: limits

- **No search volumes were measured.** No keyword database, rank tracker, Search Console or Ahrefs data exists for this project. "Demand" below is an inference from four signals: whether official docs exist for the query, how many third-party pages compete, whether the topic has had news or CVE coverage, and whether dedicated tools (calculators, detection rules) exist for it. Treat the ranking as a hypothesis to test once Search Console is available (owner-verified, free; `handoffs/2026-10-30-website-engineering-notes.md` §Measurement).
- "What currently ranks" means what the research tool surfaced in its top results on 2026-10-30. Reddit was not reachable; r/LocalLLaMA and r/ollama threads plausibly rank for many of these how-to queries and are a known blind spot.
- Query phrasings are constructed from the titles and headings of ranking pages, the official docs' own vocabulary and the questions recorded in the audience lenses. They are not drawn from a keyword tool.
- Every page UCompute writes is bounded by `claims/REGISTRY.md` and `claims/PROHIBITED.md`: no pooling, splitting, cluster, speed or throughput language; no download, install-now, sign-up or waitlist language; no privacy absolutes ("never leaves your device", "end-to-end private", "works offline"). Every Mesh page states: each request runs whole on one device; same local network; no relay or NAT traversal; no open network; no cloud; no mobile; no auto-update.
- Anything not confirmed from a page that was read is marked **unverified**.

## 1. Clusters ranked by inferred demand

| Rank | Cluster | Demand signal | Gap UCompute can truthfully fill | Covered by a ready piece? |
|---|---|---|---|---|
| 1 | Exposed local AI servers / binding to 0.0.0.0 | Two news cycles (Cisco Talos Sep 2025; SentinelLABS/Censys 2026), an Elastic detection rule, two security vendors writing against it | Large: every ranking page is VPN/ZTNA marketing or generic Q&A; none covers the shared-LAN case or device-level trust | No (openai-client page mentions loopback default only) |
| 2 | Run a model on another computer on the same network | Evergreen how-to; official Ollama FAQ and LM Studio docs; many tutorials; SSH-tunnel and Tailscale guides | Large: answers are "open the port" or "install a VPN"; nothing on pairing, device identity, revocation, audit, blocked mDNS | Partly (`2026-10-30-pairing-explainer` covers the mechanism, not the how-to) |
| 3 | Local LLM with an OpenAI-compatible API | Very common; strong official docs | Small for syntax; medium for "the key is ignored, so a non-loopback bind is unauthenticated" | **Yes**: `2026-11-02-openai-client-base-url` |
| 4 | Memory requirements of GGUF models / "will it fit" | Many calculators and articles compete; none authoritative | Medium: no calculator publishes its method; several ignore KV cache; none ties fit to the download decision | **Yes**: `2026-11-01-memory-fit-explainer` |
| 5 | Pairing devices for local AI | New since NVIDIA PAIR (first release 26 Aug 2026, wide coverage Sep 2026) | Medium: PAIR coverage dominates; nobody explains the trust model of pairing in plain language | **Yes**: `2026-10-30-pairing-explainer` |
| 6 | Local-only / no-telemetry runners | Steady; several "privacy audit" pages and official privacy pages | Medium: audits publish no captures and contradict each other; no project enumerates every outbound connection | No (needs an Engineering confirmation first; §4) |
| 7 | Verifying model downloads (SHA-256) | Niche, rising (supply-chain posts; an Ollama "verified nothing" write-up) | Large: no official Hugging Face page read explains the end-user check; Ollama docs do not name the algorithm | Partly (`2026-11-01-memory-fit-explainer` states the pinned-hash check in one sentence) |
| 8 | llama.cpp RPC security | Niche; spiked with CVE-2026-34159 | Medium: tutorials still bind RPC to all interfaces; nobody contrasts tensor-level RPC with whole-request routing | **Yes**: `2026-10-31-loopback-rpc-vs-authenticated-transport` |
| 9 | Sharing a GPU over the LAN securely | Moderate; overlaps 1 and 2 | Medium: shared bearer key or VPN membership are the only documented patterns; no per-device identity or audit | No |
| 10 | Revoking a device | Very thin; no dedicated local-AI content found | Large gap, low demand today | Partly (`2026-10-30-pairing-explainer` §revoke; `2026-10-30-what-the-audit-log-records`) |

## 2. Clusters in detail

Each cluster: phrasings, what ranks (title as read, URL), what those pages miss or get wrong, and the page UCompute can truthfully write with its claim ids.

### 2.1 Exposed local AI servers / 0.0.0.0 (rank 1)

**Phrasings.** "ollama 0.0.0.0 security risk"; "is it safe to expose ollama"; "ollama exposed to internet"; "ollama no authentication"; "ollama unauthenticated api risk"; "exposed ollama servers shodan"; "ollama port 11434 open"; "how to check if my ollama is exposed"; "ollama probllama cve-2024-37032". Audience vocabulary: `OLLAMA_HOST`, `ss -tlnp`, `curl .../api/tags`, "no built-in authentication", "LLMjacking".

**What ranks (read).**
- Cisco Talos, "Detecting Exposed LLM Servers: A Shodan Case Study on Ollama" (1 Sep 2025), https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama. 1,139 exposed instances; 214 (18.8 %) serving models; 88.89 % used the OpenAI route structure; six recommendations including "verify models by hash or trusted origin before execution".
- The Register, "In the rush to adopt hot new tech, security is often forgotten. AI is no exception" (2 Sep 2025), https://www.theregister.com/2025/09/02/exposed_ollama_servers_insecure_research/ (secondary).
- Tailscale, "Finding 1,000 exposed AI servers took researchers 10 minutes" (3 Sep 2025), https://tailscale.com/blog/AI-endpoints-on-public-web (vendor).
- Twingate, "175,000 Ollama Servers Are Exposed to the Internet Right Now. Yours Doesn't Have to Be" (2026), https://www.twingate.com/blog/ollama-server-exposure (vendor; headline figure unsourced in body).
- Elastic prebuilt rule, "Ollama API Accessed from External Network", https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/cross-platform/initial_access_ollama_api_external_access.
- Ollama FAQ and Authentication docs: "The local API at `http://localhost:11434` does not require authentication." https://docs.ollama.com/faq, https://docs.ollama.com/api/authentication.
- **Unverified** secondary figures (175,108 hosts, 130 countries; SentinelLABS/Censys) via TechRadar, SC Media, TechInformed, The Hacker News (2026-01-29). Primary report not read. Do not quote in content.

**What they miss or get wrong.** Figures from different methods and dates are mixed without stating the method. The remedy on every vendor page is the vendor's product. "Exposed" means internet-exposed; the same bind on a shared LAN (dorm, office, guest Wi-Fi) gets no treatment. No read page gives a short OS-by-OS "what is my AI server listening on" check.

**Page UCompute can write.** *What binding a local AI server to 0.0.0.0 actually exposes, and how to check yours in 60 seconds.* Neutral explainer: loopback vs all interfaces; what Ollama's, llama.cpp's and LM Studio's docs say about defaults and auth (quoted); `lsof`/`netstat`/`ss` checks for macOS, Windows, Linux; why a LAN is not automatically trusted. Then UCompute's position in registry words: the local API listens on 127.0.0.1 by default (`run-local`, `openai-clients`); local-only mode refuses every off-device request (`local-only`); other devices reach a device only after pairing (`mesh-pair-choose`, `transport`); the device that runs the request processes the prompt (`device-sees-prompt`). Cite Cisco's primary post; omit the 175,000 figure. Claims: `run-local`, `local-only`, `openai-clients`, `transport`, `mesh-pair-choose`, `device-sees-prompt`, `platforms`, `no-release`, `license`.

### 2.2 Run a model on another computer on the same network (rank 2)

**Phrasings.** "access ollama from another computer on local network"; "use desktop gpu from laptop llm"; "ollama OLLAMA_HOST 0.0.0.0 windows firewall 11434"; "lm studio serve on local network"; "connect to ollama on another pc"; "run llm on another machine ssh tunnel"; "ollama tailscale remote access"; "use my home gpu for ai from laptop"; "ollama another device same wifi"; "run LLMs on a Windows gaming PC and reach them from a Mac" (HN phrasing).

**What ranks (read).**
- blackmoreops, "Access Ollama on Kali Linux From Another PC", https://www.blackmoreops.com/how-to-access-ollama-from-another-pc-on-your-local-network/ (sets `OLLAMA_HOST=0.0.0.0:11434` and `OLLAMA_ORIGINS=*`, firewall rule; warns there is no built-in auth).
- Ollama FAQ, "How can I expose Ollama on my network?", https://docs.ollama.com/faq (example binds `0.0.0.0:11434`; no auth section).
- LM Studio, "Serve on Local Network", https://lmstudio.ai/docs/developer/core/server/serve-on-network ("Any bind other than `127.0.0.1` exposes the server beyond `localhost`"; recommends enabling authentication).
- LM Studio, "LM Link", https://lmstudio.ai/docs/lmlink ("made possible in partnership with Tailscale"; "end-to-end encrypted, thanks to Tailscale"; no pairing-approval or device-removal description on the page read).
- "Connecting to Remote Ollama Servers with SSH Tunneling" (15 Jun 2025), https://yhren.github.io/posts/ai/llm/ollama/connecting_to_remote_ollama_servers_with_ssh_tunneling/.
- Serverman, "Ollama + Tailscale: Secure Remote Access Setup Guide", https://serverman.co.uk/ai/ollama/ollama-security-guide/ ("Ollama has no authentication layer at all").
- Surfaced only: digitalcitizen.life (403), centron.de, KDnuggets, DEV (coderberry), mayhemcode, Dell blog on LM Link, university HPC SSH-forwarding pages.

**What they miss or get wrong.** Two answers only: open the port plus a firewall rule (everyone on the Wi-Fi can use it), or a VPN overlay (identity delegated to a third-party account). Nothing covers which device may talk to which, how to stop one later, what was used and when, or what to do when multicast discovery is blocked. Several guides set `OLLAMA_ORIGINS=*` while warning about exposure. Home-LAN guides assume the LAN is trusted.

**Page UCompute can write.** *Use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi.* Both devices run UCompute; pair with a short code; the laptop chooses the desktop to run a whole request (`mesh-pair-choose`); QUIC with TLS 1.3 and device keys pinned at pairing (`transport`); nothing listens for unpaired devices (`local-only`); the audit log records the off-device request without prompt or response (`audit`); connect by address when discovery is blocked (`connect-by-address`); on Windows the firewall rule covers only UCompute's own program on private networks (`windows-firewall`); revoke in one step (`revocation`). State plainly: the model must fit on the chosen device (`catalog-fit`), same local network, no relay, no speed figure, and use the exact text of `demo-2026-10-19` for the one two-machine run that may be described. Include a three-pattern comparison (open port, VPN overlay, paired devices) by what each one trusts, quoting the other tools' own docs. Claims: `mesh-pair-choose`, `transport`, `local-only`, `audit`, `revocation`, `connect-by-address`, `windows-firewall`, `catalog-fit`, `device-sees-prompt`, `demo-2026-10-19`, `platforms`, `no-release`, `license`.

### 2.3 Local LLM with an OpenAI-compatible API (rank 3)

**Phrasings.** "local llm openai compatible api"; "llama.cpp server openai api"; "ollama openai compatible endpoint python"; "openai python client base_url local model"; "lm studio openai api localhost 1234"; "use openai sdk with local model api key"; "openai compatible server gguf"; "llama-server /v1/chat/completions".

**What ranks (read).** Ollama, "OpenAI compatibility", https://docs.ollama.com/openai (`api_key='ollama'` "required but ignored"; lists limitations). llama.cpp server README, https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md (default `127.0.0.1:9931`; `--api-key` default none; CORS reflects any Origin; `--tools`/`--agent` "do not enable in untrusted environments"). LM Studio API docs, https://lmstudio.ai/docs/app/api. Surfaced only: lmsa.app, promptquorum, machinelearningplus, mindstudio, Railway template, Agno docs, llama.cpp issue #19138.

**What they miss or get wrong.** Third-party tutorials stop at "change base_url and use a dummy key" and never say the consequence: the key is ignored, so a non-loopback bind has no authentication at all. None connects route uniformity to exposure (Cisco: 88.89 % of exposed servers used the OpenAI route structure). Default-port drift for llama-server (8080 in tutorials vs 9931 in today's README; which applies per release is **unverified**) is explained nowhere.

**Covered by** `2026-11-02-openai-client-base-url` (claims `openai-clients`, `run-local`, `local-only`, `device-sees-prompt`, `no-release`, `license`). It already states the server listens on 127.0.0.1:8192 by default and that tool calling is not yet verified. **Amendment to consider:** one paragraph linking to the cluster-1 page once it exists ("what changes if you bind beyond loopback"). No new page.

### 2.4 Memory requirements / "will it fit" (rank 4)

**Phrasings.** "gguf vram calculator"; "how much ram to run 7b gguf"; "q4_k_m vs q5_k_m size"; "will this model fit my gpu"; "llm vram requirements 8gb"; "gguf memory requirements context length kv cache"; "can i run it llm"; "bits per weight q4_k_m"; audience shape: "Best Coding Model for Ryzen9/4060/64 GB Notebook?".

**What ranks (read).** Hugging Face Hub docs, "GGUF", https://huggingface.co/docs/hub/gguf (bits-per-weight table; no memory formula). llmrun.dev, "Can I Run This LLM? AI Model Hardware Checker", https://llmrun.dev (fit rating; method not explained). CanIRun.ai, https://www.canirun.ai (letter grades; no KV cache mention). bmdpat, "GGUF Q4 vs Q5 vs Q8: which quant should you pick?", https://bmdpat.com/blog/gguf-quant-which-to-pick-2026 (retracted unsourced figures). Surfaced only: SadP0i GGUF VRAM calculator Space, dlsniper/gguf-llm-vram-calculator, sammcj/quantest, ggufit, rapidtoolset, SitePoint, eastondev, inventivehq; tinyweights.dev/fit (DNS failed).

**What they miss or get wrong.** No calculator publishes its method; one ignores KV cache; none computes fit against memory actually free at download time; none combines size, license and fit in one pre-download decision.

**Covered by** `2026-11-01-memory-fit-explainer` (claims `catalog-fit`, `engine`, `platforms`, `no-release`, `license`), which publishes the pre-download lower bound, the full estimate's terms, the calibration (14 combinations, -4.6 % to +8.9 %, Apple M2) and the limits (nothing above 1.5 B measured; calibrated for Apple Silicon). No new page. Note the phrasings themselves contain prohibited tokens ("7b"); the page must not echo them in its own voice.

### 2.5 Pairing devices for local AI (rank 5)

**Phrasings.** "pair devices local ai"; "nvidia pair personal ai router setup"; "connect two computers for local llm"; "home ai cluster pairing code"; "local ai network of my own devices"; "mtls local ai cluster". (Several phrasings carry the word "cluster"; UCompute pages must not use it in their own voice.)

**What ranks (read).**
- NVIDIA Technical Blog, "NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network" (3 Sep 2026), https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/ ("PAIR does not make one inference request run across several GPUs"; mDNS or add by IP; mTLS with generated certificates).
- NVIDIA/Personal-AI-Router README, https://github.com/NVIDIA/Personal-AI-Router (six-digit PIN; "Any member can also remove it"; Apache-2.0).
- heise online, "Nvidia PAIR: Private devices become an AI network" (5 Sep 2026), https://www.heise.de/en/news/Nvidia-PAIR-Private-devices-become-an-AI-network-11442187.html.
- LocalMesh (Ydde21) README, https://github.com/Ydde21/LocalMesh (mTLS; "a model must fit within one node's resources"; 0 stars when read).
- Mesh LLM README, https://github.com/Mesh-LLM/mesh-llm (QUIC; public meshes via Nostr; ~3.7k stars).
- exo README, https://github.com/exo-explore/exo (auto-discovery; no API authentication described).
- Vellum, "Pair a device", https://www.vellum.ai/docs/hosting-options/pair-a-device (unrelated product; codes expire in 10 minutes; explicit revoke command).
- Surfaced only: wccftech, SDxCentral, MeshCompute (two repos), saint0x/mesh, EastonSell/household-compute, Ken Ashe on Mesh LLM.

**What they miss or get wrong.** PAIR's materials describe the PIN and mTLS but not what the PIN proves, what is pinned afterwards, or what "remove" does to a device's credentials (NVIDIA's getting-started page calls the PIN "a temporary bootstrap code rather than a strong credential"). exo's README describes discovery with no authentication statement. Mesh LLM targets public meshes, a different threat model from "my own devices on my LAN". None treats the shared-network case where discovery is visible to strangers.

**Covered by** `2026-10-30-pairing-explainer` (claims `mesh-pair-choose`, `transport`, `revocation`, `local-only`, `device-sees-prompt`, `audit`, `connect-by-address`, `platforms`, `no-release`, `license`). It already treats PAIR as a fair comparable. **Amendment to consider:** `research/COMPETITORS.md` now records that PAIR documents node removal as a UI step, so the piece must present revoke as part of the lifecycle, not as unique; check the lead against that before handoff.

### 2.6 Local-only / no-telemetry runners (rank 6)

**Phrasings.** "does ollama phone home"; "lm studio telemetry"; "local llm no telemetry"; "offline ai no internet privacy"; "jan ai privacy telemetry"; "which local ai is truly private"; "ollama privacy update check registry.ollama.ai"; "air gapped llm"; GitHub shape: "Clarify about Telemetry", "Does Ollama send my prompts and answers back to ollama.com?".

**What ranks (read).** Ollama FAQ, https://docs.ollama.com/faq ("We don't see your prompts or data when you run locally"; `OLLAMA_NO_CLOUD=1`). LM Studio privacy policy, https://lmstudio.ai/privacy ("does not include telemetry"; update checks send device and app information). LM Studio, "Offline operation", https://lmstudio.ai/docs/app/offline. Jan privacy page, https://jan.ai/docs/privacy. local-llm.net, "Local AI Privacy Audit 2026: What Apps Send Home" (8 Apr 2026), https://www.local-llm.net/blog/local-ai-privacy-audit/ (no captures published; per-tool claims **unverified**). InsiderLLM, "Local AI for Privacy: What's Actually Private", https://insiderllm.com/guides/local-ai-privacy-guide/ (**unverified**). PromptQuorum, "Local LLM Security and Privacy Checklist: 12 Steps to a Safe Setup", https://www.promptquorum.com/local-llms/local-llm-security-privacy-checklist.

**What they miss or get wrong.** The "audits" assert traffic findings without evidence and disagree with each other. Official pages are careful but incomplete (LM Studio's offline page omits telemetry; Jan's privacy page omits update checks). No project publishes a complete enumerated list of outbound connections and the user action that triggers each. "Local-only" is treated as a promise about prompts rather than a network policy with a default.

**Page UCompute can write (held until Engineering confirms the list).** *Every network connection UCompute makes, and why.* An enumerated manifest for the development build: the engine archive fetched on first use and checked against its published hash (`engine`); model files fetched only when the user starts a download, checked against a pinned SHA-256 (`catalog-fit`, `run-local` qualifier "Downloading a model or the engine uses the internet"); paired devices on the local network only after pairing (`mesh-pair-choose`, `transport`); no cloud exists (`planned`). Describe local-only as a policy with a default (`local-only`) and add the required context (`device-sees-prompt`). Publish the method readers can use to check (an outbound capture during a session). **Blocker:** the registry has no claim that enumerates every outbound host or states that no update check runs; the page cannot be called ready until Engineering confirms the complete list (see `research/BARRIERS.md` asks). Claims: `local-only`, `run-local`, `engine`, `catalog-fit`, `mesh-pair-choose`, `transport`, `planned`, `device-sees-prompt`, `no-release`, `license`.

### 2.7 Verifying model downloads, SHA-256 (rank 7)

**Phrasings.** "verify gguf sha256"; "huggingface model checksum sha256 verify download"; "ollama digest mismatch file must be downloaded again"; "ollama verifying sha256 digest"; "gguf model hash supply chain"; "how to check model file integrity".

**What ranks (read).** Kunal Ganglani, "Verify GGUF Model Hashes: 10-Step Supply Chain Workflow" (31 Aug 2026, updated 6 Oct 2026), https://www.kunalganglani.com/blog/verify-gguf-hashes-supply-chain. DEV, "Ollama: 'digest mismatch, file must be downloaded again'", https://dev.to/multigrid/ollama-digest-mismatch-file-must-be-downloaded-again-1k19. DEV, "It Printed 'Verifying.' It Verified Nothing.", https://dev.to/yeriahz/it-printed-verifying-it-verified-nothing-1cde (reports ollama/ollama#17520; issue not read, **unverified**). Ollama API docs, "Pull a model", https://docs.ollama.com/api/pull (algorithm not named). Hugging Face Hub docs, "Security", https://huggingface.co/docs/hub/security; "Download files from the Hub", https://huggingface.co/docs/huggingface_hub/en/guides/download; "Xet: our Storage Backend", https://huggingface.co/docs/hub/en/xet/index. Surfaced only: gguf-merge-tool, edgemodelr, codexdeep/ollama-dl, a Hailo community thread, Hub "Large File Pointer Details" block (**unverified**).

**What they miss or get wrong.** No official Hugging Face page read tells an end user how to compare a downloaded GGUF with the Hub's recorded SHA-256 or confirms the library verifies on the user's behalf. Ollama's API docs do not name the algorithm. The supply-chain post is enterprise-oriented and skips "where is the publisher's hash for this file?". Nobody says a hash published next to the file proves integrity in transit, not publisher identity.

**Page UCompute can write.** *What "verified" means in UCompute: SHA-256 against a pinned hash, before the engine opens the file.* State where the expected hash lives (pinned in UCompute's catalog, per `catalog-fit`), when it is computed (after download, before load), what happens on mismatch, and what it does not prove (publisher identity, model safety). Same treatment for the engine archive (`engine`). Include manual `shasum -a 256` / `Get-FileHash` / `sha256sum` commands for users of other tools. **Unverified, must not be implied:** whether files already on disk are re-hashed before every load; what the user sees on mismatch. Ask Engineering before writing those sentences. Claims: `catalog-fit`, `engine`, `run-local`, `no-release`, `license`.

### 2.8 llama.cpp RPC security (rank 8)

**Phrasings.** "llama.cpp rpc server security"; "rpc-server llama.cpp authentication"; "CVE-2026-34159 llama.cpp"; "ggml-rpc-server 0.0.0.0"; "llama.cpp --rpc multiple machines"; "is llama.cpp rpc encrypted"; "why not just use llama.cpp RPC?" (community phrasing). Several searchers type "llama.cpp rpc distributed inference setup"; UCompute pages must not echo that phrase.

**Verified fact for this cluster.** **CVE-2026-34159**: llama.cpp RPC backend, CVSS 3.1 base score 9.8 (critical), unauthenticated remote code execution via a `deserialize_tensor()` bounds-check bypass when a tensor's `buffer` field is 0; published 2026-04-01; fixed in build b8492. Source: https://cveawg.mitre.org/api/cve/CVE-2026-34159 (read 2026-10-30). Corroborating: GitHub advisory GHSA-j8rj-fmpv-wcxw, https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw (advisory page dated 26 Mar 2026, lists no patched version, quotes SECURITY.md "Do not use the RPC backend"); OSV, https://osv.dev/vulnerability/CVE-2026-34159 (names b8492). The release UCompute pins (b11609, per the ready piece's sources and engineering `catalog/backends.json`) is later than the fix, and the ready piece states UCompute does not use the RPC backend today and runs the engine on loopback with a per-process key.

**What ranks (read).** llama.cpp RPC README, https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md ("proof-of-concept development stage"; "fragile and insecure"; "Never run the RPC server on an open network or in a sensitive environment!"; no mention of authentication or encryption). GHSA-j8rj-fmpv-wcxw and the OSV entry (above). Arm Learning Path, "Configure the worker nodes", https://learn.arm.com/learning-paths/servers-and-cloud-computing/distributed-inference-with-llama-cpp/how-to-2/ (`rpc-server -H 0.0.0.0`; relies on cloud security groups). Surfaced only: CVE aggregators (Averlon, Mondoo, Lutra, exploitdog), Seeed Studio Jetson wiki, fungies.io 2026 guide, AMD Ryzen AI Max+ article; other llama.cpp CVEs (CVE-2025-52566, CVE-2026-21869, CVE-2025-71439, CVE-2025-53630 / CVE-2026-27940, CVE-2025-49847) **unverified**.

**What they miss or get wrong.** Tutorials bind `rpc-server` to a LAN address or 0.0.0.0 and defer security to firewalls; the README's own warning is rarely quoted. No read page states what the protocol provides or lacks. No page contrasts tensor-level RPC (one model split over hosts; the only way to run a model larger than one machine) with routing a whole request to one machine (no split; the model must fit there).

**Covered by** `2026-10-31-loopback-rpc-vs-authenticated-transport` (claims `engine`, `transport`, `mesh-pair-choose`, `planned`, `device-sees-prompt`, `no-release`, `license`); it already records the CVE with the figures above. No new page. Keep it accurate when llama.cpp's README or the pinned build changes.

### 2.9 Sharing a GPU over the LAN securely (rank 9)

**Phrasings.** "share gpu over lan llm"; "llama.cpp server --api-key lan"; "secure ollama on home network"; "ollama reverse proxy authentication nginx caddy"; "llama-server https local network"; "per-user api keys local llm proxy"; "ollama security guide".

**What ranks (read).** llama.cpp server README (above): `--api-key`, "set an API key, put the server behind a reverse proxy" for public deployments. Serverman Tailscale guide (above). Twingate and Tailscale posts (above, vendor). Cisco Talos recommendations (above): API key or OAuth2, segmentation, rate limiting and logging. Surfaced only: smol-llm-proxy (PyPI), simplified.guide, domoticx.net (Caddy in front of `--api-key`), securityscientist.net Q&A.

**What they miss or get wrong.** The only documented authentication patterns are one shared bearer key or network membership. A shared key cannot be revoked for one device without rotating it for all and says nothing about who used it. No read page covers TLS on a LAN without a public domain name. Security vendors treat "exposed" as internet-only.

**Page UCompute can write.** *Why a shared API key is not device trust.* A table of four documented patterns, each in its own words: llama.cpp `--api-key` (one shared bearer key, default none); Ollama local API (no authentication, per its docs); VPN overlay membership (Tailscale / LM Link, per their pages); UCompute pairing (device keys pinned at pairing, QUIC with TLS 1.3, per-device revoke, audit line per off-device request without prompt or response). Columns: revoke one device without touching others; attribute a request to a device; encrypt on the LAN without a public certificate; work without a third-party account. Fill UCompute's column only from `transport`, `revocation`, `audit`, `audit-detail`, `local-only`, `mesh-pair-choose`; fill the others only from their quoted docs; never write "lacks". Claims: `transport`, `revocation`, `audit`, `audit-detail`, `local-only`, `mesh-pair-choose`, `device-sees-prompt`, `no-release`, `license`.

### 2.10 Revoking a device (rank 10)

**Phrasings.** "revoke device local ai"; "remove device from ai cluster"; "nvidia pair remove node"; "unpair device llm server"; "revoke api key ollama" (misdirected: only ollama.com account keys are revocable, per https://docs.ollama.com/api/authentication).

**What ranks (read).** NVIDIA PAIR README (leave, or any member removes the node; "forgetting to leave first is recoverable"). Vellum "Pair a device" (explicit revoke; distinguishes revoke from unpair and from stopping the tunnel). Ollama Authentication docs. Surfaced only: Oracle Content Management and a familyfi issue (both unrelated).

**What they miss.** Nothing explains what device revocation must do in a local-AI setting: whether in-flight work stops, refusal by key rather than by address, removal of key material, and whether the event is recorded.

**Covered mostly by** `2026-10-30-pairing-explainer` §revoke (signed record, close within 0.002 s to 0.061 s in four runs, refusal in the next handshake, no session resumption) and `2026-10-30-what-the-audit-log-records` (revocations copied to the security trail). A standalone short page is a runner-up, not a priority: claims `revocation`, `audit`, `audit-detail`, `mesh-pair-choose`. Registry rule: never say what the revoked device is told.

## 3. Mapping to the five ready pieces

| Ready piece | Cluster(s) served | Claims | Gap it leaves |
|---|---|---|---|
| `2026-10-30-pairing-explainer` | 5 (pairing), 10 (revoke), part of 2 | mesh-pair-choose, transport, revocation, local-only, device-sees-prompt, audit, connect-by-address, platforms, no-release, license | The how-to framing searchers in cluster 2 type |
| `2026-10-31-loopback-rpc-vs-authenticated-transport` | 8 (RPC) | engine, transport, mesh-pair-choose, planned, device-sees-prompt, no-release, license | None for its cluster; records CVE-2026-34159 |
| `2026-11-01-memory-fit-explainer` | 4 (fit), one sentence of 7 | catalog-fit, engine, platforms, no-release, license | The dedicated SHA-256 page |
| `2026-11-02-openai-client-base-url` | 3 (OpenAI clients) | openai-clients, run-local, local-only, device-sees-prompt, no-release, license | The exposure consequence (cluster 1) |
| `2026-10-30-what-the-audit-log-records` | supports 9 and 10 | audit, audit-detail, local-only, device-sees-prompt, mesh-pair-choose, no-release, license | Not a search entry point on its own |

Uncovered clusters: 1, 2 (how-to), 6, 7, 9.

## 4. The next five pages to write (ranked)

Ranking: inferred demand, gap size, evidence fit, and whether the page can be written entirely from existing registry rows today.

1. **What binding a local AI server to 0.0.0.0 actually exposes, and how to check yours in 60 seconds** (cluster 1). Writable today. Claims: `run-local`, `local-only`, `openai-clients`, `transport`, `mesh-pair-choose`, `device-sees-prompt`, `platforms`, `no-release`, `license`.
2. **Use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi** (cluster 2). Writable today; the only two-machine narrative allowed is the exact `demo-2026-10-19` text. Claims: `mesh-pair-choose`, `transport`, `local-only`, `audit`, `revocation`, `connect-by-address`, `windows-firewall`, `catalog-fit`, `device-sees-prompt`, `demo-2026-10-19`, `platforms`, `no-release`, `license`.
3. **Why a shared API key is not device trust** (cluster 9). Writable today from quoted docs plus registry rows. Claims: `transport`, `revocation`, `audit`, `audit-detail`, `local-only`, `mesh-pair-choose`, `device-sees-prompt`, `no-release`, `license`.
4. **What "verified" means in UCompute: SHA-256 against a pinned hash before the engine opens the file** (cluster 7). Writable today except two sentences (re-hash on load; mismatch UX) that need an Engineering answer and are omitted until then. Claims: `catalog-fit`, `engine`, `run-local`, `no-release`, `license`.
5. **Every network connection UCompute makes, and why** (cluster 6). Draft now, hold as `drafts/` until Engineering confirms the complete outbound list; the registry has no row for "no update check" or "these are the only hosts". Claims: `local-only`, `run-local`, `engine`, `catalog-fit`, `mesh-pair-choose`, `transport`, `planned`, `device-sees-prompt`, `no-release`, `license`.

Runners-up: a Windows firewall consent explainer (`windows-firewall`; already in `journal/STATE.md` next actions; serves the "ollama windows firewall 11434" phrasings in cluster 2); a standalone revoke page (cluster 10).

## 5. The name "UCompute": what appears today (recorded exactly)

### 5.1 Brand queries
- "UCompute" (standard search, 2026-10-30) returned, in order: Wikipedia "UTEC"; Wikipedia "Umtech"; Extreme Networks "universal compute platform latest documentation" (https://ca.extremenetworks.com/s_product_versions/universal-compute-platform-latest-documentation); Mobula "Universal Basic Compute" (https://mobula.io/asset/universal-basic-compute); CoinDesk UBC price page (https://www.coindesk.com/price/ubc); two University of York "compmat" bibliography pages (unconventional computing); AAU "Interactive HPC" UCloud webinar (https://www.researcher.aau.dk/webinar-get-started-with-ucloud-e152847); dute.org "utility computing"; CNX Software "uConsole". **Nothing from ucompute.org.** The tool's own summary: "The search didn't turn up anything called exactly 'UCompute.'"
- "ucompute.org" returned only unrelated university computing pages (TUM UCHPC, Lund COMPUTE, Iowa IT communities, UPC compute inventory, Waterloo UW HPC, dblp, CORDIS, ACM). **No result from the domain.** Google indexing status: **unverified** (not checked with Google or Search Console).
- "UCompute AI local inference mesh devices" returned MeshCompute (two repos), household-compute, saint0x/mesh, BaseRT (arXiv), Ken Ashe's Mesh LLM post, LocalMesh, Wikipedia pages; nothing about UCompute.
- "ucompute github OR u-compute OR ucomputing software" returned the JPMichon uCompute hardware repos, a "Ucomputer" GitHub account, two "UniCompute" repos, uplus-io/udb.
- "ucompute reddit OR hacker news OR producthunt OR twitter local AI" returned generic local-AI guides; no posts about UCompute found (Reddit not accessible; **unverified** there).
- Wikipedia "Umtech" read to rule out a collision: no mention of UCompute (https://en.wikipedia.org/wiki/Umtech).

### 5.2 Direct fetches
- https://ucompute.org (read 2026-10-30): live landing page titled "UCompute: the network is taking shape"; tagline "Compute better. Together."; three-stage roadmap (Now: local models on the user's own hardware, in development for macOS and Windows, not yet released; Next: connected trusted devices, with the October 2026 two-machine sentence; Later: an open layer, planned); a "Team preview" link; no download links, no GitHub links, no person or company named; footer "© 2026 UCompute project. Apache-2.0 licensed."
- https://preview.ucompute.org: HTTP 302 to a Cloudflare Access login; content not visible.
- https://github.com/ucompute: an organization with no bio, no public repositories, no public members. The LICENSE-only public repository referenced elsewhere in this workspace was not found at this location; its location is **unverified** by this research.

### 5.3 Collisions to track
| Collision | What it is | Where |
|---|---|---|
| **uCompute** (RP2040 hardware) | A hardware ecosystem by GitHub user JPMichon: RP2040_uCompute ("Plateforme de développement basé sur un RP2040"), uCompute_Rover (mentions "uComputeOS"), uComputeJr | https://github.com/JPMichon/RP2040_uCompute, https://github.com/JPMichon/uCompute_Rover, https://github.com/JPMichon/uComputeJr (surfaced; not read in full) |
| **Universal Compute Platform** | Extreme Networks product line | https://ca.extremenetworks.com/s_product_versions/universal-compute-platform-latest-documentation |
| **Universal Basic Compute (UBC)** | A crypto token (UCompute content must never be read as adjacent to it; `crypto`, `token` and `on-chain` are prohibited) | https://mobula.io/asset/universal-basic-compute, https://www.coindesk.com/price/ubc |
| "UCompute" component in uplus-io/udb | A planned distributed-computing component on a roadmap | https://github.com/uplus-io/udb (surfaced; not read) |
| "Ucomputer", "UniCompute" | GitHub account; two unrelated university HPC repos | https://github.com/Ucomputer (surfaced; not read) |
| UCloud, UCOMP, UTEC, Umtech | Danish research HPC; unconventional-computing abbreviation; Wikipedia neighbours | see §5.1 |
| **Mesh LLM** (for the word "Mesh") | github.com/Mesh-LLM/mesh-llm, ~3.7k stars, Apache-2.0, QUIC; its README says it "pools GPUs and memory across machines", the opposite of what UCompute Mesh does | https://github.com/Mesh-LLM/mesh-llm |
| MeshCompute (two repos), LocalMesh, saint0x/mesh | Peer-to-peer compute projects with similar vocabulary | https://github.com/mr-tbot/MeshCompute, https://github.com/Privateersmanvogue8510/MeshCompute, https://github.com/Ydde21/LocalMesh, https://github.com/saint0x/mesh |

### 5.4 Disambiguation wording for any public profile (recommendation)
Use the same first sentence everywhere (GitHub organization bio, any future directory listing, the site's meta description), so that search engines associate the name with one meaning:

> UCompute (ucompute.org): run small open AI models on your own computer, and pair your own devices so one can run a request for another. Each request runs whole on one device. In development; no public release yet. Apache-2.0; source not yet published. Not related to the uCompute RP2040 boards, Universal Compute products or any token.

Rules: always write "UCompute Mesh" as two words, never "Mesh" or "the mesh" alone, and put "each request runs whole on one device" in the same sentence or the next (`mesh-pair-choose`); never use "cluster", "pool", "distributed" or "network" as a noun for the product (prohibited, and they pull the name toward Mesh LLM and MeshCompute); never append ™ or (TM) (trademark clearance is open); keep "no public release yet" and "source not yet published" until the registry changes (`no-release`, `license`). The line maps to `run-local`, `mesh-pair-choose`, `no-release`, `license`; everything else in it is a negation of a collision, not a product claim.

## 6. Sources
All URLs above were read on 2026-10-30 unless marked "surfaced only" or **unverified**. The complete list of 48 read pages, 4 unreadable fetches and the surfaced-only titles is in `research/raw/search-demand.md` §15.
