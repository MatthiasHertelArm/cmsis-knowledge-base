---
id: "ceed-pretty-test-suite-console-report-setup"
type: "concept"
domain: "test"
title: "Pretty Test Suite Console Report: Setup"
summary: "Enable the plugin in your project.yml by adding report_tests_pretty_stdout to the list of enabled plugins instead of any other report_testsstdout plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-pretty-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-pretty-stdout/#setup"
license: "MIT"
mode: "V"
---

Enable the plugin in your project.yml by adding `report_tests_pretty_stdout` to 
the list of enabled plugins instead of any other `report_tests_*_stdout` 
plugin.

``` YAML
:plugins:
  :enabled:
    - report_tests_pretty_stdout
```
