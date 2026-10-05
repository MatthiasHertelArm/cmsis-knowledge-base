---
id: "intr-better-firmware-with-llvm-clang-static-analysis-with-clang-and-scan-buil"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Static Analysis With Clang and scan-build"
summary: "Further down in this post, we will dive into how to migrate a project using GCC to Clang, but first, let’s take a look at some of the awesome static analysis passes and checkers we can run on …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#static-analysis-with-clang-and-scan-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Further down in this post](#porting-gcc-to-clang), we will dive into how to migrate a project using GCC to Clang, but
first, let’s take a look at some of the awesome static analysis passes and checkers we can run on
our example project with LLVM/Clang!
