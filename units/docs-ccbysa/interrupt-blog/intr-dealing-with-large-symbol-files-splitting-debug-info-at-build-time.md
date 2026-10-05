---
id: "intr-dealing-with-large-symbol-files-splitting-debug-info-at-build-time"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Splitting Debug Info at Build Time"
summary: "GCC and Clang both support an option to split out DWARF info when compiling source files into object files:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#splitting-debug-info-at-build-time"
license: "CC-BY-SA-4.0"
mode: "V"
---

GCC and Clang both support an option to split out DWARF info when compiling
source files into object files:

<https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Debugging-Options.html#index-gsplit-dwarf>

Here's an example:

```bash
# compile + link with '-gsplit-dwarf'
❯ gcc -ggdb3 -gsplit-dwarf hello.c -o hello.debug

# examine file sizes- note the .dwo file,
# and the smaller hello.debug file size
❯ ls -l hello.debug*
-rwxrwxr-x 1 noah noah 17776 Mar  2 18:03 hello.debug
-rw-rw-r-- 1 noah noah 31208 Mar  2 18:03 hello.debug-hello.dwo

# test that symbols are working correctly
❯ gdb -batch --ex 'info line main' hello.debug
threads module disabled
Line 3 of "hello.c" starts at address 0x1149 <main> and ends at 0x115c <main+19>.

# delete the dwo file and retest
❯ rm hello.debug-hello.dwo
❯ gdb -batch --ex 'info line main' hello.debug
threads module disabled

warning: Could not find DWO CU hello.debug-hello.dwo(0xef39648d198fbc2d) referenced by CU at offset 0x0 [in module /home/noah/dev/test/misc/hello.debug]
Dwarf Error: unexpected tag 'DW_TAG_skeleton_unit' at offset 0x0 [in module /home/noah/dev/test/misc/hello.debug]
No line number information available for address 0x1149 <main>
```

This has a couple of advantages:

- small (essentially stripped) binaries are produced without post-processing
- link times can be dramatically improved, because the linker has to load _much_
  less data when it `memmap`'s the input object files

The disadvantage is you'll need to keep those `.dwo` files around in order for
GDB to locate them when you load the binary, and they're not very portable.

In theory there is the `dwp` tool to pack up the `.dwo` files into a single
archive that can be shipped with the binary, but I had a bad time trying to get
it to work 😞.

<https://gcc.gnu.org/wiki/DebugFissionDWP>
