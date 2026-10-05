---
id: "rtx-operation-rtx-kernel-timer-tick"
type: "concept"
domain: "rtos"
title: "operation: RTX Kernel Timer Tick"
summary: "RTX uses the generic CMSIS_RTOS_TickAPI to configure and control its periodic Kernel Tick."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#rtx-kernel-timer-tick"
license: "Apache-2.0"
mode: "V"
---

RTX uses the generic CMSIS_RTOS_TickAPI to configure and control its periodic Kernel Tick.

To use an alternative timer as the Kernel Tick Timer one simply needs to implement a custom version of the CMSIS_RTOS_TickAPI.

> **Note**
>
> - The OS Tick implementation provided must assure that the used timer interrupt uses the same (low) priority group as the service interrupts, i.e. interrupts used by RTX must not preempt each other. Refer to the rtx_scheduler section for more details.

### Tick-less Low-Power Operation

RTX5 provides extension for tick-less operation which is useful for applications that use extensively low-power modes where the SysTick timer is also disabled. To provide a time-tick in such power-saving modes, a wake-up timer is used to derive timer intervals. The CMSIS-RTOS2 functions osKernelSuspend and osKernelResume control the tick-less operation.

Using this functions allows the RTX5 thread scheduler to stop the periodic kernel tick interrupt. When all active threads are suspended, the system enters power-down and calculates how long it can stay in this power-down mode. In the power-down mode the processor and peripherals can be switched off. Only a wake-up timer must remain powered, because this timer is responsible to wake-up the system after the power-down period expires.

The tick-less operation is controlled from the `osRtxIdleThread` thread. The wake-up timeout value is set before the system enters the power-down mode. The function osKernelSuspend calculates the wake-up timeout measured in RTX Timer Ticks; this value is used to setup the wake-up timer that runs during the power-down mode of the system.

Once the system resumes operation (either by a wake-up time out or other interrupts) the RTX5 thread scheduler is started with the function osKernelResume. The parameter _sleep_time_ specifies the time (in RTX Timer Ticks) that the system was in power-down mode.

**Code Example:**

```c
#include "msp.h"                        // Device header

/*----------------------------------------------------------------------------
 *      MSP432 Low-Power Extension Functions
 *---------------------------------------------------------------------------*/
static void MSP432_LP_Entry(void) {
  /* Enable PCM rude mode, which allows to device to enter LPM3 without waiting for peripherals */
  PCM->CTL1 = PCM_CTL1_KEY_VAL | PCM_CTL1_FORCE_LPM_ENTRY;       
  /* Enable all SRAM bank retentions prior to going to LPM3  */
  SYSCTL->SRAM_BANKRET |= SYSCTL_SRAM_BANKRET_BNK7_RET;
  __enable_interrupt();
  NVIC_EnableIRQ(RTC_C_IRQn);
  /* Do not wake up on exit from ISR */
  SCB->SCR |= SCB_SCR_SLEEPONEXIT_Msk;
  /* Setting the sleep deep bit */
  SCB->SCR |= (SCB_SCR_SLEEPDEEP_Msk);
}
 
static volatile unsigned int tc;
static volatile unsigned int tc_wakeup;
 
void RTC_C_IRQHandler(void)
{
  if (tc++ > tc_wakeup)
  {
    SCB->SCR &= ~SCB_SCR_SLEEPONEXIT_Msk;
    NVIC_DisableIRQ(RTC_C_IRQn);
    NVIC_ClearPendingIRQ(RTC_C_IRQn);
    return;
  }
  if (RTC_C->PS0CTL & RTC_C_PS0CTL_RT0PSIFG)
  {
    RTC_C->CTL0 = RTC_C_KEY_VAL;                 // Unlock RTC key protected registers
    RTC_C->PS0CTL &= ~RTC_C_PS0CTL_RT0PSIFG;
    RTC_C->CTL0 = 0;
    SCB->SCR |= (SCB_SCR_SLEEPDEEP_Msk);
  }
}
 
uint32_t g_enable_sleep = 0;
  
void osRtxIdleThread (void) {
  
  for (;;) {
    tc_wakeup = osKernelSuspend();
    /* Is there some time to sleep? */
    if (tc_wakeup > 0) {
      tc = 0;
      /* Enter the low power state */
      MSP432_LP_Entry();
      __WFE();
    }
    /* Adjust the kernel ticks with the amount of ticks slept */
    osKernelResume (tc);
  }
}
```

> **Note**
>
> - `__WFE()` is not available in every Arm Cortex-M implementation. Check device manuals for availability.

The alternative using `__WFI()` has other issues, explained in the Arm Knowledge Based Article [Low Power RTX Applications on Cortex-M Devices](https://developer.arm.com/documentation/ka002948/latest).
