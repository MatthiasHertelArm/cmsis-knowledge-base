---
id: "ceed-libraries-libraries-system"
type: "concept"
domain: "test"
title: "`:libraries`: `:libraries` ↳ `:system`"
summary: "Libraries listed here will be injected into releases and tests."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/libraries.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/libraries/#libraries-system"
license: "MIT"
mode: "V"
---

Libraries listed here will be injected into releases and tests.

These libraries are assumed to be findable by the configured linker tool, should
need no path help, and can be specified by common linker shorthand for libraries.

For example, specifying `m` will include the math library per the GCC
convention. The file itself on a Unix-like system will be `libm` and the `gcc`
command line argument will be `-lm`.

**Default**: `[]` (empty)
