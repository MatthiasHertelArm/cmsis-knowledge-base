---
id: "ceed-test-suite-report-log-factory-setup"
type: "concept"
domain: "test"
title: "Test Suite Report Log Factory: Setup"
summary: "Enable the plugin in your Ceedling project file by adding report_tests_log_factory to the list of enabled plugins."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-log-factory.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory/#setup"
license: "MIT"
mode: "V"
---

Enable the plugin in your Ceedling project file by adding `report_tests_log_factory` to the list of enabled plugins.

```yaml
:plugins:
  :enabled:
    - report_tests_log_factory
```

All generated reports are written to `<build root>/artifacts/<context>`. Your Ceedling project file specifies `<build root>` as a required entry for any build. Your build’s context defaults to `test`. Certain other test build plugins (e.g. GCov) provide a different context (e.g. `gcov`) for test builds, generally named after themselves. That is, for example, if this plugin is used in conjunction with a GCov coverage build, the reports will end up in a subdirectory other than `test/`, `gcov/`.
