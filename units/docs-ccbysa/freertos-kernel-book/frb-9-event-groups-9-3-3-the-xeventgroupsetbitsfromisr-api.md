---
id: "frb-9-event-groups-9-3-3-the-xeventgroupsetbitsfromisr-api"
type: "concept"
domain: "rtos"
title: "9 Event Groups: 9.3 Event Management Using Event Groups / 9.3.3 The xEventGroupSetBitsFromISR() API Function"
summary: "Part of: 9.3 Event Management Using Event Groups"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch09.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch09.md#9-3-3-the-xeventgroupsetbitsfromisr-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 9.3 Event Management Using Event Groups_

`xEventGroupSetBitsFromISR()` is the interrupt safe version of
`xEventGroupSetBits()`.

Giving a semaphore is a deterministic operation because it is known in
advance that giving a semaphore can result in at most one task leaving
the Blocked state. When bits are set in an event group it is not known
in advance how many tasks will leave the Blocked state, so setting bits
in an event group is not a deterministic operation.

The FreeRTOS design and implementation standard does not permit
non-deterministic operations to be performed inside an interrupt service
routine, or when interrupts are disabled. For that reason,
`xEventGroupSetBitsFromISR()` does not set event bits directly inside the
interrupt service routine, but instead defers the action to the RTOS
daemon task.




```c
BaseType_t xEventGroupSetBitsFromISR( EventGroupHandle_t xEventGroup,
                                      const EventBits_t uxBitsToSet,
                                      BaseType_t *pxHigherPriorityTaskWoken );
```
***Listing 9.3*** *The xEventGroupSetBitsFromISR() API function prototype*


**xEventGroupSetBitsFromISR() parameters and return value**

- `xEventGroup`

  The handle of the event group in which bits are being set. The event
  group handle will have been returned from the call to
  `xEventGroupCreate()` used to create the event group.

- `uxBitsToSet`

  A bit mask that specifies the event bit, or event bits, to set to
  1 in the event group. The value of the event group is updated by bitwise
  ORing the event group's existing value with the value passed in
  `uxBitsToSet`.

  As an example, setting `uxBitsToSet` to 0x05 (binary 0101) will result
  in event bit 2 and event bit 0 in the event group becoming set (if they
  were not already set), while leaving all the other event bits in the
  event group unchanged.

- `pxHigherPriorityTaskWoken`

  `xEventGroupSetBitsFromISR()` does not set the event bits directly
  inside the interrupt service routine, but instead defers the action to
  the RTOS daemon task by sending a command on the timer command queue. If
  the daemon task was in the Blocked state to wait for data to become
  available on the timer command queue, then writing to the timer command
  queue will cause the daemon task to leave the Blocked state. If the
  priority of the daemon task is higher than the priority of the currently
  executing task (the task that was interrupted), then, internally,
  `xEventGroupSetBitsFromISR()` will set `*pxHigherPriorityTaskWoken` to
  `pdTRUE`.

  If `xEventGroupSetBitsFromISR()` sets this value to `pdTRUE`, then a
  context switch should be performed before the interrupt is exited. This
  will ensure that the interrupt returns directly to the daemon task, as
  the daemon task will be the highest priority Ready state task.

- Return Value

  There are two possible return values:

  - `pdPASS` will be returned only if data was successfully sent to the
    timer command queue.

  - `pdFALSE` will be returned if the 'set bits' command could not be
    written to the timer command queue because the queue was already
    full.
