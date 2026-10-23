---
id: "ceed-ide-test-suite-console-report-plugin-overview"
type: "concept"
domain: "test"
title: "IDE Test Suite Console Report: Plugin Overview"
summary: "This plugin replaces the more commonly used \"pretty\" test report plugin that defaults for command line use. Like its sibling, it collects raw test results from the test executables of your test suite and prints them in summary form."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-ide-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout/#plugin-overview"
license: "MIT"
mode: "V"
---

This plugin replaces the more commonly used "pretty" test report plugin that defaults
for command line use. Like its sibling, it collects raw test results from the test 
executables of your test suite and prints them in summary form.

The difference is how it lists failed and ignored tests. By default, each one
prints in the shape of a GCC diagnostic. An IDE that reads GCC output turns each
line into a problem that links to the test.

Example:

```
test/TestModel.c:21:1: error: testInitShouldCallSchedulerAndTemperatureFilterInit: Function TaskScheduler_Init() called more times than expected.
```

A failed test is an `error`. An ignored test is a `warning`. The line names the
test file, the test’s line, the test case, and Unity’s message.

Unity reports a line but no column, so the column is always `1`.

Eclipse CDT, VS Code, and CLion all read this shape. So do many other IDEs and
tools that understand GCC output, including ones not covered here.
