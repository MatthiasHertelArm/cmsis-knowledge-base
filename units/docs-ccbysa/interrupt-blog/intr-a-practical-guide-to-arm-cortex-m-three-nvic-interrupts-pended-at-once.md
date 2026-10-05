---
id: "intr-a-practical-guide-to-arm-cortex-m-three-nvic-interrupts-pended-at-once"
type: "concept"
domain: "debug"
title: "A Practical guide to ARM Cortex-M Exception Handling: Code Examples / Three NVIC Interrupts Pended At Once"
summary: "For our final example, let's pend a couple exceptions at the same time so we can inspect hands on how the ARM core executes them in priority order."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-04-arm-cortex-m-exceptions-and-nvic.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#three-nvic-interrupts-pended-at-once"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Code Examples_

For our final example, let's pend a couple exceptions at the same time so we can inspect hands on
how the ARM core executes them in priority order.

Can you tell from the example code the order the breakpoints will be hit in?

```c
// External Interrupt 9
void TIMER1_IRQHandler(void) {
  __asm("bkpt 4");
}

// External Interrupt 10
void TIMER2_IRQHandler(void) {
  __asm("bkpt 5");
}

// External Interrupt 11
void RTC0_IRQHandler(void) {
  __asm("bkpt 6");
}

static void trigger_nvic_int9_int10_int11(void) {
  // Let's prioritize the interrupts with 9 having the lowest priority
  // and 10 & 11 having the same higher priority.

  // Each interrupt has 8 config bits allocated so
  // 4 interrupts can be configured per 32-bit register. This
  // means 9, 10, 11 are next to each other in IPR[2]
  volatile uint32_t *nvic_ipr2 = (void *)(0xE000E400 + 8);
  // Only 3 priority bits are implemented so we need to program
  // the upper 3 bits of each mask
  *nvic_ipr2 |= (0x7 << 5) << 8;
  *nvic_ipr2 |= (0x6 << 5) << 16;
  *nvic_ipr2 |= (0x6 << 5) << 24;

  // Enable interrupts for TIMER1_IRQHandler,
  // TIMER2_IRQHandler & RTC0_IRQHandler
  volatile uint32_t *nvic_iser = (void *)0xE000E100;
  *nvic_iser |= (0x1 << 9) | (0x1 << 10) | (0x1 << 11);

  // Pend an interrupt
  volatile uint32_t *nvic_ispr = (void *)0xE000E200;
  *nvic_ispr |= (0x1 << 9) | (0x1 << 10) | (0x1 << 11);

  // flush pipeline to ensure exception takes effect before we
  // return from this routine
  __asm("isb");
}
```

Let's call `trigger_nvic_int9_int10_int11()` and try it out!

```
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
TIMER2_IRQHandler () at ../../../main.c:81
81    __asm("bkpt 5");
(gdb)
```

So the external interrupt 10 (exception number 26) fired first. It has the same priority as NVIC Interrupt 11 but the ARM
core prioritizes higher [exception numbers](#exception-number) first which is why External Interrupt 10 is the first one that runs. We
would expect NVIC Interrupt 11 to run next.

Let's check and see what info is in the `ICSR` register this time:

```
(gdb) p/x *(uint32_t*)0xE000ED04
$9 = 0x41b81a
(gdb) p/d (*(uint32_t*)0xE000ED04)&0xff
$10 = 26
(gdb) p/d (*(uint32_t*)0xE000ED04)>>12&0x1
$11 = 1
(gdb) p/d (*(uint32_t*)0xE000ED04)>>12&0xff
$12 = 27
```

`VECTACTIVE` is 26 which matches what we expect. This time `VECTPENDING` is set too! The value is
27 which confirms that External Interrupt 11 (27-16) should be the next one to fire.

We can see all the NVIC interrupts that are pended by looking at the `NVIC_ISPR` register described
[above](#nvic-ispr). We should see bits
9 and 11 set since those interrupts haven't run yet

```
(gdb) p/x *(uint32_t[16] *)0xE000E200
$13 = {0xa00, 0x0 <repeats 15 times>}
```

Let's step through the rest of the code and confirm we see **bkpt 6** followed by **bkpt 4**:

```
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
RTC0_IRQHandler () at ../../../main.c:86
86    __asm("bkpt 6");
(gdb) next
main (a=<optimized out>, argv=<optimized out>) at ../../../main.c:127
127       bsp_board_led_invert(i);
(gdb) c
Continuing.

Program received signal SIGTRAP, Trace/breakpoint trap.
TIMER1_IRQHandler () at ../../../main.c:76
76    __asm("bkpt 4");
```
