---
id: "intr-step-through-debugging-with-no-deb-single-stepping-on-a-running-system"
type: "concept"
domain: "debug"
title: "Step-through debugging with no debugger on Cortex-M: A minimal DebugMonitor Handler / Single Stepping On a Running System"
summary: "Part of: A minimal DebugMonitor Handler"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-29-cortex-m-debug-monitor.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-debug-monitor#single-stepping-on-a-running-system"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: A minimal DebugMonitor Handler_

Now we can test out the single-step feature for `dummy_function_4`.

We can use `disassemble` in GDB to determine what we expect to see if things are working.

```
(gdb) disass dummy_function_4
Dump of assembler code for function dummy_function_4:
   0x00000270 <+0>:	ldr	r1, [pc, #4]	; (0x278 <dummy_function_4+8>)
   0x00000272 <+2>:	ldr	r0, [pc, #8]	; (0x27c <dummy_function_4+12>)
   0x00000274 <+4>:	b.w	0x6c0 <example_log>
   0x00000278 <+8>:	strb	r6, [r2, #21]
   0x0000027a <+10>:	movs	r0, r0
   0x0000027c <+12>:	strb	r1, [r1, #20]
   0x0000027e <+14>:	movs	r0, r0
End of assembler dump.
```

We will install a breakpoint at address `0x270`, so if we single step after that we should see, `0x272`,
`0x274` and then a branch to `0x6c0` executed by the processor.

```bash
shell> debug_mon_en
Monitor Mode Debug Enabled!

shell> fpb_set_breakpoint 0 0x270

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
 lr  =0x00000a05
 pc  =0x00000270
 xpsr=0x010d0000
Debug Event Detected, Awaiting 'c' or 's'
# Type 's'
Got char 's'!
 ...
 pc  =0x00000272
 ...
Debug Event Detected, Awaiting 'c' or 's'
# Type 's'
Got char 's'!
 ...
 pc  =0x00000274
 ...
Debug Event Detected, Awaiting 'c' or 's'
# Type 's'
Got char 's'!
 ...
 pc  =0x000006c0
 ...
Debug Event Detected, Awaiting 'c' or 's'
# Resume flow 'c' and we should see the
# rest of the functions get called!
Got char 'c'!

stub function 'dummy_function_4' called
stub function 'dummy_function_5' called
stub function 'dummy_function_6' called
stub function 'dummy_function_7' called
stub function 'dummy_function_8' called
stub function 'dummy_function_9' called
stub function 'dummy_function_ram' called
```

Nice, it works!

> At this point, to make the DebugMonitor CLI interface more useful, we could extend the shell to
> dump the contents of the stack or other memory regions.
