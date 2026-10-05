---
id: "intr-pocket-article-how-to-implement-an-memory-sections-in-an-embedded-program"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM: Memory sections in an embedded program"
summary: "A simple embedded application targeting the STM32F407VG would usually have these output sections in its memory map:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory#memory-sections-in-an-embedded-program"
license: "CC-BY-SA-4.0"
mode: "V"
---

A simple embedded application targeting the STM32F407VG would usually have these
output sections in its memory map:

```plaintext
❯ arm-none-eabi-size -Ax build/main.elf
build/main.elf  :
section                size         addr
.text                0x1314    0x8000000
.data                  0x78   0x20000000
.bss                   0xdc   0x20000078
```

Where:

- `.text` contains **read-only** data, such as executable code or `const` data
- `.data` contains _statically initialized_ **read-write** data (variables that
  have a non-zero initialization value)
- `.bss` contains _zero-initialized_ **read-write** data

When our program starts, the `.data` section will be loaded from the _load
address_ (LMA), and the `.bss` section will be set to all zeros, as part of the
program's startup code.
