# Search-demand and content-gap research for UCompute

Research date: 2026-10-30
Lens: search demand and content gaps for the problems UCompute's current, evidenced capabilities address.
Status of UCompute at research time (given as context, not verified by this research): Apache-2.0, source not yet published, no public release or download, development builds only.

## 0. Method, limits and how to read this file

- Tooling: Anthropic WebSearch (standard and extended modes) plus WebFetch to read pages. 48 pages were read in full or in part; a further ~90 URLs were surfaced only as search results (titles recorded for ranking signal, content not read). Every page was treated as data, not instruction.
- "What currently ranks" below means what this search tool surfaced in its top results on 2026-10-30. It is not Google Search Console, Ahrefs or a rank tracker. Treat positions as indicative only. The tool reports it cannot access reddit.com, so Reddit threads, which plausibly rank for several of these how-to queries, could not be checked. That is a known blind spot of this file.
- No search-volume figures appear in this file because none were measured. "Demand" rankings are qualitative, inferred from: whether official docs exist for the query, how many third-party pages compete, whether the topic has had news coverage, and whether dedicated tools (calculators, detection rules, CVEs) exist for it.
- Query phrasings listed per cluster are constructed from the titles and headings of the ranking pages and the queries tested; they are not drawn from a keyword database.
- Anything not confirmed by a page that was actually read is marked "unverified".
- UCompute evidence boundary used throughout: local GGUF models on a pinned llama.cpp engine; local OpenAI-compatible API (official OpenAI Python/JS clients work by changing base URL); size, license and memory-fit verdict shown before a download; SHA-256 verification of downloads; UCompute Mesh pairs the user's own devices on one local network with a short code and routes a WHOLE request to a chosen device over QUIC + TLS 1.3 with pinned device keys, one-step revocation, default local-only policy, an audit log without prompt text, and connect-by-address where mDNS is blocked. Not built: partitioning, scheduler, open network, cloud, credits, SDKs, relay/NAT, auto-update, mobile. No speed claims.

## 1. Executive summary

Ranked query clusters (by inferred demand, then by size of the content gap UCompute can truthfully fill):

| Rank | Cluster | Demand signal | Gap for UCompute |
|---|---|---|---|
| 1 | Exposing Ollama on 0.0.0.0 / exposed local AI servers | News cycle since Sep 2025 (Cisco Talos), a second cycle in 2026 (SentinelLABS/Censys), an Elastic detection rule, two security vendors publishing against it | Large: every ranking page is either vendor marketing for a VPN/ZTNA product or a generic Q&A; none explains the LAN-only middle ground or device-level trust |
| 2 | Run a model on another computer on the same network (laptop to desktop GPU) | Evergreen how-to; official Ollama FAQ and LM Studio docs, many blog tutorials, SSH-tunnel and Tailscale guides | Large: every answer is "open the port" or "install a VPN"; none covers pairing, device identity, revocation, audit, or what to do when mDNS is blocked |
| 3 | Running a local LLM with an OpenAI-compatible API | Very common; strong official docs (Ollama, llama.cpp, LM Studio) | Small for basics; medium for the security angle (the API key is ignored; OpenAI route uniformity makes exposed servers easy to fingerprint, per Cisco) |
| 4 | Memory requirements of GGUF models / "will it fit" | Many calculators and articles compete; none authoritative | Medium: calculators do not publish their method; several ignore KV cache; none ties a fit verdict to the download decision |
| 5 | Pairing devices for local AI | New since Sep 2026 (NVIDIA PAIR launch, wide coverage) | Medium: PAIR coverage dominates; nobody explains the trust model of pairing on a shared network in plain language |
| 6 | Local-only / no-telemetry AI runners | Steady; several "privacy audit" pages, official privacy pages | Medium: audits publish no evidence and contradict each other; no project publishes a complete list of connections it makes |
| 7 | Verifying model downloads (SHA-256) | Niche but rising (supply-chain posts, an Ollama verification bug write-up) | Large: no official Hugging Face page found that explains comparing a local GGUF to the Hub hash; Ollama docs do not state the algorithm |
| 8 | llama.cpp RPC security | Niche; spiked with CVE-2026-34159 (CVSS 9.8) | Medium: tutorials still bind RPC to all interfaces; nobody contrasts tensor-level RPC with whole-request routing |
| 9 | Sharing a GPU over the LAN securely (llama.cpp / Ollama) | Moderate; overlaps 1 and 2 | Medium: shared API key or VPN membership are the only patterns documented; no per-device identity, no audit, no home-LAN TLS guidance found |
| 10 | Revoking a device | Very thin; no dedicated local-AI content found | Large but low demand today: the only pages are PAIR's "leave/remove" README section and an unrelated product's CLI docs |

What appears for "UCompute" today (details in section 12): the search tool returned nothing from ucompute.org for either "UCompute" or "ucompute.org". ucompute.org itself is live with a landing page titled "UCompute: the network is taking shape" (no download, no GitHub link). preview.ucompute.org redirects to a Cloudflare Access login. github.com/ucompute is an organization with no public repositories. Name collisions: an RP2040 hardware ecosystem called "uCompute" (JPMichon, several GitHub repos), a planned "UCompute" component in uplus-io/udb, "Universal Compute Platform" (Extreme Networks), "Universal Basic Compute" (a crypto token), "UCOMP" (unconventional computing), "UCloud" (Danish research HPC). The "Mesh" sub-brand also collides with Mesh LLM (~3.7k GitHub stars), two projects named MeshCompute, and LocalMesh.

Five pages UCompute should write first (section 13): (1) what binding a local AI server to 0.0.0.0 actually exposes, and a 60-second self-check; (2) use your desktop GPU from your laptop without opening a port to everyone on the Wi-Fi; (3) pairing explained: short code, pinned device keys, QUIC + TLS 1.3, one-step revocation, and what the audit log records; (4) how UCompute decides a model fits before you download it; (5) what "verified" means: SHA-256 against the publisher's hash before the engine opens the file.

## 2. Cluster: running a local LLM with an OpenAI-compatible API

### Query phrasings developers type
- "local llm openai compatible api"
- "llama.cpp server openai api"
- "ollama openai compatible endpoint python"
- "openai python client base_url local model"
- "lm studio openai api localhost 1234"
- "use openai sdk with local model api key"
- "openai compatible server gguf"
- "llama-server /v1/chat/completions"

### What currently ranks (read)
- Ollama, "OpenAI compatibility" docs: https://docs.ollama.com/openai. States the client setup as `base_url='http://localhost:11434/v1/'` and `api_key='ollama'` with the comment "required but ignored". Lists supported endpoints (`/v1/chat/completions`, `/v1/completions`, `/v1/models`, `/v1/embeddings`, audio endpoints, stateless `/v1/responses`) and limitations (no logprobs, no `tool_choice`, no `n`, context size cannot be set through the OpenAI API, a Modelfile with `num_ctx` is needed).
- llama.cpp server README: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md. As fetched on 2026-10-30 the README says the server "by default listens on `127.0.0.1:9931`", `--host` "(default: 127.0.0.1)", and `--api-key` is "API key to use for authentication, multiple keys can be provided as a comma-separated list (default: none)". Feature list: "OpenAI API compatible chat completions, responses, and embeddings routes." Security lines: "By default the server reflects any `Origin` header back with credentials allowed"; for public deployments, "set an API key, put the server behind a reverse proxy"; `--tools` and `--agent` are marked "do not enable in untrusted environments" because enabling them "exposes file read/write over the API". (Note: several third-party tutorials surfaced in search still describe port 8080 as the default; the README text read today says 9931. Unverified which applies to a given release.)
- LM Studio API docs: https://lmstudio.ai/docs/app/api. Examples use `lms server start --port 1234` and `http://localhost:1234`; REST examples send `Authorization: Bearer $LM_API_TOKEN`; an "Authentication" page exists in the sidebar but the API page gives no setup. "Use chat, responses, embeddings, and other familiar OpenAI-style endpoints."

### What currently ranks (surfaced, not read)
- "How to Deploy OpenAI-Compatible Endpoints as Local LLM Servers" (lmsa.app) https://lmsa.app/blog/how-to-deploy-openai-compatible-endpoints-as-local-llm-servers/
- promptquorum "local llm openai compatible api" (multiple language variants) https://www.promptquorum.com/es/local-llms/local-llm-openai-compatible-api
- machinelearningplus "ollama local llms" https://machinelearningplus.com/gen-ai/ollama-local-llms/
- mindstudio "how to run local ai models with ollama" https://mindstudio.ai/blog/how-to-run-local-ai-models-with-ollama
- Railway "llamacpp server" template page (documents `LLAMA_API_KEY`) https://railway.com/deploy/llamacpp-server.md
- Agno llama.cpp provider docs https://docs.agno.com/models/providers/local/llama-cpp/overview
- llama.cpp issue #19138 about `/v1/responses` support https://github.com/ggml-org/llama.cpp/issues/19138

### What these pages miss or get wrong
- The official pages are good on syntax. Third-party tutorials stop at "change base_url and use a dummy key". None of the read pages explains the consequence: the key is ignored, so the moment the server is bound beyond loopback there is no authentication at all (Ollama's own auth page: "The local API at `http://localhost:11434` does not require authentication." https://docs.ollama.com/api/authentication).
- None connects API uniformity to exposure risk. Cisco Talos found that among exposed Ollama servers "88.89% adhered to the standardized route structure used by OpenAI (e.g., v1/chat/completions)" and argues this uniformity "facilitates the rapid development and deployment of malicious tooling" (https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama).
- Default-port drift (8080 vs 9931 for llama-server) is not explained anywhere read; tutorials go stale silently.

### Original page UCompute can write (truthful under evidence)
- "Point the official OpenAI Python and JS clients at UCompute: what works, what the API key does, and what that means for other devices on your network." A docs page showing the two-line client change, an explicit statement that the local API is loopback-only by default (local-only policy), and a plain explanation that any OpenAI-compatible server bound beyond loopback without a key is open to the whole network. No performance figures. Cross-link to the 0.0.0.0 page (cluster 5).

## 3. Cluster: running a model on another computer on the same network (laptop to desktop GPU)

### Query phrasings
- "access ollama from another computer on local network"
- "use desktop gpu from laptop llm"
- "ollama OLLAMA_HOST 0.0.0.0 windows firewall 11434"
- "lm studio serve on local network"
- "connect to ollama on another pc"
- "run llm on another machine ssh tunnel"
- "ollama tailscale remote access"
- "use my home gpu for ai from laptop"
- "ollama another device same wifi"

### What currently ranks (read)
- blackmoreops, "Access Ollama on Kali Linux From Another PC" (subtitle "Connect to Ollama on a Remote PC Over Your Local Network"; page shows "9 months ago", no exact date): https://www.blackmoreops.com/how-to-access-ollama-from-another-pc-on-your-local-network/. Steps: set `OLLAMA_HOST=0.0.0.0:11434` and `OLLAMA_ORIGINS=*`, add an inbound firewall rule for TCP 11434, find the host IP, test with `curl .../api/tags`, point Open WebUI at it. It states Ollama has no built-in authentication and recommends a reverse proxy or VPN for remote access. It does not cover TLS, how to set up the auth it recommends, API keys, revocation, logging/audit, mDNS, or rate limiting, and it sets `OLLAMA_ORIGINS=*` without reconciling that with its own warnings.
- Ollama FAQ: https://docs.ollama.com/faq. "Ollama binds 127.0.0.1 port 11434 by default." The example for changing it sets `OLLAMA_HOST` to `"0.0.0.0:11434"`. "Ollama allows cross-origin requests from `127.0.0.1` and `0.0.0.0` by default." Reverse proxy via Nginx, ngrok and Cloudflare Tunnel are documented. The FAQ does not cover authentication for the local server.
- LM Studio, "Serve on Local Network": https://lmstudio.ai/docs/developer/core/server/serve-on-network. CLI: `lms server start --bind 0.0.0.0`. "Once enabled, the server binds to a non-localhost address instead of localhost." Warning: "Any bind other than `127.0.0.1` exposes the server beyond `localhost`" and "Only do this if you know what you're doing." It recommends enabling authentication and links to a separate page; no CORS or firewall notes.
- LM Studio, "LM Link": https://lmstudio.ai/docs/lmlink. "LM Link is a new feature in LM Studio that provides a way to access local models across devices, wherever you are." "made possible in partnership with Tailscale." "All communication and data transfer between devices is always end-to-end encrypted, thanks to Tailscale." Example: run a large model on a desktop, use it from a laptop or iPhone. The page does not describe pairing approval or device removal.
- "Connecting to Remote Ollama Servers with SSH Tunneling" (June 15, 2025): https://yhren.github.io/posts/ai/llm/ollama/connecting_to_remote_ollama_servers_with_ssh_tunneling/. Forwards local 11435 to remote 11434 with `ssh -N -L`, tests with the model list, points an OpenAI-compatible client at the tunnel with a dummy key ("not used by Ollama for authentication"), suggests autossh. Does not mention 0.0.0.0 trade-offs, device revocation, audit, TLS, discovery, or multiple devices.
- Serverman, "Ollama + Tailscale: Secure Remote Access Setup Guide" (no publication date on page): https://serverman.co.uk/ai/ollama/ollama-security-guide/. Recommends binding to the Tailscale IP rather than 0.0.0.0, `tailscale serve` for TLS, nginx basic auth for shared use. States "Ollama has no authentication layer at all." No logging/audit guidance, no model-integrity guidance, no per-device restrictions (any tailnet member gets full API access including push/pull).

### What currently ranks (surfaced, not read)
- digitalcitizen.life, "How to Expose Ollama to the Network on Windows" (fetch returned HTTP 403) https://www.digitalcitizen.life/how-to-expose-ollama-to-the-network-on-windows/
- centron.de, "Expose Ollama network port hardening" https://www.centron.de/tutorials/expose-ollama-network-port-hardening
- serverman.co.uk, "ollama network remote access" https://www.serverman.co.uk/ai/ollama/ollama-network-remote-access/
- KDnuggets, "Accessing Local LLMs Remotely Using TailScale: A Step-by-Step Guide" https://www.kdnuggets.com/accessing-local-llms-remotely-using-tailscale-a-step-by-step-guide
- DEV, "How to set up Ollama on Windows for network access via Tailscale" https://dev.to/coderberry/how-to-set-up-ollama-on-windows-for-network-access-via-tailscale-4ph6
- mayhemcode, "How to Securely Access Ollama and Open WebUI Remotely Using Tailscale" (Jan 2026) https://www.mayhemcode.com/2026/01/how-to-securely-access-ollama-and-open.html
- digitalcitizen.life, "How to Use Local Models Remotely With LM Link in LM Studio" https://www.digitalcitizen.life/how-to-use-local-models-remotely-with-lm-link-in-lm-studio/
- Dell blog, "LM Studio's LM Link: Local AI Everywhere" https://www.dell.com/en-us/blog/lm-studio-s-lm-link-local-ai-everywhere/
- Hyperstack and university HPC docs on SSH-forwarding Ollama (docs.hyperstack.cloud/docs/tutorials/ollama, docs.bear.bham.ac.uk, wiki.bwhpc.de)

### What these pages miss or get wrong
- Two answers only: "bind to 0.0.0.0 plus a firewall rule" (anyone on the Wi-Fi can use it) or "install a VPN overlay" (identity is delegated to a third-party account system). Nothing in between.
- No page read covers: which device is allowed to talk to which, how to stop one device later, what was used and when, or how to connect when the network blocks multicast discovery.
- Several guides set `OLLAMA_ORIGINS=*` while warning about exposure. The official FAQ's own example uses `0.0.0.0:11434`.
- Guides written for home LANs assume the LAN is trusted. Shared networks (dorms, offices, co-working, guest Wi-Fi) are not addressed.
- LM Link is the only product page that offers cross-device use with end-to-end encryption by default, and it relies on Tailscale; the page read does not describe pairing approval or device removal.

### Original page UCompute can write (truthful under evidence)
- "Use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi." Walk through: both devices run UCompute; pair with a short code; the laptop chooses the desktop to run a WHOLE request; traffic is QUIC + TLS 1.3 with pinned device keys; nothing listens for unpaired devices by default (local-only policy); the audit log shows which device ran what without prompt text; connect by address when mDNS is blocked. State plainly that this is not pooling or model splitting, that the model must fit on the chosen device, and make no speed claim. Include a comparison of the three patterns (open port, VPN overlay, paired devices) by what each one trusts.

## 4. Cluster: sharing a GPU over the LAN with llama.cpp/Ollama securely

### Query phrasings
- "share gpu over lan llm"
- "llama.cpp server --api-key lan"
- "secure ollama on home network"
- "ollama reverse proxy authentication nginx caddy"
- "llama-server https local network"
- "per-user api keys local llm proxy"
- "ollama security guide"

### What currently ranks (read)
- llama.cpp server README (see cluster 2): `--api-key` exists, default none; "set an API key, put the server behind a reverse proxy" for public deployments.
- Serverman Tailscale guide (see cluster 3).
- Twingate, "175,000 Ollama Servers Are Exposed to the Internet Right Now. Yours Doesn't Have to Be" (byline Aug 8, 2026; metadata Oct 28, 2026): https://www.twingate.com/blog/ollama-server-exposure. Lists Ollama's lack of auth, 0.0.0.0 risk, CVE-2024-37032 ("Probllama"), and recommends its own outbound-only connector plus identity-provider login. The 175,000 headline figure is not sourced in the body. Vendor marketing.
- Tailscale, "Finding 1,000 exposed AI servers took researchers 10 minutes" (Sep 3, 2025, Kevin Purdy): https://tailscale.com/blog/AI-endpoints-on-public-web. Cites Cisco's figures; remedy is Tailscale. Vendor marketing.
- Cisco Talos recommendations (see cluster 5) include "Enforce authentication: Use API key or OAuth2-based authentication, ideally tied to role-based access control", network segmentation, rate limiting and logging, and "verify models by hash or trusted origin before execution".

### What currently ranks (surfaced, not read)
- smol-llm-proxy on PyPI (per-user keys, rate limits, usage logs; TLS terminated externally) https://pypi.org/project/smol-llm-proxy/
- simplified.guide, "How to set llama.cpp server host and port" https://www.simplified.guide/llama-cpp/server-set-host-port
- domoticx.net llama.cpp page (Caddy in front of `--host 0.0.0.0 --api-key`) https://domoticx.net/docs/llm-with-lama.cpp
- securityscientist.net Q&A pages ("How can administrators mitigate these API risks?") https://answers.securityscientist.net/q/8842/how-can-administrators-mitigate-these-api-risks

### What these pages miss or get wrong
- The only authentication patterns documented are a single shared bearer key (llama.cpp `--api-key`) or network membership (VPN). A shared key is not device identity: it cannot be revoked for one device without rotating it for all, and it says nothing about who used it.
- No page read covers TLS for a LAN without a public domain name. The search summary explicitly reported no sources on private-CA or local-domain certificate setup for a home network.
- Audit: Serverman omits logging; Ollama has no identity concept, so logs cannot attribute requests (Elastic's rule says exposed instances allow "unauthenticated model theft, prompt injection, and resource hijacking", https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/cross-platform/initial_access_ollama_api_external_access).
- Security-vendor pages treat "exposed" as "on the internet"; the LAN case (shared Wi-Fi) gets no treatment.

### Original page UCompute can write (truthful under evidence)
- "Why a shared API key isn't device trust." A technical explainer contrasting: shared bearer key (llama.cpp), no auth (Ollama local API per official docs), VPN overlay membership (Tailscale/LM Link), and UCompute's per-device pinned keys with one-step revocation and an audit log that records device and event but never prompt text. Include a table of what each approach can and cannot do (revoke one device, attribute a request, encrypt on the LAN, work without a third-party account). No claims about speed, no claims about features not built (no relay/NAT, no open network).

## 5. Cluster: exposing Ollama on 0.0.0.0 / exposed local AI servers

### Query phrasings
- "ollama 0.0.0.0 security risk"
- "is it safe to expose ollama"
- "ollama exposed to internet"
- "ollama no authentication"
- "ollama unauthenticated api risk"
- "exposed ollama servers shodan"
- "ollama port 11434 open"
- "ollama probllama cve-2024-37032"
- "how to check if my ollama is exposed"

### What currently ranks (read)
- Cisco Talos / Cisco Security blog, "Detecting Exposed LLM Servers: A Shodan Case Study on Ollama" (Sep 1, 2025; Dr. Giannis Tziakouris and Elio Biasiotto): https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama. "we identified 1,139 vulnerable Ollama instances"; about 18.8% (214) were actively serving models; 80% reachable with no models loaded; United States 36.6%, China 22.5%, Germany 8.9%; "over 1,000 instances detected within the first 10 minutes". Method: Shodan banner/port query, then a minimal test prompt (HTTP 200 meant no auth; 401/403 meant some access control). Risks: unauthorized API access ("Many ML servers operate without authentication, allowing anyone to submit queries"), model extraction, jailbreaking, resource hijacking, backdoor injection/model poisoning. Six recommendations including authentication, segmentation, rate limiting and logging, changing default ports/banners, securing model pipelines ("verify models by hash or trusted origin before execution"), continuous monitoring.
- The Register, "In the rush to adopt hot new tech, security is often forgotten. AI is no exception" (2 Sep 2025): https://www.theregister.com/2025/09/02/exposed_ollama_servers_insecure_research/. Secondary coverage of the Cisco study with the same figures and quotes.
- Tailscale blog (Sep 3, 2025) and Twingate blog (2026): see cluster 4. Both vendor marketing; both rely on Cisco's figures; Twingate's 175,000 headline is unsourced in its body.
- Elastic prebuilt detection rule, "Ollama API Accessed from External Network": https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/cross-platform/initial_access_ollama_api_external_access. Medium severity, risk score 47; detects `connection_accepted` on port 11434 from non-private IPs; mitigation "Restrict access immediately by setting OLLAMA_HOST=127.0.0.1:11434 or applying firewall rules."
- Ollama FAQ and Authentication docs (see clusters 2 and 3): local API requires no authentication; binding defaults to 127.0.0.1.

### Secondary figures (not verified against a primary source)
- 175,108 unique exposed Ollama hosts across 130 countries over 293 days; 48% of online hosts with tool calling; China about 30%, United States just over 20%. Attributed in coverage to joint SentinelLABS and Censys research. Surfaced via TechRadar ("Over 175,000 publicly exposed Ollama AI servers discovered worldwide - so fix now", https://www.techradar.com/pro/security/over-175-000-publicly-exposed-ollama-ai-servers-discovered-worldwide-so-fix-now; the article body could not be retrieved, only its title), SC Media (https://www.scworld.com/brief/report-internet-exposed-ollama-ai-servers-widespread) and TechInformed (https://techinformed.com/open-source-llms-are-forming-an-exposed-internet-compute-layer-researchers-warn/). Unverified: the primary report was not read. Do not quote these figures in UCompute content without reading the primary report.
- CVE-2024-37032 "Probllama": path traversal in `/api/pull`, fixed in Ollama 0.1.34; Wiz reported more than 1,000 vulnerable exposed instances as of June 10, 2024. Surfaced via The Hacker News and The Register coverage (https://thehackernews.com/2024/06/critical-rce-vulnerability-discovered.html, https://www.theregister.com/2024/06/24/rce_ollama_wiz/); not read in full. Unverified here.

### What currently ranks (surfaced, not read)
- securityscientist.net, "12 Questions and Answers About ollama unauthenticated api risk" and sibling Q&A pages https://www.securityscientist.net/blog/12-questions-and-answers-about-ollama-unauthenticated-api-risk/
- govinfosecurity / bankinfosecurity, "Exposed LLM Servers Expose Ollama Risks" https://www.govinfosecurity.com/exposed-llm-servers-expose-ollama-risks-a-29354
- insecurestack, "EU's exposed AI infrastructure" https://insecurestack.substack.com/p/eus-exposed-ai-infrastructure
- korben.info, "Ollama - 14,000 AI servers left wide open on the internet" https://korben.info/en/ollama-14000-ai-servers-exposed-internet.html
- cyberpress, cybersecuritynews, gbhackers re-reporting of the Cisco figures

### What these pages miss or get wrong
- Numbers from different methods and dates (1,139 in Sep 2025; "14,000"; "25,000"; 175,108) are mixed in coverage without stating the method; Twingate's headline number is unsourced in its own text.
- The remedy in every vendor page is the vendor's product. The neutral options (keep loopback, pair specific devices, check your own listening sockets) are under-served.
- "Exposed" is framed as internet exposure. The same bind on a shared LAN exposes the server to every device on that network; no read page treats this case.
- No read page offers a short, OS-by-OS "check what your AI server is listening on" procedure alongside the explanation.

### Original page UCompute can write (truthful under evidence)
- "What binding a local AI server to 0.0.0.0 actually exposes, and how to check yours in 60 seconds." Neutral explainer: loopback vs all interfaces; what Ollama's, llama.cpp's and LM Studio's official docs say about defaults and auth (quoted); `ss`/`lsof`/`netstat` checks for macOS, Windows, Linux; why a LAN is not automatically trusted. Then UCompute's position: the local API stays loopback-only by default; other devices reach it only after pairing; nothing accepts unpaired connections. Cite Cisco's primary post; do not repeat the 175,000 figure unless the primary report has been read.

## 6. Cluster: llama.cpp RPC security

### Query phrasings
- "llama.cpp rpc server security"
- "rpc-server llama.cpp authentication"
- "CVE-2026-34159 llama.cpp"
- "llama.cpp rpc distributed inference setup"
- "ggml-rpc-server 0.0.0.0"
- "llama.cpp --rpc multiple machines"
- "is llama.cpp rpc encrypted"

### What currently ranks (read)
- llama.cpp RPC README: https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md. The backend is "currently in a proof-of-concept development stage"; its functionality is "fragile and insecure"; "Never run the RPC server on an open network or in a sensitive environment!" Model weights and KV cache are split across local and remote devices in proportion to memory. The README does not mention authentication or encryption at all.
- GitHub advisory GHSA-j8rj-fmpv-wcxw (CVE-2026-34159), "Unauthenticated RCE via GRAPH_COMPUTE buffer=0 bypass in llama.cpp RPC backend" (published Mar 26, 2026): https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw. CVSS 9.8 Critical; "The RPC backend's `deserialize_tensor()` skips all bounds validation when a tensor's `buffer` field is 0." Affected "<= b7991"; the advisory page lists no patched version and quotes the project's SECURITY.md as "Do not use the RPC backend."
- OSV entry for CVE-2026-34159: https://osv.dev/vulnerability/CVE-2026-34159. Published 2026-04-01; fixed in b8492 (commit 39bf0d3c...). The two pages disagree on whether a fix version is listed; the OSV entry names b8492.
- Arm Learning Path, "Configure the worker nodes" (Distributed inference with llama.cpp): https://learn.arm.com/learning-paths/servers-and-cloud-computing/distributed-inference-with-llama-cpp/how-to-2/. "The RPC feature in `llama.cpp` is not secure by default"; starts the server with `rpc-server -c -p 50052 -H 0.0.0.0 -t 64` and relies on cloud security groups to restrict access; no authentication or encryption discussed.

### What currently ranks (surfaced, not read)
- CVE aggregator pages (Averlon, Mondoo, Lutra Security field guide, exploitdog) for CVE-2026-34159
- Seeed Studio wiki, distributed llama.cpp RPC on Jetson (binds to LAN IP, port 50052) https://wiki.seeedstudio.com/ai_robotics_distributed_llama_cpp_rpc_jetson/
- fungies.io, "How to Set Up Multi-Node Local LLM Inference: The Complete 2026 Guide" https://fungies.io/multi-node-local-llm-inference-guide-2026
- AMD, "How to Run a One Trillion-Parameter LLM Locally: An AMD Ryzen AI Max+ Cluster Guide" https://www.amd.com/ja/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html
- Other llama.cpp CVEs surfaced (server and GGUF parser): CVE-2025-52566, CVE-2026-21869 (n_discard), CVE-2025-71439, CVE-2025-53630 / CVE-2026-27940, CVE-2025-49847 via osv.dev and vuln.today; not read, unverified.

### What these pages miss or get wrong
- Tutorials bind `rpc-server` to a LAN address or 0.0.0.0 and either skip security or defer it to cloud firewall rules. The README's own warning is rarely quoted.
- No read page states what the RPC protocol provides or lacks (the README is silent on auth/encryption; the advisory shows the service is reachable unauthenticated). The search summary reported no source showing RPC traffic carried over SSH or WireGuard.
- No page contrasts the two fundamentally different ways to use a second machine: tensor-level RPC (splits one model; the only way to run a model bigger than one machine) versus routing a whole request to one machine (no split; the model must fit on that machine). Readers searching "llama.cpp rpc" often want the second.

### Original page UCompute can write (truthful under evidence)
- "llama.cpp RPC versus routing a whole request: two ways to use another computer, and what each one exposes." Explain RPC accurately and fairly (it enables models larger than one device; its README calls it proof-of-concept and insecure; CVE-2026-34159), then explain UCompute Mesh's model: one request, one chosen device, QUIC + TLS 1.3, pinned keys, no unpaired listener. State clearly that UCompute does not split models and makes no speed claim. Avoid any statement about RPC throughput.

## 7. Cluster: pairing devices for local AI

### Query phrasings
- "pair devices local ai"
- "nvidia pair personal ai router setup"
- "connect two computers for local llm"
- "home ai cluster pairing code"
- "local ai network of my own devices"
- "distribute inference across home pcs"
- "mtls local ai cluster"

### What currently ranks (read)
- NVIDIA Technical Blog, "NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network" (Sep 03, 2026): https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/. PAIR routes each independent request to one node; "PAIR does not make one inference request run across several GPUs"; works with Ollama and LM Studio; nodes discovered via mDNS "or added by IP address"; "All node to node communication is blocked until the secure connection and pairing is established"; mTLS with generated certificates; Windows/macOS/Linux (beta); RTX 20 series and newer, RTX PRO, DGX Spark, Apple M4+. A demo timing is given but the post qualifies it as "an unofficial, configuration-specific demo, not a general benchmark or a promise of linear scaling." Revocation and audit logs are not mentioned; "Jobs and metrics views" show which node handled each request.
- NVIDIA/Personal-AI-Router README: https://github.com/NVIDIA/Personal-AI-Router. "a local inference router for a group of compatible computers on the same network"; "PIN-based trust bootstrap"; "The inviting machine shows a six-digit PIN, and you enter that PIN on the machine you invited"; leave via Settings, Cluster, Leave, or "Any member can also remove it"; "forgetting to leave first is recoverable"; "PAIR routes each independent request to one node"; engines Ollama, LM Studio, llama.cpp; Windows 11, Linux, macOS; Apache License 2.0; "Read SECURITY.md before deploying it on an untrusted or shared network"; no telemetry statement in the README.
- heise online, "Nvidia PAIR: Private devices become an AI network" (Sep 5, 2026): https://www.heise.de/en/news/Nvidia-PAIR-Private-devices-become-an-AI-network-11442187.html. Six-digit code, mTLS, beta, hardware list; expects a small user group; no benchmarks.
- LocalMesh (Ydde21) README: https://github.com/Ydde21/LocalMesh. One OpenAI-compatible endpoint across machines; admin-approved enrollment tokens; mDNS discovery with CA fingerprint check; "mTLS everywhere"; "does not shard a model across machines and does not pool VRAM; a model must fit within one node's resources"; claims an audit log and no prompt storage; MIT; 0 stars at time of reading; Ollama is the only shipping engine adapter; v0.13.0; "external beta".
- Mesh LLM README: https://github.com/Mesh-LLM/mesh-llm. "Mesh LLM pools GPUs and memory across machines and exposes the result as one OpenAI-compatible API"; QUIC transport ("QUIC end-to-end encrypts traffic between Mesh nodes"); iroh relays; public meshes discovered via Nostr; "private meshes stay invite-token based"; API at `http://localhost:9337/v1`; Apache-2.0; about 3.7k stars; "experimental distributed-systems software"; no benchmark numbers.
- exo README: https://github.com/exo-explore/exo. "Devices running exo automatically discover each other - no manual configuration"; splits models across devices (tensor parallelism); OpenAI Chat Completions, Claude Messages, Responses and Ollama-compatible endpoints at `http://localhost:52415`; macOS app needs Apple silicon and macOS Sequoia 15.1+; Linux CPU-only from source; Apache-2.0; speed claims ("up to 1.8x speedup on 2 devices and 3.2x speedup on 4 devices") are vendor-stated; no API authentication described in the README.
- Vellum docs, "Pair a device": https://www.vellum.ai/docs/hosting-options/pair-a-device. A self-hosted assistant, not an inference-device product; pairing codes "work once and expire after 10 minutes"; `vellum devices revoke <hash>` cuts access immediately; notes that `unpair` on the client and stopping the tunnel do not revoke.

### What currently ranks (surfaced, not read)
- wccftech, "NVIDIA PAIR Turns Your Idle Home PCs Into A Local AI Cluster..." https://wccftech.com/nvidia-pair-turns-your-idle-home-pcs-into-a-local-ai-cluster/
- SDxCentral, "Nvidia brings AI data center networking to the home with 'personal AI router'" https://www.sdxcentral.com/news/nvidia-brings-ai-data-center-networking-to-the-home-with-personal-ai-router/
- MeshCompute (mr-tbot) and MeshCompute (Privateersmanvogue8510), saint0x/mesh, EastonSell/household-compute on GitHub
- Ken Ashe, "Mesh LLM makes distributed inference a networking problem" (Jul 12, 2026) https://kenashe.ai/blog/2026-07-12-mesh-llm-makes-distributed-inference-a-networking-problem

### What these pages miss or get wrong
- PAIR's materials describe the PIN and mTLS but not what a user should understand about trust: what the PIN proves, what is pinned afterwards, what "remove" does to a device's credentials. The README does not use the word revoke.
- exo's README describes auto-discovery with no authentication statements; on a shared network that is a meaningful omission for readers.
- Mesh LLM targets public meshes (Nostr discovery, relays), which is a different threat model from "my own devices on my LAN"; readers comparing projects get no help distinguishing these.
- None explains the shared-network case (dorm, office, co-working Wi-Fi) where discovery is visible to strangers.

### Original page UCompute can write (truthful under evidence)
- "What happens when you pair two devices." A plain-language protocol page: the short code bootstraps trust once; afterwards each device holds the other's pinned key; connections are QUIC + TLS 1.3 authenticated by those keys; a code alone is never trust; nothing accepts unpaired peers by default; connect by address when mDNS is blocked. Clearly state the boundaries: same local network only, no relay/NAT traversal, no open network, no mobile, no model splitting, no speed claim. This page can be honest about PAIR as a comparable (whole-request routing, PIN, mTLS) rather than pretending it does not exist.

## 8. Cluster: revoking a device

### Query phrasings
- "revoke device local ai"
- "remove device from ai cluster"
- "nvidia pair remove node"
- "unpair device llm server"
- "revoke api key ollama" (misdirected: Ollama local API has no keys; only ollama.com keys are revocable per https://docs.ollama.com/api/authentication)

### What currently ranks (read)
- NVIDIA PAIR README (see cluster 7): leave from the device, or any member can remove it from the Cluster list; "forgetting to leave first is recoverable".
- Vellum "Pair a device" (see cluster 7): explicit revoke command; distinguishes revoke from unpair and from stopping the tunnel.
- Ollama Authentication docs: ollama.com keys "do not expire" and can be revoked in account settings; nothing about devices.

### What currently ranks (surfaced, not read)
- Oracle Content Management, "Revoke Access to Linked Devices" (unrelated product) https://docs.oracle.com/en/cloud/paas/content-cloud/administer/revoke-access-linked-devices1.html
- familyfi issue/PR "Pair Device: separate Home access from Remote access" (unrelated) https://github.com/nickberardi/familyfi/issues/162

### What these pages miss
- There is effectively no content explaining what device revocation must do in a local-AI setting: terminate in-flight work or not, refuse reconnection by key rather than by address, remove the key material on both sides, and record the event. Vellum's page comes closest but is about a chat client, not inference devices.

### Original page UCompute can write (truthful under evidence)
- "Revoking a device in one step: what gets removed, what stops immediately, and what the audit log records." Short, precise, with the exact audit-log fields (device identifier, event, time; never prompt text). Also state what revocation does not do (it does not delete models on the other device; it does not affect devices not involved). Low demand today, but it completes the trust story and is uncontested.

## 9. Cluster: local-only / no-telemetry AI runners

### Query phrasings
- "does ollama phone home"
- "lm studio telemetry"
- "local llm no telemetry"
- "offline ai no internet privacy"
- "jan ai privacy telemetry"
- "which local ai is truly private"
- "ollama privacy update check registry.ollama.ai"
- "air gapped llm"

### What currently ranks (read)
- Ollama FAQ: "Ollama runs locally. We don't see your prompts or data when you run locally." For cloud models, "we process your prompts and responses to provide the service but do not store or log that content." Cloud features can be disabled with `OLLAMA_NO_CLOUD=1` or `disable_ollama_cloud` in `~/.ollama/server.json`. https://docs.ollama.com/faq
- LM Studio privacy policy (effective June 2026): "the application does not include telemetry or user-specific tracking"; update checks send device and app information "to give us an understanding of the software and hardware spread of our user-base" and the CDN records IP; model searches are "Anonymized search queries"; "none of your messages, chat histories, and documents are ever transmitted from your system" when running locally. https://lmstudio.ai/privacy
- LM Studio, "Offline operation": "LM Studio can operate entirely offline, just make sure to get some model files first"; network requests to huggingface.co for search/downloads; "the app updater will make a network request to check if there are any new updates available" on launch; no telemetry section on this page. https://lmstudio.ai/docs/app/offline
- Jan privacy page: "Your data (e.g., conversation history, usage logs) are stored locally and never leave your computer."; "Jan, Cortex, and all Menlo Research products do not collect personally identifying information." No telemetry section. https://jan.ai/docs/privacy
- local-llm.net, "Local AI Privacy Audit 2026: What Apps Send Home" (April 8, 2026): https://www.local-llm.net/blog/local-ai-privacy-audit/. Claims Wireshark/mitmproxy testing of Ollama, LM Studio, Jan, GPT4All, Open WebUI; publishes no captures or endpoints; contains version/licence inconsistencies and first-person text under a team byline; promotes paid services. Treat its per-tool claims as unverified.
- InsiderLLM, "Local AI for Privacy: What's Actually Private" (Feb 10, 2026; updated Jul 10, 2026): https://insiderllm.com/guides/local-ai-privacy-guide/. Claims Ollama's core runtime has no telemetry but contacts registry.ollama.ai on startup for update checks; claims LM Studio contacts its servers only for search, download and update checks. No captures or methodology shown. Unverified.
- PromptQuorum, "Local LLM Security and Privacy Checklist: 12 Steps to a Safe Setup" (updated Aug 31, 2026): https://www.promptquorum.com/local-llms/local-llm-security-privacy-checklist. 12 items including checksum verification "for sensitive use", disabling telemetry, confirming loopback binding, not exposing the API. No TLS or authentication guidance; some firm claims ("collect nothing by default") rest on repo inspection only.

### What currently ranks (surfaced, not read)
- InsiderLLM, "Run AI Offline: Air-Gapped LLMs, No Internet (2026)" https://insiderllm.com/guides/running-ai-offline-complete-guide/
- Medium, "Navigating the Local LLM Landscape: ... the Privacy Champion CodexLocal" (vendor piece) https://medium.com/@codexlocalapp/navigating-the-local-llm-landscape-ollama-lm-studio-chatgpt-grok-app-and-the-privacy-champion-f18c9ddff1ff
- meetaitools, "Jan AI Vs Ollama Vs LM Studio: Which Is Best Offline In 2026?" https://meetaitools.com/jan-ai-vs-ollama-vs-lm-studio-which-is-best-offline/
- memx.app, "Run LLMs Locally: Ollama and Privacy" https://memx.app/blog/run-llms-locally-ollama-offline-privacy/

### What these pages miss or get wrong
- The "audits" assert traffic findings without publishing evidence, and they disagree about LM Studio. Official pages are more careful but incomplete (LM Studio's offline page omits telemetry; Jan's privacy page omits update checks).
- No project page read publishes a complete, enumerated list of every outbound connection the app can make and under what user action. That is the artifact readers are searching for.
- "Local-only" is treated as a promise about prompts, not as a network policy with a default.

### Original page UCompute can write (truthful under evidence)
- "Every network connection UCompute makes, and why." An enumerated connections manifest for the development build: model download hosts (only when the user starts a download), paired devices on the local network (only after pairing), and nothing else; explicitly note there is no update checker because auto-update is not built, and no cloud because none exists. Describe the default local-only policy as a setting with a default, not a promise. Publish the method readers can use to verify (an outbound-connection capture during a session). Keep this page factual and update it whenever behaviour changes.

## 10. Cluster: memory requirements of GGUF models / "will it fit"

### Query phrasings
- "gguf vram calculator"
- "how much ram to run 7b gguf"
- "q4_k_m vs q5_k_m size"
- "will this model fit my gpu"
- "llm vram requirements 8gb"
- "gguf memory requirements context length kv cache"
- "can i run it llm"
- "bits per weight q4_k_m"

### What currently ranks (read)
- Hugging Face Hub docs, "GGUF": https://huggingface.co/docs/hub/gguf. Explains that GGUF "encodes both the tensors and a standardized set of metadata", links the Hub's GGUF viewer, and gives the quantization-type table with bits-per-weight (Q4_K "4.5 bits-per-weight", Q5_K "5.5 bits-per-weight", Q6_K "6.5625 bits-per-weight", Q3_K "3.4375", Q2_K "2.625", IQ4_XS "4.25", etc.). No memory formula; no checksum mention.
- llmrun.dev, "Can I Run This LLM? AI Model Hardware Checker": https://llmrun.dev. Browser-side hardware detection ("Detection runs in your browser, nothing is uploaded"), per-model "VRAM @ Q4" figures, a "Fit rating" S to F and a composite score; method and KV-cache handling are not explained; some entries show tokens-per-second figures.
- CanIRun.ai, "Can I run AI locally? Best models for your GPU": https://www.canirun.ai. "We detect your GPU or Mac and rank the open models that actually fit"; letter grades (S/A/B run, C/D tight, F too heavy); lists quant levels and one file size per card without saying which quant it belongs to; does not mention KV cache; open source at github.com/midudev/canirun.ai.
- bmdpat, "GGUF Q4 vs Q5 vs Q8: which quant should you pick?" (May 13, 2026; updated Sep 30, 2026): https://bmdpat.com/blog/gguf-quant-which-to-pick-2026. Recommends starting with Q4_K_M; gives no formula; a correction notes earlier quality and speed figures "had no measurement records and were removed"; heavy promotion.

### What currently ranks (surfaced, not read)
- Hugging Face Space "GGUF Model, Can I split it?" (SadP0i, adapted from NyxKrage's calculator) https://huggingface.co/spaces/SadP0i/GGUF-Model-VRAM-Calculator
- dlsniper/gguf-llm-vram-calculator (parses GGUF metadata, estimates VRAM per context length) https://github.com/dlsniper/gguf-llm-vram-calculator
- sammcj/quantest (RAM and VRAM estimates, max context for a memory budget) https://beta.pkg.go.dev/github.com/sammcj/quantest
- ggufit on PyPI (CPU-only fit against free RAM) https://pypi.org/project/ggufit/0.1.2/
- tinyweights.dev/fit (fetch failed: DNS did not resolve on 2026-10-30)
- rapidtoolset LLM VRAM calculator https://rapidtoolset.com/en/tool/llm-vram-calculator
- SitePoint, "Quantization explained: consumer GPU" https://www.sitepoint.com/quantization-explained-consumer-gpu/
- eastondev, "Ollama Model Quantization Guide: GGUF Format and Accuracy Loss Analysis" (Apr 2026) https://eastondev.com/blog/en/posts/ai/20260422-ollama-gguf-quantization/
- inventivehq, "LLM quantization explained" https://inventivehq.com/blog/llm-quantization-explained

### What these pages miss or get wrong
- The two "can I run it" sites do not publish how they compute fit; one does not mention KV cache at all. Calculators that do account for context are developer tools (Go/Python), not integrated into a download flow.
- Articles recommending quants have retracted unsourced quality/speed numbers (bmdpat) or present single-benchmark anecdotes.
- No page read computes fit against the memory actually free on the user's machine at the moment of download (ggufit does this for CPU RAM only, per its PyPI description, not read in full).
- No page combines size, license and fit in one pre-download decision.

### Original page UCompute can write (truthful under evidence)
- "How UCompute decides a model fits before you download it." Publish the exact method: inputs (file size from the publisher's metadata, bits-per-weight from the GGUF quant type, estimated KV cache for the default context, OS and engine headroom, total and currently available memory on the target device), the verdict categories and their thresholds, and the known limits of the estimate (mmap behaviour, MoE total-parameter rule, GPU/CPU split not modelled if that is the case). Pair it with the license display and the SHA-256 step. Explicitly state that no speed estimate is given and why. This is one of the few pages where UCompute can be more transparent than every calculator that currently ranks.

## 11. Cluster: verifying model downloads (SHA-256)

### Query phrasings
- "verify gguf sha256"
- "huggingface model checksum sha256 verify download"
- "ollama digest mismatch file must be downloaded again"
- "ollama verifying sha256 digest"
- "gguf model hash supply chain"
- "how to check model file integrity"

### What currently ranks (read)
- Kunal Ganglani, "Verify GGUF Model Hashes: 10-Step Supply Chain Workflow" (Aug 31, 2026; updated Oct 6, 2026): https://www.kunalganglani.com/blog/verify-gguf-hashes-supply-chain. Pin exact identity, obtain expected hashes from "release notes, a SHA256SUMS file, or an internal manifest", compute SHA-256 (`sha256sum`, `shasum -a 256`, `Get-FileHash`, `certutil`), compare, prefer a signed manifest (GPG or Sigstore), scan with ClamAV, re-verify at fetch and at startup. Does not mention Hugging Face LFS metadata as a hash source; does not say whether Ollama or LM Studio verify downloads.
- DEV Community, "Ollama: 'digest mismatch, file must be downloaded again'" (Multigrid; dated Aug 13, year not shown): https://dev.to/multigrid/ollama-digest-mismatch-file-must-be-downloaded-again-1k19. Explains that Ollama stores layers as blobs named by SHA-256 and compares against the manifest's expected digest after download; `e3b0c442...b855` is the hash of zero bytes; fix steps (`ollama rm` then pull; delete the specific blob; check free space; switch networks). Omits where the manifest's digests come from, what happens if the manifest is tampered with, and how to verify a hand-imported GGUF from Hugging Face.
- DEV Community, "It Printed 'Verifying.' It Verified Nothing." (Jeriah Keith; posted Aug 2, year not shown): https://dev.to/yeriahz/it-printed-verifying-it-verified-nothing-1cde. Reports that when a blob already exists at the expected path, Ollama printed "verifying sha256 digest" and "success" without re-hashing; a 561-byte null-filled blob passed; the author says an issue was filed as ollama/ollama#17520. The issue itself was not read; unverified.
- Ollama API docs, "Pull a model": https://docs.ollama.com/api/pull. The `digest` field is described only as "Content digest associated with the status, if applicable"; the page does not name the hash algorithm or describe verification; an `insecure` option allows "downloading over insecure connections".
- Hugging Face Hub docs, "Security": https://huggingface.co/docs/hub/security. Lists tokens, 2FA, passkeys, SSH, GPG commit signing, SSO, resource groups, malware scanning, pickle scanning, secrets scanning, third-party scanners (Protect AI, JFrog). No item about file checksums for downloaders.
- Hugging Face, "Download files from the Hub" (huggingface_hub guide): https://huggingface.co/docs/huggingface_hub/en/guides/download. Describes caching, `local_dir`, dry-run and `hf_xet`; the only integrity-related sentence is that `hf_xet` queries "the Xet content-addressable service (CAS) with the LFS SHA256 hash for this file to receive the reconstruction metadata". The guide does not state that downloads are verified against that hash for the user.
- Hugging Face, "Xet: our Storage Backend": https://huggingface.co/docs/hub/en/xet/index. Describes pointer files and chunk-level deduplication; links to Security and Deduplication sub-pages (not read).
- PromptQuorum checklist (see cluster 9): item 2 "Verify model checksums for sensitive use" with `sha256sum`; no explanation of where to obtain a trustworthy expected hash.

### What currently ranks (surfaced, not read)
- gguf-merge-tool on PyPI (claims SHA-256 verification against Hugging Face metadata) https://pypi.org/project/gguf-merge-tool/
- edgemodelr R package `edge_download_model` (verify_checksum option, trust-on-first-use) https://www.rdocumentation.org/packages/edgemodelr/versions/0.2.0/topics/edge_download_model
- codexdeep/ollama-dl (third-party `verify` command for Ollama blobs) https://github.com/codexdeep/ollama-dl
- Hailo community thread about "bad hash" after complete download https://community.hailo.ai/t/hailo-ollama-5-1-1-llama3-2-3b-pull-fails-bad-hash-after-complete-download/19480
- Hub file pages reportedly show a "Large File Pointer Details" block with the LFS SHA256 (seen only in search summaries of doc-build dataset pages; a model repo file page was not fetched; unverified).

### What these pages miss or get wrong
- No official Hugging Face page read tells an end user how to compare a downloaded GGUF with the Hub's recorded SHA-256, or confirms that `huggingface_hub` verifies the hash on the user's behalf.
- Ollama's official API docs do not name the algorithm or describe verification; the two DEV posts fill that gap informally and one documents a case where verification was skipped.
- The supply-chain post is enterprise-oriented (internal registries, Sigstore) and skips the question most users have: where is the publisher's hash for this file?
- Nobody explains that a hash in the same place as the file only proves integrity in transit, not publisher identity.

### Original page UCompute can write (truthful under evidence)
- "What 'verified' means in UCompute: SHA-256 against the publisher's hash, before the engine ever opens the file." State exactly where the expected hash comes from, when the hash is computed (after download, before load), what happens on mismatch (file is not loaded; user is told), and what it does not prove (publisher identity, model safety). Include the manual commands for users of other tools, and a short note on the limits of a hash published alongside the file. If the implementation re-hashes files already on disk before load, say so; if not, do not imply it.

## 12. What appears for "UCompute" and "ucompute.org" today (recorded exactly)

### Search results
- Query "UCompute" (standard mode, 2026-10-30) returned, in order: Wikipedia "UTEC"; Wikipedia "Umtech"; Extreme Networks "universal compute platform latest documentation" (https://ca.extremenetworks.com/s_product_versions/universal-compute-platform-latest-documentation); Mobula "Universal Basic Compute" (https://mobula.io/asset/universal-basic-compute); CoinDesk UBC price page (https://www.coindesk.com/price/ubc); two University of York "compmat" bibliography pages (unconventional computing); AAU "Interactive HPC" UCloud webinar (https://www.researcher.aau.dk/webinar-get-started-with-ucloud-e152847); dute.org "utility computing"; CNX Software "uConsole modular ARM or RISC-V handheld". No result from ucompute.org. The search tool's own summary: "The search didn't turn up anything called exactly 'UCompute.'"
- Query "ucompute.org" returned only unrelated university computing pages (TUM UCHPC workshop, Lund COMPUTE, Iowa IT communities, UPC compute inventory, Waterloo UW HPC team, dblp, CORDIS, ACM pages). No result from the domain. Indexing status in this tool: not surfaced. Google indexing status: unverified (not checked with Google).
- Query "UCompute AI local inference mesh devices" (extended) returned MeshCompute (two repos), household-compute, saint0x/mesh, BaseRT (arXiv), Ken Ashe's Mesh LLM post, LocalMesh, and Wikipedia pages; nothing about UCompute.
- Query "ucompute github OR u-compute OR ucomputing software" (extended) returned the JPMichon uCompute hardware repos, a "Ucomputer" GitHub account, two "UniCompute" repos, and uplus-io/udb.
- Query "github ucompute repository Apache-2.0 LICENSE local AI mesh" returned Mesh LLM pages and unrelated repos; no ucompute repository.
- Query "ucompute reddit OR hacker news OR producthunt OR twitter local AI" (extended) returned generic local-AI guides; the tool reported no Reddit, Hacker News, Product Hunt or Twitter posts about UCompute. (Reddit is not accessible to this tool; unverified there.)
- Wikipedia "Umtech" was read to rule out a collision: it does not mention UCompute in any spelling (https://en.wikipedia.org/wiki/Umtech).

### Direct fetches
- https://ucompute.org (read 2026-10-30): a live landing page, not a parking page. Title "UCompute: the network is taking shape". Headings "The network is taking shape." and "Where UCompute is today". Tagline "Compute better. Together." Describes UCompute as an open computing layer connecting devices, applications and the computing resources they need, starting with AI models that run on hardware the user owns and trusts. Three-stage roadmap: Now (local AI models on the user's own hardware; in development for macOS and Windows; not yet released), Next (connected trusted devices; "In October 2026, development builds on a Mac and a Windows laptop ran each other's prompts"), Later (an open layer for applications, planned; public participation off until it can be made safe). A "Team preview" link to preview.ucompute.org in header and footer. No download links. No GitHub links. No company or person named. Footer: "© 2026 UCompute project. Apache-2.0 licensed."
- https://preview.ucompute.org: HTTP 302 to a Cloudflare Access login page (sparkling-brook-03de.cloudflareaccess.com). Gated; content not visible.
- https://github.com/ucompute: a GitHub organization named "ucompute" with no bio, no public repositories and no public members. The public LICENSE-only repository mentioned in the research brief was not found at this location; its location is unverified.

### Name collisions to track
- "uCompute" RP2040 hardware ecosystem by GitHub user JPMichon: RP2040_uCompute ("Plateforme de développement basé sur un RP2040"), uCompute_Rover (mentions "uComputeOS"), uComputeJr ("lowering the barrier to entry for the uCompute ecosystem"). https://github.com/JPMichon/RP2040_uCompute, https://github.com/JPMichon/uCompute_Rover, https://github.com/JPMichon/uComputeJr (surfaced; not read in full).
- uplus-io/udb roadmap lists a planned "UCompute" distributed computing component (surfaced; not read). https://github.com/uplus-io/udb
- "Ucomputer" GitHub account (surfaced; not read). https://github.com/Ucomputer
- Universal Compute Platform (Extreme Networks product line); Universal Basic Compute (UBC, crypto token); UCloud (Danish research HPC); UCOMP (unconventional computing abbreviation); UniCompute (two unrelated university HPC repos).
- Sub-brand "Mesh": Mesh LLM (github.com/Mesh-LLM/mesh-llm, ~3.7k stars, Apache-2.0, QUIC, "pools GPUs and memory across machines"); MeshCompute (mr-tbot: "Decentralized peer-to-peer AI compute network", QUIC + NAT hole-punch, credit ledger; and a second repo of the same name by Privateersmanvogue8510); LocalMesh (Ydde21); saint0x/mesh. Searches for "UCompute Mesh" phrasing will likely surface these.

## 13. The five pages UCompute should write first

Ranking criteria: inferred demand, size of gap, fit with evidence, and defensibility (no competitor can publish it truthfully).

1. What binding a local AI server to 0.0.0.0 actually exposes, and how to check yours in 60 seconds (cluster 5). Highest-demand topic in this set, currently owned by VPN vendors and generic Q&A. UCompute's default local-only policy is the natural payoff. Cite Cisco's primary post and the official Ollama/llama.cpp/LM Studio docs; avoid the unverified 175,000 figure.
2. Use your desktop's GPU from your laptop without opening a port to everyone on the Wi-Fi (cluster 2). Evergreen how-to demand; every ranking answer is open-the-port or VPN. This is UCompute Mesh's core use case. Must say: whole request, one chosen device, model must fit there, same LAN only, no speed claim.
3. What happens when you pair two devices: short code, pinned keys, QUIC + TLS 1.3, one-step revocation, and what the audit log records (clusters 6 and 7). NVIDIA PAIR made pairing topical in September 2026; revocation has no dedicated content anywhere. Treat PAIR as a fair comparable.
4. How UCompute decides a model fits before you download it (cluster 9). Many calculators compete; none publishes its method or ties fit to the download decision. Publishing the formula and its limits is uncontested ground. Include size and license display. No speed estimate.
5. What "verified" means: SHA-256 against the publisher's hash before the engine opens the file (cluster 10). The Ollama "verified nothing" write-up and the supply-chain posts show live interest; no official Hugging Face page read explains the end-user check. Include manual commands for other tools.

Runners-up: "Every network connection UCompute makes, and why" (cluster 8), and "llama.cpp RPC versus routing a whole request" (cluster 4). The OpenAI-client page (cluster 1) belongs in docs rather than as a flagship article because the official docs already serve the basic query well.

## 14. Rules for all of these pages (derived from the evidence boundary)
- No speed, throughput or latency claims of any kind, including comparisons.
- Say "routes a whole request to one device"; never "pools", "combines", "splits", "cluster" in the pooling sense.
- Name the boundaries on every Mesh page: same local network, no relay/NAT traversal, no open network, no mobile, no cloud, no auto-update.
- Quote official docs for competitor behaviour; do not characterise a competitor as "lacking" something its docs merely do not mention.
- Do not repeat secondary statistics (175,000; 14,000; 25,000) without reading the primary report.
- The project speaks as "UCompute"; no person is named.

## 15. Sources

### Read in full or in part (WebFetch succeeded)
1. https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
2. https://github.com/ggml-org/llama.cpp/blob/master/tools/rpc/README.md
3. https://docs.ollama.com/faq
4. https://docs.ollama.com/openai
5. https://docs.ollama.com/api/authentication
6. https://docs.ollama.com/api/pull
7. https://www.blackmoreops.com/how-to-access-ollama-from-another-pc-on-your-local-network/
8. https://www.twingate.com/blog/ollama-server-exposure
9. https://tailscale.com/blog/AI-endpoints-on-public-web
10. https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
11. https://www.theregister.com/2025/09/02/exposed_ollama_servers_insecure_research/
12. https://www.elastic.co/docs/reference/security/prebuilt-rules/rules/cross-platform/initial_access_ollama_api_external_access
13. https://osv.dev/vulnerability/CVE-2026-34159
14. https://github.com/ggml-org/llama.cpp/security/advisories/GHSA-j8rj-fmpv-wcxw
15. https://learn.arm.com/learning-paths/servers-and-cloud-computing/distributed-inference-with-llama-cpp/how-to-2/
16. https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
17. https://github.com/NVIDIA/Personal-AI-Router
18. https://www.heise.de/en/news/Nvidia-PAIR-Private-devices-become-an-AI-network-11442187.html
19. https://github.com/Ydde21/LocalMesh
20. https://github.com/Mesh-LLM/mesh-llm
21. https://github.com/exo-explore/exo
22. https://www.vellum.ai/docs/hosting-options/pair-a-device
23. https://lmstudio.ai/docs/app/api
24. https://lmstudio.ai/docs/developer/core/server
25. https://lmstudio.ai/docs/developer/core/server/serve-on-network
26. https://lmstudio.ai/docs/lmlink
27. https://lmstudio.ai/docs/app/offline
28. https://lmstudio.ai/privacy
29. https://jan.ai/docs/privacy
30. https://www.local-llm.net/blog/local-ai-privacy-audit/
31. https://insiderllm.com/guides/local-ai-privacy-guide/
32. https://www.promptquorum.com/local-llms/local-llm-security-privacy-checklist
33. https://serverman.co.uk/ai/ollama/ollama-security-guide/
34. https://yhren.github.io/posts/ai/llm/ollama/connecting_to_remote_ollama_servers_with_ssh_tunneling/
35. https://huggingface.co/docs/hub/gguf
36. https://huggingface.co/docs/hub/security
37. https://huggingface.co/docs/huggingface_hub/en/guides/download
38. https://huggingface.co/docs/hub/en/xet/index
39. https://llmrun.dev
40. https://www.canirun.ai
41. https://bmdpat.com/blog/gguf-quant-which-to-pick-2026
42. https://www.kunalganglani.com/blog/verify-gguf-hashes-supply-chain
43. https://dev.to/multigrid/ollama-digest-mismatch-file-must-be-downloaded-again-1k19
44. https://dev.to/yeriahz/it-printed-verifying-it-verified-nothing-1cde
45. https://support.omadanetworks.com/en/document/13310/ (reached via redirect from https://www.tp-link.com/en/support/faq/4294)
46. https://ucompute.org
47. https://github.com/ucompute
48. https://en.wikipedia.org/wiki/Umtech

### Attempted, not readable
- https://preview.ucompute.org (302 to Cloudflare Access login)
- https://tinyweights.dev/fit/ (DNS did not resolve)
- https://www.digitalcitizen.life/how-to-expose-ollama-to-the-network-on-windows/ (HTTP 403)
- https://www.techradar.com/pro/security/over-175-000-publicly-exposed-ollama-ai-servers-discovered-worldwide-so-fix-now (only navigation returned; body not retrieved)

### Surfaced in search results only (titles/URLs recorded for ranking signal; content not read; claims from these are marked unverified above)
- https://www.centron.de/tutorials/expose-ollama-network-port-hardening
- https://www.serverman.co.uk/ai/ollama/ollama-network-remote-access/
- https://www.kdnuggets.com/accessing-local-llms-remotely-using-tailscale-a-step-by-step-guide
- https://dev.to/coderberry/how-to-set-up-ollama-on-windows-for-network-access-via-tailscale-4ph6
- https://www.mayhemcode.com/2026/01/how-to-securely-access-ollama-and-open.html
- https://www.digitalcitizen.life/how-to-use-local-models-remotely-with-lm-link-in-lm-studio/
- https://www.dell.com/en-us/blog/lm-studio-s-lm-link-local-ai-everywhere/
- https://docs.hyperstack.cloud/docs/tutorials/ollama
- https://www.securityscientist.net/blog/12-questions-and-answers-about-ollama-unauthenticated-api-risk/
- https://answers.securityscientist.net/q/8842/how-can-administrators-mitigate-these-api-risks
- https://www.govinfosecurity.com/exposed-llm-servers-expose-ollama-risks-a-29354
- https://insecurestack.substack.com/p/eus-exposed-ai-infrastructure
- https://korben.info/en/ollama-14000-ai-servers-exposed-internet.html
- https://www.scworld.com/brief/report-internet-exposed-ollama-ai-servers-widespread
- https://techinformed.com/open-source-llms-are-forming-an-exposed-internet-compute-layer-researchers-warn/
- https://thehackernews.com/2024/06/critical-rce-vulnerability-discovered.html
- https://www.theregister.com/2024/06/24/rce_ollama_wiz/
- https://research.averlon.ai/vulnerability-intelligence/cve/CVE-2026-34159
- https://fieldguide.lutrasecurity.com/CVE-2026-34159
- https://osv.dev/vulnerability/CVE-2025-52566
- https://vuln.today/tag/llama.cpp
- https://wiki.seeedstudio.com/ai_robotics_distributed_llama_cpp_rpc_jetson/
- https://fungies.io/multi-node-local-llm-inference-guide-2026
- https://www.amd.com/ja/developer/resources/technical-articles/2026/how-to-run-a-one-trillion-parameter-llm-locally-an-amd.html
- https://wccftech.com/nvidia-pair-turns-your-idle-home-pcs-into-a-local-ai-cluster/
- https://www.sdxcentral.com/news/nvidia-brings-ai-data-center-networking-to-the-home-with-personal-ai-router/
- https://kenashe.ai/blog/2026-07-12-mesh-llm-makes-distributed-inference-a-networking-problem
- https://github.com/mr-tbot/MeshCompute
- https://github.com/Privateersmanvogue8510/MeshCompute
- https://github.com/saint0x/mesh
- https://github.com/EastonSell/household-compute
- https://pypi.org/project/smol-llm-proxy/
- https://www.simplified.guide/llama-cpp/server-set-host-port
- https://domoticx.net/docs/llm-with-lama.cpp
- https://railway.com/deploy/llamacpp-server.md
- https://docs.agno.com/models/providers/local/llama-cpp/overview
- https://github.com/ggml-org/llama.cpp/issues/19138
- https://lmsa.app/blog/how-to-deploy-openai-compatible-endpoints-as-local-llm-servers/
- https://www.promptquorum.com/es/local-llms/local-llm-openai-compatible-api
- https://machinelearningplus.com/gen-ai/ollama-local-llms/
- https://mindstudio.ai/blog/how-to-run-local-ai-models-with-ollama
- https://insiderllm.com/guides/running-ai-offline-complete-guide/
- https://medium.com/@codexlocalapp/navigating-the-local-llm-landscape-ollama-lm-studio-chatgpt-grok-app-and-the-privacy-champion-f18c9ddff1ff
- https://meetaitools.com/jan-ai-vs-ollama-vs-lm-studio-which-is-best-offline/
- https://memx.app/blog/run-llms-locally-ollama-offline-privacy/
- https://huggingface.co/spaces/SadP0i/GGUF-Model-VRAM-Calculator
- https://github.com/dlsniper/gguf-llm-vram-calculator
- https://beta.pkg.go.dev/github.com/sammcj/quantest
- https://pypi.org/project/ggufit/0.1.2/
- https://rapidtoolset.com/en/tool/llm-vram-calculator
- https://www.sitepoint.com/quantization-explained-consumer-gpu/
- https://eastondev.com/blog/en/posts/ai/20260422-ollama-gguf-quantization/
- https://inventivehq.com/blog/llm-quantization-explained
- https://pypi.org/project/gguf-merge-tool/
- https://www.rdocumentation.org/packages/edgemodelr/versions/0.2.0/topics/edge_download_model
- https://github.com/codexdeep/ollama-dl
- https://community.hailo.ai/t/hailo-ollama-5-1-1-llama3-2-3b-pull-fails-bad-hash-after-complete-download/19480
- https://docs.oracle.com/en/cloud/paas/content-cloud/administer/revoke-access-linked-devices1.html
- https://github.com/nickberardi/familyfi/issues/162
- https://github.com/JPMichon/RP2040_uCompute
- https://github.com/JPMichon/uCompute_Rover
- https://github.com/JPMichon/uComputeJr
- https://github.com/uplus-io/udb
- https://github.com/Ucomputer
- https://ca.extremenetworks.com/s_product_versions/universal-compute-platform-latest-documentation
- https://mobula.io/asset/universal-basic-compute
- https://www.coindesk.com/price/ubc
- https://www.researcher.aau.dk/webinar-get-started-with-ucloud-e152847
- https://en.wikipedia.org/wiki/UTEC
- https://community.surfboard.com/g34-g36-64/ap-isolation-not-really-5543
- https://community.cambiumnetworks.com/t/isolating-devices-casting-devices-chromecast-apple-tv-android-tv-box-on-the-wlan/63167
- https://forum.openwrt.org/t/client-isolation-on-guest-vlan-in-batman-mesh-doesnt-work/98702/49
