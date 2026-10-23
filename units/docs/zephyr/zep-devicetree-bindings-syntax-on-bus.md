---
id: "zep-devicetree-bindings-syntax-on-bus"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: On-bus"
summary: "If the node appears as a device on a bus, use on-bus: in the binding to say what type of bus."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

If the node appears as a device on a bus, use `on-bus:` in the binding to say
what type of bus.

For example, a binding for an external SPI memory chip should include this line:

```YAML

on-bus: spi
```
And a binding for an I2C based temperature sensor should include this line:

```YAML

on-bus: i2c
```
When looking for a binding for a node, the build system checks if the binding
for the parent node contains `bus: <bus type>`. If it does, then only
bindings with a matching `on-bus: <bus type>` and bindings without an
explicit `on-bus` are considered. Bindings with an explicit ``on-bus: <bus
type>` are searched for first, before bindings without an explicit `on-bus``.
The search repeats for each item in the node's `compatible` property, in
order.

This feature allows the same device to have different bindings depending on
what bus it appears on. For example, consider a sensor device with compatible
`manufacturer,sensor` which can be used via either I2C or SPI.

The sensor node may therefore appear in the devicetree as a child node of
either an SPI or an I2C controller, like this:

```devicetree

spi-bus@0 {
   /* ... some compatible with 'bus: spi', etc. ... */

   sensor@0 {
       compatible = "manufacturer,sensor";
       reg = <0>;
       /* ... */
   };
};

i2c-bus@0 {
   /* ... some compatible with 'bus: i2c', etc. ... */

   sensor@79 {
       compatible = "manufacturer,sensor";
       reg = <79>;
       /* ... */
   };
};
```
You can write two separate binding files which match these individual sensor
nodes, even though they have the same compatible:

```YAML

# manufacturer,sensor-spi.yaml, which matches sensor@0 on the SPI bus:
compatible: "manufacturer,sensor"
on-bus: spi

# manufacturer,sensor-i2c.yaml, which matches sensor@79 on the I2C bus:
compatible: "manufacturer,sensor"
properties:
  uses-clock-stretching:
    type: boolean
on-bus: i2c
```
Only `sensor@79` can have a `use-clock-stretching` property. The
bus-sensitive logic ignores `manufacturer,sensor-i2c.yaml` when searching
for a binding for `sensor@0`.
