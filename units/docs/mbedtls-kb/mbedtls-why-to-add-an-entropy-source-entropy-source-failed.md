---
id: "mbedtls-why-to-add-an-entropy-source-entropy-source-failed"
type: "concept"
domain: "security"
title: "Why to add an entropy source: Entropy source failed"
summary: "When collecting entropy for a request, the entropy pool does a maximum of 256 polls to each entropy source to retrieve entropy from them."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-entropy-sources-to-entropy-pool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-entropy-sources-to-entropy-pool.md#entropy-source-failed"
license: "Apache-2.0"
mode: "V"
---

When collecting entropy for a request, the entropy pool does a maximum of 256 polls to each entropy source to retrieve entropy from them. If the **threshold** value for a source is higher than the entropy it can deliver in those 256 polls, you **will** receive an error!
