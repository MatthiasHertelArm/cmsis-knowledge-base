---
id: "zep-operation-without-threads-subsystem-behavior-without-thread-suppor"
type: "concept"
domain: "rtos"
title: "Operation without Threads: Subsystem Behavior Without Thread Support"
summary: "The sections below list driver and functional subsystems that are expected to work to some degree when CONFIG_MULTITHREADING is disabled. Subsystems that are not listed here should not be expected to work."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/nothread.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/nothread.rst"
license: "Apache-2.0"
mode: "V"
---

The sections below list driver and functional subsystems that are
expected to work to some degree when `CONFIG_MULTITHREADING` is
disabled.  Subsystems that are not listed here should not be expected to
work.

Some existing drivers within the listed subsystems do not work when
threading is disabled, but are within scope based on their subsystem, or
may be sufficiently isolated that supporting them on a particular
platform is low-impact.  Enhancements to add support to existing
capabilities that were not originally implemented to work with threads
disabled will be considered.


### Flash


The flash_api is expected to work for all SoC flash peripheral
drivers.  Bus-accessed devices like serial memories may not be
supported.

*List/table of supported drivers to go here*


### GPIO


The gpio_api is expected to work for all SoC GPIO peripheral
drivers.  Bus-accessed devices like GPIO extenders may not be supported.

*List/table of supported drivers to go here*


### UART


A subset of the uart_api is expected to work for all SoC UART
peripheral drivers.

* Applications that select `CONFIG_UART_INTERRUPT_DRIVEN` may
  work, depending on driver implementation.

* Applications that select `CONFIG_UART_ASYNC_API` may
  work, depending on driver implementation.

* Applications that do not select either `CONFIG_UART_ASYNC_API`
  or `CONFIG_UART_INTERRUPT_DRIVEN` are expected to work.

*List/table of supported drivers to go here, including which API options
are supported*
