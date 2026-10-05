---
id: "zep-interrupts-defining-a-regular-isr"
type: "concept"
domain: "rtos"
title: "Interrupts: Implementation / Defining a regular ISR"
summary: "An ISR is defined at runtime by calling IRQ_CONNECT. It must then be enabled by calling irq_enable."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/interrupts.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/interrupts.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

An ISR is defined at runtime by calling `IRQ_CONNECT`. It must
then be enabled by calling `irq_enable`.


**Note:** The unprefixed interrupt control APIs such as `irq_enable` and namespaced equivalents, `k_irq_enable`, `k_irq_lock` and so on. The unprefixed names remain fully supported.


**Important:** IRQ_CONNECT() is not a C function and does some inline assembly magic behind the scenes. All its arguments must be known at build time. Drivers that have multiple instances may need to define per-instance config functions to configure each instance of the interrupt.

The following code defines and enables an ISR.

```c

#define MY_DEV_IRQ  24       /* device uses IRQ 24 */
#define MY_DEV_PRIO  2       /* device uses interrupt priority 2 */
/* argument passed to my_isr(), in this case a pointer to the device */
#define MY_ISR_ARG  DEVICE_GET(my_device)
#define MY_IRQ_FLAGS 0       /* IRQ flags */

void my_isr(void *arg)
{
   ... /* ISR code */
}

void my_isr_installer(void)
{
   ...
   IRQ_CONNECT(MY_DEV_IRQ, MY_DEV_PRIO, my_isr, MY_ISR_ARG, MY_IRQ_FLAGS);
   irq_enable(MY_DEV_IRQ);
   ...
}
```
Since the `IRQ_CONNECT` macro requires that all its parameters be
known at build time, in some cases this may not be acceptable. It is also
possible to install interrupts at runtime with
`irq_connect_dynamic`. It is used in exactly the same way as
`IRQ_CONNECT`:

```c

void my_isr_installer(void)
{
   ...
   irq_connect_dynamic(MY_DEV_IRQ, MY_DEV_PRIO, my_isr, MY_ISR_ARG,
                       MY_IRQ_FLAGS);
   irq_enable(MY_DEV_IRQ);
   ...
}
```
Dynamic interrupts require the `CONFIG_DYNAMIC_INTERRUPTS` option to
be enabled. Removing or re-configuring a dynamic interrupt is currently
unsupported.
