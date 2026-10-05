---
id: "mbedtls-mbed-tls-coding-standards-clear-security-relevant-memory-after-use"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Clear security-relevant memory after use"
summary: "Memory that contains security-relevant information should be set to zero after use, and before being released to be reused. Use the function mbedtls_platform_zeroize() to prevent unwanted compiler optimization."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#clear-security-relevant-memory-after-use"
license: "Apache-2.0"
mode: "V"
---

Memory that contains security-relevant information should be set to zero after use, and before being released to be reused. Use the function `mbedtls_platform_zeroize()` to prevent unwanted compiler optimization.
