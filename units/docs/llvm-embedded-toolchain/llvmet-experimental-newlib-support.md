---
id: "llvmet-experimental-newlib-support"
type: "concept"
domain: "project"
title: "Experimental newlib support"
summary: "LLVM Embedded Toolchain for Arm uses picolibc as the standard C library. For compatibility with existing projects using newlib, a separate package of newlib-based library variants is provided."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/newlib.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/newlib.md"
license: "Apache-2.0"
mode: "V"
---

LLVM Embedded Toolchain for Arm uses [`picolibc`](https://github.com/picolibc/picolibc)
as the standard C library. For compatibility with existing projects using
[`newlib`](https://sourceware.org/newlib/), a separate package of `newlib`-based
library variants is provided.

> **NOTE:**  `newlib` support in LLVM Embedded Toolchain for Arm is experimental
> and may change in following releases.
