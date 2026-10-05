---
id: "intr-the-best-and-worst-gcc-compiler-fl"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded"
summary: "Compilers have hundreds of flags and configuration settings which can be toggled to control performance optimizations, code size, error checks and diagnostic information emitted."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags"
license: "CC-BY-SA-4.0"
mode: "V"
---

Compilers have hundreds of flags and configuration settings which can be toggled to control
performance optimizations, code size, error checks and diagnostic information emitted. Often
these settings wind up being copy and pasted from project to project, makefile to makefile, but
it's good to periodically audit the current options selected for a project.



In this article we will explore some of the best and worst compiler flags for GCC (and Clang). Our
focus will be on flags used for embedded projects but the reasoning applies to other development environments as well. We will explore the impact
each flag has by walking through practical C code examples.







{:.no_toc}
