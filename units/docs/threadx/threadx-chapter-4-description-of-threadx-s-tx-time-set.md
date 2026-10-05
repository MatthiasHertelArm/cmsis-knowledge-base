---
id: "threadx-chapter-4-description-of-threadx-s-tx-time-set"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_time_set"
summary: "This service sets the internal system clock to the specified value. Each timer-tick increases the internal system clock by one."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-time-set"
license: "MIT"
mode: "V"
---

Sets the current time

### Prototype

```c
VOID tx_time_set(ULONG new_time);
```

### Description

This service sets the internal system clock to the specified value. Each timer-tick increases the internal system clock by one.

> **Note:** *The actual time each timer-tick represents is application specific.*

### Parameters

- *new_time*: New time to put in the system clock, legal values range from 0 through 0xFFFFFFFF.

### Return Values

None

### Allowed From

Threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
/* Set the internal system time to 0x1234. */
tx_time_set(0x1234);

/* Current time now contains 0x1234 until the next timer
interrupt. */
```

### See Also

- [Time Services](#Time_Services)
