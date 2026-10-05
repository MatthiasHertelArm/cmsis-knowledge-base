---
id: "ceed-coverage-reporting"
type: "concept"
domain: "test"
title: "Coverage Reporting"
summary: "The gcov plugin is one of Ceedling’s most used features. It orchestrates GCC coverage instrumentation and use of the gcov tool to generate code coverage for test builds."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/gcov-plugin.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/"
license: "MIT"
mode: "V"
---

The `gcov` plugin is one of Ceedling’s most used features. It orchestrates GCC 
coverage instrumentation and use of the `gcov` tool to generate code coverage 
for test builds. Optionally, it can generate HTML, XML, JSON, and text reports 
via the GCovr and/or ReportGenerator reporting tools.

See the full [Gcov Plugin documentation](https://throwtheswitch.github.io/Ceedling/reference/gcov-plugin/../plugins/gcov/index.md) for concepts, 
installation, troubleshooting, and worked examples.

```yaml
:plugins:
  :enabled:
    - gcov

:gcov:
  :summaries: FALSE

:gcov:
  :utilities:
    - gcovr

:gcov:
  :reports:
    - HtmlBasic
```

---
