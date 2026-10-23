---
id: "mbedtls-mbed-tls-coding-standards-generic-file-structure"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Generic file structure"
summary: "Mbed TLS coding standards: Generic file structure"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/mbedtls-coding-standards.md#generic-file-structure"
license: "Apache-2.0"
mode: "V"
---

### Header files

Structure header files as follows:

* Brief description of the file.
* Copyright notice and license indication.
* Header file define for `MBEDTLS_ {MODULE_NAME} _H`:
```c
#ifndef MBEDTLS_AES_H
#define MBEDTLS_AES_H
```
* Includes. Always include `<mbedtls/build_info.h>` before anything that might depend on the compile-time configuration.
* Public defines (Generic and error codes) and portability code.
* C++ wrapper for C code:
```c
#ifdef __cplusplus
extern "C" {
#endif
```
* For modules with optional alternative implementations, check for module specific structures:
```c
#if !defined(MBEDTLS_AES_ALT)
```
* Public structures that can have alternative implementations.
* For modules with optional alternative implementations, include the alternative header file:
```c
#else  /* MBEDTLS_AES_ALT */
#include "aes_alt.h"
#endif /* MBEDTLS_AES_ALT */
```
* Public structures that should not have alternative implementations.
* Function declarations.
* C++ end wrapper:
```c
#ifdef __cplusplus
}
#endif
```
* Header file end define:
```c
#endif /* MBEDTLS_AES_H */
```

### Source files

Source files are structured as follows:

* Brief description of the file.
* Copyright notice and license indication.
* Comments on possible standard documents used.
* Preprocessor directive for module:
```c
#if defined(MBEDTLS_AES_C)
```
* Includes. All library source files start by including `"common.h"`.
* If applicable, preprocessor directive for alternative implementation:
```c
#if !defined(MBEDTLS_AES_ALT)
```
* Private local defines and portability code.
* Function definitions.
* If applicable, preprocessor directive for marking the end of an alternative implementation:
```c
#endif /* !MBEDTLS_AES_ALT */
```
* Preprocessor directive for selftest (where applicable):
```c
#if defined(MBEDTLS_SELF_TEST)
```
* Self-test test vectors.
* Self test implementation.
* Preprocessor directive for marking the end of self tests (where applicable):
```c
#endif /* MBEDTLS_SELF_TEST */
```
* Preprocessor directive for marking the end of a module:
```c
#endif /* MBEDTLS_AES_C */
```

<!---mbedtls-coding-standards
,"Coding standards used in the Mbed TLS code, include default code formatting, coding style and file structures.","code formatting, coding style, file structures, code standards","code, formatting, style, coding style",published,"2012-10-18 11:34:00",3,7553,"2017-06-05 11:14:00","Paul Bakker"--->
