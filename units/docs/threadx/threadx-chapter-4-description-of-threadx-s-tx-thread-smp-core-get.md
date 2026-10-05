---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-smp-core-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX SMP Services: tx_thread_smp_core_get"
summary: "Retrieve currently executing core of caller"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter4.md#tx-thread-smp-core-get"
license: "MIT"
mode: "V"
---

Retrieve currently executing core of caller

### Prototype

```C
UINT  tx_thread_smp_core_get(void);
```
### Description

This function returns the core ID of the core executing this service.

### Parameters

None

### Return Values

- core_id: ID of currently executing core, (0 through TX_THREAD_SMP_MAX_CORES-1)

### Allowed From

Initialization, ISRs, threads, and timers

### Example

```C
UINT core;
/* Pickup the currently executing core. */
core = tx_thread_smp_core_get();

/* At this point, "core" contains the executing core ID. */
```
### See Also

- [Thread SMP Services](#Thread_SMP_Services)
