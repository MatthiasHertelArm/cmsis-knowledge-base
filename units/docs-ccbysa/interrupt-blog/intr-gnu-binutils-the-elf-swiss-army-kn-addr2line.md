---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-addr2line"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / addr2line"
summary: "addr2line converts addresses back to function and line numbers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#addr2line"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`addr2line` converts addresses back to function and line numbers.

#### Useful Arguments

- `-a` To show the address which was decoded. This can be useful when decoding multiple addresses
  at once or using `addr2line` in a batch processing mode.
- `-f` To display the function name the address is in
- `-e <ELF>` To specify the executable to decode. (Otherwise, `addr2line` checks for `a.out` in the
  working directory and uses that.)

#### Example Usage

You can run it on a single address:

```bash
$ arm-none-eabi-addr2line -a -f -e build/zephyr/zephyr.elf 0x08000946
  0x08000946
_printk_dec_ulong
zephyr/lib/os/printk.c:465
```

or pipe a bunch of addresses in from stdin and get them all decoded at once

```bash
$ echo -e "0x8000946\n0x8000336" |
   arm-none-eabi-addr2line -a -f -e build/zephyr/zephyr.elf
0x08000946
_printk_dec_ulong
zephyr/lib/os/printk.c:465
0x08000336
__udivmoddi4
```
