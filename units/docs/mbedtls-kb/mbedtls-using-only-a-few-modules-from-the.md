---
id: "mbedtls-using-only-a-few-modules-from-the"
type: "concept"
domain: "security"
title: "Using only a few modules from the library"
summary: "Mbed TLS is a critical security component. While the developers do their best to avoid bugs and achieve the highest level of security, bugs can happen, including security-critical ones."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/using-loose-modules-without-the-full-library.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/using-loose-modules-without-the-full-library.md"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS is a critical security component. While the developers do their best to avoid bugs and achieve the highest level of security, bugs can happen, including security-critical ones. As a consequence, if you make an application that includes code from Mbed TLS, you should be prepared to upgrade Mbed TLS.

You don't have to use the whole library, however! Mbed TLS is designed so you can include only the modules that you need.
