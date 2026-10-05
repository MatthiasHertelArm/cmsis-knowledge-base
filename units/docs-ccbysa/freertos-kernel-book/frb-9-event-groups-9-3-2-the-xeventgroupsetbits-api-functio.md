---
id: "frb-9-event-groups-9-3-2-the-xeventgroupsetbits-api-functio"
type: "concept"
domain: "rtos"
title: "9 Event Groups: 9.3 Event Management Using Event Groups / 9.3.2 The xEventGroupSetBits() API Function"
summary: "Part of: 9.3 Event Management Using Event Groups"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch09.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch09.md#9-3-2-the-xeventgroupsetbits-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 9.3 Event Management Using Event Groups_

The `xEventGroupSetBits()` API function sets one or more bits in an event
group, and is typically used to notify a task that the events
represented by the bit, or bits, being set has occurred.

> *Note: Never call `xEventGroupSetBits()` from an interrupt service
> routine. The interrupt-safe version `xEventGroupSetBitsFromISR()` should
> be used in its place.*




```c
EventBits_t xEventGroupSetBits( EventGroupHandle_t xEventGroup,

const EventBits_t uxBitsToSet );
```
***Listing 9.2*** *The xEventGroupSetBits() API function prototype*


**xEventGroupSetBits() parameters and return value**

- `xEventGroup`

  The handle of the event group in which bits are being set. The event
  group handle will have been returned from the call to
  `xEventGroupCreate()` used to create the event group.

- `uxBitsToSet`

  A bit mask that specifies the event bit, or event bits, to set to
  1 in the event group. The value of the event group is updated by bitwise
  ORing the event group's existing value with the value passed in
  `uxBitsToSet`.

  As an example, setting `uxBitsToSet` to 0x04 (binary 0100) will result
  in event bit 3 in the event group becoming set (if it was not already
  set), while leaving all the other event bits in the event group
  unchanged.

- Return Value

  The value of the event group at the time the call to
  `xEventGroupSetBits()` returned. Note that the value returned will not
  necessarily have the bits specified by `uxBitsToSet` set, because the bits
  may have been cleared again by a different task.
