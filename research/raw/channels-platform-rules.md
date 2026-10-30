# Channels and platform rules for a project-branded, heavily automated, $0-budget account

Research lens: channels-platform-rules
Date researched: 2026-10-30
Subject: UCompute (Apache-2.0, pre-release, source not yet published; local llama.cpp runner with local OpenAI-compatible API; UCompute Mesh = pick which of your own LAN devices runs a whole request over QUIC + TLS 1.3 with pinned device keys).
Operating constraints assumed: project-branded (not personal) account, heavy automation, $0 paid budget, no spam, no fake accounts, no vote manipulation, founder stays anonymous.

Method: primary policy pages were read with WebFetch or, where WebFetch was blocked, with the desktop browser pane. Reddit's own domains (reddit.com, old.reddit.com, redditinc.com) were blocked by both tools; the sitewide Reddit material below comes from Reddit's help center (support.reddithelp.com) and from Reddit's own transparency filing with the New York Attorney General, which embeds the User Agreement. Subreddit-level rules could not be read and are marked unverified. Every quote carries the URL it was read from. Anything not read directly is marked "unverified".

Legend for verdicts:
- AUTOMATE+DISCLOSE: a project account may post via automation if it is labeled/disclosed as automated and the content rules below are met.
- HUMAN-ONLY: a human must author and post; automation of posting is prohibited or would plainly violate the channel's rules.
- REJECT (for now): rules exclude the project at its current stage (pre-release) or at $0, or a brand/automated account is prohibited.

---

## 1. Summary matrix

| Channel | Brand/project account allowed? | Automated posting allowed? | Disclosure required? | Self-promotion rule (short) | Free posting API? | Verdict |
|---|---|---|---|---|---|---|
| Hacker News / Show HN | Not prohibited, but "users should have an identity that others can relate to" | No: "please don't automate posting" | n/a | "It's ok to post your own stuff part of the time"; Show HN needs something people can try | No (API is read-only) | HUMAN-ONLY; Show HN only after a runnable release |
| Reddit (sitewide) | Yes | Only as a registered, App-labeled single-purpose account; promotional bots are spam | Yes: automated accounts must register and carry the App label | Promotion "not inherently" spam; many subs use a 10% rule | Yes, with approval; 100 QPM per OAuth client | HUMAN-ONLY for promotion; App-labeled bot cannot be used to promote |
| r/LocalLLaMA, r/selfhosted, r/homelab, r/MachineLearning, r/artificial | unverified | unverified | unverified | unverified (secondary sources: 10% rule, megathreads, mod permission) | same as sitewide | HUMAN-ONLY (treat as strict until rules are read) |
| Lobste.rs | Invite-only; no explicit brand-account rule | Not addressed; spam includes content "created without meaningful human authorship" | n/a | Self-promo "less than a quarter" of stories+comments; none in first 70 days | None documented | HUMAN-ONLY |
| dev.to (Forem) | Yes (Organization accounts exist) | Yes via API key | AI assistance must be disclosed | Site "is not designed primarily for the purposes of promotion or creating backlinks"; AI-assisted posts may not promote your own project | Yes, free, POST /api/articles | AUTOMATE+DISCLOSE for publishing human-written, substantive posts; no AI-written promo |
| Hashnode | Yes (publications) | API now requires paid Pro plan | n/a | No "unsolicited promotional content" | No longer free | REJECT for automation at $0; manual only |
| Medium | Yes (first-party promotion allowed) | No: programmatic posting is listed as misuse | n/a | Allowed to "promote and link to your own business, website"; traffic-driving posts are spam | No new integration tokens (unverified) | REJECT for automated account; HUMAN-ONLY, low priority |
| Substack | Yes, may face "additional verification" | No official API (unverified) | n/a | Publications whose "primary purpose is to advertise external products or services" not permitted | No (unverified) | HUMAN-ONLY |
| Bluesky | Yes | Yes | Voluntary bot label ("For now, bot labels are voluntary") | No spam/repetitive posting; no artificial manipulation | Yes, free; ~1,666 creates/hour, ~11,666/day | AUTOMATE+DISCLOSE (best fit) |
| Fosstodon (Mastodon) | Not addressed; FOSS theme | Only if a human also monitors/interacts | Mastodon bot flag (visual) | "DO NOT post commercial promotions, or advertise"; "toot your own horn" is welcomed | Yes, free (Mastodon API) | AUTOMATE+DISCLOSE with human monitoring; non-commercial only |
| Hachyderm (Mastodon) | Yes: "Projects" account type for open source; username must match project | Project accounts: "Bots are not allowed" for dedicated feeds; Automated accounts must verify, max 5/day | Yes: bot checkbox + verification + #hachybots | "Say it once"; no "cron job effect" | Yes, free | HUMAN-ONLY for the project account; separate labeled bot possible but tightly capped |
| X | Yes | Yes, API-based only; no scripting the website | Yes: Automated label, bio disclosure, link to human-run account | No duplicate/bulk posts; no unsolicited automated replies | No free tier; $0.015/post, $0.20/post with URL | AUTOMATE+DISCLOSE only with spend; at $0 HUMAN-ONLY |
| LinkedIn Page | Yes, needs a real-name member as Administrator | Official API only (w_organization_social via Marketing API; access terms unverified) | n/a | "only use the Business Services to identify and promote your own Organization" | Member posting: free self-serve, 150 requests/day; org posting: partner program (unverified) | HUMAN-ONLY in practice; real-name admin conflicts with anonymity |
| YouTube | Yes | Yes (Data API, 100 uploads/day quota) | Disclose AI-generated/altered content | "Content created solely to drive users off of YouTube" is spam | Yes, free quota | AUTOMATE+DISCLOSE for genuine videos |
| Discord | Yes (server + app/bot) | Bots via app platform only; "Do not use self-bots or user-bots" | Bot identity via app | No unsolicited DMs; no "automating messages ... to maintain activity" | Yes, free | AUTOMATE (bot app) + a human-owned server; no fake-activity bots |
| GitHub (org, Discussions) | Yes, orgs free | Yes via GitHub App or one machine account | App/bot identity | Account content "should not be advertising or promotional marketing"; no automated starring/following | Yes, free; 5,000 req/h; 80 content-creating/min | AUTOMATE+DISCLOSE (GitHub App) |
| Product Hunt | No: profiles must "represent an individual, not a company" | No ("using bots" = spam) | n/a | No asking for upvotes; "Self-promoting in comments will also be removed" | API read-only by default, non-commercial | REJECT until release; then HUMAN-ONLY |
| Console newsletter | n/a (email submission) | n/a | n/a | Editorial; "We do not do sponsored reviews" | n/a | HUMAN-ONLY; pre-1.0/beta tools eligible |
| Changelog News | n/a (web form) | n/a | n/a | Own work welcome; no commercial products | n/a | HUMAN-ONLY |
| awesome-selfhosted list | n/a (PR) | No: "Machine/LLM-generated contributions are not allowed" | n/a | Project must be "first released more than 4 months ago" with a tagged release | n/a | REJECT until 4 months after first release |
| TLDR newsletter | n/a | n/a | n/a | No free submission route found | n/a | REJECT at $0 (paid placements only, unverified) |

---

## 2. Channel-by-channel findings with quoted rules

### 2.1 Hacker News and Show HN

Governing pages read: https://news.ycombinator.com/newsguidelines.html , https://news.ycombinator.com/showhn.html , https://news.ycombinator.com/newsfaq.html , https://github.com/HackerNews/API

(a) Self-promotion. Guidelines: "Please don't use HN primarily for promotion. It's ok to post your own stuff part of the time, but the primary use of the site should be for curiosity." (https://news.ycombinator.com/newsguidelines.html)

(b) Automation and generated text. Guidelines: "please don't automate posting." and "Please don't put generated text in HN posts." (https://news.ycombinator.com/newsguidelines.html). This is a direct prohibition on an automated posting account.

(c) Brand/organization accounts. No explicit ban, but: "HN is a community—users should have an identity that others can relate to." and "Throwaway accounts are ok for sensitive information, but please don't create accounts routinely." (https://news.ycombinator.com/newsguidelines.html). Show HN adds: "The project must be something you've worked on personally and which you're around to discuss." (https://news.ycombinator.com/showhn.html)

(d) Frequency/reposts. FAQ: "a small number of reposts is ok. Otherwise we bury reposts as duplicates." and "Please don't delete and repost the same story." (https://news.ycombinator.com/newsfaq.html). Guidelines: "Please don't delete and repost." (https://news.ycombinator.com/newsguidelines.html)

Voting: FAQ "Can I ask people to upvote my submission?" answer: "No." and "We penalize or ban submissions, accounts, and sites that break this rule" (https://news.ycombinator.com/newsfaq.html). Show HN: "Please don't ask friends to upvote or comment. That's not ok on HN." (https://news.ycombinator.com/showhn.html). Guidelines: "Don't solicit upvotes, comments, or submissions." (https://news.ycombinator.com/newsguidelines.html)

Show HN eligibility, decisive for a pre-release project: "Show HN is for something you've made that other people can play with." "If your work isn't ready for users to try out, please don't do a Show HN." "Don't post landing pages or fundraisers." "Off topic: blog posts, sign-up pages, newsletters, lists, and other reading material." "New features and upgrades ("Foo 1.3.1 is out") generally aren't substantive enough to be Show HNs." "Please make it easy for users to try your thing out, ideally without barriers such as signups or emails." (https://news.ycombinator.com/showhn.html)

(e) API. The official HN API documents only read endpoints (items, users, top/new stories, updates); no submit or vote endpoints are documented (https://github.com/HackerNews/API).

Verdict: HUMAN-ONLY. A project-branded account is tolerable if a human operates it and mostly participates out of curiosity; Show HN is REJECT until a downloadable build exists.

### 2.2 Reddit (sitewide)

Governing pages read: https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community , https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy , https://support.reddithelp.com/hc/en-us/articles/50051922501268-How-to-verify-you-re-human-when-asked-by-Reddit , https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki , https://ag.ny.gov/sites/default/files/social-media-policy-report/2025-q4-reddit-inc-policy.pdf (Reddit's own April 2026 NY transparency report; Appendix A is the Reddit User Agreement effective June 28, 2025), https://github.com/reddit-archive/reddit/wiki/API (archived 2017; historical)

Not retrievable: https://redditinc.com/policies/reddit-rules and https://www.redditinc.com/policies/content-policy (blocked by both fetch tools); https://support.reddithelp.com/hc/en-us/articles/360043504951 and .../204536419 (now return "The page you were looking for doesn't exist"). The verbatim text of Reddit Rule 2 is therefore unverified here; a search snippet reproduces it as "Post authentic content into communities where you have a personal interest, and do not cheat or engage in content manipulation (including spamming, vote manipulation, ban evasion, or subscriber fraud) or otherwise interfere with or disrupt Reddit communities." (unverified; snippet surfaced from a court-filed copy, not read on reddit.com).

(a) Self-promotion. Reddit help (moderator article, updated ~October 2026): "Spam on Reddit is generally defined as repeated, unwanted, and/or unsolicited actions, whether automated or manual, that negatively affect users, Reddit communities, and/or Reddit itself. Spam is a violation of the User Agreement and Reddit Rules, punishable by content removal and temporary or permanent banning of the user's account." "On Reddit, promotional content is not inherently considered to be spam. That said, some communities do have strict policies that disallow any kind of promotional content. Other communities abide by the 10% rule: only 10% of your posting and comment history in the community can be self-promotional in nature, while the other 90% should be helpful, organic content unrelated to your personal interest. It is ultimately up to you and your team to decide what works best for your community." (https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community)

Same article lists as reportable spam: "Repeatedly posting the same or similar comments in a thread, community or across communities." and "Programming bots that harm/break Reddit, including bots intended to promote content/products/services." and "Sending large amounts of chat messages or community invites to users who are not expecting them is also considered spam."

(b) Automated accounts and disclosure. Responsible Builder Policy (updated ~October 2026), section "Apps and Automated Activity": "This section applies to all users and developers who use or develop apps –including bots, AI agents, or non-human operated accounts– with Reddit data." "Apps must register and create a developer profile to get an App profile label." "Apps must not circumvent any labeling performed by Reddit." "App accounts should solely be used to perform app functions (no mixed use accounts)." "Apps must not manipulate Reddit's features (e.g., voting, karma) or circumvent safety mechanisms (e.g., user blocking, account bans)." "Apps must not engage in spamming activity through automated posts, comments, or direct messages. This includes posting identical or substantially similar content across subreddits." Also: "Approval is required: You must request access and get explicit approval before accessing any Reddit data through our API" and "Be transparent: You must not misrepresent or mask how or why you are accessing Reddit data. This prohibits registering multiple accounts or submitting multiple requests for the same use case." (https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)

Enforcement of the label: "if we detect automated activity on your account. Based on our Responsible Builder Policy, any account running automations needs to register their account and have it labeled as an app." "If you do not verify you're human within seven days, your account will be labeled as an app and may be restricted from posting and commenting until you do." (https://support.reddithelp.com/hc/en-us/articles/50051922501268-How-to-verify-you-re-human-when-asked-by-Reddit)

User Agreement (Appendix A of Reddit's NY filing), section 7 "Things You Cannot Do": you may not "Access, search, or collect data from the Services by any means (automated or otherwise) except as permitted in these Terms or in a separate agreement with Reddit" and may not "Use the Services in any manner that we reasonably believe to be an abuse of or fraud on Reddit or any payment system." Section 4: "You will not license, sell, or transfer your Account without our prior written approval." (https://ag.ny.gov/sites/default/files/social-media-policy-report/2025-q4-reddit-inc-policy.pdf)

(c) Brand accounts. No sitewide ban on a project-named account was found in the pages read. The Responsible Builder Policy's "no mixed use accounts" means a single account cannot be both an automated poster and a human participant.

(d) Rate limits. Data API Wiki: "Clients must authenticate with a registered OAuth token. We can and will freely throttle or block unidentified Data API users." "You must use a User-Agent where possible" in the format "<platform>:<app ID>:<version string> (by /u/<reddit username>)" and "NEVER lie about your User-Agent." Free-tier limits: "100 queries per minute (QPM) per OAuth client id" (averaged over a 10-minute window); chat "2,000 messages per day per recipient" and "3,000 messages per day total"; "Traffic not using OAuth or login credentials will be blocked". (https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki)

(e) API cost. The Data API has a free-access tier at the limits above, but access requires requesting approval (Responsible Builder Policy). Commercial use needs "explicit written approval".

Verdict: HUMAN-ONLY for anything promotional. An automated account must be App-labeled and single-purpose, and Reddit explicitly classes "bots intended to promote content/products/services" as spam, so an automated brand account that posts about UCompute is a rules violation. Humans posting under a project-named account are permitted sitewide, subject to subreddit rules.

### 2.3 Specific subreddits (r/LocalLLaMA, r/selfhosted, r/homelab, r/MachineLearning, r/artificial)

Status: unverified. The rules pages (https://www.reddit.com/r/<sub>/about/rules/) could not be fetched or opened in the browser pane (reddit.com blocked). Secondary summaries found via search, all unverified and to be re-checked by a human in the sidebar before posting:

- r/LocalLLaMA: a rule titled "Limit Self-Promotion" with roughly a 10% ratio; links should go to primary sources (GitHub/Hugging Face); affiliations to be disclosed. Sources: https://intoru.ai/subreddits/localllama , https://spacestationlabs.ai/subreddits/localllama (unverified).
- r/selfhosted: projects younger than about three months reportedly restricted to a "New Project Megathread"; apps should be production-ready with docs; flair rules. Sources: https://willitstay.com/r/selfhosted , https://www.threadotter.com/subreddit-rules/selfhosted , https://homenode.tech/r-selfhosted-summer-update-2025-flair-rules-analysis/ (unverified).
- r/homelab: promotion only with moderator permission or in designated threads; sales to r/homelabsales; referral links and blogspam prohibited. Source: https://www.threadotter.com/subreddit-rules/homelab (unverified).
- r/MachineLearning: [P] flair for projects; beginner questions redirected; periodic "Self-Promotion Thread"; strict on self-promo. Source: https://www.reddit-radar-marketing.com/guides/r/machinelearning (unverified).
- r/artificial: promotion reportedly with moderator permission or in designated threads. Source: https://www.threadotter.com/subreddit-rules/artificial (unverified).

Decision guidance: treat all five as strict until read; message moderators before any launch post; use the New Project megathread pattern where it exists; never post the same text to multiple subreddits (that is also a sitewide Responsible Builder Policy violation for apps).

### 2.4 Lobste.rs

Governing page read: https://lobste.rs/about

(a) Self-promotion: "It's great to have authors participate in the community, but not to exploit it as a write-only tool" and "As a rule of thumb, self-promo should be less than a quarter of one's stories and comments in the last year." New users are "not allowed to submit self-promo" during their first 70 days. (https://lobste.rs/about)

(b) Automation: no explicit user-bot rule; spam is defined to include "content that is created without meaningful human authorship." The site itself runs an "Official Fediverse bot" that "posts all stories that have reached the front page." (https://lobste.rs/about)

(c) Brand accounts: not addressed. Joining is invite-only: "The quickest way to receive an invitation is to talk to someone you recognize from the site." and "There's no official vetting process for new users, each user is responsible for inviting people". (https://lobste.rs/about)

(d) Limits: new users "can't send invites, submit links to domains we haven't seen submitted before"; "Users must reach 50 karma to flag."; ranking has "no special priorities or penalties for specific users or domains." (https://lobste.rs/about)

(e) API for posting: none documented on the about page (unverified whether any exists).

Verdict: HUMAN-ONLY. Scope is "focused pretty narrowly on computing", so a technical write-up (QUIC + TLS 1.3 device pairing, pinned keys, audit log design) fits; a product announcement does not. A new account cannot self-promote for 70 days, so an account should be seeded by participation well before any UCompute post.

### 2.5 dev.to (Forem)

Governing pages read: https://dev.to/terms , https://dev.to/code-of-conduct , https://dev.to/guidelines-for-ai-assisted-articles-on-dev , https://developers.forem.com/api/v1 , https://developers.forem.com/api

(a) Self-promotion. Terms section 11 (Content Policy): the site "is not designed primarily for the purposes of promotion or creating backlinks." "Posts must contain substantial content — they may not merely reference an external link that contains the full post." "If a post contains affiliate links, that fact must be clearly disclosed." (https://dev.to/terms)

(b) Automation/AI disclosure. AI guidelines: authors must "Disclose the fact that they were generated or assisted by AI in the post," either "upfront using the tag #ABotWroteThis or at any point in the article's copy." AI-assisted articles should not "Promote any business, program, or course (including your own)." nor "Be published with the main purpose of building a personal brand, building a social media presence, or gaining clout." Users should not use bots or AI to write comments. (https://dev.to/guidelines-for-ai-assisted-articles-on-dev). Code of Conduct requires "disclosing AI assistance if used to create content" (https://dev.to/code-of-conduct).

(c) Organization accounts: the site navigation exposes "Organization Accounts" (https://dev.to/code-of-conduct and https://dev.to/terms); the organizations help page content could not be retrieved, so the creation rules are unverified.

(d) Rate limits: not stated on the API pages read (https://developers.forem.com/api/v1 , https://developers.forem.com/api).

(e) API: free; "All endpoints can be accessed with the 'api-key' header" and POST /api/articles "allows the client to create a new article." "This API key can be generated by the user via their settings page in Forem." (https://developers.forem.com/api/v1 , https://developers.forem.com/api)

Verdict: AUTOMATE+DISCLOSE for publishing, with a hard content constraint: the article must be human-written and substantive; any AI-assisted text must be disclosed and must not promote UCompute. Practically, use the API to publish human-authored engineering posts under an Organization, with canonical URLs back to the project site.

### 2.6 Hashnode

Governing pages read: https://hashnode.com/terms (effective February 15, 2026), https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access

(a) Self-promotion/spam: prohibited to "Post or distribute spam, including unsolicited promotional content" and "automated content generation for the purpose of manipulating search results or engagement metrics." (https://hashnode.com/terms)

(b) Automation: prohibited to "Scrape, crawl, or use automated means to access the Service in a manner that exceeds reasonable use or violates these Terms." and to "Attempt to circumvent any rate limits or access restrictions imposed on the API." (https://hashnode.com/terms)

(c) Organization accounts: no dedicated section; publications offer "custom branding and team collaboration" (https://hashnode.com/terms).

(e) API cost: "Every API request, queries and mutations, now requires a Pro plan on your publication." Reason: "Scrapers and spammers were abusing the free API at scale." "Pricing is seat-based and adjusts automatically as members join or leave." (https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access). Third-party posts put Pro at about $5/month per publication (https://dev.to/just_a_side_project/i-tried-to-add-two-more-cross-post-platforms-both-were-dead-ends-4k9c , unverified).

Verdict: REJECT for automation at $0 (API is paid). Manual publishing on a free publication is possible (unverified whether free plans retain all publishing features).

### 2.7 Medium

Governing pages read: https://policy.medium.com/medium-rules-30e5502c4eb4 ("Updated June 2023"), https://github.com/Medium/medium-policy/blob/master/Rules.md

(a) Self-promotion: "First party promotion is allowed, and you may promote and link to your own business, website, mailing list, or fundraiser." but spam includes "Posting content primarily to drive traffic to, or increase the search rankings of, an external site, product, or service" and "Repeatedly using responses, mentions, or other interactions as a method of promotion or marketing". (https://policy.medium.com/medium-rules-30e5502c4eb4)

(b) Automation: under "Paid, automatic, bulk, or non-genuine interactions": "Registering accounts, posting content, or interacting with users or content automatically, systematically, or programmatically" is prohibited. Under "Prohibitions on Use of the Services": "use any software, script, robot, spider or other automatic device, process or means ... to access the Services for any purpose". Notice clause: Medium will notify "unless we believe your account is automated or operating in bad faith". (https://policy.medium.com/medium-rules-30e5502c4eb4)

(c) Brand accounts: impersonation banned ("Posting content or impersonating a person or organization in a way likely to deceive people."); third-party sponsorship banned, first-party promotion allowed (same page).

(d) Duplicate content: "We do not allow posting duplicate copies of the same content to Medium, whether from a single account or across multiple accounts ... (You are allowed to cross-post content from your blog to Medium, provided you own the rights for the content.)" (same page)

(e) API: multiple third-party sources report Medium stopped issuing new integration tokens around January 2025 (https://bpedro.medium.com/2025-03-20-9c3405a328d4 , https://docs.n8n.io/integrations/builtin/credentials/medium/ , https://community.make.com/t/integrating-medium-with-make-com/65838). Unverified: Medium's own help-center page (help.medium.com) returned 403.

Verdict: REJECT for an automated account (programmatic posting is explicitly misuse). HUMAN-ONLY cross-posting of blog posts is allowed.

### 2.8 Substack

Governing page read: https://substack.com/content

(a)/(c) Brand publications: "We don't permit publications whose primary purpose is to advertise external products or services" and "Brands and commercial organizations publishing on Substack may be subject to additional verification." (https://substack.com/content)

(b) Automation/inauthentic activity: "We may intervene to remove accounts engaged in artificial or inauthentic activity on community surfaces." "Don't post spam when interacting with others on Substack, such as in comments, discussion threads, or email replies." "We don't allow imports of email addresses that were purchased, scraped, or harvested from third party websites." (https://substack.com/content)

(e) API: no official public publishing API found; community tools use undocumented endpoints with session cookies (https://github.com/conorbronsdon/substack-mcp , https://github.com/HighnessAtharva/substack-cli ; unverified, third party).

Verdict: HUMAN-ONLY. A project newsletter is allowed if it is mostly substantive (engineering notes, release notes) rather than advertising.

### 2.9 Bluesky

Governing pages read: https://bsky.social/about/support/community-guidelines , https://bsky.app/profile/bsky.app/post/3mhgg5ja5gc2w (official Bluesky account post, March 19, 2026), https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/moderation.md , https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/rate-limits.md

(a) Self-promotion/spam: "Do not send spam or repeatedly post content in ways that disrupt normal conversations or service use." Commercial content must not be posted "without clearly identifying its commercial nature to other users." "Do not artificially manipulate features or social signals to gain unearned reach or mislead users" (engagement metrics, follower counts). (https://bsky.social/about/support/community-guidelines)

(b) Automated accounts and labels: "Bot labels are here. If you run an automated account, you can now mark it as such in your account settings. The label will show up on your profile and posts so people know what's a bot and what's not." "To mark your account as automated, go to Settings → Account → Automation label" "For now, bot labels are voluntary, and all existing policies continue to apply. We may introduce additional policies specific to automated accounts in the future." (https://bsky.app/profile/bsky.app/post/3mhgg5ja5gc2w). The protocol-level label value "bot" "marks the account as automated" and is among the global values usable for self-labeling (https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/moderation.md).

(c) Brand accounts: allowed; "Do not impersonate others or official groups in ways that could mislead users"; "create fake accounts to deceive others about who you are" is prohibited. (https://bsky.social/about/support/community-guidelines)

(d) Rate limits: creates cost 3 points against a 5,000-point hourly and 35,000-point daily per-account budget (about 1,666 creates/hour, 11,666/day); account creation 100 per 5 minutes per IP; 3,000 requests per 5 minutes per IP overall. (https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/rate-limits.md)

(e) API: free, open (AT Protocol). No pricing page exists for write access.

Verdict: AUTOMATE+DISCLOSE. Apply the bot/automation label, keep volume far below limits, do not auto-reply to people who did not opt in.

### 2.10 Mastodon: Fosstodon

Governing pages read: https://fosstodon.org/api/v1/instance/rules (server rules JSON), https://hub.fosstodon.org/coc/ , https://hub.fosstodon.org/ , https://docs.joinmastodon.org/user/profile/

(a) Self-promotion: Rule 8: "DO NOT post commercial promotions, or advertise". CoC elaborates: "DO NOT post commercial promotions, or advertise through posts that are exclusively links" and this "includes repetitive self-promotion for profit." Encouraged: "toot your own horn and show us your authentic self" and "We want to know about cool things you are involved with and things you have achieved." (https://fosstodon.org/api/v1/instance/rules , https://hub.fosstodon.org/coc/)

(b) Automation: Rule 9: "DO NOT use automated tools to post without also monitoring and/or interacting from your account." (https://fosstodon.org/api/v1/instance/rules). Mastodon's bot flag: "Enabling the bot flag will add a bot icon to your profile. This icon will let others know that your profile may perform automated actions, or might not be monitored by a human." "Mastodon currently treats the bot flag as a visual indication only." (https://docs.joinmastodon.org/user/profile/)

(c) Brand accounts: not addressed; "The theme of this instance is Free/Libre/Open-Source software and adjacent communities." (https://hub.fosstodon.org/coc/)

(d) Frequency: no numeric limit found.

(e) API: Mastodon's API is free (standard instance API).

Verdict: AUTOMATE+DISCLOSE with human monitoring. An Apache-2.0 project account fits the theme; scheduled posts are tolerated only if a human also replies and engages from the same account; no link-only promo posts.

### 2.11 Mastodon: Hachyderm

Governing pages read: https://community.hachyderm.io/docs/account-types/ , https://community.hachyderm.io/docs/account-types/open-source-accounts/ , https://community.hachyderm.io/docs/account-types/bot-accounts/ , https://community.hachyderm.io/docs/account-types/corporate-accounts/ , https://community.hachyderm.io/docs/account-types/covenant/ , https://community.hachyderm.io/docs/account-types/verification/ . Not retrievable: https://hachyderm.io/about (blocked).

(c) Account types: recognized specialized types include Corporate ("For businesses, companies, and similar."), Projects ("For Open Source Projects."), Curated, Automated ("Any posts that are programmatic and/or scheduled in nature."), Hybrid. Unrecognized specialized accounts "will be removed." For project accounts the username must match the project name; "Posting about your project is different from an open source account." (https://community.hachyderm.io/docs/account-types/)

Open-source project accounts: "We want to have one account for each project." Bots are not allowed on these accounts: "we try to keep our content based around real words written by real people." Automated content is allowed only as part of mixed posting; the account "can't be dedicated to only publishing that type of content." (https://community.hachyderm.io/docs/account-types/open-source-accounts/)

(b) Bot accounts: "All bots must be verified with Hachyderm"; "All bots must select the bot checkbox in their profile settings."; "Bots must be clearly marked as bots so that people can easily opt-out of bot posts if they wish."; most bots must include #hachybots in every post; "upper limit of 5 curated/scheduled/automated posts per day"; "Reactionary bots may only be triggered / 'summoned' by posts that include their handle." (https://community.hachyderm.io/docs/account-types/bot-accounts/)

Specialized Account Expectations: "I agree to only share my message once." "We are explicitly trying to avoid the 'cron job' effect that we see on Twitter with promotional accounts." "your 'fines will be doubled' if you end up violating our rules". (https://community.hachyderm.io/docs/account-types/covenant/)

Corporate accounts: "Are invite-only."; "Pay a subscription cost as of 1 Mar 2023" with tiers reported on the page from $650 to $2,500 per year; "verified with their company/business/entity domain"; the category covers "businesses and business-like entities" including "certain types of projects, conferences / events, and non-profit organizations". (https://community.hachyderm.io/docs/account-types/corporate-accounts/)

Verification: "only the following are required to be verified:" "Corporate accounts," "Bot accounts," "Curated accounts." Open-source projects are listed under accounts that "will likely want to consider being verified". (https://community.hachyderm.io/docs/account-types/verification/)

Verdict: HUMAN-ONLY for a UCompute "Projects" account (bots not allowed on it; "say it once"). If the project is judged "business-like" it becomes a paid, invite-only Corporate account, which fails the $0 constraint. A separate verified bot account is possible but capped at 5 automated posts/day and must be non-promotional.

### 2.12 X (Twitter)

Governing pages read: https://help.x.com/en/rules-and-policies/x-automation ("Updated April 2026"), https://help.x.com/en/using-x/automated-account-labels , https://docs.x.com/developer-guidelines , https://docs.x.com/x-api/getting-started/about-x-api , https://docs.x.com/x-api/getting-started/pricing

(b) Automation rules: "Build solutions that automatically broadcast helpful information in posts." is listed under "Do!". Under "Don't!": "Use non-API-based forms of automation, such as scripting the >x< website. The use of these techniques may result in the permanent suspension of your account." "Spam or bother users, or otherwise send them unsolicited messages." Spam rules: "You may not post duplicative or substantially similar posts on one account or over multiple accounts you operate." "You may not create and/or automate multiple accounts for duplicative or substantially similar use cases." Automated posts: "you may post automated posts for entertainment, informational, or novelty purposes." Replies/mentions: "Automating these actions to reach many users on an unsolicited basis is an abuse of the feature, and is not permitted. For example, sending automated replies to posts based on keyword searches alone is not permitted." "a user following your account is not on its own a sufficient indication of user intent to receive an automated response." AI replies: "the deployment or operation of any AI reply bot requires prior written and explicit approval from >x<." Likes: "You may not like posts or hide replies in an automated manner." Follows: "You may not follow or unfollow >x< accounts in a bulk, aggressive, or indiscriminate manner." Brands: "Advertisers, publishers, and brands using auto-response campaigns must request approval from >x< and may be subject to additional rules." (https://help.x.com/en/rules-and-policies/x-automation)

Disclosure: Developer guidelines require automated accounts to "Enable the 'Automated' profile label", to "Disclose in bio" that the account is a bot and who operates it, and to tie the bot to "a human-managed account". Prohibited: "Identical content across accounts, fake engagement, trend manipulation, bulk posting." and "No identical cross-posting." "Account Farms": "Multiple accounts for same duplicative purpose." (https://docs.x.com/developer-guidelines). The help page on labels: "We're launching a labeling feature that allows automated accounts to identify themselves" and "Once an account accepts the invitation to our test group, an automated account label will appear on their account profile under their profile name and handle." (https://help.x.com/en/using-x/automated-account-labels). Note the tension: the help page still describes the label as a test-group feature while the developer guidelines treat enabling it as required.

(c) Brand accounts: allowed; the automation rules address "Advertisers, publishers, and brands" directly (above).

(e) API pricing: "pay-per-usage pricing" with "No subscriptions" and "Credit-based: Purchase credits, deducted per request." (https://docs.x.com/x-api/getting-started/about-x-api). Pricing page: post creation $0.015 per request, $0.200 per request for a post with a URL, $0.010 for a summoned post; reads $0.005 per Post resource; "Pay-per-usage plans are capped at 3 million Post reads per monthly billing cycle."; no free tier described; promotional credits ($20 after saving a card and first purchase, first auto-recharge matched up to $50) require payment setup. (https://docs.x.com/x-api/getting-started/pricing)

Verdict: AUTOMATE+DISCLOSE is permitted by the rules, but every API post costs money and the only non-API automation (scripting the website) is a suspension offense. At $0 this is HUMAN-ONLY (manual posting in the app).

### 2.13 LinkedIn (Company Page)

Governing pages read: https://www.linkedin.com/legal/user-agreement , https://www.linkedin.com/legal/l/linkedin-pages-terms , https://www.linkedin.com/help/linkedin/answer/a1341387 , https://www.linkedin.com/help/linkedin/answer/100826 , https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin , https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api , https://learn.microsoft.com/en-us/linkedin/marketing/getting-started . Not retrievable: Community Management API access page (404).

(b) Automation: User Agreement 8.2 Don'ts item 13: "Use bots or other unauthorized automated methods to access the Services" (https://www.linkedin.com/legal/user-agreement). Help: LinkedIn does "not permit the use of any third party software" that scrapes or automates activity; users "risk having their accounts restricted or shut down." (https://www.linkedin.com/help/linkedin/answer/a1341387)

(c) Brand pages and the human behind them: User Agreement 2.1: "you will only have one LinkedIn account, which must be in your real name"; 8.2 item 1: do not "create a Member profile for anyone other than yourself (a real person)". Pages Terms: "The Page must have at least one Administrator identified for the Page." "Each Administrator of the Page must be a current registered member of LinkedIn.com". "You also represent and warrant that you are authorized to enter into these contract terms on behalf of the Organization". "You will only use the Business Services to identify and promote your own Organization." (https://www.linkedin.com/legal/user-agreement , https://www.linkedin.com/legal/l/linkedin-pages-terms). Help: "Create a LinkedIn profile with your real first and last name." and "Build your professional network to ensure you have enough connections to create a Page." (https://www.linkedin.com/help/linkedin/answer/100826)

(d)/(e) API: Share on LinkedIn (member posting) is a self-serve product granting w_member_social; rate limit "Member 150 Requests" per day and "Application 100,000 Requests" per day (https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin). Posting as an organization needs w_organization_social, "Restricted to organizations where the authenticated member has one of the following company page roles: ADMINISTRATOR, DIRECT_SPONSORED_CONTENT_POSTER, CONTENT_ADMIN" and is part of the Marketing/Community Management API (https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api). "The 2-legged client credentials flow is not available for any marketing use cases." and access is gated behind acceptance into the LinkedIn Marketing API Program (https://learn.microsoft.com/en-us/linkedin/marketing/getting-started). Whether that program is free and what approval requires: unverified.

Verdict: HUMAN-ONLY in practice. A Page requires a real-name human administrator, which conflicts with founder anonymity; official org-posting APIs exist but are partner-gated (unverified terms). Any unofficial automation is a ban risk.

### 2.14 YouTube

Governing pages read: https://support.google.com/youtube/answer/2801973 , https://support.google.com/youtube/answer/3399767 , https://developers.google.com/youtube/v3/getting-started , https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits , https://developers.google.com/youtube/v3/docs/videos/insert (page shows "Last updated 2026-10-15 UTC"), https://www.youtube.com/howyoutubeworks/policies/community-guidelines/

(a) Spam/self-promotion: "We do not allow content, metadata, or behavior designed to take advantage of the YouTube community". Prohibited: "Content created solely to drive users off of YouTube to external sites"; "Using automated tools or AI to churn out high volumes of similar content with minimal changes."; "Using high-volume, repetitive, or deceptive comments, live chats, or other messages". Allowed: "It's okay to ask viewers to like, comment, or subscribe." Disclosure: "Creators should disclose when content is generated or meaningfully altered with AI". (https://support.google.com/youtube/answer/2801973)

Fake engagement: content that "artificially increases the number of views, likes, comments, or other metrics" "either by using automatic systems or serving up videos to unsuspecting viewers" is prohibited; "Page traffic found to be artificial will not be counted on YouTube and can lead to strikes on your account." (https://support.google.com/youtube/answer/3399767)

(d)/(e) API: default quota "100 search.list calls, 100 videos.insert calls, and 10,000 units per day combined" (https://developers.google.com/youtube/v3/getting-started). "Quota impact: 100 calls per day. A call to this method has a quota cost of 1 unit in the Video Uploads quota bucket." and "Videos uploaded from unverified API projects are not restricted to private viewing mode." (https://developers.google.com/youtube/v3/docs/videos/insert, read 2026-10-30). To exceed quota "you must first complete an audit" (https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits). The API is free within quota.

Verdict: AUTOMATE+DISCLOSE for genuine demo/explainer videos uploaded via the Data API; no engagement automation; label AI-generated media.

### 2.15 Discord

Governing pages read: https://discord.com/guidelines , https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy (effective July 8, 2024), https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery

(b) Automation: Community Guidelines 14: "Do not use self-bots or user-bots." "Each account must be associated with a human, not a bot." 13: "Do not send unsolicited bulk messages (or spam) to others." 15: "Do not engage with our service in an inauthentic way." including "artificially inflating server membership, manipulating engagement metrics". (https://discord.com/guidelines). Developer Policy 5: "Do not contact users on Discord without their explicit permission." 6: "Do not target users with advertisements or marketing." 13: "Do not misrepresent or fraudulently manipulate engagement. This includes participating in, enabling, or promoting the inflation of server membership with bot or user accounts. This also includes automating messages to be sent for the purpose of maintaining activity in a Discord server." (https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy)

(c) Servers for projects: no specific rule; servers are free to create. Discovery requires: "Server must have at least 1,000 members to qualify." "Servers need to be at least 8 weeks old to be in Discovery." plus activity requirements and "Enable the 2FA Requirement For Moderation setting." (https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery)

(e) API: free; bots are built as Applications via the Developer Portal; "Discord may set and enforce limits on your use of the APIs ... at our sole discretion." (Developer Policy, same URL)

Verdict: AUTOMATE (as a proper bot application) inside a server owned by a human account; release-note and build-status bots are fine; never use the automation to simulate activity or DM members.

### 2.16 GitHub (organization, Discussions, bot accounts)

Governing pages read: https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies , https://docs.github.com/en/site-policy/github-terms/github-terms-of-service , https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts , https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps , https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app , https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions , https://docs.github.com/en/discussions/quickstart , https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api

(a) Promotion/spam: AUP prohibits "automated excessive bulk activity and coordinated inauthentic activity", "inauthentic interactions, such as fake accounts and automated inauthentic activity;", "rank abuse, such as automated starring or following;"; account content "should not be advertising or promotional marketing." and you may not advertise in others' accounts "such as by posting monetized or excessive bulk content in issues." (https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)

(b) Machine accounts: "Accounts registered by "bots" or other automated methods are not permitted." "You may maintain no more than one free machine account in addition to your free Personal Account." "the owner of the Account is ultimately responsible for the machine's actions." (https://docs.github.com/en/site-policy/github-terms/github-terms-of-service). "User accounts are intended for humans, but you can create accounts to automate activity on GitHub." (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts). GitHub recommends apps: "we recommend building a GitHub App" for long-lived integrations; "GitHub Apps can act independently of a user." (https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app); apps can run "without needing to sign in a user or create a service account." (https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps)

(c) Organizations: "Organizations are shared accounts where a large number of people can collaborate across many projects at once." "You can use organizations for free, with GitHub Free". (https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts). Discussions: "Repository owners and people with write access can enable GitHub Discussions"; organization-level discussions are "for broader conversations that span multiple repositories" (https://docs.github.com/en/discussions/quickstart , https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)

(d) Rate limits: "personal rate limit of 5,000 requests per hour"; installation tokens "minimum rate limit of 5,000 requests per hour"; secondary limits "no more than 80 content-generating requests per minute and no more than 500 content-generating requests per hour." (https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)

(e) API: free.

Verdict: AUTOMATE+DISCLOSE. A UCompute organization with Discussions enabled is the natural first home; automation should run as a GitHub App (bot identity) rather than a second human-looking account; no automated starring, following, or mass-issue posting.

### 2.17 Product Hunt

Governing pages read: https://help.producthunt.com/en/articles/3615694-community-guidelines , https://help.producthunt.com/en/articles/484973-can-our-company-account-vote-comment-or-post-on-product-hunt , https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines , https://help.producthunt.com/en/articles/484935-can-i-ask-my-community-friends-family-to-upvote-a-product , https://help.producthunt.com/en/articles/17350772-launch-guide , https://api.producthunt.com/v2/docs

(c) Brand accounts: "we require that profiles appear human and represent an individual, not a company, service, brand, or organization." (https://help.producthunt.com/en/articles/3615694-community-guidelines). "Product Hunt is a community of individuals, so company accounts cannot participate in forums, vote, or comment." (https://help.producthunt.com/en/articles/484973-can-our-company-account-vote-comment-or-post-on-product-hunt). Launch guide: "Register under your own name, not your company's or your product's." (https://help.producthunt.com/en/articles/17350772-launch-guide)

(a)/(b) Upvotes and bots: "Mass messaging users, asking for upvotes, using bots, incentivizing upvotes" are unacceptable; "Self-promoting in comments will also be removed."; violations "may result in the removal or suspension of your account and/or products" (https://help.producthunt.com/en/articles/3615694-community-guidelines). "Please don't." ... "asking or incentivizing people to upvote may trigger the algorithm to drop the product in the ranks" or "remove it from the homepage entirely." (https://help.producthunt.com/en/articles/484935-can-i-ask-my-community-friends-family-to-upvote-a-product). "never ask outright for upvotes or run anything that requires them." (launch guide)

Unreleased software: "We only feature products that are currently available." Not featured: "Waitlisted products (unless immediate access is provided)"; "No Vaporware: We only feature products that are ready for use or have a clear path to launch." (https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines). Launch guide: "Confirm everything works in production before you go live." and "You can launch again every time you ship a major feature or update." (https://help.producthunt.com/en/articles/17350772-launch-guide)

(e) API: apps are "read-only" by default; write access is granted case by case; "The Product Hunt API must not be used for commercial purposes." (https://api.producthunt.com/v2/docs)

Verdict: REJECT until there is a downloadable release; then HUMAN-ONLY under a real individual's profile (which conflicts with anonymity unless a named maintainer fronts it).

### 2.18 Newsletters and directories that accept submissions

Console (console.dev): "Console features 2-3 interesting developer tools each week"; selection questions include "Is this interesting and useful to developers?" and "Is there a self-service signup?"; early-access tools are eligible: "the release must be pre 1.0 and/or have an appropriate label in the version number." and "Any GA or stable releases are not eligible."; submit by email to hello@console.dev; "We do not do sponsored reviews." (https://console.dev/selection-criteria). Fit: good once a public pre-1.0 build exists.

Changelog News: submission form requires sign-in; asks for URL, title and "What's interesting about it?"; both others' work and your own are welcome; how-tos/tutorials and commercial products are not wanted; "if your fellow devs will find it interesting, submit it." (https://changelog.com/news/submit). Fit: good for a technical post or release announcement.

selfh.st (This Week in Self-Hosted): tagline "Self-hosted news, content, updates, launches, events, and more."; a "Submit Content" link points to https://selfh.st/submit/ (https://selfh.st/about/). Submission criteria: unverified (page is script-rendered; text not retrieved).

awesome-selfhosted (directory, PR-based): "Any software project you are adding was first released more than 4 months ago."; a tagged release is required ("This count initiates only after a release has been created."); FOSS license required; "Software with no development activity for 6-12 months may be removed from the list."; "Machine/LLM-generated contributions are not allowed and will result in a ban." (https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/CONTRIBUTING.md). Fit: REJECT until four months after the first tagged release.

TLDR: homepage exposes only an "Advertise" route (https://advertise.tldr.tech/) and no submission link (https://tldr.tech/). Free editorial submission route: not found (unverified).

---

## 3. Cross-cutting findings that drive the channel plan

1. Unreleased software is excluded from the biggest launch surfaces. Show HN: "If your work isn't ready for users to try out, please don't do a Show HN." (https://news.ycombinator.com/showhn.html). Product Hunt: "We only feature products that are currently available." (https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines). awesome-selfhosted: "first released more than 4 months ago" (https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/CONTRIBUTING.md). Pre-release, only build-in-public channels (GitHub, Bluesky, Mastodon, a newsletter, dev.to engineering posts) are open.

2. Generated text is a liability on developer channels. HN: "Please don't put generated text in HN posts." (https://news.ycombinator.com/newsguidelines.html). Lobste.rs spam includes content "created without meaningful human authorship" (https://lobste.rs/about). dev.to requires AI disclosure and bars AI-assisted posts that "Promote any business, program, or course (including your own)." (https://dev.to/guidelines-for-ai-assisted-articles-on-dev). awesome-selfhosted bans LLM-generated contributions. Hachyderm project accounts want "real words written by real people" (https://community.hachyderm.io/docs/account-types/open-source-accounts/). Automation should schedule and distribute human-written text, not generate it.

3. Disclosure is the price of automation where it is allowed: Reddit App label (https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy), X Automated label plus bio plus human-run account link (https://docs.x.com/developer-guidelines), Bluesky bot label (voluntary) (https://bsky.app/profile/bsky.app/post/3mhgg5ja5gc2w), Mastodon bot flag (https://docs.joinmastodon.org/user/profile/), Hachyderm bot checkbox plus verification (https://community.hachyderm.io/docs/account-types/bot-accounts/), GitHub App identity (https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app).

4. "Same text everywhere" is itself a violation on several platforms: Reddit apps "must not ... post identical or substantially similar content across subreddits" (Responsible Builder Policy); X "No identical cross-posting." (https://docs.x.com/developer-guidelines) and "You may not post duplicative or substantially similar posts on one account or over multiple accounts you operate." (https://help.x.com/en/rules-and-policies/x-automation); Medium bans "Posting duplicate content, whether from a single account or across multiple accounts" (https://policy.medium.com/medium-rules-30e5502c4eb4). Cross-posting pipelines must vary the text per channel and keep canonical links.

5. Anonymity constraint. Channels that require a real, named human behind the brand: LinkedIn ("one LinkedIn account, which must be in your real name", Page needs an Administrator who is a registered member) and Product Hunt (profiles must "represent an individual", with "a clear photo of yourself" per the community guidelines). Channels where an org/project identity suffices: GitHub organization, Bluesky, Fosstodon, Hachyderm project account (username must match project), X, YouTube, Discord, dev.to Organization, Substack (may face "additional verification").

6. $0 kills API automation on X (pay-per-post) and Hashnode (Pro-only API). Free write APIs remain on Bluesky, Mastodon, GitHub, dev.to, YouTube (quota), Discord, Reddit (approval required; promotional bots are spam anyway).

---

## 4. Channels where an automated brand account would violate the rules (flags)

- Hacker News: "please don't automate posting." (https://news.ycombinator.com/newsguidelines.html). Human must post.
- Reddit: promotional bots are spam ("bots intended to promote content/products/services", https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community); any automated account must be App-labeled and single-purpose (https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy). Human must post.
- Medium: "Registering accounts, posting content, or interacting with users or content automatically, systematically, or programmatically" is misuse (https://policy.medium.com/medium-rules-30e5502c4eb4). Human must post.
- LinkedIn: "Use bots or other unauthorized automated methods to access the Services" is prohibited (https://www.linkedin.com/legal/user-agreement); only official partner-gated APIs allowed. Human must post or an approved Marketing API app must be used.
- Product Hunt: company accounts "cannot participate in forums, vote, or comment" and "using bots" is spam (https://help.producthunt.com/en/articles/484973-can-our-company-account-vote-comment-or-post-on-product-hunt , https://help.producthunt.com/en/articles/3615694-community-guidelines). Human individual must post.
- Hachyderm project account: "Bots are not allowed" on open-source project accounts (https://community.hachyderm.io/docs/account-types/open-source-accounts/). Human must post from the project account.
- Fosstodon: automation only "with also monitoring and/or interacting from your account" (https://fosstodon.org/api/v1/instance/rules). Semi-automated at most.
- X: automation allowed only through the paid API with the Automated label; "scripting the >x< website" risks "permanent suspension" (https://help.x.com/en/rules-and-policies/x-automation). At $0, human must post.
- Discord: "Do not use self-bots or user-bots" (https://discord.com/guidelines); automation only as a registered bot app, and never to simulate activity (https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy).
- Lobste.rs: no automation rule, but spam includes content "created without meaningful human authorship" and self-promo is capped at under a quarter of activity (https://lobste.rs/about). Human must post.

Channels where an automated project account is allowed with disclosure: Bluesky (bot label), Mastodon instances with the bot flag plus human monitoring (Fosstodon) or a verified capped bot account (Hachyderm), GitHub via a GitHub App, dev.to via API for human-written posts with any AI assistance disclosed, YouTube Data API uploads, Discord bot applications.

---

## 5. Items marked unverified (need a human to confirm)

- Verbatim rules of r/LocalLLaMA, r/selfhosted, r/homelab, r/MachineLearning, r/artificial (all reddit.com fetches blocked). Secondary sources listed in section 2.3.
- Verbatim Reddit Rules (Rule 2 content-manipulation text) from redditinc.com (blocked); Reddit's help center and NY filing were used instead.
- Medium integration tokens no longer issued (third-party reports only; help.medium.com returned 403).
- Substack has no official publishing API (third-party tools only).
- Hashnode Pro price (~$5/month per publication) from third-party posts; the changelog itself gives no number.
- LinkedIn Marketing API / Community Management API access requirements and whether approval is free (access page returned 404).
- dev.to Organization account creation rules (page content not retrieved).
- selfh.st submission criteria (script-rendered page).
- TLDR free submission route (none found).
- Whether Hashnode free plans still allow manual publishing without restrictions.
- X automated-label availability outside the "test group" described on the help page versus the developer guidelines' requirement to enable it.

---

## 6. Sources (every URL read)

Primary pages read directly (WebFetch or browser pane):
- https://news.ycombinator.com/newsguidelines.html
- https://news.ycombinator.com/showhn.html
- https://news.ycombinator.com/newsfaq.html
- https://github.com/HackerNews/API
- https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community
- https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy
- https://support.reddithelp.com/hc/en-us/articles/50051922501268-How-to-verify-you-re-human-when-asked-by-Reddit
- https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
- https://support.reddithelp.com/hc/en-us/search?query=self-promotion
- https://support.reddithelp.com/hc/en-us/search?query=Responsible+Builder+Policy
- https://ag.ny.gov/sites/default/files/social-media-policy-report/2025-q4-reddit-inc-policy.pdf
- https://github.com/reddit-archive/reddit/wiki/API (archived 2017; historical only)
- https://lobste.rs/about
- https://dev.to/terms
- https://dev.to/code-of-conduct
- https://dev.to/guidelines-for-ai-assisted-articles-on-dev
- https://dev.to/faq (navigation only)
- https://dev.to/organization-info (navigation only)
- https://developers.forem.com/api/v1
- https://developers.forem.com/api
- https://hashnode.com/terms
- https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access
- https://policy.medium.com/medium-rules-30e5502c4eb4
- https://github.com/Medium/medium-policy/blob/master/Rules.md
- https://substack.com/content
- https://bsky.social/about/support/community-guidelines
- https://bsky.app/profile/bsky.app/post/3mhgg5ja5gc2w
- https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/rate-limits.md
- https://raw.githubusercontent.com/bluesky-social/bsky-docs/main/docs/advanced-guides/moderation.md
- https://atproto.com/guides/tutorials (redirect target of the Bluesky bots starter page)
- https://fosstodon.org/api/v1/instance/rules
- https://hub.fosstodon.org/
- https://hub.fosstodon.org/coc/
- https://docs.joinmastodon.org/user/profile/
- https://community.hachyderm.io/docs/account-types/
- https://community.hachyderm.io/docs/account-types/open-source-accounts/
- https://community.hachyderm.io/docs/account-types/bot-accounts/
- https://community.hachyderm.io/docs/account-types/corporate-accounts/
- https://community.hachyderm.io/docs/account-types/covenant/
- https://community.hachyderm.io/docs/account-types/verification/
- https://help.x.com/en/rules-and-policies/x-automation
- https://help.x.com/en/using-x/automated-account-labels
- https://docs.x.com/developer-guidelines
- https://docs.x.com/x-api/getting-started/about-x-api
- https://docs.x.com/x-api/getting-started/pricing
- https://www.linkedin.com/legal/user-agreement
- https://www.linkedin.com/legal/l/linkedin-pages-terms
- https://www.linkedin.com/help/linkedin/answer/a1341387
- https://www.linkedin.com/help/linkedin/answer/100826
- https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin
- https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/posts-api
- https://learn.microsoft.com/en-us/linkedin/marketing/getting-started
- https://support.google.com/youtube/answer/2801973
- https://support.google.com/youtube/answer/3399767
- https://developers.google.com/youtube/v3/getting-started
- https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- https://developers.google.com/youtube/v3/docs/videos/insert
- https://www.youtube.com/howyoutubeworks/policies/community-guidelines/
- https://discord.com/guidelines
- https://support-dev.discord.com/hc/en-us/articles/8563934450327-Discord-Developer-Policy
- https://support.discord.com/hc/en-us/articles/360030843331-Enabling-Server-Discovery
- https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies
- https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts
- https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps
- https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/deciding-when-to-build-a-github-app
- https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions
- https://docs.github.com/en/discussions/quickstart
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- https://help.producthunt.com/en/articles/3615694-community-guidelines
- https://help.producthunt.com/en/articles/484973-can-our-company-account-vote-comment-or-post-on-product-hunt
- https://help.producthunt.com/en/articles/9883485-product-hunt-featuring-guidelines
- https://help.producthunt.com/en/articles/484935-can-i-ask-my-community-friends-family-to-upvote-a-product
- https://help.producthunt.com/en/articles/17350772-launch-guide
- https://api.producthunt.com/v2/docs
- https://console.dev/selection-criteria
- https://changelog.com/news/submit
- https://selfh.st/about/
- https://selfh.st/submit/ (script-rendered; text not retrieved)
- https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/CONTRIBUTING.md
- https://tldr.tech/

Secondary sources (search results only; unverified):
- https://intoru.ai/subreddits/localllama
- https://spacestationlabs.ai/subreddits/localllama
- https://willitstay.com/r/selfhosted
- https://www.threadotter.com/subreddit-rules/selfhosted
- https://homenode.tech/r-selfhosted-summer-update-2025-flair-rules-analysis/
- https://www.threadotter.com/subreddit-rules/homelab
- https://www.reddit-radar-marketing.com/guides/r/machinelearning
- https://www.threadotter.com/subreddit-rules/artificial
- https://bpedro.medium.com/2025-03-20-9c3405a328d4
- https://docs.n8n.io/integrations/builtin/credentials/medium/
- https://community.make.com/t/integrating-medium-with-make-com/65838
- https://github.com/conorbronsdon/substack-mcp
- https://github.com/HighnessAtharva/substack-cli
- https://dev.to/just_a_side_project/i-tried-to-add-two-more-cross-post-platforms-both-were-dead-ends-4k9c

Attempted and not retrievable (blocked, 403, or 404 at research time):
- https://www.reddit.com/r/LocalLLaMA/about/rules/ , https://www.reddit.com/r/selfhosted/about/rules/ , https://www.reddit.com/r/homelab/about/rules/ , https://www.reddit.com/r/MachineLearning/about/rules/ , https://www.reddit.com/r/artificial/about/rules/ (and old.reddit.com equivalents)
- https://redditinc.com/policies/reddit-rules , https://www.redditinc.com/policies/content-policy
- https://support.reddithelp.com/hc/en-us/articles/360043504951 (404), https://support.reddithelp.com/hc/en-us/articles/204536419 (404)
- https://help.medium.com/hc/en-us/articles/213477928-Medium-Rules (403)
- https://developer.x.com/en/products/x-api (402)
- https://hachyderm.io/about , https://hachyderm.io/api/v1/instance/rules
- https://fosstodon.org/about (script-rendered)
- https://learn.microsoft.com/en-us/linkedin/marketing/community-management/getting-access (404)
- https://console.dev/submit/ (404)
- https://github.com/awesome-selfhosted/awesome-selfhosted/blob/master/CONTRIBUTING.md (404; moved to awesome-selfhosted-data)
- https://docs.bsky.app/docs/starter-templates/bots (redirects; content not available)
