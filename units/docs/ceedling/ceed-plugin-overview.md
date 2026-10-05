---
id: "ceed-plugin-overview"
type: "concept"
domain: "test"
title: "Plugin Overview"
summary: "gcov: tasks entirely duplicate test: tasks and test builds because of the needs of coverage instrumentation at compile time."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/gcov/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/"
license: "MIT"
mode: "V"
---

!!! note
    When enabled, this plugin creates a new set of `gcov:` tasks that mirror
    Ceedling’s existing `test:` tasks. A `gcov:` task executes one or more tests
    with coverage enabled for the source files exercised by those tests.

    `gcov:` tasks entirely duplicate `test:` tasks and test builds because of 
    the needs of coverage instrumentation at compile time.

This plugin also provides an extensive set of options for generating various
coverage reports for your project. The simplest is text-based coverage 
summaries printed to the console after a `gcov:` test task is executed.
