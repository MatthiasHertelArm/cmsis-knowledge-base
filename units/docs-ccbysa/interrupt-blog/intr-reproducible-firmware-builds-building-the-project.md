---
id: "intr-reproducible-firmware-builds-building-the-project"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible / Building the Project"
summary: "Let's clone the Interrupt repository and build the project:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#building-the-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Making a Build Reproducible_

Let's clone the Interrupt repository and build the project:

```bash
$ mkdir -p /private/tmp/repos
$ cd /private/tmp/repos && git clone git@github.com:memfault/interrupt.git
$ cd interrupt/example/reproducible-build/
$ make
Compiling main.c
Compiling startup.c
Compiling minimal_heap.c
Compiling freertos_kernel/tasks.c
Compiling freertos_kernel/queue.c
Compiling freertos_kernel/list.c
Compiling freertos_kernel/timers.c
Compiling freertos_kernel/portable/GCC/ARM_CM4F/port.c
Compiling freertos_kernel/portable/MemMang/heap_1.c
Linking library
Generated build/nrf52.elf
```

#### Flashing the Project

In one terminal, you will need to start a GDB server:

```bash
JLinkGDBServer  -if swd -device nRF52840_xxAA
```

In the other you will need to start GDB and type `continue` to start running the application:

```bash
$ arm-none-eabi-gdb-py --eval-command="target remote localhost:2331" --ex="mon reset" --ex="load" --ex="mon reset" --se=build/nrf52.elf
[...]
Resetting target
Loading section .interrupts, size 0x48 lma 0x0
Loading section .gnu_build_id, size 0x24 lma 0x48
Loading section .text, size 0x17e8 lma 0x70
Loading section .data, size 0x1ec lma 0x1858
Start address 0x70, load size 6720
Transfer rate: 1640 KB/sec, 1680 bytes/write.
Resetting target
(gdb) continue
[...]
```

Great, looks like the app is happily running!
