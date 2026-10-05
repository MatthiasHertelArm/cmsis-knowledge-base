---
id: "txmw-chapter-3-module-manager-requireme-module-manager-initialization"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager initialization"
summary: "The resident portion of the application is responsible for calling the Module Manager initialization function txm_module_manager_initialize. This function sets up the internal structures for loading and unloading modules, including setting up the memory area used for allocating module memory."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-initialization"
license: "MIT"
mode: "V"
---

The resident portion of the application is responsible for calling the Module Manager initialization function ***txm_module_manager_initialize***. This function sets up the internal structures for loading and unloading modules, including setting up the memory area used for allocating module memory.
