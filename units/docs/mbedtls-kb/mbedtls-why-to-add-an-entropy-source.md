---
id: "mbedtls-why-to-add-an-entropy-source"
type: "concept"
domain: "security"
title: "Why to add an entropy source"
summary: "Good entropy is the fundamental basis for good cryptography and SSL or TLS. If your entropy is weak or predictable, a strong adversary can break your security."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/add-entropy-sources-to-entropy-pool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/add-entropy-sources-to-entropy-pool.md"
license: "Apache-2.0"
mode: "V"
---

Good entropy is the fundamental basis for good cryptography and SSL or TLS. If your entropy is weak or predictable, a strong adversary can break your security.

Therefore, you want to have at least one, but preferably multiple sources of good or reasonable entropy.

For that purpose, Arm Mbed TLS provides the [entropy collector](https://github.com/entropy-source-code). The entropy collector takes entropy from multiple sources and combines it into a single entropy source for use.
