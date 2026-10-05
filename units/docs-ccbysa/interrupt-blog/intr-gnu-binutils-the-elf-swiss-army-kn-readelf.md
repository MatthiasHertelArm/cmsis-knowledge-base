---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-readelf"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / readelf"
summary: "readelf lets us get overall summaries of the different sections of an ELF."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#readelf"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`readelf` lets us get overall summaries of the different sections of an ELF.

#### Dumping Sections in an ELF

With the `-S` option, we can see the sections that will be included in the final binary as well as sections with special
information such as the `.debug_*` or `NOTE` sections.

```bash
$ arm-none-eabi-readelf -S nrf52_example/build/nrf52.elf
There are 22 section headers, starting at offset 0x48e7c:

Section Headers:
  [Nr] Name              Type            Addr     Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            00000000 000000 000000 00      0   0  0
  [ 1] .interrupts       PROGBITS        00000000 010000 000048 00   A  0   0  4
  [ 2] .gnu_build_id     NOTE            00000048 010048 000024 00   A  0   0  4
  [ 3] .text             PROGBITS        00000070 010070 001858 00  AX  0   0 16
  [ 4] .data             PROGBITS        20000000 020000 0000f4 00  WA  0   0  4
  [ 5] .bss              NOBITS          200000f4 0200f4 0029a4 00  WA  0   0  4
  [ 6] .heap             PROGBITS        20002a98 0200f4 000000 00   W  0   0  1
  [ 7] .stack            NOBITS          20002a98 0200f4 000400 00  WA  0   0  1
  [ 8] .debug_info       PROGBITS        00000000 0200f4 00980b 00      0   0  1
  [ 9] .debug_abbrev     PROGBITS        00000000 0298ff 001adf 00      0   0  1
  [10] .debug_loc        PROGBITS        00000000 02b3de 003bf7 00      0   0  1
  [11] .debug_aranges    PROGBITS        00000000 02efd5 0004f0 00      0   0  1
  [12] .debug_ranges     PROGBITS        00000000 02f4c5 0007d8 00      0   0  1
  [13] .debug_macro      PROGBITS        00000000 02fc9d 0031dd 00      0   0  1
  [14] .debug_line       PROGBITS        00000000 032e7a 005447 00      0   0  1
  [15] .debug_str        PROGBITS        00000000 0382c1 00dedd 01  MS  0   0  1
  [16] .comment          PROGBITS        00000000 04619e 000079 01  MS  0   0  1
  [17] .ARM.attributes   ARM_ATTRIBUTES  00000000 046217 000032 00      0   0  1
  [18] .debug_frame      PROGBITS        00000000 04624c 000d8c 00      0   0  4
  [19] .symtab           SYMTAB          00000000 046fd8 0014c0 10     20 265  4
  [20] .strtab           STRTAB          00000000 048498 000905 00      0   0  1
  [21] .shstrtab         STRTAB          00000000 048d9d 0000df 00      0   0  1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  y (purecode), p (processor specific)
```

#### Dumping Compiler ABI Info

Every MCU architecture has an Application Binary Interface (ABI). An ABI details things such as
which registers to use for passing arguments and which ones must be preserved across function
calls. Sometimes, a given architecture may have several ABI configuration options which can be
selected via compiler flags. For example, on ARMv7-m, there are two different ABIs which can be used
for passing floating point arguments as parameters. One which passes arguments in "VFP" registers
and one which uses general purpose registers[^5]. We can discover which options are used along with
some other information by using readelf's `-A` argument:

```bash
$ arm-none-eabi-readelf -A nrf52_example/build/nrf52.elf
Attribute Section: aeabi
File Attributes
  Tag_CPU_name: "7E-M"
  Tag_CPU_arch: v7E-M
  Tag_CPU_arch_profile: Microcontroller
  Tag_THUMB_ISA_use: Thumb-2
  Tag_FP_arch: VFPv4-D16
  Tag_ABI_PCS_wchar_t: 4
  Tag_ABI_FP_denormal: Needed
  Tag_ABI_FP_exceptions: Needed
  Tag_ABI_FP_number_model: IEEE 754
  Tag_ABI_align_needed: 8-byte
  Tag_ABI_enum_size: small
  Tag_ABI_HardFP_use: SP only
  Tag_ABI_VFP_args: VFP registers
  Tag_ABI_optimization_goals: Aggressive Size
  Tag_CPU_unaligned_access: v6
```

#### Dumping DWARF Information

A DWARF section is comprised of a sequence of "Debugging Information Entries" referred to as
DIEs. You can use `readelf` to dump a human readable representation of all the debug information in
the ELF:

```bash
$ arm-none-eabi-readelf --debug-dump nrf52_example/build/nrf52.elf
  Compilation Unit @ offset 0x0:
   Length:        0x4f9 (32-bit)
   Version:       4
   Abbrev Offset: 0x0
   Pointer Size:  4
 <0><b>: Abbrev Number: 1 (DW_TAG_compile_unit)
    <c>   DW_AT_producer    : (indirect string, offset: 0x2cc5): GNU C17 9.2.1 20191025 (release) [ARM/arm-9-branch revision 277599] -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -mthumb -march=armv7e-m+fp -g3 -Os -ffunction-sections -fdata-sections
    <10>   DW_AT_language    : 12       (ANSI C99)
    <11>   DW_AT_name        : (indirect string, offset: 0x4576): main.c
    <15>   DW_AT_comp_dir    : (indirect string, offset: 0x3692): example/best-of-binutils
    <19>   DW_AT_ranges      : 0x18
    <1d>   DW_AT_low_pc      : 0x0
    <21>   DW_AT_stmt_list   : 0x0
    <25>   DW_AT_GNU_macros  : 0x0
[...]
```

#### Auditing Compiler Flag Settings

There are certain DIEs that are often interesting to look at in isolation. For example, you can
look at `DW_AT_producer` DIE on GCC and Clang to see the compiler flags which were used.

```
$ arm-none-eabi-readelf --debug-dump nrf52_example/build/nrf52.elf |
   grep DW_AT_producer.*:

    <c>   DW_AT_producer    :
    (indirect string, offset: 0x2cc5): GNU C17 9.2.1 20191025 (release)
    [ARM/arm-9-branch revision 277599]
    -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -mthumb
    -march=armv7e-m+fp -g3 -Os -ffunction-sections -fdata-sections
```

> NOTE: For more details about good compiler flag settings for embedded devices in general, check out our
> post on the topic [here](https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags).

#### Read the GNU Build ID

When using a GNU Build ID, the `-n` option can be used to quickly
print note sections and see the value.

```bash
$ arm-none-eabi-readelf -n nrf52_example/build/nrf52.elf

Displaying notes found in: .gnu_build_id
  Owner                Data size    Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
  Build ID: c61acc0ab0602a9f53bcc36b91d017834129fea1
```

> NOTE: To learn more about GNU Build IDs and how to easily add one to your project, check out
> [this article](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware).
