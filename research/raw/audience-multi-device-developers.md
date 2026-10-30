# Audience research: multi-device developers and power users

**Lens:** people who own more than one computer (laptop + desktop/gaming PC with a GPU, or a Mac + a Linux box) and want to run AI on the stronger machine from the weaker one. This is UCompute Mesh's closest real use case.

**Date of research:** 2026-10-30. Every factual claim below cites a URL that was actually read. Anything not verified from a read page is marked **unverified**. No statistics are invented; where a source gives a number it is quoted with its date.

**Scope reminder (from the brief):** UCompute Mesh today = pair your own devices on one local network with a short code, pick which device runs a request, the whole request runs on one device. QUIC + TLS 1.3, device keys pinned at pairing, instant revoke, local-only mode by default, audit log without prompt text, connect-by-address when mDNS is blocked. Not built: relay/NAT traversal, auto-update, mobile, scheduler, model splitting. Everything below is read against that.

---

## 1. Executive summary

1. **The workflow is real and common, and it is almost entirely hand-assembled.** The dominant pattern in 2025-2026 write-ups and Hacker News comments is: bind Ollama / `llama-server` / LM Studio to `0.0.0.0` (or to a Tailscale IP), open a firewall port, and point clients at a hard-coded IP or tailnet DNS name. Tailscale is the de-facto "pairing layer"; SSH tunnels are the fallback; exo is the only widely-known tool that tries to do discovery for you, and its discovery is the most complained-about part of it.
2. **The two sharpest, best-documented pains are (a) unauthenticated open ports and (b) the strong machine going to sleep.** Ollama has no built-in auth and its maintainers have closed or declined every auth request since 2023 (issues #1053, #8536, #19045). Exposure scans went from 1,139 (Cisco Talos, Sept 2025) to 10.6K (Censys, Sept 2025) to 12,269 (LeakIX, Feb 2026) to 175,000 unique hosts over 293 days (SentinelOne/Censys, Jan 2026). Sleep: Ollama issue #4072 ("Ollama should prevent sleep when working", LAN-serving Windows PC slept mid-generation) has been open since May 2024 with an open PR; Open WebUI has two Wake-on-LAN feature threads; at least two community WoL proxies exist solely for this.
3. **Discovery and pairing are unsolved outside of Tailscale-shaped products.** exo's auto-discovery (mDNS/multicast) fails silently in a cluster of GitHub issues: Linux-to-Mac (#1887), two Ubuntu nodes on one LAN (#2271), macOS Local Network permission lost after restart (#952), overlay-network conflicts (#879). exo's own README warns guest Wi-Fi and some office networks block device visibility, and that Linux is CPU-only. Manual `--bootstrap-peers` was removed ("temporarily"), so there is no connect-by-address fallback (#2271).
4. **LM Studio's LM Link is the closest commercial answer and validates the demand**, but it is Tailscale-dependent, requires the LM Studio Hub for discovery, cannot reuse your own tailnet, is in a batch-rollout Preview with paid plans planned, and HN users have reported login/auth failures and asked for non-Tailscale transports. Its one feature that users love is that remote models appear at `localhost:1234` so existing tools work unchanged.
5. **Mixed-OS is a constant, low-grade tax, not a single blocker.** Windows: `setx` vs session env vars, Private-profile firewall rules, a firewall prompt that hangs an unattended start, Tailscale reconnect after wake. macOS: LaunchDaemon + FileVault conflict, lid-closed sleep, Local Network permission. Linux: Avahi/IPv4 quirks, Docker interfering with bind addresses. Every guide re-derives these.
6. **What would make this audience switch** (from the evidence, not speculation): pairing by short code with pinned device keys instead of IP + firewall + VPN account; no account or hub; an OpenAI-compatible endpoint on the weak machine so existing tools point at `localhost`; connect-by-address when mDNS is blocked; one-click revoke and an audit log; and (the biggest unmet need UCompute does **not** yet address) keeping the strong machine awake or waking it.

---

## 2. Who this audience is (evidence)

The people describing this workflow in 2025-2026 are developers and self-hosters with a spare or dual-use GPU box:

- A developer running Qwen 27B on an AMD 7900 XTX desktop (Bazzite, Podman, llama.cpp + llama-swap, Tailscale), reached from a laptop (Crush CLI) and an iPhone; the same box runs Steam Big Picture on the TV, so the model unloads after 10 idle minutes to free VRAM for gaming. Cold start after swap/idle is ~30 s. ([HN comment 48544986, June 2026](https://news.ycombinator.com/item?id=48544986))
- A MacBook client driving a Linux RTX 4090 workstation over Tailscale for OpenCode/Codex; the author's rationale: "Run inference on a separate machine if you can" because laptop inference "eats into your available RAM" and drains the battery. ([aayushgarg.dev, 29 Mar 2026](https://aayushgarg.dev/posts/2026-03-29-local-llm-opencode/))
- A 16 GB / integrated-graphics Windows laptop using a tower's 30B model over the LAN, "to avoid copying a 20 GB file to a machine that cannot run it." ([dev.to, 27 Oct 2026](https://dev.to/alichherawalla/how-to-use-a-remote-ollama-or-llamacpp-server-from-a-desktop-ai-app-on-windows-in-2026-40pa))
- A Windows laptop (Ryzen 5 7430U, iGPU) turned into a `llama-server` box for other LAN machines, with Tailscale planned for remote. ([thundaxsoftware, 24 Aug 2026](https://thundaxsoftware.blogspot.com/2026/08/building-private-local-llm-server-on.html))
- An M4 Mac mini run as a headless Ollama LaunchDaemon reached at `http://mini.local:11434` from other machines. ([ryanfleck.ca, 20 Dec 2025](https://ryanfleck.ca/2025/m4-mac-mini-llm-server/))
- An HN commenter who wants to "run LLMs on a Windows gaming PC and reach them from a Mac"; the reply was "Start llamacpp server with the gui accessible to your Mac?" ([HN "Ollama's new app", Jul 2025](https://news.ycombinator.com/item?id=44739632))
- A retired game rig (~$200 used GPU, 11-year-old CPU) serving a private model to a whole family via LM Link/Tailscale. ([HN 48625932, mid-2026](https://news.ycombinator.com/item?id=48625932))
- A Windows GPU PC that sleeps when idle, with Open WebUI on an always-on NAS wanting to wake it. ([open-webui discussion #28601, 14 Aug 2026](https://github.com/open-webui/open-webui/discussions/28601))
- 22 HN comments (2024-2026) describing Ollama/llama-server on a home GPU or Mac reached via Tailscale from laptops and phones. ([HN Algolia search "ollama tailscale"](https://hn.algolia.com/api/v1/search?query=ollama%20tailscale&tags=comment&hitsPerPage=30))

Common motives stated: privacy/"data sovereignty", avoiding API bills, using hardware they already own, keeping laptop RAM/battery free. Common second device: a phone, which is **out of UCompute's current scope** (no mobile) and should be noted as a gap this audience will ask about.

---

## 3. What they do today: the five patterns

### 3.1 Bare LAN bind + firewall + IP address

The default for all three mainstream runners is loopback-only, and every guide's first step is to widen it:

- Ollama: "Ollama binds 127.0.0.1 port 11434 by default. Change the bind address with the `OLLAMA_HOST` environment variable." The FAQ has no security or authentication section; for inbound access it shows an Nginx reverse-proxy example. ([docs.ollama.com/faq](https://docs.ollama.com/faq))
- llama.cpp `llama-server`: `--host` default `127.0.0.1`; `--api-key` / `--api-key-file` exist; TLS requires building with OpenSSL 3 (`-DLLAMA_OPENSSL=ON`); `/health` is always unauthenticated; CORS default reflects any Origin. Docs recommend an API key plus reverse proxy for public deployments. ([llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md))
- LM Studio: "Serve on Local Network" toggle or `lms server start --bind 0.0.0.0`; docs warn "Any bind other than `127.0.0.1` exposes the server beyond `localhost`... Only do this if you know what you're doing" and "we recommend enabling authentication." ([lmstudio.ai serve-on-network](https://lmstudio.ai/docs/developer/core/server/serve-on-network)) The "Serve on the network" feature dates to LM Studio 0.3.0 (Aug 2024). ([lmstudio.ai/blog](https://lmstudio.ai/blog))

Then the firewall: Windows guides have you create an inbound TCP 11434 rule on the **Private** profile only, optionally restricted to one client IP, and restart Ollama after setting the env var system-wide. ([mykolaaleksandrov.dev, 29 Jul 2025](https://www.mykolaaleksandrov.dev/posts/2025/07/ollama-network-setup/); [dev.to, 27 Oct 2026](https://dev.to/alichherawalla/how-to-use-a-remote-ollama-or-llamacpp-server-from-a-desktop-ai-app-on-windows-in-2026-40pa)) The thundax write-up scopes the rule to `llama-server.exe`, TCP 8080, Private profile, `LocalSubnet`. ([thundaxsoftware](https://thundaxsoftware.blogspot.com/2026/08/building-private-local-llm-server-on.html))

Then the client: hard-coded `http://192.168.x.x:11434` or `http://SERVER-NAME:8080/v1`, or `OLLAMA_HOST` set on the client machine. Models must be pulled on the server, not the client. ([mykolaaleksandrov.dev](https://www.mykolaaleksandrov.dev/posts/2025/07/ollama-network-setup/))

The Ollama desktop app reportedly gained an "expose Ollama to the network" toggle in 2025 (mentioned by HN user jay_kyburz in the "Ollama's new app" thread, [HN 44739632](https://news.ycombinator.com/item?id=44739632)). The official Windows and macOS docs pages do not document such a toggle ([docs.ollama.com/windows](https://docs.ollama.com/windows), [docs.ollama.com/macos](https://docs.ollama.com/macos)); the version that introduced it is **unverified** (a third-party page claiming v0.94 returned 403 and could not be read).

### 3.2 Tailscale / WireGuard + a runner

This is the most-recommended pattern in 2025-2026 and the one security vendors push:

- Tailscale's own guide (29 May 2025) runs Ollama + Open WebUI on an NVIDIA A4000 in a NixOS VM and exposes it via Tailscale Serve "with TLS and no reverse proxy configuration required," reachable from phones/tablets on the tailnet. ([tailscale.com blog](https://tailscale.com/blog/self-host-a-local-ai-stack))
- A 2026 guide (Windows home PC → MacBook/Linux laptop) binds Ollama to the PC's **Tailscale IP** rather than `0.0.0.0` because it is narrower, notes you must fully quit the Ollama desktop app first, must allow inbound TCP 11434 from the Tailscale network in Windows Firewall, and that plain Tailscale Serve **fails with Ollama** (Serve forwards a `.ts.net` Host header and Ollama returns 403). LM Studio worked through Serve without the 403. ([logarithmicspirals.com, 7 Mar 2026, upd. 25 Jul 2026](https://logarithmicspirals.com/blog/using-tailscale-to-access-private-llms/))
- The MacBook → RTX 4090 OpenCode guide binds `llama-server --host <tailscale ip>` and uses `sk-no-key-required` as the API key placeholder, i.e. the tailnet is the only access control. ([aayushgarg.dev](https://aayushgarg.dev/posts/2026-03-29-local-llm-opencode/))
- HN: "Tailscale plus llama-server makes it easy to run inference at home and use it from anywhere" (bjackman); the porkloin setup above; simonw using Tailscale to reach LM Studio/Ollama on a Mac from his iPhone. ([HN Algolia "ollama tailscale"](https://hn.algolia.com/api/v1/search?query=ollama%20tailscale&tags=comment&hitsPerPage=30))
- One HN anecdote: a roommate "spent 45 minutes configuring NAT when Tailscale already made that unnecessary," following LLM-generated guidance. ([same Algolia search, comment 48386400](https://hn.algolia.com/api/v1/search?query=ollama%20tailscale&tags=comment&hitsPerPage=30))

Why this matters for UCompute: Tailscale solves addressing, encryption and NAT, and people are happy with it, **but** it (a) requires an account and a third-party coordination server, (b) still leaves the runner itself unauthenticated unless you add a proxy, (c) has its own sleep/reconnect bugs on Windows (below), and (d) does nothing about the GPU box sleeping. It also solves off-LAN access, which UCompute Mesh does not (no relay/NAT traversal yet).

### 3.3 SSH tunnels

`ssh -N -L 11434:127.0.0.1:11434 user@gpu-box` is "the fastest to set up" and needs no server-side change; access ends when the terminal closes. ([dev.to "Ollama Has No API Authentication"](https://dev.to/john_182319291/ollama-has-no-api-authentication-how-to-properly-gate-port-11434-48e3)) On HN, when Ollama's new app shipped without remote-host support, the suggested workaround was SSH port forwarding, with the comment that "native support would definitely be better"; another user found it "really surprising" the app couldn't take a hostname. ([HN 44742472, 31 Jul 2025](https://news.ycombinator.com/item?id=44742472)) Ollama maintainer mchiang replied in the parent thread that remote connection is "a feature we are looking into supporting." ([HN 44739632](https://news.ycombinator.com/item?id=44739632))

### 3.4 LM Studio LM Link (closest commercial analogue)

- What it is: "Your own private AI network." Link devices running LM Studio or llmster; remote models appear in the model loader and can be loaded like local ones; tools pointed at `localhost:1234` can use remote models (Codex, Claude Code, OpenCode named). Connections run on "custom Tailscale mesh VPNs"; no ports opened to the public internet; "nothing gets uploaded to LM Studio's backend servers apart from your device list." Status: **Preview**, access "rolled out in batches," free during Preview, "free and paid plans" planned for GA. ([lmstudio.ai/link](https://lmstudio.ai/link))
- How it works: "an entirely separate and self-contained utilization of Tailscale VPN primitives." "The LM Studio Hub is only used to facilitate discovery." You **cannot** use an existing tailnet: LM Link creates a dedicated network and takes "full control over the ACL," which "will not work well with any existing Tailscale networks." A device shows "disconnected" if it crashed without reporting to the discovery server. Preferred-device setting controls where a model loads. ([lmstudio.ai/docs/lmlink/basics/faq](https://lmstudio.ai/docs/lmlink/basics/faq))
- Mobile: LM Link on iPhone/iPad via the Locally app announced 4 June 2026; "All data and communication between devices is end-to-end encrypted." ([lmstudio.ai/blog/locally-lm-link](https://lmstudio.ai/blog/locally-lm-link))
- Reception: HN launch thread (Feb 2026, 4 comments) — one user praises privacy and the userspace tsnet design; one (ZeroCool2u) reports "500 and auth errors even on a new device" and being unable to log in to their LM Studio account. ([HN 47163040](https://news.ycombinator.com/item?id=47163040)) A later Ask HN ("LM Link – This is the future I want") praises it but says "The connection is powered by tailscale, long-term I would like to see other implementations" and points to Iroh, arguing a text stream "shouldn't depend on a single company's infrastructure." ([HN 48625932](https://news.ycombinator.com/item?id=48625932)) Another commenter notes you can "set up your own VPN and use llama-server" instead, though LM Link is simpler out of the box (freehorse, [HN Algolia "LM Link"](https://hn.algolia.com/api/v1/search?query=%22LM%20Link%22&hitsPerPage=30)).

Why this matters for UCompute: LM Link proves the demand and shows the winning UX (remote model looks local). Its weak points map directly onto UCompute Mesh's design: account + hub dependency, Tailscale dependency, closed-source, preview gating, paid plans coming. UCompute's "whole request on one device, chosen by the user" is the same execution model LM Link uses (preferred device), not a cluster model.

### 3.5 exo clusters (model splitting)

- README: "exo connects all your devices into an AI cluster" and "figures out the best way to split your model across all available devices." Discovery is automatic, "no manual configuration," but devices must be on the same network and the **same exo version**; "guest Wi-Fi and some office networks may block device visibility"; macOS requires Local Network permission; **"Currently, exo runs on CPU on Linux"** (GPU under development); RDMA over Thunderbolt 5 needs macOS 26.2+ and matching OS versions. 48.1k stars, 208 open issues at time of reading. ([github.com/exo-explore/exo](https://github.com/exo-explore/exo))
- Maintainer on overlay networks: "We explicitly don't network exo over tailscale as it interferes with our development setups." (Evanev7, Dec 2025, [#879](https://github.com/exo-explore/exo/issues/879))
- Discovery failures (details in §4.2): [#1887](https://github.com/exo-explore/exo/issues/1887), [#2271](https://github.com/exo-explore/exo/issues/2271), [#952](https://github.com/exo-explore/exo/issues/952), [#363](https://github.com/exo-explore/exo/issues/363).

Why this matters for UCompute: exo is the "pooling" product this audience has heard of; it is Mac-centric, Linux-CPU-only, and its discovery is fragile. UCompute Mesh explicitly does not split models, and should say so plainly. The audience's actual day-to-day pattern (§3.1-3.4) is "run the whole thing on the big box," which is exactly what Mesh does.

---

## 4. What goes wrong (evidence by theme)

### 4.1 Security of open ports: no auth, and exposure at scale

**Ollama has no authentication and the maintainers have repeatedly declined to add it.**

- Issue #1053 (opened Nov 2023, 25 comments, ~65 thumbs-up across comments) closed Dec 2024 by jmorganca: "we try to keep Ollama focused on serving an http API that can be fronted by a number of proxy servers." A community basic-auth PR (#6223) was not merged. Users noted proxies don't help client libraries that can't pass tokens, and that most clients (CherryStudio, Chatbox) can't handle basic-auth URLs. ([#1053](https://github.com/ollama/ollama/issues/1053))
- Issue #8536 (Jan 2025): collaborator rick-github: "The core team currently recommends using a proxy"; a new API-key PR's chance of merging is "slim." User: a proxy is "sort of overkill for single-user instances." The "use an external project" reply drew 10 thumbs-down. ([#8536](https://github.com/ollama/ollama/issues/8536))
- Issue #19045 (16 Oct 2026) proposes opt-in IP allowlist / rate limit / bans because "a lot of people set `OLLAMA_HOST=0.0.0.0` so another machine, a container, a phone or Open WebUI can reach it. From that point the API is unauthenticated and open to anyone who can route to the port." No maintainer response as of reading (an ollama-account comment was deleted 19 Oct 2026). ([#19045](https://github.com/ollama/ollama/issues/19045))

**Exposure measured by scanners (all primary sources read):**

| Source | Date | Finding |
|---|---|---|
| Cisco Talos | 1 Sep 2025 | 1,139 exposed Ollama instances via Shodan; 214 (~18.8%) actively serving models; "over 1,000 instances detected within the first 10 minutes"; US 36.6%, China 22.5%, Germany 8.9%. "arbitrary, unauthenticated prompt execution is possible." ([blogs.cisco.com](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama)) |
| Censys | 24 Sep 2025 | 10.6K high-confidence instances across 1,229 ASNs (from 21.1K hosts before filtering); 1.5K respond to a probing prompt; >25% on non-default ports. "security is an afterthought." ([censys.com](https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys)) |
| SentinelOne + Censys (via SecurityWeek) | 30 Jan 2026 | 175,000 unique Ollama hosts over 293 days, 130 countries, 4,032 ASNs; **56% on fixed-access telecom networks including consumer ISPs**; ~half could execute code/access APIs; 201 hosts ran guardrail-removing templates. ([securityweek.com](https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/)) |
| LeakIX | 23 Feb 2026 | 12,269 instances with zero auth; ~1,000 on versions vulnerable to CVE-2024-37032 (unauth RCE); top networks AWS 1,686, Hetzner 1,004, OVH 773, Contabo 634. Explicitly argues "These aren't hobbyist setups on home networks" but cloud GPU boxes, while blaming the `OLLAMA_HOST=0.0.0.0` quickstart habit. ([blog.leakix.net](https://blog.leakix.net/2026/02/ollama-exposed/)) |
| Tailscale (summarising Talos) | 3 Sep 2025 | Pennarun: "they slap something out on the public internet, and they cover their eyes and hope that nobody finds it." ([tailscale.com blog](https://tailscale.com/blog/AI-endpoints-on-public-web)) |

Interpretation for UCompute: the internet-exposed population is mostly cloud (LeakIX) but a large share sits on consumer ISPs (SentinelOne's 56% fixed-access telecom). The **LAN** exposure that affects our audience is less measured but is the framing of the Hive Security piece (7 May 2026): anyone on the same network, or a compromised router, or UPnP, can reach an unauthenticated 11434/1234; "any application that runs a server should be assumed to be listening on your network until you verify otherwise." ([hivesecurity.gitlab.io](https://hivesecurity.gitlab.io/blog/local-ai-tools-open-ports-security-risk/)) **Caveat:** that article states Ollama "defaults to `0.0.0.0:11434`", which contradicts Ollama's own FAQ (127.0.0.1 default); treat its default-binding table as unreliable.

**The friction the fixes add:** the dev.to gating guide ranks a reverse proxy with bearer token as the highest-effort option (proxy config, token, certs, checking clients can send headers; the `ollama` CLI cannot), mesh VPN as moderate (and "access control moves to enrolment, so remove old devices"), SSH as fastest but session-bound, firewall as a backstop only (Docker-published ports bypass ufw). ([dev.to](https://dev.to/john_182319291/ollama-has-no-api-authentication-how-to-properly-gate-port-11434-48e3)) Cisco's recommendations are exactly a product spec: API-key/token auth, network isolation, rate limiting, change default ports, audit. ([blogs.cisco.com](https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama))

### 4.2 Discovery and pairing

- Hard-coded IPs are the norm (§3.1). `.local` names are used by some (ryanfleck: `mini.local`), but mDNS is where exo breaks:
  - **Linux node invisible to Mac cluster** (Ubuntu 24.04 + 4090 vs Mac Studio; firewalls disabled; still fails). Maintainer: Avahi on Ubuntu "sometimes fails to set up IPv4 addresses with macOS's mDNS responder"; run `avahi-autoipd`. Also confirmed CUDA "planned but not yet integrated." Open. ([exo #1887, 13 Apr 2026](https://github.com/exo-explore/exo/issues/1887))
  - **Two Ubuntu nodes on the same /24, no errors, each elects itself master.** Reporter opened ports 52415/7447, verified unicast UDP, then found `--bootstrap-peers` raises `ValueError("Bootstrap peers has been temporarily removed")`, so no manual peering fallback. No maintainer response. Open. ([exo #2271, 20 Aug 2026](https://github.com/exo-explore/exo/issues/2271))
  - **macOS Local Network permission lost after restart**; cluster drops after ~20 minutes on two M3 Ultra Mac Studios over TB5; only fix is relaunching exo on both. Maintainer: "the issue is why we seem to lose this permission on restart." Open. ([exo #952, 21 Dec 2025](https://github.com/exo-explore/exo/issues/952))
  - **Overlay networks**: devices with Tailscale + ZeroTier discovered each other on LAN addresses instead of overlay addresses; fix was removing one overlay. Maintainer: exo is explicitly not networked over Tailscale. ([exo #879](https://github.com/exo-explore/exo/issues/879)) Mac Studio + MacBook Pro over OpenVPN "never discover each other and each instance runs separately"; commenter: mDNS will "not have a good surviving chance" over VPN. ([exo #363, Oct 2024](https://github.com/exo-explore/exo/issues/363))
- exo README itself: same network, same version, guest/office Wi-Fi may block visibility. ([exo README](https://github.com/exo-explore/exo))
- LM Link avoids mDNS entirely by using a cloud Hub for discovery, with the account/hub costs noted in §3.4.

### 4.3 The strong machine sleeps (and the VPN doesn't come back)

- **Ollama #4072 "Ollama should prevent sleep when working"** (1 May 2024, open): Windows 11 PC serving the API over LAN "sometimes went to sleep while client apps waited for API responses." Collaborator dhiltgen labelled it good-first-issue and pointed to `SetThreadExecutionState`; PR #16468 is open; a contributor said on 3 Jun 2026 they'd submit a PR. Workarounds posted: PowerToys Awake (keeps PC awake always, not just during work), "never sleep" power plan, WoL proxies (one user: "the PC could still sleep mid-request"), a script that fakes a keypress per request. ([#4072](https://github.com/ollama/ollama/issues/4072))
- **Open WebUI WoL requests**: #3526 (Jun 2024, still active Apr 2026, 10 participants): Open WebUI in a container on one PC, Ollama on another; user wakes it via Moonlight from a phone; "The GPU server is used occasionally, so I need it to be off most of the time." Key limitation: when Ollama is offline its models disappear from the UI, so a plugin can't wake it; a proxy is needed. ([#3526](https://github.com/open-webui/open-webui/discussions/3526)) #28601 (14 Aug 2026): Open WebUI on an always-on NAS, Ollama on a Windows GPU PC that sleeps; "Keeping the AI PC powered on 24/7 can consume significant amounts of electricity." ([#28601](https://github.com/open-webui/open-webui/discussions/28601))
- **Community WoL proxies exist for exactly this**: `wake_wol` sniffs outbound SYNs to the inference server and sends a magic packet if ping fails; needs WoL in NIC + BIOS and root/CAP_NET_RAW. ([github.com/borislemer/wake_wol](https://github.com/borislemer/wake_wol)) `LLazarus` is an OpenAI-compatible proxy that wakes on request and exposes an idle flag so a helper script can `systemctl suspend`; "Letting all inference satellites run permanently not only consumes heaps of electricity, but may also reduce their lifespan"; it "does not implement client authentication." ([github.com/Skyslycer/LLazarus](https://github.com/Skyslycer/LLazarus))
- **macOS defaults fight you**: "Macs don't stay awake, restart after outages, or wake for network access by default"; "With the lid closed, macOS sleeps unless it sees power and an external display, so do not count on lid-closed use for a server"; auto-login (needed to start services at boot) requires FileVault off. ([sidemini.com, 5 Sep 2026](https://sidemini.com/blog/mac-as-always-on-llm-server/)) The ryanfleck LaunchDaemon "absolutely refused to start on boot, even as root!" for weeks until he learned FileVault must be disabled. ([ryanfleck.ca](https://ryanfleck.ca/2025/m4-mac-mini-llm-server/))
- **Tailscale on Windows after sleep**: "slow or stalled reconnect after wake from sleep when using an exit node; resolved by restarting service" (Windows 11 26H2, Tailscale 1.104.1, 19 Oct 2026, open, linked to #8734 from 2023). ([tailscale #21842](https://github.com/tailscale/tailscale/issues/21842))
- **Dual-use boxes unload models**: porkloin's llama-swap unloads after 10 idle minutes so the GPU is free for gaming, "a little annoying"; 30 s cold start. ([HN 48544986](https://news.ycombinator.com/item?id=48544986))

### 4.4 Firewalls and unattended start (Windows especially)

- Firewall rule must be on the Private profile; `setx` vs per-session `OLLAMA_HOST` confusion; must restart Ollama for env to take effect. ([mykolaaleksandrov.dev](https://www.mykolaaleksandrov.dev/posts/2025/07/ollama-network-setup/); [logarithmicspirals.com](https://logarithmicspirals.com/blog/using-tailscale-to-access-private-llms/))
- A Windows Firewall prompt "waited for interactive input, so the server appeared to hang when no user was logged in"; plain "At startup" Task Scheduler trigger unreliable; author resorted to auto-logon + delayed "At log on" trigger + locking the workstation instead of logging out. ([thundaxsoftware](https://thundaxsoftware.blogspot.com/2026/08/building-private-local-llm-server-on.html))
- Ollama "connection refused" from another machine is overwhelmingly the loopback default plus firewall; a maintainer in #2132 asked a user whether Ollama had been configured to bind 0.0.0.0. (Secondary: search summary; the issue page itself was not read, so treat as **unverified**.)

### 4.5 Mixed OS

- **Linux as the GPU box**: exo runs CPU-only on Linux ([exo README](https://github.com/exo-explore/exo)); Linux nodes are the ones that fail discovery (§4.2); Docker's interface grabbed exo's bind address on a DGX Spark (search summary of #1682, **unverified**, not read).
- **Windows as the GPU box**: WSL filesystem performance is poor enough that people run native Windows Ollama with autostart + Tailscale + Sunshine and "quietly forget about it"; NVIDIA sysmem fallback hurts WSL2 performance. ([HN 43649711, Apr 2025](https://news.ycombinator.com/item?id=43649711)) Vulkan on integrated Radeon needed `-ngl 10` and small batches to stay stable; a Windows security block on a DLL caused a "Bad Image" error. ([thundaxsoftware](https://thundaxsoftware.blogspot.com/2026/08/building-private-local-llm-server-on.html))
- **Mac as the GPU box**: LaunchDaemon + FileVault, lid-closed sleep, launchd ignoring `.zshrc` env (search summary, **unverified**), Local Network permission (exo #952).
- **Tailscale Serve + Ollama Host-header 403** is a Mac/Windows-agnostic surprise. ([logarithmicspirals.com](https://logarithmicspirals.com/blog/using-tailscale-to-access-private-llms/))

### 4.6 Performance expectations when splitting (exo-specific)

A review-cited exo issue reported a 2-node MLX + tinygrad cluster at 5 tok/s versus 48 tok/s on a single GPU (**unverified**: from a search summary, the issue was not read). The exo README itself says adding less capable devices slows individual latency while raising cluster throughput (search summary of README text; the fetched README emphasised tensor-parallel speedups of up to 1.8x on 2 devices and 3.2x on 4 for homogeneous Macs). ([exo README](https://github.com/exo-explore/exo)) The practical lesson this audience has absorbed: splitting across a laptop and a desktop usually makes things slower; run on the big box.

---

## 5. What would make them switch (grounded in the evidence)

Ranked by how often the pain appears in sources and how directly UCompute Mesh (as described) addresses it.

| # | Pain (evidence) | What they'd need to see | UCompute Mesh status (per brief) |
|---|---|---|---|
| 1 | Open port, no auth; proxy is "overkill for single-user" (#8536); Talos: token auth + isolation + audit | Pairing with a short code, pinned device keys, TLS by default, no `0.0.0.0` ever, deny-by-default for unpaired devices | Built (QUIC+TLS 1.3, pinned keys, local-only default). Say "no open unauthenticated port" explicitly and show the refusal of an unpaired request. |
| 2 | Hard-coded IPs; mDNS fails on Linux/guest Wi-Fi/after macOS restart (exo #1887, #2271, #952, README) | Discovery that works, **and** connect-by-address when it doesn't (exo removed `--bootstrap-peers`) | Built (address fallback). This is a concrete differentiator vs exo; demonstrate a Mac↔Windows pair on a network that blocks mDNS. |
| 3 | LM Link needs an account + Hub + its own tailnet; users want non-Tailscale transport (HN 48625932); login failures (HN 47163040) | No account, no coordination server, works offline on a LAN, open source | Built (local-only, Apache-2.0). Source not yet published is the credibility gap; "open source" claims will be checked. |
| 4 | Remote models should look local (LM Link's `localhost:1234` is the loved feature; porkloin points Crush at a tailnet DNS name) | OpenAI-compatible endpoint on the weak machine that routes to the chosen device, so Claude Code/OpenCode/Open WebUI need only a base URL | Built (local OpenAI-compatible API) + "choose which device runs a request." Document the exact base-URL swap for 3 popular tools. |
| 5 | Stale device access; "remove old devices" advice (dev.to); Cisco: audit | One-click revoke; audit log of off-device requests without prompt text | Built (revoke <0.1 s in tests; audit log). Minor but reassuring; mention once, not as a headline. |
| 6 | **GPU box sleeps mid-request; waking it is a hobby project** (#4072 open since 2024; Open WebUI #3526/#28601; wake_wol; LLazarus; Tailscale #21842) | Keep the serving device awake while a request runs; surface "device asleep/unreachable" clearly; optionally send WoL | **Not built.** Highest-value gap for this audience. Keep-awake-during-request is small (Ollama's own suggested fix is `SetThreadExecutionState` on Windows; macOS has `caffeinate`-style assertions). WoL is a later item. |
| 7 | Dual-use gaming box: VRAM contention, unload timers, cold starts (HN 48544986) | Memory-fit check before load (built in Run), explicit load/unload control, honest "this model won't fit next to your desktop session" | Partly built (memory-fit check). Idle unload policy is unverified/not described in brief. |
| 8 | Off-LAN access (most Tailscale users want phone/away access) | Relay/NAT traversal or a "bring your own Tailscale/WireGuard" story | **Not built** (no relay). Be explicit: Mesh is same-LAN today; Tailscale users can keep Tailscale for the away case. Do not imply remote access. |
| 9 | Mixed OS: Linux GPU support is where exo is weakest; our Linux is CPU-only too | Linux GPU (CUDA/Vulkan) on the serving side | **Not built** (Linux CPU-only daemon in tests). The "Mac laptop + Linux GPU box" persona cannot be served yet; say so. |
| 10 | Phone as second device (simonw, Hasnep, brewtide, LM Link on iPhone) | Mobile client | **Not built.** Out of scope; expect the question. |

---

## 6. Implications for messaging and where this audience is (for the $0, no-spam constraint)

- **Say what Mesh is in their words:** "run the whole request on the machine you choose; the laptop only needs the OpenAI base URL." Explicitly: not pooling, not splitting, not exo. This audience has read the exo issue tracker and knows splitting across unlike machines is slow and fragile; they will trust a tool that doesn't promise it.
- **Lead with the two pains that have the strongest paper trail:** unauthenticated open ports (four independent scans 2025-2026, three closed/declined Ollama auth issues) and discovery/pairing (exo's open issues). Keep sleep/wake as a stated roadmap item, not a claim.
- **Be honest about the three gaps the evidence says they'll ask about first:** sleep/wake, off-LAN access, Linux GPU. Each is a documented pain in the sources; pretending otherwise would be found out immediately.
- **Where the conversations happen (observed, for listening and for honest participation only):**
  - GitHub issues: ollama/ollama #4072 (sleep), #19045 (guard middleware), #8536/#1053 (auth); exo-explore/exo #1887, #2271, #952 (discovery); open-webui discussions #3526, #28601 (WoL); tailscale/tailscale #21842. Participation should be limited to genuinely useful, disclosed comments if any; the brief's platform-rules constraint applies.
  - Hacker News: recurring "Ask HN: local models for coding" and "Running local models is good now" threads (June 2026), "My local model setup on an M4 Pro Mac Mini" (Sept 2026), LM Link threads (Feb/June 2026). These threads are where the exact persona self-describes (porkloin, hkchad, bjackman, smalltorch).
  - Independent blogs that re-derive the setup every few months (aayushgarg.dev, logarithmicspirals.com, thundaxsoftware, ryanfleck.ca, mykolaaleksandrov.dev, sidemini.com). These authors are the natural early readers of an honest comparison doc.
- **Reddit (r/LocalLLaMA, r/selfhosted) could not be read** by this research tooling (domain blocked). It is almost certainly a primary venue for this audience; treat that as a known blind spot, not as absence of demand.

---

## 7. Verification notes and unverified items

- All numbers in §4.1's table come from pages read directly (Cisco, Censys, SecurityWeek, LeakIX, Tailscale).
- **Unverified (from search summaries, page not read or fetch failed):** Ollama app network toggle introduced in "v0.94" (digitalcitizen page returned 403); Mac Studio auto-wake Medium article's 4-7 s wake times (403); exo #1682 Docker bind interference; exo 2-node 5 tok/s vs 48 tok/s; ollama #2132 maintainer question; launchd ignoring `.zshrc` for `brew services`; LM Link shipping in LM Studio 0.4.6 (Feb 2026) per a third-party wiki whose page returned empty.
- **Contradiction flagged:** Hive Security's table says Ollama defaults to `0.0.0.0`; Ollama's FAQ says `127.0.0.1`. The FAQ is authoritative.
- **Not found:** any measured count of LAN-only (non-internet) exposed runners; any public 2025-2026 thread describing UCompute-style short-code pairing as a wish in those exact words. The wish appears indirectly (want non-Tailscale transport; want remote-host support in Ollama's app; want auth without a proxy).

---

## Sources (every URL read)

Primary runner docs and code
1. https://docs.ollama.com/faq
2. https://docs.ollama.com/windows
3. https://docs.ollama.com/macos
4. https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
5. https://lmstudio.ai/docs/developer/core/server/serve-on-network
6. https://lmstudio.ai/docs/lmlink/basics/faq
7. https://lmstudio.ai/link
8. https://lmstudio.ai/blog
9. https://lmstudio.ai/blog/locally-lm-link
10. https://github.com/exo-explore/exo

GitHub issues and discussions
11. https://github.com/ollama/ollama/issues/1053
12. https://github.com/ollama/ollama/issues/8536
13. https://github.com/ollama/ollama/issues/19045
14. https://github.com/ollama/ollama/issues/4072
15. https://github.com/open-webui/open-webui/discussions/3526
16. https://github.com/open-webui/open-webui/discussions/28601
17. https://github.com/exo-explore/exo/issues/363
18. https://github.com/exo-explore/exo/issues/879
19. https://github.com/exo-explore/exo/issues/952
20. https://github.com/exo-explore/exo/issues/1887
21. https://github.com/exo-explore/exo/issues/2271
22. https://github.com/tailscale/tailscale/issues/21842
23. https://github.com/borislemer/wake_wol
24. https://github.com/Skyslycer/LLazarus

Security research
25. https://blogs.cisco.com/security/detecting-exposed-llm-servers-shodan-case-study-on-ollama
26. https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys
27. https://www.securityweek.com/175000-exposed-ollama-hosts-could-enable-llm-abuse/
28. https://blog.leakix.net/2026/02/ollama-exposed/
29. https://tailscale.com/blog/AI-endpoints-on-public-web
30. https://hivesecurity.gitlab.io/blog/local-ai-tools-open-ports-security-risk/
31. https://dev.to/john_182319291/ollama-has-no-api-authentication-how-to-properly-gate-port-11434-48e3

Workflow write-ups (2025-2026)
32. https://tailscale.com/blog/self-host-a-local-ai-stack
33. https://logarithmicspirals.com/blog/using-tailscale-to-access-private-llms/
34. https://www.mykolaaleksandrov.dev/posts/2025/07/ollama-network-setup/
35. https://aayushgarg.dev/posts/2026-03-29-local-llm-opencode/
36. https://thundaxsoftware.blogspot.com/2026/08/building-private-local-llm-server-on.html
37. https://ryanfleck.ca/2025/m4-mac-mini-llm-server/
38. https://sidemini.com/blog/mac-as-always-on-llm-server/
39. https://dev.to/alichherawalla/how-to-use-a-remote-ollama-or-llamacpp-server-from-a-desktop-ai-app-on-windows-in-2026-40pa

Hacker News
40. https://news.ycombinator.com/item?id=44739632 (Ollama's new app, Jul 2025)
41. https://news.ycombinator.com/item?id=44742472 (SSH workaround subthread)
42. https://news.ycombinator.com/item?id=48544986 (porkloin 7900 XTX + Tailscale setup, Jun 2026)
43. https://news.ycombinator.com/item?id=47163040 (LM Link launch thread, Feb 2026)
44. https://news.ycombinator.com/item?id=48625932 (LM Link "future I want")
45. https://news.ycombinator.com/item?id=49529132 (M4 Pro Mac mini setup, Sep 2026)
46. https://news.ycombinator.com/item?id=43649711 (NixOS WSL Ollama on gaming PC, Apr 2025)
47. https://hn.algolia.com/api/v1/search?query=ollama%20tailscale&tags=comment&hitsPerPage=30
48. https://hn.algolia.com/api/v1/search?query=%22LM%20Link%22&hitsPerPage=30

Attempted, not readable (not cited for facts)
- https://medium.com/@michael.hannecke/sharing-ollama-across-your-lan-with-auto-wake-one-mac-studio-whole-team-cbf09eab8f48 (403)
- https://www.digitalcitizen.life/how-to-expose-ollama-to-the-network-on-windows/ (403)
- https://medium.com/@kibotu/two-paths-to-local-llm-servers-windows-nvidia-vs-mac-apple-silicon-1e28d606f600 (403)
- https://lmstudio.ai/docs/developer/core/server/authentication (404)
- https://wiki.linux-server-admin.com/web-apps/genai/lm-studio/history (empty body)
- reddit.com (domain not accessible to the search/fetch tooling)
