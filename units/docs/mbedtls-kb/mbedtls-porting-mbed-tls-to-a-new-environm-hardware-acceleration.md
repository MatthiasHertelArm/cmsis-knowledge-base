---
id: "mbedtls-porting-mbed-tls-to-a-new-environm-hardware-acceleration"
type: "concept"
domain: "security"
title: "Porting Mbed TLS to a new environment or OS: Hardware Acceleration"
summary: "You can substitute alternative implementations of cryptographic primitives in most modules that implement them to take advantage of the hardware acceleration that may be present."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md#hardware-acceleration"
license: "Apache-2.0"
mode: "V"
---

You can substitute alternative implementations of cryptographic primitives in most modules that implement them to take advantage of the hardware acceleration that may be present. This can be achieved by defining the appropriate `MBEDTLS_*_ALT` preprocessor symbol for each module that needs to be replaced. For example `MBEDTLS_AES_ALT` may be defined to replace the whole AES API with a hardware accelerated AES driver, and `MBEDTLS_AES_ENCRYPT_ALT` may be defined for replacing only the AES block encrypt functionality. For more information, see the [hardware accelerator guidelines](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../development/hw_acc_guidelines.md).
