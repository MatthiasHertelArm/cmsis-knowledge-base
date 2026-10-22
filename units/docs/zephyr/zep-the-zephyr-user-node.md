---
id: "zep-the-zephyr-user-node"
type: "concept"
domain: "project"
title: "The `/zephyr,user` node"
summary: "Zephyr's devicetree scripts handle the /zephyr,user node as a special case: you can put essentially arbitrary properties inside it and retrieve their values without having to write a binding."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/zephyr-user-node.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/zephyr-user-node.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr's devicetree scripts handle the `/zephyr,user` node as a special case:
you can put essentially arbitrary properties inside it and retrieve their
values without having to write a binding. It is meant as a convenient container
when only a few simple properties are needed. The type is inferred from the
values assigned to the property.


**Note:** This node is meant for sample code and user applications. It should not be used in the upstream Zephyr source code for device drivers, subsystems, etc.
