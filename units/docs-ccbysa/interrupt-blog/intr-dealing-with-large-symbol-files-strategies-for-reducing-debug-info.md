---
id: "intr-dealing-with-large-symbol-files-strategies-for-reducing-debug-info"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Strategies for Reducing Debug Info"
summary: "Let's go through some techniques for reducing the debug info section sizes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#strategies-for-reducing-debug-info"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's go through some techniques for reducing the debug info section sizes.

### Remove Debug Info with `strip`

It's possible to entirely remove debug info after building, using the `strip`
binutil:

```bash
❯ strip hello.debug -o hello.strip
# now diff the original, non-debug build with the stripped build
❯ diff -duw <(size -Ax hello) <(size -Ax hello.strip)
```

```diff
--- /proc/self/fd/13    2022-03-02 13:43:27.298081401 -0500
+++ /proc/self/fd/15    2022-03-02 13:43:27.298081401 -0500
@@ -1,4 +1,4 @@
-hello  :
+hello.strip  :
 section               size     addr
 .interp               0x1c    0x318
 .note.gnu.property    0x30    0x338
```

The debug data is entirely removed from the binary:

```bash
❯ ls -l hello*
-rwxrwxr-x 1 noah noah     15952 Mar  2 12:26 hello
-rw-rw-r-- 1 noah noah        90 Mar  2 12:25 hello.c
-rwxrwxr-x 1 noah noah     42336 Mar  2 12:30 hello.debug
-rwxrwxr-x 1 noah noah     14464 Mar  2 13:43 hello.strip
```

The stripped binary is actually a bit smaller than the one compiled without
debug sections (stripping that binary results in an identical file size).
Identifying the additional data that's been stripped is left for a future
exercise 😬.

Since the debug info is removed, as in the original binary, it's no longer
possible to get rich backtraces etc. when debugging the binary.

### Extract Debug Info with `objcopy`

It's possible to copy the debug info sections into a separate file using
`objcopy`:

```bash
❯ objcopy --only-keep-debug hello.debug hello.debug.dbg
❯ ls -lh hello.debug*
-rwxrwxr-x 1 noah noah 42K Mar  2 12:30 hello.debug
-rwxrwxr-x 1 noah noah 31K Mar  2 14:00 hello.debug.dbg
```

Note that the section headers for the non-debug sections are still present in
the file, so using `size` to examine the binary will show deceptive information
(eg, `.text`, `.data`, etc). From the manual:

> Note - the section headers of the stripped sections are preserved, including
> their sizes, but the contents of the section are discarded. The section
> headers are preserved so that other tools can match up the debuginfo file with
> the real executable, even if that executable has been relocated to a different
> address space.

You can then strip the debug binary:

```bash
❯ strip -o hello.debug.stripped hello.debug
```

And in GDB, you can manually load a symbol file:

```bash
Reading symbols from hello.debug.stripped...
(No debugging symbols found in hello.debug.stripped)
>>> symbol-file hello.debug.dbg  # using this command to load the symbol file
Reading symbols from hello.debug.dbg...
```

From the same manual page, it's suggested to add a debuglink so gdb can
automatically locate the debug information:

```bash
objcopy --add-gnu-debuglink=hello.debug.dbg hello.debug.stripped
```

Then GDB auto-loads the debug info file:

```bash
Reading symbols from hello.debug.stripped...
Reading symbols from /home/noah/dev/test/misc/hello.debug.dbg...
```

This only works if the position of the files remains consistent.

> Note that there's a newish approach to using debug info files called
> `debuginfod`, which enables GCC to retrieve debug info from a remote host. You
> can read more about that here:
> <https://developers.redhat.com/blog/2019/10/14/introducing-debuginfod-the-elfutils-debuginfo-server>

### Compress Debug Info with `objcopy --compress-debug-sections`

Instead of `strip`ing or splitting out the debug info, it can be compressed
in-place:

```bash
❯ objcopy --compress-debug-sections hello.debug hello.debug.compressed
❯ ls -lh hello.debug*
-rwxrwxr-x 1 noah noah 42K Mar  2 12:30 hello.debug
-rwxrwxr-x 1 noah noah 26K Mar  2 14:09 hello.debug.compressed
```

The binary size is greatly reduced, even for a small program like this (still
quite a bit larger than the stripped binary though).

View of the debug info section reduction:

```bash
❯ diff -duw <(size -Ax hello.debug) <(size -Ax hello.debug.compressed)
```

```diff
--- /proc/self/fd/13    2022-03-02 14:09:36.028276594 -0500
+++ /proc/self/fd/15    2022-03-02 14:09:36.024276703 -0500
@@ -1,4 +1,4 @@
-hello.debug  :
+hello.debug.compressed  :
 section                size     addr
 .interp                0x1c    0x318
 .note.gnu.property     0x30    0x338
@@ -28,12 +28,12 @@
 .bss                    0x8   0x4010
 .comment               0x25      0x0
 .debug_aranges         0x30      0x0
-.debug_info            0xb9      0x0
+.debug_info            0x98      0x0
 .debug_abbrev          0x66      0x0
-.debug_line            0xe8      0x0
-.debug_str           0x4e94      0x0
-.debug_line_str       0x1f5      0x0
-.debug_macro         0x1233      0x0
-Total                0x6cdc
+.debug_line            0xb6      0x0
+.debug_str           0x1853      0x0
+.debug_line_str       0x103      0x0
+.debug_macro          0xabe      0x0
+Total                0x2de1
```

We can see the `.debug_str` section is most aggressively reduced, but all around
improvement.

There shouldn't be a significant performance hit when loading a compressed vs.
uncompressed binary into GDB; on my computer, it's a few ms for this small
program (using the excellent [hyperfine](https://github.com/sharkdp/hyperfine)
benching tool):

```bash
❯ hyperfine 'gdb -batch -ex quit hello.debug' 'gdb -batch -ex quit hello.debug.compressed'
Benchmark 1: gdb -batch -ex quit hello.debug
  Time (mean ± σ):     418.8 ms ±   9.3 ms    [User: 350.2 ms, System: 67.6 ms]
  Range (min … max):   399.8 ms … 428.9 ms    10 runs

Benchmark 2: gdb -batch -ex quit hello.debug.compressed
  Time (mean ± σ):     425.9 ms ±  14.7 ms    [User: 365.6 ms, System: 60.0 ms]
  Range (min … max):   407.7 ms … 451.3 ms    10 runs

Summary
  'gdb -batch -ex quit hello.debug' ran
    1.02 ± 0.04 times faster than 'gdb -batch -ex quit hello.debug.compressed'
```

With larger files it might be more significant, but I haven't tested that.

Note that it's possible to _decompress_ the debug sections with `objcopy` using
the `--decompress-debug-sections` flag.

### Compress Debug Info when Linking

GNU `ld` and LLVM's `lld` support the `--compress-debug-sections=zlib` option,
which performs the debug section compression when generating the binary rather
than after the fact as in `objcopy --compress-debug-sections`:

<https://sourceware.org/binutils/docs-2.39/ld/Options.html#index-_002d_002dcompress_002ddebug_002dsections_003dzlib>

This gives pretty equivalent results as doing it post-build, and is a great
option to enable if you prefer always-compressed debug info.
