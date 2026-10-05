---
id: "mbedtls-mbed-tls-coding-standards-module-self-test"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: `Module self_test()`"
summary: "Each module should have a self-test function (between a check for MBEDTLS_SELF_TEST). This function should test basic module sanity, but stay away from performing time-consuming tests."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#module-self-test"
license: "Apache-2.0"
mode: "V"
---

Each module should have a self-test function (between a check for **MBEDTLS_SELF_TEST**). This function should test basic module sanity, but stay away from performing time-consuming tests.
