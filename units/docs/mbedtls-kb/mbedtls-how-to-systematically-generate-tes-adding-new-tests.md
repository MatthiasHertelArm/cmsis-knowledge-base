---
id: "mbedtls-how-to-systematically-generate-tes-adding-new-tests"
type: "concept"
domain: "security"
title: "How to systematically generate test data: Adding new tests"
summary: "There are two options for adding new tests: - Adding classes to an existing script, such as tests/scripts/generate_bignum_tests.py. - Creating a new script. You'll need to update the build system as explained in \"Adding the script to the build system\"."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/add-test-generation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/add-test-generation.md#adding-new-tests"
license: "Apache-2.0"
mode: "V"
---

There are two options for adding new tests:
 - Adding classes to an existing script, such as
[tests/scripts/generate_bignum_tests.py](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/generate_bignum_tests.py).
 - Creating a new script.
 You'll need to update the build system as explained in
 ["Adding the script to the build system"](#adding-the-script-to-the-build-system).
