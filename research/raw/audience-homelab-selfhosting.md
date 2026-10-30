# Audience research: homelab and self-hosting communities

**Lens:** audience-homelab-selfhosting
**Date:** 2026-10-30
**For:** UCompute internal strategy repository
**Status of the product at time of writing (from the brief, not from research):** UCompute is Apache-2.0, source not yet published, no public release. UCompute Run (local GGUF via pinned llama.cpp b11609, OpenAI-compatible local API) is demonstrated on an Apple M2 Mac and a Windows 11 Intel Arc laptop; Linux ran a CPU-only daemon in tests. UCompute Mesh pairs your own devices on one LAN and runs a whole request on one chosen device (not pooling, not splitting). Private alpha is macOS Apple Silicon only, owner-managed cohort, no waitlist.

---

## 0. Method and access limitations

- Tools: WebSearch (extended mode for niche/recent) and WebFetch of primary pages. 47 distinct URLs were read in full or in part; all are listed in the Sources section with what each was used for.
- **reddit.com, old.reddit.com, redditinc.com, support.reddithelp.com and web.archive.org were not reachable** from the research tooling (blocked for the crawler / HTTP 403). Reddit search results were also unavailable (the search API reports reddit.com as inaccessible). Consequently every statement about r/selfhosted, r/homelab and r/LocalLLaMA rules below comes from third-party mirrors that quote rule text (willitstay.com) or from secondary articles, and is marked **unverified against reddit.com**. A human should re-read the three subreddits' rules pages (reddit.com/r/<sub>/about/rules) before any post.
- Lemmy, selfh.st, awesome-selfhosted, Home Assistant, TrueNAS, Unraid, Hacker News, GitHub, Fosstodon and mastodon.social were read directly.
- Quotes are kept short; paraphrase elsewhere. Nothing below is a statistic I generated; every number has a URL.

---

## 1. Executive summary

1. **This audience is Linux-first by a wide margin.** The 2025 selfh.st Self-Host User Survey (4,081 responses) found 81% run Linux, 45% use Proxmox, "nearly nine out of ten" use Docker, and Windows Server was "just under 6%" (macOS not reported). A project whose "server" story on Linux is a CPU-only daemon, with macOS and Windows as the demonstrated platforms, is inverted relative to where this audience's hardware lives. [S13][S10]
2. **The dominant local-AI pattern they already run is: one GPU box at home (Linux, usually in Docker/LXC on Proxmox/Unraid/TrueNAS) serving llama.cpp or Ollama behind Open WebUI, reached from laptop/phone over Tailscale or WireGuard.** In the October 2026 Lemmy thread "Is anyone self-hosting their own AI?" (193 comments, score 159) llama.cpp is the most common backend, Open WebUI the most common front end, and Tailscale/WireGuard the most common remote-access method. [S38][S39]
3. **Privacy is the stated motivation, not cost.** The same thread's OP cites "the absolutely abysmal privacy practices of basically all AI companies"; cost payback is debated both ways. Home Assistant's own blog says "local AI is better for your privacy and, in the long term, your wallet." [S38][S41][S34]
4. **They understand that linking two boxes over Ethernet does not make inference faster, but they still want it.** In the Lemmy "Hardware for local inference?" thread the OP asks whether two boxes can be linked; replies say you "absolutely cannot scale horizontally for speed" and that two GPUs in one machine beats two machines. Meanwhile exo ("exo connects all your devices into an AI cluster", 48.1k GitHub stars, macOS app, Linux CPU-only) shows that pooling is the thing people wish existed. UCompute Mesh's "whole request runs on one device" must be stated in the first sentence or the community will assume pooling and feel misled. [S32][S35]
5. **Home Assistant is the single biggest concrete use case, and it requires tool calling.** HA's Ollama integration: "Only models that support Tools may control Home Assistant", recommended "fewer than 25 entities" exposed, and the server must be "accessible over the network". The top HA community voice-assistant build log switched from Ollama to llama.cpp with GGUF from Hugging Face because of tool-calling failures at low quantization. UCompute has not verified tool calling; that is a blocker for the HA sub-audience. [S15][S7]
6. **Rules are strict, written, and enforced on account age and participation, not just content.** Lemmy !selfhosted@lemmy.world: account at least 30 days old with "no exemptions", 10% self-promotion cap (FLOSS without paywall exempt from the cap but not the age rule), mandatory [CBH]/[AIP] tags with a structured AI-use disclosure or the post is removed. r/selfhosted (mirror, unverified): projects under 3 months old may only be posted in the "New Project Megathread", and "Promoted apps must be production ready and have docs." r/LocalLLaMA (mirror, unverified): 10% rule, affiliation disclosed, "LLM based bots posing as humans are strictly not allowed", LLM-generated copy not allowed. Lemmy.World ToS: bots must be labeled, may not advertise, may not vote, and may post only where a community explicitly allows. [S5][S16][S17][S2][S8][S43]
7. **awesome-selfhosted will not list UCompute for at least 4 months after its first tagged release, bans machine/LLM-generated contributions, and excludes desktop apps that need a separate server.** The list is for "Free Software network services and web applications which can be hosted on your own server(s)". Ollama, LocalAI, Open WebUI and LibreChat are listed; llama.cpp, Jan and LM Studio are not. [S3][S23][S24]
8. **The showcase channels that exist are: the r/selfhosted New Project Megathread (unverified), r/selfhosted Wednesday dashboards/tools posts (unverified), Lemmy tagged [CBH]/[AIP] posts, selfh.st's Friday newsletter (35,000+ subscribers; one project per issue in "Content Spotlight"; a Submit Content link; it draws from r/selfhosted, awesome-selfhosted and Mastodon #selfhosted/#homelab), the selfh.st apps directory, the TrueNAS and Unraid app catalogs (community-maintained Docker templates), and the HA community forum.** The Self-Hosted podcast appears to have ended ("150: The Last One", 30 May 2025). r/homelab's rules could not be read from any source. [S1][S20][S46][S21][S25][S26][S44]
9. **Nothing UCompute currently has (no public release, no Linux GPU, no Docker image, no tool calling, anonymous founder, Mac-only alpha) is postable in these venues today without breaking a rule or the audience's expectations.** The honest move is participation-first: a 30-day-plus history of helpful comments on local-AI threads under the project account (clearly labeled, per Lemmy ToS), and a Linux daemon with GPU and a container image before any announcement. The 2026 selfh.st survey adds an AI section; it closes 31 October 2026 and results publish in early November, which is the right moment to re-read the audience before positioning. [S11]

---

## 2. Who this audience is (scale and platform mix)

| Community | Scale (as read) | Source |
|---|---|---|
| r/selfhosted | "had grown past 400K subscribers by mid-2025" (secondary article; unverified) | [S6] |
| !selfhosted@lemmy.world | 63.3K subscribers, 5.92K monthly active users, 383 users/day | [S9] |
| !localllama@sh.itjust.works | 5,490 subscribers, 2,466 active users/month, 645 posts, created 8 June 2023 | [S47] |
| !localllama@lemmy.world | 3 subscribers, 0 monthly active, no posts (dead; the sh.itjust.works one is the live community) | [S27] |
| selfh.st weekly newsletter | "over 35,000 subscribers", delivered every Friday | [S1] |
| selfh.st 2025 survey | 4,081 completed responses | [S10] |
| Open WebUI on TrueNAS | badge alt text "5,000 active deployments" (badge, not an official count) | [S25] |

**Operating systems and platforms (selfh.st 2025 survey, as reported by Linuxiac, 22 Nov 2025):** Linux 81% ("more than four out of five self-hosters"); Proxmox 45%; Home Assistant OS 29%; Raspberry Pi OS 24%; Windows Server "just under 6%"; FreeBSD and derivatives "just over 5%"; Docker "nearly nine out of ten respondents"; LXD 30%; Podman 11%. macOS figures were not reported in the article. The selfh.st results page itself confirms only the 4,081 figure; the full data is said to be in a GitHub JSON file that was not read. [S13][S10]

**What that means for UCompute:** the audience's "server" is a Linux box running containers, very often under Proxmox. A GPU on that box is typically shared among several workloads (Jellyfin, Frigate, LLM) via LXC rather than dedicated to one VM. [S28]

---

## 3. Local-AI needs they voice

### 3.1 Privacy and independence from cloud providers

- Lemmy, 17 Oct 2026, "Is anyone self-hosting their own AI?" (193 comments, score 159, 232 up / 73 down): the OP distrusts "the absolutely abysmal privacy practices of basically all AI companies" and wants smaller models (under 32GB) that "don't absolutely need specialized hardware to run and perform well enough for many purposes." In the replies, privacy is "the most common reason." [S38][S39][S41]
- Lemmy, ~July 2026, "[AIT] Local LLM for Server Setup Guidance?": the OP wants a local model partly because teachers at a school district accidentally share student data with cloud LLMs, and "none of us want to financially support those companies." [S33]
- Home Assistant community, 27 Oct 2025, the most-cited local voice assistant build log: motivations are "the usual privacy concern of having online microphones throughout your home" and outages ("every time AWS or something else went down you couldn't use voice to control lights in the house"). [S7]
- Home Assistant's official position (7 June 2024): "we believe users own their own data"; "local AI is better for your privacy and, in the long term, your wallet"; but "We see the best results with cloud-based LLMs" at that time. [S34]

**Fit:** UCompute's local-only default, no-prompt-text audit logs, and pinned device keys speak directly to this. The anonymity of the founder is neutral here; the community cares about the license and the code, which are not yet public.

### 3.2 "The home server runs the model; the laptop and phone use it"

- In the October 2026 Lemmy thread, "Tailscale and WireGuard are the most common, for reaching the home network from a phone or laptop." Example: twilightwolf90 (score 6): "The server has tailscale installed, so yes I can access it anywhere." Others forward an endpoint to a VPS, use Matrix as an interface, SSH from Termux, or the Conduit phone app. [S39]
- Lemmy "[AIT] Local LLM for Server Setup Guidance?": a reply advises enabling network access and creating a login "since the default is localhost only." [S33]
- Home Assistant's Ollama integration requires you to "configure Ollama to be accessible over the network" and takes a URL such as http://localhost:11434; the server runs on macOS, Linux or Windows separately from HA. [S15]
- XDA (18 July 2025): one Ollama instance in a Proxmox LXC on an RX 7900 XTX serves Open WebUI, Home Assistant, Blinko and a Frigate pipeline (Gemma 27B multimodal). [S28]

**Fit and gap:** This is exactly the Mesh use case ("choose which device runs a request"), and the community already solves it with `OLLAMA_HOST=0.0.0.0` plus Tailscale. UCompute's differentiator is therefore not "reach your server" but pairing by short code, pinned TLS 1.3 device keys, instant revoke, local-only default and audit logging without prompt text. Position Mesh against "I exposed port 11434 to my tailnet and hoped", not against Tailscale itself. Direct-by-address when mDNS is blocked matters because many homelabs segment IoT/VLANs (the HA build log moved voice hardware to a dedicated IoT network). [S7]

### 3.3 GPU sharing and pooling across the home network

- Lemmy, ~May 2026, "Hardware for local inference?": the OP (droopy4096) has a 32GB server already reserving 8GB for TrueNAS, cannot afford new hardware, and asks whether two boxes can be linked to overcome single-box slowness. Replies: sobchak says "putting 2 GPUs in a single machine does" work better than linking machines over Ethernet; ryokimball: you "absolutely cannot scale horizontally for speed"; robber@lemmy.ml: interconnect speed matters, 10+ Gbit/s if linking boxes. "The name of the game is vram" (comrade@piefed.social). Apple Silicon is called "champion of local inference" (Sonalder). [S32]
- exo README: "exo connects all your devices into an AI cluster"; "Devices running exo automatically discover each other - no manual configuration"; "exo figures out the best way to split your model across all available devices"; 48.1k stars; macOS app requires Apple silicon and macOS 15.1+; "Currently, exo runs on CPU on Linux. GPU support for Linux platforms is under development." Compatible with OpenAI Chat Completions, Claude Messages, OpenAI Responses and Ollama APIs. [S35]
- GitHub issue search in exo for "linux gpu" in title: 6 results, including "When will Linux GPU support be available?" (#1129, closed, 1 comment) and two PRs adding native CUDA for Linux (2026). Reaction counts are small (max 4), so this is a weak quantitative signal of demand; the strong signal is the star count on a project whose pitch is pooling. [S45]

**Implication:** When this audience hears "mesh" and "devices", they hear exo-style pooling. The brief says Mesh runs the whole request on one device. Every Mesh description aimed at this audience must say so in the first line, and should say why (the community already knows Ethernet-linked inference is slow, so "we route whole requests instead of splitting models because your LAN is the bottleneck" is an argument they will accept). Partitioning is "design only"; do not mention it as a feature.

### 3.4 Running on Linux servers, in containers, with shared GPUs

- 81% Linux, 45% Proxmox, Docker near-universal (section 2). [S13]
- XDA: chose LXC over VM passthrough because with a VM "the VM would have exclusive control over it," forcing Jellyfin and Frigate into the same VM; LXC lets the GPU be shared across containers. Frustration: Ollama "still defaulted to CPU generation and system RAM" until /dev/kfd permissions, ROCm and AMD drivers were sorted. [S28]
- HA build log: Beelink mini PC plus USB4 eGPU enclosure as the voice server; HA itself on an Unraid NAS; tested RTX 3050 8GB through RTX 3090 24GB; 1–3 s responses on 16–24GB cards. [S7]
- TrueNAS Apps catalog: Open WebUI (community train) added 2024-10-24, last updated 2026-10-29, min TrueNAS 24.10.2.2; an "Ollama Image" variant bundles Ollama, or you point the standard image at an external Ollama via a base URL. [S25]
- Unraid Community Applications: open-webui template (joly0's repository, first seen 2024-04-21, last updated 2026-10-27) uses `ghcr.io/open-webui/open-webui:main`; the listing tells you to add `OLLAMA_ORIGINS=*` to your Ollama container. [S26]

**Gap:** No Docker image, no Linux GPU, and a "daemon" that is CPU-only means UCompute cannot appear in either catalog or in a Proxmox LXC guide. For this audience, "Linux: CPU-only daemon in tests" reads as "not for my server."

### 3.5 Home Assistant and tool calling

- HA Ollama integration: controlling HA is experimental; "Only models that support Tools may control Home Assistant"; "we recommend exposing fewer than 25 entities"; "smaller models are more likely to make mistakes than larger models"; default context window 8k. [S15]
- HA build log (27 Oct 2025, replies to 5 Jan 2026): author recommends llama.cpp over Ollama, uses GGUF from Hugging Face at higher quantization than Ollama defaults, because early Ollama attempts failed at tool calling: "the default `:4b` models for example are often low quantization (Q4_K)." A replier on a 16GB A2000 Ada with Qwen3 4B and ~53 exposed entities reported "turn on the light in living room" sometimes hitting the wrong device; another attributed it to context overruns. [S7]
- HA blog (June 2024): goal is "making local LLMs with function calling easy for all users"; at that time Ollama could not yet control HA. [S34]

**Fit and gap:** UCompute Run's stack (llama.cpp, user-chosen GGUF, SHA-256 verified, memory-fit check) is the stack this build log recommends. But "tool calling verified" is explicitly NOT built. Until it is, UCompute cannot serve the HA sub-audience's headline use case, and should not imply it can.

### 3.6 Runtime and model preferences, and distrust of commercial wrappers

- Lemmy, 14 Oct 2024, "Guide to Self Hosting LLMs Faster/Better than Ollama" (score 341, 83 comments) by brucethemoose: "The quantizations they use tend to be suboptimal"; Ollama "abstracts away llama.cpp in a way that, frankly, leaves a lot of performance and quality on the table"; the author also dislikes the developers' "hints of a commercial product." Recommends Linux (CachyOS) or Windows with HAGS, TabbyAPI/ExLlama when the model fits in VRAM, and power-limiting the GPU. [S40]
- October 2026 Lemmy thread: llama.cpp (often with llama-swap) most common; Ollama on Mac Mini / Mac Studio; LM Studio on Arch; Lemonade on Strix Halo; Qwen 3.x dominant; kensand (score 29): "When I did the math comparing to token API pricing of Opus 4.8, it covered its own costs in a few months"; auzy1 (score 11): "We did the maths. Didn't seem worthwhile and the payback period was a very long time." [S39]
- Open WebUI's catalog descriptions on both TrueNAS and Unraid emphasize "Ollama and OpenAI-compatible APIs" as the two integration surfaces. [S25][S26]

**Fit and risk:** Exposing llama.cpp honestly (pinned build number, user-visible quantization, license shown at download) is a selling point to the brucethemoose camp. The "future compute-credit economy" direction is the kind of "hint of a commercial product" that this camp calls out; in this audience, mention it only when asked and always as direction.

---

## 4. How they react to macOS/Windows-first projects with Linux "planned"

Reddit threads could not be read. The best primary evidence available:

- **Hacker News, 20 July 2023, "Show HN: Ollama – Run LLMs on your Mac" (284 points, 94 comments).** The launch was macOS Apple Silicon only. politelemon: "Surprised to see no Linux support, considering that it's a project that manages... docker." The authors replied within hours: "Linux support is coming" (mchiang) with a `CGO_ENABLED=1 go build .` workaround; jmorgan: "Precompiled for Mac (Windows and Linux coming soon)" and "While we haven't built Linux binaries yet," explaining they wanted fast GPU support first and that Ollama already ran on a Linux server internally. No date was given. [S31][S30][S29]
  - Reading: the reaction was not hostile, but the very first substantive question was "where is Linux", and the credible answer was a build-from-source path plus a stated reason for the delay (GPU support). UCompute can copy that pattern exactly: publish source, give the Linux build command, state that Linux GPU is the gate.
- **exo** ships a macOS app and says "Currently, exo runs on CPU on Linux. GPU support for Linux platforms is under development" — the same shape as UCompute's Linux status. A "When will Linux GPU support be available?" issue exists. [S35][S45]
- **awesome-selfhosted** does not care about desktop clients at all: it lists "network services and web applications which can be hosted on your own server(s)" and excludes "desktop, mobile, or command-line apps that need a separate sync or server program." A macOS GUI is invisible to the list; a Linux daemon with an HTTP API is what would qualify. [S23][S3]
- **The Linux share (81%) and Windows Server share (under 6%)** set the baseline expectation. [S13]
- In the Lemmy hardware thread, Apple Silicon is respected ("champion of local inference") and Mac mini/Studio appear in option lists, so a macOS build is not a negative in itself; it is the absence of a Linux GPU path that is. [S32]

**Unverified:** I could not read any r/selfhosted or r/LocalLLaMA thread complaining about a Mac-only launch. The HN Ollama thread is the closest primary evidence.

---

## 5. Rules on self-promotion, bots and AI content (quoted)

### 5.1 r/selfhosted — UNVERIFIED against reddit.com (source: willitstay.com mirror, rules "last checked Oct 28, 2026")

- Rule 2 "Spam / Self-Promotion / Affiliate Links": "Do not spam or promote your own projects too much." "Promoted apps must be production ready and have docs." "Only mention your service in comments if it's relevant and adds value."
- Rule 5 "Dashboards / Companion Apps / Tools": "On Wednesdays, you may post dashboards or tools that help self-hosters provided it is flaired as such," applying "even if they are not self-hosted."
- Rule 6: "Only in the current "New Project Megathread", you may post projects that are younger than 3 months." Age is measured by "first public presence, e.g. git commit, social media post, etc."
- "r/selfhosted does not publish karma or account-age minimums in its rules," but unpublished filters are common; a standalone promo post outside designated threads "gets removed"; sitewide spam-filter removals are "instant and silent." [S2]
- Secondary (HomeNode, 24 July 2026, affiliate site; unverified): every post must carry a controlled flair; "Self Promotion requires community karma thresholds and disclosure"; "Product Announcement is restricted to actual product releases" (GitHub links do not qualify); initial community resistance to the 2025 changes, later perceived quality improvement; no figures given. [S6]
- threadotter.com shows no rule text and says "The written rules take no clear position, which is NOT permission." [S19]

### 5.2 r/LocalLLaMA — UNVERIFIED against reddit.com (source: willitstay.com mirror, "last checked Oct 28, 2026")

- "Posts must be related to Llama or the topic of LLMs."
- "LLM based bots posing as humans are strictly not allowed."
- "Completely/primarily LLM generated copy, code is not allowed." Exception only for non-native English speakers using an LLM to translate/refine, disclosed.
- "The 1/10th rule is a good guideline: self-promotion should not be more than 10% of your content."
- "Affiliation must be disclosed: No engagement farming, No 'I found this..', etc."
- No published karma/account-age minimums; the page notes the sub "removes content it judges to be AI-generated" and that Reddit's sitewide 9-to-1 guideline applies on top. No weekly or megathread is listed. [S8]

### 5.3 r/homelab — UNVERIFIED (no source displayed rule text)

- willitstay.com/r/homelab returned 404; redditmaster.com returned 404; threadotter.com states the rules "were not visible here" and gives only generic advice ("No explicit link policy"). The soar.sh database does not cover r/homelab, r/selfhosted or r/LocalLLaMA. Search snippets (not read) claim promotion requires moderator permission and that sales belong in r/homelabsales; treat as unverified. [S18][S37]

### 5.4 Reddit sitewide self-promotion guideline — UNVERIFIED

- support.reddithelp.com returned HTTP 403 and web.archive.org is blocked. The willitstay r/LocalLLaMA page references "Reddit's sitewide 9-to-1 self-promotion guideline." [S8]

### 5.5 !selfhosted@lemmy.world — read directly

Sidebar rules (verbatim): 1 "Be civil." 2 "No spam." 3 "Posts are to be related to self-hosting." 4 "Don't duplicate the full text of your blog or readme if you're providing a link." 5 "Submission headline should match the article title." 6 "No trolling." 7 "Promotion posts require active participation, with an account that is at least 30 days old." 8 "AI-related discussions and AI-involved promotional posts have additional requirements for tagging." [S9]

Detailed rules post: [S5]
- Rule 7: "Promotion posts require your active participation in selfhosting or related communities"; account "at least 30 days old," "There are no exemptions from this requirement"; "no more than 10% of your posts or comments may be self-promotional, or your post will be removed" (applies account-wide); fully open-source, fully self-hostable-without-payment projects are exempt from the 10% cap but "The exception does not exempt you from the account age requirement"; posts must be "appropriately tagged, and AI usage disclosed."
- Rule 2 (spam) covers mass-posting, karma-farming, "Using scripts/bots/gen AI to automate posts and comments," and unsolicited DMs; bots are allowed only under the Lemmy.World Rules of Use for Bots.

Expanded AI and promotional rules post (~June 2026): [S16]
- **[CBH]** "Code By Human": promotion posts where no AI was used; no disclosure needed.
- **[AIP]** "AI Project": AI used in development "in any capacity"; disclosure required.
- **[AIT]** "AI Topic": discussions involving AI (hardware for self-hosting, comparing inference tools). A post about UCompute's architecture or a hardware question would be [AIT].
- Disclosure: link an `ai-declaration.md` in the repo, or list only the categories where AI was used (Design, Implementation, Testing, Documentation, Review, Deployment) each with a level (Hint, Assisted, Pair, Generated). "[AIP] tag but no disclosure will be removed." Low-effort comments about AI use on AI-tagged posts may also be removed.

Example disclosures post (~June 2026): format is a bulleted list "Category - Level"; the sample author states they post without promoting their project in at least 90% of their posts and comments. [S17]

### 5.6 Lemmy.World Terms of Service (instance-wide) — read directly [S43]

- Bots: "Bots shall not be used for any kind of advertising."; must be labeled as bots with owner contact in bio; may post only where community owners granted explicit permission; "Bots must not vote on content."; must not post multiple times per minute.
- Section 5.1: "Do not engage in content manipulation such as posting spam content"; "vote manipulation through using several user accounts"; "You must also not vote on content posted by other accounts under your control."
- Section 7.0: Lemmy.World is "not intended to be used as a marketing channel for extensive commercial advertising"; promotion is acceptable when relevant, valuable and inviting engagement; accounts mainly promoting paid products with little other participation may be removed or banned; personal promotion (fundraising, subscription pages, blogs) falls under this rule.

### 5.7 !localllama@sh.itjust.works — read directly [S47]

Rules (verbatim): 1 "No harassment or personal character attacks of community members." 2 "No comparing artificial intelligence/machine learning models to cryptocurrency." 3 "No comparing artificial intelligence/machine learning to simple text prediction algorithms." 4 "No implying that models are devoid of purpose or potential for enriching peoples lives." No self-promotion rule in the sidebar; instance rules of sh.itjust.works apply (not read).
- Note rule 2: UCompute's "future compute-credit economy" direction will trip the crypto comparison reflex in this community. Do not lead with it there.

### 5.8 awesome-selfhosted (awesome-selfhosted-data CONTRIBUTING.md) — read directly [S3]

- "Any software project you are adding was first released more than 4 months ago." Counted from the first tagged release.
- "Machine/LLM-generated contributions are not allowed and will result in a ban." PR template attestation required.
- Software with "no development activity for 6-12 months may be removed from the list."
- Excluded: cloud-provider-dependent software; "Desktop, mobile, or command-line apps that need a separate sync or server program"; libraries/SDKs; PaaS/serverless; generic container/deployment tools (awesome-sysadmin); mere ports/Dockerizations.
- Submission: a `software/<name>.yml` file, kebab-case, via PR (or an issue if uncomfortable with PRs).
- GenAI tag currently lists 13 projects: Agenta, AnythingLLM, GoModel, Khoj, LibreChat (anti-features flagged), LLM Harbor, LLMKube, Local Deep Research, LocalAI, Ollama, Onyx CE, Open-WebUI, Vane. Not listed: llama.cpp, Jan, LM Studio, text-generation-webui, Lobe Chat. [S24]

### 5.9 Mastodon — read directly

- Fosstodon Code of Conduct: "DO toot your own horn and show us your authentic self."; prohibited: "repetitive self-promotion for profit"; "DO NOT post commercial promotions, or advertise through posts that are exclusively links and/or" excessive hashtags; "DO NOT use automated tools to post without also monitoring and/or interacting from your account." [S14]
- mastodon.social rules (API): six rules; the one relevant to AI: "Content created by others must be attributed, and use of generative AI must be disclosed"; accounts may not consist solely of AI-generated content. No explicit spam/bot rule in the six. [S22]
- selfh.st says it draws from "the #selfhosted and #homelab communities on Mastodon", so those hashtags are a real discovery surface. [S21]

### 5.10 Home Assistant community forum — read directly

- Guidelines contain only "Don't post spam or otherwise vandalize the forum." under "Always Be Civil"; nothing specific on self-promotion or AI content. [S42]

---

## 6. Weekly threads and showcase formats

| Venue | Format | Constraints | Source |
|---|---|---|---|
| r/selfhosted "New Project Megathread" | Recurring megathread for projects under 3 months old (measured from first public presence) | Standalone posts for young projects are removed; "production ready and have docs" | [S2] (unverified) |
| r/selfhosted Wednesdays | Dashboards/companion tools posts, flaired | Wednesday only | [S2] (unverified) |
| r/LocalLLaMA | No weekly/megathread shown | 10% rule, disclosure | [S8] (unverified) |
| r/homelab | Unknown | Unknown | none readable |
| !selfhosted@lemmy.world | Tagged posts: [CBH]/[AIP] for projects, [AIT] for discussions | 30-day account, participation, 10% cap, disclosure | [S5][S16] |
| selfh.st weekly (Friday) | Sections: Weekly Highlights, Newswire, Feedback, Content Spotlight, (Overheard Online), (Videos and Podcasts), Command Line Corner, Executive Sponsors, Submit Content. "Content Spotlight" features one project per issue (PatchMon on 23 Oct 2026; Homelable on 16 Oct 2026). Software updates appear in Weekly Highlights. | Independent, curated by Ethan Sholly; Submit Content form exists but no criteria published; sponsors page exists | [S20][S46][S21][S4] |
| selfh.st apps directory | Filters: stars, trending/popular/new, SSO, open-source only, licenses, languages; categories Software and Companions | No AI category visible; submission via Submit Content | [S36] |
| selfh.st survey | Annual; 2026 edition has a new AI section, 45 potential questions, closes 31 Oct 2026 9pm ET, results early November | Read results before positioning | [S11] |
| awesome-selfhosted | PR adding a YAML entry | 4 months after first tagged release; no LLM-generated PRs; must be a network service/web app | [S3] |
| TrueNAS Apps (community train) | Catalog entry with Docker image | Needs a maintained container image | [S25] |
| Unraid Community Applications | Template in a maintainer's repo (e.g., joly0) | Needs a Docker image; community maintainers write templates | [S26] |
| Home Assistant community forum | Build logs and integration threads (the voice assistant build log drew replies for 2+ months) | Spam rule only; tool-calling capability is table stakes | [S7][S42] |
| Self-Hosted podcast (Jupiter Broadcasting) | Biweekly chat show; Contact page and Discord | Last listed episode "150: The Last One" (30 May 2025); appears ended | [S44] |
| Hacker News Show HN | One-off launch thread | Expect "where is Linux" as the first question | [S31] |

---

## 7. Implications for UCompute

### What fits this audience today
- Local-only by default, pinned device keys, revoke in under 0.1 s, audit logs without prompt text: matches the privacy motivation that dominates every thread read. [S38][S7][S34]
- llama.cpp + user-chosen GGUF with visible license and SHA-256: matches the HA build log's recommendation and the anti-Ollama-abstraction camp. [S7][S40]
- OpenAI-compatible local API: matches how Open WebUI and HA integrate ("Ollama and OpenAI-compatible APIs"). [S25][S26][S15]
- Direct-by-address connection when mDNS is blocked: matches segmented IoT/VLAN homelabs. [S7]

### What blocks adoption or posting today
- No public source, no release, no docs: fails r/selfhosted's "production ready and have docs" (unverified) and makes awesome-selfhosted impossible for at least 4 months after the first tag. [S2][S3]
- Linux CPU-only daemon, no Docker image: invisible to 81%-Linux, Proxmox/Docker-first infrastructure and to both NAS app catalogs. [S13][S25][S26]
- Tool calling unverified: excludes the Home Assistant use case. [S15]
- "Mesh" vocabulary invites the exo/pooling assumption; one-device execution must be the first sentence. [S35][S32]
- "Compute-credit economy" direction: triggers the crypto-comparison rule in Lemmy LocalLLaMA and the "hints of a commercial product" distrust. [S47][S40]
- Lemmy requires a 30-day-old account with real participation before any promotion; the project account must be clearly labeled and must never vote. [S5][S43]

### Sequencing that respects the rules (no budget, no spam, no fake accounts)
1. Create the "UCompute" accounts now on lemmy.world, sh.itjust.works (or similar) and Fosstodon/mastodon.social; label them as the project account; begin answering hardware/runtime questions in [AIT] threads with no links to UCompute. This starts the 30-day and 10% clocks. [S5][S14]
2. Publish source and a Linux daemon with a build-from-source path, mirroring the 2023 Ollama HN answer ("Linux support is coming" plus a build command), before any announcement. [S31]
3. Ship a container image and a Linux GPU path (CUDA/ROCm/Vulkan) before approaching TrueNAS/Unraid catalogs or writing a Proxmox LXC guide. [S25][S26][S28]
4. First public post: Lemmy !selfhosted with [AIP] or [CBH] tag and a full AI-use disclosure, then the r/selfhosted New Project Megathread (after re-reading the real rules page), then selfh.st Submit Content for a Content Spotlight. [S16][S2][S4]
5. Read the 2026 selfh.st survey AI section (early November 2026) and adjust. [S11]

---

## 8. Open questions and items marked unverified

- Exact current rule text of r/selfhosted, r/homelab and r/LocalLLaMA (reddit.com unreachable). The willitstay quotes are consistent with the Lemmy community's rules but must be confirmed by a human.
- Reddit's sitewide self-promotion page (403).
- Whether r/homelab has any designated showcase thread.
- The 2025 selfh.st survey's hardware and AI figures (results page shows only the response count; underlying JSON not read).
- Whether the Self-Hosted podcast has resumed after episode 150.
- Any direct r/selfhosted or r/LocalLLaMA reaction to a Mac-only local-AI launch (only the HN Ollama thread was readable).

---

## Sources (every URL read, with what it supplied)

- [S1] https://selfh.st/ — weekly newsletter every Friday, "over 35,000 subscribers", Submit Content link, 2026 survey open.
- [S2] https://willitstay.com/r/selfhosted — third-party mirror quoting r/selfhosted rules 2, 5, 6; no published karma/age minimums; removal behavior; posting-time sample (sampled through 28 Oct 2026). UNVERIFIED against reddit.com.
- [S3] https://raw.githubusercontent.com/awesome-selfhosted/awesome-selfhosted-data/master/CONTRIBUTING.md — 4-month rule, LLM-contribution ban, exclusions, removal for inactivity, submission process.
- [S4] https://selfh.st/submit/ — Submit Content page; tagline only, no criteria.
- [S5] https://lemmy.world/post/48725669 — !selfhosted@lemmy.world detailed rules (Rule 7 account age/10%/FLOSS exemption; Rule 2 bots/AI abuse; Rule 8).
- [S6] https://homenode.tech/r-selfhosted-summer-update-2025-flair-rules-analysis/ — secondary article (24 July 2026) on r/selfhosted flair/self-promo changes; ">400K subscribers by mid-2025"; affiliate site; unverified claims.
- [S7] https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860 — HA local voice assistant build log (27 Oct 2025 – 5 Jan 2026): hardware, llama.cpp over Ollama, tool-calling failures, privacy/outage motivations, IoT network.
- [S8] https://willitstay.com/r/LocalLLaMA — third-party mirror quoting r/LocalLLaMA rules (10% rule, bots, LLM-generated content, disclosure); no megathread listed. UNVERIFIED against reddit.com.
- [S9] https://lemmy.world/c/selfhosted — sidebar rules 1–8 verbatim; 63.3K subscribers, 5.92K MAU; links to rules posts.
- [S10] https://selfh.st/survey/2025-results/ — 4,081 completed responses.
- [S11] https://selfh.st/survey/2026-open/ — 2026 survey: opened 7 Oct 2026, 45 potential questions, new AI section, closes 31 Oct 9pm ET, results early November.
- [S12] https://selfh.st/newsletter/ — weekly archive format; most recent issue 23 Oct 2026.
- [S13] https://linuxiac.com/self-hosters-confirm-it-again-linux-dominates-the-homelab-os-space/ — 2025 survey figures: Linux 81%, Proxmox 45%, HAOS 29%, RPi OS 24%, Windows Server <6%, FreeBSD >5%, Docker ~9/10, LXD 30%, Podman 11% (22 Nov 2025).
- [S14] https://hub.fosstodon.org/coc/ — Fosstodon CoC quotes on self-promotion, commercial posts, automated tools.
- [S15] https://www.home-assistant.io/integrations/ollama/ — network accessibility, Tools-only control, <25 entities, 8k context default.
- [S16] https://lemmy.world/post/49151085 — "AI & Promotional Post Expanded Rules": [CBH]/[AIP]/[AIT], disclosure categories and levels, removal policy (~June 2026).
- [S17] https://lemmy.world/post/49320548 — example disclosures; "Category - Level" format; 90% non-promotional example (~June 2026).
- [S18] https://www.threadotter.com/subreddit-rules/homelab — no rule text available; generic guidance only.
- [S19] https://www.threadotter.com/subreddit-rules/selfhosted — no rule text available; "not permission" caution.
- [S20] https://selfh.st/weekly/2026-10-23/ — section headings; Content Spotlight (PatchMon); AI items in issue.
- [S21] https://selfh.st/about/ — Ethan Sholly; draws from r/selfhosted, awesome-selfhosted, Mastodon #selfhosted/#homelab; Ghost CMS; Sponsors link.
- [S22] https://mastodon.social/api/v1/instance/rules — six server rules incl. generative-AI disclosure.
- [S23] https://awesome-selfhosted.net/ — scope statement ("Free Software network services and web applications which can be hosted on your own server(s)"); GenAI tag URL.
- [S24] https://awesome-selfhosted.net/tags/generative-artificial-intelligence-genai.html — 13 listed GenAI projects; Ollama/LocalAI/Open WebUI/LibreChat present; llama.cpp/Jan/LM Studio absent.
- [S25] https://apps.truenas.com/catalog/open-webui_community/ — Open WebUI community app: added 2024-10-24, updated 2026-10-29, min 24.10.2.2, Ollama image variant, "5,000 active deployments" badge.
- [S26] https://ca.unraid.net/apps/open-webui-0z497h31ntbiab — Unraid CA template (joly0), first seen 2024-04-21, updated 2026-10-27, OLLAMA_ORIGINS note.
- [S27] https://lemmy.world/c/localllama — dead community (3 subscribers, no posts).
- [S28] https://www.xda-developers.com/self-hosted-ollama-proxmox-lxc-uses-amd-gpu/ — Proxmox LXC + RX 7900 XTX; LXC vs VM reasoning; multi-consumer (Open WebUI, HA, Blinko, Frigate); CPU-fallback frustration (18 July 2025).
- [S29] https://hn.algolia.com/api/v1/search?query=ollama&tags=story&numericFilters=created_at_i%3C1694000000&hitsPerPage=10 — earliest Ollama HN stories; "Show HN: Ollama – Run LLMs on your Mac" (20 July 2023, 284 points, 94 comments).
- [S30] https://hn.algolia.com/api/v1/search?tags=comment,story_36802582&query=linux&hitsPerPage=20 — the five Linux/Windows comments in that thread with timestamps and authors.
- [S31] https://news.ycombinator.com/item?id=36802582 — thread summary; "Surprised to see no Linux support"; "Linux support is coming"; "Windows and Linux coming soon".
- [S32] https://lemmy.world/post/47480176 — "Hardware for local inference?" (~May 2026): linking two boxes, "cannot scale horizontally for speed", VRAM, Apple Silicon, budget.
- [S33] https://lemmy.world/post/49925060 — "[AIT] Local LLM for Server Setup Guidance?" (~July 2026): Debian/Docker/3090 setup, cloud-privacy motivation, "localhost only" default advice.
- [S34] https://www.home-assistant.io/blog/2024/06/07/ai-agents-for-the-smart-home/ — HA position on local vs cloud, tool calling goals, privacy quotes (7 June 2024).
- [S35] https://github.com/exo-explore/exo — pitch, auto-discovery, model splitting, macOS app requirement, "Currently, exo runs on CPU on Linux", API compatibility, 48.1k stars.
- [S36] https://selfh.st/apps/ — directory filters and categories; submission links; no AI category visible.
- [S37] https://www.soar.sh/blog/self-promotion-rules-by-subreddit-database — does not cover the three subreddits; notes unpublished karma gates are common (updated 31 May 2026).
- [S38] https://lemmy.world/api/v3/post?id=53242050 — "Is anyone self-hosting their own AI?" metadata: 17 Oct 2026, 193 comments, score 159 (232/73), OP body.
- [S39] https://lemmy.world/api/v3/comment/list?post_id=53242050&sort=Top&limit=40&max_depth=2 — top comments: backends, frontends, hardware, Tailscale/WireGuard, cost debate, quotes with scores (first 100k chars read).
- [S40] https://lemmy.world/api/v3/post?id=20828515 — "Guide to Self Hosting LLMs Faster/Better than Ollama" (14 Oct 2024, score 341, 83 comments): Ollama criticisms and recommendations.
- [S41] https://lemmy.dbzer0.com/post/77092350 — federated copy of the 17 Oct 2026 thread; OP quotes; hardware-cost frustrations (partial).
- [S42] https://community.home-assistant.io/guidelines — "Don't post spam or otherwise vandalize the forum."
- [S43] https://legal.lemmy.world/tos/ — bot rules, vote manipulation, multiple accounts, Section 7 advertising.
- [S44] https://selfhosted.show/ — Jupiter Broadcasting show; biweekly; last listed episode 150 (30 May 2025); Contact and Discord.
- [S45] https://api.github.com/search/issues?q=repo:exo-explore/exo+linux+gpu+in:title&sort=reactions&order=desc&per_page=10 — 6 results; issue #1129 "When will Linux GPU support be available?"; CUDA-for-Linux PRs (2026).
- [S46] https://selfh.st/weekly/2026-10-16/ — section headings; Content Spotlight (Homelable); software updates in Weekly Highlights.
- [S47] https://sh.itjust.works/api/v3/community?name=localllama — live Lemmy LocalLLaMA: 5,490 subscribers, 2,466 MAU, 645 posts, four rules verbatim.

Attempted but unreachable (not cited for content): reddit.com/r/*/about/rules (blocked), old.reddit.com (blocked), redditinc.com/policies/content-policy (blocked), support.reddithelp.com/hc/en-us/articles/205926439 (HTTP 403), web.archive.org (blocked), willitstay.com/r/homelab (404), redditmaster.com/subreddit-rules/homelab (404), github.com/awesome-selfhosted/awesome-selfhosted/blob/master/CONTRIBUTING.md (404; the data repo's file was used instead), awesome-selfhosted.net/tags/artificial-intelligence.html (404; the GenAI tag was used instead), hachyderm.io rules API (connection dropped), reddit-radar-marketing.com (connection refused).
