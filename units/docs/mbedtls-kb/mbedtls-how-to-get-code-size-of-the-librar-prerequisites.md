---
id: "mbedtls-how-to-get-code-size-of-the-librar-prerequisites"
type: "concept"
domain: "security"
title: "How to get code size of the library: Prerequisites"
summary: "Note: The arm-none-eabi toolchain may give different results than other toolchains, such as ARMCC or IAR."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/code-size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/code-size.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

* `arm-none-eabi` toolchain installed and found in the `PATH` environment variable.
* `make`.
* POSIX shell.
* Updated `include/mbedtls/mbedtls_config.h` with the required configuration. See [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md) for more information.

Note: The `arm-none-eabi` toolchain may give different results than other toolchains, such as `ARMCC` or `IAR.
