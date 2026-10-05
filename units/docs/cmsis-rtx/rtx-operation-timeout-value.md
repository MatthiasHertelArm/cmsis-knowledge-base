---
id: "rtx-operation-timeout-value"
type: "concept"
domain: "rtos"
title: "operation: Timeout Value"
summary: "Timeout values are an argument to several osXxx functions to allow time for resolving a request. A timeout value of 0 means that the RTOS does not wait and the function returns instantly, even when no resource is available."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#timeout-value"
license: "Apache-2.0"
mode: "V"
---

Timeout values are an argument to several `osXxx` functions to allow time for resolving a request. A timeout value of  **0** means that the RTOS does not wait and the function returns instantly, even when no resource is available. A timeout value of osWaitForever means that the RTOS waits infinitely until a resource becomes available. Or one forces the thread to resume using osThreadResume which is discouraged.

The timeout value specifies the number of timer ticks until the time delay elapses. The value is an upper bound and depends on the actual time elapsed since the last timer tick.

Examples:

- timeout value **0** : the system does not wait, even when no resource is available the RTOS function returns instantly.
- timeout value **1** : the system waits until the next timer tick occurs; depending on the previous timer tick, it may be a very short wait time.
- timeout value **2** : actual wait time is between 1 and 2 timer ticks.
- timeout value osWaitForever : system waits infinite until a resource becomes available.

(figure: Example of timeout using osDelay())
