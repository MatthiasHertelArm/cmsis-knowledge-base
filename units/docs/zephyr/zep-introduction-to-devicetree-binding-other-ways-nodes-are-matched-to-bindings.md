---
id: "zep-introduction-to-devicetree-binding-other-ways-nodes-are-matched-to-bindings"
type: "concept"
domain: "project"
title: "Introduction to Devicetree Bindings: Other ways nodes are matched to bindings"
summary: "If a node has more than one string in its compatible property, the build system looks for compatible bindings in the listed order and uses the first match."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-intro.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-intro.rst"
license: "Apache-2.0"
mode: "V"
---

If a node has more than one string in its `compatible` property, the build
system looks for compatible bindings in the listed order and uses the first
match.

Take this node as an example:

```devicetree

baz-device {
    compatible = "foo-company,baz-device", "generic-baz-device";
};
```
The `baz-device` node would get matched to a binding with a ``compatible:
"generic-baz-device"`` line if the build system can't find a binding with a
`compatible: "foo-company,baz-device"` line.

Nodes without compatible properties can be matched to bindings associated with
their parent nodes. These are called "child bindings". If a node describes
hardware on a bus, like I2C or SPI, then the bus type is also taken into
account when matching nodes to bindings. (See dt-bindings-on-bus for
details).

See dt-zephyr-user for information about a special node that doesn't
require any binding.
