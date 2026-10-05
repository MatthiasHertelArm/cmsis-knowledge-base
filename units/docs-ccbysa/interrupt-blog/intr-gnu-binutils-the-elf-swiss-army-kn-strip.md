---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-strip"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / strip"
summary: "As the name implies, strip removes sections from an ELF. Most commonly you will see it used for stripping things like debug info from an ELF."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#strip"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

As the name implies, `strip` removes sections from an ELF. Most commonly you will see it used for
stripping things like debug info from an ELF. If you are distributing your ELF files, stripping
debug information can make it harder to reverse engineeryour code. Here is an example:

```
# Confirm ELF originally has debug info
$ arm-none-eabi-readelf -S nrf52_example/build/nrf52.elf | grep debug
  [ 8] .debug_info       PROGBITS        00000000 0200f4 00980b 00      0   0  1
  [ 9] .debug_abbrev     PROGBITS        00000000 0298ff 001adf 00      0   0  1
  [10] .debug_loc        PROGBITS        00000000 02b3de 003bf7 00      0   0  1
  [11] .debug_aranges    PROGBITS        00000000 02efd5 0004f0 00      0   0  1
  [12] .debug_ranges     PROGBITS        00000000 02f4c5 0007d8 00      0   0  1
  [13] .debug_macro      PROGBITS        00000000 02fc9d 0031dd 00      0   0  1
  [14] .debug_line       PROGBITS        00000000 032e7a 005447 00      0   0  1
  [15] .debug_str        PROGBITS        00000000 0382c1 00dedb 01  MS  0   0  1
  [18] .debug_frame      PROGBITS        00000000 046248 000d8c 00      0   0  4

# Remove debug info
$ arm-none-eabi-strip -g nrf52_example/build/nrf52.elf

# Confirm ELF no longer has debug info
$ arm-none-eabi-readelf -S nrf52_example/build/nrf52.elf | grep debug
```
