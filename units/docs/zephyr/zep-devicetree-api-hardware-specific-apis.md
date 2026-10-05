---
id: "zep-devicetree-api-hardware-specific-apis"
type: "concept"
domain: "project"
title: "Devicetree API: Hardware specific APIs"
summary: "The following APIs can also be used by including <devicetree.h>; no additional include is needed."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/api/api.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/api/api.rst"
license: "Apache-2.0"
mode: "V"
---

The following APIs can also be used by including `<devicetree.h>`;
no additional include is needed.


### CAN


These conveniences may be used for nodes which describe CAN
controllers/transceivers, and properties related to them.


### Clocks


These conveniences may be used for nodes which describe clock sources, and
properties related to them.


### DMA


These conveniences may be used for nodes which describe direct memory access
controllers or channels, and properties related to them.


### Display


These conveniences may be used for nodes which describe display
controllers, and properties related to them.


### Fixed and mapped flash partitions


These conveniences may be used for the special-purpose `fixed-partitions`
and `zephyr,mapped-partition` compatibles used to encode information about
flash memory partitions in the device tree. See `fixed-partitions`
and `zephyr,mapped-partition` for more details.


### GPIO


These conveniences may be used for nodes which describe GPIO controllers/pins,
and properties related to them.


### HWSpinlock


These conveniences may be used for nodes which describe hardware spinlock,
and properties related to them.


### IO channels


These are commonly used by device drivers which need to use IO
channels (e.g. ADC or DAC channels) for conversion.


### MBOX


These conveniences may be used for nodes which describe MBOX controllers/users,
and properties related to them.


### MUX


These conveniences may be used for nodes which describe MUX controllers/consumers,
and properties related to them.


### NVMEM


These conveniences may be used for nodes which describe Non-Volatile
Memory, and properties related to them.


### Ordinals


These conveniences may be used for nodes which describe Dependency
tracking, and properties related to them.


### Pinctrl (pin control)


These are used to access pin control properties by name or index.

Devicetree nodes may have properties which specify pin control (sometimes known
as pin mux) settings. These are expressed using `pinctrl-<index>` properties
within the node, where the `<index>` values are contiguous integers starting
from 0. These may also be named using the `pinctrl-names` property.

Here is an example:

```DTS

node {
    ...
    pinctrl-0 = <&foo &bar ...>;
    pinctrl-1 = <&baz ...>;
    pinctrl-names = "default", "sleep";
};
```
Above, `pinctrl-0` has name `"default"`, and `pinctrl-1` has name
`"sleep"`. The `pinctrl-<index>` property values contain phandles. The
`&foo`, `&bar`, etc. phandles within the properties point to nodes whose
contents vary by platform, and which describe a pin configuration for the node.


### PWM


These conveniences may be used for nodes which describe PWM controllers and
properties related to them.


### Reset Controller


These conveniences may be used for nodes which describe reset controllers and
properties related to them.


### SPI


These conveniences may be used for nodes which describe either SPI controllers
or devices, depending on the case.
