---
id: "ceed-gtest-like-console-report-setup"
type: "concept"
domain: "test"
title: "GTest-like Console Report: Setup"
summary: "Enable the plugin in your Ceedling project by adding report_tests_gtestlike_stdout to the list of enabled plugins instead of any other report_testsstdout plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-gtestlike-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout/#setup"
license: "MIT"
mode: "V"
---

Enable the plugin in your Ceedling project by adding 
`report_tests_gtestlike_stdout` to the list of enabled plugins instead of any 
other `report_tests_*_stdout` plugin.

```YAML
:plugins:
  :enabled:
    - report_tests_gtestlike_stdout
```
