---
id: "ceed-example-usage-report-generation-manual-task"
type: "concept"
domain: "test"
title: "Example Usage: Report generation manual task"
summary: "If the :report_task: configuration option is enabled, reports are not automatically generaed after test suite coverage builds. Instead, report generation is triggered by the report:gcov task."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/examples.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/examples/#report-generation-manual-task"
license: "MIT"
mode: "V"
---

If the `:report_task:` configuration option is enabled, reports are not 
automatically generaed after test suite coverage builds. Instead, report 
generation is triggered by the `report:gcov` task.

```yaml
:plugins:
  :enabled:
    - gcov

:gcov:
  :utilities:
    - gcovr            # Enabled by default -- shown for completeness
  :report_task: TRUE
  :reports:            # See later section for report configuration
    - HtmlBasic        # Enabled by default -- shown for completeness

  ...                  # Further configuration for reporting (not shown)

```

With the separate reporting task enabled, it can be used like any other Ceedling task.

```shell
 > ceedling gcov:all report:gcov
```

or 

```shell
 > ceedling gcov:all

 > ceedling report:gcov
```
