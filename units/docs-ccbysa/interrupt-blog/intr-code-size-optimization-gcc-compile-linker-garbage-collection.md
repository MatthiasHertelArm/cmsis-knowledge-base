---
id: "intr-code-size-optimization-gcc-compile-linker-garbage-collection"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: Linker Garbage Collection"
summary: "Now that we’ve set the appropriate optimization level, we turn our attention to dead code elimination. Most programs contain dead code: it may come from libraries you use partially, or test functions you left in the final program."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#linker-garbage-collection"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we’ve set the appropriate optimization level, we turn our attention to
dead code elimination. Most programs contain dead code: it may come from
libraries you use partially, or test functions you left in the final program.

Since the compiler operates on one file at a time, it does not have enough
context to decide whether a function is dead code or not. Consider a library
which exposes a function to add numbers in an array: while nothing in the
library itself may call this function, the compiler has no way of knowing if
other files are using it.

The linker on the other hand has visibility into our whole program, so this is
the stage where dead code could be identified and removed. Unfortunately,
linkers do not perform optimizations by default.

To enable dead code optimization on GCC, you need two things: the compiler needs
to split each function into its own linker section so the linker knows where
each function is, and the linker needs to add an optimization pass to remove
sections that are not called by anything.

This is achieved with the `-ffunction-sections`  compile-time flag and the
`-gc-sections` link-time flag. A similar process can take place with dead data
and the `-fdata-sections` flag.

In a Makefile, it looks like this:
```makefile
CFLAGS += -ffunction-sections -fdata-sections
LDFLAGS += -Wl,--gc-sections
```

ChibiOS sets those when the `USE_LINK_GC` variable is set, so we call:
```bash
$ make USE_LINK_GC=yes USE_LTO=no
```

And get:
```bash
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  54828	    228	  98072	 153128	  25628	build/ch.elf
Creating build/ch.list
```

So dead code elimination yields close to another 10KiB!

### Preventing some symbols from being garbage collected

In some cases, you may want some code that is not explicitly called by anything
else to remain in your program. One such example is interrupt handlers: while it
may look to the linker like they are not called, the hardware will jump to those
addresses and expect the code to be there.

The linker provides the `KEEP` command to identify sections that should be kept.
For interrupts, the typical solution is to put your vector table in a section
called `vectors` and mark it in the linker script:

```
    .text :
    {
        KEEP(*(.vectors .vectors.*))
  	      [...]
    } > rom
```
