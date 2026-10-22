---
id: "zep-test-framework-quick-start-integration-testing"
type: "concept"
domain: "test"
title: "Test Framework: Quick start - Integration testing"
summary: "A simple working base is located at samples/subsys/testsuite/integration. To make a test application for the bar component of foo, you should copy the sample folder to tests/foo/bar and edit files there adjusting for your test application's purposes."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

A simple working base is located at `samples/subsys/testsuite/integration`.
To make a test application for the **bar** component of **foo**, you should copy the
sample folder to `tests/foo/bar` and edit files there adjusting for your test
application's purposes.

To build and execute all applicable test scenarios defined in your test application
use the Twister tool, for example:

```console

west twister -T tests/foo/bar/
```
To select just one of the test scenarios, run Twister with `--scenario` command:

```console

west twister --scenario tests/foo/bar/your.test.scenario.name
```
In the command line above `tests/foo/bar` is the path to your test application and
`your.test.scenario.name` references a test scenario defined in `tests.yaml`
file, which is like `sample.testing.ztest` in the boilerplate test suite sample.

See Twister test project diagram for more details
on how Twister deals with Ztest application.

The sample contains the following files:

A test application may consist of multiple test suites that
either can be testing functionality or APIs. Functions implementing a test case
should follow the guidelines below:

* Test cases function names should be prefixed with **test_**
* Test cases should be documented using doxygen
* Test case function names should be unique within the section or component being
  tested

For example:

```C

/**
 * @brief Test Asserts
 *
 * This test case verifies the zassert_true macro.
 */
ZTEST(my_suite, test_assert)
{
        zassert_true(1, "1 was false");
}
```

### Listing Tests


Tests (test applications) in the Zephyr tree consist of many test scenarios that run as
part of a project and test similar functionality, for example an API or a
feature. The `twister` script can parse the test scenarios, suites and cases in all
test applications or a subset of them, and can generate reports on a granular
level, i.e. if test cases have passed or failed or if they were blocked or skipped.

Twister parses the source files looking for test case names, so you
can list all kernel test cases, for example, by running:

```console

west twister --list-tests -T tests/kernel
```

### Skipping Tests


Special- or architecture-specific tests cannot run on all
platforms and architectures, however we still want to count those and
report them as being skipped.  Because the test inventory and
the list of tests is extracted from the code, adding
conditionals inside the test suite is sub-optimal.  Tests that need
to be skipped for a certain platform or feature need to explicitly
report a skip using `ztest_test_skip` or `Z_TEST_SKIP_IFDEF`. If the test runs,
it needs to report either a pass or fail.  For example:

```C

#ifdef CONFIG_TEST1
ZTEST(common, test_test1)
{
     zassert_true(1, "true");
}
#else
ZTEST(common, test_test1)
{
     ztest_test_skip();
}
#endif

ZTEST(common, test_test2)
{
     Z_TEST_SKIP_IFDEF(CONFIG_BUGxxxxx);
     zassert_equal(1, 0, NULL);
}

ZTEST_SUITE(common, NULL, NULL, NULL, NULL, NULL);
```
