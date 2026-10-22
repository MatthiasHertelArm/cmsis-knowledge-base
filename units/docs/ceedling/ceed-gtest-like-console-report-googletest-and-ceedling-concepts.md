---
id: "ceed-gtest-like-console-report-googletest-and-ceedling-concepts"
type: "concept"
domain: "test"
title: "GTest-like Console Report: GoogleTest and Ceedling concepts"
summary: "GoogleTest and Ceedling describe a test suite in different terms. This table maps each GoogleTest concept to its Ceedling and Unity counterpart and to this plugin’s console output."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#googletest-and-ceedling-concepts"
license: "MIT"
mode: "V"
---

GoogleTest and Ceedling describe a test suite in different terms. This table maps
each GoogleTest concept to its Ceedling and Unity counterpart and to this plugin’s
console output.

| GoogleTest | Ceedling & Unity | In this report |
|---|---|---|
| Test suite | A test file, built into one test executable | A `[----------] N tests from <test file>` section |
| Test | A Unity test case in that test file | `<test file>.<test case>` |
| Passed test (`[       OK ]`) | A passing test case | Listed and counted as passed |
| Failed test (`[  FAILED  ]`) | A failing test case | Listed with its `file(line)` location and counted as failed |
| Skipped test (`GTEST_SKIP()`, `[  SKIPPED ]`) | `TEST_IGNORE()` or `TEST_IGNORE_MESSAGE()` | Listed and counted as skipped, or left out with `:ignored_as_skipped: FALSE` |
| Disabled test (`DISABLED_` prefix) | No equivalent | Never reported |
| Per-test time | Not measured; Ceedling times each test executable | Each test reports `0 ms`; each section reports its file’s time |
| Incremental output | Results are collected at the end of a build | The full report prints once the build ends |

An ignored Unity test is a skipped GoogleTest test, not a disabled one. Unity
decides to ignore a test at runtime. `setUp()` runs, the test body begins,
`TEST_IGNORE()` ends it, and `tearDown()` runs. That is what `GTEST_SKIP()` does.
A GoogleTest `DISABLED_` test never runs at all.

Tests that never run never reach Ceedling’s results. Test cases excluded by the
`--test-case` or `--exclude-test-case` command line filters, or hidden by the
preprocessor, therefore never appear in this report. They are not reported as
disabled tests.

Each section lists its tests in source order. Skipped tests count toward the
run’s total and its suite count. The summary reports passed, then skipped, then
failed tests, as GoogleTest does. It lists skipped and failed tests only when
there are any.
