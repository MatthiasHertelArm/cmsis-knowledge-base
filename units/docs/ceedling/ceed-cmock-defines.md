---
id: "ceed-cmock-defines"
type: "concept"
domain: "test"
title: "`:cmock`: `:defines`"
summary: "Adds list of symbols used to configure CMock’s C code features in its source and header files at compile time."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/cmock.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/#defines"
license: "MIT"
mode: "V"
---

Adds list of symbols used to configure CMock’s C code features in its source
and header files at compile time.

See [Using Unity & CMock](https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/../../testing-guide/frameworks.md) for
much more on configuring and making use of these frameworks in your build.

To manage overall command line length, these symbols are only added to
compilation when a CMock C source file is compiled.

No symbols must be set unless CMock’s defaults are inappropriate for your
environment and needs.

**Default**: `[]` (empty)
