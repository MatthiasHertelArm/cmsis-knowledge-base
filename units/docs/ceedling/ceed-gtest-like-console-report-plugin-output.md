---
id: "ceed-gtest-like-console-report-plugin-output"
type: "concept"
domain: "test"
title: "GTest-like Console Report: Plugin Output"
summary: "The GoogleTest format is verbose. It lists every test with its result, then summarizes the run."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#plugin-output"
license: "MIT"
mode: "V"
---

The GoogleTest format is verbose. It lists every test with its result, then
summarizes the run.

### Example output

The example below reports a suite of 5 tests in 3 test files. One test passes
alongside a skipped test in its file, and one test fails.

```sh
 > ceedling test:all
```

```
[==========] Running 5 tests from 3 test suites.
[----------] Global test environment set-up.
[----------] 2 tests from test/TestUsartModel.c
[ RUN      ] test/TestUsartModel.c.testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting
[       OK ] test/TestUsartModel.c.testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting (0 ms)
[ RUN      ] test/TestUsartModel.c.testShouldReturnWakeupMessage
[       OK ] test/TestUsartModel.c.testShouldReturnWakeupMessage (0 ms)
[----------] 2 tests from test/TestUsartModel.c (1277 ms total)

[----------] 2 tests from test/TestTimerConductor.c
[ RUN      ] test/TestTimerConductor.c.testInitShouldCallHardwareAndInterruptInit
[       OK ] test/TestTimerConductor.c.testInitShouldCallHardwareAndInterruptInit (0 ms)
[ RUN      ] test/TestTimerConductor.c.testRunShouldHandleTimerOverflow
test/TestTimerConductor.c(34): Skipped
Waiting on driver rewrite

[  SKIPPED ] test/TestTimerConductor.c.testRunShouldHandleTimerOverflow (0 ms)
[----------] 2 tests from test/TestTimerConductor.c (402 ms total)

[----------] 1 test from test/TestModel.c
[ RUN      ] test/TestModel.c.testInitShouldCallSchedulerAndTemperatureFilterInit
test/TestModel.c(21): error: Function TaskScheduler_Init() called more times than expected.
 Actual:   FALSE
 Expected: TRUE
[  FAILED  ] test/TestModel.c.testInitShouldCallSchedulerAndTemperatureFilterInit (0 ms)
[----------] 1 test from test/TestModel.c (581 ms total)

[----------] Global test environment tear-down
[==========] 5 tests from 3 test suites ran. (2260 ms total)
[  PASSED  ] 3 tests.
[  SKIPPED ] 1 test, listed below:
[  SKIPPED ] test/TestTimerConductor.c.testRunShouldHandleTimerOverflow
[  FAILED  ] 1 test, listed below:
[  FAILED  ] test/TestModel.c.testInitShouldCallSchedulerAndTemperatureFilterInit

 1 FAILED TEST
```

A skipped test prints its location and its `TEST_IGNORE_MESSAGE()` text, then a
blank line and its result. A test ignored with `TEST_IGNORE()` has no message,
so its message line is absent.

A run in which every test passes ends at its `[  PASSED  ]` line. The failure
list and its trailer appear only when a test fails.

### Example output with ignored tests left out

The same suite with `:ignored_as_skipped: FALSE` reports 4 tests. The ignored
test is gone from its section, from the counts, and from the summary.

```
[==========] Running 4 tests from 3 test suites.

 ...

[----------] 1 test from test/TestTimerConductor.c
[ RUN      ] test/TestTimerConductor.c.testInitShouldCallHardwareAndInterruptInit
[       OK ] test/TestTimerConductor.c.testInitShouldCallHardwareAndInterruptInit (0 ms)
[----------] 1 test from test/TestTimerConductor.c (402 ms total)

 ...

[----------] Global test environment tear-down
[==========] 4 tests from 3 test suites ran. (2260 ms total)
[  PASSED  ] 3 tests.
[  FAILED  ] 1 test, listed below:
[  FAILED  ] test/TestModel.c.testInitShouldCallSchedulerAndTemperatureFilterInit

 1 FAILED TEST
```
