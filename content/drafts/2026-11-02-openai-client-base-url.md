---
id: 2026-11-02-openai-client-base-url
title: Point the official OpenAI Python and JavaScript clients at a local server
type: search-page
audience: ai-app-builders
channel_intent: website-handoff (docs or notes), syndication to dev.to/Hashnode when authorized
claims: [openai-clients, run-local, local-only, no-release, license]
status: draft
sources: engineering README (serve on 127.0.0.1:8192, OpenAI-compatible API); capability snapshot 2026-10-23b claim 4 (openai 3.31.0 and openai npm 6.49.0 verified); https://github.com/openai/openai-python (base_url parameter); https://github.com/openai/openai-node (baseURL option)
---

# Point the official OpenAI Python and JavaScript clients at a local server

*Development build, October 2026. UCompute is in development; there is no public release or download yet. The client-side steps below apply to any server that speaks the OpenAI chat-completions API; the UCompute-specific details are marked.*

If your application already uses the official OpenAI client libraries, you do not need a different SDK to talk to a model running on your own machine. Both libraries take a base URL. Change it, and keep the rest of your code.

## Python

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8192/v1",   # your local server
    api_key="unused",                      # the library requires a value; a local server may ignore it
)

stream = client.chat.completions.create(
    model="qwen2.5-0.5b-instruct-q4_k_m",  # the model id your local server exposes
    messages=[{"role": "user", "content": "Explain unified memory in two sentences."}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

## JavaScript / TypeScript

```ts
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "http://127.0.0.1:8192/v1",
  apiKey: "unused",
});

const stream = await client.chat.completions.create({
  model: "qwen2.5-0.5b-instruct-q4_k_m",
  messages: [{ role: "user", content: "Explain unified memory in two sentences." }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
```

## Three things that trip people up

1. **The `/v1` suffix.** Most local servers mount the OpenAI routes under `/v1`. If you get a 404 on `chat/completions`, that is usually why.
2. **The API key.** The libraries refuse to construct a client without one, even when the server ignores it. Pass any non-empty string, or set `OPENAI_API_KEY` in the environment to a placeholder. Never put a real cloud key in a local configuration you will commit.
3. **The model id.** A local server exposes its own ids. List them with `GET /v1/models` on your base URL, and use one of those strings; the cloud model names will not exist there.

## What UCompute does (development build)

UCompute's local API works with the official OpenAI Python and JavaScript client libraries; only the base URL changes. Demonstrated on an Apple M2 Mac (macOS 26.2); the platform is experimental. Chat and completions with streaming; tool calling is not yet verified.

- The server is started with `ucompute serve` and listens on `127.0.0.1:8192`, loopback only, by default. Nothing else on your network can reach it unless you deliberately change that.
- UCompute Run runs small open models on your own computer, with no account and no UCompute service. By default, your requests stay on your device. Demonstrated on an Apple M2 Mac (macOS 26.2) and a Windows 11 laptop with an Intel Arc 140V GPU; both platforms are experimental; other platforms are not yet available, and most are planned. Downloading a model or the engine uses the internet.
- Your prompts and responses stay on your device unless you pair another device and choose to run a request there. Local-only mode refuses every off-device request. Downloading a model or the engine uses the internet.
- The API also serves `/openapi.json` and `/metrics`, so you can see exactly which request fields a route accepts.

## Why the base URL is the whole integration

The point of an OpenAI-compatible local server is that the application layer does not change: the same SDK, the same streaming loop, the same error handling. What changes is where the request goes, and therefore who sees it. For development, tests and private data, that is a large difference for a one-line change.

UCompute's code is licensed under Apache-2.0. The source has not been published yet.
