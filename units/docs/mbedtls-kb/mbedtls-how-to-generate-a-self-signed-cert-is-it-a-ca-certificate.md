---
id: "mbedtls-how-to-generate-a-self-signed-cert-is-it-a-ca-certificate"
type: "concept"
domain: "security"
title: "How to generate a self-signed certificate: Is it a CA certificate?"
summary: "If you want this self-signed certificate to be a CA certificate capable of signing other certificates, enable it with is_ca=1."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-a-self-signed-certificate.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-a-self-signed-certificate.md#is-it-a-ca-certificate"
license: "Apache-2.0"
mode: "V"
---

If you want this self-signed certificate to be a CA certificate capable of signing other certificates, enable it with `is_ca=1`.

You then need to decide if this CA certificate can only sign regular certificates (`max_pathlen=0`) or if it is at the top of other intermediate CA certificates.
