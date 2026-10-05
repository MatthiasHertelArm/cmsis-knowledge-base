---
id: "zep-device-runtime-power-management-introduction"
type: "concept"
domain: "optimization"
title: "Device Runtime Power Management: Introduction"
summary: "The device runtime power management (PM) framework is an active power management mechanism which reduces the overall system power consumption by suspending the devices which are idle or not used independently of the system state."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/device_runtime.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/device_runtime.rst"
license: "Apache-2.0"
mode: "V"
---

The device runtime power management (PM) framework is an active power management
mechanism which reduces the overall system power consumption by suspending the
devices which are idle or not used independently of the system state. It can be
enabled by setting `CONFIG_PM_DEVICE_RUNTIME`. In this model the device
driver is responsible to indicate when it needs the device and when it does not.
This information is used to determine when to suspend or resume a device based
on usage count.

When device runtime power management is enabled on a device, its state will be
initially set to a `PM_DEVICE_STATE_SUSPENDED` indicating it is
not used. On the first device request, it will be resumed and so put into the
`PM_DEVICE_STATE_ACTIVE` state. The device will remain in this
state until it is no longer used. At this point, the device will be suspended
until the next device request. If the suspension is performed synchronously the
device will be immediately put into the
`PM_DEVICE_STATE_SUSPENDED` state, whereas if it is performed
asynchronously, it will be put into the
`PM_DEVICE_STATE_SUSPENDING` state first and then into the
`PM_DEVICE_STATE_SUSPENDED` state when the action is run.

For devices on a power domain (via the devicetree 'power-domains' property), device runtime
power management automatically attempts to request and release the dependent domain
in response to `pm_device_runtime_get` and `pm_device_runtime_put`
calls on the child device.

For the previous to automatically control the power domain state, device runtime PM must be enabled
on the power domain device. To enable device runtime PM globally, enable
`CONFIG_PM_DEVICE_RUNTIME_DEFAULT_ENABLE`. To enable device runtime PM only for
select devices, set the `zephyr,pm-device-runtime-auto` devicetree property, or use
`pm_device_runtime_enable` for the select devices.

The device runtime power management framework has been designed to minimize
devices power consumption with minimal application work. Device drivers are
responsible for indicating when they need the device to be operational and
when they do not. Therefore, applications can not manually suspend or resume a
device. An application can, however, decide when to disable or enable runtime
power management for a device. This can be useful, for example, if an
application wants a particular device to be always active.
