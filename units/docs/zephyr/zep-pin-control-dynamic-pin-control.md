---
id: "zep-pin-control-dynamic-pin-control"
type: "concept"
domain: "bring-up"
title: "Pin Control: Dynamic pin control"
summary: "Dynamic pin control refers to the capability of changing pin configuration at runtime."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/pinctrl/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/pinctrl/index.rst"
license: "Apache-2.0"
mode: "V"
---

Dynamic pin control refers to the capability of changing pin configuration
at runtime. This feature can be useful in situations where the same firmware
needs to run onto slightly different boards, each having a peripheral routed at
a different set of pins. This feature can be enabled by setting
`CONFIG_PINCTRL_DYNAMIC`.


**Note:** Dynamic pin control should only be used on devices that have not been initialized. Changing pin configurations while a device is operating may lead to unexpected behavior. Since Zephyr does not support device de-initialization yet, this functionality should only be used during early boot stages.

One of the effects of enabling dynamic pin control is that
`pinctrl_dev_config` will be stored in RAM instead of ROM (not states
or pin configurations, though). The user can then use
`pinctrl_update_states` to update the states stored in
`pinctrl_dev_config` with a new set. This effectively means that the
device driver will apply the pin configurations stored in the updated states
when it applies a state.
