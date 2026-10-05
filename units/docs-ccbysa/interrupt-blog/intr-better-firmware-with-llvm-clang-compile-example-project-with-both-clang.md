---
id: "intr-better-firmware-with-llvm-clang-compile-example-project-with-both-clang"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Compile Example Project with Both Clang and GCC!"
summary: "At this point, we can compile our example project with either GCC or Clang! Let's take a look at the results:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#compile-example-project-with-both-clang-and-gcc"
license: "CC-BY-SA-4.0"
mode: "V"
---

At this point, we can compile our example project with either GCC or Clang! Let's take a look at the results:

#### Clang Build

```bash
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ COMPILER=clang make
===Clang Compiler Detected===
# [...]
Linking library
Generated build/nrf52.elf
   text    data     bss     dec     hex	filename
  10094    2368   13048   25510    63a6	build/nrf52.elf
```

#### GCC Build

```bash
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ COMPILER=arm-none-eabi-gcc make
===GCC Compiler Detected===
# [...]
Linking library
Generated build/nrf52.elf
Generated build/nrf52.elf
   text    data     bss     dec     hex	filename
   9846    2112   13328   25286    62c6	build/nrf52.elf
```

#### Observations

We can see for our simple example app the sizes are within about 1% of each other (25,510 bytes for Clang vs 25,286 bytes for GCC).
