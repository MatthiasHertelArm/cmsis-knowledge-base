---
id: "mbedtls-alternative-cryptography-engines-i-full-module-replacement-example-aes"
type: "concept"
domain: "security"
title: "Alternative cryptography engines implementation: Full module replacement example: AES"
summary: "Add a file (conventionally aes_alt.c) to your build:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/hw_acc_guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/hw_acc_guidelines.md#full-module-replacement-example-aes"
license: "Apache-2.0"
mode: "V"
---

In `mbedtls_config.h`:

- **Enable** the definition of `MBEDTLS_AES_ALT`.

Create a file `aes_alt.h`:

- **Define** `mbedtls_aes_context` that will fit the platform's needs.
- **Define** the platform specific functions that will be used by the alternative implementation.

Add a file (conventionally `aes_alt.c`) to your build:

-  **Write** an alternative implementation of the AES interface, as defined in `aes.h`, which will access the platform's hardware accelerated engine.
