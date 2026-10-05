---
id: "zep-devicetree-bindings-syntax-class"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Class"
summary: "If nodes matching the binding can be used as devices of one or more Zephyr device classes, use class: to declare those classes:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

If nodes matching the binding can be used as devices of one or more Zephyr
device classes, use `class:` to declare those classes:

```YAML

compatible: "manufacturer,adc"
class: adc
```
The value is a device class name or a list of names. Names use lowercase
letters, digits, `- and `; malformed or duplicate names are rejected.
Each name should match a device API class registered with
`DEVICE_API` (like `adc`); lowercase-and-hyphens names are
converted to lowercase-and-underscores C tokens the same way compatibles are.

The key declares which device API class(es) the node's drivers *can*
implement; which driver and API are actually built for a node remains a
Kconfig decision. A list value covers hardware whose drivers can implement
more than one API depending on configuration:

```YAML

compatible: "manufacturer,rtc"
class: [rtc, counter]
```
`class:` is normally declared once in a device class base binding (for
example `dts/bindings/adc/adc-controller.yaml`) so that every
binding including it inherits the class. When a binding and its included
files declare classes, the values are unioned: a binding that includes
several class base bindings belongs to all of their classes.

Class membership can be queried at build time with
`DT_NODE_HAS_CLASS`, iterated with
`DT_FOREACH_CLASS_STATUS_OKAY`, counted with
`DT_NUM_CLASS_STATUS_OKAY`, and tested from Kconfig with
`$(dt_class_enabled,<class name>)`.

To add a class to a device whose binding cannot be changed, for example to
classify an upstream device from a downstream module, define a more specific
compatible whose binding includes the original binding and declares the
class, and list both compatibles on the node:

```YAML

# vnd,foo-classed.yaml
compatible: "vnd,foo-classed"
include: vnd,foo.yaml
class: xyz
```
```devicetree

compatible = "vnd,foo-classed", "vnd,foo";
```
The node's binding, and with it its classes, comes from the first compatible
that has a binding; drivers match on any of the node's compatibles, so the
original driver still binds. Two bindings for the same compatible are an
error, so an existing binding cannot be shadowed.
