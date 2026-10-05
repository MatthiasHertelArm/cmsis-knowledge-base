---
id: "frb-10-task-notifications-10-3-2-the-xtasknotifygive-api-functions"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.2 The xTaskNotifyGive() API Functions"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-2-the-xtasknotifygive-api-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

`xTaskNotifyGive()` sends a notification directly to a task, and
increments (adds one to) the receiving task's notification value.
Calling `xTaskNotifyGive()` will set the receiving task's notification
state to pending, if it was not already pending.

The `xTaskNotifyGive()` API function is provided to allow a task
notification to be used as a lighter weight and faster alternative to a
binary or counting semaphore.





```c
BaseType_t xTaskNotifyGive( TaskHandle_t xTaskToNotify );
BaseType_t xTaskNotifyGiveIndexed( TaskHandle_t xTaskToNotify, UBaseType_t uxIndexToNotify );
```

***Listing 10.1*** *The xTaskNotifyGive() API function prototype*

**xTaskNotifyGive()/xTaskNotifyGiveIndexed() parameters and return value**

- `xTaskToNotify`

  The handle of the task to which the notification is being sent—see
  the `pxCreatedTask` parameter of the `xTaskCreate()` API function for
  information on obtaining handles to tasks.

- `uxIndexToNotify`

  The index into the array

- Return value

  `xTaskNotifyGive()` is a macro that calls `xTaskNotify()`. The
  parameters passed into `xTaskNotify()` by the macro are set such that
  `pdPASS` is the only possible return value. `xTaskNotify()` is described
  later in this book.
