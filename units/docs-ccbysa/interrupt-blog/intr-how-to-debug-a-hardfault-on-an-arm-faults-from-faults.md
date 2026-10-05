---
id: "intr-how-to-debug-a-hardfault-on-an-arm-faults-from-faults"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Faults from Faults!"
summary: "The astute observer might wonder what happens when a new fault occurs in the code dealing with a fault."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#faults-from-faults"
license: "CC-BY-SA-4.0"
mode: "V"
---

The astute observer might wonder what happens when a new fault occurs in the code dealing with a fault.
If you have enabled configurable fault handlers (i.e MemManage, BusFault, or UsageFault), a fault generated in these handlers will trigger a HardFault.

Once in the HardFault Handler, the ARM Core is operating at a non-configurable priority level, -1. At this level or above, a fault will put the processor in an unrecoverable state where a reset is expected. This state is known as **Lockup**.

Typically, the processor will automatically reset upon entering lockup but this is not a requirement per the specification. For example, you may have to enable a hardware watchdog for a reset to take place. It's worth double checking the reference manual for the MCU being used for clarification.

When a debugger is attached, lockup often has a different behavior. For example, on the NRF52840,
"Reset from CPU lockup is disabled if the device is in debug interface mode"[^11].

When a lockup happens, the processor will repeatedly fetch the same fixed instruction, `0xFFFFFFFE` or the instruction which triggered the lockup, in a loop until a reset occurs.

> Fun Fact: Whether or not some classes of MemManage or BusFaults trigger a fault from an exception
> is actually configurable via the MPU_CTRL.HFNMIENA & CCR.BFHFNMIGN register fields, respectively.

{: #automating-the-analysis}
