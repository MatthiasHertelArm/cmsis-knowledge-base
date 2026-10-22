---
id: "core-interrupts-and-exceptions-nvic"
type: "concept"
domain: "core"
title: "Interrupts and Exceptions (NVIC)"
summary: "Functions to access the Nested Vector Interrupt Controller (NVIC)."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_nvic.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_nvic.txt"
license: "Apache-2.0"
mode: "V"
---

Functions to access the Nested Vector Interrupt Controller (NVIC).

This section explains how to use interrupts and exceptions and access functions for the Nested Vector Interrupt Controller (NVIC).

Arm provides a template file **startup__device_** for each supported
compiler. The file must be adapted by the silicon vendor to include interrupt vectors for all device-specific
interrupt handlers. Each interrupt handler is defined as a **_weak_** function
to an dummy handler. These interrupt handlers can be used directly in application software
without being adapted by the programmer.

The table below lists the core exception vectors of the various Cortex-M processors.



| Exception Vector | Handler Function | IRQn Value | Armv6-M | Armv7-M | Armv8-M Baseline | Armv8-M Mainline | Armv8.1-M Mainline | Description |
|---|---|---|---|---|---|---|---|---|
| **NonMaskableInt_IRQn** | NMI_Handler | -14 | √ | √ | √ | √ | √ | Non Maskable Interrupt |
| **HardFault_IRQn** | HardFault_Handler | -13 | √ | √ | √ | √ | √ | Hard Fault Interrupt |
| **MemoryManagement_IRQn** | MemManage_Handler | -12 | — | √ | — | √ | √ | Memory Management Interrupt |
| **BusFault_IRQn** | BusFault_Handler | -11 | — | √ | — | √ | √ | Bus Fault Interrupt |
| **UsageFault_IRQn** | UsageFault_Handler | -10 | — | √ | — | √ | √ | Usage Fault Interrupt |
| **SecureFault_IRQn** | SecureFault_Handler | -9 | — | — | √ | √ | √ | Secure Fault Interrupt |
| **SVCall_IRQn** | SVC_Handler | -5 | √ | √ | √ | √ | √ | SVC Interrupt |
| **DebugMonitor_IRQn** | DebugMon_Handler | -4 | — | √ | — | √ | √ | Debug Monitor Interrupt |
| **PendSV_IRQn** | PendSV_Handler | -2 | √ | √ | √ | √ | √ | Pend SV Interrupt |
| **SysTick_IRQn** | SysTick_Handler | -1 | √ | √ | √ | √ | √ | System Tick Interrupt |




Vector Table
============
The Vector Table defines the entry addresses of the processor exceptions and the
device specific interrupts.  It is typically located at the beginning of the
program memory, however using_vtor it can be relocated to RAM.  The symbol
**__Vectors** is the address of the vector table in the startup code and the
register **SCB->VTOR** holds the start address of the vector table.

\if ARMv8M
An Armv8-M implementation with TrustZone provides two vector tables:
  - vector table for Secure handlers
  - vector table for Non-Secure handlers

Refer to Model_TrustZone for more information.
\endif

Processor Exceptions
--------------------
At the beginning of the vector table, the initial stack value and the
exception vectors of the processor are defined. The vector table below
shows the exception vectors of a Armv8-M Mainline processor. Other processor
variants may have fewer vectors.

```
__Vectors       DCD     __initial_sp              ; Top of Stack initialization
                DCD     Reset_Handler             ; Reset Handler
                DCD     NMI_Handler               ; NMI Handler
                DCD     HardFault_Handler         ; Hard Fault Handler
                DCD     MemManage_Handler         ; MPU Fault Handler
                DCD     BusFault_Handler          ; Bus Fault Handler
                DCD     UsageFault_Handler        ; Usage Fault Handler
                DCD     SecureFault_Handler       ; Secure Fault Handler
                DCD     0                         ; Reserved
                DCD     0                         ; Reserved
                DCD     0                         ; Reserved
                DCD     SVC_Handler               ; SVC Handler
                DCD     DebugMon_Handler          ; Debug Monitor Handler
                DCD     0                         ; Reserved
                DCD     PendSV_Handler            ; PendSV Handler
                DCD     SysTick_Handler           ; SysTick Handler
```


Device Specific Vectors
-----------------------
Following the processor exception vectors, the vector table contains also the
device specific interrupt vectors.

```
; device specific interrupts
                DCD     WWDG_IRQHandler           ; Window Watchdog
                DCD     PVD_IRQHandler            ; PVD through EXTI Line detect
                DCD     TAMPER_IRQHandler         ; Tamper
```

All device specific interrupts should have a default interrupt handler function that can
be overwritten in user code. Below is an example for this default handler function.

```
Default_Handler PROC
                EXPORT WWDG_IRQHandler   [WEAK]
                EXPORT PVD_IRQHandler    [WEAK]
                EXPORT TAMPER_IRQHandler [WEAK]
                :
                :
                WWDG_IRQHandler
                PVD_IRQHandler
                TAMPER_IRQHandler
                :
                :
                B .
                ENDP
```


The user application may simply define an interrupt handler function by using the handler name
as shown below.

```
void WWDG_IRQHandler(void)
{
  ...
}
```

NVIC Function Usage
===================
The code below shows the usage of various CMSIS NVIC functions with an LPC1700 device.

Code Example 1
--------------
```
#include "LPC17xx.h"

uint32_t priorityGroup;                                     /* Variables to store priority group and priority*/
uint32_t priority;
uint32_t preemptPriority;
uint32_t subPriority;

int main (void)  {
  NVIC_SetPriorityGrouping(5);                              /* Set priority group to 5:
                                                               Bit[7..6] preempt priority Bits,
                                                               Bit[5..3] subpriority Bits
                                                               (valid for five priority bits)*/

  priorityGroup =  NVIC_GetPriorityGrouping();              /* Get used priority grouping*/

  priority = NVIC_EncodePriority(priorityGroup, 1, 6);      /* Encode priority with 6 for subpriority and 1 for preempt priority
                                                               Note: priority depends on the used priority grouping*/
  NVIC_SetPriority(UART0_IRQn, priority);                   /* Set new priority*/

  priority =  NVIC_GetPriority(UART0_IRQn);                 /* Retrieve priority again*/
  NVIC_DecodePriority(priority, priorityGroup, &preemptPriority, &subPriority);

  while(1);
}
```


Code Example 2
--------------
```
#include "LPC17xx.h"

uint32_t active;                                            /* Variable to store interrupt active state*/

void TIMER0_IRQHandler(void)  {                             /* Timer 0 interrupt handler */

  if (LPC_TIM0->IR & (1 << 0))  {                           /* Check if interrupt for match channel 0 occurred*/
    LPC_TIM0->IR |= (1 << 0);                               /* Acknowledge interrupt for match channel 0 occurred*/
  }
  active = NVIC_GetActive(TIMER0_IRQn);                     /* Get interrupt active state of timer 0*/
}

int main (void) {
                                                            /* Set match channel register MR0 to 1 millisecond*/
  LPC_TIM0->MR0 = (((SystemCoreClock / 1000) / 4) - 1);	    /* 1 ms?*/

  LPC_TIM0->MCR = (3 << 0);                                 /* Enable interrupt and reset for match channel MR0*/
  NVIC_EnableIRQ(TIMER0_IRQn);                              /* Enable NVIC interrupt for timer 0*/
  LPC_TIM0->TCR = (1 << 0);                                 /* Enable timer 0*/

  while(1);
}
```


NVIC API Virtualization
=======================
The CMSIS-Core has provisions for overriding NVIC APIs as required for implementing
secure systems that control access to peripherals and related interrupts.
These overrides allow an operating system to control the access privileges of
application code to critical interrupts.

The NVIC function virtualization is enabled with the following \#define symbols:
  - CMSIS_NVIC_VIRTUAL enables overriding the CMSIS-Core (Cortex-M) NVIC functions.
  - CMSIS_VECTAB_VIRTUAL enables overriding the CMSIS-Core (Cortex-M) interrupt vector table access functions.
