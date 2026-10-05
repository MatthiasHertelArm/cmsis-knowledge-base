---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-memory-load"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_memory_load"
summary: "This service loads the module's code and data area into the module memory area set up by txm_module_manager_initialize and prepares it for execution."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-memory-load"
license: "MIT"
mode: "V"
---

Load module from memory.

### Prototype

```c
UINT txm_module_manager_memory_load (
    TXM_MODULE_INSTANCE *module_instance,
    CHAR *module_name,
    VOID *location);
```

### Description

This service loads the module's code and data area into the module memory area set up by ***txm_module_manager_initialize*** and prepares it for execution.

### Input parameters

- **module_instance** Pointer to the instance of the module.
- **module_name** Name of the module.
- **location** Pointer to module's code area, preamble first.

### Return values

- **TX_SUCCESS** (0x00) Successful module load.
- **TX_CALLER_ERROR** (0x13) Invalid caller.
- **TX_NOT_AVAILABLE** (0x1D) Manager not initialized.
- **TX_NO_MEMORY** (0x10) Not enough memory to load module.
- **TX_PTR_ERROR** (0x03) Invalid pointer, module instance, or module preamble.
- **TXM_MODULE_ALIGNMENT_ERROR** (0xF0) Invalid alignment.
- **TXM_MODULE_ALREADY_LOADED** (0xF1) Module already loaded.
- **TXM_MODULE_INVALID** (0xF2) Invalid module preamble.
- **TXM_MODULE_INVALID_PROPERTIES** (0xF3) Incompatible properties.

### Allowed from

Initialization and threads

### Example

```c
TXM_MODULE_INSTANCE     my_module;

/* Initialize the module manager with 64KB of RAM starting at address 0x64010000. */
txm_module_manager_initialize((VOID *) 0x64010000, 0x10000);

/* Load the module that has its code area at address 0x080F0000. */
 txm_module_manager_memory_load(&my_module, "my module", (VOID *) 0x080F0000);
```

### See also

- txm_module_manager_file_load
- txm_module_manager_in_place_load
- txm_module_manager_unload

---
