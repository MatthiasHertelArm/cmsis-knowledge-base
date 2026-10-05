---
id: "zep-interrupts-sharing-an-interrupt-line"
type: "concept"
domain: "rtos"
title: "Interrupts: Implementation / Sharing an interrupt line"
summary: "The following code defines two ISRs using the same interrupt number."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

The following code defines two ISRs using the same interrupt number.

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
```
The same restrictions regarding `IRQ_CONNECT` described in Defining a regular ISR
are applicable here. If `CONFIG_SHARED_INTERRUPTS` is disabled, the above
code will generate a build error. Otherwise, the above code will result in the two ISRs
being invoked each time interrupt 24 is triggered.

If `CONFIG_SHARED_IRQ_MAX_NUM_CLIENTS` is set to a value lower than 2
(current number of clients), a build error will be generated.

If dynamic interrupts are enabled, `irq_connect_dynamic` will allow sharing interrupts
during runtime. Exceeding the configured maximum number of allowed clients will result in
a failed assertion.
