---
id: 2026-10-30-what-the-audit-log-records
title: What UCompute's audit log records, and what it never records
type: engineering-note
audience: multi-device-developers, homelab-selfhosting, oss-infra
channel_intent: website-handoff (Engineering notes), later syndication with canonical link
claims: [audit, local-only, device-sees-prompt, mesh-pair-choose, revocation, no-release, license]
status: draft
sources: engineering ADR-0003 section 9.11 (audit), crates/ucompute-observability/src/lib.rs (forbidden field keys, size bound, rotation constants, security kinds), docs/security/THREAT_MODEL.md rows M3-26, M3-27, M3-28 and secure default SD-08, capability snapshot 2026-10-23b claim 10 and section 3.2
---

# What UCompute's audit log records, and what it never records

*Development build, October 2026. UCompute is in development. There is no public release or download yet. The behaviour below is as built in development builds; the two-machine runs listed at the end checked the log's contents, and the rest is held by automated tests on one computer.*

If you let a second device run your prompts, two questions follow: what did I send where, and did any of it end up in a log? UCompute answers the first with an audit trail and the second with a rule the audit code enforces on itself. Audit logs record each off-device request without the prompt or the response.

## What is recorded

The audit trail is a file of JSON lines, one per event, readable only by the user account that owns it. Each line carries a UTC timestamp, an event kind, the id of the other device where one is involved, and structured fields: sizes, ids, reasons, durations. The kinds that exist in development builds:

| Event | When it is written |
|---|---|
| `pairing_started`, `pairing_succeeded`, `pairing_failed`, `pairing_locked` | a pairing window opens, completes, fails, or locks after repeated failures |
| `peer_connected`, `peer_rejected`, `peer_disconnected` | a paired device connects, an unpaired or revoked device is refused, a connection ends |
| `remote_request` | a request is sent to a paired device (phase `sent`), and once more when it ends (phase `finished`, with the outcome and the request id) |
| `peer_revoked`, `peer_removed` | you revoke a device, or a revocation from another device in the group is applied |
| `privacy_changed`, `network_changed`, `local_priority_changed`, `group_updated` | you change a setting that governs what may leave or enter the device |
| `audit_rotated` | the file rolled over; the line says how many bytes were kept and how many dropped |

Two properties of the `remote_request` line matter most:

- **The `sent` line is written before the request leaves the device.** If the line cannot be written, nothing is sent. So there is no path by which a request reaches another device without a record on yours.
- **The serving device logs the same request id.** When you run a request on your desktop from your laptop, both machines carry a line with the same id, one as sender and one as server.

A request that policy stops on the sending side writes no line at all: nothing left the device, so there is nothing to record.

## What is never recorded

The audit writer refuses, at the point of writing, any field named `prompt`, `content`, `messages`, `api_key`, `private_key` or `pkcs8`, and any string value longer than 2 KiB. Prompts and keys are longer than that; ids, reasons and sizes are not. The device's private key is never formatted into any log, and the diagnostics bundle a user can export is built from redacted data. This is a stated secure default of the product: prompts are never logged, not in engine logs, API logs, metrics, error messages, execution records or diagnostics bundles.

In the two-machine runs that checked it, the audit logs on both devices contained no prompt or response text.

## Why the trail is bounded, and why a flood cannot erase the important part

The file rotates at 8 MiB and three rotated files are kept, so the trail is bounded at roughly 32 MiB. That is a deliberate choice: an unbounded log is a disk-filling attack. The cost is that a very long history is dropped, and the design makes the drop visible: every new file begins with an `audit_rotated` line that states how many bytes were dropped.

A paired device could try to use that rotation against you: flood you with requests, and the lines you care about (a revocation, a privacy change) would scroll out. So the kinds that a remote device cannot produce at will, the owner actions and the revocations, are also copied to a second, separately rotated security trail. Lines a peer can trigger repeatedly, such as refused requests or connections, are not copied there, or the flood would rotate that file away too. Refused-connection lines are additionally capped at 20 per minute in the main trail; beyond that they are counted, and the count rides on the next line written. Reading the trail merges the two files back together.

## What this does not do

- It does not hide your prompt from the device that runs it. The device that runs your request processes your prompt. Pair only devices you control or trust. The audit trail tells you that a request went to that device; it cannot tell you what the device did with it.
- It does not record local-only work. Your prompts and responses stay on your device unless you pair another device and choose to run a request there. Local-only mode refuses every off-device request. Downloading a model or the engine uses the internet. Requests that never leave the device are not audit events.
- It is not a forensic archive. Roughly 32 MiB of history is kept per trail; what is dropped is reported, not recovered.
- Each request runs whole on one device; UCompute does not split a model across devices, so there is one serving device per request and one pair of matching lines.

## Where this has run

Development builds, October 2026. The audit logs were checked for prompt or response text in two-machine runs between one Apple M2 Mac (macOS 26.2) and one Windows 11 laptop (Intel Arc 140V), and between that Mac and one Linux desktop computer (Ubuntu, processor only, a development build of the background program started by hand; Linux is a planned platform, not a supported one). The refusal of content-bearing fields, the rotation behaviour, the security trail surviving a request flood, and the redaction of the diagnostics bundle are held by automated tests on one computer. You can revoke a paired device at any time. In our two-machine tests, its connection closed less than a tenth of a second after the revoke (between 0.002 s and 0.061 s in four runs), and its next request was refused.

UCompute's code is licensed under Apache-2.0. The source has not been published yet.
