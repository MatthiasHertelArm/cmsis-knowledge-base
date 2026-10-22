---
id: "mbedtls-entropy-collection-random-generati-how-does-entropy-collection-work"
type: "concept"
domain: "security"
title: "Entropy collection, random generation with threads: How does entropy collection work"
summary: "The entropy collector works by gathering entropy from multiple sources and integrating them into its internal entropy state. Each time entropy is collected the internal state gets better."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/entropy-collection-and-random-generation-in-threaded-environment.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/entropy-collection-and-random-generation-in-threaded-environment.md#how-does-entropy-collection-work"
license: "Apache-2.0"
mode: "V"
---

The entropy collector works by gathering entropy from multiple sources and integrating them into its internal entropy state. Each time entropy is collected the internal state gets better. Unless additional entropy sources have been added to the default entropy collector sources, mostly OS dependent random sources are used. Each time the entropy collector gathers entropy from the system, the entropy gets extracted and reduced.
