# Audience research: developers who run open LLMs locally

Lens: `audience-local-ai-developers`
Date of research: 2026-10-30
For: UCompute internal strategy repository
Status of UCompute at time of writing: Apache-2.0, source not yet published, no public release, private macOS Apple Silicon alpha behind access control. Nothing below should be read as a claim that UCompute "supports" any platform.

## 0. Method and limits

- Tools: WebSearch (standard and extended), WebFetch on primary pages, the Discord public invite API (`discord.com/api/v9/invites/<code>?with_counts=true`) for member counts, and the GitHub issue-search API for issue titles/comment counts. 45 distinct pages or API responses were read; every URL is in the Sources section.
- **Reddit was not reachable from this tooling.** `www.reddit.com`, `old.reddit.com` and reddit-scoped web search were all refused, and a Reddit JSON request via shell was denied by the permission layer and not retried. Consequences:
  - Subreddit sizes come from GummySearch, a third-party tracker that states its own "last updated" date. They are **unverified against Reddit itself**.
  - No Reddit thread was read directly. Recurring questions are evidenced from GitHub issues, Hacker News threads, official docs and FAQs, and two third-party syntheses of r/LocalLLaMA. Where a claim is about "what Reddit says", it is labelled as second-hand.
  - A public dataset of ~101k r/LocalLLaMA posts (2023-04 to 2026-03) exists on Hugging Face and could be analysed offline for exact phrasing; that was not done here.
- YouTube pages did not render counts; subscriber numbers come from vidIQ (third-party, dated) and are marked **unverified**.
- "Last 6 months" = roughly May to October 2026. Several of the recurring questions are documented in issues from 2023-2024 that are still the canonical answer; where that is the case the report says so instead of pretending the evidence is recent.

## 1. Executive summary

1. The audience is large and concentrated in a handful of venues: r/LocalLLaMA (~861k per tracker), Hugging Face Discord (245k), Ollama Discord (194k), r/LocalLLM (~253k), r/LLMDevs (~178k), r/ollama (~142k), LM Studio Discord (80k), Unsloth Discord (41k), Jan Discord (21k). GitHub star counts of the runners they watch: Ollama 185k, Open WebUI 157k, llama.cpp 133k, vLLM 96k, exo 48k, Jan 45k.
2. "Use my other computer's GPU from my laptop" is really two questions. The common, working one is "run the server on the big box, point the laptop at it" (Ollama `OLLAMA_HOST`, Tailscale, firewall port 11434). The rarer one is "split one model across two machines" (llama.cpp RPC, exo), which the community already knows is slower than one box and is documented by llama.cpp itself as "fragile and insecure." UCompute Mesh's "whole request on one device" is the first thing, and the messaging must say so explicitly or it will be read as the second.
3. Prompt privacy is a live anxiety, and it has shifted: the 2024 question was "does Ollama phone home?" (answer: only an update check). The 2026 question is "my local tool grew cloud features; where do my prompts go now?" (Ollama cloud models, Qwen3.5 routing). A tool that is local-only by default and says exactly which outbound calls it makes fits the moment.
4. Exposure, not just privacy, is now the headline: a SentinelOne/Censys study published 2026-01-29 found ~175,000 publicly reachable Ollama hosts and documented resale of hijacked compute ("LLMjacking"). Pinned device keys, TLS 1.3, local-only default and instant revoke are directly relevant and should be described in those terms.
5. Unsigned macOS apps get the "damaged / Apple cannot check it for malicious software" dialog; the community accepts an `xattr` bypass only if a checksum is published, and notarization is the expected fix (Jan notarized within ten days of the bug report in 2023). Installers that ask for admin rights or set launch-at-login get called out publicly.
6. The OpenAI-compatible endpoint is table stakes and has a fixed vocabulary: `base_url="http://localhost:<port>/v1"`, `api_key="..." # required, but unused`. Strict compatibility matters: in March 2026 llama-server broke the official `openai` SDK by returning `tool_calls.arguments` as an object instead of a string, and the issue was reverted within a day. UCompute's unverified tool calling should be stated plainly.
7. Proof that convinces: works within a minute of reading the README; tokens/sec on named hardware with model and quant named; visible credit to llama.cpp; standard GGUF files the user can reuse; open source; real-task results over benchmark scores. Dismissal triggers: "just a wrapper" with no upstream credit, hidden defaults, hidden model storage, cloud/monetization creep, admin prompts, single-benchmark claims, marketing adjectives without numbers.

## 2. Where they gather

Sizes are only those read on a page or returned by a public API; the URL and read date are given for each.

### 2.1 Reddit (third-party tracker numbers, unverified against Reddit)

| Subreddit | Members (GummySearch) | Yearly growth shown | Tracker "last updated" | Source |
|---|---|---|---|---|
| r/LocalLLaMA | "861k members" | "+307k members (55.6%)" | Oct 28, 2026 | https://gummysearch.com/r/LocalLLaMA/ |
| r/LocalLLM | "253k members" | "+162k members (178.7%)" | Oct 26, 2026 | https://gummysearch.com/r/LocalLLM/ |
| r/LLMDevs | "178k members" | "+62k members (53.5%)" | Oct 28, 2026 | https://gummysearch.com/r/LLMDevs/ |
| r/ollama | "142k members" | "+54k members (60.7%)" | Oct 29, 2026 | https://gummysearch.com/r/ollama/ |

Notes from the same tracker pages: on r/LocalLLaMA the most common flairs in the sampled window were "Discussion" (24), "Resources" (19), "New Model" (14) and "Question | Help" (13); the top topic tags were Ai, Llm, Local, Model, Coding, then Tool, Gpu, Agent, Qwen. On r/ollama the sampled "Advice" example was "Best Coding Model for Ryzen9/4060/64 GB Notebook?" and a "Bug Report" example was "Qwen2.5-Coder 7B outputs tool calls as text in OpenCode", which is the hardware-plus-model-plus-agent-tool shape of question this audience asks.

A third-party synthesis of the r/LocalLLaMA "Best Local LLMs – Apr 2026" megathread reports that single thread at 575 upvotes and 311 comments and calls it "the most active local-AI thread on the internet" (https://bigguyonstuff.com/best-local-llm-2026-megathread-synthesis/; secondary source).

Public dataset for offline analysis: `pszemraj/LocalLLaMA-posts`, about 101k rows, `created` from 2023-04-01 to 2026-03-04, columns include title, selftext, score, permalink (https://huggingface.co/datasets/pszemraj/LocalLLaMA-posts). Example titles visible: "What to pair with 3080TI for Qwen 3.5 27b?", "Apple M5 Pro & M5 Max just announced. Here's what it means for local AI".

### 2.2 Discord (counts from Discord's public invite API, read 2026-10-30)

| Server | Members | Online at read time | Server description (verbatim) | Source |
|---|---|---|---|---|
| Hugging Face | 245,049 | 12,900 | "We're working to democratize good machine learning" | https://discord.com/api/v9/invites/hugging-face-879548962464493619?with_counts=true |
| Ollama | 194,368 | 12,732 | (none) | https://discord.com/api/v9/invites/ollama?with_counts=true |
| LM Studio | 79,743 | 6,927 | "LM Studio Community - Discover, download, and run LLMs on your computer" | https://discord.com/api/v9/invites/lmstudio?with_counts=true |
| Unsloth AI | 41,497 | 4,694 | "The place for local AI, open-source LLMs, fine-tuning, and Unsloth." | https://discord.com/api/v9/invites/unsloth?with_counts=true |
| Jan | 20,589 | 1,530 | "Jan is building Open Superintelligence. The best of open-source AI in an easy-to-use product." | https://discord.com/api/v9/invites/FTk2MvZwJH?with_counts=true |

The Jan invite code `FTk2MvZwJH` is the one listed in the janhq/jan README "Links" section (https://github.com/janhq/jan). llama.cpp has no official Discord that I could find; its community lives in GitHub Discussions and r/LocalLLaMA (unverified absence).

### 2.3 GitHub repositories they watch (star counts read 2026-10-30)

| Repo | Stars | Forks | One-line description (verbatim) | Source |
|---|---|---|---|---|
| ollama/ollama | 185.3k | 18.7k | "Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models." | https://github.com/ollama/ollama |
| open-webui/open-webui | 157.2k | 22.9k | "User-friendly AI Interface (Supports Ollama, OpenAI API, ...)" | https://github.com/open-webui/open-webui |
| ggml-org/llama.cpp | 132.8k | 24.9k | "LLM inference in C/C++" (12,005 commits; README quick start: "Launch OpenAI-compatible API server"; backends table lists "RPC") | https://github.com/ggml-org/llama.cpp |
| vllm-project/vllm | 95.9k | 24.2k | "A high-throughput and memory-efficient inference and serving engine for LLMs" | https://github.com/vllm-project/vllm |
| exo-explore/exo | 48.1k | 3.6k | "Run frontier AI locally." README: devices "automatically discover each other - no manual configuration"; "Currently, exo runs on CPU on Linux" | https://github.com/exo-explore/exo |
| janhq/jan | 45.2k | 3.1k | "Jan is an open source alternative to ChatGPT that runs 100% offline on your computer." Local server at `localhost:1337`; "bundled llama.cpp engine" | https://github.com/janhq/jan |
| LostRuins/koboldcpp | 12.1k | 805 | "KoboldCpp - Run GGUF AI models locally with a KoboldAI UI. One File. Zero Install." OpenAI-compatible API at `http://localhost:5001/v1` | https://github.com/LostRuins/koboldcpp |
| mostlygeek/llama-swap | 6.1k | 529 | "Reliable model swapping for any local OpenAI/Anthropic compatible server - llama.cpp, vllm, etc" | https://github.com/mostlygeek/llama-swap |

LM Studio's desktop app is not open source; its community presence is the Discord above and the `lmstudio-ai/lmstudio-bug-tracker` issue tracker (seen via GitHub search; not read in full).

### 2.4 Hacker News

- "The local LLM ecosystem doesn't need Ollama": 648 points, 207 comments, about 6 months old at read time (https://news.ycombinator.com/item?id=47788385). The single richest primary source on what this audience values and resents; see section 4.
- "Show HN: Ollama – Run LLMs on your Mac" (2023-07-20): 284 points, 94 comments (https://news.ycombinator.com/item?id=36802582). Useful as a template of first-contact questions.
- Show HN posts about local LLM tools are frequent; one from October 2026 (a macOS voice assistant) drew a commenter asking for OpenAI-compatible local endpoints so it could work with "a bare llama.cpp server" (search snippet; the thread itself was not read, so unverified).

### 2.5 YouTube (third-party stats, unverified)

| Channel | Subscribers | Videos | Date of stat | Notes | Source |
|---|---|---|---|---|---|
| Alex Ziskind (@azisk) | 578K (578,000) | 1,229 | Oct 29, 2026 | Recent titles are almost entirely local-AI hardware: "Llama Cpp Flags That Instantly Speed It Up" (Sep 18, 2026), "DGX Spark Dell GB10 2 Node Cluster" (Oct 17, 2026), "This Laptop Beat My DGX Spark... Then I Unplugged It" (Oct 23, 2026), "It Begins... Local AI and the Cloud Start Sharing" (Oct 20, 2026), "M5 Ultra vs 2 DGX Sparks" (Oct 1, 2026) | https://vidiq.com/youtube-stats/channel/@azisk/videos/ |
| Matt Williams / Technovangelist (ex-Ollama) | 96.3K | 501 | Oct 28, 2026 | Top titles: "Optimize Your AI - Quantization Explained", "Is Open Webui The Ultimate Ollama Frontend Choice?", "How to run Ollama on Docker" | https://vidiq.com/youtube-stats/channel/@technovangelist/ |

Not verified: a channel named "Local LLM" (@myLocalLLM) that appeared in search results describing itself as a hub for local AI tutorials; no count was read.

### 2.6 Blogs and newsletters

- Simon Willison's `local-llms` tag: 165 posts, described as "LLMs that can run on consumer hardware like laptops or mobile phones"; recent posts include "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things" (Aug 16, 2026) and a quote from Georgi Gerganov on local models and coding agents (Jun 16, 2026) (https://simonwillison.net/tags/local-llms/). This is the single most-cited independent blog for this audience; a tool mentioned there gets read.
- It's FOSS "Local AI Weekly": weekly, Wednesdays, separate opt-in from FOSS Weekly; the author says they prefer replicable setups to benchmark charts and tests on home hardware (ZimaCube with an Nvidia Ada GPU, Raspberry Pi with AI HAT, a Zenbook with an NPU) (https://itsfoss.com/local-ai-weekly/). No subscriber count shown.
- Technovangelist Substack: search snippet said "over 1,000 subscribers"; page not read, **unverified**.
- Seen in search results only, not read, unverified: "Concorde Weekly" (Buttondown, Munich self-hosting), llm-stats.com weekly email, Latent Space (cited as a source by the megathread synthesis).

## 3. Recurring questions

### 3.1 "How do I use my other computer's GPU / RAM from my laptop?"

Two different questions hide under this phrasing. The evidence shows the community treats them very differently.

**(a) Run the model on the big machine, talk to it from the laptop.** This is the common case and it works today; the friction is networking and security, not inference.

- Ollama binds to `127.0.0.1:11434` by default; the official FAQ entry is literally titled "How can I expose Ollama on my network?" and the answer is `OLLAMA_HOST` (https://docs.ollama.com/faq). The FAQ also has entries for ngrok and Cloudflare Tunnel.
- The canonical bug report is "Error when requesting ollama api from another pc (windows)" (2024-03-13): requests to the remote IP got no reply; fix was `OLLAMA_HOST=0.0.0.0`, the firewall turned out not to be the cause, and three users reported the same thing in two days (https://github.com/ollama/ollama/issues/3089). A related issue, "MacOS Ollama not binding to 0.0.0.0", has 43 comments (seen in GitHub search results, body not read).
- Guides written in 2026 still answer the same question. One (about February 2026) walks through `OLLAMA_HOST=0.0.0.0:11434`, `OLLAMA_ORIGINS=*`, a firewall rule for TCP 11434, `curl http://<ip>:11434/api/tags` from the other PC, and warns: binding to 0.0.0.0 exposes every interface, do not forward 11434 on the router, "Ollama has no built-in authentication" (https://www.blackmoreops.com/how-to-access-ollama-from-another-pc-on-your-local-network/). Another (about April 2026) recommends Tailscale, binding `OLLAMA_HOST` to the Tailscale `100.x.x.x` IP rather than 0.0.0.0, verifying with `ss -tlnp | grep 11434`, and says if an external curl gets a response to "Treat this as an active security incident" (https://www.serverman.co.uk/ollama/ollama-tailscale-remote-access/).
- Scale of the mistake: SentinelOne (SentinelLABS) and Censys reported about 175,000 unique publicly reachable Ollama hosts in 130 countries, a little over 30% in China, described as an "unmanaged, publicly accessible layer of AI compute infrastructure"; Pillar Security documented an operation that scans for unauthenticated Ollama, vLLM and OpenAI-compatible endpoints and resells access; the researchers say LLM endpoints "must be treated with the same authentication, monitoring, and network controls" as other exposed infrastructure (The Hacker News, 2026-01-29, https://thehackernews.com/2026/01/researchers-find-175000-publicly.html).

**(b) Split one model across two machines ("pool VRAM").** Possible, niche, and known to be slow and insecure.

- llama.cpp's RPC backend was merged 2024-05-14 (PR #6829, "ggml : add RPC backend"); it "proxies all backend operations to a remote server" and splits layers across hosts (https://github.com/ggml-org/llama.cpp/pull/6829).
- The current RPC README says the backend is "proof-of-concept development stage", "the functionality is fragile and insecure", and in bold: "Never run the RPC server on an open network or in a sensitive environment!" Usage is `--rpc 192.168.88.10:50052,192.168.88.11:50052`; default port 50052 (https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md).
- Measured cost, same model on one box vs split over 10 GbE (M2 Ultra 128 GB host + GB10 "DGX Spark" remote, 9.41 Gbps measured): Qwen2.5-72B Q4_K_M generation 11.1 tok/s local vs 5.9 tok/s over RPC; Qwen2.5-7B Q4_K_M 91.8 vs 52.7 tok/s. The README attributes it to per-token round trips, notes the RPC protocol "isn't versioned, so mismatched builds can cause silent failures or crashes", and has no security section (https://github.com/kjaiswal/llama-cpp-distributed-benchmarks).
- An independent comparison (published 2026-02-26, updated 2026-04-23; author's own hardware, unverified) of Llama 3.1 70B 4-bit on two RTX 3090s in separate boxes: llama.cpp RPC 6.1 tok/s over 2.5 GbE (2.8 on 1 GbE, 7.4 on 10 GbE) vs 14.2 tok/s with both GPUs in one box; exo 4.3 tok/s; Petals 0.9 tok/s. It states llama.cpp RPC "has no authentication by default" (https://localaimaster.com/blog/distributed-inference-local-ai).
- exo (48.1k stars) is the consumer-friendly version of (b): automatic discovery, splits models "larger than would fit on a single device", macOS app requires Apple silicon and macOS 15.1+, and "Currently, exo runs on CPU on Linux" (https://github.com/exo-explore/exo).
- A 2024 llama.cpp Q&A thread on RPC across two AMD clusters shows the experimentation vocabulary (`--rpc`, `-ngl`, `--mem`, row split, `GGML_RPC`, RDMA, `llama-bench`) and the failure modes (GPU hangs, backend count assertion) (https://github.com/ggml-org/llama.cpp/discussions/9257).

**Implication for UCompute (analysis, not a source claim).** Mesh is case (a) with the networking and security solved: short-code pairing instead of `OLLAMA_HOST`/firewall/Tailscale, pinned keys and TLS 1.3 instead of an open port, local-only by default, revoke. That is a real and documented pain. But the words "mesh", "together" and "compute" make people hear case (b). Every description of Mesh should carry the sentence "the whole request runs on one device; this is not pooling or splitting a model", and should cite the RPC README's own warning when asked "why not just use llama.cpp RPC?".

### 3.2 "Do my prompts leave my machine?"

- The 2024 version: "Clarify abou Telemetry" (2024-02-17): "Please clarify what this data is and where it is sent to"; the reporter had seen periodic traffic to Cloudflare IPs. A maintainer answered that the only outgoing call is the auto-update check in `app/lifecycle/updater.go`, which sends OS and architecture, and that Ollama does not track user data or input. A later commenter (Oct 2024) was unconvinced and told users to monitor outgoing connections themselves. No opt-out was added (https://github.com/ollama/ollama/issues/2567).
- Official position today: FAQ entry "Does Ollama send my prompts and answers back to ollama.com?": "Ollama runs locally. We don't see your prompts or data when you run locally." Cloud models: "we process your prompts and responses to provide the service but do not store or log that content". A separate FAQ, "How do I disable Ollama's cloud features?", documents `OLLAMA_NO_CLOUD=1` (https://docs.ollama.com/faq).
- The 2026 version of the anxiety is about local tools acquiring cloud paths: issue "Qwen3.5-397B-A17B Cloud data retention and privacy concerns" (2026-02-16) asks whether Ollama Cloud routes to Alibaba's API, argues the "Keep your data private" wording is incomplete without that answer, and the thread closed in June 2026 with no direct maintainer answer; the reporter's framing was "If this wasn't an issue it would be clear in the docs." (https://github.com/ollama/ollama/issues/14279).
- The HN thread lists "monetization" (cloud services, a closed GUI) as a reason commenters now distrust Ollama (https://news.ycombinator.com/item?id=47788385).
- Two more issue titles seen in GitHub search (bodies not read): "Ollama's privacy policy" (2025-07) and "Auto-Start of ollama without permisson" (2026-10-16).

**Implication.** The audience wants: a plain list of every outbound connection the software makes and why (they will packet-capture it), a hard local-only mode that is the default, and no silent cloud path. UCompute's "local-only mode refuses every off-device request by default" and "audit logs record off-device requests without prompt text" are the right shape; publish the outbound-connection list (model download hosts, nothing else) as a document, not a sentence.

### 3.3 "Why does macOS say the app is damaged?" (unsigned / un-notarized apps)

- Jan, 2023-09-29: "Jan cannot be opened because Apple cannot check it for malicious software"; workaround right-click > Open; fixed by notarization ("Finished. Our app is notarized", 2023-10-06), closed 2023-10-09 (https://github.com/janhq/jan/issues/224).
- A local-LLM troubleshooting guide lists the dialog "'LM Studio' is damaged and can't be opened. You should move it to the Bin." and says most local-AI tooling is small open-source work without a paid certificate, so "Gatekeeper reports them as damaged when they are merely unsigned"; the `xattr` bypass is "safe if you verify the download first and reckless if you do not" (https://llmconfigurator.com/en/guides/troubleshooting/apple).
- Installer behaviour is judged too: in the original Show HN the installer asking for administrator access to create a CLI symlink and setting itself to launch at login drew criticism and an apology from the maintainer (https://news.ycombinator.com/item?id=36802582).
- Windows: a third-party llama.cpp manager's release notes state the binary is unsigned so SmartScreen will warn until a signing certificate is in place (search snippet; page not read, **unverified**). No GitHub issue about SmartScreen on koboldcpp, llama.cpp or LM Studio was found.
- Recent LM Studio bug-tracker titles show the next level of scrutiny: "MacOS app modifies or removes sealed resources inside its signed bundle after first launch" (2026-06-29) and "macOS resource seal" (2026-08-17) (seen in GitHub search; bodies not read).

**Implication.** For the alpha and any later build: sign and notarize, publish SHA-256 for the app the same way UCompute already does for models, never ask for admin, never set launch-at-login without asking. The audience has an explicit norm here and a vocabulary ("notarized", "xattr -cr", "quarantine flag", "checksum").

### 3.4 "How do I point my app/agent at a local OpenAI-compatible endpoint?"

- The canonical snippet comes from Ollama's 2024-02-08 blog post: `OpenAI(base_url='http://localhost:11434/v1', api_key='ollama', # required, but unused)` in Python and `baseURL`/`apiKey: 'ollama', // required but unused` in JS (https://ollama.com/blog/openai-compatibility).
- Every runner now exposes `/v1`: LM Studio at `http://localhost:1234/v1` with `/v1/models`, `/v1/chat/completions`, `/v1/responses`, `/v1/embeddings`, `/v1/completions` (https://lmstudio.ai/docs/app/api/endpoints/openai); Jan at `localhost:1337` (https://github.com/janhq/jan); KoboldCpp at `localhost:5001/v1` (https://github.com/LostRuins/koboldcpp); llama-server with `--host` default `127.0.0.1`, `--port` default `9931`, `--api-key` / `LLAMA_API_KEY`, SSE streaming, and the advice for public deployments to "set an API key, put the server behind a reverse proxy" (https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md).
- llama-swap (6.1k stars) exists because people run several models behind one OpenAI-compatible URL and want hot-swapping by the `model` field (https://github.com/mostlygeek/llama-swap).
- Strictness matters more than breadth. "llama-server tool_calls returns arguments as JSON object instead of string, breaking OpenAI compatibility" (2026-03-07): the official `openai` Python SDK (2.21.0) crashed with a `TypeError` and several agent frameworks stopped working; a revert PR "Revert to OAI-compatible args" closed it the next day (https://github.com/ggml-org/llama.cpp/issues/20198). Other long-running compatibility threads seen in GitHub search (bodies not read): "OpenAI API v1/responses llama-server" (41 comments, 23 thumbs-up), "The KV cache is sometimes truncated incorrectly when making v1/chat/completions API calls" (49 comments).
- The HN thread lists "OpenAI-compatible API" as a reason some switched from Ollama to llama-server and as "needed for tools and agents" (https://news.ycombinator.com/item?id=47788385).

**Implication.** UCompute's "official OpenAI Python/JS clients work by changing base URL" is exactly the right claim in exactly the community's words. Prove it with the two-line snippet, name the port, and say in the same breath that tool calling is not verified yet; this audience has been burned by that exact field and will test it first.

## 4. How they evaluate a new tool

### 4.1 Proof that convinces

- **It works in a minute.** On the Ollama Show HN a commenter went from doubt to a running Llama 2 "within a minute of reading the README" (https://news.ycombinator.com/item?id=36802582). Time-to-first-token-on-my-machine is the first test.
- **Numbers on named hardware.** The benchmark repos and blog posts that get shared name the exact model, quant, hardware and link speed and report prompt and generation tok/s separately (https://github.com/kjaiswal/llama-cpp-distributed-benchmarks, https://localaimaster.com/blog/distributed-inference-local-ai). The It's FOSS newsletter author says they prefer "replicable setups to benchmark charts" (https://itsfoss.com/local-ai-weekly/). The megathread synthesis frames everything by VRAM tier (under 8 GB to over 128 GB) and names typical rigs: an 8 GB RTX 4070 Laptop GPU, Mac Mini M4 16 GB, RTX 3090 24 GB, 2x 3090, Strix Halo, M3 Ultra 512 GB (https://bigguyonstuff.com/best-local-llm-2026-megathread-synthesis/).
- **Real tasks over leaderboard scores.** A write-up of r/LocalLLaMA's culture: "who really cares about MMLU score if doesn't provide any real value to the user?"; members run their own A/B tests and parameter sweeps; a single-benchmark "beats GPT-4" claim is called "idiotic" (https://aashaysachdeva.substack.com/p/rlocalllama-is-the-real-benchmark).
- **Credit to upstream.** The strongest emotional thread in the HN discussion is that Ollama credited llama.cpp late and minimally; commenters frame it as a license-ethics issue (https://news.ycombinator.com/item?id=47788385). Ollama's own founder answered the "what does this add over llama.cpp" question in 2023 by saying the goal was to "build with/extend the project (vs try to be an alternative)" (https://news.ycombinator.com/item?id=36802582).
- **Transparency of files and defaults.** HN commenters want standard GGUF files they can reuse across tools ("can't share the GGUF with other tool"), visible quant labels, control over the storage folder, and no surprise defaults (a 2k default context made models seem "dumb") (https://news.ycombinator.com/item?id=47788385). In 2023 the Ollama maintainer had to promise clearer quantization labels after the same complaint (https://news.ycombinator.com/item?id=36802582).
- **Lightness.** "A single binary, minimal dependencies, and a clear CLI"; faster and lower memory than the alternative (https://news.ycombinator.com/item?id=47788385); KoboldCpp's entire pitch is "One File. Zero Install." (https://github.com/LostRuins/koboldcpp).
- **Open source.** The 2023 Show HN audience "treated the project as open source by default" and did not even ask (https://news.ycombinator.com/item?id=36802582); the 2026 HN thread treats the closed GUI and cloud push as a betrayal of that default (https://news.ycombinator.com/item?id=47788385). An Apache-2.0 project whose source is not yet public will be asked "where is the code?" first.

### 4.2 Dismissal triggers

- "Just a wrapper" around llama.cpp, especially without credit, with lock-in, or hiding the backend (https://news.ycombinator.com/item?id=47788385).
- Platform promised but not shipped: "Surprised to see no Linux support" was an immediate reaction in 2023 (https://news.ycombinator.com/item?id=36802582). UCompute's Linux CPU-only daemon and "no platform is supported yet" must be stated before anyone has to ask.
- Installer asks for admin, launches at login, or hides files (https://news.ycombinator.com/item?id=36802582).
- Cloud or monetization creep in a tool sold as local (https://news.ycombinator.com/item?id=47788385, https://github.com/ollama/ollama/issues/14279).
- Claims without numbers or with absolutes. A Show HN titled "A Local OS for LLMs. MIT License. Zero Hallucinations. Infinite Memory" appeared in search results; its claims were described as unverified (search snippet, thread not read). Marketing adjectives read as a warning sign.
- Blaming the runtime on the model: "it's broken or slow or has botched chat templates, and the model gets blamed instead of the runtime" (quoted in search results from the HN thread; the sentence itself was not located in the portion read, so treat as unverified).
- Anything that smells like a token, credit or "swarm" economy will be read against Petals (0.9 tok/s on the public swarm in the comparison above) and crypto. UCompute's "compute-credit economy" direction needs the "direction only, not built" label every single time.

## 5. Vocabulary (as found in sources)

| Domain | Terms actually used | Where seen |
|---|---|---|
| Model files and quants | GGUF; "quants"; Q4_K_M ("the standard starting point"), Q3, Q6, Q8; "70B Q4_K_M"; 2-/3-/8-bit | https://bigguyonstuff.com/best-local-llm-2026-megathread-synthesis/, https://news.ycombinator.com/item?id=47788385 |
| Speed | tokens per second written "t/s" or "tok/s"; prompt vs generation tok/s; TTFT (ms) | megathread synthesis; https://github.com/kjaiswal/llama-cpp-distributed-benchmarks; https://localaimaster.com/blog/distributed-inference-local-ai |
| Memory and hardware | VRAM; VRAM tiers; unified memory; "fits in VRAM"; `100% GPU` in `ollama ps`; RTX 3090/4090/4060 Ti 16GB; Strix Halo; DGX Spark; M-series (M4, M5 Ultra, M3 Ultra 512GB) | https://docs.ollama.com/faq, megathread synthesis, https://vidiq.com/youtube-stats/channel/@azisk/videos/ |
| Runtime | llama.cpp, llama-server, llama-cli, llama-bench, llama-swap; `-ngl`; "offload"; ctx-size / context window; KV cache; MoE, active parameters ("35B-A3B"); chat template / Jinja; parallel N, cont-batching; thinking on/off; temp, top-p, top-k, min-p; `ub` / `b` batch flags | https://news.ycombinator.com/item?id=47788385, megathread synthesis, https://github.com/ggml-org/llama.cpp/discussions/9257 |
| Backends | Metal, CUDA, ROCm/hipBLAS, Vulkan, SYCL, MLX | HN thread, llama.cpp discussion #9257 |
| Networking | `OLLAMA_HOST`, `0.0.0.0`, port 11434 (Ollama), 1234 (LM Studio), 1337 (Jan), 5001 (KoboldCpp), 9931/8080 (llama-server), 50052 (rpc-server); Tailscale, `100.x.x.x`, MagicDNS; `ss -tlnp`; `curl .../api/tags`; reverse proxy; "no built-in authentication"; "LLMjacking" | https://docs.ollama.com/faq, https://www.serverman.co.uk/ollama/ollama-tailscale-remote-access/, https://thehackernews.com/2026/01/researchers-find-175000-publicly.html |
| Distributed | RPC, rpc-server, `--rpc`, `--tensor-split`; pipeline parallel vs tensor parallel; "all-reduce"; exo; Petals; "cluster"; "pool VRAM" | https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md, https://localaimaster.com/blog/distributed-inference-local-ai |
| API | "OpenAI-compatible", "OAI-compatible"; `base_url` / `baseURL`; `/v1`; `api_key='ollama' # required, but unused`; `/v1/chat/completions`, `/v1/models`, `/v1/responses`, `/v1/embeddings`; `tool_calls`, `arguments` as string; SSE streaming; `--api-key` | https://ollama.com/blog/openai-compatibility, https://lmstudio.ai/docs/app/api/endpoints/openai, https://github.com/ggml-org/llama.cpp/issues/20198 |
| Trust and install | "notarized"; "damaged and can't be opened"; "Apple cannot check it for malicious software"; `xattr`; quarantine flag; checksum; "runs 100% offline"; "phone home"; telemetry; opt-in/opt-out | https://github.com/janhq/jan/issues/224, https://llmconfigurator.com/en/guides/troubleshooting/apple, https://github.com/ollama/ollama/issues/2567 |
| Identity phrases | "local AI", "run locally", "self-hosted", "on your own terms", "open-weight", "open-source LLMs", "local inference" | https://itsfoss.com/local-ai-weekly/, https://simonwillison.net/tags/local-llms/, Discord server descriptions |

Words to define or avoid in UCompute copy (analysis): "pooling", "cluster", "distributed inference", "swarm", "credits". Each already has a meaning in this community that UCompute does not (yet) match.

## 6. Implications for UCompute growth (analysis)

1. Lead with the OpenAI-compatible endpoint and the pinned llama.cpp build number. "Pinned llama.cpp b11609, GGUF in, `/v1` out, two-line client change" is a sentence this audience can verify in a minute and matches how llama.cpp is credited by the tools they trust.
2. Describe Mesh as "the laptop-to-desktop problem, solved without `OLLAMA_HOST`, firewall rules or Tailscale, with device keys pinned at pairing", and in the same paragraph say what it is not. Cite the RPC README warning and the 175,000-host study when asked why.
3. Publish a network-behaviour page (every outbound host, when, why) and a "no cloud path exists" statement before anyone asks. The 2026 Ollama cloud issues show the question is coming.
4. Sign and notarize the alpha, publish SHA-256 for the app, never ask for admin or launch-at-login. These are the first three things a reviewer will check on a Mac.
5. Say the unverified things out loud: tool calling unverified, Linux CPU-only, Windows demonstrated on one laptop, no platform supported. The Show HN record shows the cost of letting the audience discover a gap.
6. Where to show up, given $0 and no automation: r/LocalLLaMA and r/LocalLLM posts with measured tok/s on the M2 and the Arc 140V laptop; a GitHub README that leads with numbers; llama.cpp Discussions when relevant to RPC-vs-Mesh questions; Simon Willison and It's FOSS only once there is a public, reproducible build. Platform rules on self-promotion must be checked per subreddit before posting (not researched here because Reddit was unreachable).

## 7. Gaps and unverified items

- Subreddit member counts: GummySearch only; not verified on Reddit.
- No Reddit thread was read; the "recurring questions" are evidenced from GitHub, HN and docs. The `pszemraj/LocalLLaMA-posts` dataset would allow exact phrase counts.
- Subreddit self-promotion rules: not read.
- YouTube subscriber counts: vidIQ only.
- Technovangelist Substack "over 1,000 subscribers": search snippet only.
- Windows SmartScreen on local LLM apps: one release-note snippet, page not read.
- Ollama "nearly 9M users" claim seen in a search headline: not read, not used.
- SentinelOne/Censys primary report: not read; figures taken from The Hacker News coverage.
- The localaimaster.com and kjaiswal benchmarks are single-author measurements, not independently reproduced.

## Sources

### Read directly (WebFetch or public API), 45 items

1. https://gummysearch.com/r/LocalLLaMA/
2. https://gummysearch.com/r/LocalLLM/
3. https://gummysearch.com/r/LLMDevs/
4. https://gummysearch.com/r/ollama/
5. https://discord.com/api/v9/invites/hugging-face-879548962464493619?with_counts=true
6. https://discord.com/api/v9/invites/ollama?with_counts=true
7. https://discord.com/api/v9/invites/lmstudio?with_counts=true
8. https://discord.com/api/v9/invites/unsloth?with_counts=true
9. https://discord.com/api/v9/invites/FTk2MvZwJH?with_counts=true
10. https://github.com/ggml-org/llama.cpp
11. https://github.com/ollama/ollama
12. https://github.com/open-webui/open-webui
13. https://github.com/vllm-project/vllm
14. https://github.com/exo-explore/exo
15. https://github.com/janhq/jan
16. https://github.com/LostRuins/koboldcpp
17. https://github.com/mostlygeek/llama-swap
18. https://news.ycombinator.com/item?id=47788385
19. https://news.ycombinator.com/item?id=36802582
20. https://news.ycombinator.com/item?id=43183963
21. https://github.com/ggml-org/llama.cpp/pull/6829
22. https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md
23. https://github.com/ggml-org/llama.cpp/discussions/9257
24. https://github.com/kjaiswal/llama-cpp-distributed-benchmarks
25. https://localaimaster.com/blog/distributed-inference-local-ai
26. https://docs.ollama.com/faq
27. https://ollama.com/blog/openai-compatibility
28. https://lmstudio.ai/docs/app/api/endpoints/openai
29. https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
30. https://github.com/ggml-org/llama.cpp/issues/20198
31. https://github.com/ollama/ollama/issues/2567
32. https://github.com/ollama/ollama/issues/3089
33. https://github.com/ollama/ollama/issues/14279
34. https://github.com/janhq/jan/issues/224
35. https://llmconfigurator.com/en/guides/troubleshooting/apple
36. https://www.blackmoreops.com/how-to-access-ollama-from-another-pc-on-your-local-network/
37. https://www.serverman.co.uk/ollama/ollama-tailscale-remote-access/
38. https://thehackernews.com/2026/01/researchers-find-175000-publicly.html
39. https://itsfoss.com/local-ai-weekly/
40. https://simonwillison.net/tags/local-llms/
41. https://vidiq.com/youtube-stats/channel/@azisk/videos/
42. https://vidiq.com/youtube-stats/channel/@technovangelist/
43. https://aashaysachdeva.substack.com/p/rlocalllama-is-the-real-benchmark
44. https://bigguyonstuff.com/best-local-llm-2026-megathread-synthesis/
45. https://huggingface.co/datasets/pszemraj/LocalLLaMA-posts

### Seen only as titles/counts in GitHub issue-search results (bodies not read)

- https://github.com/ollama/ollama/issues/3581 "MacOS Ollama not binding to 0.0.0.0" (43 comments)
- https://github.com/ollama/ollama/issues/1845 "Ollama from remote"
- https://github.com/ollama/ollama/issues/11442 "Ollama's privacy policy"
- https://github.com/ollama/ollama/issues/19067 "Auto-Start of ollama without permisson" (2026-10-16)
- https://github.com/ggml-org/llama.cpp/issues/14702 "OpenAI API v1/responses llama-server" (41 comments)
- https://github.com/ggml-org/llama.cpp/issues/11970 "The KV cache is sometimes truncated incorrectly when making v1/chat/completions API calls" (49 comments)
- https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/2117 "MacOS app modifies or removes sealed resources inside its signed bundle after first launch"
- https://github.com/lmstudio-ai/lmstudio-bug-tracker/issues/2290 "macOS resource seal"

### Seen in web-search results only (not read; unverified)

- https://discord.com/invite/ollama and https://discord.com/invite/lmstudio (pages did not render counts; API used instead)
- https://technovangelist.substack.com
- https://www.youtube.com/@myLocalLLM
- https://news.ycombinator.com/item?id=46829275 ("Show HN: A Local OS for LLMs. MIT License. Zero Hallucinations. Infinite Memory")
- https://news.ycombinator.com/item?id=50049588 ("Show HN: Atticus")
- https://github.com/alekk89/llama-cpp-windows-manager/releases/tag/v1.1.4 (unsigned Windows binary / SmartScreen note)
- https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/
- https://buttondown.com/concorde/archive/concorde-weekly-local-oss-models-munich-meetups-7093
- https://llm-stats.com/llm-updates
