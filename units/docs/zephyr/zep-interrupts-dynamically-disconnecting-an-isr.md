---
id: "zep-interrupts-dynamically-disconnecting-an-isr"
type: "concept"
domain: "rtos"
title: "Interrupts: Implementation / Dynamically disconnecting an ISR"
summary: "The following code defines two ISRs using the same interrupt number. The second ISR is disconnected during runtime."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

The following code defines two ISRs using the same interrupt number. The second
ISR is disconnected during runtime.

```c

#define MY_DEV_IRQ 24        /* device uses INTID 24 */
#define MY_DEV_IRQ_PRIO 2        /* device uses interrupt priority 2 */
/*  this argument may be anything */
#define MY_FST_ISR_ARG INT_TO_POINTER(1)
/*  this argument may be anything */
#define MY_SND_ISR_ARG INT_TO_POINTER(2)
#define MY_IRQ_FLAGS 0        /* IRQ flags */

void my_first_isr(void *arg)
{
   ... /* some magic happens here */
}

void my_second_isr(void *arg)
{
   ... /* even more magic happens here */
}

void my_isr_installer(void)
{
   ...
   IRQ_CONNECT(MY_DEV_IRQ, MY_DEV_IRQ_PRIO, my_first_isr, MY_FST_ISR_ARG, MY_IRQ_FLAGS);
   IRQ_CONNECT(MY_DEV_IRQ, MY_DEV_IRQ_PRIO, my_second_isr, MY_SND_ISR_ARG, MY_IRQ_FLAGS);
   ...
}

void my_isr_uninstaller(void)
{
   ...
   irq_disconnect_dynamic(MY_DEV_IRQ, MY_DEV_IRQ_PRIO, my_first_isr, MY_FST_ISR_ARG, MY_IRQ_FLAGS);
   ...
}
```
The `irq_disconnect_dynamic` call will result in interrupt 24 becoming
unshared, meaning the system will act as if the first `IRQ_CONNECT`
call never happened. This behaviour is only allowed if
`CONFIG_DYNAMIC_INTERRUPTS` is enabled, otherwise a linker
error will be generated.
