# Prohibited or premature phrases

Mirrors capability snapshot section 9. `scripts/claims_lint.py` fails any content line matching these (case-insensitive) unless the line negates it. Say the registry claim instead.

| pattern | why (snapshot section 9) |
|---|---|
| `pool(s|ing)? your (devices|gpus|computers)` | pooling and partitioning do not exist (Gate D); remote execution is not pooling |
| `combine the (power|memory|gpus?) of` | see snapshot section 9 |
| `split(s|ting)? (a|one|the) model across` | see snapshot section 9 |
| `models? too big for (one|a single) (machine|device)` | see snapshot section 9 |
| `distributed inference` | same |
| `\bcluster\b` | same |
| `ai supercomputer` | see snapshot section 9 |
| `coming soon` | see snapshot section 9 |
| `join the ucompute network` | Swarm disabled, Gate F unverified |
| `contribute your gpu` | see snapshot section 9 |
| `share with the world` | see snapshot section 9 |
| `public network` | see snapshot section 9 |
| `decentrali[sz]ed network` | see snapshot section 9 |
| `peer-to-peer marketplace` | see snapshot section 9 |
| `earn credits` | no credits, billing, payments or payouts exist |
| `get paid for your gpu` | see snapshot section 9 |
| `buy credits` | see snapshot section 9 |
| `\bpricing\b` | see snapshot section 9 |
| `free credits` | see snapshot section 9 |
| `\brewards?\b` | see snapshot section 9 |
| `passive income` | see snapshot section 9 |
| `ucompute token` | see snapshot section 9 |
| `earn tokens` | see snapshot section 9 |
| `\bcrypto\b` | never required, not implemented |
| `on-chain` | see snapshot section 9 |
| `free forever` | no release; free is direction and not unlimited |
| `\bunlimited\b` | see snapshot section 9 |
| `\bdownload (now|the app|ucompute)\b` | no release record, no signed installers, no cohort open |
| `get the app` | see snapshot section 9 |
| `install now` | see snapshot section 9 |
| `available for (macos|windows|linux)` | see snapshot section 9 |
| `try the beta` | see snapshot section 9 |
| `early access` | see snapshot section 9 |
| `join the waitlist` | a sign-up needs its own owner authorization (spec 29.5) |
| `sign up` | see snapshot section 9 |
| `waitlist` | a sign-up needs its own owner authorization (spec 29.5) |
| `one-click install` | F-10-01 unverified |
| `installs in minutes` | see snapshot section 9 |
| `\bno setup\b` | see snapshot section 9 |
| `supported on (macos|windows|linux)` | no platform is SUPPORTED |
| `works on any hardware` | see snapshot section 9 |
| `runs any model` | see snapshot section 9 |
| `(nvidia|cuda|amd|rocm) support` | see snapshot section 9 |
| `works on your phone` | see snapshot section 9 |
| `runs on linux` | one CPU daemon in tests; Linux is PLANNED |
| `linux (version|app)` | see snapshot section 9 |
| `works on ubuntu` | see snapshot section 9 |
| `runs on your home server` | see snapshot section 9 |
| `runs on apple silicon` | only M2 on macOS 26.2 is experimental |
| `\b(m1|m3|m4) (mac|macs|macbook|pro|max|ultra)\b` | see snapshot section 9 |
| `any mac` | see snapshot section 9 |
| `runs (llama|mistral|deepseek|qwen 7b|gemma)` | evidence covers models up to 0.5B (memory planning to 1.5B) |
| `\b(7b|13b|70b)\b` | evidence covers models up to 0.5B (memory planning to 1.5B) |
| `x faster|\d+(\.\d+)?[x×] faster` | all tok/s figures are path checks on tiny models |
| `speeds up inference` | see snapshot section 9 |
| `faster than the cloud` | all tok/s figures are path checks on tiny models |
| `faster on linux` | all tok/s figures are path checks on tiny models |
| `end-to-end private` | see snapshot section 9 |
| `never leaves your device` | the executing device sees the prompt; downloads use the internet |
| `nothing leaves your device` | see snapshot section 9 |
| `zero-knowledge` | see snapshot section 9 |
| `confidential computing` | see snapshot section 9 |
| `verifiable inference` | see snapshot section 9 |
| `provable inference` | see snapshot section 9 |
| `military-grade` | see snapshot section 9 |
| `works offline` | no offline test; first run downloads |
| `no internet needed` | see snapshot section 9 |
| `air-gapped` | see snapshot section 9 |
| `open protocol` | one implementation, experimental |
| `open standard` | see snapshot section 9 |
| `interoperable with` | see snapshot section 9 |
| `stable protocol` | see snapshot section 9 |
| `protocol 1\.0` | see snapshot section 9 |
| `python (and|&) typescript sdks?` | SDKs are planned |
| `full openai api compatibility` | see snapshot section 9 |
| `tool calling` | see snapshot section 9 |
| `function calling` | see snapshot section 9 |
| `view on github` | source unpublished; the public repo holds only a LICENSE |
| `github\.com/div0rce` | see snapshot section 9 |
| `works across the internet` | see snapshot section 9 |
| `connect from anywhere` | same-network evidence only |
| `remote access` | see snapshot section 9 |
| `find each other automatically on any network` | see snapshot section 9 |
| `pair any two` | see snapshot section 9 |
| `any of your devices` | see snapshot section 9 |
| `\b(code.)?signed (installer|app|build|binary|dmg|msi|download)` | no release record, no signed installers, no cohort open |
| `notarized` | see snapshot section 9 |
| `verified installer` | see snapshot section 9 |
| `secure installer` | see snapshot section 9 |
| `automatic updates` | not started |
| `mobile app` | see snapshot section 9 |
| `picks the best device` | see snapshot section 9 |
| `ucompute cloud (is|offers|available)` | see snapshot section 9 |
| `enterprise (plan|edition)` | no paid service authorized |
| `\bper month\b` | see snapshot section 9 |
| `ucompute™|ucompute®|\(tm\)` | trademark clearance open |
| `the linux of (ai|compute)` | see snapshot section 9 |
| `ucompute\.app` | see snapshot section 9 |
| `ucompute setup` | see snapshot section 9 |
| `\d+ (users|testers|downloads|devices in the field)` | no release record, no signed installers, no cohort open |
| `voiceover|nvda|screen.reader` | no screen reader run yet |
| `mac.to.mac` | pairing failed on 2026-10-21, not repeated |

## Identity patterns (never negatable)

Any match anywhere in `content/` fails the lint: founder identity, affiliation, testers, machines, networks, private repositories, paths, IP addresses, private site addresses.

- `nasr`
- `div0rce`
- `moustafa`
- `rutgers`
- `scarletmail`
- `\bkyle\b`
- `\bjess\b`
- `sentinel`
- `eduroam`
- `cloudflareaccess`
- `ucompute-dev`
- `ucompute-website`
- `ucompute-core-lab`
- `/Users/`
- `C:\\Users`
- `C:/Users`
- `\b(?!127\.0\.0\.1\b)(?!0\.0\.0\.0\b)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b`
- `users\.noreply\.github\.com`
- `@[a-z0-9.-]+\.edu\b`
- `preview\.ucompute\.org`
- `stage-snapshot`
