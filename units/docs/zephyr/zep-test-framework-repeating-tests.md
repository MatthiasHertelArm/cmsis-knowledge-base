---
id: "zep-test-framework-repeating-tests"
type: "concept"
domain: "test"
title: "Test Framework: Repeating Tests"
summary: "By default the tests are executed once. The test cases and test suites may be executed multiple times. Enable CONFIG_ZTEST_REPEAT to execute the tests multiple times."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

By default the tests are executed once. The test cases and test suites
may be executed multiple times. Enable `CONFIG_ZTEST_REPEAT` to
execute the tests multiple times. By default the multiplication factors are 3, which
means every test suite is executed 3 times and every test case is executed 3 times. This can
be changed by the `CONFIG_ZTEST_SUITE_REPEAT_COUNT` and
`CONFIG_ZTEST_TEST_REPEAT_COUNT` Kconfig options.
