---
id: "ceed-defines-defines-preprocess"
type: "concept"
domain: "test"
title: "`:defines`: `:defines` ↳ `:preprocess`"
summary: "This project configuration entry adds the specified items as symbols to any needed preprocessing of components in a test executable’s build. Preprocessing must be enabled for this matching to have any effect. (See :project ↳ :use_test_preprocessor.)"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/#defines-preprocess"
license: "MIT"
mode: "V"
---

This project configuration entry adds the specified items as symbols to any
needed preprocessing of components in a test executable’s build. Preprocessing
must be enabled for this matching to have any effect. (See `:project` ↳
`:use_test_preprocessor`.)

Preprocessing here refers to handling macros, conditional includes, etc. in
header files that are mocked and in complex test files before runners are
generated from them. (See more about the
[Ceedling preprocessing](https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/../../testing-guide/conventions.md#test-preprocessing)
feature.)

Like the `:test` context, compilation symbols may be represented in a simple
YAML list or with a more sophisticated file matcher YAML key plus symbol list.
Both are documented below.

!!! note "Default `:preprocess` symbols"
    Left unspecified, `:preprocess` symbols default to be identical to
    `:test` symbols. Override this behavior by adding `:defines` ↳ `:preprocess`
    symbols. If you want no additional symbols for preprocessing regardless of
    `test` symbols, specify an empty list `[]` in your `:preprocess` matcher.

**Default**: Identical to `:test` context unless specified
