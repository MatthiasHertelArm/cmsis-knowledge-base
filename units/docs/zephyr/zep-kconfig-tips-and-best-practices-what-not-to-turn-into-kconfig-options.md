---
id: "zep-kconfig-tips-and-best-practices-what-not-to-turn-into-kconfig-options"
type: "concept"
domain: "project"
title: "Kconfig - Tips and Best Practices: What not to turn into Kconfig options"
summary: "In Zephyr, Kconfig configuration is done after selecting a target board. In general, it does not make sense to use Kconfig for a value that corresponds to a fixed machine-specific setting. Usually, such settings should be handled via devicetree instead."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/kconfig/tips.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/kconfig/tips.rst"
license: "Apache-2.0"
mode: "V"
---

In Zephyr, Kconfig configuration is done after selecting a target board. In
general, it does not make sense to use Kconfig for a value that corresponds to
a fixed machine-specific setting. Usually, such settings should be handled via
devicetree instead.

In particular, avoid adding new Kconfig options of the following types:


### Options that specify a device in the system by name


For example, if you are writing an I2C device driver, avoid creating an option
named `MY_DEVICE_I2C_BUS_NAME` for specifying the bus node your device is
controlled by. See dt-drivers-that-depend for alternatives.

Similarly, if your application depends on a hardware-specific PWM device to
control an RGB LED, avoid creating an option like `MY_PWM_DEVICE_NAME`. See
dt-apps-that-depend for alternatives.


### Options that specify fixed hardware configuration


For example, avoid Kconfig options specifying a GPIO pin.

An alternative applicable to device drivers is to define a GPIO specifier with
type phandle-array in the device binding, and using the
devicetree-gpio-api devicetree API from C. Similar advice applies to
other cases where devicetree.h provides devicetree-hw-api for referring
to other nodes in the system. Search the source code for drivers using these
APIs for examples.

An application-specific devicetree binding to identify
board specific properties may be appropriate. See
`tests/drivers/gpio/gpio_basic_api` for an example.

For applications, see blinky for a devicetree-based alternative.
