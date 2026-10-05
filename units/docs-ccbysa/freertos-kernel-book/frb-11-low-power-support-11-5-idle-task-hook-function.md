---
id: "frb-11-low-power-support-11-5-idle-task-hook-function"
type: "concept"
domain: "rtos"
title: "11 Low Power Support: 11.5 Idle Task Hook Function"
summary: "The Idle task can optionally call an application defined hook (or callback) function - the idle hook."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch11.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch11.md#11-5-idle-task-hook-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Idle task can optionally call an application defined hook (or callback) function - the idle hook. 
The idle task runs at the lowest priority, so such an idle hook function will only get executed when 
there are no tasks of higher priority that are able to run. This makes the Idle hook function an ideal 
place to put the processor into a low power state - providing an automatic power saving whenever there 
is no processing to be performed. The Idle hook will only get called if `configUSE_IDLE_HOOK` is set 
to 1 within FreeRTOSConfig.h.



```c
void vApplicationIdleHook( void );
```
***Listing 11.7*** *The vApplicationIdleHook API function prototype*


The idle hook is called repeatedly as long as the idle task is running. It is paramount that the idle 
hook function does not call any API functions that could cause it to block. Also, if the application 
makes use of the `vTaskDelete()` API function then the idle task hook must be allowed to periodically 
return, since the idle task is responsible for cleaning up the resources that were allocated by the RTOS 
kernel to the task that has been deleted.
