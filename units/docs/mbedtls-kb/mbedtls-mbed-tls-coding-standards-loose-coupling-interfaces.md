---
id: "mbedtls-mbed-tls-coding-standards-loose-coupling-interfaces"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Loose coupling interfaces"
summary: "Each module should keep loose coupling with external modules and functions in mind. Use flexible function pointers over hard functions calls in cases where you want to replace part of the code with a local version."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#loose-coupling-interfaces"
license: "Apache-2.0"
mode: "V"
---

Each module should keep loose coupling with external modules and functions in mind. Use flexible function pointers over hard functions calls in cases where you want to replace part of the code with a local version.
