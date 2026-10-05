---
id: "txmw-chapter-4-module-apis-txm-module-object-allocate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Module APIs: txm_module_object_allocate"
summary: "Allocate memory in the object pool (created by the resident application) for a module object control block."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter4.md#txm-module-object-allocate"
license: "MIT"
mode: "V"
---

Allocate memory in the object pool (created by the resident application) for a module object control block.

### Prototype

```c
UINT txm_module_object_allocate(
   VOID **object_ptr, 
   ULONG object_size);
```

### Description

This service allocates memory for a module object from memory outside of the module, which helps prevent corruption of the object control block by the module's code. In memory protected systems, all object control blocks must be allocated with this API before they can be created.

### Input parameters

- **object_ptr** Destination of object pointer on successful allocation.
- **object_size** Size in bytes of the object to be allocated.

### Return values

- **TX_SUCCESS** (0x00) Successful object allocate.
- **TX_NO_MEMORY** (0x10) Not enough memory.
- **TX_NOT_AVAILABLE** (0x1D) Module manager has not created an object pool to allocate from

### Allowed from

Module threads

### Example

```c
TX_QUEUE *queue_pointer;

/* Allocate a control block for a module message queue. */
status = txm_module_object_allocate(&queue_pointer, sizeof(TX_QUEUE));

/* If status is TX_SUCCESS the queue_pointer points to
   memory allocated outside of the module and can be supplied
   to tx_queue_create to create a queue for the module. */
```

### See also

- [Threadx Module APIs](#Threadx_Module_APIs)
