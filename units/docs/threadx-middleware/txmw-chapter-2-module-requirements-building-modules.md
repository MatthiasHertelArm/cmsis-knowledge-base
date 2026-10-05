---
id: "txmw-chapter-2-module-requirements-building-modules"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Module requirements: Building Modules"
summary: "Building a module is dependent on the tool chain being used. See appendix for port-specific examples. Common activities to all ports include the following."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter2.md#building-modules"
license: "MIT"
mode: "V"
---

Building a module is dependent on the tool chain being used. See [appendix](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/appendix.md) for port-specific examples. Common activities to all ports include the following.

- Building a module library
- Building the module application

Each module is required to have a **txm_module_preamble** (setup specifically for the module) and the module library (for example, ***txm.a***).
