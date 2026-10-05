---
id: "intr-better-firmware-with-llvm-clang"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang"
summary: "If you have ever done software development that involves Apple products, FreeBSD, WebAssembly, or Rust, you have used the wildly popular compiler toolchain known as LLVM."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you have ever done software development that involves Apple products, FreeBSD, WebAssembly, or Rust, you have used the wildly popular compiler toolchain known as LLVM. However, LLVM and the open source C-language compiler built on top of it (Clang) do not get a lot of attention in the embedded world.



In this article, I hope I can convince you that adding a Clang build target to your project can be
a relatively simple and useful endeavor. We will cover how to take advantage of some of the
rich features shipped with the toolchain and identify some memory leaks and mutex deadlocks in an
example project at compile time! We will also walk through a step-by-step example of updating a GCC
based ARM Cortex-M project to cross-compile with LLVM/Clang.



> Note: While the focus of the article will be using LLVM/Clang with ARM Cortex-M embedded devices, the
> general overview of LLVM as well as the features leveraged can be applied to any architecture
> supported by the toolchain.
