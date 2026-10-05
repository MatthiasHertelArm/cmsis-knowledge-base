---
id: "llvmet-migrating-from-arm-gnu-toolchain-startup-code"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Startup code"
summary: "Refer to Using Picolibc in Embedded Systems for the details of how picolibc handles initialization."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#startup-code"
license: "Apache-2.0"
mode: "V"
---

Refer to [Using Picolibc in Embedded Systems](https://github.com/picolibc/picolibc/blob/main/doc/using.md)
for the details of how `picolibc` handles initialization.

By default, `picolibc` provides an interrupt vector table. To replace it,
the application interrupt vector table should be placed into the `init`
[linker script](https://github.com/picolibc/picolibc/blob/main/doc/linking.md)
section and referenced by the `__interrupt_vector` symbol.
