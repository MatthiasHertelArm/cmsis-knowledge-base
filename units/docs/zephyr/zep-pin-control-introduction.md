---
id: "zep-pin-control-introduction"
type: "concept"
domain: "bring-up"
title: "Pin Control: Introduction"
summary: "The hardware blocks that control pin multiplexing and pin configuration parameters such as pin direction, pull-up/down resistors, etc. are named pin controllers."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/pinctrl/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/pinctrl/index.rst"
license: "Apache-2.0"
mode: "V"
---

The hardware blocks that control pin multiplexing and pin configuration
parameters such as pin direction, pull-up/down resistors, etc. are named **pin
controllers**. The pin controller's main users are SoC hardware peripherals,
since the controller enables exposing peripheral signals, like for example,
map `I2C0` `SDA` signal to pin `PX0`. Not only that, but it usually allows
configuring certain pin settings that are necessary for the correct functioning
of a peripheral, for example, the slew-rate depending on the operating
frequency. The available configuration options are vendor/SoC dependent and can
range from simple pull-up/down options to more advanced settings such as
debouncing, low-power modes, etc.

The way pin control is implemented in hardware is vendor/SoC specific. It is
common to find a *centralized* approach, that is, all pin configuration
parameters are controlled by a single hardware block (typically named pinmux),
including signal mapping. The figure below illustrates this
approach. `PX0` can be mapped to `UART0_TX`, `I2C0_SCK` or `SPI0_MOSI`
depending on the `AF` control bits. Other configuration parameters such as
pull-up/down are controlled in the same block via `CONFIG` bits. This model is
used by several SoC families, such as many from NXP and STM32.

Other vendors/SoCs use a *distributed* approach. In such case, the pin mapping
and configuration are controlled by multiple hardware blocks.
The figure below illustrates a distributed approach where pin
mapping is controlled by peripherals, such as in Nordic nRF SoCs.

From a user perspective, there is no difference in pin controller usage
regardless of the hardware implementation: a user will always apply a state.
The only difference lies in the driver implementation. In general, implementing
a pin controller driver for a hardware that uses a distributed approach requires
more effort, since the driver needs to gather knowledge of peripheral dependent
registers.


### Pin control vs. GPIO


Some functionality covered by a pin controller driver overlaps with GPIO
drivers. For example, pull-up/down resistors can usually be enabled by both the
pin control driver and the GPIO driver. In Zephyr context, the pin control
driver purpose is to perform peripheral signal multiplexing and configuration of
other pin parameters required for the correct operation of that peripheral.
Therefore, the main users of the pin control driver are SoC peripherals. In
contrast, GPIO drivers are for general purpose control of a pin, that is, when
its logic level is read or controlled manually.
