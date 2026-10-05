---
id: "intr-faster-debugging-with-watchpoints-example-project-setup"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: Example Project Setup"
summary: "In the following sections, we will explore how watchpoints work by building on top of the bare-metal application running on a nRF52 that we used to investigate how breakpoints work and how to debug without a debugger."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#example-project-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the following sections, we will explore how watchpoints work by building on top of the bare-metal application running on a nRF52 that we used to investigate [how breakpoints work](https://interrupt.memfault.com/blog/cortex-m-breakpoints) and [how to debug without a debugger](https://interrupt.memfault.com/blog/cortex-m-debug-monitor).

We will make use of the following setup:

- a nRF52840-DK[^1] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^2] as our gdbserver (V6.84a)
- GCC 9.3.1 / GNU Arm Embedded Toolchain as our compiler[^3]
- GNU Make as our build system
- the simple CLI shell [we built up in a previous post](https://interrupt.memfault.com/blog/firmware-shell).
- PySerial's `miniterm.py`[^miniterm] to connect to the serial console on the nRF52.

### Compiling and Flashing Project

If you have an nRF52840-DK and would like to follow along:

#### Launch JLinkGDBServer

```bash
$ JLinkGDBServer  -if swd -device nRF52840_xxAA  -nogui
```

#### Clone, Compile & Flash

```bash
$ git clone https://github.com/memfault/interrupt.git
$ cd example/watchpoints

# Build
$ make
Compiling src/accel_fake.c
Compiling src/dummy_functions.c
Compiling src/dwt.c
Compiling src/graphics_fake.c
Compiling src/log_port.c
Compiling src/main.c
Compiling src/minimal_nrf52_uart.c
Compiling src/shell.c
Compiling src/shell_commands.c
Compiling src/shell_port.c
Compiling src/startup.c
Linking library
Generated build/nrf52.elf

# Flash & Debug
$ make flash
(gdb)
```

#### Open a Serial Connection to Shell

```bash
# Start Miniterm (Separate Terminal)
$ miniterm.py /dev/cu.usbmodem* 115200 --raw
--- Miniterm on /dev/cu.usbmodem0006838593731  115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---
==Booted==

shell>
```
