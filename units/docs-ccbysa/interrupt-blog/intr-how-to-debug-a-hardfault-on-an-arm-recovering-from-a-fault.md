---
id: "intr-how-to-debug-a-hardfault-on-an-arm-recovering-from-a-fault"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Recovering From A Fault"
summary: "Occasionally, you may want to recover the system from a fault without rebooting it. For example, maybe you have one RTOS task isolated by the MPU that just needs to be restarted."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#recovering-from-a-fault"
license: "CC-BY-SA-4.0"
mode: "V"
---

> DISCLAIMER: Typically when a fault occurs, the best thing to do is reset the MCU since it's hard to be certain what parts of the MCU were corrupted as part of the fault (embedded MCUs don't offer a MMU like you would find on a bigger processors).

Occasionally, you may want to recover the system from a fault without rebooting it. For example, maybe you have one RTOS task isolated by the MPU that just needs to be restarted.

Let's quickly explore how we could implement a recovery mechanism that puts a RTOS task which experience a UsageFault into an idle loop and reboots the system otherwise.

We will use the
[Application Interrupt and Reset Control Register](https://interrupt.memfault.com/blog/arm-cortex-m-exceptions-and-nvic#application-interrupt-and-reset-control-register-aircr---0xe000ed0c) to reset the device if the fault is unrecoverable. We can easily extend `my_fault_handler_c` from [above](#my-fault-handler-c):

```c
void my_fault_handler_c(sContextStateFrame *frame) {
[...]
  volatile uint32_t *cfsr = (volatile uint32_t *)0xE000ED28;
  const uint32_t usage_fault_mask = 0xffff0000;
  const bool non_usage_fault_occurred =
      (*cfsr & ~usage_fault_mask) != 0;
  // the bottom 8 bits of the xpsr hold the exception number of the
  // executing exception or 0 if the processor is in Thread mode
  const bool faulted_from_exception = ((frame->xpsr & 0xFF) != 0);

  if (faulted_from_exception || non_usage_fault_occurred) {
    // For any fault within an ISR or non-usage faults
    // let's reboot the system
    volatile uint32_t *aircr = (volatile uint32_t *)0xE000ED0C;
    *aircr = (0x05FA << 16) | 0x1 << 2;
    while (1) { } // should be unreachable
  }
[...]
}
```

Now, the interesting part, how do we clean up our state and return to normal code from the HardFault handler?!

There's a few things we will need to do:

- Clear any logged faults from the `CFSR` by writing 1 to each bit which is set.
- Change the function we return to so we idle the task. In the example case it's `recover_from_task_fault`.
- Scribble a known pattern over the `lr`. The function we are returning to will need to take special action (i.e like deleting the task or entering a `while(1)` loop). It can't just exit and branch to where we were before so we _want_ to fault if this is attempted.
- Reset the `xpsr`. Among other things the xpsr tracks the state of previous comparison instructions which were run and whether or not we are in the middle of a "If-Then" instruction block. The only bit that needs to remain set is the "T" field (bit 24) indicating the processor is in thumb mode[^15].

This winds up looking like:

```c
  // Clear any logged faults from the CFSR
  *cfsr |= *cfsr;
  // the instruction we will return to when we exit from the exception
  frame->return_address = (uint32_t)recover_from_task_fault;
  // the function we are returning to should never branch
  // so set lr to a pattern that would fault if it did
  frame->lr = 0xdeadbeef;
  // reset the psr state and only leave the
  // "thumb instruction interworking" bit set
  frame->xpsr = (1 << 24);
```

You may recall from the
[RTOS Context Switching post](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#context-state-stacking)
that fault handlers can work just like regular C functions so after these changes we will exit from
`my_fault_handler_c` and start executing whatever is in `recover_from_task_fault` function. We will walk through an example of this [below](#usage-fault-recovery-example).
