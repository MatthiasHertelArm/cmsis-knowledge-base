---
id: "zep-power-domain-introduction"
type: "concept"
domain: "optimization"
title: "Power Domain: Introduction"
summary: "The Zephyr power domain abstraction is designed to support groupings of devices powered by a common source to be notified of power source state changes in a generic fashion."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/pm/power_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/pm/power_domain.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr power domain abstraction is designed to support groupings of devices
powered by a common source to be notified of power source state changes in a
generic fashion. Application code that is using device A does not need to know
that device B is on the same power domain and should also be configured into a
low power state.

Power domains are optional on Zephyr, to enable this feature the
option `CONFIG_PM_DEVICE_POWER_DOMAIN` has to be set.

When a power domain turns itself on or off, it is the responsibility of the
power domain to notify all devices using it through their power management
callback called with
`PM_DEVICE_ACTION_TURN_ON` or
`PM_DEVICE_ACTION_TURN_OFF` respectively. This
work flow is illustrated in the diagram below.


### Internal Power Domains


Most of the devices in an SoC have independent power control that can
be turned on or off to reduce power consumption. But there is a
significant amount of static current leakage that can't be controlled
only using device power management. To solve this problem, SoCs
normally are divided into several regions grouping devices that
are generally used together, so that an unused region can be
completely powered off to eliminate this leakage. These regions are
called "power domains", can be present in a hierarchy and can be
nested.


### External Power Domains


Devices external to a SoC can be powered from sources other than the main power
source of the SoC. These external sources are typically a switch, a regulator,
or a dedicated power IC. Multiple devices can be powered from the same source,
and this grouping of devices is typically called a "power domain".

Placing devices on power domains can be done for a variety of reasons,
including to enable devices with high power consumption in low power mode to be
completely turned off when not in use.
