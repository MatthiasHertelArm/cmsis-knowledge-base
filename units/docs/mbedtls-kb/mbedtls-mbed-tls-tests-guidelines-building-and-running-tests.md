---
id: "mbedtls-mbed-tls-tests-guidelines-building-and-running-tests"
type: "concept"
domain: "security"
title: "Mbed TLS tests guidelines: Building and running tests"
summary: "The test suite .c files are auto generated with the generate_test_code.py script. You could either use this script directly, or run make in the tests/ folder, as the Makefile utilizes this script."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/test_suites.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/test_suites.md#building-and-running-tests"
license: "Apache-2.0"
mode: "V"
---

### Building your test suites

The test suite `.c` files are auto generated with the `generate_test_code.py` script. You could either use this script directly, or run `make` in the `tests/` folder, as the [`Makefile`](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/Makefile) utilizes this script. Once the `.c` files are generated, you could build the test suite executables running `make` again. Running `make` from the Mbed TLS root folder will also generate the test suite source code, and build the test suite executables.

### Running unit tests

You can run a single test suite individually. To run all the test suites:

* Run `make test` from the top-level directory of the build tree.
* When building with Make, this runs `tests/scripts/run-test-suites.pl`, which you can call directly.
* When building with CMake, this uses `ctest`.

To skip a few test suites:

* With Make, set the environment variable `SKIP_TEST_SUITES` to a comma-separated list of short names, e.g.
    ```
    SKIP_TEST_SUITES=constant_time_hmac,lmots,lms,gcm,psa_crypto.pbkdf2,ssl_decrypt make test
    ```
* With CMake, set the CMake parameter `SKIP_TEST_SUITES` to a comma or semicolon-separated list of short names, e.g.
    ```
    cmake -B build-debug -DCMAKE_BUILD_TYPE=Debug -DSKIP_TEST_SUITES=constant_time_hmac,lmots,lms,gcm,psa_crypto.pbkdf2,ssl_decrypt
    ```
    You have to re-run `cmake` if you want to change the set of skipped suites.

### Running only one test case

If you just want to see information about failing test cases:

```
tests/test_suite_foo |& grep -Ev '(PASS|SKIP|----)'
```

But sometimes you want to set a breakpoint in a debugger and not have it trigger on “boring” test cases. At the time of writing, there is no way to skip individual test cases. Various kludges are possible, such as:

* Edit the `.data` file to remove or comment out the boring test cases, and rebuild the test suite. Remember not to commit this change!
* Copy the interesting test case to the top of the `.data` file. Remember to update the test case in its “true” location if you modify it, and not to commit the copy.
* Copy the `.datax` file, remove boring test cases from the copy and pass it to the executable.
    ```
    awk -vRS= -vORS='\n\n' '/test case description regex/' <tests/test_suite_foo.datax >my.datax
    tests/test_suite_foo my.datax
    ```
