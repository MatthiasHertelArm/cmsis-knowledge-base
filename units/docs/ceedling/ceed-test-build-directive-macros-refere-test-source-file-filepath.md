---
id: "ceed-test-build-directive-macros-refere-test-source-file-filepath"
type: "concept"
domain: "test"
title: "Test Build Directive Macros Reference: `TEST_SOURCE_FILE(\"filepath\")`"
summary: "Inject a specific source file into a test executable's build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/reference/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/build-directives/#test-source-file-filepath"
license: "MIT"
mode: "V"
---

!!! tip
    Ceedling [distinguishes files of the same name by their path](https://throwtheswitch.github.io/Ceedling/reference/build-directives/../testing-guide/conventions.md#distinguishing-same-named-files).
    Include a partial path to distinguish any source files of the
    same name to be compiled and linked with your test executable.

Inject a specific source file into a test executable's build. Use this when
a source file has no corresponding header file that Ceedling can discover by
convention, or when you need to explicitly include an assembly file (`.s`) in
a test build that has assembly support enabled.

- Argument: a filepath string using forward slashes
- The file must exist within Ceedling's source file collection
- Multiple uses per test file are allowed, one per line

A subtractive decorator `-:` prepending a filepath removes the C file
from the test executable build. This can be useful in overriding certain
Ceedling conventions.
