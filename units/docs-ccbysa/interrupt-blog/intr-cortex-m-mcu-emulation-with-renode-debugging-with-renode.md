---
id: "intr-cortex-m-mcu-emulation-with-renode-debugging-with-renode"
type: "concept"
domain: "debug"
title: "Cortex-M MCU Emulation with Renode: Debugging with Renode"
summary: "Inevitably things will go wrong and you will need to debug them. This is one area where Renode really shines."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-23-intro-to-renode.md"
doc_source: "https://interrupt.memfault.com/blog/intro-to-renode#debugging-with-renode"
license: "CC-BY-SA-4.0"
mode: "V"
---

Inevitably things will go wrong and you will need to debug them. This is one
area where Renode really shines.

### Tracing Function Calls

One of the advantages of emulators is that they make it much easier to
introspect and trace the device state. One of the more useful hooks exposed by
Renode is execution tracing. Provided you fed the emulator an ELF file with
debug symbols, Renode will print out log out every function being executed.

Going back to our hello world example, we can enable function tracing with a
single command:

```
(machine-0) sysbus.cpu LogFunctionNames True
(machine-0)
```

You will likely want to write the output to a file rather than stdout, you can
do this with a single command as well:

```
(machine-0) logFile @/tmp/function-trace.log
(machine-0)
```

Once we've started our emulation, we can retrieve the file and inspect it:

```
[...]
23:12:16 [INFO] cpu: Entering function _write at 0x80001D8¬
23:12:16 [INFO] cpu: Entering function usart_send_blocking (entry) at 0x80003B4¬
23:12:16 [INFO] cpu: Entering function usart_wait_send_ready (entry) at 0x80003D2¬
23:12:16 [INFO] cpu: Entering function usart_wait_send_ready at 0x80003D8¬
23:12:16 [INFO] cpu: Entering function usart_send_blocking at 0x80003BE¬
23:12:16 [INFO] cpu: Entering function usart_send (entry) at 0x80003CA¬
23:12:16 [INFO] cpu: Entering function _write at 0x80001E2¬
23:12:16 [INFO] cpu: Entering function _write at 0x80001BE¬
23:12:16 [INFO] cpu: Entering function _write at 0x80001CA¬
23:12:16 [INFO] cpu: Entering function _write at 0x80001D0¬
23:12:16 [INFO] cpu: Entering function usart_send_blocking (entry) at 0x80003B4¬
23:12:16 [INFO] cpu: Entering function usart_wait_send_ready (entry) at 0x80003D2¬
23:12:16 [INFO] cpu: Entering function usart_wait_send_ready at 0x80003D8¬
23:12:16 [INFO] cpu: Entering function usart_send_blocking at 0x80003BE¬
23:12:16 [INFO] cpu: Entering function usart_send (entry) at 0x80003CA¬
23:12:16 [INFO] cpu: Entering function _write at 0x80001D8¬
23:12:16 [INFO] cpu: Entering function usart_send_blocking (entry) at 0x80003B4¬
[...]
```

### GDB Integration

When it comes to debugging, GDB is my go to tool. I was pleasantly surprised to
learn that Renode will spin up a GDB server for you out of the box. This is
extremely easy to use.

First, we enable the GDB server and bind it to port 3333:

```
(machine-0) machine StartGdbServer 3333
(machine-0)
```

> Note: For the example config we have added this to renode-config.resc so it happens automatically
> when spinning up the environment

In a separate terminal window, we start GDB and connect to the server on port 3333.

```
$ arm-none-eabi-gdb renode-example.elf
GNU gdb (GNU Tools for Arm Embedded Processors 8-2018-q4-major)
8.2.50.20181213-git
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "--host=x86_64-apple-darwin10
--target=arm-none-eabi".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from renode-example.elf...

(gdb) target remote :3333
Remote debugging using :3333
0x00000000 in ?? ()
```

We can then issue monitor commands to renode via the `monitor` gdb command, and
debug as we would a real target

```
(gdb) break main
Breakpoint 1 at 0x80001f8: file renode-example.c, line 62.
(gdb) monitor start
Starting emulation...
(gdb) c
Continuing.

Breakpoint 1, main () at renode-example.c:62
62              clock_setup();
(gdb) step
rcc_periph_clock_enable (clken=clken@entry=RCC_GPIOD) at
../common/rcc_common_all.c:136
136             _RCC_REG(clken) |= _RCC_BIT(clken);
(gdb) n
clock_setup () at renode-example.c:12
12              rcc_periph_clock_enable(RCC_GPIOA);
(gdb) n
15              rcc_periph_clock_enable(RCC_USART2);
(gdb)
```
