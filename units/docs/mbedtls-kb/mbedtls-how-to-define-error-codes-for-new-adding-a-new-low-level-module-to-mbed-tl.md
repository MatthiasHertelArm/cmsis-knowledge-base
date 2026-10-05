---
id: "mbedtls-how-to-define-error-codes-for-new-adding-a-new-low-level-module-to-mbed-tl"
type: "concept"
domain: "security"
title: "How to define error codes for new modules: Adding a new low-level module to Mbed TLS"
summary: "Find some space within the error.h file to fit the number of the error codes you need."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/how-are-error-codes-defined.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/how-are-error-codes-defined.md#adding-a-new-low-level-module-to-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Find some space within the `error.h` file to fit the number of the error codes you need.

Add the name to the list of low-level modules in the `error.h` file and in `scripts/generate_errors.pl`.
