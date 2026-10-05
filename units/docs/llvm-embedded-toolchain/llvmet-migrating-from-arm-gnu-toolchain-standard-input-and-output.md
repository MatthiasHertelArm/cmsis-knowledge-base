---
id: "llvmet-migrating-from-arm-gnu-toolchain-standard-input-and-output"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Standard input and output"
summary: "See Picolibc and Operating Systems for the details on redirecting stdin, stdout and stderr."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#standard-input-and-output"
license: "Apache-2.0"
mode: "V"
---

See [Picolibc and Operating Systems](https://github.com/picolibc/picolibc/blob/main/doc/os.md)
for the details on redirecting `stdin`, `stdout` and `stderr`.

The `baremetal-uart` [sample](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/tree/main/samples/src/baremetal-uart)
provides a basic code example for redirecting `stdout`.
