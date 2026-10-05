---
id: "intr-a-practical-guide-to-arm-cortex-m-setup-prep"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Code Examples / Setup Prep"
summary: "Most SDKs have a pre-defined vector table with default Exception Handlers. The definitions for the Handlers are usually defined as \"weak\" so they can be overridden."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#setup-prep"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Code Examples_

Most SDKs have a pre-defined vector table with default **Exception Handlers**. The definitions for the
Handlers are usually defined as "weak" so they can be overridden.

> **CAUTION**: The default **exception handler** provided in most vendor SDKs is usually defined as a `while(1){}` loop --
> even for fault handlers! This means when a fault occurs the MCU will just sit in an infinite loop. The
> device will only recover in this situation if it's manually reset or runs out of power. It's
> generally a good idea to make sure all exception handlers at least reboot the device when a fault
> occurs to give the device a chance to recover

When building the blinky app for the NRF52840 with gcc, this vector table definition can be found
at `modules/nrfx/mdk/gcc_startup_nrf52840.S`:

```c
    .section .isr_vector
    .align 2
    .globl __isr_vector
__isr_vector:
    .long   __StackTop                  /* Top of Stack */
    .long   Reset_Handler
    .long   NMI_Handler
    .long   HardFault_Handler
    .long   MemoryManagement_Handler
    .long   BusFault_Handler
    .long   UsageFault_Handler
    .long   0                           /*Reserved */
    .long   0                           /*Reserved */
    .long   0                           /*Reserved */
    .long   0                           /*Reserved */
    .long   SVC_Handler
    .long   DebugMon_Handler
    .long   0                           /*Reserved */
    .long   PendSV_Handler
    .long   SysTick_Handler

     /* External Interrupts */
    .long   POWER_CLOCK_IRQHandler
    .long   RADIO_IRQHandler
    .long   UARTE0_UART0_IRQHandler
    .long   SPIM0_SPIS0_TWIM0_TWIS0_SPI0_TWI0_IRQHandler
    .long   SPIM1_SPIS1_TWIM1_TWIS1_SPI1_TWI1_IRQHandler
    .long   NFCT_IRQHandler
    .long   GPIOTE_IRQHandler
    .long   SAADC_IRQHandler
    .long   TIMER0_IRQHandler
    .long   TIMER1_IRQHandler
    .long   TIMER2_IRQHandler
    .long   RTC0_IRQHandler
    .long   TEMP_IRQHandler
    .long   RNG_IRQHandler
    [...]
```

We can pretty easily compute the **Exception Number** by counting the offset within this table.
`__StackTop` is **0**, `Reset_Handler` is **1**, `POWER_CLOCK_IRQHandler` is **16**.

Most vendors also provide a CMSIS compatible `IRQn_Type` define which gives you the enumerated list of **External
Interrupt Numbers** (**Exception Number** - 16). We will want this when we go to configure external
interrupts that are part of the NVIC. For the NRF52840, this can be found at
`modules/nrfx/mdk/nrf52840.h` and looks something like this:

```c
typedef enum {
[...]
  POWER_CLOCK_IRQn          =   0,              /*!< 0  POWER_CLOCK                                                            */
  RADIO_IRQn                =   1,              /*!< 1  RADIO                                                                  */
  UARTE0_UART0_IRQn         =   2,              /*!< 2  UARTE0_UART0                                                           */
  SPIM0_SPIS0_TWIM0_TWIS0_SPI0_TWI0_IRQn=   3,  /*!< 3  SPIM0_SPIS0_TWIM0_TWIS0_SPI0_TWI0                                      */
  SPIM1_SPIS1_TWIM1_TWIS1_SPI1_TWI1_IRQn=   4,  /*!< 4  SPIM1_SPIS1_TWIM1_TWIS1_SPI1_TWI1                                      */
  NFCT_IRQn                 =   5,              /*!< 5  NFCT                                                                   */
  GPIOTE_IRQn               =   6,              /*!< 6  GPIOTE                                                                 */
  SAADC_IRQn                =   7,              /*!< 7  SAADC                                                                  */
  TIMER0_IRQn               =   8,              /*!< 8  TIMER0                                                                 */
  TIMER1_IRQn               =   9,              /*!< 9  TIMER1                                                                 */
  TIMER2_IRQn               =  10,              /*!< 10 TIMER2                                                                 */
  RTC0_IRQn                 =  11,              /*!< 11 RTC0                                                                   */
[...]
  } IRQn_Type;
```

As discussed [above](#nvic-ipr), the actual number of interrupt priority levels is implementation specific. You can
find the number of levels implemented in the vendors data sheet for the MCU being used or determine it dynamically with
gdb. Unimplemented bits are Read-as-Zero (RAZ) in the `NVIC_IPR` registers so if we write
0xff and read it back we can figure out the number of levels. Let's give it a try in GDB:

```
(gdb) p/x *(uint32_t*)0xE000E400
$1 = 0x0
(gdb) set *(uint32_t*)0xE000E400=0xff
(gdb) p/x *(uint32_t*)0xE000E400
$2 = 0xe0
```

Great! We see the top 3 bits "stuck" which means the NRF52840 MCU supports 8 priority levels (0-7).

{: #pendsv-example}
