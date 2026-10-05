---
id: "zep-device-driver-model-driver-apis"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Driver APIs"
summary: "The following APIs for device drivers are provided by device.h. The APIs are intended for use in device drivers only and should not be used in applications."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

The following APIs for device drivers are provided by `device.h`. The APIs
are intended for use in device drivers only and should not be used in
applications.

`DEVICE_DEFINE()`
   Create device object and related data structures including setting it
   up for boot-time initialization.

`DEVICE_NAME_GET()`
   Converts a device identifier to the global identifier for a device
   object.

`DEVICE_GET()`
   Obtain a pointer to a device object by name.

`DEVICE_DECLARE()`
   Declare a device object.  Use this when you need a forward reference
   to a device that has not yet been defined.

`DEVICE_API()`
   Wrap a driver API declaration to assign it to its respective linker section.
   Use of this macro is mandatory for any driver implementing an upstream driver
   class, as `DEVICE_API_GET` and `DEVICE_API_IS` rely on API
   instances being placed in their class linker section to validate the device's
   API class at runtime.
