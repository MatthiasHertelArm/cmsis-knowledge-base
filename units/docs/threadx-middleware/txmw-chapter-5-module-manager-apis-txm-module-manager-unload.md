---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-unload"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_unload"
summary: "This service unloads the previously loaded and stopped module, freeing all the associated module memory resources."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-unload"
license: "MIT"
mode: "V"
---

Unload the module.

### Prototype

```c
UINT txm_module_manager_unload(TXM_MODULE_INSTANCE *module_instance);
```

### Description

This service unloads the previously loaded and stopped module, freeing all the associated module memory resources.

### Input parameters

- **module_instance** Pointer to the instance of the module.

### Return values

- **TX_SUCCESS** 0x00) Successful module unload.
- **TX_CALLER_ERROR** (0x13) Invalid caller.
- **TX_NOT_AVAILABLE** (0x1D) Manager not initialized.
- **TX_NOT_DONE** (0x20) Invalid module or module not stopped.
- **TX_PTR_ERROR** (0x03) Invalid pointer or module instance.

### Allowed from

Initialization and threads

### Example

```c
/* Stop the module. */
txm_module_manager_stop(&my_module);

/* Unload the module. */
status = txm_module_manager_unload(&my_module);
```

### See also

- txm_module_manager_absolute_load
- txm_module_manager_file_load
- txm_module_manager_in_place_load
- txm_module_manager_memory_load
- txm_module_manager_stop
