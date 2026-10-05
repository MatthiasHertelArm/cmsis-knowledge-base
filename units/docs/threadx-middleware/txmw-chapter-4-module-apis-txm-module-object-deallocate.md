---
id: "txmw-chapter-4-module-apis-txm-module-object-deallocate"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Module APIs: txm_module_object_deallocate"
summary: "Deallocate previously allocated object memory"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter4.md#txm-module-object-deallocate"
license: "MIT"
mode: "V"
---

Deallocate previously allocated object memory

### Prototype

```c
UINT txm_module_object_deallocate(VOID *object_ptr);
```

### Description

***This service has been deprecated because it is no longer needed***.

The memory that was previously allocated via ***txm_module_object_allocate*** is deallocated in the ***tx_\*_delete*** service.

### Input parameters

- **object_ptr** Object pointer to deallocate.

### Return values

- **TX_SUCCESS** (0x00) Successful object allocate.

### Allowed from

Module threads

### Example

```c
TX_QUEUE *queue_pointer;

/* Deallocate control block for a module message queue. */
status = txm_module_object_deallocate(queue_pointer);

/* If status is TX_SUCCESS the object memory associated
   with queue_pointer is deallocated. */
```

### See also

- [Threadx Module APIs](#Threadx_Module_APIs)
