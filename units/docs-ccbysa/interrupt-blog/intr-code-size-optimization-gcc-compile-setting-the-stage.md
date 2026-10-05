---
id: "intr-code-size-optimization-gcc-compile-setting-the-stage"
type: "concept"
domain: "debug"
title: "Code Size Optimization: GCC Compiler Flags: Setting the stage"
summary: "In order to get measurable improvements in code size, we need a reasonably large code-base to begin with. To that end, we’ll use example code from ChibiOS[^1], a free and open source RTOS."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-20-code-size-optimization-gcc-flags.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags#setting-the-stage"
license: "CC-BY-SA-4.0"
mode: "V"
---

In order to get measurable improvements in code size, we
need a reasonably large code-base to begin with. To that end, we’ll use example
code from ChibiOS[^1], a free and open
source RTOS. Specifically, we’ll use their FatFS+USB example for STM32F1 MCUs.

You can reproduce our setup simply by cloning the project and extracting
libraries:

```
$ git clone https://github.com/ChibiOS/ChibiOS.git
[...]
$ cd ChibiOS/ext
$ 7za x fatfs-0.13c_patched.7z
[...]
$ cd ../demos/STM32/RT-STM32F103-STM3210E_EVAL-FATFS-USB
```

To get our baseline, let’s disable all optimizations and build the project:

```
$ make USE_LINK_GC=no USE_LTO=no
[...]
Linking build/ch.elf
Creating build/ch.hex
Creating build/ch.bin
Creating build/ch.dmp

   text	   data	    bss	    dec	    hex	filename
  72824	    232	  98072	 171128	  29c78	build/ch.elf
Creating build/ch.list
```

Which means we are starting with a firmware size of about 71KiB.
