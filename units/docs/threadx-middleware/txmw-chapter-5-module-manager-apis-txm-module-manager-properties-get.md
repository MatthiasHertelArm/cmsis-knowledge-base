---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-properties-get"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_properties_get"
summary: "This service returns the properties (specified in the preamble) of a module."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-properties-get"
license: "MIT"
mode: "V"
---

Get module properties.

### Prototype

```c
UINT txm_module_manager_properties_get(
    TXM_MODULE_INSTANCE *module_instance,
    ULONG *module_properties_ptr);
```

### Description

This service returns the properties (specified in the preamble) of a module.

### Input parameters

- **module_instance** Pointer to the module instance.
- **module_properties_ptr** Pointer to destination for module's properties.

### Return values

- **TX_SUCCESS** (0x00) Successful initialization.
- **TX_PTR_ERROR** (0x03) Invalid pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller.

### Allowed from

Threads

### Example

```c
TXM_MODULE_INSTANCE     my_module;
ULONG                   module_properties;

/* Initialize the module manager with 64KB of RAM starting at address 0x64010000. */
txm_module_manager_initialize((VOID *) 0x64010000, 0x10000);

/* Create an object memory pool in the next 64KB of memory. */
txm_module_manager_object_pool_create((VOID *) 0x64020000, 0x10000);

/* Load the module that has its code area at address 0x080F0000. */
txm_module_manager_in_place_load(&my_module, "my module", (VOID *) 0x080F0000);

/* Get module properties. */
txm_module_manager_properties_get(&my_module, &module_properties);
```

---
