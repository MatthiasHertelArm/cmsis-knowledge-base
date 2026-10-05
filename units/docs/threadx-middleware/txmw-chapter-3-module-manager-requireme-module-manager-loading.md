---
id: "txmw-chapter-3-module-manager-requireme-module-manager-loading"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager loading"
summary: "The Module Manager can load modules dynamically into the module memory from binary module files or from a module code section that is already present in the resident code area."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-loading"
license: "MIT"
mode: "V"
---

The Module Manager can load modules dynamically into the module memory from binary module files or from a module code section that is already present in the resident code area. In addition, the module manager can execute code in place, that is, only the module data is allocated in the module memory and the code execution is done in place. The following Module Manager load API functions are available.

* ***txm_module_manager_file_load***

* ***txm_module_manager_in_place_load***

* ***txm_module_manager_memory_load***

The memory protected version of the Module Manager also makes sure that the module is loaded with the proper alignment and the memory management registers are set up properly for each module. When memory protection is enabled via the module preamble options, module memory access is restricted to the module code and data areas.
