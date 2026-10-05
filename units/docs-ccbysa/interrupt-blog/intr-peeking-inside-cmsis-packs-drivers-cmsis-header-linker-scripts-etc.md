---
id: "intr-peeking-inside-cmsis-packs-drivers-cmsis-header-linker-scripts-etc"
type: "concept"
domain: "debug"
title: "Peeking inside CMSIS-Packs: Drivers, CMSIS Header, Linker Scripts, etc."
summary: "Often a CMSIS Pack will contain a C header file with register definitions; in our example pack above, it's samd21b/include/samd21e15bu.h, and it has the well-known CMSIS style, defining interrupt vectors and peripheral registers:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-07-cmsis-packs.md"
doc_source: "https://interrupt.memfault.com/blog/cmsis-packs#drivers-cmsis-header-linker-scripts-etc"
license: "CC-BY-SA-4.0"
mode: "V"
---

### CMSIS Header

Often a CMSIS Pack will contain a C header file with register definitions; in
our example pack above, it's `samd21b/include/samd21e15bu.h`, and it has the
well-known CMSIS style, defining interrupt vectors and peripheral registers:

_Excerpt with interrupt vector enum:_

```c
/* Interrupt Number Definition */
typedef enum IRQn
{
/******  CORTEX-M0PLUS Processor Exceptions Numbers ******************************/
  Reset_IRQn                = -15, /* -15 Reset Vector, invoked on Power up and warm reset */
  NonMaskableInt_IRQn       = -14, /* -14 Non maskable Interrupt, cannot be stopped or preempted */
  HardFault_IRQn            = -13, /* -13 Hard Fault, all classes of Fault    */
  SVCall_IRQn               =  -5, /* -5  System Service Call via SVC instruction */
  PendSV_IRQn               =  -2, /* -2  Pendable request for system service */
  SysTick_IRQn              =  -1, /* -1  System Tick Timer                   */

/******  SAMD21E15BU specific Interrupt Numbers ***********************************/
  PM_IRQn                   =   0, /* 0   Power Manager (PM)                  */
  SYSCTRL_IRQn              =   1, /* 1   System Control (SYSCTRL)            */
  WDT_IRQn                  =   2, /* 2   Watchdog Timer (WDT)                */
...
```

_Excerpt with peripheral registers structure access (the structures are defined
in a common file in this Pack):_

```c
#define ADC_REGS                         ((adc_registers_t*)0x42004000)                /* ADC Registers Address        */
#define DAC_REGS                         ((dac_registers_t*)0x42004800)                /* DAC Registers Address        */
```

### Peripheral Drivers

Packs may also contain device drivers (CMSIS-style or other); for example, the
Pack for the STM32F407 family contains both:

- STM32CubeF4 HAL drivers
- CMSIS-style generated drivers

Often these drivers will be less applicable in production than what's available
from the vendor directly; Packs may not be updated as regularly, or contain
simplified driver code.

### Linker Scripts and Startup Code

Look for files with `startup` in the name, typically `.c` or `.s` files. These
are usually pretty generic (initialize `.data` and `.bss`, call some clock init
function), but are a useful reference.

Example linker files are often provided, usually hit or miss whether GNU `ld`
format or IAR (`*.icf`) etc., varies from vendor to vendor. These can be a
useful reference, eg if there are special one-time-programmable regions in flash
that can result in bricked chips, or if there's a certain way RAM is banked on
the chip that isn't obvious from the datasheet, etc., but always check directly
with the vendor as well.
