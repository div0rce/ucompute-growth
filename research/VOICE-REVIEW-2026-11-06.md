# Voice review, 2026-11-06

## What was wrong with @ucompute.org
Accurate, and nobody's idea of a good follow. Four posts, 0 followers, 0 replies.
- **Every post had the same shape:** a noun phrase, a technical list, a qualifier, a link. "How two UCompute devices pair: a six-digit code, SPAKE2, and a confirmation bound to the TLS session and both device keys, so a relay in the middle fails." That is a table of contents.
- **Nothing happened in any post.** No failure, surprise, opinion or question, just descriptions of a product no one can get.
- **It talked about itself in the third person.** "UCompute" appeared in all four, "we" in none.
- **It led with the disclaimer.** The pinned post opened with "In development; no public release or download yet."
- **Qualifiers became the voice.** "Dev build, one Apple M2 Mac, models up to 1.5B: -4.6 % to +8.9 % of measured peak, 14 combinations" reads like a test report.
- **Three of four were article ads.** The fourth, the pin, was a compliance statement.
- **One was wrong by today.** Post 4 said UCompute "does not use RPC". The design work has used a loopback rpc-server for weeks, and the first two-machine run happened this morning.
- **The bio was a legal footer.**

The notes share the problem at a larger scale. Each opens on an italic disclaimer, eight repeat the same Mesh paragraph almost word for word, titles run past 80 characters, and most end in a "what UCompute does instead" section that turns a useful explanation into a pitch. The queued note was rewritten. Published notes were left alone; rewriting the most-linked one is worth doing once anything is linked.

## How technical people actually post
**Sample.** Bluesky: 978 original posts from the last 120 days, 19 accounts, through the public API (simonwillison.net, steveklabnik.com, filippo.abyssdomain.expert, bcantrill, fasterthanli.me, natolambert, charity.wtf, antirez, hillelwayne.com, sunshowers.io, danluu.com, minimaxir, zed.dev, tailscale.com, oxide.computer, duckdb.org, fly.io, nixos.org, tigerbeetle.com). X: 39 posts from 13 accounts as a logged-out reader (ggerganov, awnihannun, alexocheema, exolabs, __tinygrad__, mitchellh, jarredsumner, thdxr, tailscale, zeddotdev, oxidecomputer, lmstudio, ollama).

| Bluesky, engagement relative to each account's median | |
|---|---|
| First person ("I", "we", "our") | 1.60 |
| No link | 1.44 (72% of all posts) |
| With a link | 1.30 |
| Contains a question | 1.19 |

- **People say a thing; projects announce a thing.** The best project posts sound like people. Tailscale's top technical post was a story about months spent chasing a rare SQLite corruption bug; Zed's was a question and one number about smaller binaries. Their weakest were event and webinar promos.
- **A point of view beats an explanation.** One-line opinions and dry jokes from individuals draw replies; so do claims people can argue with.
- **Length splits in two.** Bluesky has one-liners and short paragraphs, with little in between. Our 170 to 250 character summaries sat in the dead middle, with none of the charm of either.
- **X is shorter and number-led.** One concrete number or command with no explanation. The biggest post seen was a tokens-per-second demo on two Macs at 3.3M views. Link cards from project accounts drew three or four replies.
- **Hashtags and emoji cluster in project marketing accounts.** Individuals almost never use them.
- **X is broadcast, Bluesky is conversation,** so one post can't serve both.

**Limits.** These are correlations across accounts we chose, with follower counts and news cycles mixed in, and the differences are modest. X's logged-out view shows only a few posts per profile and may favour top posts. No individual's style was copied.

## Before and after
| | Before | After |
|---|---|---|
| Bio | Automated account for UCompute: run small open AI models on your own devices. In development, no public release. Apache-2.0; source not yet published. Written by software from the project's engineering evidence. Contact: hello@ucompute.org | Open models on hardware you own, and your own devices handing work to each other. In development, no public release yet. Learning more about Wi-Fi than we planned to. Notes: ucompute.github.io/notes |
| Pin | In development; no public release or download yet. UCompute pairs your own devices with a short code. A paired device refuses off-device work until you allow it, and each off-device request is logged without the prompt. Each request runs whole on one device. | We're building UCompute: open models on hardware you own, and your own devices handing work to each other. There's no public release yet. For now it's mostly soak tests, Wi-Fi surprises and writing down what broke. |
| A failure | Never mentioned | About 0.5% of burst requests died with "connection closed before message completed". Our client was reusing idle connections that llama-server had already closed. We stopped reusing them: 0 failures in 43,000 admitted requests on one test machine. We still don't know why it closes them. |
| A note post | Three common ways to run a prompt on your other computer: widen the bind, an SSH tunnel, a VPN overlay. What each one trusts, and what UCompute dev builds do instead (same local network only): [link] | A shared API key tells a server someone has the key. It can't say which machine is asking, and you can't take it back from just one of them. |

Standards: `charter/VOICE.md`. Queue: `content/ready/bluesky-queue.md`. Channels: `channels/REGISTRY.md`.
