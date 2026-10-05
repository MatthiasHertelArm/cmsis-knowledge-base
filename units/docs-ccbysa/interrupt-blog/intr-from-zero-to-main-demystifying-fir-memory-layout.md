---
id: "intr-from-zero-to-main-demystifying-fir-memory-layout"
type: "concept"
domain: "debug"
title: "From Zero to main(): Demystifying Firmware Linker Scripts: Memory Layout"
summary: "In order to allocate program space, the linker needs to know how much memory is available, and at what addresses that memory exists. This is what the MEMORY definition in the linker script is for."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-06-25-how-to-write-linker-scripts-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#memory-layout"
license: "CC-BY-SA-4.0"
mode: "V"
---

In order to allocate program space, the linker needs to know how much memory is
available, and at what addresses that memory exists. This is what the `MEMORY`
definition in the linker script is for.

The syntax for MEMORY is defined in the [binutils
docs](https://sourceware.org/binutils/docs/ld/MEMORY.html#MEMORY) and is as follow:

```
MEMORY
  {
    name [(attr)] : ORIGIN = origin, LENGTH = len
    …
  }
```

Where

- `name` is a name you want to use for this region. Names do not carry meaning,
  so you're free to use anything you want. You'll often find "flash", and "ram"
  as region names.
- `(attr)` are optional attributes for the region, like whether it's writable
  (`w`), readable (`r`), or executable (`x`). Flash memory is usually `(rx)`,
  while ram is `rwx`. Marking a region as non-writable does not magically make it
  write protected: these attributes are meant to describe the properties of the
  memory, not set it.
- `origin` is the start address of the memory region.
- `len` is the size of the memory region, in bytes.

The memory map for the SAMD21G18 chip we've got on our board can be found in its
[datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/SAMD21-Family-DataSheet-DS40001882D.pdf)
in table 10-1, reproduced below.



| Memory | Start Address | Size |
|---|---|---|
| Internal Flash | 0x00000000 | 256 Kbytes |
| Internal SRAM | 0x20000000 | 32 Kbytes |





Transcribed into a `MEMORY` definition, this gives us:

```
MEMORY
{
  rom      (rx)  : ORIGIN = 0x00000000, LENGTH = 0x00040000
  ram      (rwx) : ORIGIN = 0x20000000, LENGTH = 0x00008000
}
```
