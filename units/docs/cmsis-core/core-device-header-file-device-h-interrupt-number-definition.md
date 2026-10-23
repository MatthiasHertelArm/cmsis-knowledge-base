---
id: "core-device-header-file-device-h-interrupt-number-definition"
type: "concept"
domain: "core"
title: "Device Header File `<Device.h>`: Interrupt Number Definition"
summary: "device_h_pg contains the enumeration IRQn_Type that defines all exceptions and interrupts of the device. - Negative IRQn values represent processor core exceptions (internal interrupts). - Positive IRQn values represent device-specific exceptions (external interrupts)."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/core_device_h.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/core_device_h.md#interrupt-number-definition"
license: "Apache-2.0"
mode: "V"
---

device_h_pg contains the enumeration IRQn_Type that defines all exceptions and interrupts of the device.
 - Negative IRQn values represent processor core exceptions (internal interrupts).
 - Positive IRQn values represent device-specific exceptions (external interrupts). The first device-specific interrupt has the IRQn value 0.
   The IRQn values needs extension to reflect the device-specific interrupt vector table in the startup_c_pg.

**Example:**

The following example shows the extension of the interrupt vector table for the LPC1100 device family.

```c
typedef enum IRQn
{
/******  Cortex-M0 Processor Exceptions Numbers ***************************************************/
  NonMaskableInt_IRQn           = -14,      /*!< 2 Non Maskable Interrupt                         */
  HardFault_IRQn                = -13,      /*!< 3 Cortex-M0 Hard Fault Interrupt                 */
  SVCall_IRQn                   = -5,       /*!< 11 Cortex-M0 SVC Interrupt                       */
  PendSV_IRQn                   = -2,       /*!< 14 Cortex-M0 PendSV Interrupt                    */
  SysTick_IRQn                  = -1,       /*!< 15 Cortex-M0 System Tick Interrupt               */

/******  LPC11xx/LPC11Cxx Specific Interrupt Numbers **********************************************/
  WAKEUP0_IRQn                  = 0,        /*!< All I/O pins can be used as wakeup source.       */
  WAKEUP1_IRQn                  = 1,        /*!< There are 13 pins in total for LPC11xx           */
  WAKEUP2_IRQn                  = 2,
                 :       :
                 :       :
  EINT1_IRQn                    = 30,       /*!< External Interrupt 1 Interrupt                   */
  EINT0_IRQn                    = 31,       /*!< External Interrupt 0 Interrupt                   */
} IRQn_Type;
```
