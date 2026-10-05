---
id: "intr-differences-between-elf-32-and-elf"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64"
summary: "Have you ever wondered if ELF is portable between 32-bit and 64-bit targets? Probably not, but this might be a common scenario for you if you work on 32-bit embedded devices but use a 64-bit host."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences"
license: "CC-BY-SA-4.0"
mode: "V"
---

Have you ever wondered if ELF is portable between 32-bit and 64-bit targets?
Probably not, but this might be a common scenario for you if you work on 32-bit
embedded devices but use a 64-bit host. Or maybe you've developed tooling for
32-bit MCUs and are transitioning to working on 64-bit targets.



The ELF object file format is one of the most commonly used today. Most build
systems provide an output to this format, and ELF is commonly used to output
coredumps. The format varies in subtle ways for 32-bit and 64-bit targets
though, which can present problems for tools supporting both. This post will
highlight the main differences and is intended as a quick reference for these
differences.
