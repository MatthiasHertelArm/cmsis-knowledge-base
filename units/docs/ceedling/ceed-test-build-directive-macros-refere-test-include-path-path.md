---
id: "ceed-test-build-directive-macros-refere-test-include-path-path"
type: "concept"
domain: "test"
title: "Test Build Directive Macros Reference: `TEST_INCLUDE_PATH(\"path\")`"
summary: "Add a header search path to an individual test executable's compiler invocation. This supplements — it does not replace — the :paths ↳ :include entries from your project file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/reference/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/build-directives/#test-include-path-path"
license: "MIT"
mode: "V"
---

Add a header search path to an individual test executable's compiler
invocation. This supplements — it does not replace — the `:paths` ↳ `:include`
entries from your project file.

- Argument: a path string using forward slashes
- Paths are relative to the working directory from which `ceedling` is executed
- Multiple uses per test file are allowed, one per line
