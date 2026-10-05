---
id: "threadx-chapter-4-description-of-threadx-s-tx-interrupt-control"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_interrupt_control"
summary: "This service enables or disables interrupts as specified by the input parameter new_posture."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-interrupt-control"
license: "MIT"
mode: "V"
---

Enable and disable interrupts

### Prototype

```c
UINT tx_interrupt_control(UINT new_posture);
```

### Description

This service enables or disables interrupts as specified by the input parameter *new_posture*.

> **Note:** *If this service is called from an application thread, the interrupt posture remains part of that thread's context. For example, if the thread calls this routine to disable interrupts and then suspends, when it is resumed, interrupts are disabled again.*

> **Warning:** *This service should not be used to enable interrupts during initialization! Doing so could cause unpredictable results.*

### Parameters

- *new_posture*: This parameter specifies whether interrupts are disabled or enabled. Legal values include **TX_INT_DISABLE** and **TX_INT_ENABLE**. The actual values for these parameters are port specific. In addition, some processing architectures might support additional interrupt disable postures.

### Return Values
- **previous posture** This service returns the previous interrupt posture to the caller. This allows users of the service to restore the previous posture after interrupts are disabled.

### Allowed From

Threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
UINT my_old_posture;

/* Lockout interrupts */
my_old_posture = tx_interrupt_control(TX_INT_DISABLE);

/* Perform critical operations that need interrupts
locked-out.... */

/* Restore previous interrupt lockout posture. */
tx_interrupt_control(my_old_posture);
```

### See Also

None
