---
id: "intr-how-do-breakpoints-even-work-using-all-the-hardware-breakpoints"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Cortex-M Hardware Breakpoints / Using all the Hardware Breakpoints"
summary: "Part of: Cortex-M Hardware Breakpoints"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#using-all-the-hardware-breakpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Cortex-M Hardware Breakpoints_

Let's halt and install 5 more breakpoints, exhausting our 6 available hardware breakpoints, and see what happens!

```bash
(gdb) break dummy_function_2
Breakpoint 2 at 0x250: file dummy_functions.c, line 8.
(gdb) break dummy_function_3
Breakpoint 3 at 0x260: file dummy_functions.c, line 12.
(gdb) break dummy_function_4
Breakpoint 4 at 0x270: file dummy_functions.c, line 16.
(gdb) break dummy_function_5
Breakpoint 5 at 0x280: file dummy_functions.c, line 20.
(gdb) break dummy_function_6
Breakpoint 6 at 0x290: file dummy_functions.c, line 24.
(gdb) c
Continuing.
Sending packet: $Z0,240,2#aa...Packet received: OK
Sending packet: $Z0,250,2#ab...Packet received: OK
Sending packet: $Z0,260,2#ac...Packet received: OK
Sending packet: $Z0,270,2#ad...Packet received: OK
Sending packet: $Z0,280,2#ae...Packet received: OK
Sending packet: $Z0,290,2#af...Packet received: OK
Sending packet: $Z0,20000000,2#96...Packet received: OK
Sending packet: $c#63...
```

As expected, we see requests to install breakpoints on all the locations we specified. We can dump the `fpb` config from the CLI and confirm:

```
shell> fpb_dump
FPB Revision: 0, Enabled: 1, Hardware Breakpoints: 6
  FP_COMP[0] Enabled 1, Replace: 1, Address 0x240
  FP_COMP[1] Enabled 1, Replace: 1, Address 0x250
  FP_COMP[2] Enabled 1, Replace: 1, Address 0x260
  FP_COMP[3] Enabled 1, Replace: 1, Address 0x270
  FP_COMP[4] Enabled 1, Replace: 1, Address 0x280
  FP_COMP[5] Enabled 1, Replace: 1, Address 0x290
```
