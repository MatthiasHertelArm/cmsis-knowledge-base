---
id: "mbedtls-alternative-cryptography-engines-i-guidelines"
type: "concept"
domain: "security"
title: "Alternative cryptography engines implementation: Guidelines"
summary: "There are few basic rules for supporting full module alternative implementation: 1. Enable the relevant ALT in the configuration file. 1. Define the module context in <module name>alt.h file. 1. Implement the module API in <module name>alt.c file. 1."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/hw_acc_guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/hw_acc_guidelines.md#guidelines"
license: "Apache-2.0"
mode: "V"
---

There are few basic rules for supporting full module alternative implementation:  
1. Enable the relevant `*_ALT` in the configuration file.  
1. Define the module context in `<module name>_alt.h` file.  
1. Implement the module API in `<module name>_alt.c` file.  
1. If the hardware doesn't support specific functionality, such as key size, then the developer must decide whether to implement a software fallback or return the error `MBEDTLS_ERR_PLATFORM_FEATURE_UNSUPPORTED`.

- For "function alternative implementation" method, implement the alternative function in any file that is being compiled as part of the library.  
- For hardware entropy implementation, implement `mbedtls_hardware_poll()` in any file that is being compiled as part of the library.

**Note:** In the case of unsupported features, we recommend you return the error `MBEDTLS_ERR_PLATFORM_FEATURE_UNSUPPORTED` instead of falling back to software implementation because:

-  Adding software fallback for features not supported by your hardware accelerator doesn't reduce code size, so your users miss out on this advantage of using a hardware accelerator.
- Copying the software implementation from Mbed TLS will require updating your ALT implementation every time Mbed TLS updates in order to get bug fixes and other enhancements.
