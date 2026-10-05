---
id: "mbedtls-why-use-ephemeral-diffie-hellman-ciphersuites-supporting-ephemeral-diffie"
type: "concept"
domain: "security"
title: "Why use Ephemeral Diffie-Hellman: Ciphersuites supporting Ephemeral Diffie-Hellman"
summary: "There are a lot of ciphersuites that support Ephemeral Diffie-Hellman. The key exchange methods that use (EC)DHE in TLS are:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/ephemeral-diffie-hellman.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/ephemeral-diffie-hellman.md#ciphersuites-supporting-ephemeral-diffie-hellman"
license: "Apache-2.0"
mode: "V"
---

There are a lot of ciphersuites that support Ephemeral Diffie-Hellman. The key exchange methods that use (EC)DHE in TLS are:

- Ephemeral Diffie Hellman with RSA (DHE-RSA) key exchange
- Elliptic Curve Ephemeral Diffie Hellman with RSA (ECDHE-RSA) key exchange
- Elliptic Curve Ephemeral Diffie Hellman with ECDSA (ECDHE-ECDSA) key exchange
- Pre Shared Key with Diffie Hellman (DHE-PSK) key exchange
- Pre Shared Key with Elliptic Curve Diffie Hellman (ECDHE-PSK) key exchange
The full list of ciphersuites can be found in our [list of supported SSL ciphersuites](https://github.com/supported-ssl-ciphersuites).
