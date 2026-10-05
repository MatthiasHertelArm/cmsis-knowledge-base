---
id: "ceed-libraries-libraries-test"
type: "concept"
domain: "test"
title: "`:libraries`: `:libraries` ↳ `:test`"
summary: "Libraries that should be injected into your test builds when linking occurs."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/libraries.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/libraries/#libraries-test"
license: "MIT"
mode: "V"
---

Libraries that should be injected into your test builds when linking occurs.

These can be specified as naked library names or with relative paths if search
paths are specified with `:paths` ↳ `:libraries`. Otherwise, absolute paths
may be used here.

These library files **must** exist when tests build.

**Default**: `[]` (empty)
