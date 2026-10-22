---
id: "mbedtls-how-to-generate-a-self-signed-cert"
type: "concept"
domain: "security"
title: "How to generate a self-signed certificate"
summary: "This tutorial outlines how to generate your own keys and certificates for your system."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/generate-a-self-signed-certificate.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/generate-a-self-signed-certificate.md"
license: "Apache-2.0"
mode: "V"
---

This tutorial outlines how to generate your own keys and certificates for your system.

Mbed TLS includes the core and applications for generating and using certificates. Mbed TLS 4 does not provide a command-line program for generating keys, so this tutorial uses OpenSSL to create the key file.

This article assumes you have compiled and installed the Mbed TLS library on your system.
