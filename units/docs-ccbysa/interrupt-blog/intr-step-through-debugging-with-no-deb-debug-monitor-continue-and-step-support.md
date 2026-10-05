---
id: "intr-step-through-debugging-with-no-deb-debug-monitor-continue-and-step-support"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: A minimal DebugMonitor Handler / Debug Monitor Continue and Step Support"
summary: "Part of: A minimal DebugMonitor Handler"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#debug-monitor-continue-and-step-support"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: A minimal DebugMonitor Handler_

Stepping over a breakpoint is a several step process:

1. If it's a `bkpt` instruction, we need to advance the program counter by the size of the instruction (2
   bytes).
2. If a `bkpt` event was generated from a breakpoint configured in the FPB, we need to:
   - Disable the FPB. Otherwise, any attempt to continue will just hit the breakpoint again.
   - Single-Step one instruction.
   - Re-enable the FPB and disable single-stepping in order to resume program execution.

In our `DebugMon_Handler`, we can:

- inspect the `pc` from the `frame` parameter passed to `debug_monitor_handler_c` to figure out
  whether or not the debug event was caused by executing a breakpoint instruction.
- Disable/Enable the FPB by clearing & setting the `ENABLE` bit in the FPB `FP_CTRL` register.
- Enable/Disable single-step functionality by setting and clearing the `MON_STEP` bit in the `DEMCR`.

#### C Code Additions for DebugMonitor Breakpoint & Single-Step Handling

Let's implement the logic described above in code:

```c
  const uint32_t demcr_single_step_mask = (1 << 18);

  if (is_bkpt_dbg_evt) {
    const uint16_t instruction = *(uint16_t*)frame->return_address;
    if ((instruction & 0xff00) == 0xbe00) {
      // advance past breakpoint instruction
      frame->return_address += sizeof(instruction);
    } else {
      // It's a FPB generated breakpoint
      // We need to disable the FPB and single-step
      fpb_disable();
      EXAMPLE_LOG("Single-Stepping over FPB at 0x%x", frame->return_address);
    }

    // single-step to the next instruction
    // This will cause a DebugMonitor interrupt to fire
    // once we return from the exception and a single
    // instruction has been executed. The HALTED bit
    // will be set in the DFSR when this happens.
    *demcr |= (demcr_single_step_mask);
    // We have serviced the breakpoint event so clear mask
    *dfsr = dfsr_bkpt_evt_bitmask;
  } else if (is_halt_dbg_evt) {
    // re-enable FPB in case we got here via single-step
    // for a BKPT debug event
    fpb_enable();

    if (s_debug_state != kDebugState_SingleStep) {
      *demcr &= ~(demcr_single_step_mask);
    }

    // We have serviced the single step event so clear mask
    *dfsr = dfsr_halt_evt_bitmask;
  }
```
