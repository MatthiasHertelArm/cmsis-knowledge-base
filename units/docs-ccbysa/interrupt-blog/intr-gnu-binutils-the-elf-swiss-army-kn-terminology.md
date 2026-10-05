---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-terminology"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: Terminology"
summary: "Introduced in the late 1980s as part of the Unix operating system, ELF has become the ubiquitous output format used by compilers for embedded development."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#terminology"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Executable and Linkable Format (ELF)

Introduced in the late 1980s as part of the Unix operating system, ELF has become the ubiquitous
output format used by compilers for embedded development. A full discussion of the ELF file format
is outside the scope of this article, but at a high level, it's a binary data format which holds
program data as well as debug information in different "sections". Since the format is well specified, many
tools have been developed to parse it.

It is easy to check if a file is an ELF format by
inspecting the first four bytes of the file where you should see `0x7f` followed by "ELF":

```bash
$ xxd -l4 <YOUR ELF FILE>
00000000: 7f45 4c46                                .ELF
```

Compilers and IDEs will sometimes use different extensions for ELF artifacts. The most common ones
you will see are `.elf`, `.out`, or `.axf`.

### DWARF

DWARF is a standardized format[^3] for representing debug information (i.e symbol names, struct
layouts, how to recover backtraces, etc). The format was developed in the late 1980s as
part of Unix System V Release 4 (SVR4):

> Fun Fact: "The name DWARF is something of a pun, since it was developed along with the ELF object file
> format. The name is an acronym for “Debugging With Arbitrary Record Formats”".[^2]

When a program is compiled with debug information enabled (e.g. with the `-g` CFLAG), this
information will be written into special `.debug_` ELF sections that look like:

```
$ readelf -S <ELF>
  ...
  [ 8] .debug_info       PROGBITS        00000000 0200f4 00980b 00      0   0  1
  [ 9] .debug_abbrev     PROGBITS        00000000 0298ff 001adf 00      0   0  1
  [10] .debug_loc        PROGBITS        00000000 02b3de 003bf7 00      0   0  1
  [11] .debug_aranges    PROGBITS        00000000 02efd5 0004f0 00      0   0  1
  [12] .debug_ranges     PROGBITS        00000000 02f4c5 0007d8 00      0   0  1
  [13] .debug_macro      PROGBITS        00000000 02fc9d 0031dd 00      0   0  1
  [14] .debug_line       PROGBITS        00000000 032e7a 005447 00      0   0  1
  [15] .debug_str        PROGBITS        00000000 0382c1 00dedd 01  MS  0   0  1
```

### stabs, COFF, XCOFF

While rather infrequent, if you are working with custom compilers (such as
those shipped with some DSPs), you may see binary or debug information emitted in alternative formats such as
stabs, COFF, or XCOFF. These are all legacy formats that have largely been superseded by ELF and
DWARF. I view it as a red-flag in the evaluation process if a vendor's compiler emits information in
these formats. At this point, a lot of binary inspection tools have deprecated support
for these formats, which makes it harder to debug and workaround issues on chips using them.
