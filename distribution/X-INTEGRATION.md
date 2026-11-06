# X through Buffer

Verified 2026-11-06 against official pages. Status: **built, tested offline, not live.** Nothing has been sent to X or Buffer, and no account exists.

## Findings
| Question | Answer | Source |
|---|---|---|
| X API direct | $0.015 per post, $0.20 with a URL, no free tier, needs a card. Rejected: a paid dependency | docs.x.com/x-api/getting-started/pricing |
| Buffer free plan | $0. 3 channels, 10 scheduled posts per channel (a queue limit, not a publishing cap), X supported | buffer.com/pricing; support article 643 |
| Buffer API on free | Yes. 1 key, 150 requests per 15 min, 600 per day, 1,000 per channel per 30 days. GraphQL `createPost`, `customScheduled`, `saveToDraft` | support article 859; developers.buffer.com |
| Buffer on X | Works with 280 characters on a free X account; no polls, one X account at a time, threads through the web app | support article 561 |
| Typefully free plan | $0. API included, but 10 posts a month, and the API can answer 402 requiring a paid plan | typefully.com/pricing; typefully.com/docs/api |
| X automation rules (April 2026) | Automated informational posts allowed. No scripting the site, no duplicate posts, no keyword replies | help.x.com, Automation rules |
| AI-generated replies on X | Need X's prior approval | docs.x.com/developer-guidelines |

**Choice: Buffer.** It works at $0 with no monthly post limit and fits the owner's stated preference. Typefully is a sound fallback, because 10 posts a month is near our real pace. Replies are not automated on any route.

## The catch
Unattended posting is technically possible, but X says automated accounts must display a label and "remain connected to a human-run account", and that the label connects that account "to let everyone know who's managing it" (help.x.com, About Automated account labels). X's Developer Guidelines add a bio line naming the operator. For us that would publicly tie the account to a person. So:

- **Draft mode (default, recommended).** Growth writes and gates each post, then saves it as a Buffer draft. A person releases it from the Buffer app. The account stays human-run, so no label or link applies. Cost: a tap per post, a few times a week. Buffer's Team-plan approval feature isn't needed; drafts exist on every plan.
- **Unattended mode (off).** Needs a human-run managing account that identifies no one, the Automated label, a bio disclosure, and a separate grant. Whether a project-run managing account satisfies X is X's call, so this stays off unless the owner chooses it.

## How it fits
`scripts/x_post.py` reuses Bluesky's queue parser, caps, claims lint, link checks and voice lint, so nothing is duplicated and Bluesky, GitHub and notes automation are untouched. Queue: `content/ready/x-queue.md`, written for X. Ledger: `analytics/x-posted.jsonl`. Workflow: `.github/workflows/x.yml`, off until the variable `X_ENABLED` is true. The script also refuses unless `channels/REGISTRY.md` marks X AUTHORIZED, so two independent switches protect the account.

**Tested:** `x_post.py --selftest` covers both gates, the Buffer request shape, floors, caps, length, voice and repeats. **Not tested:** any live Buffer call. `CreatePostInput` lists more required fields than the official example sends, so the first live call may need a small fix. Whether Buffer's free plan behaves for a brand-new X account is also unknown until tried.

**Measurement.** X gives Buffer no impressions, and Buffer's post metrics are an early preview for personal use. Replies, likes and follows are readable on the public profile by a local session, by hand. Do not automate that: X forbids scraping.

## To activate
OWNER-ASKS 14 lists the owner's steps. Then a local session sets `X_ENABLED`, dispatches `x-post` once, confirms a draft appears, and moves the X row to AUTHORIZED only if the owner's grant is quoted there.
