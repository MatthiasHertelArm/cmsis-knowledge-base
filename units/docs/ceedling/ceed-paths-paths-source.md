---
id: "ceed-paths-paths-source"
type: "concept"
domain: "test"
title: "`:paths`: `:paths` ↳ `:source`"
summary: "All C files containing release code (code to be tested)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#paths-source"
license: "MIT"
mode: "V"
---

All C files containing release code (code to be tested).

!!! note "Build configuration requirement"
    `:paths` ↳ `:source` must be set for any build — release build or test suite —
    to run.

**Default**: `[]` (empty)
