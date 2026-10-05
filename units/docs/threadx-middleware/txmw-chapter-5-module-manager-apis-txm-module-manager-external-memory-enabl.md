---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-external-memory-enabl"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_external_memory_enable"
summary: "Enable module to access a shared memory space."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-external-memory-enable"
license: "MIT"
mode: "V"
---

Enable module to access a shared memory space.

### Prototype

```c
UINT txm_module_manager_external_memory_enable(
     TXM_MODULE_INSTANCE *module_instance,
     VOID *start_address,
     ULONG length,
     UINT attributes);
```

### Description

This service creates an entry in the memory management hardware table for a shared memory region that the module can access.

### Input parameters

- **module_instance** Pointer to the instance of the module.
- **start_address** Starting address of shared memory region.
- **length** Length of shared memory region.
- **attributes** Attributes of memory region (cache, read, write, etc.). Attributes are port-specific; see [appendix](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/appendix.md) for attributes format.

### Return values

- **TX_SUCCESS** (0x00) Memory entry created successfully.
- **TX_NOT_AVAILABLE** (0x1D) Manager not initialized or feature not available.
- **TX_PTR_ERROR** (0x03) Invalid module instance.
- **TX_START_ERROR** (0x10) Module not in loaded state.
- **TXM_MODULE_ALIGNMENT_ERROR** (0xF0) Invalid start address alignment.
- **TXM_MODULE_INVALID_PROPERTIES** (0xF3) Incompatible properties.

### Allowed from

Initialization and threads

### Example

```c
TXM_MODULE_INSTANCE my_module;

/* Initialize the module manager with 64KB of RAM starting at address 0x64010000. */
txm_module_manager_initialize((VOID *) 0x64010000, 0x10000);

/* Load the module that has its code area at address 0x080F0000. */
txm_module_manager_in_place_load(&my_module, "my module", (VOID *) 0x080F0000);

/* Create a shared memory space 256 bytes long at address 0x64005000
   with read & write, no execute, outer & inner write back cache
   attributes. Note that these attributes are port-specific. */
txm_module_manager_external_memory_enable(&my_module, (VOID*)0x64005000, 256, 0x3F);
```

---
