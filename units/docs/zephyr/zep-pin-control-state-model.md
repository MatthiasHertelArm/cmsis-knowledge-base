---
id: "zep-pin-control-state-model"
type: "concept"
domain: "bring-up"
title: "Pin Control: State model"
summary: "For a device driver to operate correctly, a certain pin configuration needs to be applied. Some device drivers require a static configuration, usually set up at initialization time."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/pinctrl/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/pinctrl/index.rst"
license: "Apache-2.0"
mode: "V"
---

For a device driver to operate correctly, a certain pin configuration needs to
be applied. Some device drivers require a static configuration, usually set up
at initialization time. Others need to change the configuration at runtime
depending on the operating conditions, for example, to enable a low-power mode
when suspending the device. Such requirements are modeled using **states**, a
concept that has been adapted from the one in the Linux kernel. Each device
driver owns a set of states. Each state has a unique name and contains a full
pin configuration set (see the figure below). This effectively
means that states are independent of each other, so they do not need to be
applied in any specific order. Another advantage of the state model is that it
isolates device drivers from pin configuration.


+----+------------------+----+------------------+
| `UART0` peripheral                          |
+====+==================+====+==================+
| `default` state     | `sleep` state       |
+----+------------------+----+------------------+
| TX | - Pin: PA0       | TX | - Pin: PA0       |
|    | - Pull: NONE     |    | - Pull: NONE     |
|    | - Low Power: NO  |    | - Low Power: YES |
+----+------------------+----+------------------+
| RX | - Pin: PA1       | RX | - Pin: PA1       |
|    | - Pull: UP       |    | - Pull: NONE     |
|    | - Low Power: NO  |    | - Low Power: YES |
+----+------------------+----+------------------+

### Standard states


The name assigned to pin control states or the number of them is up to the
device driver requirements. In many cases a single state applied at
initialization time will be sufficient, but in some other cases more will be
required. In order to make things consistent, a naming convention has been
established for the most common use cases. The figure below
details the standardized states and its purpose.


+-------------+----------------------------------+-------------------------+
| State       | Identifier                       | Purpose                 |
+-------------+----------------------------------+-------------------------+
| `default` | `PINCTRL_STATE_DEFAULT` | State of the pins when  |
|             |                                  | the device is in        |
|             |                                  | operational state       |
+-------------+----------------------------------+-------------------------+
| `sleep`   | `PINCTRL_STATE_SLEEP`   | State of the pins when  |
|             |                                  | the device is in low    |
|             |                                  | power or sleep modes    |
+-------------+----------------------------------+-------------------------+
Note that other standard states could be introduced in the future.


### Custom states


Some device drivers may require using custom states beyond the standard ones. To
achieve that, the device driver needs to have in its scope definitions for the
custom state identifiers named as `PINCTRL_STATE_{STATE_NAME}`, where
`{STATE_NAME}` is the capitalized state name. For example, if `mystate` has
to be supported, a definition named `PINCTRL_STATE_MYSTATE` needs to be
in the driver's scope.


**Note:** It is important that custom state identifiers start from

If custom states need to be accessed from outside the driver, for example to
perform dynamic pin control, custom identifiers should be placed in a header
that is publicly accessible.


### Skipping states


In most situations, the states defined in Devicetree will be the ones used in
the compiled firmware. However, there are some cases where certain states will
be conditionally used depending on a compilation flag. A typical case is the
`sleep` state. This state is only used in practice if
`CONFIG_PM` or `CONFIG_PM_DEVICE` is enabled.
If a firmware variant without these power management configurations is needed,
one should in theory remove the `sleep` state from Devicetree to not waste ROM
space storing such unused state.

States can be skipped by the `pinctrl` Devicetree macros if a definition named
`PINCTRL_SKIP_{STATE_NAME}` expanding to `1` is present when pin control
configuration is defined. In case of the `sleep` state, the `pinctrl` API
already provides such definition conditional to the availability of device power
management:

```c

#if !defined(CONFIG_PM) && !defined(CONFIG_PM_DEVICE)
/** Out of power management configurations, ignore "sleep" state. */
#define PINCTRL_SKIP_SLEEP 1
#endif
```
