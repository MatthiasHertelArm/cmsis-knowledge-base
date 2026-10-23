---
id: "zep-test-framework-api-reference"
type: "concept"
domain: "test"
title: "Test Framework: API reference"
summary: "These macros will instantly fail the test if the related assertion fails. When an assertion fails, it will print the current file, line and function, alongside a reason for the failure and an optional message."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

### Running tests



### Assertions


These macros will instantly fail the test if the related assertion fails.
When an assertion fails, it will print the current file, line and function,
alongside a reason for the failure and an optional message. If the config
`CONFIG_ZTEST_ASSERT_VERBOSE` is 0, the assertions will only print the
file and line numbers, reducing the binary size of the test.

Example output for a failed macro from
`zassert_equal(buf->ref, 2, "Invalid refcount")`:

```none

Assertion failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
Aborted at unit test function
```

### Expectations


These macros will continue test execution if the related expectation fails and subsequently fail the
test at the end of its execution.  When an expectation fails, it will print the current file, line,
and function, alongside a reason for the failure and an optional message but continue executing the
test. If the config `CONFIG_ZTEST_ASSERT_VERBOSE` is 0, the expectations will only print the
file and line numbers, reducing the binary size of the test.

For example, if the following expectations fail:

```C

zexpect_equal(buf->ref, 2, "Invalid refcount");
zexpect_equal(buf->ref, 1337, "Invalid refcount");
```
The output will look something like:

```none

START - test_get_single_buffer
    Expectation failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
    Expectation failed at main.c:63: test_get_single_buffer: Invalid refcount (buf->ref not equal to 1337)
 FAIL - test_get_single_buffer in 0.0 seconds
```

### Assumptions


These macros will instantly skip the test or suite if the related assumption fails.
When an assumption fails, it will print the current file, line, and function,
alongside a reason for the failure and an optional message. If the config
`CONFIG_ZTEST_ASSERT_VERBOSE` is 0, the assumptions will only print the
file and line numbers, reducing the binary size of the test.

Example output for a failed macro from
`zassume_equal(buf->ref, 2, "Invalid refcount")`:

```none

START - test_get_single_buffer
    Assumption failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
 SKIP - test_get_single_buffer in 0.0 seconds
```

### Ztress



### Mocking via FFF


Zephyr has integrated with FFF for mocking. See FFF for documentation. To use it,
include the relevant header:

```C

#include <zephyr/fff.h>
```
Zephyr provides several FFF-based fake drivers which can be used as either stubs or mocks. Fake
driver instances are configured via devicetree and kconfig. See the following
devicetree bindings for more information:

.. zephyr-keep-sorted-start

* `zephyr,fake-can`
* `zephyr,fake-comp`
* `zephyr,fake-eeprom`
* `zephyr,fake-leds`
* `zephyr,fake-pwm`
* `zephyr,fake-regulator`
* `zephyr,fake-rtc`
* `zephyr,fake-stepper-ctrl`
* `zephyr,fake-stepper-driver`

.. zephyr-keep-sorted-stop

Zephyr also has defined extensions to FFF for simplified declarations of fake functions.
See FFF Extensions.
