---
id: "zep-introduction-to-devicetree-binding-a-simple-example"
type: "concept"
domain: "project"
title: "Introduction to Devicetree Bindings: A simple example"
summary: "Here is a minimal binding file which matches the node:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-intro.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-intro.rst"
license: "Apache-2.0"
mode: "V"
---

Here is an example devicetree node:

```devicetree

/* Node in a DTS file */
bar-device {
    compatible = "foo-company,bar-device";
     num-foos = <3>;
};
```
Here is a minimal binding file which matches the node:

```yaml

# A YAML binding matching the node

compatible: "foo-company,bar-device"

properties:
  num-foos:
    type: int
    required: true
```
The build system matches the `bar-device` node to its YAML binding because
the node's `compatible` property matches the binding's `compatible:` line.
