---
id: "zep-gdb-stub-enabling-gdb-stub"
type: "concept"
domain: "debug"
title: "GDB stub: Enabling GDB Stub"
summary: "GDB stub can be enabled with the CONFIG_GDBSTUB option."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/debugging/gdbstub.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/debugging/gdbstub.rst"
license: "Apache-2.0"
mode: "V"
---

GDB stub can be enabled with the `CONFIG_GDBSTUB` option.


### Using Serial Backend


The serial backend for GDB stub can be enabled with
the `CONFIG_GDBSTUB_SERIAL_BACKEND` option.

Since serial backend utilizes UART devices to send and receive GDB commands,

* If there are spare UART devices on the board, set `zephyr,gdbstub-uart`
  property of the chosen node to the spare UART device so that `printk`
  and log messages are not being printed to the same UART device used for GDB.

* For boards with only one UART device, `printk` and logging
  must be disabled if they are also using the same UART device for output.
  GDB related messages may interleave with log messages which may have
  unintended consequences. Usually this can be done by disabling
  `CONFIG_PRINTK` and `CONFIG_LOG`.
