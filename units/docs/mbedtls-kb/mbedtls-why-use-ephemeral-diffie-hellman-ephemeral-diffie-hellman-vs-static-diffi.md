---
id: "mbedtls-why-use-ephemeral-diffie-hellman-ephemeral-diffie-hellman-vs-static-diffi"
type: "concept"
domain: "security"
title: "Why use Ephemeral Diffie-Hellman: Ephemeral Diffie-Hellman vs static Diffie-Hellman"
summary: "When a key exchange uses Ephemeral Diffie-Hellman a temporary DH key is generated for every connection and thus the same key is never used twice."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/ephemeral-diffie-hellman.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/ephemeral-diffie-hellman.md#ephemeral-diffie-hellman-vs-static-diffie-hellman"
license: "Apache-2.0"
mode: "V"
---

**Ephemeral Diffie-Hellman** (DHE in the context of TLS) differs from the **static Diffie-Hellman** (DH) in the way that static Diffie-Hellman key exchanges always use the same Diffie-Hellman private keys. So, each time the same parties do a DH key exchange, they end up with the same shared secret.

When a key exchange uses Ephemeral Diffie-Hellman a temporary DH key is generated for every connection and thus the same key is never used twice. This enables **Forward Secrecy** (FS), which means that if the long-term private key of the server gets leaked, past communication is still secure.

This distinction also holds for the Elliptic Curve variants ECDHE (ephemeral, provides Forward Secrecy) and ECDH (static).

Due to increasing concern about pervasive surveillance, key exchanges that provide Forward Secrecy are recommended, see for example [RFC 7525, section 6.3](https://tools.ietf.org/html/rfc7525#section-6.3).
