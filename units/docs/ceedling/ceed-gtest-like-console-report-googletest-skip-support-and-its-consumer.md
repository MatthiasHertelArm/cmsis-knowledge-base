---
id: "ceed-gtest-like-console-report-googletest-skip-support-and-its-consumer"
type: "concept"
domain: "test"
title: "GTest-like Console Report: GoogleTest skip support and its consumers"
summary: "GoogleTest added skipped tests in version 1.10.0, released in October 2019. That release introduced GTEST_SKIP() along with the [ SKIPPED ] lines in its console output. Earlier versions have no skipped outcome."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#googletest-skip-support-and-its-consumers"
license: "MIT"
mode: "V"
---

GoogleTest added skipped tests in version 1.10.0, released in October 2019.
That release introduced `GTEST_SKIP()` along with the `[  SKIPPED ]` lines in
its console output. Earlier versions have no skipped outcome.

Tools that read GoogleTest output may not understand skipped tests. Some predate
GoogleTest 1.10.0, and others added support only later. LLVM’s `lit` test runner,
for example, added explicit handling for skipped GoogleTest tests in 2021. A tool
written for older output may treat a `[  SKIPPED ]` line as unknown or may report
a skipped test as passed.

Which tools parse this plugin’s output is unknown. If yours misreads skipped
tests, set `:ignored_as_skipped: FALSE` to restore a report without them.
