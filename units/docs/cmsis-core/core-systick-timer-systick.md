---
id: "core-systick-timer-systick"
type: "concept"
domain: "core"
title: "Systick Timer (SYSTICK)"
summary: "The System Tick Time (SysTick) generates interrupt requests on a regular basis. This allows an OS to carry out context switching to support multiple tasking."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_systick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_systick.txt"
license: "Apache-2.0"
mode: "V"
---

Initialize and start the SysTick timer.

    The System Tick Time (SysTick) generates interrupt requests on a regular basis.
    This allows an OS to carry out context switching to support multiple tasking. For applications
    that do not require an OS, the SysTick can be used for time keeping, time measurement, or as an 
    interrupt source for tasks that need to be executed regularly.
