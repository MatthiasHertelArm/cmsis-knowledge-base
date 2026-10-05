---
id: "llvmet-migrating-from-arm-gnu-toolchain-toolchain-identification"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Toolchain identification"
summary: "Note that clang defines GNU macros for compatibility too: _GNUC_ equal to 4, _GNUC_MINOR_ equal to 2, and _GNUC_PATCHLEVEL_ equal to 1."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#toolchain-identification"
license: "Apache-2.0"
mode: "V"
---

Toolchain version macros:

|Version number|GNU macro|LLVM macro|
|-------|---------|----------|
|Major|`__GNUC__`|`__clang_major__`|
|Minor|`__GNUC_MINOR__`|`__clang_minor__`|
|Patch level|`__GNUC_PATCHLEVEL__`|`__clang_patchlevel__`|

Note that `clang` defines GNU macros for compatibility too:
`__GNUC__` equal to `4`, `__GNUC_MINOR__` equal to `2`,
and `__GNUC_PATCHLEVEL__` equal to `1`.
