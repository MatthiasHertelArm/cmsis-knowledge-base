---
id: "intr-dealing-with-large-symbol-files-llvm-dwarfutil"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: `llvm-dwarfutil`"
summary: "An interesting tool that can be used to clean up / optimize debugging information in ELF files:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#llvm-dwarfutil"
license: "CC-BY-SA-4.0"
mode: "V"
---

An interesting tool that can be used to clean up / optimize debugging
information in ELF files:

https://llvm.org/docs/CommandGuide/llvm-dwarfutil.html

Usage is pretty straightforward:

```bash
❯ llvm-dwarfutil-20 hello.debug hello.debug.dwarfutil
❯ ll -h hello.debug*
-rwxrwxr-x 1 noah noah 44K Aug 29 11:23 hello.debug
-rwxrwxr-x 1 noah noah 19K Aug 29 11:23 hello.debug.dwarfutil
```

We can see the file size reduces dramatically. Comparing `readelf -SW` output
side-by-side we can see which debug sections were impacted:

```plaintext
  [29] .debug_aranges    PROGBITS        0000000000000000 003036 000030 00      0   0  1
  [30] .debug_info       PROGBITS        0000000000000000 003066 0000b9 00      0   0  1
  [31] .debug_abbrev     PROGBITS        0000000000000000 00311f 000066 00      0   0  1
  [32] .debug_line       PROGBITS        0000000000000000 003185 0000f1 00      0   0  1
  [33] .debug_str        PROGBITS        0000000000000000 003276 0055d7 01  MS  0   0  1
  [34] .debug_line_str   PROGBITS        0000000000000000 00884d 00024c 01  MS  0   0  1
  [35] .debug_macro      PROGBITS        0000000000000000 008a99 001396 00      0   0  1
  [36] .symtab           SYMTAB          0000000000000000 009e30 000360 18     37  18  8
  [37] .strtab           STRTAB          0000000000000000 00a190 0001db 00      0   0  1
  [38] .shstrtab         STRTAB          0000000000000000 00a36b 000185 00      0   0  1
```

And after:

```plaintext
  [29] .symtab           SYMTAB          0000000000000000 003038 0002e8 18     30  13  8
  [30] .strtab           STRTAB          0000000000000000 003320 0001c0 00      0   0  1
  [31] .shstrtab         STRTAB          0000000000000000 0034e0 0001a7 00      0   0  1
  [32] .debug_line       PROGBITS        0000000000000000 003687 0000f1 00      0   0  1
  [33] .debug_aranges    PROGBITS        0000000000000000 003778 000030 00      0   0  1
  [34] .debug_macinfo    PROGBITS        0000000000000000 0037a8 000000 00      0   0  1
  [35] .debug_macro      PROGBITS        0000000000000000 0037a8 0000f7 00      0   0  1
  [36] .debug_info       PROGBITS        0000000000000000 00389f 000092 00      0   0  1
  [37] .debug_abbrev     PROGBITS        0000000000000000 003931 00005b 00      0   0  1
  [38] .debug_str        PROGBITS        0000000000000000 00398c 00025a 00      0   0  1
  [39] .debug_str_offsets PROGBITS        0000000000000000 003be6 00003c 00      0   0  1
  [40] .debug_line_str   PROGBITS        0000000000000000 003c22 000264 00      0   0  1
```
