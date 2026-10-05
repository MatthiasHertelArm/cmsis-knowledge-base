---
id: "txmw-chapter-3-module-manager-requireme-module-manager-starting"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager starting"
summary: "The Module Manager initiates execution of a previously-loaded module via the txm_module_manager_start API function. To initiate module execution, this function creates a thread that enters the module at the starting location specified in the module preamble."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-starting"
license: "MIT"
mode: "V"
---

The Module Manager initiates execution of a previously-loaded module via the ***txm_module_manager_start*** API function. To initiate module execution, this function creates a thread that enters the module at the starting location specified in the module preamble. The priority and stack size of this thread is also specified in the module preamble.
