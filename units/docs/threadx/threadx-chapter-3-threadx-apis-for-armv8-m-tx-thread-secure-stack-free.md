---
id: "threadx-chapter-3-threadx-apis-for-armv8-m-tx-thread-secure-stack-free"
type: "concept"
domain: "rtos"
title: "Chapter 3  ThreadX APIs for ARMv8-M: tx_thread_secure_stack_free"
summary: "This service frees a thread's secure stack in secure memory. This function should be called if a thread has a secure stack and when the thread no longer needs to call secure functions or the thread is deleted."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/user-guide-armv8m/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/user-guide-armv8m/chapter3.md#tx-thread-secure-stack-free"
license: "MIT"
mode: "V"
---

Free a thread stack in secure memory. 

### Prototype

```c
UINT tx_thread_secure_stack_free(TX_THREAD *thread_ptr);
```

### Description

This service frees a thread's secure stack in secure memory. This function should be called if a thread has a secure stack and when the thread no longer needs to call secure functions or the thread is deleted.

### Input Parameters

- **thread_ptr** Pointer to previously created thread.

### Return Values

- **TX_SUCCESS** (0x00) Successful request.

- **TX_THREAD_ERROR** (0x0E) Invalid thread pointer.

- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was compiled to run in secure mode.

### Allowed From

Initialization, threads

### Example

```c
/* Free thread's secure stack.  */
status = tx_thread_secure_stack_free(&thread_0);

/* If status is TX_SUCCESS the request was successful.  */

/* Delete thread.  */
tx_thread_delete(&thread_0);
```
