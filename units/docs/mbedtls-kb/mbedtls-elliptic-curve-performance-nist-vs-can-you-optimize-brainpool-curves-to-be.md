---
id: "mbedtls-elliptic-curve-performance-nist-vs-can-you-optimize-brainpool-curves-to-be"
type: "concept"
domain: "security"
title: "Elliptic curve performance: NIST vs. Brainpool: Can you optimize Brainpool curves to be as fast as the NIST curves?"
summary: "Unfortunately, this is not possible. The design decision for Brainpool to use random primes was aimed at:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md#can-you-optimize-brainpool-curves-to-be-as-fast-as-the-nist-curves"
license: "Apache-2.0"
mode: "V"
---

Unfortunately, this is not possible. The design decision for Brainpool to use random primes was aimed at:

* avoiding possible patent issues with fast reduction algorithms
* avoiding potential security issues with non-random primes

Brainpool curve performance cannot be adjusted to be equivalent to NIST curve performance.
