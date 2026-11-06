---
to: Engineering workstream (via the owner)
from: UCompute Growth
date: 2026-10-30
status: rerouted
---

> **Rerouted 2026-11-06 (Program Control HO-004b). Under D-032 Engineering is consumed through records, not requests. These ten facts are carried by HO-002 and answered by the next capability snapshot, including "not yet". Growth asks nothing further.**
# Ask: ten facts for the next capability snapshot, so public writing can say them

Growth writes only what the capability snapshot (sections 8 and 9) and the decisions register support. The adoption-barrier research (`research/BARRIERS.md`, `research/raw/adoption-barriers.md`, 35 primary sources) shows that developers' first questions about a tool like this are ones the current snapshot does not answer either way. Each item below asks for one sentence of verified fact in the next snapshot, or an explicit "not yet"; Growth will quote it with its qualifier and never go beyond it. No code change is requested; no deadline is implied.

| # | Fact requested as a snapshot row | Why developers ask (barrier id in `research/BARRIERS.md`) |
|---|---|---|
| 1 | Current signing status of the macOS and Windows builds (ad-hoc, not notarized; unsigned), and the exact OS dialog a tester sees | B1: Gatekeeper on macOS Sequoia removed the Control-click override; Windows Smart App Control has no per-app bypass. Testers need the sanctioned steps in the project's words |
| 2 | The complete list of outbound connections a development build makes (engine archive host, model hosts, paired devices, anything else) and whether any update or telemetry check runs | B6: privacy-conscious users verify "no telemetry" by capturing traffic; a published list lets Growth state it and lets readers check it |
| 3 | Whether an interrupted model or engine download resumes, how a stall is handled, and what the user sees on a SHA-256 mismatch | B4: large downloads failing late are the most cited first-run complaint |
| 4 | Whether a file already on disk is re-hashed before every load | B4, SEARCH query group 7: "what does verified mean" |
| 5 | What the requesting device shows when the chosen device stops answering (sleep, lid closed, network loss), and whether an in-flight request is reported as failed | B10: laptop sleep breaking servers is a top repeat-use complaint |
| 6 | Whether a version mismatch between two paired devices is detected and shown | B7: mixed-OS pairing with no auto-update |
| 7 | Whether a "does not fit" memory verdict can be overridden, and how the estimate behaves on the Windows laptop and on unified-memory hardware | B3: the memory-fit note states the macOS calibration only |
| 8 | Tool calling: verified against the official OpenAI clients, or the list of request fields accepted, ignored and rejected (and whether `/v1/responses` or embeddings exist) | B8: AI app builders front coding agents; the base-URL page currently says "tool calling is not yet verified" |
| 9 | Whether a reason is surfaced when a paired device cannot be reached (discovery blocked, firewall, client isolation) | B5: campus and guest networks |
| 10 | The two-Mac pairing result when the run is repeated | B5, B7: the registry qualifier says "Pairing between two Macs is not yet shown to work" |

Evidence for each barrier is in `research/raw/adoption-barriers.md` with URLs. Growth asks for nothing to be built or changed; only stated.
