---
id: "intr-step-through-debugging-with-no-deb-debug-fault-status-register-dfsr-0xe000e"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: A minimal DebugMonitor Handler / Debug Fault Status Register, DFSR, 0xE000ED30"
summary: "Part of: A minimal DebugMonitor Handler"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#debug-fault-status-register-dfsr-0xe000ed30"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: A minimal DebugMonitor Handler_

When the DebugMonitor Exception fires, the DFSR can be inspected for information about what debug
event took place:



Some of the events are only possible when using a **halting debug**. For the DebugMonitor the
states of interest are:

- `DWTTRAP` Indicates the a debug event was generated due to a configuration in the DWT.
- `BKPT` Indicates one or more breakpoint event took place (either via the FPB or a BKPT instruction).
- `HALTED` Indicates the core was halted due to a MON_STEP request.

> NOTE: DFSR bits are sticky and you have to write 1 to the value to clear them

#### Example C Code For DebugMon_Handler

Let's extend `debug_monitor_handler_c` to dump some of the state we are collecting:

```c
void debug_monitor_handler_c(sContextStateFrame *frame) {
  volatile uint32_t *demcr = (uint32_t *)0xE000EDFC;

  volatile uint32_t *dfsr = (uint32_t *)0xE000ED30;
  const uint32_t dfsr_dwt_evt_bitmask = (1 << 2);
  const uint32_t dfsr_bkpt_evt_bitmask = (1 << 1);
  const uint32_t dfsr_halt_evt_bitmask = (1 << 0);
  const bool is_dwt_dbg_evt = (*dfsr & dfsr_dwt_evt_bitmask);
  const bool is_bkpt_dbg_evt = (*dfsr & dfsr_bkpt_evt_bitmask);
  const bool is_halt_dbg_evt = (*dfsr & dfsr_halt_evt_bitmask);

  EXAMPLE_LOG("DebugMonitor Exception");

  EXAMPLE_LOG("DEMCR: 0x%08x", *demcr);
  EXAMPLE_LOG("DFSR:  0x%08x (bkpt=%d, halt=%d, dwt=%d)", *dfsr,
              (int)is_bkpt_dbg_evt, (int)is_halt_dbg_evt,
              (int)is_dwt_dbg_evt);

  EXAMPLE_LOG("Register Dump");
  EXAMPLE_LOG(" r0  =0x%08x", frame->r0);
  EXAMPLE_LOG(" r1  =0x%08x", frame->r1);
  EXAMPLE_LOG(" r2  =0x%08x", frame->r2);
  EXAMPLE_LOG(" r3  =0x%08x", frame->r3);
  EXAMPLE_LOG(" r12 =0x%08x", frame->r12);
  EXAMPLE_LOG(" lr  =0x%08x", frame->lr);
  EXAMPLE_LOG(" pc  =0x%08x", frame->return_address);
  EXAMPLE_LOG(" xpsr=0x%08x", frame->xpsr);

  // ...
}
```

#### Triggering a breakpoint

To test things out we can create a super simple CLI command that issues a breakpoint instruction:

```c
static int prv_issue_breakpoint(int argc, char *argv[]) {
  __asm("bkpt 1");
  return 0;
}
```

In one terminal you will need to start a gdbserver:

```bash
$ JLinkGDBServer  -if swd -device nRF52840_xxAA  -nogui
```

Then you need to compile the example application and flash it

```bash
$ cd ${INTERRUPT_REPO}/example/debugmon/
$ make
Compiling src/debug_monitor_exception.c
[...]
Linking library
Generated build/nrf52.elf
$ arm-none-eabi-gdb-py --eval-command="target remote localhost:2331"  --ex="mon reset" --ex="load"
--ex="mon reset"  --se=build/nrf52.elf
(gdb)
```

From GDB. we will disable halting debug so the program will continue running:

```
(gdb) set *(uint32_t*)0xE000EDF0=(0xA05F<<16)
```

In a final terminal we will open a serial connection using miniterm:

```bash
$ miniterm.py - 115200 --raw
--- Available ports:
...
---  4: /dev/cu.usbmodem0006838593731 'J-Link'
--- Enter port index or full name: 4
--- Miniterm on /dev/cu.usbmodem0006838593731  115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
shell> debug_mon_en
Monitor Mode Debug Enabled!
shell> bkpt
DebugMonitor Exception
DEMCR: 0x01010000
DFSR:  0x00000002 (bkpt=1, halt=0, dwt=0)
Register Dump
 r0  =0x00000001
 r1  =0x20003310
 r2  =0x73734900
 r3  =0x000009d5
 r12 =0xffffffff
 lr  =0x0000094b
 pc  =0x000009d4
 xpsr=0x210e0000
 ...
```

As expected we see bit 1 in `DFSR` is set indicating a breakpoint debug event was generated.
We can use GDB to inspect the instruction located at`0x000009d4` and confirm it is indeed a breakpoint
instruction:

```
(gdb) x/i 0x000009d4
  0x9d4 <prv_issue_breakpoint>:	bkpt	0x0001
```

We can also dump the instruction and confirm it matches the BKPT instruction encoding (`0xbe..`):



```
(gdb) p/x *(uint16_t*)0x000009d4
$4 = 0xbe01
```
