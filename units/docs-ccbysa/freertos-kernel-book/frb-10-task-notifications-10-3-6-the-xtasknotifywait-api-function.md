---
id: "frb-10-task-notifications-10-3-6-the-xtasknotifywait-api-function"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.6 The xTaskNotifyWait() API Function"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-6-the-xtasknotifywait-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

`xTaskNotifyWait()` is a more capable version of `ulTaskNotifyTake()`. It
allows a task to wait, with an optional timeout, for the calling task's
notification state to become pending, should it not already be pending.
`xTaskNotifyWait()` provides options for bits to be cleared in the calling
task's notification value both on entry to the function, and on exit
from the function.





```c
BaseType_t xTaskNotifyWait( uint32_t   ulBitsToClearOnEntry,
                            uint32_t   ulBitsToClearOnExit,
                            uint32_t   *pulNotificationValue,
                            TickType_t xTicksToWait );
```

***Listing 10.9*** *The xTaskNotifyWait() API function prototype*

**xTaskNotifyWait() parameters and return value**

- `ulBitsToClearOnEntry`

  If the calling task did not have a notification pending before it
  called `xTaskNotifyWait()`, then any bits set in `ulBitsToClearOnEntry` will
  be cleared in the task's notification value on entry to the function.

  For example, if `ulBitsToClearOnEntry` is 0x01, then bit 0 of the
  task's notification value will be cleared. As another example, setting
  `ulBitsToClearOnEntry` to 0xffffffff (`ULONG_MAX`) will clear all the bits
  in the task's notification value, effectively clearing the value to 0.

- `ulBitsToClearOnExit`

  If the calling task exits `xTaskNotifyWait()` because it received a
  notification, or because it already had a notification pending when
  `xTaskNotifyWait()` was called, then any bits set in `ulBitsToClearOnExit`
  will be cleared in the task's notification value before the task exits
  the `xTaskNotifyWait()` function.

  The bits are cleared after the task's notification value has been
  saved in `*pulNotificationValue` (see the description of
  `pulNotificationValue` below).

  For example, if `ulBitsToClearOnExit` is 0x03, then bit 0 and bit 1 of
  the task's notification value will be cleared before the function
  exits.

  Setting `ulBitsToClearOnExit` to 0xffffffff (`ULONG_MAX`) will clear all
  the bits in the task's notification value, effectively clearing the
  value to 0.

- `pulNotificationValue`

  Used to pass out the task's notification value. The value copied
  to `*pulNotificationValue` is the task's notification value as it was
  before any bits were cleared due to the `ulBitsToClearOnExit` setting.

  `pulNotificationValue` is an optional parameter and can be set to NULL
  if it is not required.

- `xTicksToWait`

  The maximum amount of time the calling task should remain in the
  Blocked state to wait for its notification state to become pending.

  The block time is specified in tick periods, so the absolute time it
  represents is dependent on the tick frequency. The macro `pdMS_TO_TICKS()`
  can be used to convert a time specified in milliseconds to a time
  specified in ticks.

  Setting `xTicksToWait` to `portMAX_DELAY` will cause the task to wait
  indefinitely (without timing out), provided `INCLUDE_vTaskSuspend` is set
  to 1 in `FreeRTOSConfig.h`.

- Return value

  There are two possible return values:

  - `pdTRUE`

    This indicates `xTaskNotifyWait()` returned because a notification was
    received, or because the calling task already had a notification pending
    when `xTaskNotifyWait()` was called.

    If a block time was specified (`xTicksToWait` was not zero), then it is
    possible that the calling task was placed into the Blocked state, to
    wait for its notification state to become pending, but its notification
    state was set to pending before the block time expired.

  - `pdFALSE`

    This indicates that `xTaskNotifyWait()` returned without the calling
    task receiving a task notification.

    If `xTicksToWait` was not zero, then the calling task will have been
    held in the Blocked state to wait for its notification state to become
    pending, but the specified block time expired before that happened.
