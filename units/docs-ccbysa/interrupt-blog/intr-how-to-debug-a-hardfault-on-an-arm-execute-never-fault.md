---
id: "intr-how-to-debug-a-hardfault-on-an-arm-execute-never-fault"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples / eXecute Never Fault"
summary: "We can check the CFSR to see if there is any information about the fault which occurred."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#execute-never-fault"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Examples_

#### Code

```c
int illegal_instruction_execution(void) {
  int (*bad_instruction)(void) = (void *)0xE0000000;
  return bad_instruction();
}
```

#### Analysis

```
(gdb) break main
(gdb) continue
Breakpoint 1, main () at ./cortex-m-fault-debug/main.c:180
180	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=0
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00000218 in my_fault_handler_c (frame=0x200005e8 <ucHeap+1152>) at ./cortex-m-fault-debug/startup.c:91
91	  HALT_IF_DEBUGGING();
(gdb) bt
#0  0x00000218 in my_fault_handler_c (frame=0x200005e8 <ucHeap+1152>) at ./cortex-m-fault-debug/startup.c:91
#1  <signal handler called>
#2  0x00001468 in prvPortStartFirstTask () at ./cortex-m-fault-debug/freertos_kernel/portable/GCC/ARM_CM4F/port.c:267
#3  0x000016e6 in xPortStartScheduler () at ./cortex-m-fault-debug/freertos_kernel/portable/GCC/ARM_CM4F/port.c:379
#4  0x1058e476 in ?? ()
```

We can check the `CFSR` to see if there is any information about the fault which occurred.

```
(gdb) p/x *(uint32_t*)0xE000ED28
$3 = 0x1
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
	IACCVIOL:     1  Instruction access violation flag
[...]
```

That's interesting! We hit a Memory Management instruction access violation fault even though we haven't enabled any MPU regions. From the CFSR, we know that the stacked frame is valid so we can take a look at that to see what it reveals:

```
(gdb) p/a *frame
$1 = {
  r0 = 0x0 <g_pfnVectors>,
  r1 = 0x200003c4 <ucHeap+604>,
  r2 = 0x10000000,
  r3 = 0xe0000000,
  r12 = 0x200001b8 <ucHeap+80>,
  lr = 0x195 <prvQueuePingTask+52>,
  return_address = 0xe0000000,
  xpsr = 0x80000000
}
```

We can clearly see that the executing instruction was `0xe0000000` and that the calling function was `prvQueuePingTask`.

From the ARMv7-M reference manual[^9] we find:

> The MPU is restricted in how it can change the default memory map attributes associated with System space, that is, for addresses 0xE0000000 and higher. System space is always marked as XN, Execute Never.

So the fault registers didn't lie to us, and it does make sense that we hit a memory management fault!

{: #bad-address-read-example}
