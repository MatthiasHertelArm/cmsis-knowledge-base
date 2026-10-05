---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-initialize"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_initialize"
summary: "This service initializes the Module Manager's internal resources, including the memory area used for loading modules."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-initialize"
license: "MIT"
mode: "V"
---

Initialize the module manager.

### Prototype

```c
UINT txm_module_manager_initialize(
    VOID *module_memory_start,
    ULONG module_memory_size);
```

### Description

This service initializes the Module Manager's internal resources, including the memory area used for loading modules.

### Input parameters

- **module_memory_start** Pointer to the start of module memory.
- **module_memory_size** Size in bytes of the module memory.

### Return values

- **TX_SUCCESS** (0x00) Successful initialization.
- **TX_CALLER_ERROR** (0x13) Invalid caller.

### Allowed from

Initialization and threads

### Example

```c
/* Initialize the module manager with 64KB of RAM starting at
   address 0x64010000. */
txm_module_manager_initialize((VOID *) 0x64010000, 0x10000);
```

### See also

- txm_module_manager_object_pool_create

---
