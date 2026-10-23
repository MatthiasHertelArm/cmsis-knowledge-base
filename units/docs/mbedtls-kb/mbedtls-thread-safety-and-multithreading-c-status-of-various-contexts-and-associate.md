---
id: "mbedtls-thread-safety-and-multithreading-c-status-of-various-contexts-and-associate"
type: "concept"
domain: "security"
title: "Thread safety and multithreading: concurrency issues: Status of various contexts and associated functions"
summary: "All contexts have associated init() and free() functions. For contexts that include mutexes, these functions create and initialize the mutex and then free and destroy it."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/thread-safety-and-multi-threading.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/thread-safety-and-multi-threading.md#status-of-various-contexts-and-associated-functions"
license: "Apache-2.0"
mode: "V"
---

All contexts have associated `_init()` and `_free()` functions. For contexts that include mutexes, these functions create and initialize the mutex and then free and destroy it. If you share a context between threads, you need to call these functions only from the main thread, at the beginning and end of the context's lifetime.

Mbed TLS currently provides automatic locking (when the threading layer is enabled) for relevant functions in the following modules (unless indicated otherwise):

- RSA.
- The SSL cache callbacks provided in `ssl_cache.c`.
- Memory buffer-based allocator.
- Entropy
- In the X.509 module, `mbedtls_x509_crt_parse_path()` is thread-safe..
- CTR-DRBG and HMAC-DRBG.
- The SSL session tickets callbacks provided in *ssl_ticket.c*.
- The DTLS CLientHello cookie callbacks provided in *ssl_cookie.c*.
- PSA, since Mbed TLS 3.6.0.

This covers the most common cases in which you need to share a context across threads. If you have use cases in which you need to share another context across threads, please let us know.
