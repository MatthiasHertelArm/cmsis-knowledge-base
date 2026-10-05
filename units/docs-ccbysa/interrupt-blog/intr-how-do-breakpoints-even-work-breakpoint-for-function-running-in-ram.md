---
id: "intr-how-do-breakpoints-even-work-breakpoint-for-function-running-in-ram"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Cortex-M Hardware Breakpoints / Breakpoint for function Running in RAM"
summary: "Part of: Cortex-M Hardware Breakpoints"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#breakpoint-for-function-running-in-ram"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M Hardware Breakpoints_

Recall that Version 1 of the FPB only works on addresses in code space. Let's install a breakpoint for a function running in SRAM (Address `0x20000000-0x3FFFFFFF`) and see what happens:

```bash
(gdb) break dummy_function_ram
Sending packet: $m20000000,40#7f...Packet received: [...]
Sending packet: $m20000008,4#57...Packet received: c8730000
Sending packet: $m20000008,4#57...Packet received: c8730000
Sending packet: $m20000000,2#4d...Packet received: 0149
Breakpoint 2 at 0x20000000: file dummy_functions.c, line 41.
(gdb) c
Continuing.
==> Sending packet: $Z0,240,2#aa...Packet received: OK
==> Sending packet: $Z0,20000000,2#96...Packet received: OK
Sending packet: $c#63...
```

Cool, we can see GDB has requested breakpoints get installed at address `0x240` & `0x20000000`.

```
shell> fpb_dump
FPB Revision: 0, Enabled: 1, Hardware Breakpoints: 6
  FP_COMP[0] Enabled 1, Replace: 1, Address 0x240
  FP_COMP[1] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[2] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[3] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[4] Enabled 0, Replace: 0, Address 0x0
  FP_COMP[5] Enabled 0, Replace: 0, Address 0x0
```

We can see the breakpoint for `dummy_function_1` is still configured in the FPB but where is the one for the RAM function?!

The only way this could have worked is if the debugger was able to install a "software breakpoint". Let's take a look at the instructions:

```
shell> dump_dummy_funcs
dummy_function_1: Starts at 0x240. First Instruction = 0x48024901
dummy_function_2: Starts at 0x250. First Instruction = 0x48024901
dummy_function_3: Starts at 0x260. First Instruction = 0x48024901
dummy_function_4: Starts at 0x270. First Instruction = 0x48024901
dummy_function_5: Starts at 0x280. First Instruction = 0x48024901
dummy_function_6: Starts at 0x290. First Instruction = 0x48024901
dummy_function_7: Starts at 0x2a0. First Instruction = 0x48024901
dummy_function_8: Starts at 0x2b0. First Instruction = 0x48024901
dummy_function_9: Starts at 0x2c0. First Instruction = 0x48024901
dummy_function_ram: Starts at 0x20000000. First Instruction = 0x4802be00
```

You can see that the first instruction for `dummy_function_ram` has been modified by the debugger from `0x4901` to `0xbe00`.

The astute observer may realize right away this is the encoding for a breakpoint in thumb mode:

#### BKPT Instruction Encoding


