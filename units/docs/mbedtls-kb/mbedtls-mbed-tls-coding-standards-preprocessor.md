---
id: "mbedtls-mbed-tls-coding-standards-preprocessor"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Preprocessor"
summary: "To minimize the code size and external dependencies, the availability of modules and module functionality is controlled by preprocessor directives located in mbedtls/mbedtls_config.h. Each module should have at least its own module define for enabling or disabling the module altogether."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#preprocessor"
license: "Apache-2.0"
mode: "V"
---

### Minimize code based on preprocessor directives

To minimize the code size and external dependencies, the availability of modules and module functionality is controlled by preprocessor directives located in `mbedtls/mbedtls_config.h`. Each module should have at least its own module define for enabling or disabling the module altogether. Other files using the module header should only include the header file if the module is actually available.

Since often systems that use Mbed TLS do not have a file system, functions specifically using the file system should be contained in `MBEDTLS_FS_IO` directives.

### Conditional compilation hygiene

The span of a conditional compilation directive should generally be a sequence of C instructions or declarations.

If necessary, the span can be an expression or a sequence of expressions. For example, this is acceptable:
```c
static char self_test_key = {
    0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
#if !defined(SUPPORT_128_BIT_KEYS)
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17,
    0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
#endif
};
```

This is acceptable, but deprecated:
```c
    if (
#if defined(MBEDTLS_USE_PSA_CRYPTO)
        psa_condition()
#else
        legacy_condition()
#endif
      )
        do_stuff();
```
Such code is generally more readable with an intermediate variable, thus the following style is preferred:
```c
#if defined(MBEDTLS_USE_PSA_CRYPTO)
    const int want_stuff = psa_condition();
#else
    const int want_stuff = legacy_condition();
#endif
    if (want_stuff)
        do_stuff();
```

Do not put partial instructions in a conditionally compiled span. For example, do not write the code above like this:
```c
#if defined(MBEDTLS_USE_PSA_CRYPTO)     // NO!
    if (psa_condition())                // NO!
#else                                   // NO!
    if (legacy_condition())             // NO!
#endif                                  // NO!
        do_stuff();                     // NO!
```
Having two instances of `if` in the source code, but only one actually compiled, is confusing both for humans and for tools such as indenters and linters.

Exception: the following idiom, with a chain of if-else-if statements, is accepted.
```c
#if defined(MBEDTLS_FOO)
    if (is_a_foo(type))
        process_foo(type, data);
    else
#endif /* MBEDTLS_FOO */
#if defined(MBEDTLS_BAR)
    if (is_a_bar(type))
        process_bar(type, data);
    else
#endif /* MBEDTLS_BAR */
    {
        return ERROR_NOT_SUPPORTED;
    }
```

Never have unbalanced braces in a conditionally compiled span. Exception: public headers can, and must, have `extern "C" {` and `}` guarded by `#ifdef __cplusplus`.

### Minimize use of macros

Only use macros if they improve readability or maintainability, preferably both. If macros seem necessary for maintainability but hinder readability, consider generating code from a Python script instead.

If possible, use the C core language rather than macros. For example, if an expression is used often, a `static inline` function is better because it provides type checks, allows the compiler to keep the function call when optimizing for size, and avoids problems with arguments evaluated more than once. However, if the expression needs to be a compile-time constant when its parameters are, this is a good reason to use a macro.

### Macro definition hygiene

When the code contains a macro call `MBEDTLS_FOO(x, y)`, it should behave as much as possible as if `MBEDTLS_FOO` was a function. Deviate from this only to the extent necessary to make the macro practical.

If the arguments of a macro are C expressions (they usually are), put parentheses around the argument in the expansion. For example:
```c
#define FOO_SIZE(bits) (((bits) + 7) / 8 + 4)
```
The expansion contains `((bits) + 7)`, not `bits + 7`, so that a call like `FOO_SIZE(x << 3)` is parsed correctly. As an exception, it's ok to omit parentheses if the argument is directly passed to a function argument (or comma operator): `#define A(x) f(x, 0)` is acceptable.

If the expansion of a macro is a C expression, put parentheses around the expansion. Continuing the example above, this is so that a call like `FOO_SIZE(x) * 2` is parsed correctly. As an exception, it's ok to omit parentheses if the expansion is a function call or other highest-precedence operator: `#define A(x) f(x, 0)` is acceptable.

If a macro expands to a statement, wrap it in `do { ... } while (0)` so that it can be used in contexts that expect a single statement. For example:
```c
#define MBEDTLS_MPI_CHK(f)       \
    do {                          \
        if ((ret = (f)) != 0)    \
            goto cleanup;        \
    } while (0)`
```
The expansion is not just `if ((ret = (f)) != 0) goto cleanup` because that would not work in a context like `if (condition) MBEDTLS_MPI_CHK(f()); else ++x;` (the `else` would get attached to the wrong `if`).

Follow the expression paradigm or the statement paradigm if possible. Other paradigms are permitted if necessary, for example a macro that expands to an initializer such as
```c
#define MBEDTLS_FOO_INIT {0, {0, 0}}
```
The expansion of a macro must not contain unbalanced parentheses, brackets or braces.

In macro expansions, do not make assumptions about the calling context, for example do not assume that a particular variable is defined. Exception: variable names with a very strong convention in the code base, like the `ret` example above which is systematically used for status codes in the classic mbedtls API. If the macro needs an intermediate variable, give it a long name that won't clash with anything else, but strongly consider using a function instead.
