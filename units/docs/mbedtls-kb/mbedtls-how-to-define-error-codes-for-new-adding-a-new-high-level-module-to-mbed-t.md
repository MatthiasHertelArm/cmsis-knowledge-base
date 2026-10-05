---
id: "mbedtls-how-to-define-error-codes-for-new-adding-a-new-high-level-module-to-mbed-t"
type: "concept"
domain: "security"
title: "How to define error codes for new modules: Adding a new high-level module to Mbed TLS"
summary: "Find some module space in the error.h file to fit the number of error codes you need. As all the high-level module numbers are filled, we are now also starting to use the same numbers from the top."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/how-are-error-codes-defined.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/how-are-error-codes-defined.md#adding-a-new-high-level-module-to-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Find some module space in the `error.h` file to fit the number of error codes you need. As all the high-level module numbers are filled, we are now also starting to use the same numbers from the top.

Add the name to the list of high-level modules in the `error.h` file and in `scripts/generate_errors.pl`.
