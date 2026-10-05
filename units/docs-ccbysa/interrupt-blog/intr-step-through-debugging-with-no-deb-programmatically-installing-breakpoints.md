---
id: "intr-step-through-debugging-with-no-deb-programmatically-installing-breakpoints"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: A minimal DebugMonitor Handler / Programmatically installing Breakpoints with the FPB"
summary: "Part of: A minimal DebugMonitor Handler"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#programmatically-installing-breakpoints-with-the-fpb"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: A minimal DebugMonitor Handler_

In the FPB we can program one of the`FP_COMP` register to hold the address we would like to break
on.

The layout of the `FP_COMP` register is a little odd but basically for a given `instr_addr`, `FP_COMP[31:30]` map
`instr_addr[1:0]`, `FP_COMP[28:2]` map to `instr_addr[28:2]`, and the lowest bit `FP_COMP[0]` controls
whether the breakpoint is enabled or not.

For the NRF52, we can transcribe the logic into code as follows:

```c
bool fpb_set_breakpoint(size_t comp_id, uint32_t instr_addr) {
  if (instr_addr >= 0x20000000) {
    // for revision 1 only breakpoints in code can be installed :/
    return false;
  }
  // make sure the FPB is enabled
  FPB->FP_CTRL |= 0x3;

  const uint32_t replace = (instr_addr & 0x2) == 0 ? 1 : 2;
  const uint32_t fp_comp = (instr_addr & ~0x3) | 0x1 | (replace << 30);
  FPB->FP_COMP[comp_id] = fp_comp;
  return true;
}
```

> For more details on how to configure the Flash Patch And Breakpoint (**FPB**) unit,
> [check out our "How do breakpoints even work?" post](https://interrupt.memfault.com/blog/cortex-m-breakpoints#flash-patch--breakpoint-unit)!

To facilitate breakpoint testing, I've added `dummy_function_1` through `dummy_function_9` to my
program. All the functions do is print the name of the function being executed:

```c
void dummy_function_3(void) {
  EXAMPLE_LOG("stub function '%s' called", __func__);
}
```

We will be calling these functions to test out our debug monitor mode implementation.

I've also added a few CLI commands to the shell to help us configure the DebugMonitor exception
handler, enable breakpoints, and call the dummy functions:

```bash
shell> help
bkpt: Issue a Breakpoint Instruction
debug_mon_en: Enable Monitor Debug Mode
fpb_dump: Dump Active FPB Settings
fpb_set_breakpoint: Set Breakpoint [Comp Id] [Address]
call_dummy_funcs: Invoke dummy functions
dump_dummy_funcs: Print first instruction of each dummy function
help: Lists all commands
```

Let's try configuring a breakpoint for `dummy_function_4`, address `0x270`, and see what happens:

```bash
shell> dump_dummy_funcs
 ...
dummy_function_4: Starts at 0x270. First Instruction = 0x48024901
 ...
shell> debug_mon_en
Monitor Mode Debug Enabled!

shell> fpb_set_breakpoint 0 0x270
Set breakpoint on address 0x270 in FP_COMP[0] Succeeded

shell> fpb_dump
FPB Revision: 0, Enabled: 1, Hardware Breakpoints: 6
  FP_COMP[0] Enabled 1, Replace: 1, Address 0x270
  ...

shell> call_dummy_funcs
stub function 'dummy_function_1' called
stub function 'dummy_function_2' called
stub function 'dummy_function_3' called
DebugMonitor Exception
DEMCR: 0x01010000
DFSR:  0x00000002 (bkpt=1, halt=0, dwt=0)
Register Dump
 r0  =0x200031d8
 r1  =0x00000028
 r2  =0x00000001
 r3  =0x00000271
 r12 =0xffffffff
 lr  =0x000009ed
 pc  =0x00000270
 xpsr=0x010f0000
```

As expected we see our `DebugMon_Handler` has been invoked on address `pc =0x00000270` which
is where we installed the breakpoint!

#### Adding a CLI to the DebugMonitor Exception

To add a CLI for DebugMonitor handling, all we need is a way to read in bytes over a UART from a ISR. This
can be done by either polling the peripheral or by using an interrupt that is configured to run at
a higher priority than the DebugMonitor exception to do the reading.

In our example app, we will add two commands:

- `c` - To continue after the DebugMonitor exception fires
- `s` - To step one instruction and then return to the DebugMonitor Exception

#### C Code Additions for DebugMonitor CLI

```c
typedef enum {
  kDebugState_None,
  kDebugState_SingleStep,
} eDebugState;

static eDebugState s_user_requested_debug_state = kDebugState_None;

void debug_monitor_handler_c(sContextStateFrame *frame) {
  // ... logic to dump info ...

  if (is_dwt_dbg_evt || is_bkpt_dbg_evt ||
      (s_user_requested_debug_state == kDebugState_SingleStep))  {
    EXAMPLE_LOG("Debug Event Detected, Awaiting 'c' or 's'");
    while (1) {
      char c;
      if (!shell_port_getchar(&c)) {
        continue;
      }

      EXAMPLE_LOG("Got char '%c'!\n", c);
      if (c == 'c') {
        s_user_requested_debug_state = kDebugState_None;
        break;
      } else if (c == 's') {
        s_user_requested_debug_state = kDebugState_SingleStep;
        break;
      }
    }
  } else {
    EXAMPLE_LOG("Resuming ...");
  }

  // ... other logic ...
}
```
