---
id: "mbedtls-mbed-tls-abstraction-layers-implementation-abstraction"
type: "concept"
domain: "security"
title: "Mbed TLS abstraction layers: Implementation abstraction"
summary: "These are abstractions for functions that we already provide an implementation for. However, some users may want to use their own versions instead, for example, those optimized for their platforms."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/generic/abstraction-layers.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/generic/abstraction-layers.md#implementation-abstraction"
license: "Apache-2.0"
mode: "V"
---

These are abstractions for functions that we already provide an implementation for. However, some users may want to use their own versions instead, for example, those optimized for their platforms.

Examples: AES, MD5 and Timing.

To enable an implementation abstraction:
- You'll need to enable the relevant macro: `MBEDTLS_XXX_ALT` in `mbedtls_config.h`.
- Provide a custom header, named: `xxx_alt.h`.
- Provide an implementation.

You can also opt to provide your own version of the `core` function of a module, rather than the whole module.

Examples: AES setkey, AES block encrypt and decrypt, and SHA process.

To enable an implementation abstraction, you must provide your own implementation of the relevant function with the same prototype as the default implementation.

<!--",abstraction-layers,"Explanation on the different abstraction layers that Mbed TLS provides, such as for memory allocation. threading and cryptographic implementations.",,"abstraction, threading, memory, printf",published,"2014-02-06 13:04:00",1,2425,"2017-04-23 15:02:00","Paul Bakker"-->
