---
id: "intr-dealing-with-large-symbol-files-analyzing-binaries-for-bloat-using-bloat"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Analyzing Binaries for Bloat Using `bloaty`"
summary: "An interesting tool for examining binary bloat is bloaty:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#analyzing-binaries-for-bloat-using-bloaty"
license: "CC-BY-SA-4.0"
mode: "V"
---

An interesting tool for examining binary bloat is `bloaty`:

<https://github.com/google/bloaty>

It's pretty straightforward to build, I followed the instructions here:

<https://github.com/google/bloaty#install>

It has a nice diff view, for example:

```bash
# run bloaty on the cmake binary with debug symbols.
# this output should look pretty similar to 'size -Ax'
❯ ~/dev/github/bloaty/build/bloaty bin/cmake
    FILE SIZE        VM SIZE
 --------------  --------------
  68.2%   121Mi   0.0%       0    .debug_info
  11.2%  19.9Mi   0.0%       0    .debug_str
   5.9%  10.5Mi  71.9%  10.5Mi    .text
   5.1%  9.04Mi   0.0%       0    .strtab
   3.5%  6.28Mi   0.0%       0    .debug_line
   1.2%  2.21Mi  15.1%  2.21Mi    .eh_frame
   1.2%  2.08Mi   0.0%       0    .symtab
   1.0%  1.81Mi   0.0%       0    .debug_abbrev
   1.0%  1.73Mi   0.0%       0    .debug_aranges
   0.7%  1.17Mi   0.0%       0    .debug_rnglists
   0.4%   724Ki   4.8%   724Ki    .rodata
   0.3%   543Ki   3.6%   543Ki    .eh_frame_hdr
   0.2%   307Ki   2.0%   307Ki    .gcc_except_table
   0.1%   149Ki   1.0%   149Ki    .rela.dyn
   0.0%  63.4Ki   0.4%  63.4Ki    .data.rel.ro
   0.0%  60.4Ki   0.0%       0    .debug_line_str
   0.0%  59.9Ki   0.3%  49.5Ki    [24 Others]
   0.0%       0   0.3%  49.8Ki    .bss
   0.0%  23.4Ki   0.2%  23.4Ki    .dynstr
   0.0%  21.4Ki   0.1%  21.4Ki    .dynsym
   0.0%  19.4Ki   0.1%  19.4Ki    .rela.plt
 100.0%   178Mi 100.0%  14.6Mi    TOTAL

# now run it against the compressed debug info version, and
# also passing a '-- BASE_FILE' to show the difference
❯ ~/dev/github/bloaty/build/bloaty cmake.compressed -- bin/cmake
    FILE SIZE        VM SIZE
 --------------  --------------
  +8.1%      +3  [ = ]       0    .comment
 -85.3% -51.5Ki  [ = ]       0    .debug_line_str
 -66.6%  -801Ki  [ = ]       0    .debug_rnglists
 -78.2% -1.35Mi  [ = ]       0    .debug_aranges
 -79.1% -1.43Mi  [ = ]       0    .debug_abbrev
 -68.1% -4.28Mi  [ = ]       0    .debug_line
 -89.8% -17.9Mi  [ = ]       0    .debug_str
 -53.2% -64.7Mi  [ = ]       0    .debug_info
 -50.7% -90.5Mi  [ = ]       0    TOTAL
```

It's pretty handy for quickly examining binaries, but has a lot of other
features for pretty deep analysis, check out the manual here:

<https://github.com/google/bloaty/blob/master/doc/using.md>
