---
id: "zep-pin-control-implementation-guidelines"
type: "concept"
domain: "bring-up"
title: "Pin Control: Implementation guidelines"
summary: "Pin control drivers need to implement a single function: pinctrl_configure_pins. This function receives an array of pin configurations that need to be applied. Furthermore, if CONFIG_PINCTRL_STORE_REG is set, it also receives the associated device register address for the given pins."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/pinctrl/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/pinctrl/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Pin control drivers


Pin control drivers need to implement a single function:
`pinctrl_configure_pins`. This function receives an array of pin
configurations that need to be applied. Furthermore, if
`CONFIG_PINCTRL_STORE_REG` is set, it also receives the associated
device register address for the given pins. This information may be required by
some drivers to perform device specific actions.

The pin configuration is stored in an opaque type that is vendor/SoC dependent:
`pinctrl_soc_pin_t`. This type needs to be defined in a header named
`pinctrl_soc.h` file that is in the Zephyr's include path. It can range from
a simple integer value to a struct with multiple fields. `pinctrl_soc.h` also
needs to define a macro named `Z_PINCTRL_STATE_PINS_INIT` that accepts two
arguments: a node identifier and a property name (`pinctrl-N`). With this
information the macro needs to define an initializer for all pin configurations
contained within the `pinctrl-N` property of the given node.

Regarding Devicetree pin configuration representation, vendors can decide which
option is better for their devices. However, the following guidelines should be
followed:

- Use `pinctrl-N` (N=0, 1, ...) and `pinctrl-names` properties to define pin
  control states. These properties are defined in
  `dts/bindings/pinctrl/pinctrl-device.yaml`.
- Use standard pin configuration properties as defined in
  `dts/bindings/pinctrl/pincfg-node.yaml`.

Representations not following these guidelines may be accepted if they are
already used by the same vendor in other operating systems, e.g. Linux.


### Device drivers


In this section you will find some tips on how a device driver should use the
`pinctrl` API to successfully configure the pins it needs.

The device compatible needs to be modified in the corresponding binding so that
the `pinctrl-device.yaml` is included. For example:

```yaml

include: [base.yaml, pinctrl-device.yaml]
```
This file is needed to add `pinctrl-N` and `pinctrl-names` properties to the
device.

From a device driver perspective there are two steps that need to be performed
to be able to use the `pinctrl` API. First, the pin control configuration
needs to be defined. This includes all states and pins.
`PINCTRL_DT_DEFINE` or `PINCTRL_DT_INST_DEFINE` macros
should be used for this purpose. Second, a reference to
the device instance `pinctrl_dev_config` needs to be stored, since it
is required to later use the API. This can be achieved using the
`PINCTRL_DT_DEV_CONFIG_GET` and
`PINCTRL_DT_INST_DEV_CONFIG_GET` macros.

It is worth to note that the only relationship between a device and its
associated pin control configuration is based on variable naming conventions.
The way an instance of `pinctrl_dev_config` is named for a
corresponding device instance allows to later obtain a reference to it given the
device's Devicetree node identifier. This allows to minimize ROM usage, since
only devices requiring pin control will own a reference to a pin control
configuration.

Once the driver has defined the pin control configuration and kept a reference
to it, it is ready to use the API. The most common way to apply a state is by
using `pinctrl_apply_state`. It is also possible to use the lower level
function `pinctrl_apply_state_direct` to skip state lookup if it is
cached in advance (e.g. at init time). Since state lookup time is expected to be
fast, it is recommended to use `pinctrl_apply_state`.

The example below contains a complete example of a device driver that uses the
`pinctrl` API.

```c

/* A driver for the "mydev" compatible device */
#define DT_DRV_COMPAT mydev

...
#include <zephyr/drivers/pinctrl.h>
...

struct mydev_config {
    ...
    /* Reference to mydev pinctrl configuration */
    const struct pinctrl_dev_config *pcfg;
    ...
};

...

static int mydev_init(const struct device *dev)
{
    const struct mydev_config *config = dev->config;
    int ret;
    ...
    /* Select "default" state at initialization time */
    ret = pinctrl_apply_state(config->pcfg, PINCTRL_STATE_DEFAULT);
    if (ret < 0) {
        return ret;
    }
    ...
}

#define MYDEV_DEFINE(i)                                                    \
    /* Define all pinctrl configuration for instance "i" */                \
    PINCTRL_DT_INST_DEFINE(i);                                             \
    ...                                                                    \
    static const struct mydev_config mydev_config_##i = {                  \
        ...                                                                \
        /* Keep a ref. to the pinctrl configuration for instance "i" */    \
        .pcfg = PINCTRL_DT_INST_DEV_CONFIG_GET(i),                         \
        ...                                                                \
    };                                                                     \
    ...                                                                    \
                                                                           \
    DEVICE_DT_INST_DEFINE(i, mydev_init, NULL, &mydev_data##i,             \
                          &mydev_config##i, ...);

DT_INST_FOREACH_STATUS_OKAY(MYDEV_DEFINE)
```
