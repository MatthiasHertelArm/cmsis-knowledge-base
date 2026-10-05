---
id: "intr-how-to-debug-a-hardfault-on-an-arm-fault-entry-exception"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples / Fault Entry Exception"
summary: "Let's take a look at CFSR again to get a clue about what happened:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#fault-entry-exception"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Examples_

#### Code

```c
void stkerr_from_psp(void) {
  extern uint32_t _start_of_ram[];
  uint8_t dummy_variable;
  const size_t distance_to_ram_bottom =
      (uint32_t)&dummy_variable - (uint32_t)_start_of_ram;
  volatile uint8_t big_buf[distance_to_ram_bottom - 8];
  for (size_t i = 0; i < sizeof(big_buf); i++) {
    big_buf[i] = i;
  }

  trigger_irq();
}
```

#### Analysis

```
(gdb) break main
(gdb) continue
Breakpoint 4, main () at ./cortex-m-fault-debug/main.c:182
182	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=4
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x0000021c in my_fault_handler_c (frame=0x1fffffe0) at ./cortex-m-fault-debug/startup.c:91
91	  HALT_IF_DEBUGGING();
```

Let's take a look at `CFSR` again to get a clue about what happened:

```
(gdb) p/x *(uint32_t*)0xE000ED28
$39 = 0x1000
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
[...]
	STKERR:       1  Bus fault on stacking for exception entry
```

#### Debug Tips when dealing with a STKERR

There are two really important things to note when a stacking exception occurs:

1. The stack pointer will always reflect the correct adjusted position as if the hardware successfully stacked the registers. This means you can find the stack pointer prior to exception entry by adding the adjustment value.
2. Depending on what access triggers the exception, the stacked frame may be partially valid. For example, the very last store of the hardware stacking could trigger the fault and all the other stores could be valid. However, the **order** the hardware pushes register state on the stack is **implementation specific**. So when inspecting the frame assume the values being looked at may be invalid!

Taking this knowledge into account, let's examine the stack frame:

```
(gdb) p frame
$40 = (sContextStateFrame *) 0x1fffffe0
```

Interestingly, if we look up the memory map of the NRF52[^10], we will find that RAM starts at `0x20000000`. Our stack pointer location, `0x1fffffe0` is right below that in an undefined memory region. This must be why we faulted! We see that the stack pointer is 32 bytes below RAM, which matches the size of `sContextStateFrame`. This unfortunately means none of the values stacked will be valid since all stores were issued to a non-existent address space!

We can manually walk up the stack to get some clues:

```
(gdb) x/a 0x20000000
0x20000000 <uxCriticalNesting>:	0x3020100
(gdb)
0x20000004 <g_crash_config>:	0x7060504
(gdb)
0x20000008 <xQueue>:	0xb0a0908
(gdb)
0x2000000c <s_buffer>:	0xf0e0d0c
(gdb)
0x20000010 <s_buffer+4>:	0x13121110
(gdb)
0x20000014 <s_buffer+8>:	0x17161514
(gdb)
0x20000018 <pxCurrentTCB>:	0x1b1a1918
(gdb)
0x2000001c <pxDelayedTaskList>:	0x1f1e1d1c
(gdb)
0x20000020 <pxOverflowDelayedTaskList>:	0x23222120
```

It looks like the RAM has a pattern of sequentially increasing values _and_ that the RAM addresses map to different variables in our code (i.e `pxCurrentTCB`). This suggests we overflowed the stack we were using and started to clobber RAM in the system until we ran off the end of RAM!

> TIP: To catch this type of failure sooner consider using an [MPU Region](https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#catch-stack-overflows-with-the-mpu)

Since the crash is reproducible, let's leverage a watchpoint and see if we can capture the stack corruption in action! Let's add a watchpoint for any access near the bottom of RAM, `0x2000000c`:

```
(gdb) mon reset
(gdb) continue
Breakpoint 4, main () at ./cortex-m-fault-debug/main.c:182
182	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=4
(gdb) watch *(uint32_t*)0x2000000c
Hardware watchpoint 9: *(uint32_t*)0x2000000c
```

> TIP: Sometimes it will take a couple tries to choose the right RAM range to watch. It's possible an area of the stack never gets written to and the watchpoint never fires or that the memory address being watched gets updated many many times before the actual failure. In this example, I intentionally opted not to watch 0x20000000 because that is the address of a FreeRTOS variable, `uxCriticalNesting` which is updated a lot.

Let's continue and see what happens:

```
(gdb) continue
Hardware watchpoint 9: *(uint32_t*)0x2000000c

Old value = 0
New value = 12
0x000000c0 in stkerr_from_psp () at ./cortex-m-fault-debug/main.c:68
68	    big_buf[i] = i;
(gdb) bt
#0  0x000000c0 in stkerr_from_psp () at ./cortex-m-fault-debug/main.c:68
#1  0x00000198 in prvQueuePingTask (pvParameters=<optimized out>) at ./cortex-m-fault-debug/main.c:162
#2  0x00001488 in ?? () at ./cortex-m-fault-debug/freertos_kernel/portable/GCC/ARM_CM4F/port.c:703
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb) list *0xc0
0xc0 is in stkerr_from_psp (./cortex-m-fault-debug/main.c:68).
63	  extern uint32_t _start_of_ram[];
64	  uint8_t dummy_variable;
65	  const size_t distance_to_ram_bottom = (uint32_t)&dummy_variable - (uint32_t)_start_of_ram;
66	  volatile uint8_t big_buf[distance_to_ram_bottom - 8];
67	  for (size_t i = 0; i < sizeof(big_buf); i++) {
68	    big_buf[i] = i;
69	  }
70
71	  trigger_irq();
72	}
```

Great, we've found a variable located on the stack `big_buf` being updated. It must be this function call path which is leading to a stack overflow. We can now inspect the call chain and remove big stack allocations!

{: #usage-fault-recovery-example}
