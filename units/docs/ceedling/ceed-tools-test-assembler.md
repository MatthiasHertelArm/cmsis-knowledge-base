---
id: "ceed-tools-test-assembler"
type: "concept"
domain: "test"
title: "`:tools`: `:test_assembler`"
summary: "`:tools`: `:test_assembler`"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#test-assembler"
license: "MIT"
mode: "V"
---

Assembler for test assembly code

- `${1}`: input assembly source file
- `${2}`: output object file
- `${3}`: search paths
- `${4}`: #define symbols (accepted but ignored by GNU assembler)

**Default**: `as`
