---
id: "core-using-cmsis-core-usage-examples"
type: "concept"
domain: "core"
title: "Using CMSIS-Core: Usage Examples"
summary: "Also see using_TrustZone_pg that details CMSIS-Core support for Arm TrusZone operation on Cortex-M."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/using.md#usage-examples"
license: "Apache-2.0"
mode: "V"
---

**Examples**

 - using_basic is a simple example that shows the usage of the CMSIS layer.
 - using_vtor shows how to remap the interrupt vector table.
 - using_arm explains how to use CMSIS-Core (Cortex-M) for Arm processors.
 - using_ARM_Lib_sec explains how to create libraries that support various Cortex-M cores.

Also see using_TrustZone_pg that details CMSIS-Core support for Arm TrusZone operation on Cortex-M.

### Basic CMSIS Example

A typical example for using the CMSIS layer is provided below. The example is based on a STM32F10x Device.

```c
#include <stm32f10x.h>                           // File name depends on device used
 
uint32_t volatile msTicks;                       // Counter for millisecond Interval
 
void SysTick_Handler (void) {                    // SysTick Interrupt Handler
  msTicks++;                                     // Increment Counter
}
 
void WaitForTick (void)  {
  uint32_t curTicks;
 
  curTicks = msTicks;                            // Save Current SysTick Value
  while (msTicks == curTicks)  {                 // Wait for next SysTick Interrupt
    __WFE ();                                    // Power-Down until next Event/Interrupt
  }
}
 
void TIM1_UP_IRQHandler (void) {                 // Timer Interrupt Handler
  ;                                              // Add user code here
}
 
void timer1_init(int frequency) {                // Set up Timer (device specific)
  NVIC_SetPriority (TIM1_UP_IRQn, 1);            // Set Timer priority
  NVIC_EnableIRQ (TIM1_UP_IRQn);                 // Enable Timer Interrupt
}
 
 
void Device_Initialization (void)  {             // Configure & Initialize MCU
  if (SysTick_Config (SystemCoreClock / 1000)) { // SysTick 1mSec
       : // Handle Error 
  }
  timer1_init ();                                // setup device-specific timer
}
 
 
// The processor clock is initialized by CMSIS startup + system file
void main (void) {                               // user application starts here
  Device_Initialization ();                      // Configure & Initialize MCU
  while (1)  {                                   // Endless Loop (the Super-Loop)
    __disable_irq ();                            // Disable all interrupts
    Get_InputValues ();                          // Read Values
    __enable_irq ();                             // Enable all interrupts 
    Calculation_Response ();                     // Calculate Results
    Output_Response ();                          // Output Results
    WaitForTick ();                              // Synchronize to SysTick Timer
  }
}
```

### Using Interrupt Vector Remap

Most Cortex-M processors provide VTOR register for remapping interrupt vectors. The following example shows a typical use case where the interrupt vectors are copied to RAM and the `SysTick_Handler` is replaced.

```c
#include "ARMCM3.h"                     // Device header
 
#define VECTORTABLE_SIZE        (240)    /* size of the used vector tables    */
                                         /* see startup file startup_ARMCM3.c */
#define VECTORTABLE_ALIGNMENT   (0x100U) /* 16 Cortex + 32 ARMCM3 = 48 words  */
                                         /* next power of 2 = 256             */

/* externals from startup_ARMCM3.c */
extern uint32_t __VECTOR_TABLE[VECTORTABLE_SIZE];        /* vector table ROM  */

/* new vector table in RAM, same size as vector table in ROM */
uint32_t vectorTable_RAM[VECTORTABLE_SIZE] __attribute__(( aligned (VECTORTABLE_ALIGNMENT) ));

 
/*----------------------------------------------------------------------------
  SysTick_Handler
 *----------------------------------------------------------------------------*/
volatile uint32_t msTicks = 0;                        /* counts 1ms timeTicks */
void SysTick_Handler(void) {
  msTicks++;                                             /* increment counter */
}
 
/*----------------------------------------------------------------------------
  SysTick_Handler (RAM)
 *----------------------------------------------------------------------------*/
volatile uint32_t msTicks_RAM = 0;                    /* counts 1ms timeTicks */
void SysTick_Handler_RAM(void) {
  msTicks_RAM++;                                      /* increment counter */
}
 
/*----------------------------------------------------------------------------
  MAIN function
 *----------------------------------------------------------------------------*/
int main (void) {
  uint32_t i;
   
  for (i = 0; i < VECTORTABLE_SIZE; i++) {
    vectorTable_RAM[i] = __VECTOR_TABLE[i];       /* copy vector table to RAM */
  }
                                                   /* replace SysTick Handler */
  vectorTable_RAM[SysTick_IRQn + 16] = (uint32_t)SysTick_Handler_RAM;
  
  /* relocate vector table */ 
  __disable_irq();
    SCB->VTOR = (uint32_t)&vectorTable_RAM;
  __DSB();
  __enable_irq();
 
  SystemCoreClockUpdate();                        /* Get Core Clock Frequency */
  SysTick_Config(SystemCoreClock / 1000ul); /* Setup SysTick Timer for 1 msec */
   
  while(1);
}
```

### Use generic Arm Devices

Test and example projects of many software components have a need for implementations that are independent from specific device vendors but still have adaptations for various Arm Cortex-M cores to benefit from their architectural differenceis.

The [Cortex_DFP pack](https://github.com/ARM-software/Cortex_DFP) provides generic device definitions for standard Arm Cortex-M cores and contains corresponding cmsis_device_files. These generic Arm devices can be used as a target for embedded programs, with execution, for example, on processor simulation models.

Validation suits and example projects for such components as [CMSIS-DSP](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/../DSP/index.html), [CMSIS-RTOS](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/../RTOS2/index.html) and [CMSIS-Core](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/index.html) itself use that approach already.

### Create generic libraries

The CMSIS Processor and Core Peripheral files allow also to create generic libraries. 
The [CMSIS-DSP libraries](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/../DSP/index.html) are an example for such a generic library.

To build a generic Library set the define `__CMSIS_GENERIC` and include the relevant `core_<cpu>.h` CMSIS CPU & Core Access header file for the processor.

The define `__CMSIS_GENERIC` disables device-dependent features such as the **SysTick** timer and the **Interrupt System**.

Refer to core_config_sect for a list of the available `core_<cpu>.h` header files.

**Example:**

The following code section shows the usage of the `core_<cpu>.h` header files to build a generic library for Cortex-M0, Cortex-M3, Cortex-M4, or Cortex-M7 devices.

To select the processor, the source code uses the defines `CORTEX_M7`, `CORTEX_M4`, `CORTEX_M3`, `CORTEX_M0`, or `CORTEX_M0PLUS`. One of these defines needs to be provided on the compiler command line. By using this header file, the source code can access the correct implementations for Core_Register_gr, intrinsic_CPU_gr, intrinsic_SIMD_gr, and ITM_Debug_gr.

```c
#define __CMSIS_GENERIC              /* disable NVIC and Systick functions */

#if defined (CORTEX_M7)
  #include "core_cm7.h"
#elif defined (CORTEX_M4)
  #include "core_cm4.h"
#elif defined (CORTEX_M3)
  #include "core_cm3.h"
#elif defined (CORTEX_M0)
  #include "core_cm0.h"
#elif defined (CORTEX_M0PLUS)
  #include "core_cm0plus.h"
#else
  #error "Processor not specified or unsupported."
#endif
```
