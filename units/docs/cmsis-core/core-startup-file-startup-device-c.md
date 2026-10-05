---
id: "core-startup-file-startup-device-c"
type: "concept"
domain: "core"
title: "Startup File startup_`<Device>`.c"
summary: "The startup file defines device exceptions and interrupts, and provides their initial (weak) handler functions. The file has a naming convention startup<Device>.c where <Device> corresponds to the device name."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/core_startup_c.md"
license: "Apache-2.0"
mode: "V"
---

The startup file defines device exceptions and interrupts, and provides their initial (weak) handler functions. The file has a naming convention `startup_<Device>.c` where `<Device>` corresponds to the device name.

Specifically, following functionalities are provided in the startup file:

 - The reset handler `Reset_Handler` which is executed upon CPU reset and typically calls the `SystemInit()` function. After the system init the control is transferred to the C/C++ run-time library which performs initialization and calls the `main` function in the user code.
 - The setup values for the Main Stack Pointer (MSP).
 - Exception vectors of the Cortex-M Processor with weak functions that implement default routines.
 - Interrupt vectors that are device specific with weak functions that implement default routines.

To adapt the file to a specific device only the interrupt vector table needs to be extended with the device-specific
interrupt handlers. The following table shows the mapping of the interrupt names vs. handler names:

| Interrupt name        | Handler name        |
| --------------------- | ------------------- |
| NonMaskableInt_IRQn   | NMI_Handler         |
| HardFault_IRQn        | HardFault_Handler   |
| MemoryManagement_IRQn | MemManage_Handler   |
| BusFault_IRQn         | BusFault_Handler    |
| UsageFault_IRQn       | UsageFault_Handler  |
| SecureFault_IRQn      | SecureFault_Handler |
| SVCall_IRQn           | SVC_Handler         |
| DebugMonitor_IRQn     | DebugMon_Handler    |
| PendSV_IRQn           | PendSV_Handler      |
| SysTick_IRQn          | SysTick_Handler     |

Additional application-specific adaptations may be required in the startup code and therefore so the startup file shall be located in the application project. cmsis_files_dfps explains how this can be achieved when device support is provided in [CMSIS pack format](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html).

**Example:**

The following example shows the extension of the interrupt vector table for the LPC1100 device family.

```c
/*----------------------------------------------------------------------------
  Exception / Interrupt Handler
 *----------------------------------------------------------------------------*/
/* Exceptions */
void WAKEUP0_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
void WAKEUP1_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
void WAKEUP2_IRQHandler     (void) __attribute__ ((weak, alias("Default_Handler")));
// :
// :
void EINT1_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
void EINT2_IRQHandler       (void) __attribute__ ((weak, alias("Default_Handler")));
// :
// :

/*----------------------------------------------------------------------------
  Exception / Interrupt Vector table
 *----------------------------------------------------------------------------*/
extern const pFunc __VECTOR_TABLE[240];
       const pFunc __VECTOR_TABLE[240] __VECTOR_TABLE_ATTRIBUTE = {
  (pFunc)(&__INITIAL_SP),                   /*     Initial Stack Pointer */
  Reset_Handler,                            /*     Reset Handler */
  NMI_Handler,                              /* -14 NMI Handler */
  HardFault_Handler,                        /* -13 Hard Fault Handler */
  MemManage_Handler,                        /* -12 MPU Fault Handler */
  BusFault_Handler,                         /* -11 Bus Fault Handler */
  UsageFault_Handler,                       /* -10 Usage Fault Handler */
  0,                                        /*     Reserved */
  0,                                        /*     Reserved */
  0,                                        /*     Reserved */
  0,                                        /*     Reserved */
  SVC_Handler,                              /*  -5 SVC Handler */
  DebugMon_Handler,                         /*  -4 Debug Monitor Handler */
  0,                                        /*     Reserved */
  PendSV_Handler,                           /*  -2 PendSV Handler */
  SysTick_Handler,                          /*  -1 SysTick Handler */

  /* Interrupts */
  WAKEUP0_IRQHandler,                       /*   0 Wakeup PIO0.0 */
  WAKEUP1_IRQHandler,                       /*   1 Wakeup PIO0.1 */
  WAKEUP2_IRQHandler,                       /*   2 Wakeup PIO0.2 */
  // :
  // :
  EINT1_IRQHandler,                         /*  30 PIO INT1 */
  EINT2_IRQHandler,                         /*  31 PIO INT2 */
  // :
  // :
};
```
