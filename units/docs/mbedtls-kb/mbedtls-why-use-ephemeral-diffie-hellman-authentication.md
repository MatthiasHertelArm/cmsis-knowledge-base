---
id: "mbedtls-why-use-ephemeral-diffie-hellman-authentication"
type: "concept"
domain: "security"
title: "Why use Ephemeral Diffie-Hellman: Authentication"
summary: "Ephemeral Diffie-Hellman doesn't provide authentication on its own, because the key is different every time. So neither party can be sure that the key is from the intended party."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/cryptography/ephemeral-diffie-hellman.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/ephemeral-diffie-hellman.md#authentication"
license: "Apache-2.0"
mode: "V"
---

Ephemeral Diffie-Hellman doesn't provide authentication on its own, because the key is different every time. So neither party can be sure that the key is from the intended party.

Within SSL you will often use DHE as part of a key-exchange that uses an additional authentication mechanism (e.g. **RSA**, **PSK** or **ECDSA**). So the fact that the SSL server **signs** the content of its server key exchange message that contain the ephemeral public key implies to the SSL client that this Diffie-Hellman public key is from the SSL server.
