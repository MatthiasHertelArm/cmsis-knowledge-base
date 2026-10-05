---
id: "intr-how-to-debug-a-hardfault-on-an-arm-imprecise-fault"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Examples / Imprecise Fault"
summary: "Yikes, the error is imprecise. This means the stack frame will point to the general area where the fault occurred but not the exact instruction!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#imprecise-fault"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Examples_

#### Code

```c
void bad_addr_double_word_write(void) {
  volatile uint64_t *buf = (volatile uint64_t *)0x30000000;
  *buf = 0x1122334455667788;
}
```

#### Analysis

```
(gdb) break main
(gdb) continue
Breakpoint 4, main () at ./cortex-m-fault-debug/main.c:182
182	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=3
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x0000021c in my_fault_handler_c (frame=0x200005e8 <ucHeap+1152>) at ./cortex-m-fault-debug/startup.c:91
91	  HALT_IF_DEBUGGING();
```

Let's inspect `CFSR`:

```
(gdb) p/x *(uint32_t*)0xE000ED28
$31 = 0x400
(gdb) svd SCB CFSR_UFSR_BFSR_MMFSR
Fields in SCB CFSR_UFSR_BFSR_MMFSR:
[...]
	IMPRECISERR:  1  Imprecise data bus error
[...]
```

Yikes, the error is imprecise. This means the stack frame will point to the general area where the fault occurred but **not** the exact instruction!

```
(gdb) p/a *frame
$32 = {
  r0 = 0x55667788,
  r1 = 0x11223344,
  r2 = 0x10000000,
  r3 = 0x30000000,
  r12 = 0x200001b8 <ucHeap+80>,
  lr = 0x199 <prvQueuePingTask+52>,
  return_address = 0x198 <prvQueuePingTask+52>,
  xpsr = 0x81000000
}
(gdb) list *0x198
0x198 is in prvQueuePingTask (./cortex-m-fault-debug/main.c:162).
157
158	  while (1) {
159	    vTaskDelayUntil(&xNextWakeTime, mainQUEUE_SEND_FREQUENCY_MS);
160	    xQueueSend(xQueue, &ulValueToSend, 0U);
161
==> Crash somewhere around here
162	    trigger_crash(g_crash_config);
163	  }
164	}
165
166	static void prvQueuePongTask(void *pvParameters) {
```

#### Analysis after making the Imprecise Error Precise

If the crash was not readily reproducible we would have to inspect the code around this region and hypothesize what looks suspicious. However, [recall](#cortex-m3-m4-debug-trick) that there is a trick we can use for the Cortex-M4 to make all memory stores precise. Let's enable that and re-examine:

```
(gdb) mon reset
Resetting target
(gdb) c
Continuing.

Breakpoint 4, main () at ./cortex-m-fault-debug/main.c:182
182	  xQueue = xQueueCreate(mainQUEUE_LENGTH, sizeof(unsigned long));
(gdb) set g_crash_config=3

==> Make all memory stores precise at the cost of performance
==> by setting DISDEFWBUF in the Cortex M3/M4 ACTLR reg
(gdb) set *(uint32_t*)0xE000E008=(*(uint32_t*)0xE000E008 | 1<<1)

(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
0x0000021c in my_fault_handler_c (frame=0x200005e8 <ucHeap+1152>) at ./cortex-m-fault-debug/startup.c:91
91	  HALT_IF_DEBUGGING();
(gdb) p/a *frame
$33 = {
  r0 = 0x55667788,
  r1 = 0x11223344,
  r2 = 0x10000000,
  r3 = 0x30000000,
  r12 = 0x200001b8 <ucHeap+80>,
  lr = 0x199 <prvQueuePingTask+52>,
  return_address = 0xfa <bad_addr_double_word_write+10>,
  xpsr = 0x81000000
}
(gdb) list *0xfa
0xfa is in bad_addr_double_word_write (./cortex-m-fault-debug/main.c:92).
90	void bad_addr_double_word_write(void) {
91	  volatile uint64_t *buf = (volatile uint64_t *)0x30000000;
==> FAULT HERE
92	  *buf = 0x1122334455667788;
93	}
(gdb)
```

Awesome, that saved us some time ... we were able to determine the exact line that caused the crash!

{: #stkerr-example}
