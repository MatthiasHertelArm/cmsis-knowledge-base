---
id: "zep-devicetree-bindings-syntax-nexus-nodes-and-maps"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Nexus nodes and maps"
summary: "All phandle-array type properties support mapping through -map properties, e.g. gpio-map, as defined by the Devicetree specification."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

All `phandle-array` type properties support mapping through `*-map`
properties, e.g. `gpio-map`, as defined by the Devicetree specification.

This is used, for example, to define connector nodes for common breakout
headers, such as the `arduino_header` nodes that are conventionally defined
in the devicetrees for boards with Arduino compatible expansion headers.
