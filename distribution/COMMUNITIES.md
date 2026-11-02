# Community and channel database

Research date: **2026-10-30**. Written from `research/raw/channels-platform-rules.md` (primary; every platform rule below was read on the page cited, except where marked unverified) and the community sections of `research/raw/audience-local-ai-developers.md`, `audience-multi-device-developers.md`, `audience-ai-app-builders.md`, `audience-homelab-selfhosting.md` and `audience-oss-infra-and-researchers.md`.

**This file grants nothing.** `channels/REGISTRY.md` is the decision file; a channel is usable only when that file marks it AUTHORIZED with the owner's written grant quoted. Today nothing is AUTHORIZED. The GitHub organization `ucompute` exists (created by the owner 2026-10-30) but awaits the owner's written grant, so nothing is created or published under it. This file records what each platform's own rules allow, what the audience there looks like, and what Growth would do first if and when a grant arrives.

Status vocabulary (one primary status per surface; the "Gate today" line names what stands between the status and first use):

| Status | Meaning |
|---|---|
| `AUTOMATED_OK_WITH_DISCLOSURE` | The platform's written rules allow a project-branded account to post by automation if the automation is labelled/disclosed and the content rules are met |
| `HUMAN_ONLY` | A human must author and post; automated posting is prohibited or plainly against the surface's rules. Growth drafts; the owner (or a future human maintainer) posts |
| `PREREQUISITE_OWNER_ACCOUNT` | Usable only after the owner creates the account (Growth never creates accounts) and writes the grant into `channels/REGISTRY.md` |
| `SUITABLE_WHEN_SOURCE_PUBLIC` | Rules or norms require public source (a LICENSE-only repository does not count) |
| `SUITABLE_WHEN_RELEASED` | Rules or norms require something people can run without a gate |
| `REJECTED` | Excluded today, with the reason |

Fields per surface: URL; audience and size signal as read (or unverified); rules that govern an automated project-branded account, quoted with the URL they were read from; status; cadence norms; what to post first (only things truthful today: the five engineering notes in `content/ready/`); what Growth must never do there.

The five notes referred to below (all in `content/ready/`, claims-linted, canonical home pending the website handoff `handoffs/2026-10-30-website-engineering-notes.md`):
- **Pairing note:** "How two UCompute devices pair: the six-digit code, the keys and the revoke" (`2026-10-30-pairing-explainer`)
- **Audit note:** "What UCompute's audit log records, and what it never records" (`2026-10-30-what-the-audit-log-records`)
- **RPC note:** "llama.cpp's RPC backend is not a network transport, and what UCompute does instead" (`2026-10-31-loopback-rpc-vs-authenticated-transport`)
- **Memory-fit note:** "Before you load a model: how UCompute estimates whether a GGUF fits" (`2026-11-01-memory-fit-explainer`)
- **Base-URL note:** "Point the official OpenAI Python and JavaScript clients at a local server" (`2026-11-02-openai-client-base-url`)

---

## 0. Quick matrix

| Surface | Status | Gate today | First post (when gates clear) |
|---|---|---|---|
| Hacker News / Show HN | HUMAN_ONLY (Show HN also SUITABLE_WHEN_RELEASED) | a human submitter; Show HN needs a runnable public build | plain submission of the RPC note once live; Growth drafts an answer sheet |
| Lobste.rs | HUMAN_ONLY | invite; 70-day no-self-promo period | pairing note, after 70 days, by a human |
| Product Hunt | REJECTED (nothing publicly usable; project accounts cannot participate; bots are spam) | public release, then a named individual | none |
| daily.dev | REJECTED (programmatic and AI-generated content rejected; Growth's text is AI-written) | — | none |
| Reddit sitewide | HUMAN_ONLY (promotional bots are spam) | owner-created, human-operated account | answers to real questions, affiliation disclosed |
| r/LocalLLaMA | HUMAN_ONLY; rules unverified | same; 5 comment-karma reportedly required | answers; the owner's own words (LLM-written copy reportedly banned) |
| r/selfhosted | HUMAN_ONLY; rules unverified; project posts SUITABLE_WHEN_RELEASED | same | comments only; New Project Megathread after release |
| r/homelab | HUMAN_ONLY; rules unverified | same; moderator permission reportedly required | comments only |
| r/MachineLearning, r/artificial | HUMAN_ONLY; rules unverified | same | none planned |
| r/LocalLLM, r/LLMDevs, r/ollama | HUMAN_ONLY (sitewide); sub rules not researched | same | answers only |
| !selfhosted@lemmy.world | HUMAN_ONLY for the project account (automated posts/comments are spam there) | owner account, 30 days old before any promotion | [AIT] answers; later an [AIP] post of the audit note |
| !localllama@sh.itjust.works | HUMAN_ONLY (instance bot rules unverified) | owner account | answers |
| Fosstodon (Mastodon) | AUTOMATED_OK_WITH_DISCLOSURE (bot flag, replies answered, non-commercial) | PREREQUISITE_OWNER_ACCOUNT; canonical URL for the notes | pairing note as a short thread |
| Hachyderm (Mastodon) | HUMAN_ONLY for a Projects account (bots not allowed on it) | not pursued | none |
| mastodon.social | REJECTED (accounts may not consist solely of AI-generated content) | — | none |
| Bluesky | AUTOMATED_OK_WITH_DISCLOSURE (automation label) — **LIVE, AUTHORIZED 2026-11-01** (`channels/REGISTRY.md`) | none: `@ucompute.org` exists, bot label and disclosure bio set, post 1 pinned 2026-11-02 | done (post 1); queue in `content/ready/bluesky-first-posts.md`, 1/day, 4/week |
| dev.to (Organization) | AUTOMATED_OK_WITH_DISCLOSURE (AI assistance disclosed; no promotional AI-assisted articles) | PREREQUISITE_OWNER_ACCOUNT; canonical URL | base-URL note with disclosure and canonical link |
| Hashnode | REJECTED for automation (API is Pro-only since 2026-05-13); manual only | — | none |
| Medium | HUMAN_ONLY (programmatic posting is listed misuse); low priority | — | none |
| Substack | REJECTED (a newsletter collects emails; spec 29.5 needs owner authorization; no API) | — | none |
| X | REJECTED (no free API tier; scripting the website risks permanent suspension) | — | none |
| LinkedIn Page | REJECTED (needs a real-name member as Administrator) | — | none |
| YouTube | SUITABLE_WHEN_RELEASED (rules allow Data API uploads with AI disclosure) | a runnable build to record | none today |
| Discord: a UCompute server | REJECTED for now (the Community page says none exists; an empty server misleads) | public release | none |
| Discord: other projects' servers | HUMAN_ONLY (self-bots banned); peer questions only | owner's human account | none as the project |
| GitHub organization `ucompute` | AUTOMATED_OK_WITH_DISCLOSURE — **LIVE, AUTHORIZED** (`channels/REGISTRY.md`) | none; identity choice (own token vs GitHub App) still open as OWNER-ASKS 9 | done: profile README, `notes` repository and Pages site (8 notes on 2026-11-02, one new note a day at most) |
| GitHub Discussions (public repo) | SUITABLE_WHEN_SOURCE_PUBLIC | source publication (engineering B-007/D-028) | pinned "what exists / what does not" thread |
| Other projects' issue threads | HUMAN_ONLY; data-bearing comments only; any UCompute mention SUITABLE_WHEN_SOURCE_PUBLIC | — | none |
| awesome-selfhosted | REJECTED (needs a tagged release older than 4 months; LLM-generated PRs banned) | — | none |
| Ollama README integrations, janhq/awesome-local-ai, topic `openai-compatible` | SUITABLE_WHEN_SOURCE_PUBLIC | source publication | one PR each, by a human |
| Hugging Face local-apps; framework docs (AI SDK, Zed, Continue, Open WebUI, CrewAI, LiteLLM) | SUITABLE_WHEN_RELEASED | public installer and docs URL | provider page PRs |
| Console (console.dev) | SUITABLE_WHEN_RELEASED (pre-1.0 public build with self-service access) | release; project mailbox | one suggestion email |
| Changelog News | PREREQUISITE_OWNER_ACCOUNT (form needs sign-in; own technical work welcome) | account; canonical URL | RPC note URL |
| selfh.st weekly | SUITABLE_WHEN_RELEASED (submission criteria unverified) | release | Submit Content for a spotlight |
| TLDR / TLDR AI | REJECTED (paid placements only; no free submission route found) | — | none |
| Latent Space, It's FOSS Local AI Weekly, Import AI, Ben's Bites | SUITABLE_WHEN_RELEASED; earned only | release | one tip email where a tips address exists |
| Earned surfaces (Simon Willison, Alex Ziskind, Technovangelist, Jeff Geerling) | SUITABLE_WHEN_RELEASED; never pitched by automation | release | none |
| arXiv (cs.DC / cs.CR) | HUMAN_ONLY (named author); SUITABLE_WHEN_SOURCE_PUBLIC | a named human author | threat model and protocol note |
| Home Assistant community forum | SUITABLE_WHEN_RELEASED (tool calling unverified; the use case does not exist yet) | release with verified tool calling | none |
| TrueNAS / Unraid app catalogs | SUITABLE_WHEN_RELEASED (needs a maintained container image) | Linux container build | none |

---

## 1. Aggregators and forums

### 1.1 Hacker News and Show HN
- **URL:** https://news.ycombinator.com/ (Show HN: https://news.ycombinator.com/show)
- **Audience and size:** no member count published on the pages read. Signals in this niche: "The local LLM ecosystem doesn't need Ollama" 648 points / 207 comments (https://news.ycombinator.com/item?id=47788385); exo launch about 439 points / 151 comments (https://news.ycombinator.com/item?id=40973339); "Show HN: Open-source engine running Gemma 4 26B in 2 GB RAM on any M-series Mac" 919 / 342 (https://news.ycombinator.com/item?id=49098510); a long tail of 1-4 point "OpenAI-compatible local server" Show HNs with zero comments (https://hn.algolia.com/api/v1/search?query=local%20LLM%20OpenAI%20compatible%20server&tags=show_hn&hitsPerPage=20).
- **Rules for an automated project-branded account:**
  - Automation and generated text: "please don't automate posting." and "Please don't put generated text in HN posts." (https://news.ycombinator.com/newsguidelines.html)
  - Self-promotion: "Please don't use HN primarily for promotion. It's ok to post your own stuff part of the time, but the primary use of the site should be for curiosity." (https://news.ycombinator.com/newsguidelines.html)
  - Org accounts: "HN is a community—users should have an identity that others can relate to." and "Throwaway accounts are ok for sensitive information, but please don't create accounts routinely." (https://news.ycombinator.com/newsguidelines.html). Show HN: "The project must be something you've worked on personally and which you're around to discuss." (https://news.ycombinator.com/showhn.html)
  - Frequency: "a small number of reposts is ok. Otherwise we bury reposts as duplicates." and "Please don't delete and repost the same story." (https://news.ycombinator.com/newsfaq.html)
  - Votes: "Don't solicit upvotes, comments, or submissions." (https://news.ycombinator.com/newsguidelines.html); "Can I ask people to upvote my submission?" answered "No." (https://news.ycombinator.com/newsfaq.html); "Please don't ask friends to upvote or comment. That's not ok on HN." (https://news.ycombinator.com/showhn.html)
  - Show HN eligibility: "Show HN is for something you've made that other people can play with." "If your work isn't ready for users to try out, please don't do a Show HN." "Don't post landing pages or fundraisers." "Off topic: blog posts, sign-up pages, newsletters, lists, and other reading material." "Please make it easy for users to try your thing out, ideally without barriers such as signups or emails." (https://news.ycombinator.com/showhn.html)
  - Posting API: none; the official API documents read endpoints only (https://github.com/HackerNews/API)
- **Status:** `HUMAN_ONLY`. Show HN additionally `SUITABLE_WHEN_RELEASED`. Gate today: a human submitter (the owner); for Show HN, a public build with no gate.
- **Cadence norms:** self-promotion "part of the time"; one Show HN per real milestone; a small number of reposts tolerated; never delete-and-repost.
- **First post:** nothing by Growth. Growth drafts for the owner: a plain (not Show HN) submission of the RPC note once it is live at its canonical URL, plus an answer sheet for the predictable objections (bandwidth, "why not split", Linux, "where is the source"). The note's security backdrop (unauthenticated RPC, CVE-2026-34159, pinned engine build) is the most HN-shaped of the five.
- **Never:** submit, comment or vote from any automated or project-controlled account; paste generated text; solicit votes or comments; post a Show HN before a runnable public build; link the LICENSE-only repository; create accounts.

### 1.2 Lobste.rs
- **URL:** https://lobste.rs/ (rules: https://lobste.rs/about)
- **Audience and size:** "focused pretty narrowly on computing" (https://lobste.rs/about); no size read.
- **Rules:**
  - Self-promotion: "It's great to have authors participate in the community, but not to exploit it as a write-only tool" and "As a rule of thumb, self-promo should be less than a quarter of one's stories and comments in the last year."; new users are "not allowed to submit self-promo" during their first 70 days (https://lobste.rs/about)
  - Automation and generated text: no explicit user-bot rule; spam includes "content that is created without meaningful human authorship." (https://lobste.rs/about)
  - Accounts: invite-only; "The quickest way to receive an invitation is to talk to someone you recognize from the site." and "There's no official vetting process for new users, each user is responsible for inviting people" (https://lobste.rs/about). Brand accounts not addressed.
  - Limits: new users "can't send invites, submit links to domains we haven't seen submitted before" (https://lobste.rs/about)
  - Posting API: none documented (unverified)
- **Status:** `HUMAN_ONLY`. Gate today: an invited human account seeded by participation for 70 days.
- **Cadence norms:** self-promo under a quarter of stories plus comments over a year; none in the first 70 days.
- **First post:** none by Growth. If a human maintainer ever holds an account: the pairing note (QUIC, TLS 1.3, pinned device keys, revocation) after the 70-day period, under security and networking tags; never a product announcement.
- **Never:** seek an invite as the project; automate anything; submit text "created without meaningful human authorship".

### 1.3 Product Hunt
- **URL:** https://www.producthunt.com/
- **Audience and size:** not read.
- **Rules:**
  - Org accounts: "we require that profiles appear human and represent an individual, not a company, service, brand, or organization." (https://help.producthunt.com/en/articles/3615694-community-guidelines); "Product Hunt is a community of individuals, so company accounts cannot participate in forums, vote, or comment." (https://help.producthunt.com/en/articles/484973-can-our-company-account-vote-comment-or-post-on-product-hunt); "Register under your own name, not your company's or your product's." (https://help.producthunt.com/en/articles/17350772-launch-guide)
  - Bots and votes: "Mass messaging users, asking for upvotes, using bots, incentivizing upvotes" are unacceptable; "Self-promoting in comments will also be removed." (https://help.producthunt.com/en/articles/3615694-community-guidelines); "never ask outright for upvotes or run anything that requires them." (https://help.producthunt.com/en/articles/17350772-launch-guide)
  - Unreleased software: "We only feature products that are currently available."; not featured: "Waitlisted products (unless immediate access is provided)"; "No Vaporware: We only feature products that are ready for use or have a clear path to launch." (https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines)
  - API: "read-only" by default; "The Product Hunt API must not be used for commercial purposes." (https://api.producthunt.com/v2/docs)
- **Status:** `REJECTED` (nothing publicly usable; a project account cannot participate; bots are spam). After a public release it becomes `HUMAN_ONLY` under a named individual, which conflicts with founder anonymity unless a named maintainer fronts it.
- **Cadence norms:** "You can launch again every time you ship a major feature or update." (https://help.producthunt.com/en/articles/17350772-launch-guide)
- **First post:** none.
- **Never:** create a project-named profile; ask for upvotes; comment promotionally.

### 1.4 daily.dev
- **URL:** https://daily.dev/ (rules: https://docs.daily.dev/content-guidelines/)
- **Audience and size:** developer content aggregator; no size read.
- **Rules** (as summarised in `research/raw/audience-ai-app-builders.md` from https://docs.daily.dev/content-guidelines/; not verbatim): company and personal blogs are not eligible as sources; content primarily for self-promotion is rejected; programmatic or auto-populated content is rejected; AI-generated content and content with AI characteristics are rejected; paid distribution only through labelled Sponsored/Boost placements; the only auto-posting route (RSS/YouTube) is the paid Verified Company Squad; a free Squad is posted by a human.
- **Status:** `REJECTED` (reason: AI-generated and programmatic content are rejected regardless of who posts; Growth's notes are written by software; the paid Squad fails the $0 constraint).
- **First post:** none.
- **Never:** submit Growth-written text there under any account.

---

## 2. Reddit

Reddit's own domains (reddit.com, old.reddit.com, redditinc.com) were unreachable from the research tooling on 2026-10-30. Sitewide rules below come from Reddit's help center and Reddit's own filing with the New York Attorney General (which embeds the User Agreement). **Every subreddit-level rule below is unverified** (third-party mirrors only) and must be re-read on the live sidebar by a human before any post.

### 2.1 Reddit sitewide
- **URLs:** https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community ; https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy ; https://support.reddithelp.com/hc/en-us/articles/50051922501268-How-to-verify-you-re-human-when-asked-by-Reddit ; https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki ; https://ag.ny.gov/sites/default/files/social-media-policy-report/2025-q4-reddit-inc-policy.pdf
- **Audience and size:** see the subreddit rows.
- **Rules:**
  - Self-promotion: "On Reddit, promotional content is not inherently considered to be spam. That said, some communities do have strict policies that disallow any kind of promotional content. Other communities abide by the 10% rule: only 10% of your posting and comment history in the community can be self-promotional in nature, while the other 90% should be helpful, organic content unrelated to your personal interest." (https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community)
  - Promotional bots are spam: reportable spam includes "Programming bots that harm/break Reddit, including bots intended to promote content/products/services." and "Repeatedly posting the same or similar comments in a thread, community or across communities." and "Sending large amounts of chat messages or community invites to users who are not expecting them is also considered spam." (same URL)
  - Automated accounts and disclosure: "This section applies to all users and developers who use or develop apps –including bots, AI agents, or non-human operated accounts– with Reddit data." "Apps must register and create a developer profile to get an App profile label." "App accounts should solely be used to perform app functions (no mixed use accounts)." "Apps must not manipulate Reddit's features (e.g., voting, karma) or circumvent safety mechanisms (e.g., user blocking, account bans)." "Apps must not engage in spamming activity through automated posts, comments, or direct messages. This includes posting identical or substantially similar content across subreddits." "Approval is required: You must request access and get explicit approval before accessing any Reddit data through our API" (https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)
  - Label enforcement: "any account running automations needs to register their account and have it labeled as an app." "If you do not verify you're human within seven days, your account will be labeled as an app and may be restricted from posting and commenting until you do." (https://support.reddithelp.com/hc/en-us/articles/50051922501268-How-to-verify-you-re-human-when-asked-by-Reddit)
  - Org accounts: no sitewide ban on a project-named account was found in the pages read; "no mixed use accounts" means one account cannot be both an automated poster and a human participant.
  - API and limits: "Clients must authenticate with a registered OAuth token. We can and will freely throttle or block unidentified Data API users."; User-Agent format "<platform>:<app ID>:<version string> (by /u/<reddit username>)" and "NEVER lie about your User-Agent."; free tier "100 queries per minute (QPM) per OAuth client id"; "Traffic not using OAuth or login credentials will be blocked" (https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki). Commercial use needs "explicit written approval" (Responsible Builder Policy).
  - User Agreement: you may not "Access, search, or collect data from the Services by any means (automated or otherwise) except as permitted in these Terms or in a separate agreement with Reddit" (https://ag.ny.gov/sites/default/files/social-media-policy-report/2025-q4-reddit-inc-policy.pdf)
- **Status:** `HUMAN_ONLY` for anything about UCompute (an App-labelled account cannot promote; an unlabelled automated account violates the policy). Gate today: `PREREQUISITE_OWNER_ACCOUNT` (owner-created, human-operated project-named account).
- **Cadence norms:** the 10% rule as the common community norm; answers first.
- **First post:** none by Growth. For the owner's human-operated account: answers to real questions ("How do I point my app at a local OpenAI-compatible endpoint?", "Do my prompts leave my machine?") drawing on the base-URL and audit notes, affiliation disclosed in the comment; no project post until something is publicly usable.
- **Never:** run automation on the account; post the same text to several subreddits; vote on, or from, project-controlled accounts; send chats or invites; create a second account.

### 2.2 r/LocalLLaMA
- **URL:** https://www.reddit.com/r/LocalLLaMA/ (rules page unreachable: https://www.reddit.com/r/LocalLLaMA/about/rules/)
- **Audience and size (unverified, third-party trackers):** "861k members", "+307k members (55.6%)" yearly, tracker last updated Oct 28, 2026 (https://gummysearch.com/r/LocalLLaMA/); about 840k members per https://spacestationlabs.ai/subreddits/localllama. Dominant flairs in the sampled window: "Discussion", "Resources", "New Model", "Question | Help" (GummySearch). The "Best Local LLMs – Apr 2026" megathread reportedly reached 575 upvotes / 311 comments (https://bigguyonstuff.com/best-local-llm-2026-megathread-synthesis/, secondary). Latent Space's editor reads it "almost daily" (https://latent.space/p/ainews-top-local-models-list-april/).
- **Rules (UNVERIFIED; mirror https://willitstay.com/r/LocalLLaMA, "last checked Oct 28, 2026"):** "Posts must be related to Llama or the topic of LLMs."; "LLM based bots posing as humans are strictly not allowed."; "Completely/primarily LLM generated copy, code is not allowed." (exception only for non-native speakers using an LLM to translate or refine, disclosed); "The 1/10th rule is a good guideline: self-promotion should not be more than 10% of your content."; "Affiliation must be disclosed: No engagement farming, No 'I found this..', etc." Secondary (https://spacestationlabs.ai/subreddits/localllama, unverified): 5 karma earned inside the subreddit via comments before posting; links go directly to the source; projects use the Resources flair, never News; product launches posted as Discussion are commonly removed.
- **Status:** `HUMAN_ONLY`; treat as strict until the live rules are read. Gate today: `PREREQUISITE_OWNER_ACCOUNT`. Note the consequence of the reported LLM-copy rule: text written by Growth may not be posted there even by a human; the owner must write in their own words, using Growth's notes as source material only.
- **Cadence norms:** 10% self-promotion; comment karma before posting; hardware, quantisation and tokens-per-second specifics expected (every figure labelled "path check, not performance").
- **First post:** none by Growth. Owner, in own words: answers in "Question | Help" threads about pointing agents at local OpenAI-compatible endpoints and about memory fit.
- **Never:** post Growth-written copy; run an undisclosed bot; post a project launch before a public build; use a sensational title.

### 2.3 r/selfhosted
- **URL:** https://www.reddit.com/r/selfhosted/ (rules page unreachable)
- **Audience and size (unverified):** "had grown past 400K subscribers by mid-2025" (https://homenode.tech/r-selfhosted-summer-update-2025-flair-rules-analysis/, affiliate site).
- **Rules (UNVERIFIED; mirror https://willitstay.com/r/selfhosted, "last checked Oct 28, 2026"):** Rule 2 "Do not spam or promote your own projects too much." "Promoted apps must be production ready and have docs." "Only mention your service in comments if it's relevant and adds value."; Rule 5 "On Wednesdays, you may post dashboards or tools that help self-hosters provided it is flaired as such"; Rule 6 "Only in the current "New Project Megathread", you may post projects that are younger than 3 months.", age measured by "first public presence, e.g. git commit, social media post, etc."; no published karma or account-age minimums; standalone promo posts outside designated threads are removed. Secondary (homenode.tech, unverified): every post needs a controlled flair; "Product Announcement is restricted to actual product releases".
- **Status:** `HUMAN_ONLY`; project posts additionally `SUITABLE_WHEN_RELEASED` ("production ready and have docs"). Gate today: `PREREQUISITE_OWNER_ACCOUNT`.
- **Cadence norms:** New Project Megathread for projects under three months of public presence; Wednesdays for tools; comments only when relevant.
- **First post:** none by Growth. Owner: comments answering privacy and "home server runs the model" questions, drawing on the audit note; a New Project Megathread entry only after release with docs.
- **Never:** a standalone project post before release; mention UCompute in a comment where it does not answer the question; automation.

### 2.4 r/homelab
- **URL:** https://www.reddit.com/r/homelab/ (rules page unreachable; mirrors returned 404 or no text: https://www.threadotter.com/subreddit-rules/homelab)
- **Audience and size:** not read.
- **Rules (UNVERIFIED, search snippets only):** promotion only with moderator permission or in designated threads; sales belong in r/homelabsales; referral links and blogspam prohibited.
- **Status:** `HUMAN_ONLY`; rules unknown. Gate today: `PREREQUISITE_OWNER_ACCOUNT` plus moderator permission.
- **First post:** none by Growth; owner comments only.
- **Never:** any post about UCompute without moderator permission; automation.

### 2.5 r/MachineLearning and r/artificial
- **URLs:** https://www.reddit.com/r/MachineLearning/ , https://www.reddit.com/r/artificial/ (rules pages unreachable)
- **Rules (UNVERIFIED):** r/MachineLearning: [P] flair for projects, periodic "Self-Promotion Thread", strict on self-promo (https://www.reddit-radar-marketing.com/guides/r/machinelearning); r/artificial: promotion with moderator permission or in designated threads (https://www.threadotter.com/subreddit-rules/artificial).
- **Status:** `HUMAN_ONLY`; low fit (UCompute is infrastructure, not research). Nothing planned.

### 2.6 r/LocalLLM, r/LLMDevs, r/ollama
- **Audience and size (unverified, GummySearch):** r/LocalLLM "253k members" (https://gummysearch.com/r/LocalLLM/); r/LLMDevs "178k members" (https://gummysearch.com/r/LLMDevs/); r/ollama "142k members" (https://gummysearch.com/r/ollama/). Question shape seen on r/ollama: "Best Coding Model for Ryzen9/4060/64 GB Notebook?".
- **Rules:** not researched; sitewide rules apply.
- **Status:** `HUMAN_ONLY` (sitewide); subreddit rules to be read before any use. Gate today: `PREREQUISITE_OWNER_ACCOUNT`.
- **First post:** owner answers only (memory-fit and base-URL questions).

---

## 3. Fediverse: Lemmy

### 3.1 !selfhosted@lemmy.world
- **URL:** https://lemmy.world/c/selfhosted (rules posts: https://lemmy.world/post/48725669 , https://lemmy.world/post/49151085 , examples https://lemmy.world/post/49320548 ; instance terms: https://legal.lemmy.world/tos/)
- **Audience and size (read on the page 2026-10-30):** 63.3K subscribers, 5.92K monthly active users, 383 users/day (https://lemmy.world/c/selfhosted). The 17 Oct 2026 thread "Is anyone self-hosting their own AI?" reached 193 comments, score 159 (https://lemmy.world/api/v3/post?id=53242050).
- **Rules:**
  - Sidebar (verbatim): 2 "No spam." 4 "Don't duplicate the full text of your blog or readme if you're providing a link." 5 "Submission headline should match the article title." 7 "Promotion posts require active participation, with an account that is at least 30 days old." 8 "AI-related discussions and AI-involved promotional posts have additional requirements for tagging." (https://lemmy.world/c/selfhosted)
  - Detailed rules: "Promotion posts require your active participation in selfhosting or related communities"; account "at least 30 days old", "There are no exemptions from this requirement"; "no more than 10% of your posts or comments may be self-promotional, or your post will be removed" (account-wide); fully open-source, fully self-hostable projects are exempt from the 10% cap but "The exception does not exempt you from the account age requirement"; Rule 2 spam covers "Using scripts/bots/gen AI to automate posts and comments" and unsolicited DMs (https://lemmy.world/post/48725669)
  - Tags and AI disclosure: [CBH] "Code By Human"; [AIP] "AI Project" (AI used in development "in any capacity", disclosure required); [AIT] "AI Topic"; disclosure by linking an `ai-declaration.md` or listing categories (Design, Implementation, Testing, Documentation, Review, Deployment) with levels (Hint, Assisted, Pair, Generated); "[AIP] tag but no disclosure will be removed." (https://lemmy.world/post/49151085)
  - Instance bots: "Bots shall not be used for any kind of advertising."; bots must be labelled as bots with owner contact in the bio; may post only where community owners granted explicit permission; "Bots must not vote on content."; must not post multiple times per minute; Section 7: Lemmy.World is "not intended to be used as a marketing channel for extensive commercial advertising" (https://legal.lemmy.world/tos/)
  - API: Lemmy's API is free (standard instance API).
- **Status:** `HUMAN_ONLY` for the project account: automating posts or comments is spam under Rule 2, and a labelled bot needs explicit community-owner permission and may not advertise. Gate today: `PREREQUISITE_OWNER_ACCOUNT` (the 30-day clock starts at creation).
- **Cadence norms:** 30-day account age before any promotion; at most 10% promotional account-wide (UCompute, Apache-2.0, qualifies for the FLOSS exemption once source is public; the age rule still applies); one post per topic; tag every post.
- **First post:** by the owner on the project account: [AIT] answers in hardware and runtime threads with no UCompute links; the first project post, once source is public, an [AIP] link to the audit note with the full AI-use disclosure (Growth prepares the `ai-declaration.md` text honestly: Documentation - Generated for the notes).
- **Never:** automate posts or comments there; vote from any project-controlled account; duplicate a note's full text when linking; lead with the compute-credit direction; DM anyone.

### 3.2 !localllama@sh.itjust.works
- **URL:** https://sh.itjust.works/c/localllama (read via https://sh.itjust.works/api/v3/community?name=localllama)
- **Audience and size (read 2026-10-30):** 5,490 subscribers, 2,466 active users/month, 645 posts, created 8 June 2023. (!localllama@lemmy.world is dead: 3 subscribers, no posts, https://lemmy.world/c/localllama.)
- **Rules (verbatim, community sidebar):** 1 "No harassment or personal character attacks of community members." 2 "No comparing artificial intelligence/machine learning models to cryptocurrency." 3 "No comparing artificial intelligence/machine learning to simple text prediction algorithms." 4 "No implying that models are devoid of purpose or potential for enriching peoples lives." No self-promotion rule in the sidebar; the sh.itjust.works instance rules were not read (unverified).
- **Status:** `HUMAN_ONLY` (instance bot and promotion rules unverified; treat like lemmy.world). Gate today: `PREREQUISITE_OWNER_ACCOUNT`.
- **First post:** owner answers on memory fit and local OpenAI-compatible endpoints.
- **Never:** mention the compute-credit direction there (rule 2 reflex); automate.

---

## 4. Fediverse: Mastodon

### 4.1 Fosstodon
- **URL:** https://fosstodon.org/ (rules: https://fosstodon.org/api/v1/instance/rules ; Code of Conduct: https://hub.fosstodon.org/coc/ ; Mastodon bot flag: https://docs.joinmastodon.org/user/profile/)
- **Audience and size:** not read. "The theme of this instance is Free/Libre/Open-Source software and adjacent communities." (https://hub.fosstodon.org/coc/). selfh.st says it draws from "the #selfhosted and #homelab communities on Mastodon" (https://selfh.st/about/), so those hashtags are a discovery surface.
- **Rules:**
  - Self-promotion: Rule 8 "DO NOT post commercial promotions, or advertise" (https://fosstodon.org/api/v1/instance/rules); CoC: "DO NOT post commercial promotions, or advertise through posts that are exclusively links", including "repetitive self-promotion for profit"; encouraged: "toot your own horn and show us your authentic self" and "We want to know about cool things you are involved with and things you have achieved." (https://hub.fosstodon.org/coc/)
  - Automation: Rule 9 "DO NOT use automated tools to post without also monitoring and/or interacting from your account." (https://fosstodon.org/api/v1/instance/rules)
  - Disclosure: Mastodon bot flag: "Enabling the bot flag will add a bot icon to your profile. This icon will let others know that your profile may perform automated actions, or might not be monitored by a human." "Mastodon currently treats the bot flag as a visual indication only." (https://docs.joinmastodon.org/user/profile/)
  - Org accounts: not addressed; an Apache-2.0 project fits the theme.
  - Frequency: no numeric limit found.
  - API: free (standard Mastodon API).
- **Status:** `AUTOMATED_OK_WITH_DISCLOSURE`, conditional on: bot flag on; the account answers replies and mentions from the same account in every Growth session; no link-only or commercial posts. Gate today: `PREREQUISITE_OWNER_ACCOUNT`, plus a canonical URL for the notes. Open question for the instance admins before the first scheduled post: whether replies made by software in scheduled sessions satisfy Rule 9's "monitoring and/or interacting"; Growth asks once, from the account, quoting the rule, and does not post until answered.
- **Cadence norms:** Growth's own cap (section 10): at most 1 scheduled post per day and 4 per week; replies on demand.
- **First post:** the pairing note as a short thread (what the six-digit code does, what is pinned, how revoke works) linking its canonical URL, with #selfhosted and #homelab (two hashtags at most).
- **Never:** post without the bot flag; post while replies go unread; post link-only promotions; stuff hashtags; call anything commercial, priced or available.

### 4.2 Hachyderm
- **URL:** https://hachyderm.io/ (account-type docs: https://community.hachyderm.io/docs/account-types/ , https://community.hachyderm.io/docs/account-types/open-source-accounts/ , https://community.hachyderm.io/docs/account-types/bot-accounts/ , https://community.hachyderm.io/docs/account-types/corporate-accounts/ , https://community.hachyderm.io/docs/account-types/covenant/ , https://community.hachyderm.io/docs/account-types/verification/ ; https://hachyderm.io/about was blocked)
- **Audience and size:** not read.
- **Rules:**
  - Account types: Projects ("For Open Source Projects."), Automated ("Any posts that are programmatic and/or scheduled in nature."), Corporate ("For businesses, companies, and similar."); unrecognised specialised accounts "will be removed."; project usernames must match the project name (https://community.hachyderm.io/docs/account-types/)
  - Open-source project accounts: "We want to have one account for each project."; bots are not allowed on them: "we try to keep our content based around real words written by real people."; automated content only as part of mixed posting, the account "can't be dedicated to only publishing that type of content." (https://community.hachyderm.io/docs/account-types/open-source-accounts/)
  - Bot accounts: "All bots must be verified with Hachyderm"; "All bots must select the bot checkbox in their profile settings."; "Bots must be clearly marked as bots so that people can easily opt-out of bot posts if they wish."; most bots include #hachybots in every post; "upper limit of 5 curated/scheduled/automated posts per day"; "Reactionary bots may only be triggered / 'summoned' by posts that include their handle." (https://community.hachyderm.io/docs/account-types/bot-accounts/)
  - Covenant: "I agree to only share my message once." "We are explicitly trying to avoid the 'cron job' effect that we see on Twitter with promotional accounts." (https://community.hachyderm.io/docs/account-types/covenant/)
  - Corporate accounts: "Are invite-only."; "Pay a subscription cost as of 1 Mar 2023"; covers "businesses and business-like entities" including "certain types of projects" (https://community.hachyderm.io/docs/account-types/corporate-accounts/)
- **Status:** `HUMAN_ONLY` for a UCompute Projects account. A separate verified bot account (5 automated posts/day, #hachybots, non-promotional) is permitted by the rules but not pursued: Fosstodon serves the same audience with one account, and a project judged "business-like" becomes a paid, invite-only Corporate account.
- **Cadence norms:** "say it once"; 5 automated posts/day cap for bots.
- **First post:** none.
- **Never:** run automation on a Projects account; repost the same message.

### 4.3 mastodon.social
- **URL:** https://mastodon.social/ (rules: https://mastodon.social/api/v1/instance/rules)
- **Rules (six server rules read):** "Content created by others must be attributed, and use of generative AI must be disclosed"; accounts may not consist solely of AI-generated content (paraphrased in `research/raw/audience-homelab-selfhosting.md`; verbatim text to be re-read). No explicit spam or bot rule among the six.
- **Status:** `REJECTED` (reason: a Growth-operated account would consist solely of software-generated posts, which the instance's rule excludes; FOSS audience thinner than Fosstodon's).
- **Never:** use as a fallback without re-reading the rule verbatim.

---

## 5. Bluesky
- **URL:** https://bsky.app/ (guidelines: https://bsky.social/about/support/community-guidelines ; bot label announcement: https://bsky.app/profile/bsky.app/post/3mhgg5ja5gc2w ; labels: https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/moderation.md ; rate limits: https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/rate-limits.md)
- **Audience and size:** platform figures not read. For this niche: 142+ machine-learning starter packs listed as of Oct 2026, none specific to LLM infrastructure or open-source AI systems (https://blueskystarterpack.com/machine-learning); the OSS-infra research judges that the "infra/local-inference community has not visibly formed there". Best rules fit, weakest audience fit of the automated channels.
- **Rules:**
  - Spam and promotion: "Do not send spam or repeatedly post content in ways that disrupt normal conversations or service use."; commercial content must not be posted "without clearly identifying its commercial nature to other users."; "Do not artificially manipulate features or social signals to gain unearned reach or mislead users" (https://bsky.social/about/support/community-guidelines)
  - Automation and disclosure: "Bot labels are here. If you run an automated account, you can now mark it as such in your account settings. The label will show up on your profile and posts so people know what's a bot and what's not." "To mark your account as automated, go to Settings → Account → Automation label" "For now, bot labels are voluntary, and all existing policies continue to apply. We may introduce additional policies specific to automated accounts in the future." (https://bsky.app/profile/bsky.app/post/3mhgg5ja5gc2w). The self-label value "bot" "marks the account as automated" (https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/moderation.md)
  - Org accounts: allowed; "Do not impersonate others or official groups in ways that could mislead users"; creating "fake accounts to deceive others about who you are" is prohibited (https://bsky.social/about/support/community-guidelines). A domain handle (`@ucompute.org`) proves the project identity.
  - Rate limits: creates cost 3 points against a 5,000-point hourly and 35,000-point daily per-account budget (about 1,666 creates/hour, 11,666/day); 3,000 requests per 5 minutes per IP (https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/rate-limits.md)
  - API: free and open (AT Protocol); no pricing for write access.
- **Status:** `AUTOMATED_OK_WITH_DISCLOSURE`; **live since 2026-11-02 03:02 UTC** (owner grant 2026-11-01; account, DNS handle, bot label and disclosure bio in place). Canonical URLs: the notes site `https://ucompute.github.io/notes/`.
- **Cadence norms:** platform limits are far above any sane volume; Growth's own cap: at most 1 post per day and 4 per week; replies only to mentions and to replies on its own threads.
- **First post:** the pairing note as a short thread linking its canonical URL; second, the audit note. Each post labelled; the bio carries the disclosure wording in section 10.
- **Never:** post without the automation label; reply to strangers' posts found by search; auto-follow or auto-like; post the same text as the Mastodon account; imply a release exists.

---

## 6. Developer blogging platforms

### 6.1 dev.to (Forem)
- **URL:** https://dev.to/ (terms: https://dev.to/terms ; Code of Conduct: https://dev.to/code-of-conduct ; AI guidelines: https://dev.to/guidelines-for-ai-assisted-articles-on-dev ; API: https://developers.forem.com/api/v1 , https://developers.forem.com/api)
- **Audience and size:** not read. The audience research lists dev.to write-ups among the places multi-device and local-AI developers re-derive their setups.
- **Rules:**
  - Self-promotion: the site "is not designed primarily for the purposes of promotion or creating backlinks." "Posts must contain substantial content — they may not merely reference an external link that contains the full post." "If a post contains affiliate links, that fact must be clearly disclosed." (https://dev.to/terms)
  - AI disclosure: authors must "Disclose the fact that they were generated or assisted by AI in the post," either "upfront using the tag #ABotWroteThis or at any point in the article's copy."; AI-assisted articles should not "Promote any business, program, or course (including your own)." nor "Be published with the main purpose of building a personal brand, building a social media presence, or gaining clout."; users should not use bots or AI to write comments (https://dev.to/guidelines-for-ai-assisted-articles-on-dev). The Code of Conduct requires "disclosing AI assistance if used to create content" (https://dev.to/code-of-conduct)
  - Org accounts: "Organization Accounts" exist (navigation on https://dev.to/terms); creation rules unverified (page not retrieved). Company blogs may be shared under that company's organization (per the AI-app-builders research reading of the backlink exception).
  - Frequency: no limit stated on the pages read.
  - API: free; "All endpoints can be accessed with the 'api-key' header"; POST /api/articles "allows the client to create a new article."; "This API key can be generated by the user via their settings page in Forem." (https://developers.forem.com/api/v1 , https://developers.forem.com/api)
- **Status:** `AUTOMATED_OK_WITH_DISCLOSURE` for publishing substantive articles with the AI disclosure, under a UCompute Organization, with canonical URLs. Hard constraint: because Growth's text is software-written, every article is AI-disclosed, and AI-assisted articles may not promote the author's own project; an engineering note that explains UCompute's own design sits on that line. Growth therefore starts with the generic educational note and treats UCompute-specific notes on dev.to as an owner decision. Gate today: `PREREQUISITE_OWNER_ACCOUNT` (Organization), plus a canonical URL.
- **Cadence norms:** Growth's own cap: at most 1 article per week; substantial body, not a link stub.
- **First post:** the base-URL note ("Point the official OpenAI Python and JavaScript clients at a local server"), with the in-copy disclosure sentence from section 10 and `#ABotWroteThis`, canonical URL set to its ucompute.org page once the handoff lands. Candidate second: the memory-fit note (general GGUF sizing method), same disclosure.
- **Never:** write or post comments by software; publish an undisclosed AI-assisted article; publish a link-only post; publish a note whose purpose is to drive adoption of a product nobody can obtain.

### 6.2 Hashnode
- **URL:** https://hashnode.com/ (terms: https://hashnode.com/terms , effective February 15, 2026; API change: https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access ; Code of Conduct: https://hashnode.com/code-of-conduct)
- **Rules:**
  - Spam: prohibited to "Post or distribute spam, including unsolicited promotional content" and "automated content generation for the purpose of manipulating search results or engagement metrics." (https://hashnode.com/terms)
  - Automation: prohibited to "Scrape, crawl, or use automated means to access the Service in a manner that exceeds reasonable use or violates these Terms." and to "Attempt to circumvent any rate limits or access restrictions imposed on the API." (https://hashnode.com/terms)
  - API cost: "Every API request, queries and mutations, now requires a Pro plan on your publication." "Scrapers and spammers were abusing the free API at scale." (https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access); about $5/month per publication per a third-party post (unverified)
  - Org accounts: publications offer "custom branding and team collaboration" (https://hashnode.com/terms)
- **Status:** `REJECTED` for automation (paid API fails the $0 constraint); manual publishing would duplicate dev.to with no added audience evidence. Suggest `channels/REGISTRY.md` split the "dev.to / Hashnode" row accordingly (section 12).
- **Never:** use unofficial API access.

### 6.3 Medium
- **URL:** https://medium.com/ (rules: https://policy.medium.com/medium-rules-30e5502c4eb4 , "Updated June 2023"; mirror https://github.com/Medium/medium-policy/blob/master/Rules.md)
- **Rules:**
  - Self-promotion: "First party promotion is allowed, and you may promote and link to your own business, website, mailing list, or fundraiser." but spam includes "Posting content primarily to drive traffic to, or increase the search rankings of, an external site, product, or service" (https://policy.medium.com/medium-rules-30e5502c4eb4)
  - Automation: "Registering accounts, posting content, or interacting with users or content automatically, systematically, or programmatically" is prohibited; so is using "any software, script, robot, spider or other automatic device, process or means ... to access the Services for any purpose" (same URL)
  - Duplicates: "We do not allow posting duplicate copies of the same content to Medium, whether from a single account or across multiple accounts ... (You are allowed to cross-post content from your blog to Medium, provided you own the rights for the content.)" (same URL)
  - API: new integration tokens reportedly stopped around January 2025 (third-party; https://docs.n8n.io/integrations/builtin/credentials/medium/ ; help.medium.com returned 403; unverified)
- **Status:** `HUMAN_ONLY`, low priority (programmatic posting is listed misuse; no verified API; audience overlap with dev.to).
- **First post:** none planned.
- **Never:** automate; duplicate content across accounts.

### 6.4 Substack
- **URL:** https://substack.com/ (content guidelines: https://substack.com/content)
- **Rules:** "We don't permit publications whose primary purpose is to advertise external products or services" and "Brands and commercial organizations publishing on Substack may be subject to additional verification."; "We may intervene to remove accounts engaged in artificial or inauthentic activity on community surfaces."; "We don't allow imports of email addresses that were purchased, scraped, or harvested from third party websites." (https://substack.com/content). No official publishing API found (third-party tools use undocumented endpoints; unverified).
- **Status:** `REJECTED` for now, consistent with the Newsletter row in `channels/REGISTRY.md`: collecting emails needs its own owner authorization (spec 29.5), there is no API, and nothing to announce. Revisit at public release.
- **Never:** import or collect addresses; automate posting.

---

## 7. Other social platforms

### 7.1 X
- **URL:** https://x.com/ (automation rules: https://help.x.com/en/rules-and-policies/x-automation , "Updated April 2026"; labels: https://help.x.com/en/using-x/automated-account-labels ; developer guidelines: https://docs.x.com/developer-guidelines ; pricing: https://docs.x.com/x-api/getting-started/pricing)
- **Audience and size:** not read. Relevant handles seen: `@exolabs`, `@ggerganov`, `@awnihannun` (from project READMEs; follower counts unverified).
- **Rules:**
  - Automation: "Use non-API-based forms of automation, such as scripting the >x< website. The use of these techniques may result in the permanent suspension of your account."; "You may not post duplicative or substantially similar posts on one account or over multiple accounts you operate."; "sending automated replies to posts based on keyword searches alone is not permitted."; "the deployment or operation of any AI reply bot requires prior written and explicit approval from >x<." (https://help.x.com/en/rules-and-policies/x-automation)
  - Disclosure: automated accounts must "Enable the 'Automated' profile label", "Disclose in bio" that the account is a bot and who operates it, and tie it to "a human-managed account"; "No identical cross-posting." (https://docs.x.com/developer-guidelines)
  - Cost: post creation $0.015 per request, $0.200 per request for a post with a URL; no free tier (https://docs.x.com/x-api/getting-started/pricing)
- **Status:** `REJECTED` for now, consistent with `channels/REGISTRY.md` (every API post costs money; the only free automation route is a suspension offence; manual posting would need a human).
- **Never:** script the website; cross-post identical text.

### 7.2 LinkedIn Company Page
- **URL:** https://www.linkedin.com/ (User Agreement: https://www.linkedin.com/legal/user-agreement ; Pages Terms: https://www.linkedin.com/legal/l/linkedin-pages-terms ; help: https://www.linkedin.com/help/linkedin/answer/a1341387 , https://www.linkedin.com/help/linkedin/answer/100826 ; API: https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api)
- **Rules:** "Use bots or other unauthorized automated methods to access the Services" is prohibited; "you will only have one LinkedIn account, which must be in your real name" (https://www.linkedin.com/legal/user-agreement); "The Page must have at least one Administrator identified for the Page." "You will only use the Business Services to identify and promote your own Organization." (https://www.linkedin.com/legal/l/linkedin-pages-terms); "Create a LinkedIn profile with your real first and last name." (https://www.linkedin.com/help/linkedin/answer/100826). Organization posting via `w_organization_social` is gated behind the Marketing API Program; terms unverified (access page 404).
- **Status:** `REJECTED` (a real-name human administrator conflicts with founder anonymity; unofficial automation is a ban risk), consistent with `channels/REGISTRY.md`.

### 7.3 YouTube
- **URL:** https://www.youtube.com/ (spam policy: https://support.google.com/youtube/answer/2801973 ; fake engagement: https://support.google.com/youtube/answer/3399767 ; API quota: https://developers.google.com/youtube/v3/getting-started , https://developers.google.com/youtube/v3/docs/videos/insert)
- **Audience and size (third-party, unverified):** Alex Ziskind (@azisk) 578K subscribers, 1,229 videos, Oct 29, 2026, recent titles almost entirely local-AI hardware (https://vidiq.com/youtube-stats/channel/@azisk/videos/); Matt Williams / Technovangelist 96.3K subscribers (https://vidiq.com/youtube-stats/channel/@technovangelist/).
- **Rules:** prohibited: "Content created solely to drive users off of YouTube to external sites"; "Using automated tools or AI to churn out high volumes of similar content with minimal changes."; "Using high-volume, repetitive, or deceptive comments, live chats, or other messages"; disclosure: "Creators should disclose when content is generated or meaningfully altered with AI"; allowed: "It's okay to ask viewers to like, comment, or subscribe." (https://support.google.com/youtube/answer/2801973). Fake engagement: content that "artificially increases the number of views, likes, comments, or other metrics" is prohibited (https://support.google.com/youtube/answer/3399767). API: default quota "100 search.list calls, 100 videos.insert calls, and 10,000 units per day combined" (https://developers.google.com/youtube/v3/getting-started); uploads cost 1 unit of the 100/day upload bucket (https://developers.google.com/youtube/v3/docs/videos/insert). Free within quota.
- **Status:** `SUITABLE_WHEN_RELEASED`. The rules allow Data API uploads of genuine videos with AI disclosure (`AUTOMATED_OK_WITH_DISCLOSURE` by rule), but there is nothing truthful to film today: the private alpha runs behind an access gate and screen recordings risk exposing machine names and identity.
- **First post:** none today. Later: a screen recording of pairing two named devices with the six-digit code, every figure labelled "path check, not performance".
- **Never:** automate comments or engagement; ask the owner to buy views; publish AI-generated media undisclosed.

---

## 8. Discord

### 8.1 A UCompute server
- **URLs:** https://discord.com/guidelines ; https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy ; https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery
- **Rules:** Community Guidelines 14 "Do not use self-bots or user-bots." "Each account must be associated with a human, not a bot."; 13 "Do not send unsolicited bulk messages (or spam) to others."; 15 "Do not engage with our service in an inauthentic way." including "artificially inflating server membership, manipulating engagement metrics" (https://discord.com/guidelines). Developer Policy 5 "Do not contact users on Discord without their explicit permission."; 6 "Do not target users with advertisements or marketing."; 13 "This also includes automating messages to be sent for the purpose of maintaining activity in a Discord server." (https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy). Discovery: "Server must have at least 1,000 members to qualify." "Servers need to be at least 8 weeks old to be in Discovery." (https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery). Bots are free as Applications; a release-notes bot inside a human-owned server is within the rules.
- **Status:** `REJECTED` for now, consistent with `channels/REGISTRY.md`: the ucompute.org Community page says no community server exists, and a server without a usable product would be empty. Revisit at public release (then: a human-owned server, a labelled release-notes bot app, no activity simulation).
- **Never:** run a self-bot; automate messages to simulate activity; DM members.

### 8.2 Other projects' servers (listening and peer questions only)
- **Audience and size (Discord invite API, read 2026-10-30):** Hugging Face 245,049 members / 12,900 online (https://discord.com/api/v9/invites/hugging-face-879548962464493619?with_counts=true); Ollama 194,368 / 12,732 (https://discord.com/api/v9/invites/ollama?with_counts=true); LM Studio 79,743 / 6,927 (https://discord.com/api/v9/invites/lmstudio?with_counts=true); Unsloth AI 41,497 / 4,694 (https://discord.com/api/v9/invites/unsloth?with_counts=true); Jan 20,589 / 1,530 (https://discord.com/api/v9/invites/FTk2MvZwJH?with_counts=true). exo, Petals and distributed-llama servers are linked from their READMEs (https://github.com/exo-explore/exo , https://github.com/bigscience-workshop/petals , https://github.com/b4rtaz/distributed-llama); EleutherAI about 39.9k and Nous Research about 147k (search-only, unverified). llama.cpp has no official Discord found (unverified absence).
- **Rules:** Discord's self-bot ban above applies to any automated posting from a user account; each server's own rules were not read (unverified).
- **Status:** `HUMAN_ONLY`. Other projects' servers are not UCompute's channel: "Ask and answer technical questions; do not announce." (`research/raw/audience-oss-infra-and-researchers.md`).
- **First post:** none as the project.
- **Never:** announce UCompute; automate; DM members; recruit.

---

## 9. GitHub surfaces

### 9.1 Organization `ucompute` (profile README, a `notes` repository, organization Discussions)
- **URL:** https://github.com/ucompute (zero public repositories at 2026-10-30 16:56 UTC; this account is an admin; no written grant yet)
- **Audience and size:** the repositories this audience watches, star counts read 2026-10-30: ollama/ollama 185.3k, open-webui/open-webui 157.2k, ggml-org/llama.cpp 132.8k, vllm-project/vllm 95.9k, exo-explore/exo 48.1k, janhq/jan 45.2k, LostRuins/koboldcpp 12.1k, mostlygeek/llama-swap 6.1k (https://github.com/ollama/ollama , https://github.com/open-webui/open-webui , https://github.com/ggml-org/llama.cpp , https://github.com/vllm-project/vllm , https://github.com/exo-explore/exo , https://github.com/janhq/jan , https://github.com/LostRuins/koboldcpp , https://github.com/mostlygeek/llama-swap).
- **Rules:**
  - Promotion: account content "should not be advertising or promotional marketing."; prohibited: "automated excessive bulk activity and coordinated inauthentic activity", "inauthentic interactions, such as fake accounts and automated inauthentic activity;", "rank abuse, such as automated starring or following;"; no advertising in others' accounts "such as by posting monetized or excessive bulk content in issues." (https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)
  - Machine accounts and apps: "Accounts registered by "bots" or other automated methods are not permitted." "You may maintain no more than one free machine account in addition to your free Personal Account." "the owner of the Account is ultimately responsible for the machine's actions." (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service); "we recommend building a GitHub App" for long-lived integrations; "GitHub Apps can act independently of a user." (https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app)
  - Organizations and Discussions: "You can use organizations for free, with GitHub Free" (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts); organization-level discussions are "for broader conversations that span multiple repositories" (https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)
  - Rate limits: "personal rate limit of 5,000 requests per hour"; "no more than 80 content-generating requests per minute and no more than 500 content-generating requests per hour." (https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
  - API: free.
- **Status:** `AUTOMATED_OK_WITH_DISCLOSURE` (automation runs as a GitHub App with a bot identity, never as a second human-looking account). Gate today: the owner's written grant (OWNER-ASKS 3), which `channels/REGISTRY.md` records as pending. Nothing is created or published under the organization until then.
- **Cadence norms:** commits and releases are not posts; Discussions announcements at most one per note; no automated starring or following.
- **First post (after the grant):** the organization profile README (one claims-clean paragraph plus the status line "private alpha, no public release, source not yet published"), then a public `notes` repository holding the five engineering notes with a feed via GitHub Pages or releases, which also gives Bluesky, Mastodon and dev.to their canonical URLs if the website handoff is slower.
- **Never:** push to or link the LICENSE-only source repository; create repositories before the grant; star, follow or open issues by automation; put identity material in commits (author identity on commits is the owner's decision).

### 9.2 Discussions on the public source repository
- **URL:** https://github.com/ucompute (repository to be published by engineering; owner decision B-007/D-028)
- **Rules:** "Repository owners and people with write access can enable GitHub Discussions" (https://docs.github.com/en/discussions/quickstart). Same AUP and rate limits as 9.1.
- **Status:** `SUITABLE_WHEN_SOURCE_PUBLIC`. Growth never pushes to that repository (`channels/REGISTRY.md` HANDOFF row); it proposes Discussions categories, templates and a pinned thread through `handoffs/`.
- **First post:** a pinned "What exists today and what does not" thread mirroring the claims registry; the RPC note as the first technical thread.
- **Never:** publish before source; answer by automation without the bot identity.

### 9.3 Other projects' issue threads (forums in practice)
- **URLs:** https://github.com/ollama/ollama/issues/4643 (multi-machine Ollama; opened 26 May 2024, still active 18 Oct 2026, 61 thumbs-up on the original post); ollama/ollama #4072 (sleep), #19045, #8536, #1053 (auth); exo-explore/exo #1887, #2271, #952 (discovery); open-webui discussions #3526, #28601 (Wake-on-LAN); tailscale/tailscale #21842 (from `research/raw/audience-multi-device-developers.md`).
- **Rules:** GitHub AUP forbids advertising in others' accounts (9.1). The OSS-infra research: "A single comment with measured whole-request routing numbers, once public, is legitimate; a product plug is not."
- **Status:** `HUMAN_ONLY`; any UCompute mention `SUITABLE_WHEN_SOURCE_PUBLIC`.
- **First post:** none. Later, one data-bearing comment in ollama/ollama#4643 by a human, with reproducible numbers and the RPC note linked.
- **Never:** automated comments; more than one comment per thread about UCompute; linking the LICENSE-only repository.

### 9.4 Lists, topics and directories
- **awesome-selfhosted** (https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/CONTRIBUTING.md): "Any software project you are adding was first released more than 4 months ago." (counted from the first tagged release); "Machine/LLM-generated contributions are not allowed and will result in a ban."; "Software with no development activity for 6-12 months may be removed from the list."; excluded: "Desktop, mobile, or command-line apps that need a separate sync or server program". GenAI tag lists 13 projects today (https://awesome-selfhosted.net/tags/generative-artificial-intelligence-genai.html). Status: `REJECTED` until four months after the first tagged release, then a human-authored PR. Never: a Growth-written PR.
- **Ollama README "Community Integrations"** (about 150 entries; "Want to add your project? Open a pull request." https://github.com/ollama/ollama), **janhq/awesome-local-ai** (about 2.0k stars; "Your contributions are always welcome!" https://github.com/janhq/awesome-local-ai), **GitHub topic `openai-compatible`** (6,669 repositories; partly spam-polluted; https://github.com/topics/openai-compatible): Status `SUITABLE_WHEN_SOURCE_PUBLIC`; one PR each by a human; the topic is added by the repository owner. Never: list a LICENSE-only repository.
- **Hugging Face "Use this model" local apps** (https://huggingface.co/docs/hub/local-apps ; https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/src/local-apps.ts): "add new apps there and suggestions are welcome... If possible, you need to support deeplinks and be as cross-platform as possible"; needs a public, runnable product and a docs URL. Status `SUITABLE_WHEN_RELEASED`.
- **Framework docs** (Vercel AI SDK https://ai-sdk.dev/providers/openai-compatible-providers ; Zed https://zed.dev/docs/ai/use-a-local-model.md ; Continue https://docs.continue.dev/customize/model-providers/more/llamacpp ; Open WebUI https://docs.openwebui.com/alternatives/lm-studio.md ; CrewAI https://docs.crewai.com/en/concepts/llms ; LiteLLM https://docs.litellm.ai/docs/providers/openai_compatible): a provider page must point at a working server. Status `SUITABLE_WHEN_RELEASED`. The base-URL note is the draft of such a page.

---

## 10. Newsletters, editorial and earned surfaces

| Surface | URL | Audience / size as read | Rules or criteria quoted | Status | First action |
|---|---|---|---|---|---|
| Console | https://console.dev/selection-criteria ; https://console.dev/about | "30k+ subscribers", weekly, Thursdays | "Console features 2-3 interesting developer tools each week"; "the release must be pre 1.0 and/or have an appropriate label in the version number."; "Any GA or stable releases are not eligible."; "We do not do sponsored reviews."; submit by email to hello@console.dev | `SUITABLE_WHEN_RELEASED` (needs self-service access; the gated alpha does not qualify) | one suggestion email from the project mailbox (OWNER-ASKS 2) |
| Changelog News | https://changelog.com/news/submit | not read | form requires sign-in; asks for URL, title and "What's interesting about it?"; own work welcome; "if your fellow devs will find it interesting, submit it."; how-tos and commercial products not wanted | `PREREQUISITE_OWNER_ACCOUNT` | submit the RPC note's canonical URL once live |
| selfh.st weekly | https://selfh.st/ ; https://selfh.st/about/ ; https://selfh.st/submit/ | "over 35,000 subscribers", every Friday; Content Spotlight features one project per issue (PatchMon 23 Oct 2026, Homelable 16 Oct 2026: https://selfh.st/weekly/2026-10-23/ , https://selfh.st/weekly/2026-10-16/) | submission criteria unverified (script-rendered page); draws from r/selfhosted, awesome-selfhosted and Mastodon #selfhosted/#homelab | `SUITABLE_WHEN_RELEASED` | Submit Content once a Linux/container path exists; read the 2026 survey AI section (results early November 2026, https://selfh.st/survey/2026-open/) first |
| TLDR / TLDR AI | https://tldr.tech/ ; https://advertise.tldr.tech/ | TLDR AI claims about 1.1M subscribers; TLDR overall "8M+" (advertise page) | only an "Advertise" route; no free submission found | `REJECTED` (paid only) | none |
| Latent Space | https://www.latent.space/about | no audience number published; recap covers 12 subreddits and about 544 X accounts | tips: tips@latent.space; no guest form | `SUITABLE_WHEN_RELEASED`, earned only | one tip email when something public and technically interesting exists |
| Ben's Bites | https://www.bensbites.com/ | "Over 117,000 subscribers" | no submission path on the page (unverified) | `SUITABLE_WHEN_RELEASED`, earned only | none |
| It's FOSS Local AI Weekly | https://itsfoss.com/local-ai-weekly/ | weekly, Wednesdays; no count shown; author prefers replicable setups to benchmark charts | no submission path read | `SUITABLE_WHEN_RELEASED`, earned only | none |
| Import AI | https://jack-clark.net/ | not read | picks technical reports with primary links | `SUITABLE_WHEN_RELEASED`, earned only | none |
| Simon Willison, `local-llms` tag | https://simonwillison.net/tags/local-llms/ | 165 posts under the tag | n/a (personal blog) | `SUITABLE_WHEN_RELEASED`, earned only; never pitched by automation | none |
| YouTube creators (Alex Ziskind, Technovangelist, Jeff Geerling) | https://vidiq.com/youtube-stats/channel/@azisk/videos/ ; https://vidiq.com/youtube-stats/channel/@technovangelist/ ; https://www.jeffgeerling.com/ | 578K / 96.3K subscribers (third-party, unverified); Geerling publishes failures and cost | n/a | `SUITABLE_WHEN_RELEASED`, earned only | none |
| arXiv cs.DC / cs.CR | https://arxiv.org/list/cs.DC/recent | 36 new cs.DC submissions on 30 Oct 2026 | requires a named author (endorsement system) | `HUMAN_ONLY`; `SUITABLE_WHEN_SOURCE_PUBLIC` | a threat-model and protocol note, if a named human author exists |
| Home Assistant community forum | https://community.home-assistant.io/guidelines | build logs draw replies for months (https://community.home-assistant.io/t/my-journey-to-a-reliable-and-enjoyable-locally-hosted-voice-assistant/944860) | "Don't post spam or otherwise vandalize the forum." | `SUITABLE_WHEN_RELEASED` (tool calling unverified; the HA use case does not exist yet) | none |
| TrueNAS Apps / Unraid Community Applications | https://apps.truenas.com/catalog/open-webui_community/ ; https://ca.unraid.net/apps/open-webui-0z497h31ntbiab | Open WebUI badge "5,000 active deployments" (badge, not official) | needs a maintained container image | `SUITABLE_WHEN_RELEASED` (Linux container build) | none |

---

## 11. Operating rules Growth adopts

These are Growth's own rules, stricter than any platform rule above, and apply on every surface once `channels/REGISTRY.md` authorizes it.

1. **Disclosure wording for automated accounts.** Bio on Bluesky, Mastodon and dev.to, and the description of the GitHub App:
   > Automated account for the UCompute project (Apache-2.0; source not yet published; in development, no public release). Posts and replies are written and scheduled by software operating for the project and are reviewed in scheduled sessions, not in real time. No human is represented here. Every technical statement is checkable at the linked source.
   Platform flags in addition to the bio: Bluesky automation label on; Mastodon bot flag on; dev.to `#ABotWroteThis` plus this in-copy sentence: "This article was written by UCompute's automated growth workstream from the project's engineering records; the facts are independently checkable at the linked sources."; GitHub automation runs as a GitHub App whose name ends in `[bot]`. A project mailbox (OWNER-ASKS 2) is added to the bio when it exists. No account is created by Growth.
2. **Frequency caps.** Per automated account: at most 1 scheduled post per day and 4 per week; at most 1 dev.to article per week; at most 1 Discussions announcement per note; a given note is not posted to the same channel twice within 30 days; API usage stays below 10% of each platform's published limit with a single honest client identity and back-off on any 429.
3. **Answer questions first.** On every surface where the account may participate, it answers before it announces: replies to mentions and to replies on its own threads are handled in every session before any new post is scheduled; at least three useful non-promotional contributions (answers, corrections, data) precede each post about UCompute; no post about UCompute in the first 30 days of any community account (the lemmy.world rule applied everywhere). The account never replies to strangers' posts found by keyword search, never auto-follows, never auto-likes. On human-only surfaces the owner's account follows the same norm, in the owner's own words where the community bans LLM-written text.
4. **No cross-posting identical text.** Each note has one canonical URL (ucompute.org via the website handoff, or the `notes` repository once granted). Every channel gets text written for that channel; the same wording never appears on two platforms; a note's full text is never duplicated where the community forbids it (lemmy.world rule 4, Medium's duplicate rule); every syndicated copy carries the canonical link.
5. **No vote solicitation, no engagement manipulation.** Never ask for upvotes, likes, stars, follows, comments or submissions anywhere; never vote, star or follow from any project-controlled account on project content; no coordination of votes; no second accounts.
6. **Truth and labels.** Every sentence about the product maps to a claim ID in `claims/registry.json` and passes `scripts/claims_lint.py`; tokens-per-second figures are always labelled "path check, not performance"; direction is labelled as direction and kept out of technical posts; the LICENSE-only repository is never linked; nothing implies a release, a download or a sign-up exists.
7. **Identity.** The public identity is UCompute; no founder name, handle, affiliation, machine name, tester or private repository appears; no invented human.
8. **Opt-out and contact.** Blocks, mutes and "stop" are honoured permanently; no DMs; at most one question to any moderation team, and no post on that surface until it is answered.
9. **Record.** Every publish is recorded in `content/published/INDEX.md` and `journal/LOG.md` with URL, timestamp, channel and piece id; the channel's row here is re-read before each publish; measurement is scheduled at 7 and 30 days in `analytics/`.
10. **Human-only surfaces.** Growth drafts and prepares answer sheets; a human submits and answers; Growth never operates those accounts.

---

## 12. Blocked or unverified

Sources the research could not read on 2026-10-30, and claims that rest on secondary sources:

- **Reddit subreddit rules were unreachable.** https://www.reddit.com/r/LocalLLaMA/about/rules/ , https://www.reddit.com/r/selfhosted/about/rules/ , https://www.reddit.com/r/homelab/about/rules/ , https://www.reddit.com/r/MachineLearning/about/rules/ , https://www.reddit.com/r/artificial/about/rules/ and their old.reddit.com equivalents were blocked for both fetch tools, as was web.archive.org. Everything in sections 2.2-2.6 about subreddit rules comes from third-party mirrors (willitstay.com, spacestationlabs.ai, intoru.ai, threadotter.com, homenode.tech, reddit-radar-marketing.com) and is unverified; r/homelab has no readable rule text anywhere. A human must read the live sidebars before any post.
- **Reddit sitewide:** https://redditinc.com/policies/reddit-rules and https://www.redditinc.com/policies/content-policy blocked; https://support.reddithelp.com/hc/en-us/articles/360043504951 and .../204536419 return "The page you were looking for doesn't exist"; the verbatim text of Reddit Rule 2 is unverified. Subreddit sizes are third-party tracker figures (GummySearch, spacestationlabs, homenode), not read on Reddit.
- **Medium:** help.medium.com returned 403; the claim that new integration tokens stopped in January 2025 rests on third-party reports.
- **Substack:** no official publishing API found; third-party tools only.
- **Hashnode:** the about $5/month Pro price is third-party; whether free plans still allow unrestricted manual publishing is unverified.
- **LinkedIn:** Marketing API / Community Management API access page returned 404; whether approval is free is unverified.
- **dev.to:** Organization account creation rules were not retrieved (page content missing).
- **X:** whether the Automated label is available outside the "test group" described on the help page, versus the developer guidelines' requirement to enable it, is unresolved.
- **Hachyderm:** https://hachyderm.io/about and its rules API were unreachable; account-type docs on community.hachyderm.io were used.
- **Fosstodon:** https://fosstodon.org/about is script-rendered; rules came from the instance rules API and the CoC hub.
- **mastodon.social:** only the six API-listed rules were read; the "solely AI-generated content" rule is paraphrased in the audience research and needs a verbatim re-read.
- **sh.itjust.works:** instance-level rules not read; only the community sidebar was.
- **selfh.st:** https://selfh.st/submit/ is script-rendered; submission criteria unknown.
- **TLDR:** no free editorial submission route found; may not exist.
- **Ben's Bites, It's FOSS Local AI Weekly, Import AI:** no submission path read; treated as earned-only.
- **Console:** https://console.dev/submit/ returned 404; the email route on the selection-criteria page was used.
- **Discord servers of other projects:** member counts come from Discord's invite API (verified); per-server rules were not read; EleutherAI and Nous Research counts are search-only.
- **YouTube creator figures:** vidiq.com third-party stats, not YouTube.
- **Bluesky audience fit:** platform user figures are search-only; the absence of an LLM-infrastructure community there is an inference from starter-pack listings.
- **awesome-selfhosted:** the CONTRIBUTING file moved to awesome-selfhosted-data (the old path returned 404); the data repository's file was read.
- **Bluesky bots starter page** (https://docs.bsky.app/docs/starter-templates/bots) redirected; content not available.

---

## 13. Suggested updates to `channels/REGISTRY.md` (non-binding; the registry decides)

- Split "dev.to / Hashnode": dev.to stays PREREQUISITE (rules allow API publishing with AI disclosure); Hashnode becomes REJECTED for automation (Pro-only API since 2026-05-13).
- "Mastodon (a FOSS-friendly instance)": name Fosstodon as the instance (bot flag plus answered replies; non-commercial); record Hachyderm as HUMAN_ONLY for a Projects account and mastodon.social as rejected for a software-only account.
- Reddit row: add that r/LocalLLaMA reportedly bans LLM-written copy outright (unverified), so even the owner's posts there must be in the owner's own words; add the Lemmy communities (!selfhosted@lemmy.world, !localllama@sh.itjust.works) as PREREQUISITE, human-operated, with the 30-day clock.
- Add daily.dev (REJECTED: AI-generated and programmatic content rejected) and YouTube (WHEN_RELEASED; rules allow disclosed automated uploads).
- The three accounts to ask the owner to create first, in this order: Bluesky (`@ucompute.org` domain handle), Fosstodon, dev.to Organization. Each needs the project mailbox (OWNER-ASKS 2) first and the written grant line (OWNER-ASKS 3) after. The GitHub organization needs only the grant line.

Nothing in this file authorizes publication. Research date 2026-10-30; re-read platform pages before each registry change.

---

## 14. Weekly review 2026-W45 (2026-11-02, cloud weekly)

Evidence gathered this week and what it changed:
- **Bluesky:** community guidelines re-read 2026-11-02 at https://bsky.social/about/support/community-guidelines ("Last Updated: September 19, 2025"; spam and undisclosed-commercial-content rules unchanged). Status moved from PREREQUISITE to live/AUTHORIZED (owner grant, account live). Audience fit unchanged: still the weakest audience of the automated channels; the account had 0 followers at the 2026-11-02 baseline. Watch follower count and replies in the daily Actions file (`bluesky_account`); this is the first channel where Growth can observe any reaction at all.
- **GitHub organization / notes site:** live; 8 notes on 2026-11-02, 2 more scheduled (2026-11-03, 2026-11-04). 0 stars, 0 watchers, 0 org followers in every Actions file of the week.
- **Fosstodon and dev.to:** rules **not re-read** this week: `fosstodon.org` and `dev.to` both fail from the cloud session with `getaddrinfo ENOTFOUND` (outside the session's allowed network domains). Statuses unchanged (PREREQUISITE). Fosstodon remains the next account to ask for (OWNER-ASKS 3).
- **Reddit, Lemmy, Hacker News, Lobste.rs, Product Hunt and the rest:** no new evidence; statuses unchanged. Nothing is publicly usable, so every SUITABLE_WHEN_RELEASED / WHEN_SOURCE_PUBLIC row stays gated.
- **selfh.st 2026 survey:** results not yet published (web search 2026-11-02 found only the 2025 results at https://selfh.st/survey/2025-results/); re-check next week for the homelab audience re-read.
