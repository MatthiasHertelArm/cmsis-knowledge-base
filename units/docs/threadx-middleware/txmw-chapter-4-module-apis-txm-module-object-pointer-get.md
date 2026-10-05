---
id: "txmw-chapter-4-module-apis-txm-module-object-pointer-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Module APIs: txm_module_object_pointer_get"
summary: "Find system object and retrieve object pointer"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter4.md#txm-module-object-pointer-get"
license: "MIT"
mode: "V"
---

Find system object and retrieve object pointer

### Prototype

```c
UINT txm_module_object_pointer_get(
   UINT object_type, CHAR *name, 
   VOID **object_ptr);
```

### Description

This service retrieves the object pointer of a particular type with a particular name. If the object is not found, an error is returned. Otherwise, if the object is found, the address of that object is placed in "object_ptr." This pointer can then be used to make system service calls, to interact with the resident code, and/or other loaded modules in the system.

### Input parameters

- **object_type** Type of ThreadX object requested. Valid types are as follows:
  - TXM_BLOCK_POOL_OBJECT
  - TXM_BYTE_POOL_OBJECT
  - TXM_EVENT_FLAGS_OBJECT
  - TXM_MUTEX_OBJECT
  - TXM_QUEUE_OBJECT
  - TXM_SEMAPHORE_OBJECT
  - TXM_THREAD_OBJECT
  - TXM_TIMER_OBJECT
  - TXM_IP_OBJECT
  - TXM_PACKET_POOL_OBJECT
  - TXM_UDP_SOCKET_OBJECT
  - TXM_TCP_SOCKET_OBJECT
- **name** Application-specific object name as defined when the object was created.
- **object_ptr** Destination for object pointer.

### Return values

- **TX_SUCCESS** (0x00) Successful object get.
- **TX_OPTION_ERROR** (0x08) Invalid object type.
- **TX_PTR_ERROR** (0x03) Invalid destination.
- **TX_SIZE_ERROR** (0x05) Invalid size.
- **TX_NO_INSTANCE** (0x0D) Object not found.

### Allowed from

Module threads

### Example

```c
TX_QUEUE *queue_pointer;

/* Find the pointer for "fft_queue" in the resident part
   of the application. */
status = txm_module_object_pointer_get(TXM_QUEUE_OBJECT,
         "fft_queue", &queue_pointer);

/* If status is TX_SUCCESS the found queue pointer is in
   "queue_pointer". This queue pointer can then be used to
   send messages to the "fft_queue." */
```

### See also

- [Threadx Module APIs](#Threadx_Module_APIs)
