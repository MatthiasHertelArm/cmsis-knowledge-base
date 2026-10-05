---
id: "frb-11-low-power-support-11-2-freertos-sleep-modes"
type: "concept"
domain: "rtos"
title: "11 Low Power Support: 11.2 FreeRTOS Sleep Modes"
summary: "There are three types of sleep modes supported in FreeRTOS:"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch11.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch11.md#11-2-freertos-sleep-modes"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are three types of sleep modes supported in FreeRTOS: 

1. eAbortSleep - This mode denotes a task has been made ready, a context switch was pended or a tick 
   interrupt has already occurred but was pended since the scheduler was suspended. It signals the RTOS 
   to abort entering a sleep mode.

2. eStandardSleep - This mode allows to enter a sleep mode that will not last longer than the expected 
   idle time.

3. eNoTasksWaitingTimeout - This mode is entered when no tasks are waiting for a timeout so it is safe to 
   enter a sleep mode that can only be exited by an external interrupt or reset.
