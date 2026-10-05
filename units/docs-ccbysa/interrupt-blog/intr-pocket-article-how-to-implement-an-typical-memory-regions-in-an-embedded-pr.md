---
id: "intr-pocket-article-how-to-implement-an-typical-memory-regions-in-an-embedded-pr"
type: "concept"
domain: "debug"
title: "Pocket article: How to implement and use `.noinit` RAM: Typical memory regions in an embedded program"
summary: "For more background, see these references on linker scripts:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-11-23-noinit-memory.md"
doc_source: "https://interrupt.memfault.com/blog/noinit-memory#typical-memory-regions-in-an-embedded-program"
license: "CC-BY-SA-4.0"
mode: "V"
---

For more background, see these references on linker scripts:

- [From Zero to main(): Demystifying Firmware Linker Scripts](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware)
- [Stargirl Flower's _outstanding_ "The most thoroughly commented linker script
  (probably)"
  post](https://blog.thea.codes/the-most-thoroughly-commented-linker-script/)
- [Elecia White's (of embedded.fm !) excellent Memory Map talk](https://www.youtube.com/watch?v=XRXLUcbJIxY)

A typical small embedded device (running bare-metal or an RTOS) will usually
have two types of memory available:

- read-only memory (usually flash)
- read-write memory (usually SRAM)

For example, the STM32F407VG chip has:

- 1 megabyte of flash
- 192 kilobytes of SRAM

On that chip, flash and SRAM are mapped to the following addresses:

```plaintext
┌───────────────────┐0x0800 0000
│Flash (1024kB)     │
└────────┬──────────┘0x080F FFFF
        ...
┌────────┴──────────┐0x1000 0000
│CCM data RAM (64kB)│
└────────┬──────────┘0x1000 FFFF
        ...
┌────────┴──────────┐0x2000 0000
│SRAM (128kB)       │
└───────────────────┘0x2001 FFFF
```
