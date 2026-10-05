---
id: "mbedtls-how-to-use-server-name-indication-why-is-sni-useful"
type: "concept"
domain: "security"
title: "How to use Server Name Indication: Why is SNI useful?"
summary: "When several virtual servers are running on the same host with the same IP address but have different domain names with corresponding certificates, the host has no way of knowing which virtual server certificate to send during a handshake."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/use-sni.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/use-sni.md#why-is-sni-useful"
license: "Apache-2.0"
mode: "V"
---

When several virtual servers are running on the same host with the same IP address but have different domain names with corresponding certificates, the host has no way of knowing which virtual server certificate to send during a handshake. This is because the peers only send application layer data like domain names after the TLS handshake finishes.

One possible solution would be to have the virtual servers share a certificate. A more maintainable and flexible solution is to perform the handshake using the SNI Extension, which lets the server know the DNS hostname(s) of the target virtual server. This allows the server to respond with a server-specific certificate.
