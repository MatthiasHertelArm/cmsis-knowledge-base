---
id: "ceed-plugin-overview-advanced-coverage-reports"
type: "concept"
domain: "test"
title: "Plugin Overview: Advanced Coverage Reports"
summary: "For more advanced visualizations and reporting, this plugin also supports a variety of report generation options."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/#advanced-coverage-reports"
license: "MIT"
mode: "V"
---

For more advanced visualizations and reporting, this plugin also supports a 
variety of report generation options.

Advanced report generation uses [gcovr] and / or [ReportGenerator] to generate
HTML, XML, JSON, or text-based reports from coverage-instrumented test runs. 
See the tools' respective sites for examples of the reports they can generate.

In the default configuration, if reports are enabled, this plugin automatically
generates reports in the build’s `artifacts/` directory after each execution of
a `gcov:` task.

An optional setting documented below disables automatic report generation, 
providing a separate Ceedling task instead. Reports can then be generated
on demand after test suite runs.

[gcovr]: https://www.gcovr.com/
[ReportGenerator]: https://reportgenerator.io
