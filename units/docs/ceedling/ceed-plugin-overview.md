---
id: "ceed-plugin-overview"
type: "concept"
domain: "test"
title: "Plugin Overview"
summary: "When enabled, this plugin creates a new set of gcov: tasks that mirror Ceedling’s existing test: tasks. A gcov: task executes one or more tests with coverage enabled for the source files exercised by those tests."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/gcov/overview.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/"
license: "MIT"
mode: "V"
---

When enabled, this plugin creates a new set of `gcov:` tasks that mirror
Ceedling’s existing `test:` tasks. A `gcov:` task executes one or more tests
with coverage enabled for the source files exercised by those tests.

The Gcov plugin creates a duplicate test build with `gcov:` 
command line plugin tasks because of the needs of coverage instrumentation 
at compile time. [This is intentional and needed](https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/../index.md#understanding-plugin-build-duplication).

!!! note
    A `gcov:` task is a [delta build](https://throwtheswitch.github.io/Ceedling/plugins/gcov/overview/../../getting-started/builds.md).
    This plugin maintains its own dependency cache. A test executable will be 
    rebuilt the first time you run a `gcov:` build.

This plugin also provides an extensive set of options for generating various
coverage reports for your project. The simplest is text-based coverage 
summaries printed to the console after a `gcov:` test task is executed.
