---
id: "threadx-chapter-3-threadx-apis-for-armv8-m-tx-thread-secure-stack-allocate"
type: "concept"
domain: "rtos"
title: "Chapter 3  ThreadX APIs for ARMv8-M: tx_thread_secure_stack_allocate"
summary: "Allocate a thread stack in secure memory."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/user-guide-armv8m/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/user-guide-armv8m/chapter3.md#tx-thread-secure-stack-allocate"
license: "MIT"
mode: "V"
---

Allocate a thread stack in secure memory.

### Prototype

```c
UINT tx_thread_secure_stack_allocate(
    TX_THREAD *thread_ptr, 
    ULONG stack_size);
```

### Description

This service allocates a stack of size stack_size bytes in secure memory. This function should be called for every thread that calls secure functions.

### Input Parameters

- **thread_ptr** Pointer to previously created thread.

- **stack_size** Size of secure stack.

### Return Values

- **TX_SUCCESS** (0x00) Successful request.

- **TX_SIZE_ERROR** (0x05) Stack size out of range.

- **TX_THREAD_ERROR** (0x0E) Invalid thread pointer.

- **TX_NO_MEMORY** (0x10) Unable to allocate memory.

- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was compiled to run in secure mode.

### Allowed From

Initialization, threads

### Example

```c
/* Create thread.  */
tx_thread_create(&thread_0, "thread 0", thread_0_entry, 0, pointer, DEMO_STACK_SIZE, 1, 1, TX_NO_TIME_SLICE, TX_AUTO_START);

/* Allocate secure stack so this thread can call secure functions.  */
status = tx_thread_secure_stack_allocate(&thread_0, 256);

/* If status is TX_SUCCESS the request was successful.  */
```

### See Also

tx_thread_secure_stack_free
