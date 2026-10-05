---
id: "frb-6-software-timer-management-6-2-software-timer-callback-functions"
type: "concept"
domain: "rtos"
title: "6 Software Timer Management: 6.2 Software Timer Callback Functions"
summary: "Software timer callback functions are implemented as C functions. The only thing special about them is their prototype, which must return void, and take a handle to a software timer as its only parameter."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch06.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch06.md#6-2-software-timer-callback-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

Software timer callback functions are implemented as C functions. The
only thing special about them is their prototype, which must return
void, and take a handle to a software timer as its only parameter. The
callback function prototype is demonstrated by Listing 6.1.




```c
void ATimerCallback( TimerHandle_t xTimer );
```
***Listing 6.1*** *The software timer callback function prototype*

Software timer callback functions execute from start to finish, and exit
in the normal way. They should be kept short, and must not enter the
Blocked state.

> *Note: As will be seen, software timer callback functions execute in the
> context of a task that is created automatically when the FreeRTOS
> scheduler is started. Therefore, it is essential that software timer
> callback functions never call FreeRTOS API functions that will result in
> the calling task entering the Blocked state. It is ok to call functions
> such as `xQueueReceive()`, but only if the function's `xTicksToWait`
> parameter (which specifies the function's block time) is set to 0. It is
> not ok to call functions such as `vTaskDelay()`, as calling `vTaskDelay()`
> will always place the calling task into the Blocked state.*
