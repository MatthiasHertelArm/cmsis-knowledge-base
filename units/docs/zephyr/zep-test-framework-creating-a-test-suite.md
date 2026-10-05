---
id: "zep-test-framework-creating-a-test-suite"
type: "concept"
domain: "test"
title: "Test Framework: Creating a test suite"
summary: "Using Ztest to create a test suite is as easy as calling the ZTEST_SUITE. The macro accepts the following arguments:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

Using Ztest to create a test suite is as easy as calling the `ZTEST_SUITE`. The macro
accepts the following arguments:

* `suite_name` - The name of the suite. This name must be unique within a single binary.
* `ztest_suite_predicate_t` - An optional predicate function to allow choosing when the
  test will run. The predicate will get a pointer to the global state passed in through
  `ztest_run_all` and should return a boolean to decide if the suite should run.
* `ztest_suite_setup_t` - An optional setup function which returns a test fixture. This
  will be called and run once per test suite run.
* `ztest_suite_before_t` - An optional before function which will run before every single
  test in this suite.
* `ztest_suite_after_t` - An optional after function which will run after every single
  test in this suite.
* `ztest_suite_teardown_t` - An optional teardown function which will run at the end of
  all the tests in the suite.

Below is an example of a test suite using a predicate:

```C

#include <zephyr/ztest.h>
#include "test_state.h"

static bool predicate(const void *global_state)
{
     return ((const struct test_state*)global_state)->x == 5;
}

ZTEST_SUITE(alternating_suite, predicate, NULL, NULL, NULL, NULL);
```
