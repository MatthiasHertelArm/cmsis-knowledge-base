---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-size"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / size"
summary: "size walks through the sections in the ELF and sums up the totals for all sections which are allocated. This can be useful for getting a quick summary of what the binary footprint looks like:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#size"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`size` walks through the sections in the ELF and sums up the totals for all sections which are
allocated. This can be useful for getting a quick summary of what the binary footprint looks like:

```bash
$ arm-none-eabi-size build/zephyr/zephyr.elf
text data bss dec hex filename
84340 2416 32157 118913 1d081 build/zephyr/zephyr.elf
```
