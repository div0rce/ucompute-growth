---
to: Engineering workstream (via the owner)
from: UCompute Growth
date: 2026-10-31
status: rerouted
---

> **Rerouted 2026-11-06 (Program Control HO-004b, C-6). A tested security route and a named responder are owner and Engineering matters, tracked as OWN-4. The public text stays as it is: it gives an address and promises no handling.**
# Proposal: make hello@ucompute.org (or a security@ alias) the tested private security route

**Situation.** UCompute now has public pages: the organization profile at https://github.com/ucompute and engineering notes at https://ucompute.github.io/notes/. Readers need somewhere private to send a suspected vulnerability. The owner set up `hello@ucompute.org` (Cloudflare Email Routing) as the project's public address on 2026-10-31, and Growth's pages now say: "Corrections and questions: hello@ucompute.org. Please send anything security-related there rather than posting it publicly." Issues are off on the notes repository so nothing is reported in public by default. No response time is promised anywhere.

**Gap.** The engineering `SECURITY.md` still points reporters to "the repository's GitHub profile" and a private advisory on the personal-account repository, and says: "Before external beta, maintainers must verify the private reporting route and name a responsible responder." Neither has happened.

**Ask (owner and Engineering decide):**
1. Choose the route: `hello@ucompute.org`, or a `security@ucompute.org` alias on the same routing.
2. Send one harmless test report through it and record the result, as `SECURITY.md` requires.
3. Update `SECURITY.md` to name that address once tested, and add a capability-snapshot row for it so Growth can state it in the claims registry.

Until then Growth keeps the current wording and promises nothing about handling.
