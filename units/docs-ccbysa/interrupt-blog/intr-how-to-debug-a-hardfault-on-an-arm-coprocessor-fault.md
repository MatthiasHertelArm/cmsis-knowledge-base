---
id: "intr-how-to-debug-a-hardfault-on-an-arm-coprocessor-fault"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples / Coprocessor Fault"
summary: "We can inspect CFSR to get a clue about the crash which took place"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#coprocessor-fault"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Examples_

#### Code

```c
void access_disabled_coprocessor(void) {
  // FreeRTOS will automatically enable the FPU co-processor.
  // Let's disable it for the purposes of this example
  __asm volatile(
      "ldr r0, =0xE000ED88 \n"
      "mov r1, #0 \n"
      "str r1, [r0]	\n"
      "dsb \n"
      "vmov r0, s0 \n"
      );
}
```

#### Analysis

```
(gdb) break main
(gdb) continue
Breakpoint 4, main () at ./cortex-m-fault-debug/main.c:180
180	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=2
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00000218 in my_fault_handler_c (frame=0x20002d80) at ./cortex-m-fault-debug/startup.c:91
91	  HALT_IF_DEBUGGING();
```

We can inspect `CFSR` to get a clue about the crash which took place

```
(gdb) p/x *(uint32_t*)0xE000ED28
$13 = 0x8200
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
[...]
	NOCP:         1  No coprocessor usage fault.
[...]
```

We see it was a coprocessor UsageFault which tells us we either issued an instruction to a non-existent or disabled Cortex-M coprocessor. We know the frame contents are valid so we can inspect that to figure out where the fault originated:

```
(gdb) p/a *frame
$27 = {
  r0 = 0xe000ed88,
  r1 = 0x0 <g_pfnVectors>,
  r2 = 0x10000000,
  r3 = 0x0 <g_pfnVectors>,
  r12 = 0x200001b8 <ucHeap+80>,
  lr = 0x199 <prvQueuePingTask+52>,
  return_address = 0x114 <access_disabled_coprocessor+12>,
  xpsr = 0x81000000
}

(gdb) disassemble 0x114
Dump of assembler code for function access_disabled_coprocessor:
   0x00000108 <+0>:	ldr	r0, [pc, #16]	; (0x11c)
   0x0000010a <+2>:	mov.w	r1, #0
   0x0000010e <+6>:	str	r1, [r0, #0]
   0x00000110 <+8>:	dsb	sy
===> FAULT HERE on a Floating Point instruction
   0x00000114 <+12>:	vmov	r0, s0
   0x00000118 <+16>:	bx	lr
```

`vmov` is a floating point instruction so we now know what coprocessor the NOCP was caused by. The FPU is enabled using bits 20-23 of the [CPACR](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#fpu-config-options) register located at `0xE000ED88`. A value of 0 indicates the extension is disabled. Let's check it:

```
(gdb) p/x (*(uint32_t*)0xE000ED88 >> 20) & 0xf
$29 = 0x0
```

We can clearly see the FP Extension is disabled. We will have to enable the FPU to fix our bug.

{: #imprecise-error-code-example}
