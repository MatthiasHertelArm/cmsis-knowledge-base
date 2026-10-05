---
id: "intr-a-practical-guide-to-arm-cortex-m-triggering-a-built-in-exception-pendsv"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Code Examples / Triggering a Built In Exception (PendSV)"
summary: "Let's first start by generating a common built in exception, often used for RTOS context switching, the PendSV exception handler. To make it easier to step through the code with a debugger and examine register state, let's utilize breakpoint instructions."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#triggering-a-built-in-exception-pendsv"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Code Examples_

Let's first start by generating a common built in exception, often used for RTOS context switching,
the PendSV exception handler. To make it easier to step through the code with a debugger and
examine register state, let's utilize breakpoint instructions.

```c
void PendSV_Handler(void) {
  __asm("bkpt 1");
}

__attribute__((optimize("O0")))
static void trigger_pendsv(void) {
  volatile uint32_t *icsr = (void *)0xE000ED04;
  // Pend a PendSV exception using by writing 1 to PENDSVSET at bit 28
  *icsr = 0x1 << 28;
  // flush pipeline to ensure exception takes effect before we
  // return from this routine
  __asm("isb");
}
```

Let's call `trigger_pendsv()` from our main loop and see what happens!

```
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
PendSV_Handler () at ../../../main.c:48
48    __asm("bkpt 1");
(gdb)
```

Great we see the `PendSV_Handler` was invoked. We can read the `ICSR` register (specifically
`VECTACTIVE`, `RETTOBASE`, & `VECTPENDING`) described [above](#icsr-register) for
additional context:

```
(gdb) p/x (*(uint32_t*)0xE000ED04)&0xff
$2 = 0xe
(gdb) p/x (*(uint32_t*)0xE000ED04)>>11&0x1
$3 = 0x1
(gdb) p/x (*(uint32_t*)0xE000ED04)>>12&0xff
$4 = 0x0
```

The first 8 bits (`VECTACTIVE`) tell us that Exception Number 0xe is active. This is the PendSV Exception so that
matches what we expect! We see `RETTOBASE` is `1` so no other exceptions are active. And bits 12-20 (`VECTPENDING`)
are zero so we also know no other exceptions are pended.
