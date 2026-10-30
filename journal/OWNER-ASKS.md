# Owner asks

The only things Growth cannot do alone. Each is one-time. Nothing here blocks the rest of the operation; the sessions keep working around them. When one is done, write the grant (date, exact words) into `channels/REGISTRY.md` and strike it here.

| # | Ask | Why it needs you | Effort |
|---|---|---|---|
| 1 | **Create the GitHub organization `ucompute`** (free plan) and add the account that runs this repository as a member. The login was free when checked on 2026-10-30; names like this get taken. | Only you may create accounts; a branded org keeps the public identity separate from your personal handle | 5 min |
| 2 | **Create a project mailbox** such as `hello@ucompute.org` with Cloudflare Email Routing (free) forwarding to an inbox you control, and tell Growth the address (not the destination). | You hold the Cloudflare zone | 10 min |
| 3 | **Authorize channels in writing.** For each channel you want Growth to operate autonomously (Bluesky with the `ucompute.org` domain handle, a Mastodon account, dev.to or Hashnode), create the account under the project mailbox, store the credential in the secrets store you choose, and write one line: "Growth may publish ordinary content to <channel> within the claims registry." | Account creation and credentials are yours; the authorization must be explicit | 10 min per channel |
| 4 | **Cloud routine repository access.** The cloud routines clone `div0rce/ucompute-growth`. If a run fails its repository-access check, grant the Claude GitHub app access to that repository at https://github.com/settings/installations. Optionally also grant read access to `ucompute-dev` so the daily run can read new capability snapshots directly instead of the mirror. | Installation permissions are account-level | 2 min |
| 5 | **Decide whether Growth may propose a sign-up.** Spec 29.5 says contact collection needs its own authorization. Growth will not build or mention a waitlist until you say so. | Owner-gated by the specification | 1 line |
| 6 | Standing items Growth tracks but does not own: source publication (engineering B-007), a tested security contact, trademark clearance, public launch (website LAUNCH.md). Growth prepares launch communications for each and publishes nothing until the gate opens. | Release and launch gates | — |
