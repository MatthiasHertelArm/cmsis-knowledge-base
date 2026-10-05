---
id: "intr-exploring-printf-on-cortex-m-redirecting-stdio"
type: "concept"
domain: "debug"
title: "Exploring printf on Cortex-M: Redirecting stdio"
summary: "This section describes a few approaches for redirecting libc standard input/output functions, and compares the tradeoffs each one makes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-20-printf-on-embedded.md"
doc_source: "https://interrupt.memfault.com/blog/printf-on-embedded#redirecting-stdio"
license: "CC-BY-SA-4.0"
mode: "V"
---

This section describes a few approaches for redirecting libc standard
input/output functions, and compares the tradeoffs each one makes.

| Method      | Advantages                                                                              | Disadvantages                                                                              |
| ----------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| UART        | - simple, no special host HW needed                                                     | - requires spare UART + pins on target
- can be slow                                   |
| Semihosting | - no extra HW requirements on target                                                    | - requires a debug probe for the host to use
- _prohibitively_ slow, interrupts target |
| SWO         | - requires only a single (often specific) spare pin on the target
- relatively fast | - usually needs a debug probe for the host to use
- output only                        |
| RTT         | - no extra HW requirements on target
- relatively fast                               | - requires a debug probe for the host to use
- license may be problematic              |

### UART

UART: asynchronous serial. Most embedded microcontrollers will have at least
one.

Pros:

- simple and widely available protocol (lots of available software and hardware
  tools interface to it)
- doesn't require an attached debugger; you can use it in PROD 😀

Cons:

- requires extra hardware to interface to the PC host, typically (USB to
  asynchronous serial adapter, like the FTDI or CP2102 adapters)
- requires configuring and using the UART peripheral (if your microcontroller
  doesn't have many UARTs, might be a problem using it for `printf`)

The biggest downside is you're spending one of your UART peripherals for printf,
which might be needed for your actual application.

Also, configuring a UART might require managing clock configuration, chip
power/sleep modes, figuring out buffering the data (DMA?), making sure
everything is interrupt safe, etc.

And finally, you'll usually need some kind of adapter dongle to interface the
UART with your PC (eg USB-to-TTL or USB-to-asynchronous serial).

Because the interface is contained entirely on the microcontroller, it can be
used without a debug probe, which can make it useful when not actively debugging
your system (eg you can use it to write log statements to an attached PC!).

Worth noting, if your microcontroller has support for USB, you might be able to
skip the need for an external FTDI-like adapter by implementing CDC
(Communications Device Class) on-chip. That adds a lot more software to your
system, but can be useful. Out of scope of this FAQ.

### Semihosting

Next up the food chain, semihosting is a protocol that proxies the "hosting"
(meaning libc hosting, eg `printf`/`scanf`/`open`/`close` etc) over an attached
debug probe to the PC.

Some good descriptions:

- <https://wiki.segger.com/Semihosting>
- <https://developer.arm.com/documentation/dui0375/g/What-is-Semihosting-/What-is-semihosting->

And the reference documentation can be found in:

> ARM Developer Suite (ADS) v1.2 Debug Target Guide, Chapter 5. Semihosting

This describes the detailed "RDIMON" ("Remote Debug Interface Monitor")
operation.

TLDR, semihosting operates by the target executing the breakpoint instruction
with a special breakpoint id, `bkpt 0xab`, with the I/O opcode stored in `r1`
and whatever necessary data stored in a pointer loaded into `r2`.

The debug probe executes the I/O operation based on the opcode and data, then
resumes the microcontroller.

To use it, the simplest approach is to use newlib's rdimon library spec:

```bash
# add these to your linker command line
LDFLAGS += --specs=nano.specs --specs=rdimon.specs
```

Then add this call somewhere in your system init, prior to calling any libc I/O
functions:

```c
// this executes some exchanges with the debug monitor to set up the correct
// file handles for stdout, stderr, and stdin
extern void initialise_monitor_handles(void);
initialise_monitor_handles();
```

`printf` and friends should work after that! Be sure to check the user manual
for your debug probe on how it exposes the semihosting interface. For example,
segger jlink requires running some commands to enable semihosting:

```bash
# from gdb client
monitor semihosting enable
monitor semihosting ioclient 2
```

(From <https://wiki.segger.com/J-Link_GDB_Server>).

For pyocd, you can pass the `--semihosting` argument when starting the gdb
server.

As an extra bonus, see below for a simplified semihosting solution based on the
newlib one that doesn't require linking against `rdimon.specs`, and saves some
code space. Note that some debug probes require the setup steps run by
[`initialise_monitor_handles()`](https://github.com/bminor/newlib/blob/1a0908203606527b6ac0ed438669b5bcd247a5f9/newlib/libc/sys/arm/syscalls.c#L114-L169),
so those may need to be included as well (depending on your setup).

```c
// Based on the implementation here:
// https://github.com/bminor/newlib/blob/1a0908203606527b6ac0ed438669b5bcd247a5f9/newlib/libc/sys/arm/syscalls.c#L314-L338
// And here:
// https://github.com/bminor/newlib/blob/69f4c4029183fb26d2fcae00790881620c1978a3/newlib/libc/sys/arm/swi.h#L74-L89
int _write(int file, uint8_t *ptr, int len) {
  int data[3] = {file, (int) ptr, len};
  __asm__("mov r0, %0 \n mov r1, %1 \n bkpt #0xAB"
          : : "r" (5), "r" (&data) : "r0", "r1", "memory");
  return len;
}
```

Pros:

- only requires SWD connection (SWCLK + SWDIO)
- built into most debug servers (pyocd, openocd, blackmagic, segger jlink)
- basic implementation is provided by newlib (no extra user code) and is dead
  simple to use
- can do lots more than just printf; open, fwrite, read from stdin!

Cons:

- slowwww. really slow. tens to hundreds of milliseconds per transfer, depending
  on debug probe and host
- doesn't work when debugger is disconnected (target will be stuck on `bkpt`
  instruction; either a forever hang or a crash depending on cortex-m
  architecture set). this can worked around by handling the `DebugMon` exception
  on-chip, or by checking the DHCSR register[^1] `C_DEBUGEN` bit, to detect if a
  debugger is connected.
- the newlib implementation (`--specs=rdimon.specs`) consumes about 1.5-2kB of
  flash

### Serial Wire Output (SWO)

A dedicated pin that can be used essentially as a UART for outputting data. It
can be pretty fast- baud rate sometimes reaching 1/1 of CPU core clock, since it
uses the TPIU.

It is however an optional hardware feature, so might not be available on every
chip (most common chips like STM32's and nRF chips tend to include it), and
requires an extra pin- typically routed to the 10-pin ARM debug header.

It's output only, and there's a small bit of code necessary on the target to
enable routing `printf` to SWO.

A good tutorial, including background information and an example implementation,
can be found here:

<https://mcuoneclipse.com/2016/10/17/tutorial-using-single-wire-output-swo-with-arm-cortex-m-and-eclipse/>

The debug adapter and software does need to support the protocol. Most debug
adapters do support it, however (ST-Link's, JLINK, DAPLink, etc).

Pros:

- generally pretty fast, similar performance to UART (speed is both target and
  probe hardware dependent)
- simple implementation

Cons:

- output only
- uses a pin on the target
- not all chips or probes support it

### Real Time Transfer (RTT)

<https://wiki.segger.com/RTT>

Segger's RTT reads/writes into a buffer in RAM while the chip is running. It can
be pretty fast compared to even a fast UART, and is _much_ more efficient than
Semihosting without requiring any extra pins or hardware.

It also supports both output (target -> host) and input (host -> target).

Segger provides the RTT target implementation, as well as a few tools for using
RTT on the host. OpenOCD and PyOCD also support the protocol.

You can download the implementation here:

<https://www.segger.com/products/debug-probes/j-link/technology/about-real-time-transfer/#downloading-rtt-target-package>

Zephyr also maintains a copy here, if you're curious about perusing it (or want
to use it as a git submodule):

<https://github.com/zephyrproject-rtos/segger/tree/master/SEGGER>

The downside is it requires a debug adapter to operate, since it relies on
reading and writing to memory.

It's also important to understand the implications of enabling this in
production; be sure your device doesn't get into a bad state if there's no debug
adapter connected (i.e. when no debugger is attached, drop data instead of
backing up the RTT buffers).

I'm personally a big fan of RTT over semihosting- it's usually going to be a
strict improvement if you don't need file I/O.

Pros:

- fast!
- simple on-device implementation
- supported out of the box on Zephyr RTOS, among other platforms

Cons:

- requires a debugger with support for RTT
