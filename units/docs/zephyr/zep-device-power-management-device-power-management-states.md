---
id: "zep-device-power-management-device-power-management-states"
type: "concept"
domain: "optimization"
title: "Device Power Management: Device Power Management States"
summary: "The power management subsystem defines device states in pm_device_state. This method is used to track power states of a particular device."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

The power management subsystem defines device states in
`pm_device_state`. This method is used to track power states of
a particular device. It is important to emphasize that, although the
state is tracked by the subsystem, it is the responsibility of each device driver
to handle device actions(`pm_device_action`) which change device state.

Device drivers implement the `pm_device_action_cb_t` hook internally
which receives the `pm_device_action` for the device driver to handle.
If the `CONFIG_PM_DEVICE` option is selected, the device
drivers implementations of the hooks are exposed to the PM subsystem, enabling
runtime power management of the devices.

`pm_device_action` actions have direct and unambiguous relationships with
`pm_device_state` states:

As mentioned above, device drivers do not directly change between these states.
This is entirely done by the power management subsystem. Instead, drivers are
responsible for implementing any hardware-specific tasks needed to handle state
changes.
