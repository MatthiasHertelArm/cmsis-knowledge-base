---
id: "frb-10-task-notifications-10-3-3-the-vtasknotifygivefromisr-api-fu"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.3 The vTaskNotifyGiveFromISR() API Function"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-3-the-vtasknotifygivefromisr-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

`vTaskNotifyGiveFromISR()` is a version of `xTaskNotifyGive()` that can be
used in an interrupt service routine.





```c
void vTaskNotifyGiveFromISR( TaskHandle_t xTaskToNotify,
                             BaseType_t *pxHigherPriorityTaskWoken );
```

***Listing 10.2*** *The vTaskNotifyGiveFromISR() API function prototype*

**vTaskNotifyGiveFromISR() parameters and return value**

- `xTaskToNotify`

  The handle of the task to which the notification is being sent—see
  the `pxCreatedTask` parameter of the `xTaskCreate()` API function for
  information on obtaining handles to tasks.

- `pxHigherPriorityTaskWoken`

  If the task to which the notification is being sent is waiting in
  the Blocked state to receive a notification, then sending the
  notification will cause the task to leave the Blocked state.

  If calling `vTaskNotifyGiveFromISR()` causes a task to leave the
  Blocked state, and the unblocked task has a priority higher than the
  priority of the currently executing task (the task that was
  interrupted), then, internally, `vTaskNotifyGiveFromISR()` will set
  `*pxHigherPriorityTaskWoken` to `pdTRUE`.

  If `vTaskNotifyGiveFromISR()` sets this value to `pdTRUE`, then a context
  switch should be performed before the interrupt is exited. This will
  ensure that the interrupt returns directly to the highest priority Ready
  state task.

  As with all interrupt safe API functions, the
  `pxHigherPriorityTaskWoken` parameter must be set to `pdFALSE` before it is used.
