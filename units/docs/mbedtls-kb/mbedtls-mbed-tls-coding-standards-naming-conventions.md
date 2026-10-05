---
id: "mbedtls-mbed-tls-coding-standards-naming-conventions"
type: "concept"
domain: "security"
title: "Mbed TLS coding standards: Naming conventions"
summary: "All public names (functions, variables, types, enum constants, macros) must start with either MBEDTLS or mbedtls, usually followed by the name of the module they belong to (and submodule if applicable), followed by a descriptive part."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/mbedtls-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/mbedtls-coding-standards.md#naming-conventions"
license: "Apache-2.0"
mode: "V"
---

### Name spacing

All public names (functions, variables, types, `enum` constants, macros) must start with either `MBEDTLS_` or `mbedtls_`, usually followed by the name of the module they belong to (and submodule if applicable), followed by a descriptive part. Macros and `enum` constants are uppercase with underscores; other names are lowercase with underscores:
```c
    mbedtls_x509_crt_parse_file()
    mbedtls_aes_setkey_decrypt()
```

Note that all externally linked functions must have a name starting with `mbedtls_` to avoid link-time conflicts, even if they are not declared in a public header. This also applies to global variables (which should be used very sparingly).

Exception: code implementing the PSA crypto API uses the `PSA_` and `psa_` prefixes. This includes official APIs as well as draft APIs that are on the PSA standards track. API extensions which are meant to remain specific to Mbed TLS, and internal functions, should use the `MBEDTLS_/mbedtls_` prefix, however there are many existing cases of using the `PSA_/psa_` prefix.

Exception: macros may have lowercase names if they behave exactly like normal variables and functions. In particular, function-like macros may have lowercase names only if they expand to an expression that evaluates each argument exactly once. Even in those cases, uppercase names are strongly preferred and new code should not use lowercase macro names for anything other than function replacement (like `#define mbedtls_printf printf`).

### Local names

Static functions can use the same naming scheme as non-static functions (`mbedtls_MODULE_frobnicate()` or `psa_frobnicate()`). This is convenient if they are made non-static later, for example for testing. They can also have shorter names if it's convenient. Keeping the module name (`MODULE_frobnicate()`) as a prefix makes it slightly easier to follow call stacks across modules, but it is not compulsory.

Macros defined only in the `library` directory should follow the same naming scheme as non-static functions (`MBEDTLS_MODULE_FOO` or `PSA_FOO`). They can use shorter names (omitting `MBEDTLS_`, the module name, or both) if it's convenient. However, avoid names without underscores as some embedded platforms define short macro names in their system headers. Exception: macros defined in headers used by alternative implementations or PSA drivers (including headers that they include) must start with `MBEDTLS_` or `PSA_`.

Function parameters and local variables need no name spacing. They should use descriptive names unless they're very short-lived or are used for simple looping or are "standard" names (such as `p` for a pointer to the current position in a buffer).

### Lengths and sizes

By default all lengths and sizes are in bytes (or in number of elements, for arrays). If a name refers to a length or size in bits (as is often the case for key sizes) then the name must explicitly include `bit`, for example `mbedtls_pk_get_bitlen()` returns the size of the key in bits, while `mbedtls_pk_get_len()` returns the size in bytes. In addition, the documentation should always mention explicitly if key sizes are in bits or in bytes.

`size` should refer to the capacity of a buffer, and `length` to the length of the contents. Most of the time these are interchangeable. A typical exception is when the output is written in a buffer, but the exact length is not known by the caller.

### Modules: `bignum_core`, `bignum_mod` and `bignum_mod_raw`

Generic conventions:

- `mbedtls_mpi_uint *` input operands should be named by capital letters starting at the beginning of the alphabet (`A`, `B`, `C`, ...).
- `mbedtls_mpi_uint` operands in turn should be named by lower case letters starting at the beginning of the alphabet (`a`, `b`, `c`)
- For the result `X` or `x` should be used depending on the type.
- `N` is generally used for the modulus.
- `T` is generally used for a temporary work area given to a function.
- An exception from this convention is where the naming of function parameters and local variables follows the literature (e.g. Handbook of Applied Cryptography)

Length parameters:

- For length of `mbedtls_mpi_uint *` buffers we use `limbs`.
- Length parameters are qualified if possible (e.g. `input_length` or `A_limbs`)
