---
id: "threadx-chapter-4-description-of-threadx-s-tx-time-get"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_time_get"
summary: "This service returns the contents of the internal system clock. Each timertick increases the internal system clock by one. The system clock is set to zero during initialization and can be changed to a specific value by the service tx_time_set."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-time-get"
license: "MIT"
mode: "V"
---

Retrieves the current time

Application Timers

### Prototype

```c
ULONG tx_time_get(VOID);
```

### Description

This service returns the contents of the internal system clock. Each timertick increases the internal system clock by one. The system clock is set to zero during initialization and can be changed to a specific value by the service ***tx_time_set***.

> **Note:** *The actual time each timer-tick represents is application-specific.*

### Parameters

None

### Return Values

- *system clock ticks** Value of the internal, free running, system clock.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible
No

### Example

```c
ULONG current_time;

/* Pickup the current system time, in timer-ticks. */
current_time = tx_time_get();

/* Current time now contains a copy of the internal system
clock. */
```

### See Also

- [Time Services](#Time_Services)
