---
id: "llvmet-migrating-from-arm-gnu-toolchain-assembly-language"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Assembly language"
summary: "clang should be used instead of arm-none-eabi-as to compile assembly (.s and .S) files."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#assembly-language"
license: "Apache-2.0"
mode: "V"
---

`clang` should be used instead of `arm-none-eabi-as` to compile assembly
(`.s` and `.S`) files.

There are minor differences in the assembly syntax between GNU and LLVM
compilers, however most of the time it is possible to write code that is
accepted by both.

For example, GNU and LLVM compilers differ in:
* Use of `.N` and `.W` suffixes for Thumb instructions.
* Use of `S` suffix for flag setting instructions.
