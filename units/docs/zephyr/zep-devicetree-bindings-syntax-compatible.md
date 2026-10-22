---
id: "zep-devicetree-bindings-syntax-compatible"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Compatible"
summary: "This key is used to match nodes to this binding as described in dt-binding-compat. It should look like this in a binding file:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

This key is used to match nodes to this binding as described in
dt-binding-compat. It should look like this in a binding file:

```YAML

# Note the comma-separated vendor prefix and device name
compatible: "manufacturer,device"
```
This devicetree node would match the above binding:

```devicetree

device {
    compatible = "manufacturer,device";
};
```
Assuming no binding has `compatible: "manufacturer,device-v2"`, it would also
match this node:

```devicetree

device-2 {
    compatible = "manufacturer,device-v2", "manufacturer,device";
};
```
Each node's `compatible` property is tried in order. The
bindings are uniquely identified by a pair of
(compatible,
on-bus), where the
on-bus may be unspecified. A specified
on-bus takes precedence over unspecified. The
first matching binding is used.

For the following device:

```devicetree

spi-bus {
        device-3 {
                compatible = "manufacturer,device";
        };
};
```
The following two bindings can coexist and would match in the following order:

`manufacturer,device-spi.yaml`

```YAML

compatible: "manufacturer,device"
on-bus: spi
```
`manufacturer,device.yaml`

```YAML

compatible: "manufacturer,device"
```
The following binding can coexist but would not match.

`manufacturer,device-i2c.yaml`

```YAML

compatible: "manufacturer,device"
on-bus: i2c
```
If more than one matching binding for a compatible is found, an error is raised.

The `manufacturer` prefix identifies the device vendor. See
`dts/bindings/vendor-prefixes.txt` for a list of accepted vendor
prefixes. The `device` part is usually from the datasheet.

Some bindings apply to a generic class of devices which do not have a specific
vendor. In these cases, there is no vendor prefix. One example is the
`gpio-leds` compatible which is commonly used to describe board
LEDs connected to GPIOs.
