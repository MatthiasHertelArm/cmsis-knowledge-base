---
id: "zep-device-driver-model-introduction"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Introduction"
summary: "The Zephyr kernel supports a variety of device drivers. Whether a driver is available depends on the board and the driver."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr kernel supports a variety of device drivers. Whether a
driver is available depends on the board and the driver.

The Zephyr device model provides a consistent device model for configuring the
drivers that are part of a system. The device model is responsible
for initializing all the drivers configured into the system.

Each type of driver (e.g. UART, SPI, I2C) is supported by a generic type API.

In this model the driver fills in the pointer to the structure containing the
function pointers to its API functions during driver initialization. These
structures are placed into the RAM section in initialization level order.
