---
id: "zep-device-power-management-wakeup-capability"
type: "concept"
domain: "optimization"
title: "Device Power Management: Wakeup capability"
summary: "Some devices are capable of waking the system up from a sleep state. When a device has such capability, applications can enable or disable this feature on a device dynamically using pm_device_wakeup_enable."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/device.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/device.rst"
license: "Apache-2.0"
mode: "V"
---

Some devices are capable of waking the system up from a sleep state.
When a device has such capability, applications can enable or disable
this feature on a device dynamically using
`pm_device_wakeup_enable`.

This property can be set on device declaring the property `wakeup-source` in
the device node in devicetree. For example, this devicetree fragment sets the
`gpio0` device as a "wakeup" source:

```devicetree

gpio0: gpio@40022000 {
        compatible = "ti,cc13xx-cc26xx-gpio";
        reg = <0x40022000 0x400>;
        interrupts = <0 0>;
        status = "disabled";
        label = "GPIO_0";
        gpio-controller;
        wakeup-source;
        #gpio-cells = <2>;
};
```
By default, "wakeup" capable devices do not have this functionality enabled
during the device initialization. Applications can enable this functionality
later calling `pm_device_wakeup_enable`.


**Note:** This property is **only** used by the system power management to identify devices that should not be suspended. It is responsibility of driver or the application to do any additional configuration required by the device to support it.
