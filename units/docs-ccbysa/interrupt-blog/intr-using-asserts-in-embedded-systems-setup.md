---
id: "intr-using-asserts-in-embedded-systems-setup"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples / Setup"
summary: "Part of: Custom Assert Implementation Examples"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Custom Assert Implementation Examples_

For this setup we will use:

- a nRF52840-DK[^5] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^6] as our GDB Server.
- GCC 8.3.1 / GNU Arm Embedded Toolchain as our compiler[^7]
- GNU make as our build system

All the code can be found on the
[Interrupt Github page](https://github.com/memfault/interrupt/tree/master/example/debugging-asserts)
with more details in the `README` in the directory linked.

#### Compiling the code and launching it with GDB

```
# Compile the first assert implementation
$ IMPL=ASSERT1 make
Compiling main.c
Compiling startup.c
Compiling freertos_kernel/tasks.c
Compiling freertos_kernel/queue.c
Compiling freertos_kernel/list.c
Compiling freertos_kernel/timers.c
Compiling freertos_kernel/portable/GCC/ARM_CM4F/port.c
Compiling freertos_kernel/portable/MemMang/heap_1.c
Compiling impls/assert1.c
Linking library
Generated build/nrf52.elf

# In one terminal, start a GDB Server
$ JLinkGDBServer  -if swd -device nRF52840_xxAA
SEGGER J-Link GDB Server V6.52a Command Line Version

# Flash the code on the NRF52 and start gdb
$ arm-none-eabi-gdb-py --eval-command="target remote localhost:2331" --ex="mon reset" --ex="load"
--ex="mon reset" --se=build/nrf52.elf
GNU gdb (GNU Tools for Arm Embedded Processors 8-2019-q3-update) 8.3.0.20190703-git
Copyright (C) 2019 Free Software Foundation, Inc.
[...]
Resetting target
Loading section .interrupts, size 0x40 lma 0x0
Loading section .text, size 0x194d lma 0x40
Loading section .data, size 0x4 lma 0x1990
Start address 0x40, load size 6545
Transfer rate: 2130 KB/sec, 2181 bytes/write.
Resetting target
(gdb)
```

#### Assert metadata structure

To help with the usability of our implementation, both while connected to a
debugger and when logging to persistent storage, we'll define a structure to
store information about the assert.

```c
// Convenience structure that we can store items in
//  to print out later when we add logging.
typedef struct sAssertInfo {
  uint32_t pc;
  uint32_t lr;
  uint32_t line;
  // I don't suggest actually using these, but they
  // are included for the examples.
  char file[256];
  char msg[256];
} sAssertInfo;

extern sAssertInfo g_assert_info;
```

This provides fields for the ARM program counter and link register, the file and
line number, and the message if any provided to the assert. In our example
assert implementations, we'll fill in the fields we can access.
