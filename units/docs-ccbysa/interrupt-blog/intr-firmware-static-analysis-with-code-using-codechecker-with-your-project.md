---
id: "intr-firmware-static-analysis-with-code-using-codechecker-with-your-project"
type: "concept"
domain: "debug"
title: "Firmware Static Analysis with CodeChecker: Using CodeChecker with your Project"
summary: "In this post, we will use ChibiOS as our example project. ChibiOS is a popular RTOS with support for a wide variety of chips. Most importantly, it is relatively straightforward to set up and comes with lots of examples."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-19-static-analysis-with-codechecker.md"
doc_source: "https://interrupt.memfault.com/blog/static-analysis-with-codechecker#using-codechecker-with-your-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Setup

In this post, we will use ChibiOS as our example project. ChibiOS is a popular
RTOS with support for a wide variety of chips. Most importantly, it is
relatively straightforward to set up and comes with lots of examples.

You can download the latest ChibiOS release from [their
website](https://osdn.net/projects/chibios/releases), though I simply `clone`-d
it from [GitHub](https://github.com/ChibiOS/ChibiOS):

```bash
$ git clone https://github.com/ChibiOS/ChibiOS/
```

You’ll need to install a few dependencies, like an ARM toolchain and the `make`
build system:

```
$ apt install gcc-arm-none-eabi make p7zip-full
```

Before you proceed, make sure to decompress the libraries in the `ext` folder:

```
$ cd ext
$ ls *.7z | xargs -I {} 7z x {}
```

At this point, you should be able to build an example. I will use
`RT-STM32-LWIP-FATFS-USB`:

```
$ cd demos/STM32/RT-STM32-LWIP-FATFS-USB
$ make -f make/stm32f769_discovery.make
[...]
Linking build/stm32f769_discovery/ch.elf
lto-wrapper: warning: Options to Xassembler do not match: -alms=./build/stm32f769_discovery/lst/crt1.lst, -alms=./build/stm32f769_discovery/lst/hal.lst, dropping all -Xassembler and -Wa options.
Creating build/stm32f769_discovery/ch.hex
Creating build/stm32f769_discovery/ch.bin
Creating build/stm32f769_discovery/ch.dmp

   text    data     bss     dec     hex filename
 126224     232  430496  556952   87f98 build/stm32f769_discovery/ch.elf
Creating build/stm32f769_discovery/ch.list

Done
```

Alright, we’ve got a project to statically analyze!
