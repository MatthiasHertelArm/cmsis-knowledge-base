---
id: "rtos2-os-tick-api-os-tick-getclock"
type: "concept"
domain: "rtos"
title: "OS Tick API: OS_Tick_GetClock"
summary: "Return the input clock frequency of the OS Tick timer. This is the increment rate of the counter value returned by the function OS_Tick_GetCount. This function is used to by the function osKernelGetSysTimerFreq."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t OS_Tick_GetClock (void)
```

 
Get OS Tick timer clock frequency.

Return the input clock frequency of the OS Tick timer. This is the increment rate of the counter value returned by the function OS_Tick_GetCount.
This function is used to by the function osKernelGetSysTimerFreq.

**Cortex-M SysTick implementation:**

```
uint32_t OS_Tick_GetClock (void) {
  return (SystemCoreClock);
}
```
