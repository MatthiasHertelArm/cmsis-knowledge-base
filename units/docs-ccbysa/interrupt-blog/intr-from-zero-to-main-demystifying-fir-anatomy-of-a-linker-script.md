---
id: "intr-from-zero-to-main-demystifying-fir-anatomy-of-a-linker-script"
type: "concept"
domain: "debug"
title: "From Zero to main(): Demystifying Firmware Linker Scripts: Anatomy of a Linker Script"
summary: "From Zero to main(): Demystifying Firmware Linker Scripts: Anatomy of a Linker Script"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-25-how-to-write-linker-scripts-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#anatomy-of-a-linker-script"
license: "CC-BY-SA-4.0"
mode: "V"
---

A linker script contains four things:

- Memory layout: what memory is available where
- Section definitions: what part of a program should go where
- Options: commands to specify architecture, entry point, ...etc. if needed
- Symbols: variables to inject into the program at link time
