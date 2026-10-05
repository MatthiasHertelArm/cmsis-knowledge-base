---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-smp-core-exclude-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX SMP Services: tx_thread_smp_core_exclude_get"
summary: "Gets the thread's current core exclusion"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter4.md#tx-thread-smp-core-exclude-get"
license: "MIT"
mode: "V"
---

Gets the thread's current core exclusion

### Prototype

```C
UINT tx_thread_smp_core_exclude_get(TX_THREAD *thread_ptr,
                         ULONG *exclusion_map_ptr);
```
### Description

This function returns the current core exclusion list.

### Parameters

- **thread_ptr**: Pointer to thread from which to retrieve the core exclusion.
- **exclusion_map_ptr**: Destination for current core exclusion bit map.

### Return Values

- **TX_SUCCESS**: (0x00) Successful retrieval of thread's core exclusion.
- **TX_THREAD_ERROR**: (0x0E) Invalid thread pointer.
- **TX_PTR_ERROR**: (0x03) Invalid exclusion destination pointer.

### Allowed From

Initialization, ISRs, threads, and timers

### Example

```C
ULONG excluded_cores;
/* Retrieve the core exclusion for "Thread 0". */
tx_thread_smp_core_exclude_get(&thread_0, &excluded_cores);
```

### See Also

- [Thread SMP Services](#Thread_SMP_Services)
