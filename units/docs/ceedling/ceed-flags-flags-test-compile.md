---
id: "ceed-flags-flags-test-compile"
type: "concept"
domain: "test"
title: "`:flags`: `:flags` ↳ `:test` ↳ `:compile`"
summary: "This project configuration entry adds the specified items as flags to compilation of C components in a test executable’s build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#flags-test-compile"
license: "MIT"
mode: "V"
---

This project configuration entry adds the specified items as flags to
compilation of C components in a test executable’s build.

Flags may be represented in a simple YAML list or with a more sophisticated
file matcher YAML key plus flag list. Both are documented below.

**Default**: `[]` (empty)
