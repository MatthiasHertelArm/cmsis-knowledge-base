---
id: "frb-10-task-notifications-10-3-5-the-xtasknotify-and-xtasknotifyfr"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.5 The xTaskNotify() and xTaskNotifyFromISR() API Functions"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-5-the-xtasknotify-and-xtasknotifyfromisr-api-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

`xTaskNotify()` is a more capable version of `xTaskNotifyGive()` that can be
used to update the receiving task's notification value in any of the
following ways:

- Increment (add one to) the receiving task's notification value, in
  which case `xTaskNotify()` is equivalent to `xTaskNotifyGive()`.

- Set one or more bits in the receiving task's notification value.
  This allows a task's notification value to be used as a lighter
  weight and faster alternative to an event group.

- Write a completely new number into the receiving task's notification
  value, but only if the receiving task has read its notification
  value since it was last updated. This allows a task's notification
  value to provide similar functionality to that provided by a queue
  that has a length of one.

- Write a completely new number into the receiving task's notification
  value, even if the receiving task has not read its notification
  value since it was last updated. This allows a task's notification
  value to provide similar functionality to that provided by the
  `xQueueOverwrite()` API function. The resultant behavior is sometimes
  referred to as a 'mailbox'.

`xTaskNotify()` is more flexible and powerful than `xTaskNotifyGive()`, and
because of that extra flexibility and power, it is also a little more
complex to use.

`xTaskNotifyFromISR()` is a version of `xTaskNotify()` that can be used in
an interrupt service routine, and therefore has an additional
`pxHigherPriorityTaskWoken` parameter.

Calling `xTaskNotify()` will always set the receiving task's notification
state to pending, if it was not already pending.





```c
BaseType_t xTaskNotify( TaskHandle_t xTaskToNotify,
                        uint32_t ulValue,
                        eNotifyAction eAction );

BaseType_t xTaskNotifyFromISR( TaskHandle_t xTaskToNotify,
                               uint32_t ulValue,
                               eNotifyAction eAction,
                               BaseType_t *pxHigherPriorityTaskWoken );
```

***Listing 10.8*** *Prototypes for the xTaskNotify() and xTaskNotifyFromISR() API functions*

**xTaskNotify() parameters and return value**

- `xTaskToNotify`

  The handle of the task to which the notification is being sent—see
  the `pxCreatedTask` parameter of the `xTaskCreate()` API function for
  information on obtaining handles to tasks.

- `ulValue`

  How ulValue is used is dependent on the eNotifyAction value. See below.

- `eNotifyAction`

  An enumerated type that specifies how to update the receiving task's
  notification value. See below.

- Return value

  `xTaskNotify()` will return `pdPASS` *except* in the one case noted below.

**Valid xTaskNotify() eNotifyAction Parameter Values, and Their Resultant
Effect on the Receiving Task's Notification Value**

- `eNoAction`

  The receiving task's notification state is set to pending without
  it's notification value being updated. The `xTaskNotify()` `ulValue`
  parameter is not used.

  The `eNoAction` action allows a task notification to be used as a
  faster and lighter-weight alternative to a binary semaphore.

- `eSetBits`

  The receiving task's notification value is bitwise OR'ed with the
  value passed in the `xTaskNotify()` `ulValue` parameter. For example, if
  `ulValue` is set to 0x01, then bit 0 will be set in the receiving task's
  notification value. As another example, if `ulValue` is 0x06 (binary 0110)
  then bit 1 and bit 2 will be set in the receiving task's notification value.

  The `eSetBits` action allows a task notification to be used as a faster
  and lighter-weight alternative to an event group.

- `eIncrement`

  The receiving task's notification value is incremented. The
  `xTaskNotify()` `ulValue` parameter is not used.

  The `eIncrement` action allows a task notification to be used as a
  faster and lighter-weight alternative to a binary or counting semaphore,
  and is equivalent to the simpler `xTaskNotifyGive()` API function.

- `eSetValueWithoutOverwrite`

  If the receiving task had a notification pending before
  `xTaskNotify()` was called, then no action is taken and `xTaskNotify()` will
  return `pdFAIL`.

  If the receiving task did not have a notification pending before
  `xTaskNotify()` was called, then the receiving task's notification value
  is set to the value passed in the `xTaskNotify()` `ulValue` parameter.

- `eSetValueWithOverwrite`

  The receiving task's notification value is set to the value passed
  in the `xTaskNotify()` `ulValue` parameter, regardless of whether the
  receiving task had a notification pending before `xTaskNotify()` was
  called or not.
