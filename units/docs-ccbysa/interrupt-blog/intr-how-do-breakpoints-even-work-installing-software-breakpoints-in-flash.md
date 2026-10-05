---
id: "intr-how-do-breakpoints-even-work-installing-software-breakpoints-in-flash"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Cortex-M Hardware Breakpoints / Installing Software Breakpoints in Flash"
summary: "Part of: Cortex-M Hardware Breakpoints"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#installing-software-breakpoints-in-flash"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M Hardware Breakpoints_

Now that we have used all of the available hardware breakpoints what happens if we try to add one for another flash-based function?

```
break dummy_function_7
Breakpoint 8 at 0x2a0: file dummy_functions.c, line 28.
(gdb) c
Continuing.
Sending packet: $Z0,240,2#aa...Packet received: OK
Sending packet: $Z0,250,2#ab...Packet received: OK
Sending packet: $Z0,260,2#ac...Packet received: OK
Sending packet: $Z0,270,2#ad...Packet received: OK
Sending packet: $Z0,280,2#ae...Packet received: OK
Sending packet: $Z0,290,2#af...Packet received: OK
Sending packet: $Z0,2a0,2#d7...Packet received: OK
Sending packet: $Z0,20000000,2#96...Packet received: OK
Sending packet: $c#63...
```

```
shell> fpb_dump
FPB Revision: 0, Enabled: 1, Hardware Breakpoints: 6
  FP_COMP[0] Enabled 1, Replace: 1, Address 0x250
  FP_COMP[1] Enabled 1, Replace: 1, Address 0x260
  FP_COMP[2] Enabled 1, Replace: 1, Address 0x270
  FP_COMP[3] Enabled 1, Replace: 1, Address 0x280
  FP_COMP[4] Enabled 1, Replace: 1, Address 0x290
  FP_COMP[5] Enabled 1, Replace: 1, Address 0x2a0
```

Interesting, it looks like the breakpoint for `dummy_function_1` (address 0x240) has been removed from `FP_COMP_0` and `dummy_function_2` through `dummy_function_7` have been configured as hardware breakpoints.

Let's call all the functions, using the `call_dummy_funcs` shell command and confirm we break at `dummy_function_1`..`dummy_function_7` as well as `dummy_function_ram`:

```bash
(gdb) c
Continuing.

Breakpoint 1, dummy_function_1 () at dummy_functions.c:4
4     EXAMPLE_LOG("stub function '%s' called", __func__);
(gdb) c
Continuing.

Breakpoint 3, dummy_function_2 () at dummy_functions.c:8
8     EXAMPLE_LOG("stub function '%s' called", __func__);
(gdb) c
Continuing.

[...]

Breakpoint 8, dummy_function_7 () at dummy_functions.c:28
28    EXAMPLE_LOG("stub function '%s' called", __func__);
(gdb) c
Continuing.

Breakpoint 2, dummy_function_ram () at dummy_functions.c:41
41    EXAMPLE_LOG("stub function '%s' called", __func__);
(gdb) c
```

Neat, they all worked so a breakpoint was installed for the flash-based function (`dummy_function_1`) that was missing from the FPB configuration.

Let's dump the functions information to examine if any instructions were modified:

```
shell> dump_dummy_funcs
dummy_function_1: Starts at 0x240. First Instruction = 0x4802be00
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

Woah, we can see `dummy_function_1` also was updated to include a breakpoint instruction, `0xbe00`. What's interesting here is this address is in the nRF52's internal flash space. This means to inject this breakpoint the flash page the address is in must have been reprogrammed.

This is in fact exactly what happened. The SEGGER JLinkGDBServer implements a feature referred to
in the docs as "unlimited flash breakpoints"[^11] which will patch flash regions the J-Link
Software knows how to write to with `bkpt` instructions. To support this feature, the JLink
software ships with flash drivers for all those chips since they are not standard across different
chip vendors.

#### Flash Software Breakpoint Optimizations

To minimize the number of times the flash sector has to be rewritten, the JLinkGDBServer will also
perform some nifty optimizations such as caching the flash sector and "simulating"
instruction execution rather than always removing/adding breakpoints on each halt like the `gdb`
client requests.

Let's walk through a quick example for our `dummy_function_1` where the `0x4901` instruction at
`0x240` has been replaced by the gdbserver with a breakpoint instruction.

```bash
$ arm-none-eabi-objdump  --disassemble=dummy_function_1  \
    example/breakpoint/build/nrf52.elf
[...]
00000240 <dummy_function_1>:
 240:	4901        ldr	r1, [pc, #4] ; (248 <dummy_function_1+0x8>)
 242:	4802        ldr	r0, [pc, #8] ; (24c <dummy_function_1+0xc>)
 244:	f000 b966   b.w	514 <example_log>
 248:	0000732f    .word	0x0000732f
 24c:	00007315    .word	0x00007315
```

As we discovered in this article, when we hit the breakpoint at `dummy_function_1`, the gdb client
will request that we uninstall all breakpoints. Then when we `continue`, the
`gdb` client will request a "single-step" over the instruction. In our example this means executing the instruction at
0x240 and halting again on the instruction fetch at `0x242`. At this time the `gdb` client will ask
the server to re-install all the breakpoints (including the one originally at `0x240`) and resume.

Instead, the JLinkGDBServer ignores the requests to remove/reinstall the breakpoint and when it
receives the "single-step" request, "simulates" the instruction and updates the registers
with the result directly from the debugger over the [Debug Access Port](https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#the-debug-access-port). For the
instruction in our example, this would involve updating `$r1` with the `.word` at `$pc+4` (`0x248`) and then
advancing the `$pc` by two bytes.

Using this technique the GDBServer rarely has to actually reprogram the flash sector reducing
flash write cycles and speeding up the average time it takes to "set" flash breakpoints.

> Note: Not many debuggers have this kind of sophisticated functionality. With a gdbserver like OpenOCD or pyOCD, the request to set a breakpoint in a flash region would just fail when you run out of available hardware breakpoints.

##### Consequences

One adverse side-effect of this approach is if you pull the power to your board and don't terminate
things gracefully, a breakpoint instruction could get stuck on your device until you reflash the
board. When no debugger is enabled, executing a breakpoint instruction will
[escalate to a HardFault](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#hardfault-status-register-hfsr---0xe000ed2c), so this could leave your firmware in a state where it would crash loop!

We can try this ourselves:

1. Pull USB power on the nRF52

2. Instead of reattaching GDB, just start a shell:

   ```
   $ miniterm.py /dev/cu.usbmodem* 115200 --raw
   shell>
   ```

3. Dump functions and confirm breakpoint instruction, `0xbe00`, is still installed.

   ```
   shell> dump_dummy_funcs
   dummy_function_1: Starts at 0x240. First Instruction = 0x4802be00
   [...]
   ```

4. Execute dummy functions and confirm this now causes a reboot!

   ```
   shell> call_dummy_funcs
   ==Booted==
   ```
