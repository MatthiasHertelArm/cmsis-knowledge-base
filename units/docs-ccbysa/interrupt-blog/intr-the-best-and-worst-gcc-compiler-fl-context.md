---
id: "intr-the-best-and-worst-gcc-compiler-fl-context"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: Context"
summary: "For any embedded software project, three aspects typically crucial for success are:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#context"
license: "CC-BY-SA-4.0"
mode: "V"
---

For any embedded software project, three aspects typically crucial for success are:

- Catching common programmatic errors before executing any code
- Generating a binary that is debuggable
- Minimizing code size and RAM usage

The flags presented in this article were chosen based on how much they have aided or hindered
working towards these goals on projects I've been involved with.

{:.no_toc}
