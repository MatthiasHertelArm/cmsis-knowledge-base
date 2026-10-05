---
id: "intr-a-practical-guide-to-arm-cortex-m-pre-emption-of-an-nvic-interrupt"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Code Examples / Pre-emption of an NVIC Interrupt"
summary: "Now let's configure one interrupt in the NVIC and then call trigger_pendsv() from that interrupt to check out pre-emption!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#pre-emption-of-an-nvic-interrupt"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Code Examples_

Now let's configure one interrupt in the NVIC and then call `trigger_pendsv()` from that interrupt
to check out pre-emption!

```c
__attribute__((optimize("O0")))
void POWER_CLOCK_IRQHandler(void) {
  __asm("bkpt 2");
  trigger_pendsv();
  __asm("bkpt 3");
}

static void trigger_nvic_int0(void) {
  // Let's set the interrupt priority to be the
  // lowest possible for the NRF52. Note the default
  // NVIC priority is zero which would match our current pendsv
  // config so no pre-emption would take place if we didn't change this
  volatile uint32_t *nvic_ipr = (void *)0xE000E400;
  *nvic_ipr = 0xe0;

  // Enable the POWER_CLOCK_IRQ (External Interrupt 0)
  volatile uint32_t *nvic_iser = (void *)0xE000E100;
  *nvic_iser |= 0x1;

  // Pend an interrupt
  volatile uint32_t *nvic_ispr = (void *)0xE000E200;
  *nvic_ispr |= 0x1;

  // flush pipeline to ensure exception takes effect before we
  // return from this routine
  __asm("isb");
}
```

Let's call `trigger_nvic_int0` from our main loop and explore what happens!

```
Program received signal SIGTRAP, Trace/breakpoint trap.
POWER_CLOCK_IRQHandler () at ../../../main.c:53
53    __asm("bkpt 2");
(gdb) p/x *(uint32_t*)0xE000ED04
$1 = 0x810
```

Reading the ICSR register again, we see the active exception number is 0x10 corresponding to external interrupt 0 and that no
other exceptions are pended or active. Let's continue!

```
(gdb) next
54    trigger_pendsv();
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
PendSV_Handler () at ../../../main.c:38
38    __asm("bkpt 1");
(gdb) bt
#0  PendSV_Handler () at ../../../main.c:38
#1  <signal handler called>
#2  0x00000306 in trigger_pendsv () at ../../../main.c:48
#3  0x00000322 in POWER_CLOCK_IRQHandler () at ../../../main.c:54
#4  <signal handler called>
#5  0x000003a8 in trigger_nvic_int0 () at ../../../main.c:76
#6  main (a=<optimized out>, argv=<optimized out>) at ../../../main.c:129
(gdb) p/x *(uint32_t*)0xE000ED04
$2 = 0xe
```

The active exception is 0xe, PendSV -- just like we saw in the [first example](#pendsv-example). We see the `RETTOBASE` bit is
clear meaning another exception is active (NVIC Interrupt 0). We can also check this by looking at
the `NVIC_IABR` registers described [above](#iabr-register) and confirming bit 1 is set:

```
(gdb) p/x *(uint32_t[16] *)0xE000E300
$3 = {0x1, 0x0 <repeats 15 times>}
```

We can continue from here and confirm we drop back to the first exception:

```
(gdb) next
POWER_CLOCK_IRQHandler () at ../../../main.c:55
55    __asm("bkpt 3");
(gdb) p/x *(uint16_t[16] *)0xE000E300
$4 = {0x1, 0x0 <repeats 15 times>}
(gdb) p/x *(uint32_t*)0xE000ED04
$5 = 0x810
```

{: #complex-config-example}
