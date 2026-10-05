---
id: "intr-code-size-optimization-gcc-compile-c-library"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: C Library"
summary: "The C library often times takes a non trivial amount of code space. Looking at our example program, we can see multiple libc symbols in list of the 30 largest symbols:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#c-library"
license: "CC-BY-SA-4.0"
mode: "V"
---

The C library often times takes a non trivial amount of code space. Looking at
our example program, we can see multiple libc symbols in list of the 30 largest
symbols:

```
$ arm-none-eabi-nm --print-size --size-sort --radix=d build/ch.elf | tail -30
[...]
134218584 00000442 T strcmp
[...]
134235240 00000664 T chvprintf.
[...]
```

Those two symbols alone represent 1KiB of code space!

By default, `arm-none-eabi-gcc` ships with newlib[^4], a libc implementation
optimized for embedded systems. While newlib is quite small, ARM added a slimmed
down version of newlib dubbed “newlib-nano”, which does away with some C99
features and rewrites part of the library directly in thumb code to shrink its
size. You can read more about newlib nano on ARM’s website[^6].

Libc selection in GCC is implemented with specs files. I won’t go into too many
details, but the easiest way to think about specs files is that they are CFLAGS
and LDFLAGS which are conveniently bundled into a single configuration. You can
find the spec file for newlib-nano on
GitHub[^5].

In order to use newlib nano, we add the spec file to our flags:
```
CFLAGS += --specs=nano.specs
LDFLAGS += --specs=nano.specs
```

Recompiling our example with newlib-nano gives us:
```
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  50450	    228	  98072	 148750	  2450e	build/ch.elf
Creating build/ch.list
```

Almost 2KiB saved!
