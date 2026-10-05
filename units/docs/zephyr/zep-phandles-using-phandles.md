---
id: "zep-phandles-using-phandles"
type: "concept"
domain: "project"
title: "Phandles: Using phandles"
summary: "Here are the main ways you will use phandles."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/phandles.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/phandles.rst"
license: "Apache-2.0"
mode: "V"
---

**Note:** "Type" in this section refers to one of the type names documented in

Here are the main ways you will use phandles.


### One node: phandle type


You can use phandles to refer to `node-b` from `node-a`, where `node-b`
is related to `node-a` in some way.

One common example is when `node-a` represents some hardware that
generates an interrupt, and `node-b` represents the interrupt
controller that receives the asserted interrupt. In this case, you could
write:

```DTS

node_b: node-b {
        interrupt-controller;
};

node-a {
        interrupt-parent = <&node_b>;
};
```
This uses the standard `interrupt-parent` property defined in the
devicetree specification to capture the relationship between the two nodes.

These properties have type `phandle`.


### Zero or more nodes: phandles type


You can use phandles to make an array of references to other nodes.

One common example occurs in pin control. Pin control
properties like `pinctrl-0`, `pinctrl-1` etc. may contain multiple
phandles, each of which "points" to a node containing information related to
pin configuration for that hardware peripheral. Here's an example of six
phandles in a single property:

```DTS

pinctrl-0 = <&quadspi_clk_pe10 &quadspi_ncs_pe11
             &quadspi_bk1_io0_pe12 &quadspi_bk1_io1_pe13
             &quadspi_bk1_io2_pe14 &quadspi_bk1_io3_pe15>;
```
These properties have type `phandles`.


### Zero or more nodes with metadata: phandle-array type


You can use phandles to refer to and configure one or more resources that are
"owned" by some other node.

This is the most complex case. There are examples and more details in the
next section.

These properties have type `phandle-array`.
