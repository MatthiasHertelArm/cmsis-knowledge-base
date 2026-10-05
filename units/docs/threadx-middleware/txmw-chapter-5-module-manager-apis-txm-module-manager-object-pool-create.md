---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-object-pool-create"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_object_pool_create"
summary: "This service creates a Module Manager object memory pool that the modules can allocate ThreadX/NetX Duo objects from, thereby keeping the system object out of the module's memory area."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-object-pool-create"
license: "MIT"
mode: "V"
---

Create an object pool for modules.

### Prototype

```c
UINT txm_module_manager_object_pool_create(
    VOID *pool_memory_start,
    ULONG pool_memory_size);
```

### Description

This service creates a Module Manager object memory pool that the modules can allocate ThreadX/NetX Duo objects from, thereby keeping the system object out of the module's memory area.

### Input parameters

- **pool_memory_start** Pointer to the start of object memory.
- **pool_memory_size** Size in bytes of the object memory pool.

### Return values

- **TX_SUCCESS** (0x00) Successful initialization.
- **TX_CALLER_ERROR** (0x13) Invalid caller.

### Allowed from

Initialization and threads

### Example

```c
TXM_MODULE_INSTANCE my_module;

/* Initialize the module manager with 64KB of RAM starting at address 0x64010000. */
txm_module_manager_initialize((VOID *) 0x64010000, 0x10000);

/* Create an object memory pool in the next 64KB of memory. */
txm_module_manager_object_pool_create((VOID *) 0x64020000, 0x10000);
```

### See also

- txm_module_manager_initialize

---
