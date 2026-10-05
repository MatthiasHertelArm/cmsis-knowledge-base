---
id: "intr-a-guide-to-watchdog-timers-for-emb-debugging-hangs-inside-interrupts"
type: "concept"
domain: "debug"
title: "A Guide to Watchdog Timers for Embedded Systems: Debugging Hangs Inside Interrupts"
summary: "Let's see how the system fairs if a hang occurs within an ISR:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-18-firmware-watchdog-best-practices.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#debugging-hangs-inside-interrupts"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's see how the system fairs if a hang occurs within an ISR:

```
(gdb) set g_watchdog_hang_config=4
(gdb) c
Continuing.
Resuming Software Watchdog
(gdb) p/a *frame
$2 = {
  r0 = 0x3 <g_pfnVectors+3>,
  r1 = 0x200001bc <ucHeap+84>,
  r2 = 0xe000e100,
  r3 = 0x1 <g_pfnVectors+1>,
  r12 = 0x200003e0 <ucHeap+632>,
  lr = 0xfffffffd,
  return_address = 0xd0 <ExternalInt0_Handler>,
  xpsr = 0x21000010
}
```

The return address points to an interrupt handler, `ExternalInt0_Handler`. Inspecting the code it does indeed hang:

```c
void ExternalInt0_Handler(void) {
  while (1) {}
}
```

### ARM Cortex-M Design Suggestions

Over the years, I've developed a set of best practices for implementing watchdogs on cortex-M MCUs:

- Make sure the software watchdog handler runs at the highest possible configurable priority and that all other interrupts run at a priority less than that. This way even if the hang is within an ISR, the software handler will be able to run and you will be able to trace what went wrong.
- If the architecture supports configuring the BASEPRI (any Cortex-M except Cortex-M0's), use `__set_BASEPRI` for entering and exiting critical sections instead of `__disable/__enable_irq()`. In this manner you can ensure the "Software Watchdog" interrupt handler is always enabled and even catch hangs which occur from within a critical section!

> NOTE: For more info about ARM exceptions in general, check out [our post here](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic)
