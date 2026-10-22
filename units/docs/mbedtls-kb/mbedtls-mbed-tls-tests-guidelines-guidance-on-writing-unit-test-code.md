---
id: "mbedtls-mbed-tls-tests-guidelines-guidance-on-writing-unit-test-code"
type: "concept"
domain: "security"
title: "Mbed TLS tests guidelines: Guidance on writing unit test code"
summary: "Many helper macros and functions are available in the tests directory of the framework repository (location since Mbed TLS 3.6.0, also applying to TF-PSA-Crypto). They are declared in <test/xxx.h> header files."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/test_suites.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/test_suites.md#guidance-on-writing-unit-test-code"
license: "Apache-2.0"
mode: "V"
---

Many helper macros and functions are available in [the `tests` directory of the framework repository](https://github.com/Mbed-TLS/mbedtls-framework/blob/main/tests) (location since Mbed TLS 3.6.0, also applying to TF-PSA-Crypto). They are declared in [`<test/xxx.h>` header files](https://github.com/Mbed-TLS/mbedtls-framework/blob/main/tests/include/test).

### Testing expected results

Calls to library functions in test code should always check the function's return status. Fail the test if anything is unexpected.

The header file [`<test/macros.h>`](https://github.com/Mbed-TLS/mbedtls-framework/blob/development/tests/include/test/macros.h) declares several useful macros, including:

* `TEST_EQUAL(x, y)` when two integer values are expected to be equal, for example `TEST_EQUAL(mbedtls_library_function(), 0)` when expecting a success or `TEST_EQUAL(mbedtls_library_function(), MBEDTLS_ERR_xxx)` when expecting an error.
* `TEST_LE_U(x, y)` to test that the unsigned integers `x` and `y` satisfy `x <= y`, and `TEST_LE_S(x, y)` when `x` and `y` are signed integers.
* `TEST_MEMORY_COMPARE(buffer1, size1, buffer2, size2)` to compare the actual output from a function with the expected output.
* `PSA_ASSERT(psa_function_call())` when calling a function that returns a `psa_status_t` and is expected to return `PSA_SUCCESS`.
* `TEST_FAIL("explanation of why this shouldn't happen")` for code that should be unreachable.
* `TEST_ASSERT(condition)` for a condition that doesn't fit any of the special cases.

Older test code only had `TEST_ASSERT`. But in new test code, please use higher-level macros where applicable, as they have additional conveniences.

These macros can be used in the `.function` file, but also in auxiliary functions. If the assertion fails, in addition to marking the test case as failed, the macros cause `goto exit` to happen, thus the function must have an `exit` label. Often you'll need to write some code after the `exit:` label, but as a convenience, if you have no cleanup code, the test framework will add `exit:;` to test entry points that don't have an `exit:` label.

### Output on failure

If a test fails, the location of the error is displayed, as well as the failed assertion.

If the test code runs into more than one failed assertion, only information about the first one is displayed. This is usually the right thing because as soon as one assertion has failed, the data is probably in a bad state anyway.

When a test assertion is in a loop, or in an auxiliary function that is called multiple times, the location is not enough to know exactly where the failure happened. You can call `mbedtls_test_set_step()` to declare a “step number” which is displayed together with the location on failure. For example:

```
for (int i = 0; i < max; i++) {
    mbedtls_test_set_step(i);
    one_iteration(i);
    TEST_ASSERT(intermediate_check());
}

mbedtls_test_set_step(max);
final_checks(left_output);
mbedtls_test_set_step(max + 1);
final_checks(right_output);
```

### Buffer allocation

When a function expects an input or an output to have a certain size, you should pass it an allocated buffer with exactly the expected size. The continuous integration system runs tests in many configurations with Asan or Valgrind, and these will cause test failures if there is a buffer overflow or underflow.

For output buffers, it's usually desirable to also check that the function works if it's given a buffer that's larger than necessary, and that it returns the expected error if given a buffer that's too small.

Here is an example of a test function that checks that a library function has the desired output for a given input.
```c
/* BEGIN_CASE */
void test_function(data_t *input, data_t *expected_output)
{
// must be set to NULL both for TEST_CALLOC and so that mbedtls_free(actual_output) is safe
    unsigned char *actual_output = NULL;
    size_t output_size;
    size_t output_length;

    /* Good case: exact-size output buffer */
    output_size = expected_output->len;
    TEST_CALLOC(actual_output, output_size);
// set output_length to a bad value to ensure mbedtls_library_function updates it
    output_length = 0xdeadbeef;
    TEST_EQUAL(mbedtls_library_function(input->x, input->len,
                                        actual_output, output_size,
                                        &output_length), 0);
// Check both the output length and the buffer contents
    TEST_MEMORY_COMPARE(expected_output->x, expected_output->len,
                        actual_output, output_length);
// Free the output buffer to prepare it for the next subtest
    mbedtls_free(actual_output);
    actual_output = NULL;

    /* Good case: larger output buffer */
    output_size = expected_output->len + 1;
    TEST_CALLOC(actual_output, output_size);
    output_length = 0xdeadbeef;
    TEST_EQUAL(mbedtls_library_function(input->x, input->len,
                                        actual_output, output_size,
                                        &output_length), 0);
    TEST_MEMORY_COMPARE(expected_output->x, expected_output->len,
                        actual_output, output_length);
    mbedtls_free(actual_output);
    actual_output = NULL;

    /* Bad case: output buffer too small */
    output_size = expected_output->len - 1;
    TEST_CALLOC(actual_output, output_size);
    TEST_EQUAL(mbedtls_library_function(input->x, input->len,
                                        actual_output, output_size,
                                        &output_length),
               MBEDTLS_ERR_XXX_BUFFER_TOO_SMALL);
    mbedtls_free(actual_output);
    actual_output = NULL;

exit:
    mbedtls_free(actual_output);
}
/* END_CASE */
```

### PSA initialization and deinitialization

In a test case that always uses PSA crypto, call `PSA_INIT()` at the beginning and `PSA_DONE()` at the end (in the cleanup section). Destroy all keys used by the test before calling `PSA_DONE()`: if any key is still live at that point, it is considered a resource leak in the test.

In a test case that uses PSA crypto only when building with `MBEDTLS_USE_PSA_CRYPTO`, call `USE_PSA_INIT()` at the beginning and `USE_PSA_DONE()` at the end.

See [`<test/psa_crypto_helpers.h>`](https://github.com/Mbed-TLS/mbedtls-framework/blob/development/tests/include/test/psa_crypto_helpers.h) for more complex cases.

### Constant-flow testing

We run some tests with [MemorySanitizer (MSan)](https://github.com/google/sanitizers/wiki/memorysanitizer) and [Valgrind](https://valgrind.org/docs/manual/mc-manual.html) configured to detect secret-dependent control flow: branches or memory addresses computed from secret data. These tests detect library code that could leak secret data through timing side channels to local attackers via shared hardware components such as a memory cache or a branch predictor. We refer to such tests as “constant-time” or more accurately “constant-flow” testing.

Constant-flow testing was added relatively recently in the history of the project, and many functions that should be constant-flow are not tested. However, constant-flow testing is preferred when writing new code that claims to be constant-flow, and especially when fixing a timing side channel.

In unit tests, use the following macros, from [`<test/constant_flow.h>`](https://github.com/Mbed-TLS/mbedtls-framework/blob/main/tests/include/test/constant_flow.h):

* `TEST_CF_SECRET(buffer, size)`: marks the given buffer as secret. Call this on keys, plaintext and other confidential data before passing it to library functions.
* `TEST_CF_PUBLIC(buffer, size)`: marks the given buffer as public. Call this on outputs before testing their content.

Note that you need to call `TEST_CF_PUBLIC` before `TEST_MEMORY_COMPARE`. However, it is not needed with scalar comparison assertions (`TEST_EQUAL`, etc.), which make a public copy of its argument before comparing them.
