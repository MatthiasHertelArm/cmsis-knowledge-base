---
id: "llvmet-migrating-from-arm-gnu-toolchain-benefits"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: Benefits"
summary: "Using multiple toolchains to build a project benefits from different checks and warnings present in different compilers to catch more issues, particularly C and C++ standards compliance, during build time."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#benefits"
license: "Apache-2.0"
mode: "V"
---

Using multiple toolchains to build a project benefits from different checks
and warnings present in different compilers to catch more issues,
particularly C and C++ standards compliance, during build time.

LLVM Embedded Toolchain for Arm provides support for multiple sanitizers
and memory safety features to also catch typical issues at runtime during testing,
see the [Clang documentation](https://clang.llvm.org/docs/index.html)
and [samples](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/tree/main/samples/src).

LLVM Embedded Toolchain for Arm provides superior performance when targeting the
Armv8-M or later architecture, including the
[Arm Helium Technology](https://www.arm.com/technologies/helium)
(M-Profile Vector Extension, MVE).
