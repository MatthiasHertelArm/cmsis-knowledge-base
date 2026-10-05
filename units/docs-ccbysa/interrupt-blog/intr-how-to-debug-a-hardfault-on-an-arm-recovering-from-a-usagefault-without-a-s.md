---
id: "intr-how-to-debug-a-hardfault-on-an-arm-recovering-from-a-usagefault-without-a-s"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples / Recovering from a UsageFault **without** a SYSRESET"
summary: "In this example we'll just step through the code we developed above and confirm we don't reset when a UsageFault occurs."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#recovering-from-a-usagefault-without-a-sysreset"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Examples_

In this example we'll just step through the code we developed [above](#recovering-from-a-fault) and confirm we don't reset when a UsageFault occurs.

#### Code

```c
void unaligned_double_word_read(void) {
  extern void *g_unaligned_buffer;
  uint64_t *buf = g_unaligned_buffer;
  *buf = 0x1122334455667788;
}
```

#### Analysis

```
(gdb) break main
(gdb) continue
Breakpoint 4, main () at ./cortex-m-fault-debug/main.c:188
188	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=5
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x00000228 in my_fault_handler_c (frame=0x200005e8 <ucHeap+1152>) at ./cortex-m-fault-debug/startup.c:94
94	  HALT_IF_DEBUGGING();
```

We have entered the breakpoint in the fault handler. We can step over it and confirm we fall through to the `recover_from_task_fault` function.

```
(gdb) break recover_from_task_fault
Breakpoint 12 at 0x1a8: file ./cortex-m-fault-debug/main.c, line 181.
(gdb) n
108	  volatile uint32_t *cfsr = (volatile uint32_t *)0xE000ED28;
(gdb) c
Continuing.

Breakpoint 12, recover_from_task_fault () at ./cortex-m-fault-debug/main.c:181
181	void recover_from_task_fault(void) {

(gdb) list *recover_from_task_fault
0x1a8 is in recover_from_task_fault (./cortex-m-fault-debug/main.c:181).
181	void recover_from_task_fault(void) {
182	  while (1) {
183	    vTaskDelay(1);
184	  }
185	}
```

If we continue from here we will see the system happily keeps running because the thread which was calling the problematic `trigger_crash` function is now parked in a while loop. The the while loop could be extended in the future to delete and/or restart the FreeRTOS task if we wanted as well.

{:.no_toc}
