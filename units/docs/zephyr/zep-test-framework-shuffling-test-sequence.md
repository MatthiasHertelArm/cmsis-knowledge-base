---
id: "zep-test-framework-shuffling-test-sequence"
type: "concept"
domain: "test"
title: "Test Framework: Shuffling Test Sequence"
summary: "By default the tests are sorted and ran in alphanumerical order. Test cases may be dependent on this sequence. Enable CONFIG_ZTEST_SHUFFLE to randomize the order. The output from the test will display the seed for failed tests."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

By default the tests are sorted and ran in alphanumerical order.  Test cases may
be dependent on this sequence. Enable `CONFIG_ZTEST_SHUFFLE` to
randomize the order. The output from the test will display the seed for failed
tests.  For native simulator builds you can provide the seed as an argument to
twister with `--seed`.
