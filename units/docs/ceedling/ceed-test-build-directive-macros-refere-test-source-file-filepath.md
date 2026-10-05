---
id: "ceed-test-build-directive-macros-refere-test-source-file-filepath"
type: "concept"
domain: "test"
title: "Test Build Directive Macros Reference: `TEST_SOURCE_FILE(\"filepath\")`"
summary: "Inject a specific source file into a test executable's build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/build-directives/#test-source-file-filepath"
license: "MIT"
mode: "V"
---

Inject a specific source file into a test executable's build. Use this when
a source file has no corresponding header file that Ceedling can discover by
convention, or when you need to explicitly include an assembly file (`.s`) in
a test build that has assembly support enabled.

- Argument: a filepath string using forward slashes
- The file must exist within Ceedling's source file collection
- Multiple uses per test file are allowed, one per line
