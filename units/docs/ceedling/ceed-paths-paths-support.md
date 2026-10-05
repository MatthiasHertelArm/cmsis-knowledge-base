---
id: "ceed-paths-paths-support"
type: "concept"
domain: "test"
title: "`:paths`: `:paths` ↳ `:support`"
summary: "Any C files you might need to aid your unit testing. For example, on occasion, you may need to create a header file containing a subset of function signatures matching those elsewhere in your code (e.g."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#paths-support"
license: "MIT"
mode: "V"
---

Any C files you might need to aid your unit testing. For example, on occasion,
you may need to create a header file containing a subset of function signatures
matching those elsewhere in your code (e.g. a subset of your OS functions, a
portion of a library API, etc.). Why? To provide finer grained control over
mock function substitution or limiting the size of the generated mocks.

**Default**: `[]` (empty)
