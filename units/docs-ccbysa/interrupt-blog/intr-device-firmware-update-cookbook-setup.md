---
id: "intr-device-firmware-update-cookbook-setup"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Setup"
summary: "All the code in this post was written for the STM32F429 MCU by ST Micro. While the examples run fine on the STM32F429i discovery board they were developed in Renode, a popular MCU emulation platform."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

All the code in this post was written for the STM32F429 MCU by ST Micro. While
the examples run fine on the STM32F429i discovery board they were developed in
Renode, a popular MCU emulation platform.

You can find the complete code example for this blog post in the [Interrupt
Github repository](https://github.com/memfault/interrupt/tree/master/example/fwup-architecture)

### Renode

Since writing about Renode for Interrupt, I’ve been looking for an opportunity
to use it for another project. This blog post was the perfect pretext. If you
are not familiar with Renode, I recommend reading [my previous blog post](https://interrupt.memfault.com/blog/intro-to-renode) on
the topic.

Because we use true firmware images `.bin`'s rather than `elf` files in this post, I had to make two
change to the Renode configuration:

1. I used `sysbus LoadBinary $bin 0x8000000` rather than `LoadELF` to load the
   firmware.
2. I manually set the Vector Table Offset with `sysbus.cpu VectorTableOffset
   0x8000000`. By default, Renode looks for the vector table at `0x0` which
different from the default behavior of the STM32.

**Update: As of July 2020, Renode has merged our updates to implement the AICR
register so you can run our code on a standard Renode built**

~~Additionally, I had to modify Renode slightly to enable software-controlled
resets. Cortex-M microcontrollers can be reset by writing to the AICR register,
which was not fully implemented in the emulator. As of this writing, this change
is still in review and not yet merged into the emulator. You can find the pull
request [on
Github](https://github.com/renode/renode-infrastructure/pull/15/files).~~

~~Thankfully, building our own version of Renode is relatively
straightforward using [their
instructions](https://renode.readthedocs.io/en/latest/advanced/building_from_sources.html).~~

I updated my `start.sh` script to run my home-built Renode instance rather than
the installed binary:

```
#!/bin/sh

RENODE_EXE_PATH=~/code/renode/output/bin/Release/Renode.exe

mono64 $RENODE_EXE_PATH renode-config.resc
```

You will have to update this script to point at your own `Renode.exe`.

### Toolchain

I used the following tools to build my firmware:
* GNU Make 4.2.1 as the build system
* `arm-none-eabi-gcc` version 9.2.1 20191025 (release) as compiler

Rather than the STM32Cube HAL, I used an open source MCU HAL called `libopencm3`
with excellent support for the STM32. I find it easier to use, and like that it
is open source and on Github. The included `Makefile` will clone `libopencm3`
during your first build.

### Building & Running the Example

The example can be built with Make. From the `examples/fwup-architecture`
directory:

```terminal
$ make
  LD            build/fwup-example-boot.elf
  OBJCOPY       build/fwup-example-boot.bin
  LD            build/fwup-example-app.elf
  OBJCOPY       build/fwup-example-app.bin
  XXD           build/app_bin.c
  LD            build/fwup-example-loader.elf
  OBJCOPY       build/fwup-example-loader.bin
  CAT           build/fwup-example.bin
```

After which you can call `./start.sh` to start Renode. You will need to type the
`start` command in the Renode window to get the emulation going.


