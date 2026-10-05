---
id: "txmw-chapter-3-module-manager-requireme-module-manager-building"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager building"
summary: "The txm_module_manager\\ source files must be added to the ThreadX library."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-building"
license: "MIT"
mode: "V"
---

The ***txm_module_manager_\**** source files must be added to the ThreadX library.

A ThreadX Module Manager application is effectively the same as a standard ThreadX application, which is one or more application files linked together with the ThreadX library ***tx.a***. Building a module manager application is dependent on the tool chain being used. See [appendix](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/appendix.md) for port-specific examples.
