---
id: "mbedtls-entropy-collection-random-generati-entropy-collection-and-random-generation"
type: "concept"
domain: "security"
title: "Entropy collection, random generation with threads: Entropy collection and random generation"
summary: "Random generators, such as the CTR-DRBG module, require a source of entropy to kick-start and refresh their own internal entropy state. Mbed TLS includes the Entropy collection module to provide a central pool of entropy to extract entropy from."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/entropy-collection-and-random-generation-in-threaded-environment.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/entropy-collection-and-random-generation-in-threaded-environment.md#entropy-collection-and-random-generation"
license: "Apache-2.0"
mode: "V"
---

Random generators, such as the [CTR-DRBG module](https://github.com/ctr-drbg-source-code), require a source of entropy to kick-start and refresh their own internal entropy state. Mbed TLS includes the [Entropy collection module](https://github.com/entropy-source-code) to provide a central pool of entropy to extract entropy from. In a single-threaded application, both the entropy pool and the random generator exist within the same thread context. In case of a multi-threaded application, you can either use a central entropy pool and/or random generator or thread-specific versions.
