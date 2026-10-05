---
id: "ceed-test-suite-report-log-factory-configuration"
type: "concept"
domain: "test"
title: "Test Suite Report Log Factory: Configuration"
summary: "Enable the reports you wish to generate — json, junit, and/or cppunit — within the :report_tests_log_factory ↳ :reports configuration list."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/report-tests-log-factory.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory/#configuration"
license: "MIT"
mode: "V"
---

Enable the reports you wish to generate — `json`, `junit`, and/or `cppunit` — within the `:report_tests_log_factory` ↳ `:reports` configuration list.

```yaml
:report_tests_log_factory:
  # Any one or all four of the following...
  :reports:
    - json
    - junit
    - cppunit
    - html
```

Each report is written to a default filename within `<build root>/artifacts/<context>`:

* JSON: _tests_report.json_
* JUnit XML: _junit_tests_report.xml_
* CppUnit XML: _cppunit_tests_report.xml_
* HTML: _tests_report.html_

To change the output filename, specify it with the `:filename` key beneath the relevant report within the `:report_tests_log_factory` configuration block:

```yaml
:report_tests_log_factory:
  # Replace `<report>` with one of the available options above.
  # Each report can have its own sub-configuration block.
  :reports:
    - <report>
  :<report>:
    :filename: 'more_better_filename.ext'
```
