---
id: "mbedtls-the-external-dependencies-mbed-tls-external-function-dependencies"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: External function dependencies"
summary: "Mbed TLS is as loosely coupled as possible and does not rely on any external libraries for its code. It does use a number of standard libc function calls."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#external-function-dependencies"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS is as loosely coupled as possible and does not rely on any external libraries for its code. It does use a number of standard `libc` function calls. This page describes which external calls are present and how you can remove them if no support for that function is available; it focuses on the core library only (excluding the example programs and test suites, but including the self test functions as they are part of the library).

Configuration flags control some of the dependencies. Please see [How do I configure mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/../compiling-and-building/how-do-i-configure-mbedtls.md) and [How do I port Mbed TLS to a new environment or OS](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/../how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md) for a full description of how to set the configuration flags to port Mbed TLS to a new environment.
