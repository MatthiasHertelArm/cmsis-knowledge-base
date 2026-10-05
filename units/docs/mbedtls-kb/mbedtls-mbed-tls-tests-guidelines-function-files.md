---
id: "mbedtls-mbed-tls-tests-guidelines-function-files"
type: "concept"
domain: "security"
title: "Mbed TLS tests guidelines: `.function` files"
summary: "Code file that contains the actual test functions. The file contains a series of code sequences that the following delimit:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/test_suites.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/test_suites.md#function-files"
license: "Apache-2.0"
mode: "V"
---

Code file that contains the actual test functions. The file contains a series of code sequences that the following delimit:

* `BEGIN_HEADER` / `END_HEADER` - Code that will be added to the header of the generated `.c` file. It could contain include directives, global variables, type definitions and static functions.
* `BEGIN_DEPENDENCIES` / `END_DEPENDENCIES` - A list of configuration options that this test suite depends on. The test suite will only be generated if all of these options are enabled in `mbedtls_config.h`.
* `BEGIN_SUITE_HELPERS` / `END_SUITE_HELPERS` - Similar to `XXXX_HEADER` sequence, except that this code will be added after the header sequence, in the generated `.c` file.
* `BEGIN_CASE` / `END_CASE` - The test case functions in the test suite. Between each of these pairs, you should write *exactly* one function that is used to create the dispatch code. The function must return `void` and may only take supported parameter types. Comments are allowed before and inside the function's prototype.

An optional addition `depends_on:` has same usage as in the `.data` files. The section with this annotation will only be generated if all of the specified options are enabled in `mbedtls_config.h`. It can be added to the following delimiters:

* `BEGIN_DEPENDENCIES` - When added in this delimiter section, the whole test suite will be generated only if all the configuration options are defined in `mbedtls_config.h`.

    For example:
    ```c
    /* BEGIN_DEPENDENCIES
     * depends_on:MBEDTLS_CIPHER_C
     * END_DEPENDENCIES
     */
    ```

* `BEGIN_CASE` - When added to this delimiter, this specific test case will be generated at compile time only if the configuration option is defined in `mbedtls_config.h`.

    For example:
    ```c
    /* BEGIN_CASE depends_on:MBEDTLS_AES_C */
    ```
