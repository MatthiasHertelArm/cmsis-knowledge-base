---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-stop"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_stop"
summary: "This service stops a module that was previously loaded and started. Stopping a module includes executing the module's optional stop thread, terminating all threads, and deleting all resources associated with the module."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-stop"
license: "MIT"
mode: "V"
---

Stop execution of the module.

### Prototype

```c
UINT txm_module_manager_stop(TXM_MODULE_INSTANCE *module_instance);
```

### Description

This service stops a module that was previously loaded and started. Stopping a module includes executing the module's optional stop thread, terminating all threads, and deleting all resources associated with the module.

### Input parameters

- **module_instance** Pointer to module instance.

### Return values

- **TX_SUCCESS** (0x00) Successful module stop.
- **TX_CALLER_ERROR** (0x13) Invalid caller.
- **TX_NOT_AVAILABLE** (0x1D) Manager not initialized.
- **TX_PTR_ERROR** (0x03) Invalid pointer or module instance.
- **TX_START_ERROR** (0x10) Module not started.

### Allowed from

Threads

### Example

```c
/* Start the module. */
txm_module_manager_start(&my_module);

/* Let the module run for a while. */
tx_thread_sleep(20000);

/* Stop the module. */
txm_module_manager_stop(&my_module);

/* Unload the module. */
txm_module_manager_unload(&my_module);
```

### See also

- txm_module_manager_start

---
