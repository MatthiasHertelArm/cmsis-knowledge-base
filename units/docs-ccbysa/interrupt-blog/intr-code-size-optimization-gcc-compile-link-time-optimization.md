---
id: "intr-code-size-optimization-gcc-compile-link-time-optimization"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: Link-time optimization"
summary: "While linkers do not traditionally do much optimizing, this has started to change. Nowadays, all the major compilers offer Link Time Optimization or LTO."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#link-time-optimization"
license: "CC-BY-SA-4.0"
mode: "V"
---

While linkers do not traditionally do much optimizing, this has started to
change. Nowadays, all the major compilers offer Link Time Optimization or LTO.
LTO enables optimizations that are not available to the compiler as they touch
multiple compilation units at once.

LTO comes with a few drawbacks:
1. compilation time - even for simple programs the difference in build time will
   be noticeable, some of your colleagues may complain about it!
2. debug-ability - Newer versions of debuggers like GDB and LLDB do a much
   better job of coping with LTO however, and while there is still an impact it is not dramatic.
3. higher stack usage - more aggressive inlining can use more stack memory and
   lead to overflows.

Enabling LTO is as simple as passing the `-flto` flag to both the compilation
and link steps:

```makefile
CFLAGS += -flto
LDFLAGS += -flto
```

ChibiOS once again has a build variable for it (`USE_LTO`), so we run:
```
$ make USE_LINK_GC=yes USE_LTO=yes
```

And get the following output:
```
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  51960	    228	  98072	 150260	  24af4	build/ch.elf
Creating build/ch.list
```

To get an idea of the difference in compile time, we can use the `time` command
on OSX:

Before:
```
$ time make USE_LINK_GC=yes USE_LTO=no
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  54828	    228	  98072	 153128	  25628	build/ch.elf
Creating build/ch.list

Done

real	0m27.462s
user	0m23.545s
sys	0m2.752s
```

After:
```
$ time make USE_LINK_GC=yes USE_LTO=yes
[...]
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  51960	    228	  98072	 150260	  24af4	build/ch.elf
Creating build/ch.list

Done

real	0m32.865s
user	0m26.861s
sys	0m3.386s
```

So we traded 5 seconds of build time for ~3KiB of code space.

> Note: /u/xenoamor on Reddit[^7] pointed out that in some cases, LTO is dropping
> vector tables even when the KEEP command is used. You can find more details,
> as well as a workaround on Launchpad[^8].
