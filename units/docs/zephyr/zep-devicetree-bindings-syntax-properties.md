---
id: "zep-devicetree-bindings-syntax-properties"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties"
summary: "The properties: key describes properties that nodes which match the binding contain. For example, a binding for a UART peripheral might look something like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

The `properties:` key describes properties that nodes which match the binding
contain. For example, a binding for a UART peripheral might look something like
this:

```YAML

compatible: "manufacturer,serial"

properties:
  reg:
    type: array
    description: UART peripheral MMIO register space
    required: true
  current-speed:
    type: int
    description: current baud rate
    required: true
```
In this example, a node with compatible `"manufacturer,serial"` must contain
a property named `current-speed`. The property's value must be a single
integer. Similarly, the node must contain a `reg` property.

The build system uses bindings to generate C macros for devicetree properties
that appear in DTS files. You can read more about how to get property values in
source code from these macros in dt-from-c. Generally speaking, the
build system only generates macros for properties listed in the `properties:`
key for the matching binding. Properties not mentioned in the binding are
generally ignored by the build system.

The one exception is that the build system will always generate macros for
standard properties, like reg, whose meaning is
defined by the devicetree specification. This happens regardless of whether the
node has a matching binding or not.
