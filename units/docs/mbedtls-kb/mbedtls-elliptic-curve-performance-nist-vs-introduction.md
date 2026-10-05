---
id: "mbedtls-elliptic-curve-performance-nist-vs-introduction"
type: "concept"
domain: "security"
title: "Elliptic curve performance: NIST vs. Brainpool: Introduction"
summary: "Using different elliptic curves has a high impact on the performance of ECDSA, ECDHE and ECDH operations. Each type of curve was designed with a different primary goal in mind, which is reflected in the performance of the specific curves."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md#introduction"
license: "Apache-2.0"
mode: "V"
---

Using different elliptic curves has a high impact on the performance of ECDSA, ECDHE and ECDH operations. Each type of curve was designed with a different primary goal in mind, which is reflected in the performance of the specific curves.

The following numbers, measured with Mbed TLS 2.18.0  on a 3.40 GHz Core i7, are only indicative of the relative speed of the various curves. The absolute value depends on your platform. These numbers also use the default settings for speed-memory trade-offs, and you can read more about [Reducing Mbed TLS memory and storage footprint](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/../how-to/reduce-polarssl-memory-and-storage-footprint.md).
