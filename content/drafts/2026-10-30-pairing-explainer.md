---
id: 2026-10-30-pairing-explainer
title: How two UCompute devices pair: the code, the keys and the revoke
type: engineering-note
audience: multi-device-developers, oss-infra
channel_intent: website-handoff (Engineering notes), later syndication with canonical link
claims: [mesh-pair-choose, transport, revocation, local-only, device-sees-prompt, audit, connect-by-address, platforms, no-release, license]
status: draft
sources: engineering ADR-0003 section 9 (implementation notes), docs/security/THREAT_MODEL.md section 2.13 and 4, capability snapshot 2026-10-23b sections 3.2, 8 and 9 (all read-only, mirrored in evidence/upstream/)
---

# How two UCompute devices pair: the code, the keys and the revoke

*Development build, October 2026. UCompute is in development; there is no public release or download yet. This note describes behaviour that has been tested with development builds on the hardware named at the end.*

You have a laptop and a desktop with a better GPU. You want a prompt typed on the laptop to run on the desktop. The usual way to do this with a local model server is to bind it to every network interface and point the laptop at the desktop's address. That works, and it also means anything on the network that can reach that port can send prompts, read answers, and often load models. UCompute Mesh takes a different route: two devices pair once with a short code, every later connection is mutually authenticated and encrypted, and either device can cut the other off with one action. This note explains how that is built.

One sentence to keep in mind throughout: **a request runs whole on one device**. UCompute Mesh lets you pair your own devices with a short code and choose which one runs a request. Each request runs whole on one device; UCompute does not split a model across devices.

## Every device has one key

Each UCompute device generates one Ed25519 key pair the first time it runs. That key is the device's identity. There are no certificates, no certificate authority and no accounts: the peer transport is QUIC with TLS 1.3 using raw public keys (RFC 7250), both ways. When two devices connect, each one proves it holds the private key for a public key the other has already pinned. If the key is not pinned, the handshake fails before any application data moves.

So pairing is the act of getting the other device's public key into your pin list in a way you can trust, and nothing more.

## Pairing: a six-digit code, used once

Typing a long public key fingerprint on a second machine is error-prone, so pairing uses a short code and a password-authenticated key exchange (SPAKE2). The order of events, as built:

```
  Device A (shows the code)                 Device B (types the code)
  ─────────────────────────                 ─────────────────────────
  opens a pairing endpoint,
  120-second window, 6-digit code  ──────▶  user types the code
                                   ◀──────  TLS 1.3 connection (any key accepted here;
                                            trust comes from the code, not the handshake)
                                   ◀──────  SPAKE2 message B
  SPAKE2 message A                 ──────▶
  both derive the shared secret K
  both read a 32-byte value exported from this TLS session
  MAC_A = HMAC(K, "A" ‖ exporter ‖ idA ‖ idB)  ──────▶
                                   ◀──────  MAC_B = HMAC(K, "B" ‖ exporter ‖ idA ‖ idB)
  each checks the other's MAC in constant time
  only now: exchange device name and service port
  both pin the other's key; both write an audit line
```

Three details carry the security:

1. **The confirmation is bound to this TLS session and to both identities.** The MAC covers a value exported from the TLS session and both device ids. A relay that terminates TLS on each side presents its own key on each leg, so the exported values differ, both MACs fail, and both ends record a man-in-the-middle attempt. A wrong code fails the same check.
2. **Nothing is learned before the MAC verifies.** The device name and the service port are sent only after the confirmation succeeds. A party that does not know the code learns neither.
3. **Guessing is bounded.** The code is six uniformly random digits, single use, valid for 120 seconds. The device handles one attempt at a time, each with a ten-second limit, and after the sixth failure within 60 seconds the pairing endpoint closes.

A QR code variant carries the device's public key, its address and a secret. A device that scanned the QR accepts only that key inside the handshake; if another device answers at that address, nothing is pinned.

## After pairing: the handshake is the gate

Once both devices hold each other's keys, every connection between them is a mutually authenticated TLS 1.3 handshake. Some choices that follow from "the verdict is inside the handshake":

- **No session resumption.** TLS 1.3 resumption would skip the client-key check on reconnect, which is exactly where a revoked device would try to return. UCompute issues no tickets and keeps no session cache, so every connection is a full handshake against the current pin list.
- **No 0-RTT, no plaintext path.** There is no unencrypted peer transport and no downgrade negotiation; TLS 1.3 only.
- **Address validation before cryptography.** The endpoint answers an unvalidated source with a QUIC Retry first, so a flood of spoofed packets costs no TLS work.
- **A refusal is only believed from the device itself.** A close or alert that arrives before the dialler has read the other device's own hello on the control stream is treated as unproven, because such packets can be forged on the path. The dialler reports "did not prove it is that device" and tries the next address. Every address is a hint; the key is the identity. This is also why paired devices can reconnect by address on networks that block discovery: an address alone is never trusted.

Traffic between paired devices is encrypted and both ends are authenticated: QUIC with TLS 1.3 and device keys pinned at pairing. Your device will not send work to a device you have not paired.

## Authentication is not authorization

A pinned key proves which device is on the other end. It does not decide whether that device may do anything. That is a separate policy layer:

- **Networking is off by default**, and nothing listens beyond loopback until you turn it on.
- **Local-only is the default privacy mode.** Your prompts and responses stay on your device unless you pair another device and choose to run a request there. Local-only mode refuses every off-device request. The policy check runs before any network activity, again before a stream opens, and again on the serving side.
- **Leaving local-only requires an acknowledgment.** The device that runs your request processes your prompt. Pair only devices you control or trust. The disclosure says this before you can choose a mode that sends work elsewhere; the API requires an explicit acknowledgment flag, the command line asks for a yes.
- **Serving is opt-in and per group.** A paired device may send you work only if you turned serving on and the two devices share a group that allows it. Per-device rate limits bound requests and tokens per minute, and a peer never takes the last engine slot ahead of your own work.

Audit logs record each off-device request without the prompt or the response. The audit line for a sent request is written before the request leaves the device; if it cannot be written, nothing is sent.

## Revocation: one action, immediate effect

You can revoke a paired device at any time. A revocation is a signed record that names the target device; it is accepted only if the issuer is itself pinned and not revoked and shares a group with the target, so a stranger cannot cut off your devices, and a replayed old revocation cannot undo a later re-pair. Every open connection to the revoked device closes at once, its key is refused inside the next handshake, and because there is no session resumption, there is no cached ticket to come back with. Other devices in the group receive the record over their existing connections and again on every reconnect until they confirm it.

In our two-machine tests, the revoked device's connection closed less than a tenth of a second after the revoke (between 0.002 s and 0.061 s in four runs), and its next request was refused.

## What this does not do

- It does not hide your prompt from the device that runs it. Encryption protects the traffic from observers on the network, not from the endpoint. The device that runs your request processes your prompt. Pair only devices you control or trust.
- It does not pool devices. Each request runs whole on one device; UCompute does not split a model across devices. Running one model across several devices is planned, with no date.
- It does not work across the internet. The evidence covers two devices on the same local network. There is no relay and no NAT traversal.
- It is not a stable protocol. One implementation exists and its peer profile is experimental.

## Where this has run

Tested with development builds between one Apple M2 Mac and one Windows 11 laptop (Intel Arc 140V) on the same Wi-Fi network or phone hotspot, and between that Mac and one Linux desktop computer (Ubuntu, processor only, a development build of the background program compiled and started by hand; no app or installer) on a home Wi-Fi network. In both pairs pairing has been shown starting from either device; with the Linux computer it went through the devices' background programs rather than an app window, and pairing started in the Mac app's window has been shown only with an earlier version of the app. Linux is a planned platform, not a supported one. Pairing between two Macs is not yet shown to work. Reconnecting by address was shown between one Mac and one Windows laptop on the same campus network, with development builds. The check that captured traffic carries no readable prompt text ran on one computer, and the statement that a device you have not paired cannot send you work was tested with several instances on one computer, not yet between two machines.

No platform is declared supported yet. macOS 26.2 on Apple M2 and Windows 11 on an Intel Core Ultra 7 258V with Arc 140V are experimental; Linux, other GPUs and phones (as clients) are planned.

UCompute's code is licensed under Apache-2.0. The source has not been published yet. When it is, this note will link to the modules and the tests that hold each rule above in place.
