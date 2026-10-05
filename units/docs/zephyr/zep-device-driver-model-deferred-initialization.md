---
id: "zep-device-driver-model-deferred-initialization"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Deferred initialization"
summary: "Initialization of devices can also be deferred to a later time. In this case, the device is not automatically initialized by Zephyr at boot time. Instead, the device is initialized when the application calls device_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Initialization of devices can also be deferred to a later time. In this case,
the device is not automatically initialized by Zephyr at boot time. Instead,
the device is initialized when the application calls `device_init`.
To defer a device driver initialization, add the property `zephyr,deferred-init`
to the associated device node in the DTS file. For example:

```devicetree

/ {
        a-driver@40000000 {
                reg = <0x40000000 0x1000>;
                zephyr,deferred-init;
        };
};
```
