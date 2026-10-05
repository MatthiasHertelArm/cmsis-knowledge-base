---
id: "intr-differences-between-elf-32-and-elf-elf-internals"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: ELF Internals"
summary: "This post won’t detail the complete specification. For that task, I recommend these:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#elf-internals"
license: "CC-BY-SA-4.0"
mode: "V"
---

This post won’t detail the complete specification. For that task, I recommend
these:

- [https://blog.k3170makan.com/2018/09/introduction-to-elf-format-elf-header.html](https://blog.k3170makan.com/2018/09/introduction-to-elf-format-elf-header.html)
  Excellent series with some great illustrations highlighting the specific bytes
  belonging to parts of the ELF
- [https://cpu.land/becoming-an-elf-lord](https://cpu.land/becoming-an-elf-lord)
  A very fun overview focusing on how a program is actually run. Chapter 4
  focuses on ELFs
- [https://uclibc.org/docs/elf.pdf](https://uclibc.org/docs/elf.pdf) The
  original ELF-32 specification
- [https://uclibc.org/docs/elf-64-gen.pdf](https://uclibc.org/docs/elf-64-gen.pdf)
  The newer ELF-64 specification
