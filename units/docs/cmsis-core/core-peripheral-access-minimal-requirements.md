---
id: "core-peripheral-access-minimal-requirements"
type: "concept"
domain: "core"
title: "Peripheral Access: Minimal Requirements"
summary: "To access the peripheral registers and related function in a device, the files device.h and core_cm#.h define as a minimum: \\n\\n - The Register Layout Typedef for each peripheral that defines all register names."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
license: "Apache-2.0"
mode: "V"
---

To access the peripheral registers and related function in a device, the files **_device.h_** and **core_cm_#_.h** define as a minimum:
\n\n
- The **Register Layout Typedef** for each peripheral that defines all register names.
  RESERVED is used to introduce space into the structure for adjusting the addresses of
  the peripheral registers.
\n\n
**Example:**
```
typedef struct
{
  __IOM uint32_t CTRL;                /* Offset: 0x000 (R/W)  SysTick Control and Status Register */
  __IOM uint32_t LOAD;                /* Offset: 0x004 (R/W)  SysTick Reload Value Register       */
  __IOM uint32_t VAL;                 /* Offset: 0x008 (R/W)  SysTick Current Value Register      */
  __IM  uint32_t CALIB;               /* Offset: 0x00C (R/ )  SysTick Calibration Register        */
} SysTick_Type;
```


- **Base Address** for each peripheral (in case of multiple peripherals
    that use the same **register layout typedef** multiple base addresses are defined).
    \n\n
**Example:**
```
#define SysTick_BASE (SCS_BASE + 0x0010)            /* SysTick Base Address     */
```


- **Access Definitions** for each peripheral. In case of multiple peripherals that are using the same
    **register layout typdef**, multiple access definitions exist (LPC_UART0, LPC_UART2).
    \n\n
**Example:**
```
#define SysTick ((SysTick_Type *) Systick_BASE)    /* SysTick access definition */
```


These definitions allow accessing peripheral registers with simple assignments.

- **Example:**
  \n
```
SysTick->CTRL = 0;
```
