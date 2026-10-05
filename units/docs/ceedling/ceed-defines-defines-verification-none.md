---
id: "ceed-defines-defines-verification-none"
type: "concept"
domain: "test"
title: "`:defines`: `:defines` verification (none)"
summary: "Ceedling does no verification of your configured :define symbols."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/defines.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/defines/#defines-verification-none"
license: "MIT"
mode: "V"
---

Ceedling does no verification of your configured `:define` symbols.

Unity and CMock conditional compilation statements, your
toolchain’s preprocessor, and/or your toolchain’s compiler will complain
appropriately if your specified symbols are incorrect, incomplete, or
incompatible.

Ceedling _does_ validate your `:defines` block in your project configuration.
