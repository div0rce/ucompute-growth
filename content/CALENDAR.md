# Distribution calendar

No public channel is authorized yet (`channels/REGISTRY.md`). The calendar therefore schedules **readiness**, not publication: each piece is made ready so that the day a channel or gate opens, publication is a one-step action with no new writing.

| Target state | Piece (content/ id) | Audience | Waits on | Ready by |
|---|---|---|---|---|
| Ready, website handoff | `2026-10-30-pairing-explainer` (how two devices pair: code, keys, revocation) | multi-device developers; OSS infra | nothing (evidence committed) | 2026-10-31 |
| Ready, website handoff | `2026-10-31-loopback-rpc-vs-authenticated-transport` (why llama.cpp's RPC stays on loopback and what UCompute puts around it) | local-AI developers; OSS infra | nothing | 2026-11-02 |
| Ready, website handoff | `2026-11-01-memory-fit-explainer` (how UCompute estimates whether a GGUF fits before loading) | local-AI developers; AI app builders | nothing | 2026-11-04 |
| Ready, search page | `2026-11-02-openai-client-base-url` (point the official OpenAI clients at a local server) | AI app builders | nothing | 2026-11-06 |
| Ready, community answers bank | `community-answers.md` (truthful answers to the recurring questions in `research/`) | all | research synthesis | 2026-11-03 |
| Drafted, held | Source-publication announcement | all | owner publishes the source (engineering B-007) | draft within 24 h of the decision |
| Drafted, held | Public release communication | all | website LAUNCH.md gates | draft within 24 h |
| Weekly | `analytics/weekly/` report | owner (internal) | — | every Monday |
