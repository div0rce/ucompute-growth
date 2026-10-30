# Audiences

Internal. Research date: **2026-10-30**. Written from the five audience lenses in `research/raw/` (local-AI developers, multi-device developers, AI app builders, homelab and self-hosting, OSS infrastructure and researchers), `research/raw/adoption-barriers.md`, `research/raw/search-demand.md`, `research/raw/channels-platform-rules.md`, `research/COMPETITORS.md` and `research/POSITIONING.md`. Every market fact carries the URL its raw file read, or is marked **unverified**. Reddit was unreachable from the research tooling in every lens, so every Reddit figure and rule is third-party and **unverified against reddit.com**.

Product truth this file respects: development builds only; no public release, download, source publication, sign-in or cohort anyone can join [`no-release`, `private-alpha`, `license`]. Nothing in this file is an offer to try anything; "likelihood to try an unsigned development build" scores a future moment, when the owner authorizes one.

Where each audience gathers is summarised here and detailed in `distribution/COMMUNITIES.md` (being written by another writer from `research/raw/channels-platform-rules.md`; not yet present on 2026-10-30).

## 1. Scored matrix

Scale 1 (worst) to 5 (best) on each criterion; for friction, 5 means least friction. Scores are this file's judgement; the evidence column says what they rest on. Funnel stages used throughout: discovery, install, first workload, second device, repeat use (`research/raw/adoption-barriers.md` section 1).

| Audience | Reach at $0 | Fit with current evidence | Would try an unsigned development build | Path to second-device activation | Risk and compliance friction (5 = least) | Total |
|---|---|---|---|---|---|---|
| A. Multi-device developers and power users | 3 | 5 | 4 | 4 | 4 | **20** |
| B. Local-AI developers (run open models locally) | 4 | 3 | 3 | 3 | 3 | **16** |
| C. OSS infrastructure enthusiasts and researchers | 2 | 4 | 2 | 3 | 3 | **14** |
| D. AI app builders wanting a local OpenAI-compatible backend | 4 | 2 | 2 | 2 | 4 | **14** |
| E. Homelab and self-hosting | 3 | 2 | 1 | 2 | 2 | **10** |

Evidence behind each row:

- **A. Multi-device.** Reach 3: found in GitHub issue threads (ollama #4072, #19045, #8536, #1053; exo #1887, #2271, #952; open-webui #3526, #28601), Hacker News comment threads and personal blogs that re-derive the setup every few months (`research/raw/audience-multi-device-developers.md` section 6); no venue of its own; Reddit unread. Fit 5: pains 1 to 5 in that lens's table (open unauthenticated port, hard-coded IPs and failing discovery, account and hub dependency, remote model should look local, stale device access) map to built behaviour [`transport`, `connect-by-address`, `mesh-pair-choose`, `openai-clients`, `revocation`]. Try 4: they already hand-assemble `OLLAMA_HOST`, firewall rules and Tailscale (https://www.mykolaaleksandrov.dev/posts/2025/07/ollama-network-setup/, https://logarithmicspirals.com/blog/using-tailscale-to-access-private-llms/), so an OS warning is not their blocker; the macOS Sequoia Gatekeeper change still applies (https://developer.apple.com/news/?id=saqachfa). Second device 4: by definition two machines; discounted because the common second device is a phone (not built) or a Linux GPU box (processor only in tests) (`research/raw/audience-multi-device-developers.md` section 5, rows 8 to 10). Friction 4: GitHub participation is allowed with a disclosed identity; HN is human-only (https://news.ycombinator.com/newsguidelines.html).
- **B. Local-AI developers.** Reach 4: the largest pool: r/LocalLLaMA "861k members" (GummySearch, https://gummysearch.com/r/LocalLLaMA/, **unverified**), Hugging Face Discord 245,049 and Ollama Discord 194,368 (Discord invite API, `research/raw/audience-local-ai-developers.md` section 2.2), the HN thread with 648 points on whether the ecosystem needs Ollama (https://news.ycombinator.com/item?id=47788385); discounted because posting rules are strict and unverified. Fit 3: Run is table stakes against `llama serve` and Ollama (https://llama.app); the audience's first question is the second-device problem, which is Mesh (https://docs.ollama.com/faq, https://github.com/ollama/ollama/issues/3089); the pre-download memory verdict answers a declined request (https://github.com/ollama/ollama/issues/10920). Try 3: they accept an `xattr` bypass only with a published checksum and expect notarization (https://llmconfigurator.com/en/guides/troubleshooting/apple, https://github.com/janhq/jan/issues/224), and they ask "where is the code?" first (https://news.ycombinator.com/item?id=36802582). Second device 3: many own two machines but this lens is single-machine first. Friction 3: a 10% self-promotion guideline and a ban on LLM-generated copy are reported for r/LocalLLaMA (https://willitstay.com/r/LocalLLaMA, **unverified**); HN human-only.
- **C. OSS infra and researchers.** Reach 2: small; arXiv cs.DC and cs.CR, HN, other projects' Discords, which are not UCompute's channels (`research/raw/audience-oss-infra-and-researchers.md` section 3). Fit 4: they value an explicit threat model, protocol specifics, experimental labelling and losing cases (section 4 of that lens), all of which the ready pieces supply. Try 2: they build from source, and the source is unpublished; a LICENSE-only repository is the first comment (https://news.ycombinator.com/item?id=40973339). Second device 3: they own hardware and will test revocation and the audit log. Friction 3: HN human-only; arXiv fine; never announce in other projects' Discords.
- **D. AI app builders.** Reach 4: framework docs, the Hugging Face local-apps list, dev.to and Hashnode allow educational human-written posts now (https://dev.to/terms, https://hashnode.com/code-of-conduct). Fit 2: "change the base URL" is table stakes (https://github.com/openai/openai-python); the dominant 2026 use is fronting coding agents, which needs tool calling that UCompute has not yet verified (https://news.ycombinator.com/item?id=47651540); whether `/v1/responses` exists is **unverified** and Agents SDK users get 404s without it (https://openai.github.io/openai-agents-python/models/). Try 2: they need a stable backend and will ask "why not `llama serve`?" (https://llama.app). Second device 2: Mesh is a placement feature for them, not throughput. Friction 4: dev.to and Hashnode open for non-promotional posts; HN rules apply.
- **E. Homelab and self-hosting.** Reach 3: r/selfhosted "past 400K subscribers" (secondary, https://homenode.tech/r-selfhosted-summer-update-2025-flair-rules-analysis/, **unverified**), !selfhosted@lemmy.world 63.3K (https://lemmy.world/c/selfhosted), selfh.st "over 35,000 subscribers" (https://selfh.st/). Fit 2: 81% run Linux and "nearly nine out of ten" use Docker (https://linuxiac.com/self-hosters-confirm-it-again-linux-dominates-the-homelab-os-space/); UCompute has no Linux package, a processor-only daemon in tests and no container image; Home Assistant control needs models that support tools (https://www.home-assistant.io/integrations/ollama/). Privacy motivation fits (https://lemmy.world/api/v3/post?id=53242050). Try 1: a macOS build is invisible to a Linux server audience; awesome-selfhosted excludes desktop apps (https://raw.githubusercontent.com/awesome-selfhosted/awesome-selfhosted-data/master/CONTRIBUTING.md). Second device 2: their pattern is exactly server plus clients, but the server is Linux. Friction 2: Lemmy requires a 30-day-old account, a 10% cap and [AIP] disclosure (https://lemmy.world/post/48725669, https://lemmy.world/post/49151085); r/selfhosted reportedly requires "production ready" projects with docs (https://willitstay.com/r/selfhosted, **unverified**); awesome-selfhosted waits 4 months after a first tagged release; the Lemmy LocalLLaMA community bans comparing models to cryptocurrency, which the credits direction would trip (https://sh.itjust.works/api/v3/community?name=localllama).

## 2. Chosen audiences

**Primary: A. Multi-device developers and power users.** Top reason: UCompute Mesh's built behaviour answers their five best-documented pains, and the problem they describe ("use my desktop GPU from my laptop") is the one Mesh solves, with the whole-request limitation they already accept because they know splitting across unlike machines is slow (https://lemmy.world/post/47480176, https://github.com/ollama/ollama/issues/4643). The evidence for the problem is primary and recent: Ollama's maintainers have declined built-in authentication since 2023 (https://github.com/ollama/ollama/issues/1053, https://github.com/ollama/ollama/issues/8536), exo's discovery fails silently with no manual fallback (https://github.com/exo-explore/exo/issues/2271), and LM Link users ask for a transport that does not depend on one company (https://news.ycombinator.com/item?id=48625932). The positioning in `research/POSITIONING.md` (default-deny, prompt-free audit, pair-allow-audit-revoke) is written for this audience. Known gaps they will raise first: the strong machine sleeping (https://github.com/ollama/ollama/issues/4072), off-network access, Linux GPU, phones; each is stated, not hidden.

**Secondary: B. Local-AI developers.** Top reason: it is the pool the primary audience comes from and the venue where its vocabulary and its "why not Ollama or llama.cpp" test live; the pre-download memory-fit verdict and the pinned, credited engine are the two Run facts this audience can verify in a minute. It is also the audience with the largest reach once a human-posted account exists.

**Credibility audience, not a growth audience: C. OSS infra and researchers.** The threat-model and protocol content (pairing explainer, audit-log note, RPC comparison) is read here first and quoted elsewhere; it does not convert to installs quickly (prima.cpp has an ICLR paper and about 125 stars on its official repository, https://github.com/OpenCPIL/prima.cpp).

**Deferred: D. AI app builders** until tool calling is verified and the `/v1/responses` question is answered by Engineering; the one piece that serves them now is the base-URL page (`content/ready/2026-11-02-openai-client-base-url.md`). **Deferred: E. Homelab and self-hosting** until a Linux package with a GPU path and a container image exist; until then the only honest activity is listening and the 30-day participation clock, which requires an owner-created account (`journal/OWNER-ASKS.md` 3).

## 3. Audience profiles

Each profile: vocabulary; where they are; recurring questions (the community-answers bank is written from these); funnel stages with what Growth can offer today; what is unverified. "Today" means 2026-10-30: no channel is AUTHORIZED, nothing is downloadable, and the five ready pieces wait on the website handoff (`handoffs/2026-10-30-website-engineering-notes.md`).

### 3.1 A. Multi-device developers and power users (primary)

Who: people with a laptop and a stronger desktop, gaming PC or Mac mini who want the laptop to use the other machine's model; motives stated as privacy, API bills, using hardware they own, keeping laptop RAM and battery free (`research/raw/audience-multi-device-developers.md` section 2; examples https://aayushgarg.dev/posts/2026-03-29-local-llm-opencode/, https://dev.to/alichherawalla/how-to-use-a-remote-ollama-or-llamacpp-server-from-a-desktop-ai-app-on-windows-in-2026-40pa, https://ryanfleck.ca/2025/m4-mac-mini-llm-server/).

Vocabulary: `OLLAMA_HOST`, `0.0.0.0`, 11434, 1234, 8080; "Private profile" firewall rule; `setx`; Tailscale, tailnet, Tailscale Serve, `100.x.x.x`, MagicDNS; SSH tunnel `-L`; reverse proxy, bearer token; `.local` names, mDNS, Avahi; Wake-on-LAN, magic packet, "the GPU box sleeps"; "remote model looks local"; "point Claude Code / OpenCode / Open WebUI at a base URL"; LaunchDaemon, FileVault, `caffeinate`; "run inference on a separate machine". Search phrasings: "access ollama from another computer on local network", "use desktop gpu from laptop llm", "ollama tailscale remote access", "use my home gpu for ai from laptop" (`research/raw/search-demand.md` section 3).

Where they are (details in `distribution/COMMUNITIES.md`): GitHub issue threads that act as forums (https://github.com/ollama/ollama/issues/4072, https://github.com/ollama/ollama/issues/19045, https://github.com/ollama/ollama/issues/4643, https://github.com/exo-explore/exo/issues/2271, https://github.com/open-webui/open-webui/discussions/28601); Hacker News threads where the persona self-describes (https://news.ycombinator.com/item?id=48544986, https://news.ycombinator.com/item?id=48625932, https://news.ycombinator.com/item?id=44739632); personal blogs that re-derive the setup (https://logarithmicspirals.com/blog/using-tailscale-to-access-private-llms/, https://thundaxsoftware.blogspot.com/2026/08/building-private-local-llm-server-on.html, https://sidemini.com/blog/mac-as-always-on-llm-server/); r/LocalLLaMA and r/selfhosted (**unverified**, unread).

Recurring questions:
1. How do I reach the model on my desktop from my laptop without binding to 0.0.0.0 and opening a port to everyone on the Wi-Fi? (https://github.com/ollama/ollama/issues/8536; https://dev.to/john_182319291/ollama-has-no-api-authentication-how-to-properly-gate-port-11434-48e3)
2. Can a device on my network that I did not pair send prompts to my machine, or read answers? [`transport`, with its qualifier: tested with several instances on one computer, not yet between two machines]
3. Does my laptop just need the base URL, like LM Link's `localhost:1234`? (https://lmstudio.ai/link) [`openai-clients`, `mesh-pair-choose`]
4. Why can't my two devices see each other (guest or campus Wi-Fi, VLANs, Linux and Mac mDNS)? (https://github.com/exo-explore/exo/issues/1887, https://github.com/bjarneo/flux/issues/127) [`connect-by-address`; client isolation that blocks unicast is out of reach]
5. What happens when the strong machine sleeps mid-request? (https://github.com/ollama/ollama/issues/4072) Not addressed by current evidence; the honest answer is that it is a documented gap.
6. Does it work off my network, over Tailscale, from my phone? No relay or NAT traversal; no mobile; same local network only. Tailscale users can keep Tailscale for the away case; UCompute makes no claim there.
7. How do I remove a device, and what does revoke actually do? [`revocation`: connection closed in 0.002 s to 0.061 s in four runs, next request refused; never say what the revoked device is told] Parity with PAIR's documented node removal (`research/COMPETITORS.md`).
8. What does Windows ask me when I pair? [`windows-firewall`: a rule for its own program on private networks, administrator approval requested; shown on one laptop in October 2026]
9. Can the GPU box be Linux? Processor only in tests; Linux is planned, not supported [`platforms`, `mesh-pair-choose`].
10. What if the two machines run different versions? exo made peers silently invisible until October 2026 (https://github.com/exo-explore/exo/pull/2419); PAIR says all nodes should run the same version (https://docs.nvidia.com/local-ai/nvpair/getting-started/). UCompute's behaviour: **unverified**; no auto-update exists.
11. How is this different from PAIR, LM Link and Mesh LLM? Answer with `research/POSITIONING.md` section 4, parity stated as parity.
12. Is the audit log going to contain my prompts? [`audit`, `audit-detail`]

Funnel stages and what Growth can offer today:
- Discovery: the pairing explainer and the audit-log note (ready), a "use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi" page (to write; `research/raw/search-demand.md` section 13 item 2), honest answers in the GitHub threads above once a disclosed project account is authorized.
- Install: nothing. No download exists; installers are not signed or notarized. The only truthful statement is the development-build status [`no-release`].
- First workload: the base-URL page (ready) and the memory-fit explainer (ready), as reading.
- Second device: the pairing explainer with its "where this has run" list; the demo text [`demo-2026-10-19`] used verbatim.
- Repeat use: nothing to offer; sleep, version drift and no auto-update are stated gaps.

Unverified for this audience: Reddit presence and rules; whether a peer-unreachable or version-mismatch reason is surfaced; behaviour when a peer sleeps; the Ollama desktop app's network toggle and its version; any measured count of LAN-only exposure (`research/raw/audience-multi-device-developers.md` section 7).

### 3.2 B. Local-AI developers (secondary)

Who: developers who run open GGUF models on their own machine with Ollama, llama.cpp, LM Studio, Jan or KoboldCpp, judge tools by time-to-first-token on their hardware and by credit to upstream, and distrust cloud creep in local tools (`research/raw/audience-local-ai-developers.md` sections 1 and 4).

Vocabulary: GGUF, quants, Q4_K_M, "tok/s", TTFT, VRAM tiers, unified memory, `-ngl`, ctx-size, KV cache, chat template, llama-server, llama-swap, Metal, CUDA, ROCm, Vulkan, MLX; "OpenAI-compatible", `base_url`, `/v1`, `api_key` "required, but unused"; "notarized", `xattr`, quarantine flag, checksum; "phone home", telemetry; "just a wrapper"; "local AI", "open-weight". Search phrasings: "local llm openai compatible api", "gguf vram calculator", "does ollama phone home", "verify gguf sha256" (`research/raw/search-demand.md` sections 2, 9, 10, 11).

Where they are (details in `distribution/COMMUNITIES.md`): r/LocalLLaMA, r/LocalLLM, r/LLMDevs, r/ollama (tracker counts, https://gummysearch.com/r/LocalLLaMA/, **unverified**); Hugging Face, Ollama, LM Studio, Unsloth and Jan Discords (counts read from the invite API on 2026-10-30, `research/raw/audience-local-ai-developers.md` section 2.2); GitHub repositories they watch (https://github.com/ggml-org/llama.cpp, https://github.com/ollama/ollama, https://github.com/janhq/jan); Hacker News (https://news.ycombinator.com/item?id=47788385); Simon Willison's local-llms tag (https://simonwillison.net/tags/local-llms/) and It's FOSS Local AI Weekly (https://itsfoss.com/local-ai-weekly/), both relevant only once a public, reproducible build exists.

Recurring questions:
1. How do I use my other computer's GPU or RAM from my laptop? Two questions hide here: run on the big box and talk to it (what Mesh does) and split one model across machines (what Mesh does not do). (https://docs.ollama.com/faq, https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md)
2. Do my prompts leave my machine, and what outbound connections does the software make? (https://github.com/ollama/ollama/issues/2567, https://github.com/ollama/ollama/issues/14279) [`local-only` with "downloading a model or the engine uses the internet"; the complete connection list is a page to write]
3. Why does macOS say the app is damaged, is it notarized, where is the checksum? (https://github.com/janhq/jan/issues/224) Development builds are not notarized; say so.
4. How do I point my app or agent at the local endpoint, and does `tool_calls` return `arguments` as a string? (https://ollama.com/blog/openai-compatibility, https://github.com/ggml-org/llama.cpp/issues/20198) [`openai-clients`; tool calling is not yet verified]
5. Why not just llama-server, `llama serve` or Ollama; is this a wrapper? (https://news.ycombinator.com/item?id=47788385, https://llama.app) Answer: for one machine, llama.cpp's own server does what Run does and more; the distinct part is the paired-device policy layer and the pre-download verdict [`engine`].
6. Where is the code? [`license`: Apache-2.0, source not yet published]
7. Which model and quant fits my memory? [`catalog-fit`: size, license and fit verdict before download; estimates calibrated on Apple Silicon]
8. What tok/s do you get on your hardware? Only the registry figures, with model, hardware, build and "path check, not performance".
9. Linux? Planned; processor-only daemon in tests [`platforms`].
10. Why not llama.cpp RPC or exo to pool memory? Quote the RPC README's own warning and state that UCompute does not split a model (`content/ready/2026-10-31-loopback-rpc-vs-authenticated-transport.md`).
11. Does the installer ask for admin or set launch-at-login? (https://news.ycombinator.com/item?id=36802582) **Unverified** for UCompute's build; answer only from evidence.

Funnel stages and what Growth can offer today:
- Discovery: the RPC comparison note and the memory-fit explainer (ready); a "what binding a local AI server to 0.0.0.0 actually exposes, and a 60-second self-check" page (to write; `research/raw/search-demand.md` section 13 item 1); a "what verified means: SHA-256 before the engine opens the file" page (to write; item 5).
- Install: nothing downloadable; state the development-build status and, when a build exists, the exact OS dialog text and why.
- First workload: the base-URL page (ready).
- Second device: the pairing explainer (ready), with the two-questions framing from question 1 in its first paragraph.
- Repeat use: nothing yet.

Unverified for this audience: all subreddit counts and rules; YouTube channel figures (third-party); Windows SmartScreen reports on local LLM apps; whether UCompute's build asks for admin rights or sets launch-at-login; download resume behaviour (`research/raw/audience-local-ai-developers.md` section 7, `research/raw/adoption-barriers.md` section 6).

### 3.3 C. OSS infrastructure enthusiasts and distributed or edge-inference researchers (credibility)

Who: people who read READMEs, SECURITY.md files, advisories and arXiv cs.DC and cs.CR; they asked exo for benchmarks, a security model and a LICENSE on day one (https://news.ycombinator.com/item?id=40973339) and they publish losing cases (https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5/).

Vocabulary: threat model, trust boundary, attacker model; mTLS, raw public keys, ALPN, QUIC streams, handshake; pipeline parallelism, tensor parallelism, activations, memory-bandwidth bound, RDMA, interconnect; TPOT, TTFT, decode; "experimental", "proof-of-concept"; CVE, GHSA, CVSS; "verify weights against a known-good hash"; pre-registration, reproducibility; "volunteer compute", "untrusted peers".

Where they are (details in `distribution/COMMUNITIES.md`): arXiv cs.DC and cs.CR (https://arxiv.org/list/cs.DC/recent); Hacker News; GitHub issue threads such as https://github.com/ollama/ollama/issues/4643; other projects' Discords (exo, Petals, distributed-llama; never a UCompute announcement venue); EleutherAI's community (https://www.eleuther.ai/community/); newsletters that pick up technical reports with primary links (https://jack-clark.net/2025/04/21/import-ai-409-huawei-trains-a-model-on-8000-ascend-chips-32b-decentralized-training-run-and-the-era-of-experience-and-superintelligence/, https://latent.space/p/ainews-top-local-models-list-april/).

Recurring questions:
1. What is the threat model; what can a malicious paired device do; what is in and out of scope? [`transport`, `device-sees-prompt`: the device that runs your request processes your prompt] A public SECURITY.md and disclosure path for UCompute: **unverified**.
2. Why not partition? Answer with others' measurements: Apple's "pipeline parallelism does not speed up decode" (https://machinelearning.apple.com/research/mlx-distributed-inference), the mlx-optiq two-Mac regression (https://mlx-optiq.com/docs/cluster), the Ollama thread's two-machine slowdown on a fast link (https://github.com/ollama/ollama/issues/4643); concede that whole-request routing cannot run a model larger than the chosen device; cite prima.cpp as the state of the art for the deferred problem (https://arxiv.org/abs/2504.08791).
3. Where are tok/s and TTFT on named hardware, including the losing cases? Only registry figures with "path check, not performance"; a reproducible harness is a future artifact, not a claim.
4. Protocol specifics: what crosses the wire, which keys, what the handshake rejects? From the pairing explainer (Ed25519 device keys, QUIC with TLS 1.3 using raw public keys, both ways) [`transport`].
5. What does revoke do to the pinned key, and is a revoked device refused? [`revocation`; never say what the revoked device is told]
6. How does the pinned llama.cpp build move against upstream advisories? (https://github.com/ggml-org/llama.cpp/security/advisories) Update policy: **unverified**; the pin is b11609 per the ready RPC piece.
7. Where is the code and the license? [`license`]
8. Is "credits" a token? Direction only, not built, never in technical posts [`direction`, `planned`].
9. What exactly is in the audit log? [`audit-detail`]
10. Does any activation or partial state leave a device? None, because requests are not split [`mesh-pair-choose`]; the split-inference leakage and tampering papers do not apply by construction (https://arxiv.org/abs/2602.16760, https://arxiv.org/abs/2607.19490), said precisely and not as a marketing line.

Funnel stages and what Growth can offer today:
- Discovery: the three engineering notes (pairing, audit log, RPC comparison) as a threat-model-shaped set; a "why UCompute routes whole requests and does not split models" note (to write; `research/raw/audience-oss-infra-and-researchers.md` section 6.2).
- Install and first workload: nothing until source is published; a LICENSE-only repository is the first comment they will make.
- Second device: the demo text [`demo-2026-10-19`] and the pairing explainer's "where this has run" list.
- Repeat use: not applicable yet.

Unverified for this audience: Discord member counts for EleutherAI and Nous (search snippets); Mesh LLM's HN point count; whether UCompute will publish a SECURITY.md and a disclosure contact (`journal/OWNER-ASKS.md` 6 tracks a tested security contact); prima.cpp's full affiliation list (`research/raw/audience-oss-infra-and-researchers.md` section 9).

### 3.4 D. AI app builders wanting a local OpenAI-compatible backend (deferred)

Who: developers wiring Vercel AI SDK, LangChain, LlamaIndex, the OpenAI Agents SDK, CrewAI, LiteLLM, Zed, Continue or Open WebUI to a local server, mostly to front coding agents without API cost (`research/raw/audience-ai-app-builders.md` sections 1.1 and 1.2).

Vocabulary: `base_url` / `baseURL` / `OPENAI_BASE_URL`; "dummy API key"; `createOpenAICompatible`, `maxRetries: 0`; `OpenAILike(api_base=...)`; `set_default_openai_api("chat_completions")`; Responses API vs Chat Completions; "silently ignored parameters", "assert on the response body"; `num_ctx`, context window default; `/props`; embeddings; "drop-in replacement"; "is it really local?".

Where they are (details in `distribution/COMMUNITIES.md`): framework provider docs (https://ai-sdk.dev/providers/openai-compatible-providers/lmstudio, https://zed.dev/docs/ai/use-a-local-model.md, https://docs.continue.dev/customize/model-providers/more/llamacpp, https://docs.openwebui.com/alternatives/lm-studio.md, https://docs.litellm.ai/docs/providers/openai_compatible); the Hugging Face local-apps list (https://huggingface.co/docs/hub/local-apps, PR path https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/src/local-apps.ts; post-release only); community lists (https://github.com/janhq/awesome-local-ai; post-source only); Hacker News (https://news.ycombinator.com/item?id=47651540); dev.to and Hashnode for educational posts now (https://dev.to/terms, https://hashnode.com/code-of-conduct).

Recurring questions:
1. What is the base URL, the port and the placeholder key? [`openai-clients`: official Python and JavaScript clients, only the base URL changes; the ready page names 127.0.0.1:8192]
2. Which OpenAI parameters are honoured, ignored or rejected? Ollama publishes its list (https://docs.ollama.com/api/openai-compatibility); UCompute's list: **unverified**, a page to draft with Engineering.
3. Is there `/v1/responses`? **Unverified**; Agents SDK and Codex users 404 without it (https://openai.github.io/openai-agents-python/models/, https://lmstudio.ai/docs/app/api/endpoints/openai).
4. Does tool calling work, and with which chat templates? Not yet verified; say so before any agent-wiring guide.
5. What is the default context window and does the server expose model metadata? **Unverified**.
6. Embeddings? **Unverified**.
7. Why not `llama serve` or Ollama, and is llama.cpp credited? (https://llama.app, https://news.ycombinator.com/item?id=44003741) [`engine`]
8. How many concurrent requests? **Unverified**.
9. Will the model fit, and what happens if not? [`catalog-fit`]
10. Is it really local by default, or does a default require a cloud key? (https://news.ycombinator.com/item?id=46930391) [`run-local`: no account and no UCompute service]

Funnel stages and what Growth can offer today:
- Discovery: educational, non-promotional posts allowed now on dev.to and Hashnode, written by a person with AI assistance disclosed where used, such as how each framework sets a base URL and why a placeholder key is still needed (`research/raw/audience-ai-app-builders.md` section 7.1 item 6); requires an owner-created account (`journal/OWNER-ASKS.md` 3).
- Install: nothing.
- First workload: the base-URL page (ready).
- Second device: not their question; Mesh is placement, not throughput.
- Repeat use: nothing.

Unverified for this audience: everything in questions 2, 3, 5, 6 and 8, flagged for Engineering; r/LocalLLaMA rules (third-party); Ollama's "8.9 million developers every month" (company figure via TechCrunch, https://techcrunch.com/?p=3140214).

### 3.5 E. Homelab and self-hosting (deferred)

Who: Linux-first operators running one GPU box in Docker or LXC on Proxmox, Unraid or TrueNAS, serving llama.cpp or Ollama behind Open WebUI, reached over Tailscale or WireGuard, often feeding Home Assistant (https://linuxiac.com/self-hosters-confirm-it-again-linux-dominates-the-homelab-os-space/, https://lemmy.world/api/v3/comment/list?post_id=53242050&sort=Top&limit=40&max_depth=2, https://www.xda-developers.com/self-hosted-ollama-proxmox-lxc-uses-amd-gpu/).

Vocabulary: Proxmox, LXC, GPU passthrough, `/dev/kfd`, ROCm; Docker, compose, Unraid template, TrueNAS app, `OLLAMA_ORIGINS`; Open WebUI; Tailscale, WireGuard, VPS forward; Home Assistant, "exposed entities", voice assistant; "the name of the game is VRAM"; "you cannot scale horizontally for speed"; [CBH], [AIP], [AIT] tags; "production ready and have docs".

Where they are (details in `distribution/COMMUNITIES.md`): !selfhosted@lemmy.world (https://lemmy.world/c/selfhosted) and !localllama@sh.itjust.works (https://sh.itjust.works/api/v3/community?name=localllama); r/selfhosted, r/homelab, r/LocalLLaMA (**unverified**, unread); selfh.st weekly and its Submit Content form (https://selfh.st/, https://selfh.st/submit/); the Home Assistant community forum (https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860); awesome-selfhosted, TrueNAS and Unraid catalogs (post-release, container image required; https://apps.truenas.com/catalog/open-webui_community/, https://ca.unraid.net/apps/open-webui-0z497h31ntbiab); Mastodon #selfhosted and #homelab (https://selfh.st/about/).

Recurring questions:
1. Is there a Linux build, a Docker image, a Proxmox LXC guide, GPU passthrough? No package; processor-only daemon in tests; Linux planned [`platforms`].
2. Does it control Home Assistant? Needs models that support tools (https://www.home-assistant.io/integrations/ollama/); UCompute's tool calling is not yet verified.
3. Can I link two boxes to go faster? No; each request runs whole on one device; they already know Ethernet-linked inference is not faster (https://lemmy.world/post/47480176).
4. Does it phone home; what are the connections? [`local-only`, downloads use the internet]
5. Can I reach it from my phone over Tailscale or WireGuard? Same local network only; no relay; no mobile.
6. Is "credits" crypto? Direction only; the sh.itjust.works community forbids the comparison, so do not raise it there [`direction`].
7. Where is the source and the license? [`license`]
8. Which quant, and is llama.cpp exposed honestly rather than abstracted? (https://lemmy.world/api/v3/post?id=20828515) [`engine`, `catalog-fit`]
9. My IoT or voice hardware is on a separate VLAN; can paired devices still connect? [`connect-by-address`, with its scope: shown between one Mac and one Windows laptop on one campus network]
10. Is it in awesome-selfhosted, TrueNAS or Unraid? No; awesome-selfhosted waits 4 months after a first tagged release and excludes desktop apps.

Funnel stages and what Growth can offer today:
- Discovery: listening only; the audit-log note (ready) is the one piece that speaks to their stated privacy motive. Account creation for the 30-day participation clock is an owner action.
- Install, first workload, second device, repeat use: nothing honest to offer until a Linux daemon with a GPU path and a container image exist.
- Timing: the 2026 selfh.st survey adds an AI section, closes 31 October 2026 and publishes in early November (https://selfh.st/survey/2026-open/); re-read this audience then.

Unverified for this audience: every Reddit rule and count (willitstay mirror); r/homelab rules (no source); the Self-Hosted podcast's status after episode 150 (https://selfhosted.show/); whether UCompute's Windows and macOS builds mean anything to a Linux-server operator beyond "not for my server" (`research/raw/audience-homelab-selfhosting.md` section 8).

## 4. Cross-audience barriers that no message fixes

From `research/raw/adoption-barriers.md`: unsigned and un-notarized installers block the install stage for everyone (Sequoia removed the Control-click override, https://developer.apple.com/news/?id=saqachfa; Smart App Control has no per-app bypass, https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003); "verify it yourself" trust needs published source; sleep, version drift and no auto-update hurt repeat use. Growth's job while these stand is readiness: content that passes the lint, variant texts for X-02 and X-04 (`research/POSITIONING.md` section 7), and honest answers to the questions above.

## 5. Change record

- 2026-10-30: file created from the five audience lenses, adoption barriers, search demand and platform rules. Primary audience: multi-device developers; secondary: local-AI developers; credibility: OSS infra and researchers; deferred: AI app builders (tool calling, Responses API) and homelab (Linux package, container image). Re-score when: a channel is AUTHORIZED, source is published, a signed build exists, tool calling is verified, a Linux package ships, or the 2026 selfh.st survey results publish.
