---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-memory-fault-notify"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_memory_fault_notify"
summary: "Register an application callback on memory fault."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-memory-fault-notify"
license: "MIT"
mode: "V"
---

Register an application callback on memory fault.

### Prototype

```c
UINT txm_module_manager_memory_fault_notify(
     VOID (*notify_function)(TX_THREAD *, MODULE_INSTANCE *));
```

### Description

This service registers the specified application memory fault notification callback function with the Module Manager. If a memory fault occurs, this function is called with a pointer to the offending thread and the module instance corresponding to the offending thread. The Module Manager processing automatically terminates the offending thread, but leaves any other threads in the module untouched. It is up to the application to decide what to do with the module associated
with the memory fault.

Please see the internal **_txm_module_manager_memory_fault_info** struct for specific information on the memory fault itself.

> **Note:** The memory fault notification callback function is executed directly from the memory fault exception, so only ThreadX APIs Allowed from interrupt service routines can be called. Thus, in order to stop and unload the offending module, the application notification callback must send a signal to an application task so that the module can be stopped and unloaded.

### Input parameters

- **notify_function** Function pointer to the application's memory fault notification callback. Supplying a NULL value disables the memory fault notification.

### Return values

- **TX_SUCCESS** (0x00) Successful notification function registration.

### Allowed from

Initialization and threads

### Example

```c
/* Register a memory fault callback. */
txm_module_manager_memory_fault_notify(my_memory_fault_handler);
```

---
