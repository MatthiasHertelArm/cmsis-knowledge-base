---
id: "txmw-chapter-5-module-manager-apis-summary-of-module-manager-apis"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: Summary of Module Manager APIs"
summary: "There are several additional APIs available to the resident portion of the application, as follows."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#summary-of-module-manager-apis"
license: "MIT"
mode: "V"
---

There are several additional APIs available to the resident portion of the application, as follows.

- ***txm_module_manager_absolute_load*** - *Module's code and data are at absolute (fixed) addresses*
- ***txm_module_manager_external_memory_enable*** - *Enable module access to a shared memory space*
- ***txm_module_manager_file_load*** - *Load module from file via FileX*
- ***txm_module_manager_in_place_load*** - *Load module data, execute in place*
- ***txm_module_manager_initialize*** - *Initialize the module manager*
- ***txm_module_manager_mm_initialize*** - *Initialize the memory management hardware*
- ***txm_module_manager_maximum_module_priority_set*** - *Set the maximum thread priority allowed in a module*
- ***txm_module_manager_memory_fault_notify*** - *Register an application callback on memory fault*
- ***txm_module_manager_memory_load*** - *Load the module from memory*
- ***txm_module_manager_object_pool_create*** - *Create an object pool for modules*
- ***txm_module_manager_properties_get*** - *Get module properties*
- ***txm_module_manager_start*** - *Start execution of the specified module*
- ***txm_module_manager_stop*** - *Stop execution of the specified module*
- ***txm_module_manager_unload*** - *Unload the module*

---
