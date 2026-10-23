---
id: "rtos2-os-tick-api-os-tick-getcount"
type: "concept"
domain: "rtos"
title: "OS Tick API: OS_Tick_GetCount"
summary: "Return the current value of the OS Tick counter: 0 ... (reload value -1). The reload value is returned by the function OS_Tick_GetInterval. The OS Tick timer counter value is used to by the function osKernelGetSysTimerCount."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t OS_Tick_GetCount (void)
```

 

Get OS Tick timer counter value.

Return the current value of the OS Tick counter: 0 ... (reload value -1). The reload value is returned by the function OS_Tick_GetInterval.
The OS Tick timer counter value is used to by the function osKernelGetSysTimerCount.

**Cortex-M SysTick implementation:**

```
uint32_t OS_Tick_GetCount (void) {
  uint32_t val;
  uint32_t count;
 
  val = SysTick->VAL;
  if (val != 0U) {
    count = (SysTick->LOAD - val) + 1U;
  } else {
    count = 0U;
  }
 
  return (count);
}
```
