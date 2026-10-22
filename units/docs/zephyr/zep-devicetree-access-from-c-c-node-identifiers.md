---
id: "zep-devicetree-access-from-c-c-node-identifiers"
type: "concept"
domain: "project"
title: "Devicetree access from C/C++: Node identifiers"
summary: "To get information about a particular devicetree node, you need a node identifier for it. This is a just a C macro that refers to the node."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/api-usage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/api-usage.rst"
license: "Apache-2.0"
mode: "V"
---

To get information about a particular devicetree node, you need a *node
identifier* for it. This is a just a C macro that refers to the node.

These are the main ways to get a node identifier:

By path
   Use `DT_PATH()` along with the node's full path in the devicetree,
   starting from the root node. This is mostly useful if you happen to know the
   exact node you're looking for.

By node label
   Use `DT_NODELABEL()` to get a node identifier from a :ref:`node
   label <dt-node-labels>`. Node labels are often provided by SoC `.dtsi`
   files to give nodes names that match the SoC datasheet, like `i2c1`,
   `spi2`, etc.

By alias
   Use `DT_ALIAS()` to get a node identifier for a property of the
   special `/aliases` node. This is sometimes done by applications (like
   blinky, which uses the `led0` alias) that need to
   refer to *some* device of a particular type ("the board's user LED") but
   don't care which one is used.
   You may also use `DT_HAS_ALIAS()` to verify whether an alias
   node exists.

By instance number
   This is done primarily by device drivers, as instance numbers are a way to
   refer to individual nodes based on a matching compatible. Get these with
   `DT_INST()`, but be careful doing so. See below.

By chosen node
   Use `DT_CHOSEN()` to get a node identifier for `/chosen` node
   properties.

By parent/child
   Use `DT_PARENT()` and `DT_CHILD()` to get a node identifier
   for a parent or child node, starting from a node identifier you already have.

Two node identifiers which refer to the same node are identical and can be used
interchangeably.

Here's a DTS fragment for some imaginary hardware we'll return to throughout
this file for examples:

Here are a few ways to get node identifiers for the `i2c@40002000` node:

- `DT_PATH(soc, i2c_40002000)`
- `DT_NODELABEL(i2c1)`
- `DT_ALIAS(sensor_controller)`
- `DT_INST(x, vnd_soc_i2c)` for some unknown number `x`. See the
  `DT_INST()` documentation for details.


**Important:** Non-alphanumeric characters like dash (`-`) and the at sign (`@) in devicetree names are converted to underscores (`). The names in a DTS are also converted to lowercase.
