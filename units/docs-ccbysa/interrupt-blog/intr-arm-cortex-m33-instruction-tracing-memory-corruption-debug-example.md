---
id: "intr-arm-cortex-m33-instruction-tracing-memory-corruption-debug-example"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Example Project / Memory Corruption Debug Example"
summary: "Another challenging type of crash to resolve is a hardfault that arises after executing a sequence of instructions that corrupts register state. Some cases where I've seen this happen in the past include:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#memory-corruption-debug-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Example Project_

Another challenging type of crash to resolve is a hardfault that arises after executing a sequence of instructions that corrupts register state. Some cases where I've seen this happen in the past include:

- Memory corruption leading to the execution of a random memory region as if it is a sequence of instructions
- Memory being used after it was free and a function pointer within that memory no longer being correct
- A misconfigured vector table leading to the execution of bogus code on exception entry
- Incorrect assembly leading to invalid execution path.

Let's check out an example:

```
$ make flash
# Enable stack overflow example
(gdb) set g_trace_example_config=2
(gdb) Program received signal SIGTRAP, Trace/breakpoint trap.
HardFault_Handler () at ./main.c:106
106   __asm("bkpt 6");


```

In this scenario, even if we follow the steps from our previous post on how [to recover the callstack after a HardFault](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#registers-prior-to-exception), there isn't a lot of context revealed.

```
p/a *(uint32_t[8] *)$psp
$2 = {
  0x0,
  0x200083b4 <ucHeap+84>,
  0xbf00de4d,
  0x2,
  0x200085a4 <ucHeap+580>,
==> lr
  0x0,
==> pc
  0xbf00de4c,
  0x61000000
}
```

A full discussion is outside the scope of this article but by dumping the `$psp` we can find out the `lr` prior to this exception was `0x00000000` and the `pc` was `0xbf00de4c`. All this really tells us is something is seriously wrong!

However, with the MTB output we should be able to see the exact instruction execution history. Let's try it out:

```
(gdb) mtb --limit 10
>S: 0x20002f24 - 0x20002f24 @ ?:?
 D: 0x20001ef6 - xQueueReceive @ ./freertos_kernel/queue.c:1356
>S: 0x20001efa - xQueueReceive @ ./freertos_kernel/queue.c:1361
 D: 0x20001f16 - xQueueReceive @ ./freertos_kernel/queue.c:1377
>S: 0x20001f16 - xQueueReceive @ ./freertos_kernel/queue.c:1377
 D: 0x20002bd4 - vPortExitCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:427
>S: 0x20002bda - vPortExitCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:427
 D: 0x20002be6 - vPortExitCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/port.c:428
>S: 0x20002bf2 - vPortExitCritical @ ./freertos_kernel/portable/GCC/ARM_CM4F/portmacro.h:231
 D: 0x20001f1a - xQueueReceive @ ./freertos_kernel/queue.c:1378
>S: 0x20001f1e - xQueueReceive @ ./freertos_kernel/queue.c:1378
 D: 0x2000045e - prvQueuePongTask @ ./main.c:86
>S: 0x20000468 - prvQueuePongTask @ ./main.c:91
 D: 0x200003ec - bad_asm_function @ ./main.c:75
>S: 0x200003f6 - bad_asm_function @ ./main.c:75
 D: 0xbf00de4c - 0xbf00de4c @ ?:?
>S: 0xbf00de4c - Exception (or debug) Entry from 0xbf00de4c @ ?:?
 D: 0x20000486 - HardFault_Handler @ ./main.c:107
>S: 0x20000488 - HardFault_Handler @ ./main.c:107
 D: 0x200004e0 - mtb_disable @ ./mtb.c:41
```

From the trace we can immediately see what was executing prior to the bad jump to `0xbf00de4c`. In
this case it is a suspiciously named function that I instrumented, `bad_asm_function()` which was
invoked from `prvQueuePongTask()`:

```c
// for illustrative purposes, an assembly function that clobbers
// the lr and then jumps to a bogus address
__attribute__((naked))
static void bad_asm_function(void) {
  __asm("mov r0, 0 \n"
        "ldr r2, =3204505165 \n"
        "mov lr, 0 \n"
        "bx r2 \n"
        );
}
```

Although contrived, I hope the example conveys the general idea how the instruction trace can be useful for root causing this class of bug!
