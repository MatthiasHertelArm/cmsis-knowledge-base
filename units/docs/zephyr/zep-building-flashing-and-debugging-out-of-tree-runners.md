---
id: "zep-building-flashing-and-debugging-out-of-tree-runners"
type: "concept"
domain: "project"
title: "Building, Flashing and Debugging: Out of tree runners"
summary: "Zephyr modules can have external runners discovered by adding python files in their module.yml. Create an external runner class by inheriting from ZephyrBinaryRunner and implement all abstract methods."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/build-flash-debug.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/build-flash-debug.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr modules can have external runners discovered by adding python
files in their module.yml. Create an external runner class by
inheriting from `ZephyrBinaryRunner` and implement all abstract methods.


**Note:** Support for custom out-of-tree runners makes the `runners.core` module part of the public API and backwards incompatible changes need to undergo the
