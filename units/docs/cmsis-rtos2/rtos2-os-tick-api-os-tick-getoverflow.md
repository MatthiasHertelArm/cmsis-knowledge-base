---
id: "rtos2-os-tick-api-os-tick-getoverflow"
type: "concept"
domain: "rtos"
title: "OS Tick API: OS_Tick_GetOverflow"
summary: "Return the state of OS Tick timer interrupt pending bit that indicates timer overflows to adjust SysTimer calculations."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
license: "Apache-2.0"
mode: "V"
---

```c
OS_Tick_GetOverflow (void)
```

 
Get OS Tick timer overflow status.

Return the state of OS Tick timer interrupt pending bit that indicates timer overflows to adjust SysTimer calculations.

**Cortex-M SysTick implementation:**

```
uint32_t OS_Tick_GetOverflow (void) {
  return ((SCB->ICSR & SCB_ICSR_PENDSTSET_Msk) >> SCB_ICSR_PENDSTSET_Pos);
}
```
