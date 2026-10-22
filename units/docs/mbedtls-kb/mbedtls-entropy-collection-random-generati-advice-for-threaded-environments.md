---
id: "mbedtls-entropy-collection-random-generati-advice-for-threaded-environments"
type: "concept"
domain: "security"
title: "Entropy collection, random generation with threads: Advice for threaded environments"
summary: "Regarding entropy, our advice is to use a central entropy collector. Initialize once. This makes sure that the entropy collector gets the best entropy from its sources as it does not have to share with sibling entropy collectors."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/entropy-collection-and-random-generation-in-threaded-environment.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/entropy-collection-and-random-generation-in-threaded-environment.md#advice-for-threaded-environments"
license: "Apache-2.0"
mode: "V"
---

Regarding entropy, our advice is to use a central entropy collector. Initialize once. This makes sure that the entropy collector gets the best entropy from its sources as it does not have to share with sibling entropy collectors. For more details, see [Thread Safety and Multi Threading](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/thread-safety-and-multi-threading.md).

You have two options:

* For each thread, use a separate CTR-DRBG or HMAC-DRBG random generator using a thread-specific value (like the thread ID) for the custom personalization string. Provide the DRBG with `mbedtls_entropy_func()` as its entropy callback. This ensures that the random generators between the different threads have the least amount of correlation possible and can thus be considered as independent as possible.
 
* Use a central CTR-DRBG or HMAC-DRBG context initialized once in the main thread, and share in across threads. The DRBG modules are thread-safe, as they contain locks within the contexts, which are used within the modules if threading is enabled, see [Thread Safety and Multi Threading](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/thread-safety-and-multi-threading.md).
