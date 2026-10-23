---
id: "mbedtls-elliptic-curve-performance-nist-vs-why-are-nist-curves-faster-than-brainpoo"
type: "concept"
domain: "security"
title: "Elliptic curve performance: NIST vs. Brainpool: Why are NIST curves faster than Brainpool curves"
summary: "Brainpool curves use random primes, as opposed to the quasi-Mersenne primes that NIST curves use. As a result, fast reduction is not possible for Brainpool curves, and this has major consequences for the performance of the different curves."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md#why-are-nist-curves-faster-than-brainpool-curves"
license: "Apache-2.0"
mode: "V"
---

Brainpool curves use random primes, as opposed to the quasi-Mersenne primes that NIST curves use. As a result, fast reduction is not possible for Brainpool curves, and this has major consequences for the performance of the different curves.
