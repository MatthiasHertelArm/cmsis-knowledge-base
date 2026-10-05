---
id: "intr-dealing-with-large-symbol-files-building-with-debug-info-enabled"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Building With Debug Info Enabled"
summary: "Compile it with gcc hello.c -o hello, and let's take a look at the output size:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#building-with-debug-info-enabled"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's start with a small C program:

```c
#include <stdio.h>

int main(int argc, char **argv) {
  printf("hello!\n");
  return 0;
}
```

> Note: the example C file and a Makefile with the various `obcopy` and `ld`
> example invocations can be found here:
> <https://github.com/memfault/interrupt/blob/master/example/large-symbol-files/>

Compile it with `gcc hello.c -o hello`, and let's take a look at the output
size:

```bash
❯ size -Ax hello
hello  :
section               size     addr
.interp               0x1c    0x318
.note.gnu.property    0x30    0x338
.note.gnu.build-id    0x24    0x368
.note.ABI-tag         0x20    0x38c
.gnu.hash             0x24    0x3b0
.dynsym               0xa8    0x3d8
.dynstr               0x8d    0x480
.gnu.version           0xe    0x50e
.gnu.version_r        0x30    0x520
.rela.dyn             0xc0    0x550
.rela.plt             0x18    0x610
.init                 0x1b   0x1000
.plt                  0x20   0x1020
.plt.got              0x10   0x1040
.plt.sec              0x10   0x1050
.text                0x112   0x1060
.fini                  0xd   0x1174
.rodata                0xb   0x2000
.eh_frame_hdr         0x34   0x200c
.eh_frame             0xac   0x2040
.init_array            0x8   0x3db8
.fini_array            0x8   0x3dc0
.dynamic             0x1f0   0x3dc8
.got                  0x48   0x3fb8
.data                 0x10   0x4000
.bss                   0x8   0x4010
.comment              0x25      0x0
Total                0x7e9
```

Phew! lots of stuff in there. We can see a few typical sections like `.text`,
`.data`, `.bss`, and several other ones.

Overall file size of this binary is:

```bash
❯ ls -lh hello
-rwxrwxr-x 1 noah noah 16K Mar  2 12:26 hello
```

Wow, 16kB for printing `hello!`! 

Loading this executable into gdb, we get the following warning:

```bash
Reading symbols from hello...
(No debugging symbols found in hello)
```

🥺

Ok, let's now compile with debug information enabled. Checking the
[manual for GCC](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Debugging-Options.html),
we see several different options for debug information. Let's go with the
highest level, `ggdb3`:

```bash
❯ gcc -ggdb3 hello.c -o hello.debug
❯ ls -lh hello*
-rwxrwxr-x 1 noah noah  16K Mar  2 12:26 hello
-rw-rw-r-- 1 noah noah   90 Mar  2 12:25 hello.c
-rwxrwxr-x 1 noah noah  42K Mar  2 12:30 hello.debug
```

Ok, our 90 byte source file compiled to 16kB without debug information, and
**42kB** with debug information 😮!

Checking the section sizes again, we see some new sections prefixed with
`.debug_` that account for all of the added size:

```bash
# diff the result of the 'size' command for the 'hello' and 'hello.debug' files
❯ diff -duw <(size -Ax hello) <(size -Ax hello.debug)
```

```diff
--- /proc/self/fd/13    2022-03-02 12:34:14.796360776 -0500
+++ /proc/self/fd/15    2022-03-02 12:34:14.796360776 -0500
@@ -1,4 +1,4 @@
-hello  :
+hello.debug  :
 section               size     addr
 .interp               0x1c    0x318
 .note.gnu.property    0x30    0x338
@@ -27,6 +27,13 @@
 .data                 0x10   0x4000
 .bss                   0x8   0x4010
 .comment              0x25      0x0
-Total                0x7e9
+.debug_aranges         0x30      0x0
+.debug_info            0xb9      0x0
+.debug_abbrev          0x66      0x0
+.debug_line            0xe8      0x0
+.debug_str           0x4e94      0x0
+.debug_line_str       0x1f5      0x0
+.debug_macro         0x1233      0x0
+Total                0x6cdc
```

> Note: if you're using the `arm-none-eabi` tools from ARM, you might want to
> use those variants of the binutils referenced in this article (`size`,
> `strip`, `objcopy`), for example `arm-none-eabi-size` here instead of `size`
