---
id: "ceed-test-build-directive-macros-refere"
type: "concept"
domain: "test"
title: "Test Build Directive Macros Reference"
summary: "For detailed usage guidance, purpose explanations, and examples for these macros, see Test Build Directive Macros."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/build-directives.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/build-directives/"
license: "MIT"
mode: "V"
---

For detailed usage guidance, purpose explanations, and examples for these
macros, see [Test Build Directive Macros](https://throwtheswitch.github.io/Ceedling/reference/build-directives/../testing-guide/build-directives.md).

Both macros are defined in `unity.h` and evaluate to empty strings at compile
time — they serve only as text markers for Ceedling's scanner. `#include "unity.h"`
must appear above their use in a test file.

!!! warning "Incompatible with conditional preprocessor blocks"
    `TEST_SOURCE_FILE()` and `TEST_INCLUDE_PATH()` cannot be enclosed in
    `#ifdef` or other conditional compilation preprocessor statements. See
    [preprocessing gotchas](https://throwtheswitch.github.io/Ceedling/reference/build-directives/../testing-guide/conventions.md#preprocessing-gotchas)
    for details.
