---
id: "mbedtls-why-to-add-an-entropy-source-limited-sources"
type: "concept"
domain: "security"
title: "Why to add an entropy source: Limited sources"
summary: "If you have an entropy source that only provides some limited entropy, but not on every poll, it can be wise to select a threshold value of 0."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-entropy-sources-to-entropy-pool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-entropy-sources-to-entropy-pool.md#limited-sources"
license: "Apache-2.0"
mode: "V"
---

If you have an entropy source that only provides some limited entropy, but not on every poll, it can be wise to select a *threshold* value of **0**. A zero-threshold does not cause the entropy pool to return an error if it cannot provide any entropy in 256 calls.
