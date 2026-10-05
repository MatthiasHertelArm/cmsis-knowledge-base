---
id: "zep-device-runtime-power-management-design-principles"
type: "concept"
domain: "optimization"
title: "Device Runtime Power Management: Design principles"
summary: "When runtime PM is enabled on a device it will no longer be resumed or suspended during system power transitions. Instead, the device is fully responsible to indicate when it needs a device and when it does not."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/device_runtime.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/device_runtime.rst"
license: "Apache-2.0"
mode: "V"
---

When runtime PM is enabled on a device it will no longer be resumed or suspended
during system power transitions. Instead, the device is fully responsible to
indicate when it needs a device and when it does not. The device runtime PM API
uses reference counting to keep track of device's usage. This allows the API to
determine when a device needs to be resumed or suspended. The API uses the *get*
and *put* terminology to indicate when a device is needed or not, respectively.
This mechanism plays a key role when we account for device dependencies. For
example, if a bus device is used by multiple sensors, we can keep the bus active
until the last sensor has finished using it.


**Note:** As of today, the device runtime power management API does not manage device dependencies. This effectively means that, if a device depends on other devices to operate (e.g. a sensor may depend on a bus device), the bus will be resumed and suspended on every transaction. In general, it is more efficient to keep parent devices active when their children are used, since the children may perform multiple transactions in a short period of time. Until this feature is added, devices can manually *get* or *put* their dependencies.

The `pm_device_runtime_get` function can be used by a device driver to
indicate it *needs* the device to be active or operational. This function will
increase device usage count and resume the device if necessary. Similarly, the
`pm_device_runtime_put` function can be used to indicate that the device
is no longer needed. This function will decrease the device usage count and
suspend the device if necessary. It is worth to note that in both cases, the
operation is carried out synchronously. The sequence diagram shown below
illustrates how a device can use this API and the expected sequence of events.

The synchronous model is as simple as it gets. However, it may introduce
unnecessary delays since the application will not get the operation result until
the device is suspended (in case device is no longer used). It will likely not
be a problem if the operation is fast, e.g. a register toggle. However, the
situation will not be the same if suspension involves sending packets through a
slow bus. For this reason the device drivers can also make use of the
`pm_device_runtime_put_async` function. This function will schedule
the suspend operation, again, if device is no longer used.


By default, runtime PM operations are offloaded to the system work queue.
However, device drivers must not perform any blocking operations during suspend, as
this can stall the system work queue and negatively impact system responsiveness.

To address this, applications can configure runtime PM to use a dedicated work queue
by enabling `CONFIG_PM_DEVICE_RUNTIME_USE_DEDICATED_WQ`.

If blocking behavior is required—for example, when accessing a slow peripheral
or waiting for a bus transaction—the PM subsystem work queue must be used instead.
Drivers that require this behavior can explicitly request it by enabling
`CONFIG_PM_DEVICE_DRIVER_NEEDS_DEDICATED_WQ`.

For targets with constrained resources that do not need asynchronous
operations, this functionality can be disabled altogether by
de-selecting `CONFIG_PM_DEVICE_RUNTIME_ASYNC`, reducing
memory usage and system complexity.
