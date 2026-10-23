---
id: "mbedtls-tls-prf-key-derivation"
type: "concept"
domain: "security"
title: "TLS PRF key derivation"
summary: "RFC 5246 defines the pseudorandom function (PRF) as follows: >In addition, a construction is required to do expansion of secrets into blocks of data for the purposes of key generation or validation."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/tls_prf.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/tls_prf.md"
license: "Apache-2.0"
mode: "V"
---

[RFC 5246](https://tools.ietf.org/html/rfc5246) defines the pseudorandom function (PRF) as follows:
>In addition, a construction is required to do expansion of secrets
   into blocks of data for the purposes of key generation or validation.
   This pseudorandom function (PRF) takes as input a secret, a seed, and
   an identifying label and produces an output of arbitrary length.

The TLS PRF is a function that generates key material, which security protocols can use to derive a key for ciphering data. Many security protocols that rely on TLS for authentication, such as [DTLS-SRTP](https://tools.ietf.org/html/rfc5764) and [EAP-TLS](https://tools.ietf.org/html/rfc5216), use the TLS-defined PRF and other TLS handshake data (the master key and the handshake random bytes) to derive their own key material, using their own defined string label.
