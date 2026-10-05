---
id: "ceed-flags-flags-test-preprocess"
type: "concept"
domain: "test"
title: "`:flags`: `:flags` ↳ `:test` ↳ `:preprocess`"
summary: "This project configuration entry adds the specified items as flags to any needed preprocessing of components in a test executable’s build. Preprocessing must be enabled for this matching to have any effect. (See :project ↳ :use_test_preprocessor.)"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/flags.md"
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
    Left unspecified, `:preprocess` flags default to behaving identically
    to `:compile` flags. Override this behavior by adding `:test` ↳ `:preprocess`
    flags. If you want no additional flags for preprocessing regardless of test
    compilation flags, simply specify an empty list `[]`.

**Default**: Same flags as specified for test compilation
