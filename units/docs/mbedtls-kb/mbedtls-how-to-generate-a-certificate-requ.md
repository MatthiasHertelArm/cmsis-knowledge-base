---
id: "mbedtls-how-to-generate-a-certificate-requ"
type: "concept"
domain: "security"
title: "How to generate a Certificate Request (CSR)"
summary: "This tutorial describes how to generate your own certificate request for use in an online SSL certificate request."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-a-certificate-request-csr.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-a-certificate-request-csr.md"
license: "Apache-2.0"
mode: "V"
---

This tutorial describes how to generate your own certificate request for use in an online SSL certificate request.

Mbed TLS includes the core and applications for generating and using certificate requests. Mbed TLS 4 does not provide a command-line program for generating keys, so this tutorial uses OpenSSL to create the key file.

This article assumes you have compiled and installed the Mbed TLS library and example programs on your system.
