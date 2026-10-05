---
id: "mbedtls-mbed-tls-tests-guidelines-data-files"
type: "concept"
domain: "security"
title: "Mbed TLS tests guidelines: `.data` files"
summary: "A test data file consists of a sequence of paragraphs separated by a single empty line. Each paragraph is referred as test case data. Line breaks may be in Unix (LF) or Windows (CRLF) format."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/test_suites.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/test_suites.md#data-files"
license: "Apache-2.0"
mode: "V"
---

A test data file consists of a sequence of paragraphs separated by a single empty line. Each paragraph is referred as test case data. Line breaks may be in Unix (LF) or Windows (CRLF) format. Lines starting with the character '#' are ignored (the parser behaves as if they were not present). The first line must not be an empty line.

Each paragraph describes one test case and must consist of:

1. One line, which is the test case name.
1. An optional line starting with the 11-character prefix `depends_on:`. This line consists of a list of compile-time options separated by the character ':', with no whitespace. The test case is executed only if all of these configuration options are enabled in `mbedtls_config.h`. Note that this filtering is done at run time.
1. A line containing the test case function to execute and its parameters. This last line contains a test function name and a list of parameters separated by the character ':'. The parameter must be valid for the function type:
    * `int` or other integral type: an integer-valued C expression, evaluated in a separate function in the same C source file as the test code. So this expression has access to macros, types and even global variables defined in the header of the `.function` file, but not to local variables of the test function.
    * `[const] char *`: a string between double quotes. A backslash escapes the next character (needed for `\":`).
    * `[const] data_t *`: a byte string written in hexadecimal, between double quotes.

For example:

```
Parse RSA Key #8 (AES-256 Encrypted)
depends_on:MBEDTLS_MD5_C:MBEDTLS_AES_C:MBEDTLS_PEM_PARSE_C:MBEDTLS_CIPHER_MODE_CBC
pk_parse_keyfile_rsa:"data_files/keyfile.aes256":"testkey":0
```
