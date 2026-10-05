---
id: "llvmet-experimental-llvm-libc-support-limitations-of-llvm-libc-in-llvm-embedde"
type: "concept"
domain: "project"
title: "Experimental LLVM libc support: Limitations of LLVM libc in LLVM Embedded Toolchain for Arm"
summary: "At present, this toolchain does not build any C++ libraries to go with LLVM libc."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/llvmlibc.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/llvmlibc.md#limitations-of-llvm-libc-in-llvm-embedded-toolchain-for-arm"
license: "Apache-2.0"
mode: "V"
---

At present, this toolchain does not build any C++ libraries to go with
LLVM libc.

At the time of writing this (2024-07), LLVM libc is a work in
progress. It is incomplete: not all standard C library functionality
is provided.
