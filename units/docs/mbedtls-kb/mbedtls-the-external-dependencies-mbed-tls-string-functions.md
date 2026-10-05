---
id: "mbedtls-the-external-dependencies-mbed-tls-string-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: String functions"
summary: "The printf() function is used in all self test functions as mbedtls_printf(), controlled by the MBEDTLS_SELF_TEST configuration flags. In addition, in the MPI module (bignum.c), mbedtls_mpi_write_file() uses mbedtls_printf() to print to stdout if MBEDTLS_FS_IO is defined."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#string-functions"
license: "Apache-2.0"
mode: "V"
---

The `printf()` function is used in all self test functions as `mbedtls_printf()`, controlled by the `MBEDTLS_SELF_TEST` configuration flags. In addition, in the *MPI* module (`bignum.c`), `mbedtls_mpi_write_file()` uses `mbedtls_printf()` to print to `stdout` if `MBEDTLS_FS_IO` is defined. You can disable these dependencies in the `mbedtls_config.h` file. You can also provide your own implementation through the platform layer, see `MBEDTLS_PLATFORM_PRINTF_ALT` for an example. If your platform supports a print function with a different name, you can set it as `MBEDTLS_PLATFORM_PRINTF_MACRO`.

**Functions covered:** `printf()`

The `snprintf()` function is defined as `mbedtls_snprintf()`. It is used in the *X.509* module for the various `mbedtls_x509_xxx_info()` functions and `mbedtls_x509_crt_parse_path()`. It is also used by the *SSL debug* module (`debug.c`) for formatting debug messages, by `error.c` for `mbedtls_strerror()` and by `oid.c` for `mbedtls_oid_get_numeric_string()` (not used in the library). You can provide your own implementation through the platform layer, see `MBEDTLS_PLATFORM_PRINTF_ALT` for an example. If your platform supports a similar function with a different name, you can set it as `MBEDTLS_PLATFORM_SNPRINTF_MACRO`.

**Functions covered:** `snprintf()`

The other string functions are used in actual core scenarios. There are workarounds possible in any of there scenarios.

**Functions covered:** 

- `strcmp()`
- `strlen()`
- `strncmp()`
- `strncpy()`
- `strstr()`
