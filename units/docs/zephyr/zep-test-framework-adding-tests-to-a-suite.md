---
id: "zep-test-framework-adding-tests-to-a-suite"
type: "concept"
domain: "test"
title: "Test Framework: Adding tests to a suite"
summary: "There are 5 macros used to add a test to a suite, they are:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

There are 5 macros used to add a test to a suite, they are:

* `ZTEST` `(suite_name, test_name)` - Which can be used to add a test by `test_name` to a
  given suite by `suite_name`.
* `ZTEST_P` `(suite_name, test_name)` - Add a value-parameterized test to a given suite.
  The test body is executed once per registered parameter value. Inside the body, call
  `ztest_get_current_param` or use the `ZTEST_GET_PARAM` typed helper to
  retrieve the current value. The suite fixture (`data` argument) is independent from the
  parameter and is never overwritten. See Value-parameterized tests for the full API.
* `ZTEST_USER` `(suite_name, test_name)` - Which behaves the same as `ZTEST`, only
  that when `CONFIG_USERSPACE` is enabled, then the test will be run in a userspace
  thread.
* `ZTEST_F` `(suite_name, test_name)` - Which behaves the same as `ZTEST`, only
  that the test function will already include a variable named `fixture` with the type
  `<suite_name>_fixture`.
* `ZTEST_USER_F` `(suite_name, test_name)` - Which combines the fixture feature of
  `ZTEST_F` with the userspace threading for the test.


### Test fixtures


Test fixtures can be used to help simplify repeated test setup operations. In many cases, tests in
the same suite will require some initial setup followed by some form of reset between each test.
This is achieved via fixtures in the following way:

```C

#include <zephyr/ztest.h>

struct my_suite_fixture {
     size_t max_size;
     size_t size;
     uint8_t buff[1];
};

static void *my_suite_setup(void)
{
     /* Allocate the fixture with 256 byte buffer */
     struct my_suite_fixture *fixture = malloc(sizeof(struct my_suite_fixture) + 255);

     zassume_not_null(fixture, NULL);
     fixture->max_size = 256;

     return fixture;
}

static void my_suite_before(void *f)
{
     struct my_suite_fixture *fixture = (struct my_suite_fixture *)f;
     memset(fixture->buff, 0, fixture->max_size);
     fixture->size = 0;
}

static void my_suite_teardown(void *f)
{
     free(f);
}

ZTEST_SUITE(my_suite, NULL, my_suite_setup, my_suite_before, NULL, my_suite_teardown);

ZTEST_F(my_suite, test_feature_x)
{
     zassert_equal(0, fixture->size);
     zassert_equal(256, fixture->max_size);
}
```
Using memory allocated by a test fixture in a userspace thread, such as during execution of
`ZTEST_USER` or `ZTEST_USER_F`, requires that memory to be declared userspace
accessible. This is because the fixture memory is owned and initialized by kernel space. The Ztest
framework provides the `ZTEST_DMEM` and `ZTEST_BMEM` macros for use of such
user/kernel space shared memory.
