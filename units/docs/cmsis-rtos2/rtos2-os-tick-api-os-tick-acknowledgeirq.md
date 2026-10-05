---
id: "rtos2-os-tick-api-os-tick-acknowledgeirq"
type: "concept"
domain: "rtos"
title: "OS Tick API: OS_Tick_AcknowledgeIRQ"
summary: "Acknowledge execution of OS Tick timer interrupt."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void  OS_Tick_AcknowledgeIRQ (void)
```

 
Acknowledge execution of OS Tick timer interrupt.

Acknowledge the execution of the OS Tick timer interrupt function, for example clear the pending flag.

**Cortex-M SysTick implementation:**

```
void  OS_Tick_AcknowledgeIRQ (void) {

  (void)SysTick->CTRL;

}
```
