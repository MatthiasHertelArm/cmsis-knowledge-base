---
id: "mbedtls-thread-safety-and-multithreading-c-thread-safety-with-different-versions"
type: "concept"
domain: "security"
title: "Thread safety and multithreading: concurrency issues: Thread safety with different versions"
summary: "Mbed TLS has a generic threading layer that handles default locks and mutexes for the user and abstracts the threading layer to allow easy pluging in any thread-library."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/thread-safety-and-multi-threading.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/thread-safety-and-multi-threading.md#thread-safety-with-different-versions"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS has a generic threading layer that handles default locks and mutexes for the user and abstracts the threading layer to allow easy pluging in any thread-library.

Defining **MBEDTLS_THREADING_C** in `mbedtls_config.h` enables this threading layer. Please see [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../compiling-and-building/how-do-i-configure-mbedtls.md) for more information. It is not enabled by default; you also need to pick an underlying threading library. We provide built-in support for `pthread` with **MBEDTS_THREADING_PTHREAD**. You can also plug any other thread-library with **MBEDTLS_THREADING_ALT** and call `mbedtls_threading_set_alt()` at the beginning of your program and `mbedtls_threading_free_alt()` at the end.
