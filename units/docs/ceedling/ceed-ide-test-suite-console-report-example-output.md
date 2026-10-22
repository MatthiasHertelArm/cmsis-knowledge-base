---
id: "ceed-ide-test-suite-console-report-example-output"
type: "concept"
domain: "test"
title: "IDE Test Suite Console Report: Example Output"
summary: "The Gcov, Bullseye, and Valgrind plugins print their test results through this plugin when it is enabled. Their failed and ignored tests are listed the same way."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-ide-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/#example-output"
license: "MIT"
mode: "V"
---

```sh
 > ceedling test:Model
```

```
--------------------
IGNORED TEST SUMMARY
--------------------
test/TestModel.c:36:1: warning: testFilterShouldSettle: Awaiting new sensor driver

-------------------
FAILED TEST SUMMARY
-------------------
test/TestModel.c:21:1: error: testInitShouldCallSchedulerAndTemperatureFilterInit: Function TaskScheduler_Init() called more times than expected.

--------------------
OVERALL TEST SUMMARY
--------------------
TESTED:  3
PASSED:  1
FAILED:  1
IGNORED: 1

---------------------
BUILD FAILURE SUMMARY
---------------------
 • Unit test failures.
```

The Gcov, Bullseye, and Valgrind plugins print their test results through this
plugin when it is enabled. Their failed and ignored tests are listed the same way.
