---
id: 2026-11-01-memory-fit-explainer
title: Before you load a model: how UCompute estimates whether a GGUF fits
type: explainer
audience: local-ai-developers, ai-app-builders
channel_intent: website-handoff (Engineering notes), search page
claims: [catalog-fit, engine, platforms, no-release, license]
status: draft
sources: engineering crates/ucompute-models/src/feasibility.rs (read-only, calibration constants and check_fit), capability snapshot 2026-10-23b section 7 (numbers register: estimate vs measured), docs/VERIFICATION.md F-01-03
---

# Before you load a model: how UCompute estimates whether a GGUF fits

*Development build, October 2026. UCompute is in development; there is no public release or download yet.*

The most common first failure with a local model is not a crash. It is a machine that starts swapping, a laptop fan that never stops, and a first token that arrives a minute late. The cause is almost always the same: the model file was about the size of the free memory, and everything the engine allocates on top of the weights pushed it over.

Before you download a model, UCompute shows its size, its license and whether it fits in your computer's memory. Every download is checked against a pinned SHA-256 hash. This note explains the "fits in memory" part: what the estimate counts, where the numbers come from, and how far off it has been measured to be.

## The file size is not the footprint

A GGUF file is mostly weights, and the weights are only one of four things the engine keeps in memory:

| Component | What it is | How UCompute estimates it |
|---|---|---|
| **Weights** | The tensors in the file, minus the header | File size minus the data offset. If the model ties its input and output embeddings (no separate output tensor), the engine keeps a second copy of the token embedding on the compute device, so that tensor is counted twice |
| **KV cache** | The attention keys and values for every token in the context | Per-token bytes from the model's layer count, KV heads and head size, times the context length, with the context rounded up to whole blocks of 256 cells because that is how the engine allocates it (asking for a 128-token context allocates 256 cells) |
| **Compute buffers** | Scratch space for one batch of tokens through the graph | Batch size (512 by default, capped at the context) times a per-token cost that scales with the feed-forward width plus a per-cell cost for the attention mask |
| **Process baseline and tokenizer tables** | The engine process itself, its libraries, the GPU device, and the vocabulary maps | A measured fixed baseline, plus a per-token cost for the tokenizer. Byte-pair tokenizers keep token and merge maps that cost about 1.1 KiB per vocabulary entry on macOS; a 150,000-entry vocabulary is therefore about 160 MiB before a single layer loads, more than the KV cache of a small model at a 4,096-token context |

The total is compared with the memory the system reports as available, keeping a headroom fraction spare. If it does not fit, the verdict is a sentence, not a stack trace:

> This model needs about 3.2 GiB but only 2.1 GiB is available.

## Where the constants come from

Every coefficient in the estimate was measured against the pinned engine release on an Apple M2 Mac, by reading the engine's own log lines for the model buffer, the KV cache and the compute buffer, and the process's peak physical footprint with a filled context. The constants live in one place in the code with the measurement that produced each of them, so a new engine release means re-measuring, not guessing.

Measured against the engine on fourteen model and context combinations, from a 260,000-parameter test model to a 1.5-billion-parameter instruct model, the estimate landed between 4.6 % below and 8.9 % above the engine's actual footprint. Memory-fit estimates are calibrated for Apple Silicon Macs; a Linux CPU build measured a much smaller tokenizer and baseline overhead, and the estimate uses its own figures there. Windows is not yet separately measured and uses the larger macOS figures, which errs on the side of saying "does not fit".

## Why the estimate is shown before the download

A model that does not fit is a model you should not have spent a gigabyte of bandwidth on. The catalog entry carries the information the estimate needs, so the verdict is available before the first byte of weights arrives. The same estimate runs again before every load, against the memory available at that moment, because a browser with forty tabs changes the answer.

## What this does not claim

- It is an estimate, not a guarantee. Headroom is deliberately kept.
- It has been calibrated on small models (memory planning up to 1.5 billion parameters) and on one engine release.
- No platform is declared supported yet. macOS 26.2 on Apple M2 and Windows 11 on an Intel Core Ultra 7 258V with Arc 140V are experimental; Linux, other GPUs and phones (as clients) are planned.

UCompute runs models through a pinned release of llama.cpp (MIT), downloaded on first use and verified against its published hash; UCompute does not write its own inference kernels. UCompute's code is licensed under Apache-2.0. The source has not been published yet.
