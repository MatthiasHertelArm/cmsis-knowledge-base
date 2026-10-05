---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-start"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_start"
summary: "This service starts execution of the specified, already loaded module."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-start"
license: "MIT"
mode: "V"
---

Start execution of the module.

### Prototype

```c
UINT txm_module_manager_start(TXM_MODULE_INSTANCE *module_instance);
```

### Description

This service starts execution of the specified, already loaded module.

### Input parameters

- **module_instance** Pointer to previously loaded module instance.

### Return values

- **TX_SUCCESS** (0x00) Successful module start.
- **TX_CALLER_ERROR** (0x13) Invalid caller.
- **TX_NOT_AVAILABLE** (0x1D) Manager not initialized.
- **TX_PTR_ERROR** (0x03) Invalid pointer or module instance.
- **TX_START_ERROR** (0x10) Module already started.

### Allowed from

Initialization and threads

### Example

```c
/* Start the module. */
txm_module_manager_start(&my_module);

/* Let the module run for a while. */
tx_thread_sleep(2000);

/* Stop the module. */
txm_module_manager_stop(&my_module);

/* Unload the module. */
txm_module_manager_unload(&my_module);
```

### See also

- txm_module_manager_stop

---
