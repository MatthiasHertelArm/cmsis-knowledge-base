---
id: "intr-profiling-newlib-nano-s-memcpy"
type: "concept"
domain: "debug"
title: "Profiling newlib-nano's memcpy"
summary: "Newlib is a very popular libc targeting embedded systems. It's the libc that ships with the GNU Arm Embedded Toolchain published by ARM."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-09-07-memcpy-newlib-nano.md"
doc_source: "https://interrupt.memfault.com/blog/memcpy-newlib-nano"
license: "CC-BY-SA-4.0"
mode: "V"
---

[Newlib](http://www.sourceware.org/newlib/) is a very popular libc targeting
embedded systems. It's the libc that ships with the [GNU Arm Embedded
Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm)
published by ARM.



This article takes a look at one of the commonly used functions provided by the
Newlib C library: `memcpy`. We'll examine the default nano implementation and
the performance implications, comparing it against the faster non-default
implementation.
