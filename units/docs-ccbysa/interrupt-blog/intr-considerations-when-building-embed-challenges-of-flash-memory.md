---
id: "intr-considerations-when-building-embed-challenges-of-flash-memory"
type: "concept"
domain: "debug"
title: "Considerations when Building Embedded Databases: Challenges of Flash Memory"
summary: "Let's consider a few of the ways that flash differs from RAM from the C-programmer's perspective:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-24-choosing-or-building-an-embedded-db.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#challenges-of-flash-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's consider a few of the ways that flash differs from RAM from the
C-programmer's perspective:

1. First off, flash must be **erased** before it can be **programmed**. Erasing
   changes all bits to `1` while programming changes some bits to `0`. And
   although single bits may be programmed, only entire **pages** of flash may be
   erased.

2. These pages vary in size between flash chips and microcontrollers, from 512
   bytes to 32k, with 4k being a typical size.

3. Flash operations must be **aligned** to specific offsets, usually 32 bytes
   but this varies. The page size, alignment, and possibly restricted read/write
   lengths together are referred to as the flash **geometry**.

4. Flash has a limited number of program-erase cycles, typically 10k to 100k.
   So, to avoid premature failure, values that change many times per day must be
   distributed across different flash pages, a scheme known as "wear leveling".

5. Flash reading, programming, and especially erasing, is much slower than RAM
   operations. So frequently-accessed data must at least be cached in RAM.

These challenges mean that for non-trivial applications such as the smart home
hub where there are many small pieces of information to persist, there is a
clear need for a well-organized scheme for managing the use of the flash to save
and load this data. This is what we refer to as an **embedded database**.
