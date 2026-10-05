---
id: "intr-a-guide-to-using-arm-stack-limit-r-references"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers: References"
summary: "[^m33-psplim_msplim]: Cortex M33 MSPLIM PSPLIM TRM"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow#references"
license: "CC-BY-SA-4.0"
mode: "V"
---

[^m33-psplim_msplim]:
    [Cortex M33 MSPLIM PSPLIM TRM](https://developer.arm.com/documentation/100231/0002/)

[^m33-usfr]:
    [Cortex M33 USFR](https://developer.arm.com/documentation/100235/0004/the-cortex-m33-peripherals/system-control-block/configurable-fault-status-register)

[^ARMV8_Guards]:
    [DA1469x Github Example](https://github.com/dialog-semiconductor/BLE_SDK10_examples/tree/main/features/armv8_stack_overflow_guards)

[^gcc_attributes]:
    [GCC Attributes](https://gcc.gnu.org/onlinedocs/gcc-4.3.0/gcc/Function-Attributes.html#Function-Attributes)

[^1]:
    [FreeRTOS Kernel Stack Overflow Check](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/a8a9c3ea3e34c10c6818f654883dac3dbdae12d1/tasks.c#L3052)

[^2]:
    [FreeRTOS Stack Overflow Check](https://www.freertos.org/Stacks-and-stack-overflow-checking.html)

[^3]:
    [DA14695 Development Kit – USB](https://www.dialog-semiconductor.com/products/da14695-development-kit-usb)

[^4]:
    [DA1469x Datasheet](https://www.dialog-semiconductor.com/sites/default/files/da1469x_datasheet_3v2.pdf)

[^5]:
    [GCC Instrumentation Options](https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html)
