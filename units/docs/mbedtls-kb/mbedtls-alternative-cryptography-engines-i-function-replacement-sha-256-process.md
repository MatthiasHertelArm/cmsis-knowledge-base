---
id: "mbedtls-alternative-cryptography-engines-i-function-replacement-sha-256-process"
type: "concept"
domain: "security"
title: "Alternative cryptography engines implementation: Function replacement: SHA-256 process"
summary: "Add a file (conventionally sha256_alt.c) to your build:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/hw_acc_guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/hw_acc_guidelines.md#function-replacement-sha-256-process"
license: "Apache-2.0"
mode: "V"
---

In `mbedtls_config.h`:

- **Enable** the definition of `MBEDTLS_SHA256_PROCESS_ALT`.

Add a file (conventionally `sha256_alt.c`) to your build:

- **Implement** `mbedtls_internal_sha256_process`.
- Mbed TLS 2.x only: Implement `mbedtls_sha256_process` if you need it in legacy applications.
