---
id: "frb-10-task-notifications-10-3-1-task-notification-api-options"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.1 Task Notification API Options"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-1-task-notification-api-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

Task notifications are a very powerful feature that can often be used in
place of a binary semaphore, a counting semaphore, an event group, and
sometimes even a queue. This wide range of usage scenarios can be
achieved by using the `xTaskNotify()` API function to send a task
notification, and the `xTaskNotifyWait()` API function to receive a task
notification.

However, in the majority of cases, the full flexibility provided by the
`xTaskNotify()` and `xTaskNotifyWait()` API functions is not required, and
simpler functions would suffice. Therefore, the `xTaskNotifyGive()` API
function is provided as a simpler but less flexible alternative to
`xTaskNotify()`, and the `ulTaskNotifyTake()` API function is provided as a
simpler but less flexible alternative to `xTaskNotifyWait()`.

The task notification system is not limited to a single notification event.  The
configuration parameter `configTASK_NOTIFICATION_ARRAY_ENTRIES` is set to 1 by default.
If it is set to a value greater than 1, an array of notifications are created inside
each task.  This allows notifications to be managed by index.  Every task
notification api function has an indexed version.  Using the non-indexed version
will result in accessing notification[0] (the first one in the array).  The `indexed`
version of each API function is identified by the suffix `Indexed` so the function
`xTaskNotify` becomes `xTaskNotifyIndexed`.  For simplicity only the non-indexed
versions of each function will be used throughout this book.

The task notification API's are implemented as macro that make calls to the
underlying `Generic` versions of each API function type.  For simplicy the API
macros will be called functions throughout this book.

#### 10.3.1.1 The complete list of API functions 27

- `xTaskNotifyGive`
- `xTaskNotifyGiveIndexed`
- `vTaskNotifyGiveFromISR`
- `vTaskNotifyGiveIndexedFromISR`
- `vTaskNotifyTake`
- `vTaskNotifyTakeIndexed`
- `xTaskNotify`
- `xTaskNotifyIndexed`
- `xTaskNotifyWait`
- `xTaskNotifyWaitIndexed`
- `xTaskNotifyStateClear`
- `xTaskNotifyStateClearIndexed`
- `ulTaskNotifyValueClear`
- `ulTaskNotifyValueClearIndexed`
- `xTaskNotifyAndQueryIndexedFromISR`
- `xTaskNotifyAndQueryFromISR`
- `xTaskNotifyFromISR`
- `xTaskNotifyIndexedFromISR`
- `xTaskNotifyAndQuery`
- `xTaskNotifyAndQueryIndexed`

*(27): These functions are actually implemented as macros.*

>Note: The `FromISR` functions do not exist for receiving notifications because a notification is always sent to a task and interrupts are not associated with any task.
