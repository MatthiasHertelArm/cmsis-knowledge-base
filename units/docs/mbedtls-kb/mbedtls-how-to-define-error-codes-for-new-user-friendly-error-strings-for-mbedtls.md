---
id: "mbedtls-how-to-define-error-codes-for-new-user-friendly-error-strings-for-mbedtls"
type: "concept"
domain: "security"
title: "How to define error codes for new modules: User-friendly error strings for `mbedtls_strerror()`"
summary: "Add the respective error codes to your module's header file with a description, like this:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/how-are-error-codes-defined.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/how-are-error-codes-defined.md#user-friendly-error-strings-for-mbedtls-strerror"
license: "Apache-2.0"
mode: "V"
---

Add the respective error codes to your module's header file with a description, like this:

```
#define MBEDTLS_ERR_AES_INVALID_KEY_LENGTH-0x0020  /**< Invalid key length. */
```

The doxygen description will be used as the user-friendly `mbedtls_strerror()` error message.

Regenerate the `error.c` file.

Now regenerate `library/error.c` with:

`scripts/generate_errors.pl`
