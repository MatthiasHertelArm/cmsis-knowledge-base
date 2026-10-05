---
id: "intr-pocket-article-how-to-implement-an-what-about-bootloaders"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM: What about bootloaders"
summary: "See some background information on bootloader operation here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory#what-about-bootloaders"
license: "CC-BY-SA-4.0"
mode: "V"
---

See some background information on bootloader operation here:

- [How to write a bootloader from scratch (The Interrupt)](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch)

Since a bootloader usually will use the same RAM regions as the application, we
need to make sure that the `NOINIT` region in the bootloader is similarly
reserved from its normal `RAM` region. This can be done by simply matching the
same `REGIONS` as in the application, ensuring nothing is placed into the
`NOINIT` regions:

```c
MEMORY
{
  FLASH  (rx)  : ORIGIN = 0x08000000, LENGTH = 1M
  RAM    (rwx) : ORIGIN = 0x20000000, LENGTH = 128K - 0x100
  /* the application relies on this noinit region being left alone! */
  NOINIT (rwx) : ORIGIN = 0x20000000 + 128K - 0x100, LENGTH = 0x100
}
```
