---
id: "mbedtls-mbed-tls-coding-standards-code-structure"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Code structure"
summary: "However, don't use variable-length arrays (VLAs) as they are not supported by all compilers/systems, and can cause problems for static analysis."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#code-structure"
license: "Apache-2.0"
mode: "V"
---

### ISO C99

The code uses the C99 ISO standard.

However, don't use variable-length arrays (VLAs) as they are not supported by all compilers/systems, and can cause problems for static analysis.

In addition, avoid using `const` values to size arrays or as part of rvalues for other constants, as this is not supported by (at least) MSVC.

### Proper argument and variable typing

Type function arguments and variables properly. Specifically, the `int` and `size` fields hold their maximum length in a platform-independent way. For buffer length, this almost always means using `size_t`.

For values that can't be negative, use unsigned variables. Keep the type in mind when building loops with unsigned variables.

When it's unavoidable that a `size_t` must be passed as an `int` function parameter, it's necessary to add a cast to avoid warnings on some compilers.

### Variable initialization

Try to give variables the smallest scope possible. For example, `for` loop counters should be declared in the loop's initialization statement. Variables that are only used in one block should be declared in that block.

Where possible, declare a variable at the point where it receives its first "real" value, rather than at the top of the block.

This is sometimes impossible, in particular when a variable is used on some code paths, including the cleanup at the end of a function, but unused in other paths.
If so, you should initialize the variable.
Avoid relying on compilers to detect uninitialized variables, because in complex cases where the compiler can't decide whether there is an initialization on all code paths, many compilers don't warn.

Try to initialize the variable to a safe default. Here are some guidelines for safe initialization:

* Initialize pointers to `NULL`.
* Initialize `int` variables containing an MBEDTLS status code to `MBEDTLS_ERR_ERROR_CORRUPTION_DETECTED`. (Not `0` because that would report success if the code is missing a case.)
* Initialize `psa_status_t` variables containing a PSA status code to `PSA_ERROR_CORRUPTION_DETECTED`. (Not `PSA_SUCCESS` because that would report success if the code is missing a case.)
* For `mbedtls_xxx` structures with an `mbedtls_xxx_init` initialization function, call the initialization function immediately after declaring the variable. Note that for some types, calling `mbedltls_xxx_init` is necessary even for zero-initialized memory.
* For `psa_xxx_t` structures, use the `PSA_XXX_INIT` initializer (`{0}` causes warnings with some compilers). In zero-initialized memory (typically returned by `mbedtls_calloc`), no further initialization is necessary.
* For byte arrays:
    * `{0}` is ok as an initializer if there's no reason to prefer something else.
    * Something like `memset(buf, '!', sizeof(buf))` may be better if there's a risk that all-bits-zero will be treated as valid, or if it helps to have a different bit pattern to stand out while debugging.
    * It's ok to leave the array uninitialized if it's evidently going to be overwritten. In particular, it's ok to leave an array uninitialized when different code paths will use a different length of data in the array, and the code is simple enough that we don't feel the need to initialize the whole array.

Note that these are only guidelines: it's ok to do things differently if those guidelines don't make sense in a specific context. For example, it's ok to initialize a status variable to `0` or `PSA_SUCCESS` if that variable is used for checks that are only present on some code paths, but only consider this if a `CORRUPTION_DETECTED` initialization requires extra complexity.

There is a lot of older code that doesn't follow these guidelines because it was written for C89, which required initializations to come before statements. New code should take advantage of the ability to initialize variables in the middle of a block since C99.

### `Goto`

Use of `goto` is allowed in functions that have to do cleaning up before returning from the function even when an error has occurred. It can also be used to exit nested loops. In other cases the use of `goto` should be avoided.

Some compilers (e.g. IAR) issue warnings when a `goto` jumps over a variable declaration. In these cases, either hoist the variable to the top of the function, use a local block, or extract the code with this variable into a smaller `static` function. If hoisting a pointer, it must be initialized, to avoid potential code-paths where it may be used uninitialized.

### Exit early and prevent nesting

Structure functions to exit or `goto` the exit code as early as possible. This prevents nesting of code blocks and improves code readability.

Most functions that need cleanup have a single cleanup block at the end. The label for this block can be `cleanup:` or `exit:` (or `error:` if the block is skipped on success); follow the established convention when extending an existing module. Code that uses bignum must use `cleanup:` for the sake of `MBEDTLS_MPI_CHK`.

### External function dependencies

Mbed TLS code should minimize use of external functions. Standard `libc` functions are allowed, but should be documented in the [KB article on external dependencies](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/what-external-dependencies-does-mbedtls-rely-on.md).
