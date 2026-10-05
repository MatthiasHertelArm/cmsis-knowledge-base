---
id: "llvmet-optimization-flags-additional-loop-unroll-in-the-lto-pipeli"
type: "concept"
domain: "project"
title: "optimization flags: Additional loop unroll in the LTO pipeline"
summary: "In some cases it is benefitial to perform an additional loop unroll pass so that extra information becomes available to later passes, e.g. SROA. Use cases where this could be beneficial - multiple (N>=4) nested loops."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/optimization-flags.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/optimization-flags.md#additional-loop-unroll-in-the-lto-pipeline"
license: "Apache-2.0"
mode: "V"
---

In some cases it is benefitial to perform an additional loop unroll pass so that extra information becomes available to later passes, e.g. SROA.
Use cases where this could be beneficial - multiple (N>=4) nested loops.

### Usage:
    -Wl,-plugin-opt=-extra-LTO-loop-unroll=true/false
