---
id: "zep-interrupts-defining-a-direct-isr"
type: "concept"
domain: "rtos"
title: "Interrupts: Implementation / Defining a 'direct' ISR"
summary: "Regular Zephyr interrupts introduce some overhead which may be unacceptable for some low-latency use-cases. Specifically:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

Regular Zephyr interrupts introduce some overhead which may be unacceptable
for some low-latency use-cases. Specifically:

* The argument to the ISR is retrieved and passed to the ISR

* If power management is enabled and the system was idle, all the hardware
  will be resumed from low-power state before the ISR is executed, which can be
  very time-consuming

* Although some architectures will do this in hardware, other architectures
  need to switch to the interrupt stack in code

* After the interrupt is serviced, the OS then performs some logic to
  potentially make a scheduling decision

* zlis must always be declared as direct ISRs, since regular
  ISRs interact with the kernel

Zephyr supports so-called 'direct' interrupts, which are installed via
`IRQ_DIRECT_CONNECT` and whose handlers are declared using
`ISR_DIRECT_DECLARE`. These direct interrupts have some special
implementation requirements and a reduced feature set; see the definitions
of `IRQ_DIRECT_CONNECT` and `ISR_DIRECT_DECLARE` for details.

Direct interrupts are only available on architectures selecting
`CONFIG_ARCH_HAS_DIRECT_INTERRUPTS`. Using
`IRQ_DIRECT_CONNECT` or `ISR_DIRECT_DECLARE` on any other
architecture fails the build.

The following code demonstrates a direct ISR:

```c

#define MY_DEV_IRQ  24       /* device uses IRQ 24 */
#define MY_DEV_PRIO  2       /* device uses interrupt priority 2 */
#define MY_IRQ_FLAGS 0       /* IRQ flags */

ISR_DIRECT_DECLARE(my_isr)
{
   do_stuff();
   /* PM done after servicing interrupt for best latency. This cannot be
   used for zero-latency IRQs because it accesses kernel data. */
   ISR_DIRECT_PM();
   /* Ask the kernel to check if scheduling decision should be made. If the
   ISR is for a zero-latency IRQ then the return value must always be 0. */
   return 1;
}

void my_isr_installer(void)
{
   ...
   IRQ_DIRECT_CONNECT(MY_DEV_IRQ, MY_DEV_PRIO, my_isr, MY_IRQ_FLAGS);
   irq_enable(MY_DEV_IRQ);
   ...
}
```
Installation of dynamic direct interrupts is supported on an
architecture-specific basis. The feature is currently implemented in the Arm
Cortex-M architecture variant via the macro
`ARM_IRQ_DIRECT_DYNAMIC_CONNECT`, which can be used to declare a direct
and dynamic interrupt.
