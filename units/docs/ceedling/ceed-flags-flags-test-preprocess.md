---
id: "ceed-flags-flags-test-preprocess"
type: "concept"
domain: "test"
title: "`:flags`: `:flags` ↳ `:test` ↳ `:preprocess`"
summary: "This project configuration entry adds the specified items as flags to any needed preprocessing of components in a test executable’s build. Preprocessing must be enabled for this matching to have any effect. (See :project ↳ :use_test_preprocessor.)"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#flags-test-preprocess"
license: "MIT"
mode: "V"
---

This project configuration entry adds the specified items as flags to any
needed preprocessing of components in a test executable’s build. Preprocessing
must be enabled for this matching to have any effect. (See `:project` ↳
`:use_test_preprocessor`.)

Preprocessing here refers to handling macros, conditional includes, etc. in
header files that are mocked and in complex test files before runners are
generated from them. (See more about the
[Ceedling preprocessing](https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/../../testing-guide/conventions.md#test-preprocessing)
feature.)

Flags may be represented in a simple YAML list or with a more sophisticated
file matcher YAML key plus flag list. Both are documented below.

!!! note "`:preprocess` flags default behavior"
    Left unspecified entirely, `:preprocess` flags default to behaving
    identically to `:compile` flags for every file.

    If `:preprocess` is a matcher hash the flags apply **per file**. A 
    test file that matches one of your `:preprocess` matchers gets exactly 
    those flags, while a test file that matches none of them falls back 
    to flags resolved under `:compile`.

    Override this behavior by adding `:test` ↳ `:preprocess` flags. If you
    want no additional flags for preprocessing regardless of test compilation
    flags, specify an empty list `[]` for the relevant matcher (or for the
    whole `:preprocess` section, if using the simple list format).

!!! warning "Keep line markers in preprocessor output"
    Ceedling reads the line markers in preprocessor output to find 
    `#include`s, mockable functions, and test cases. With test preprocessing 
    enabled, Ceedling refuses to start if `-P` or `--no-line-commands` 
    appears in `:preprocess` flags. The same holds for `:compile` flags, 
    which preprocessing uses wherever no `:preprocess` flags apply.

**Default**: Same flags as that same file resolved to for `:compile`, unless specified
