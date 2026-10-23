---
id: "ceed-test-suite-report-log-factory-plugin-overview"
type: "concept"
domain: "test"
title: "Test Suite Report Log Factory: Plugin Overview"
summary: "Test reports are handy for all sorts of reasons. Various build and reporting tools are able to generate, visualize, or otherwise process results encoded in handy container formats including JSON and XML."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-log-factory.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory/#plugin-overview"
license: "MIT"
mode: "V"
---

Test reports are handy for all sorts of reasons. Various build and reporting tools are able to generate, visualize, or otherwise process results encoded in handy container formats including JSON and XML.

This plugin generates one or more of up to four available test suite report formats:

1. JSON
1. JUnit XML
1. CppUnit XML
1. HTML

This plugin generates reports after test builds, storing them in your project `artifacts/` build path. It also regenerates reports when `ceedling summary` is executed, building reports from the test results a previous test build left on disk. These reports are written for the `test` context and carry no build duration, since no build ran.

With a limited amount of Ruby code, you can also create your own report without creating an entire Ceedling plugin.
