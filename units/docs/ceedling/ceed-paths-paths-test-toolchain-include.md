---
id: "ceed-paths-paths-test-toolchain-include"
type: "concept"
domain: "test"
title: "`:paths`: `:paths` ↳ `:test_toolchain_include`"
summary: "System header files needed by the test toolchain — should your compiler be unable to find them, finds the wrong system include search path, or you need a creative solution to a tricky technical problem."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#paths-test-toolchain-include"
license: "MIT"
mode: "V"
---

System header files needed by the test toolchain — should your compiler be
unable to find them, finds the wrong system include search path, or you need a
creative solution to a tricky technical problem.

Note that if you configure your own toolchain in the `:tools` section, this
search path is largely meaningless to you. However, this is a convenient way
to control the system include path should you rely on the default [GCC][GCC]
tools.

**Default**: `[]` (empty)
