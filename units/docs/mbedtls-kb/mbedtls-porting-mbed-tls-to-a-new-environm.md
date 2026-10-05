---
id: "mbedtls-porting-mbed-tls-to-a-new-environm"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS"
summary: "Mbed TLS is portable across different architectures and runtime environments, and can execute on a variety of different operating systems or bare-metal ports."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS is portable across different architectures and runtime environments, and can execute on a variety of different operating systems or bare-metal ports. Using C in a generic way ensures the portability of the architecture, and minimizing platform dependencies allows for environment and architecture independence. Doing this reduces the amount of environment - or OS-dependent code, and cleanly isolates platform-specific code from the highly portable core so you can easily replace the platform code.

This page explains how to port Mbed TLS to a new environment.

**Note:** This article is about porting Mbed TLS to a new runtime environment, not to a new hardware platform. It only covers the library, not the Mbed TLS example programs nor the test suites, which have different system requirements.
