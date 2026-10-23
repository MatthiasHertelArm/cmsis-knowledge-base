---
id: "ceed-flags-flags-test-link"
type: "concept"
domain: "test"
title: "`:flags`: `:flags` ↳ `:test` ↳ `:link`"
summary: "This project configuration entry adds the specified items as flags to the link step of test executables."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#flags-test-link"
license: "MIT"
mode: "V"
---

This project configuration entry adds the specified items as flags to the link
step of test executables.

Flags may be represented in a simple YAML list or with a more sophisticated
file matcher YAML key plus flag list. Both are documented below.

**Default**: `[]` (empty)
