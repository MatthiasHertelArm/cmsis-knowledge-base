---
id: "ceed-gtest-like-console-report-configuration"
type: "concept"
domain: "test"
title: "GTest-like Console Report: Configuration"
summary: "One setting controls how the report treats ignored tests. By default, a test ignored with Unity’s TEST_IGNORE() or TEST_IGNORE_MESSAGE() is reported as a GoogleTest skipped test."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#configuration"
license: "MIT"
mode: "V"
---

One setting controls how the report treats ignored tests. By default, a test
ignored with Unity’s `TEST_IGNORE()` or `TEST_IGNORE_MESSAGE()` is reported as a
GoogleTest skipped test.

```YAML
:report_tests_gtestlike_stdout:
  :ignored_as_skipped: TRUE    # Default
```

Set it to `FALSE` to leave ignored tests out of the report. Ignored tests are
then neither listed nor counted, and a test file whose every test is ignored has
no section at all. The rest of the report is unchanged.
