---
id: "mbedtls-mbed-tls-coding-standards-clear-and-free-what-you-made"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Clear and free what you made"
summary: "The module that allocated a piece of heap memory is also responsible for releasing it later on unless explicitly documented in the function definition in the header file."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#clear-and-free-what-you-made"
license: "Apache-2.0"
mode: "V"
---

The module that allocated a piece of heap memory is also responsible for releasing it later on unless explicitly documented in the function definition in the header file.
