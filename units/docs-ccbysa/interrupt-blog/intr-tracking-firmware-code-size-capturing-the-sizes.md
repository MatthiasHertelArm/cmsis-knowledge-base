---
id: "intr-tracking-firmware-code-size-capturing-the-sizes"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Capturing the Sizes"
summary: "To get a generic code size calculation, we can use size, or in the case of this blog post, arm-none-eabi-size. This captures the text, data, and bss region code sizes and prints them to the terminal."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#capturing-the-sizes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

To get a generic code size calculation, we can use `size`, or in the case of
this blog post, `arm-none-eabi-size`. This captures the `text`, `data`, and
`bss` region code sizes and prints them to the terminal.

```
$ arm-none-eabi-size zephyr/zephyr.elf
   text    data     bss     dec     hex filename
 130780    3356   21167  155303   25ea7 build/zephyr/zephyr.elf
```

There are a [number of ways to
capture](https://interrupt.memfault.com/blog/best-firmware-size-tools) this data,
and some projects or teams want to track other data important to them. These
might include specific linker region sizes, resource pack size (fonts, images,
etc), or possibly the largest 10 files or symbols in the codebase. Whatever is
important to you and your team, track it!
