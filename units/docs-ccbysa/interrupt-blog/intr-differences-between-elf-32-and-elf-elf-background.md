---
id: "intr-differences-between-elf-32-and-elf-elf-background"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: ELF Background"
summary: "If you’re running a program on a UNIX-ish system, you’re probably using an ELF file. If you’re building firmware for your MCU, it’s probably an ELF file targeted for your MCU architecture."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#elf-background"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you’re running a program on a UNIX-ish system, you’re probably using an ELF
file. If you’re building firmware for your MCU, it’s probably an ELF file
targeted for your MCU architecture. MacOS and Windows of course have their own
slightly different formats, Mach-O and Portable Executable. This format contains
information on loading your program into memory or linking with other object
files to form an executable object. Static libraries are ELFs. Compiling a
source file produces an ELF. Coredumps can be collected as ELFs. You might even
be an ELF 😱!
