---
id: "zep-devicetree-howtos-find-a-devicetree-binding"
type: "concept"
domain: "project"
title: "Devicetree HOWTOs: Find a devicetree binding"
summary: "dt-bindings are YAML files which declare what you can do with the nodes they describe, so it's critical to be able to find them for the nodes you are using."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/howtos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/howtos.rst"
license: "Apache-2.0"
mode: "V"
---

dt-bindings are YAML files which declare what you can do with the nodes
they describe, so it's critical to be able to find them for the nodes you are
using.

If you don't have them already, get-devicetree-outputs. To find a node's
binding, open the generated header file, which starts with a list of nodes in a
block comment:

```c

/*
 * [...]
 * Nodes in dependency order (ordinal and path):
 *   0   /
 *   1   /aliases
 *   2   /chosen
 *   3   /flash@0
 *   4   /memory@20000000
 *          (etc.)
 * [...]
 */
```
Make note of the path to the node you want to find, like `/flash@0`. Search
for the node's output in the file, which starts with something like this if the
node has a matching binding:

```c

/*
 * Devicetree node:
 *   /flash@0
 *
 * Binding (compatible = soc-nv-flash):
 *   $ZEPHYR_BASE/dts/bindings/mtd/soc-nv-flash.yaml
 * [...]
 */
```
See missing-dt-binding for troubleshooting.
