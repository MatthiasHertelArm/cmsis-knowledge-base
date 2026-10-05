---
id: "intr-code-size-optimization-gcc-compile-introduction"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: Introduction"
summary: "This is the second post in our Firmware Code Size Optimization series. Last time, we talked about measuring code size as a precondition to improving it. Now we’ll leap from planning into action!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#introduction"
license: "CC-BY-SA-4.0"
mode: "V"
---

This is the second post in our [Firmware Code Size Optimization]() series. [Last time](https://interrupt.memfault.com/blog/best-firmware-size-tools), we talked about measuring code size as a
precondition to improving it. Now we’ll leap from planning into action!


In this post, we will review compiler options that we can
use to reduce firmware code size. We will focus on `arm-none-eabi-gcc`, the GCC
compiler used for ARM-based microcontrollers, though most of the compile-time
flags we will cover are available in other GCC flavors as well as in Clang.


You would think that a single flag could be used for “make this as small as
possible”, but unfortunately it isn’t so. Instead, code size optimization
involves complicated trade-offs that must be considered on a case by case basis.
