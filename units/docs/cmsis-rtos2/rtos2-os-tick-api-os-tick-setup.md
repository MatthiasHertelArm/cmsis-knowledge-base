---
id: "rtos2-os-tick-api-os-tick-setup"
type: "concept"
domain: "rtos"
title: "OS Tick API: OS_Tick_Setup"
summary: "Setup OS Tick timer to generate periodic RTOS Kernel Ticks."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_os_tick.txt"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t  OS_Tick_Setup (uint32_t freq, IRQHandler_t handler)
```

 

Setup OS Tick timer to generate periodic RTOS Kernel Ticks.

The timer should be configured to generate periodic interrupts at frequency specified by **freq.**
The parameter **handler** defines the interrupt handler function that is called.

The timer should only be initialized and configured but must not be started to create interrupts.
The RTOS kernel calls the function OS_Tick_Enable to start the timer interrupts.

**Cortex-M SysTick implementation:**
```
#ifndef SYSTICK_IRQ_PRIORITY
#define SYSTICK_IRQ_PRIORITY    0xFFU
#endif

static uint8_t PendST;

int32_t  OS_Tick_Setup (uint32_t freq, IRQHandler_t handler) {
  (void)handler;
  uint32_t load;
 
  if (freq == 0U) {
    return (-1);
  }
 
  load = (SystemCoreClock / freq) - 1U;
  if (load > 0x00FFFFFFU) {
    return (-1);
  }
 
  NVIC_SetPriority(SysTick_IRQn, SYSTICK_IRQ_PRIORITY);
 
  SysTick->CTRL =  SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_TICKINT_Msk;
  SysTick->LOAD =  load;
  SysTick->VAL  =  0U;
 
  PendST = 0U;

  return (0);
}
```
