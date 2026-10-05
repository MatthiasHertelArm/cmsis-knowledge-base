---
id: "intr-how-to-debug-a-hardfault-on-an-arm-examples"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples"
summary: "In the sections below we will walk through the analysis of a couple faults."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the sections below we will walk through the analysis of a couple faults.

For this setup we will use:

- a nRF52840-DK[^13] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^12] as our GDB Server.
- GCC 8.3.1 / GNU Arm Embedded Toolchain as our compiler[^16]
- GNU make as our build system

All the code can be found on the [Interrupt Github page](https://github.com/memfault/interrupt/tree/master/example/cortex-m-fault-debug) with more details in the `README` in the directory linked.

#### Setup

Start a GDB Server:

```shell
JLinkGDBServer -if swd -device nRF52840_xxAA
```

{: #svd-usage-example}
Follow the instructions [above](#pycortex-svd-gdb-setup) to setup support for reading SVD files from GDB, build, and flash the example app:

```shell
$ make
[...]
Linking library
Generated build/nrf52.elf
$ arm-none-eabi-gdb-py --eval-command="target remote localhost:2331" --ex="mon reset" --ex="load" --ex="mon reset" --se=build/nrf52.elf
$ source PyCortexMDebug/cmdebug/svd_gdb.py
$ (gdb) svd_load cortex-m4-scb.svd
Loading SVD file cortex-m4-scb.svd...
(gdb)
```

The app has eight different crashes you can configure by changing `FAULT_EXAMPLE_CONFIG` at compile time or by editing the value at runtime:

```
(gdb) break main
(gdb) continue
(gdb) set g_crash_config=1
(gdb) continue
```

{: #bad-pc-mpu-fault}
