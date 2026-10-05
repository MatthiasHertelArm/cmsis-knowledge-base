---
id: "intr-gnu-binutils-the-elf-swiss-army-kn"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife"
summary: "There's a lot that takes place between the C code you write and the binary that winds up executing on a device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils"
license: "CC-BY-SA-4.0"
mode: "V"
---

There's a lot that takes place between the C code you write and the binary that winds up executing
on a device. Understanding how to look at and inspect what is emitted by the compiler saves time and
can improve your efficiency in many areas of the development lifecycle -- such as
debugging system problems, identifying issues with compilers or debug info emitted, reducing the
size of binaries, and optimizing an application for performance and latency.



In this article, we will explore some of my favorite binary introspection tools, such as GNU
Binutils. The material is geared toward the embedded software crowd that typically writes C and
C++, but many of the ideas, tools, and lessons learned can be applied to a variety of low-level
software. We will walk through practical examples of how the tools can be leveraged to aid in the
development process irrespective of the compiler you are using (e.g. GCC, Clang, IAR,
ARMCC, etc).
