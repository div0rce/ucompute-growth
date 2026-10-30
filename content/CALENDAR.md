# Distribution calendar

No public channel is authorized yet (`channels/REGISTRY.md`). The calendar therefore schedules **readiness**, not publication: each piece is made ready so that the day a channel or gate opens, publication is a one-step action with no new writing.

| Target state | Piece (content/ id) | Audience | Waits on | Ready by |
|---|---|---|---|---|
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-10-30-pairing-explainer` (how two devices pair: code, keys, revocation) | multi-device developers; OSS infra | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-10-31-loopback-rpc-vs-authenticated-transport` (llama.cpp's RPC backend is not a network transport, and what UCompute does instead) | local-AI developers; OSS infra | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-11-01-memory-fit-explainer` (how UCompute estimates whether a GGUF fits before loading) | local-AI developers; AI app builders | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-11-02-openai-client-base-url` (point the official OpenAI clients at a local server) | AI app builders | nothing: reviewed, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-10-30-what-the-audit-log-records` (what the audit log records and never records) | multi-device developers; homelab; OSS infra | nothing: fact-checked, lint clean, in `content/ready/` | done |
| **READY 2026-10-30** (awaits an AUTHORIZED channel or the website handoff) | `2026-11-03-what-0000-exposes` (what binding a local AI server to 0.0.0.0 exposes; OS-by-OS self-check) | local-AI developers; multi-device developers | nothing: self fact-checked, lint clean, in `content/ready/`; Cisco/Elastic/LM Studio quotes to be re-read by a local session (hosts blocked from the cloud) | done |
| **READY 2026-10-30** (internal bank; used only in AUTHORIZED channels) | `community-answers.md` (25 answers in 9 themes, quotations traced to `research/raw/`) | all | nothing: lint clean, reviewed | done |
| Drafted, held | Source-publication announcement | all | owner publishes the source (engineering B-007) | draft within 24 h of the decision |
| Drafted, held | Public release communication | all | website LAUNCH.md gates | draft within 24 h |
| Weekly | `analytics/weekly/` report | owner (internal) | — | every Monday |

## Week 2026-W45 (2026-11-02 to 2026-11-08), set by the 2026-W44 weekly review
Dates slipped because the founding session's draft review was interrupted. One piece reviewed and promoted per daily run, in the order above; one research lens per daily run after that. Publication remains zero until a channel is AUTHORIZED.
