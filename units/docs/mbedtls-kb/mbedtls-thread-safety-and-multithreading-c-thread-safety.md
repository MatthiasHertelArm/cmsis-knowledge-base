---
id: "mbedtls-thread-safety-and-multithreading-c-thread-safety"
type: "concept"
domain: "security"
title: "Thread safety and multithreading: concurrency issues: Thread safety"
summary: "You can use Arm Mbed TLS in threaded and nonthreaded environments. To keep Mbed TLS thread-safe, it is important to remember a few things."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/thread-safety-and-multi-threading.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/thread-safety-and-multi-threading.md#thread-safety"
license: "Apache-2.0"
mode: "V"
---

You can use Arm Mbed TLS in threaded and nonthreaded environments. To keep Mbed TLS thread-safe, it is important to remember a few things.

First, most `mbedtls_xxx()` functions use an explicit context. Most of the time, as long as threads do not share this context, you're safe. However, sometimes threads can share a context indirectly. For example, an SSL context can point to an RSA context (the private key).

The default philosophy is that a single thread should only use or access one context at a same time, unless:

- The documentation for the functions that access the shared context explicitly states the function is thread-safe, or
- You perform explicit locking yourself (perhaps in a wrapper function).

**Warning: [The PSA API is not thread-safe before Mbed TLS 3.6.0](https://github.com/Mbed-TLS/mbedtls/issues/3263).** Upgrade to the 3.6 LTS branch or newer if you need the PSA API or TLS 1.3 (which uses PSA under the hood) in a multithreaded application. Since Mbed TLS 3.6.0, the PSA API is thread-safe when `MBEDTLS_THREADING_C` is enabled.
