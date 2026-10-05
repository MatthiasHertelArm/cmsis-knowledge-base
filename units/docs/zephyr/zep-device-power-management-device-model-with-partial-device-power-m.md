---
id: "zep-device-power-management-device-model-with-partial-device-power-m"
type: "concept"
domain: "optimization"
title: "Device Power Management: Device Model with Partial Device Power Management Support"
summary: "If CONFIG_PM_DEVICE is not enabled, the device power state is tied to the devices initialization state."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

If `CONFIG_PM_DEVICE` is not enabled, the device
power state is tied to the devices initialization state.

Once a device is initialized, the device driver PM action hook is
used to move the device to the expected initial state through calling
`pm_device_driver_init`. Following the
`Device actions x states` graph and the definition of the `OFF`
state, this results in a call to `PM_DEVICE_ACTION_TURN_ON`
followed by `PM_DEVICE_ACTION_RESUME`.

If the driver's PM hook returns an error, initialization fails and the
device is left in its previous state (for devices that support PM this is
typically `SUSPENDED` or `OFF`).

Given power domains and buses are "just devices", every power
domain and bus will be resumed before its child devices as they
are initialized according to the devicetree dependency ordinals.
Every device is assumed to be powered, and the devices a device
depends on are assumed to be `ACTIVE`, when device is initialized.

Once a device is deinitialized, the device driver PM action hook
is used to move the device to the `SUSPENDED` state through
calling `pm_device_driver_deinit`. Following the
`Device actions x states`, and assuming power domains are "always
on" this results in a call to `PM_DEVICE_ACTION_SUSPEND`.
