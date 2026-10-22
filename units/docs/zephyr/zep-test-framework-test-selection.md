---
id: "zep-test-framework-test-selection"
type: "concept"
domain: "test"
title: "Test Framework: Test Selection"
summary: "For tests built for native simulator, use command line arguments to list or select tests to run. The test argument expects a comma separated list of suite::test ."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

For tests built for native simulator, use command line arguments to list
or select tests to run. The test argument expects a comma separated list
of `suite::test` .  You can substitute the test name with an `*` to run all
tests within a suite.

For example

```bash

$ zephyr.exe -list
$ zephyr.exe -test="fixture_tests::test_fixture_pointer,framework_tests::test_assert_mem_equal"
$ zephyr.exe -test="framework_tests::*"
```
