---
id: "zep-devicetree-bindings-syntax-bus"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Bus"
summary: "If the node is a bus controller, use bus: in the binding to say what type of bus. For example, a binding for a SPI peripheral on an SoC would look like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

If the node is a bus controller, use `bus:` in the binding to say what type
of bus. For example, a binding for a SPI peripheral on an SoC would look like
this:

```YAML

compatible: "manufacturer,spi-peripheral"
bus: spi
# ...
```
The presence of this key in the binding informs the build system that the
children of any node matching this binding appear on this type of bus.

This in turn influences the way `on-bus:` is used to match bindings for the
child nodes.

For a single bus supporting multiple protocols, e.g. I3C and I2C, the `bus:`
in the binding can have a list as value:

```YAML

compatible: "manufacturer,i3c-controller"
bus: [i3c, i2c]
# ...
```
