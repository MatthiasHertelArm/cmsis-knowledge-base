---
id: "intr-how-to-debug-a-hardfault-on-an-arm-bad-address-read"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples / Bad Address Read"
summary: "Again, let's take a look at the CFSR and see if it tells us anything useful."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#bad-address-read"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Examples_

#### Code

```c
uint32_t read_from_bad_address(void) {
  return *(volatile uint32_t *)0xbadcafe;
}
```

#### Analysis

```
(gdb) break main
(gdb) continue
Breakpoint 1, main () at ./cortex-m-fault-debug/main.c:189
189	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=1
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00000218 in my_fault_handler_c (frame=0x200005e8 <ucHeap+1152>) at ./cortex-m-fault-debug/startup.c:91
91	  HALT_IF_DEBUGGING();
```

Again, let's take a look at the `CFSR` and see if it tells us anything useful.

```
(gdb) p/x *(uint32_t*)0xE000ED28
$13 = 0x8200
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
[...]
    PRECISERR:    1  Precise data bus error
[...]
    BFARVALID:    1  Bus Fault Address Register (BFAR) valid flag
```

Great, we have a precise bus fault which means the return address in the stack frame holds the instruction which triggered the fault and that we can read BFAR to determine what memory access triggered the fault!

```
(gdb) svd/x SCB BFAR
Fields in SCB BFAR:
	BFAR:  0x0BADCAFE  Bus fault address

(gdb) p/a *frame
$16 = {
  r0 = 0x1 <g_pfnVectors+1>,
  r1 = 0x200003c4 <ucHeap+604>,
  r2 = 0x10000000,
  r3 = 0xbadcafe,
  r12 = 0x200001b8 <ucHeap+80>,
  lr = 0x195 <prvQueuePingTask+52>,
  return_address = 0x13a <trigger_crash+22>,
  xpsr = 0x81000000
}

(gdb) info line *0x13a
Line 123 of "./cortex-m-fault-debug/main.c" starts at address 0x138 <trigger_crash+20> and ends at 0x13e <trigger_crash+26>.

(gdb) list *0x13a
0x13a is in trigger_crash (./cortex-m-fault-debug/main.c:123).
118	  switch (crash_id) {
119	    case 0:
120	      illegal_instruction_execution();
121	      break;
122	    case 1:
===> FAULT HERE
123	      read_from_bad_address();
124	      break;
125	    case 2:
126	      access_disabled_coprocessor();
127	      break;
```

Great, so we have pinpointed the exact code which triggered the issue and can now fix it!

{: #coprocessor-fault-example}
