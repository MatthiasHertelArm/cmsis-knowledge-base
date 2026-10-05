---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-maximum-module-priori"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_maximum_module_priority_set"
summary: "Set the maximum thread priority allowed in a module."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-maximum-module-priority-set"
license: "MIT"
mode: "V"
---

Set the maximum thread priority allowed in a module.

### Prototype

```c
UINT txm_module_manager_maximum_module_priority_set(
         TXM_MODULE_INSTANCE *module_instance,
         UINT priority);
```

### Description

This service sets the maximum thread priority allowed in a module.

### Input parameters

- **module_instance** Pointer to the instance of the module.
- **priority** Maximum thread priority.

### Return values

- **TX_SUCCESS** (0x00) Successful initialization.
- **TX_NOT_AVAILABLE** (0x1D) Manager not initialized.
- **TX_PTR_ERROR** (0x03) Invalid module instance.
- **TX_START_ERROR** (0x10) Module not in loaded state.

### Allowed from

Initialization and threads

### Example

```c
/* Load the module that has its code area at address 0x080F0000. */
txm_module_manager_in_place_load(&my_module, "my module", (VOID *) 0x080F0000);

/* Set the maximum thread priority in my_module to 5. */
txm_module_manager_maximum_module_priority_set(&my_module, 5);
```

---
