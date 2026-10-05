---
id: "intr-tools-we-use-installing-gdb-for-ar-crosstool-ng"
type: "concept"
domain: "debug"
title: "Tools we use: installing GDB for ARM: Details on each strategy / crosstool-NG"
summary: "From the website:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-03-installing-gdb.md"
doc_source: "https://interrupt.memfault.com/blog/installing-gdb#crosstool-ng"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Details on each strategy_

From the [website](https://crosstool-ng.github.io/):

> Crosstool-NG is a versatile (cross) toolchain generator. It supports many
> architectures and components and has a simple yet powerful menuconfig-style
> interface.

It's quite easy to get started with crosstool-ng, and there's a good number of
example configurations provided. A quickstart might run like this:

```bash
# 1. build crosstool-ng itself

# fetch the crosstool-ng repo
❯ git clone https://github.com/crosstool-ng/crosstool-ng
❯ cd crosstool-ng
❯ git checkout crosstool-ng-1.25.0

# build crosstool-ng
❯ ./bootstrap && ./configure --enable-local && make -j$(nproc)

# 2. now to build a toolchain

# use one of the example configs
❯ ./ct-ng arm-nano-eabi
# you can use './ct-ng menuconfig' to adjust the config, eg, add CT_DEBUG_GDB=y
# to enable building gdb

# build the toolchain. this can take a while- on my middle-range laptop, it
# took about 12 minutes
❯ ./ct-ng build

# now to test it (the toolchain output needs to be inserted to path)
❯ export PATH=$PWD/.build/arm-nano-eabi/buildtools/bin:$PATH
❯ export PATH=$PWD/.build/arm-nano-eabi/build/build-gdb-cross/gdb:$PATH
# confirm gdb is the freshly built one
❯ which gdb
/home/noah/dev/github/crosstool-ng/.build/arm-nano-eabi/build/build-gdb-cross/gdb/gdb
# run the check-architecture script from above
❯ gdb --batch -nx --ex 'set architecture' 2>&1 | tail -n 1 | sed 's/auto./\n/g' | sed 's/,/\n/g' | sed 's/Requires an argument. Valid arguments are/\n/g' | sed '/^[ ]*$/d' | sort | uniq

 arm
 arm_any
 armv2
 armv2a
 armv3
 armv3m
 armv4
 armv4t
 armv5
 armv5t
 armv5te
 armv5tej
 armv6
 armv6k
 armv6kz
 armv6-m
 armv6s-m
 armv6t2
 armv7
 armv7e-m
 armv8.1-m.main
 armv8-a
 armv8-m.base
 armv8-m.main
 armv8-r
 ep9312
 iwmmxt
 iwmmxt2
 xscale

# build an uninteresting program
❯ echo "int main(){return 0;}" > main.c
❯ arm-nano-eabi-gcc -mcpu=cortex-m0plus -ggdb3 -nostdlib -Wl,--entry=main -o arm.elf main.c
# check the elf it built with binutils
❯ gdb arm.elf -batch --ex 'disassemble /s main'
threads module disabled
Dump of assembler code for function main:
main.c:
1       int main(){return 0;}
   0x00008000 <+0>:     push    {r7, lr}
   0x00008002 <+2>:     add     r7, sp, #0
   0x00008004 <+4>:     movs    r3, #0
   0x00008006 <+6>:     movs    r0, r3
   0x00008008 <+8>:     mov     sp, r7
   0x0000800a <+10>:    pop     {r7, pc}
End of assembler dump.

❯ arm-nano-eabi-objdump --disassemble=main --source arm.elf

arm.elf:     file format elf32-littlearm


Disassembly of section .text:

00008000 <main>:
int main(){return 0;}
    8000:       b580            push    {r7, lr}
    8002:       af00            add     r7, sp, #0
    8004:       2300            movs    r3, #0
    8006:       0018            movs    r0, r3
    8008:       46bd            mov     sp, r7
    800a:       bd80            pop     {r7, pc}

❯ arm-nano-eabi-size -Ax arm.elf
arm.elf  :
section             size      addr
.text                0xc    0x8000
.persistent          0x0   0x1800c
.noinit              0x0   0x1800c
.comment            0x22       0x0
.debug_aranges      0x20       0x0
.debug_info         0x48       0x0
.debug_abbrev       0x3a       0x0
.debug_line         0x3c       0x0
.debug_frame        0x2c       0x0
.debug_str        0x2c12       0x0
.debug_macro       0xa7d       0x0
.ARM.attributes     0x2c       0x0
Total             0x37f3
```

You end up with a fully-baked toolchain set up to your specifications, without a
ton of work manually configuring and building various packages.

The Zephyr project currently bases its toolchain builds on crosstool-NG, with
some custom sources:

<https://github.com/zephyrproject-rtos/sdk-ng/tree/61bd806b61e9fa92a90c8e1d81237353556a0560>

And the famous Compiler Explorer project also uses crosstool-NG for cross
toolchain building:

<https://github.com/compiler-explorer/gcc-cross-builder/blob/190e5ba158c42529090fa8ea5f33a4f79b6e179b/Dockerfile#L77>
