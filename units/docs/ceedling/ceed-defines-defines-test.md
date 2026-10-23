---
id: "ceed-defines-defines-test"
type: "concept"
domain: "test"
title: "`:defines`: `:defines` ↳ `:test`"
summary: "This project configuration entry adds the specified items as symbols to compilation of C components in a test executable’s build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/#defines-test"
license: "MIT"
mode: "V"
---

This project configuration entry adds the specified items as symbols to
compilation of C components in a test executable’s build.

Symbols may be represented in a simple YAML list or with a more sophisticated
file matcher YAML key plus symbol list. Both are documented below.

Every C file that comprises a test executable build will be compiled with the
symbols configured that match the test filename itself.

**Default**: `[]` (empty)
