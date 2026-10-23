---
id: "mbedtls-mbed-tls-tests-guidelines"
type: "concept"
domain: "security"
title: "Mbed TLS tests guidelines"
summary: "Mbed TLS includes an elaborate amount of test suites in the tests/ folder that initially requires Perl to generate the tests executable files. These files are generated from a function file and a data file, located in the suites/ subfolder."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/test_suites.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/test_suites.md"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS includes an elaborate amount of test suites in the `tests/` folder that initially requires Perl to generate the tests executable files. These files are generated from a function file and a data file, located in the `suites/` subfolder. The function file contains the test cases code, while the data file contains the test cases data, specified as parameters that will be passed to the test case code. In addition, some tests use data resource files (such as certificates and keys). They are in the `data_files/` subfolder. You should introduce new tests when you add a new feature to the library, or if you want to improve the test coverage.

Following are explanations on the `.function` and `.data` files that should assist you with adding your own test suite code.

Note that the test files are independent, and their order should not be dependent on each other.
