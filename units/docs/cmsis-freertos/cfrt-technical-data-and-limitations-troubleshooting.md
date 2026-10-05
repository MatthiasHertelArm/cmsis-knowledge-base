---
id: "cfrt-technical-data-and-limitations-troubleshooting"
type: "concept"
domain: "rtos"
title: "Technical Data and Limitations: Troubleshooting"
summary: "Users looking for help shall check subsection of the full FreeRTOS FAQ. It contains many useful information that also apply when using FreeRTOS in context of CMSIS-FreeRTOS."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/technical_data.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/technical_data.md#troubleshooting"
license: "Apache-2.0"
mode: "V"
---

Users looking for help shall check [subsection of the full FreeRTOS FAQ](https://www.freertos.org/Why-FreeRTOS/FAQs). It contains many useful information that also apply when using FreeRTOS in context of CMSIS-FreeRTOS.

Additionally, please take a look at the following:

1. **Interrupts are disabled when main is called or before the kernel is started**

    Before the FreeRTOS kernel is started, threads (i.e. tasks) may be created together with other objects like mutexes, semaphores, message queues etc. When functions like `xTaskCreate`, `xSemaphoreCreateMutex`, `xQueueCreate` and others get called, they prevent interrupt handlers from calling FreeRTOS API functions in order to keep FreeRTOS kernel variables and state machine consistent (see also here [Interrupts are not executing](https://www.freertos.org/Why-FreeRTOS/FAQs)). In cases when interrupts may be executed after object creation and before the FreeRTOS kernel is started they can be re-enabled:
    ```c
        portENABLE_INTERRUPTS();
    ```
    Make sure that the interrupts you execute in such case do not call FreeRTOS API.
