---
id: "intr-gnu-build-ids-for-firmware-bundling-the-gnu-build-id-in-firmware-bi"
type: "concept"
domain: "debug"
title: "GNU Build IDs for Firmware: Bundling the GNU build ID in firmware bin files"
summary: "Getting the build ID in your executables on Linux is easy: they are ELF files!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-29-gnu-build-id-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-build-id-for-firmware#bundling-the-gnu-build-id-in-firmware-bin-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

Getting the build ID in your executables on Linux is easy: they are ELF files!
Firmware on the other hand typically deals with binaries which are assembled by
copying relevant sections of the elf at the right offset in a file.

This is typically accomplished with objcopy:
```terminal
$ arm-none-eabi-objcopy firmware.elf firmware.bin -O binary
```

This takes every elf section earmarked to be loaded and places them at
the correct offset in the bin file. In the process, most debug sections are stripped out.

Dumping the elf sections of the resulting `minimal.elf` gives us:

```
$ arm-none-eabi-objdump -h build/minimal.elf

build/minimal.elf:     file format elf32-littlearm

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .note.gnu.build-id 00000024  00000000  00000000  00010000  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  1 .text         000004e4  00000024  00000024  00010024  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  2 .bss          00000000  20000000  20000000  00000000  2**0
                  ALLOC
  3 .data         00000000  20000000  20000000  00010508  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  4 .stack        00002000  20000000  20000000  00020000  2**0
                  ALLOC
  5 .debug_info   00004076  00000000  00000000  00010508  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_abbrev 00000ac3  00000000  00000000  0001457e  2**0
                  CONTENTS, READONLY, DEBUGGING
  7 .debug_aranges 000000f8  00000000  00000000  00015041  2**0
                  CONTENTS, READONLY, DEBUGGING
  8 .debug_ranges 000000b8  00000000  00000000  00015139  2**0
                  CONTENTS, READONLY, DEBUGGING
  9 .debug_line   00000cfa  00000000  00000000  000151f1  2**0
                  CONTENTS, READONLY, DEBUGGING
 10 .debug_str    0000111a  00000000  00000000  00015eeb  2**0
                  CONTENTS, READONLY, DEBUGGING
 11 .comment      00000075  00000000  00000000  00017005  2**0
                  CONTENTS, READONLY
 12 .ARM.attributes 0000002c  00000000  00000000  0001707a  2**0
                  CONTENTS, READONLY
 13 .debug_frame  00000298  00000000  00000000  000170a8  2**2
                  CONTENTS, READONLY, DEBUGGING
```

As you can see, the `.text`, `.bss`, `.data`, `.stack` sections each have the
`LOAD` attribute, all others (including our `.note.gnu.build-id`) do not and will be
discarded.

To add a section to our binary, we must specify an address for it in our linker
script. Assuming your linker script declares the following memory layout:

```
MEMORY
{
  rom      (rx)  : ORIGIN = 0x00000000, LENGTH = 0x00040000
  ram      (rwx) : ORIGIN = 0x20000000, LENGTH = 0x00008000
}
```

You can add the build ID to your flash memory with:

```
.gnu_build_id :
{
  PROVIDE(g_note_build_id = .);
  *(.note.gnu.build-id)
} > rom
```

This instructs the linker to append the contents of `.note.gnu.build-id` to the
`rom` region of memory and create a symbol (`g_note_build_id`) to point to it.

Let's check our elf sections now:

```
$ arm-none-eabi-objdump -h build/minimal.elf

build/minimal.elf:     file format elf32-littlearm

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000004e4  00000000  00000000  00010000  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, CODE
  1 .gnu_build_id 00000024  000004e4  000004e4  000104e4  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  2 .bss          00000000  20000000  20000000  00000000  2**0
                  ALLOC
  3 .data         00000000  20000000  20000000  00010508  2**0
                  CONTENTS, ALLOC, LOAD, DATA
  4 .stack        00002000  20000000  20000000  00020000  2**0
                  ALLOC
  5 .debug_info   00004076  00000000  00000000  00010508  2**0
                  CONTENTS, READONLY, DEBUGGING
  6 .debug_abbrev 00000ac3  00000000  00000000  0001457e  2**0
                  CONTENTS, READONLY, DEBUGGING
  7 .debug_aranges 000000f8  00000000  00000000  00015041  2**0
                  CONTENTS, READONLY, DEBUGGING
  8 .debug_ranges 000000b8  00000000  00000000  00015139  2**0
                  CONTENTS, READONLY, DEBUGGING
  9 .debug_line   00000cfa  00000000  00000000  000151f1  2**0
                  CONTENTS, READONLY, DEBUGGING
 10 .debug_str    0000111a  00000000  00000000  00015eeb  2**0
                  CONTENTS, READONLY, DEBUGGING
 11 .comment      00000075  00000000  00000000  00017005  2**0
                  CONTENTS, READONLY
 12 .ARM.attributes 0000002c  00000000  00000000  0001707a  2**0
                  CONTENTS, READONLY
 13 .debug_frame  00000298  00000000  00000000  000170a8  2**2
                  CONTENTS, READONLY, DEBUGGING
```

As you can see, our build ID now has an address assigned to it and is marked
with the `LOAD` attribute.

**Note**: Make sure to declare the `.gnu_build_id` section after the `.text`
section, otherwise the build ID will be set to address `0x0` and the firmware
will not boot.
