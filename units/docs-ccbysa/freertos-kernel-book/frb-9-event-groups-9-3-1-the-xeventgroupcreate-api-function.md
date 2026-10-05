---
id: "frb-9-event-groups-9-3-1-the-xeventgroupcreate-api-function"
type: "concept"
domain: "rtos"
title: "9 Event Groups: 9.3 Event Management Using Event Groups / 9.3.1 The xEventGroupCreate() API Function"
summary: "Part of: 9.3 Event Management Using Event Groups"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch09.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch09.md#9-3-1-the-xeventgroupcreate-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 9.3 Event Management Using Event Groups_

FreeRTOS also includes the `xEventGroupCreateStatic()` function,
which allocates the memory required to create an event group statically
at compile time: An event group must be explicitly created before it can
be used.

Event groups are referenced using variables of type `EventGroupHandle_t`.
The `xEventGroupCreate()` API function is used to create an event group,
and returns an `EventGroupHandle_t` to reference the event group it
creates.




```c
EventGroupHandle_t xEventGroupCreate( void );
```
***Listing 9.1*** *The xEventGroupCreate() API function prototype*


**xEventGroupCreate() return value**

- Return Value

  If NULL is returned, then the event group cannot be created
  because there is insufficient heap memory available for FreeRTOS to
  allocate the event group data structures. Chapter 3 provides more
  information on heap memory management.

  A non-NULL value being returned indicates that the event group has
  been created successfully. The returned value should be stored as the
  handle to the created event group.
