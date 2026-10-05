---
id: "intr-diving-into-jtag-debugging-part-2-interacting-with-the-processor-core"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2): Interacting with the Processor Core"
summary: "Well, we’ve explored how the debugger interacts with the microcontroller’s memory. Now, let’s delve into how the debugger can halt program execution, step through code, read the processor’s registers, and so on."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2#interacting-with-the-processor-core"
license: "CC-BY-SA-4.0"
mode: "V"
---

Well, we’ve explored how the debugger interacts with the microcontroller’s memory. Now, let’s delve into how the debugger can halt program execution, step through code, read the processor’s registers, and so on. In the case of the STM32F407VG microcontroller, this is achieved through special registers:



As detailed in section *C1.6 Debug system registers* of the [ARMv7-M Architecture Reference Manual](https://developer.arm.com/documentation/ddi0403/latest/), these registers play a pivotal role in debugging.

What’s crucial for us now is understanding that by setting the `C_DEBUGEN` and `C_HALT` bits of the `DHCSR` register, we can halt the execution of the program. Similarly, by setting the `C_DEBUGEN` and `C_STEP` bits, we can execute the program step by step.

Access to these registers via the DAP module is essentially the same as accessing memory. Instead of providing a memory address, you provide the address of the desired register. For instance, in the case of the `DHCSR` register, the address is `0xE000EDF0`. If you let me, I won't delve into an example with the bit sequence since it would be identical to the example from the chapter on memory interaction.
