---
id: "ceed-tools-release-assembler"
type: "concept"
domain: "test"
title: "`:tools`: `:release_assembler`"
summary: "`:tools`: `:release_assembler`"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#release-assembler"
license: "MIT"
mode: "V"
---

Assembler for release assembly code

- `${1}`: input assembly source file
- `${2}`: output object file
- `${3}`: search paths
- `${4}`: #define symbols (accepted but ignored by GNU assembler)

**Default**: `as`
