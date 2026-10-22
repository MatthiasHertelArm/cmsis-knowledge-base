---
id: "mbedtls-mbed-tls-tests-guidelines-introducing-new-tests"
type: "concept"
domain: "security"
title: "Mbed TLS tests guidelines: Introducing new tests"
summary: "When you want to introduce a new test, if the test function:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/test_suites.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/test_suites.md#introducing-new-tests"
license: "Apache-2.0"
mode: "V"
---

When you want to introduce a new test, if the test function:

* Already exists and it only missing the test data, then update the .data file with the additional test data. If required, you can add a resource file to the `data_files/` subfolder.
* Doesn't exist, you can implement a new test function in the relevant `.function` file following the guidelines mentioned above and add test cases to the .data file to test your new feature.

You should write your test code in the same platform abstraction as the library, and should not assume the existence of platform-specific functions.

Note that historically, most of SSL was tested differently, with sample programs under the `programs/ssl/` folder. These are executed when you run the scripts `tests/ssl-opt.sh` and `tests/compat.sh`. However, for new code, we prefer to have unit tests as well.
