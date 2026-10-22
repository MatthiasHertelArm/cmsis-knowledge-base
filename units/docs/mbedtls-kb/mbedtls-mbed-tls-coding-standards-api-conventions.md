---
id: "mbedtls-mbed-tls-coding-standards-api-conventions"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: API conventions"
summary: "This section applies fully to classic mbedtls_xxx() APIs and mostly to the newer psa_xxx() APIs. PSA have their own conventions described in the PSA Crypto API specification which take precedence in case of conflicts."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/mbedtls-coding-standards.md#api-conventions"
license: "Apache-2.0"
mode: "V"
---

This section applies fully to classic `mbedtls_xxx()` APIs and mostly to the newer `psa_xxx()` APIs. PSA have their own [conventions described in the PSA Crypto API specification](https://arm-software.github.io/psa-api/crypto/1.1/overview/conventions.html) which take precedence in case of conflicts.

### Module contexts

If a module uses a context structure for passing around its state, the module should contain an `init()` and `free()` function, with the module or context name prepended to it. The `init()` function must always return `void`. If some initialization must be done that may fail (such as allocating memory), it should be done in a separate function, usually called `setup()`. The `free()` function must free any allocated memory within the context, but not the context itself. It must set to zero any data in the context or substructures:
```c
    mbedtls_cipher_context_t ctx;
    mbedtls_cipher_init(&ctx);
    ret = mbedtls_cipher_setup(&ctx, ...);
    /* Check ret, goto cleanup on error */
    /* Do things, goto cleanup on error */
    cleanup:
    mbedtls_cipher_free(&ctx);
```
The goal of separating the `init()` and `setup()` part is that if you have multiple contexts, you can call all the `init()` functions first and then all contexts are ready to be passed to the `free()` function in case an error happens in one of the `setup()` functions or elsewhere.

### Return type

Most functions should return `int`, more specifically `0` on success (the operation was successfully performed, the object checked was found acceptable, etc.) and a negative error code otherwise. Each module defines its own error codes, see `error.h` for the allocation scheme. Exceptions to this rule:

* Functions that can never fail should either return `void` (such as `mbedtls_cipher_init()`) or directly the information requested (such as `mbedtls_mpi_get_bit()`).
* Functions that look up some information should return either a pointer to this information or `NULL` if it wasn't found.
* PSA functions that can fail return a [`psa_status_t` value](https://arm-software.github.io/psa-api/crypto/1.1/overview/conventions.html#return-status).
* Some functions may multiplex the return value, such as `mbedtls_asn1_write_len()` returns the length written on success or a negative error code. This mimics the behavior of some standard functions such as `write()` and `read()`, except there is no equivalent to `errno`: the return code should be specific enough.
* Some internal functions may return `-1` on errors rather than a specific error code; it is then up to the calling function to pick a more appropriate error code if the error is to be propagated back to the user.
* Functions whose name clearly indicates a boolean (such as, the name contains "has", "is" or "can") should return `0` for false and `1` for true. The name must be clear: for example, `mbdtls_has_foobar_support()` will return `1` if support for foobar is present; by contrast, `mbedtls_check_foobar_support()` will return `0` if support for foobar is present (success) and `-1` or a more specific error code if not. All functions named `check` must follow this rule and return `0` to indicate acceptable/valid/present/etc. Preference should generally be given to `check` names in order to avoid a mixture of `== 0` and `!= 0` tests.
* Functions called `cmp` must return `0` if the two arguments are equal, and if it makes sense, should return `-1` or `1` to indicate which argument is greater.

### Limited use of in-out parameters

Function should avoid in-out parameters for length (multiplexing buffer size on entry with length used/written on exit) since they tend to impair readability. For example:
```c
mbedtls_write_thing(..., unsigned char *buf, size_t *len); // no
mbedtls_write_thing(..., unsigned char *buf, size_t buflen, size_t *outlen); // yes
```

For PSA functions, [input buffers](https://arm-software.github.io/psa-api/crypto/1.1/overview/conventions.html#input-buffer-sizes) have a `size_t xxx_size` parameter after the buffer pointer, and [output buffers](https://arm-software.github.io/psa-api/crypto/1.1/overview/conventions.html#output-buffer-sizes) have a `size_t xxx_size` parameter for the buffer size followed by a `size_t *xxx_length` parameter for the output length. This convention is also preferred in new `mbedtls_xxx` code, but older modules often use different conventions.

You can use in-out parameters for functions that receive a pointer to some buffer, and update it after parsing from or writing to that buffer:
```c
mbedtls_asn1_get_int(unsigned char **p,
                     const unsigned char *end,
                     int *value);
```
In that case, the `end` argument should always point to one past the one of the buffer on entry.

Also, contexts are usually in-out parameters, which is acceptable.

### `Const` correctness

Function declarations should keep `const` correctness in mind when declaring function arguments. Arguments that are pointers and are *not* changed by the functions should be marked as such:
```c
int do_calc_length(const unsigned char *str);
```
