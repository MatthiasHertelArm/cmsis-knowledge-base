---
id: "zep-power-domain-implementation-guidelines"
type: "concept"
domain: "optimization"
title: "Power Domain: Implementation guidelines"
summary: "In a first place, a device that acts as a power domain needs to declare compatible with power-domain. Taking pm-domain-work-flow as example, the following code defines a domain called gpio_domain."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/pm/power_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/pm/power_domain.rst"
license: "Apache-2.0"
mode: "V"
---

In a first place, a device that acts as a power domain needs to
declare compatible with `power-domain`. Taking
pm-domain-work-flow as example, the following code defines a
domain called `gpio_domain`.

```devicetree

gpio_domain: gpio_domain@4 {
    compatible = "power-domain";
    ...
};
```
A power domain needs to implement the PM action callback used by the
PM subsystem to turn devices on and off.

```c

static int mydomain_pm_action(const struct device *dev,
                           enum pm_device_action action)
{
    switch (action) {
    case PM_DEVICE_ACTION_RESUME:
        /* resume the domain */
        ...
        /* notify children domain is now powered */
        pm_device_children_action_run(dev, PM_DEVICE_ACTION_TURN_ON, NULL);
        break;
    case PM_DEVICE_ACTION_SUSPEND:
        /* notify children domain is going down */
        pm_device_children_action_run(dev, PM_DEVICE_ACTION_TURN_OFF, NULL);
        /* suspend the domain */
        ...
        break;
    case PM_DEVICE_ACTION_TURN_ON:
        /* turn on the domain (e.g. setup control pins to disabled) */
        ...
        break;
    case PM_DEVICE_ACTION_TURN_OFF:
        /* turn off the domain (e.g. reset control pins to default state) */
        ...
        break;
    default:
        return -ENOTSUP;
    }

    return 0;
}
```
Devices belonging to this device can be declared referring it in the
`power-domain` node's property. The example below declares devices
`gpio0` and `gpio1` belonging to domain `gpio_domain``.

```devicetree

&gpio0 {
        compatible = "zephyr,gpio-emul";
        gpio-controller;
        power-domains = <&gpio_domain>;
};

&gpio1 {
        compatible = "zephyr,gpio-emul";
        gpio-controller;
        power-domains = <&gpio_domain>;
};
```
All devices under a domain will be notified when the domain changes
state. These notifications are sent as actions in the device PM action
callback and can be used by them to do any additional work required.
They can safely be ignored though.

```c

static int mydev_pm_action(const struct device *dev,
                           enum pm_device_action *action)
{
    switch (action) {
    case PM_DEVICE_ACTION_SUSPEND:
        /* suspend the device */
        ...
        break;
    case PM_DEVICE_ACTION_RESUME:
        /* resume the device */
        ...
        break;
    case PM_DEVICE_ACTION_TURN_ON:
        /* configure the device into low power mode */
        ...
        break;
    case PM_DEVICE_ACTION_TURN_OFF:
        /* prepare the device for power down */
        ...
        break;
    default:
        return -ENOTSUP;
    }

    return 0;
}
```

**Note:** It is responsibility of driver or the application to set the domain as "wakeup" source if a device depending on it is used as "wakeup" source.
