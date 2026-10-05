---
id: "intr-how-to-debug-a-hardfault-on-an-arm-recovering-the-call-stack"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Recovering the Call Stack"
summary: "To fix a fault, we will want to determine what code was running when the fault occurred. To accomplish this, we need to recover the register state at the time of exception entry."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#recovering-the-call-stack"
license: "CC-BY-SA-4.0"
mode: "V"
---

To fix a fault, we will want to determine what code was running when the fault occurred. To accomplish this, we need to recover the register state at the time of exception entry.

If the fault is readily reproducible and we have a debugger attached to the board, we can manually add a breakpoint for the function which handles the exception. In GDB this will look something like

```shell
(gdb) break HardFault_Handler
```

Upon exception entry some registers will always be automatically saved on the stack. Depending on whether or not an FPU is in use, either a [basic](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#basic-context-state-frame) or [extended](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#extended-context-state-frame) stack frame will be pushed by hardware.

{: #determine-pre-exception-sp}
Regardless, the hardware will _always_ push the same core set of registers to the very top of the stack which was active prior to entering the exception. ARM Cortex-M devices have [two stack pointers](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#stack-pointers-and-usage), `msp` & `psp`. Upon exception entry, the active stack pointer is encoded in bit 2 of the `EXC_RETURN` value pushed to the link register. If the bit is set, the `psp` was active prior to exception entry, else the `msp` was active.

Let's look at the state when we break in `HardFault_Handler` for a pathological example:

```c
int illegal_instruction_execution(void) {
  int (*bad_instruction)(void) = (void *)0xE0000000;
  return bad_instruction();
}
```

```
(gdb) p/x $lr
$4 = 0xfffffffd

# psp was active prior to exception if bit 2 is set
# otherwise, the msp was active
(gdb) p/x $lr&(1<<2)
$5 = 0x4

# First eight values on stack will always be:
# r0, r1, r2, r3, r12, LR, pc, xPSR
(gdb) p/a *(uint32_t[8] *)$psp
$16 = {
  0x0 <g_pfnVectors>,
  0x200003c4 <ucHeap+604>,
  0x10000000,
  0xe0000000,
  0x200001b8 <ucHeap+80>,
  0x61 <illegal_instruction_execution+16>,
  0xe0000000,
  0x80000000
}
```

Offset 6 and 7 in the array dumped hold the LR (`illegal_instruction_execution`) & PC (`0xe0000000`) so we now can see exactly where the fault originated!

{:.no_toc}
