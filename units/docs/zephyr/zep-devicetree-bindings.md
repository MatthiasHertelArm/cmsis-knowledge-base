---
id: "zep-devicetree-bindings"
type: "concept"
domain: "project"
title: "Devicetree bindings"
summary: "A devicetree on its own is only half the story for describing hardware, as it is a relatively unstructured format. Devicetree bindings provide the other half."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings.rst"
license: "Apache-2.0"
mode: "V"
---

A devicetree on its own is only half the story for describing hardware, as it
is a relatively unstructured format. *Devicetree bindings* provide the other
half.

A devicetree binding declares requirements on the contents of nodes, and
provides semantic information about the contents of valid nodes. Zephyr
devicetree bindings are YAML files in a custom format (Zephyr does not use the
dt-schema tools used by the Linux kernel).

These pages introduce bindings, describe what they do, note where they are
found, and explain their data format.


**Note:** See the devicetree_binding_index for reference information on bindings built in to Zephyr.
