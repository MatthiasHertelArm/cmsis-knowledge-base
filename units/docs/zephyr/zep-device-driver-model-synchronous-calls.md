---
id: "zep-device-driver-model-synchronous-calls"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Synchronous Calls"
summary: "Zephyr provides a set of device drivers for multiple boards. Each driver should support an interrupt-based implementation, rather than polling, unless the specific hardware does not provide any interrupt."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr provides a set of device drivers for multiple boards. Each driver
should support an interrupt-based implementation, rather than polling, unless
the specific hardware does not provide any interrupt.

High-level calls accessed through device-specific APIs, such as
`i2c.h` or `spi.h`, are usually intended as synchronous. Thus,
these calls should be blocking.
