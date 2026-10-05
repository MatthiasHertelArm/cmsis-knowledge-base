---
id: "mbedtls-how-to-put-tls-keys-into-an-extern-protecting-a-server-s-private-key"
type: "concept"
domain: "security"
title: "How to put TLS keys into an external cryptoprocessor: Protecting a server's private key"
summary: "Protect your server's long-term private key: if the key is leaked, attackers can impersonate the server."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/ssl_async.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/ssl_async.md#protecting-a-server-s-private-key"
license: "Apache-2.0"
mode: "V"
---

Protect your server's long-term private key: if the key is leaked, attackers can impersonate the server.

One way to do this is to put the private key in an **external cryptoprocessor**. This is a separate environment that holds the server's private key. The external cryptoprocessor performs operations such as decryption or signature on behalf of the server, but doesn't allow the server to access the key itself. A typical example of an external cryptoprocessor is a hardware security module (HSM), which is a hardened device dedicated to holding keys that can't be extracted from the HSM and performing cryptographic operations with those keys. An external cryptoprocessor could also be, for example, a smartcard or a separate virtual environment.

If an attacker breaches the server, they can use the external cryptoprocessor only as long as they have access to the server. If the private key is stored directly on the server, then the attacker can copy the key and keep using it. However, if the key is in an external cryptoprocessor, then once the attacker loses access to the external cryptoprocessor, they lose access to the key. This isolates the damage. Furthermore, if the external cryptoprocessor keeps a key use log, the attacker cannot erase those logs.

To place the private key in an external cryptoprocessor, instead of the server, override the code that uses the private key with your own code that calls the external cryptoprocessor. You can do this by registering your code as callbacks in the TLS configuration object. When these callbacks are present, Mbed TLS doesn't need to have access to the private key.
