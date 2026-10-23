---
id: "mbedtls-elliptic-curve-performance-nist-vs-curve25519-support"
type: "concept"
domain: "security"
title: "Elliptic curve performance: NIST vs. Brainpool: Curve25519 support"
summary: "Bernstein & al have designed high-performance alternatives, such as Curve25519 for key exchange and Ed25519 for signatures."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/elliptic-curve-performance-nist-vs-brainpool.md#curve25519-support"
license: "Apache-2.0"
mode: "V"
---

Bernstein & al have designed high-performance alternatives, such as **Curve25519** for key exchange and **Ed25519** for signatures. Unfortunately, they use slightly different data structures and representations than the other curves, so they haven't been ported yet to TLS and PKIX in Mbed TLS. We do support basic Curve25519 arithmetic though. Their use in TLS has been standardized in [RFC 8422](https://tools.ietf.org/html/rfc8422).
