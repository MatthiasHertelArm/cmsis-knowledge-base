---
id: "intr-profiling-firmware-on-cortex-m-enabling-pc-sampling-with-itm-and-openoc"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M: PC Sampling with ITM / Enabling PC Sampling with ITM and OpenOCD"
summary: "You will notice that \"PC Sampling\" is explicitly called out as one of the things we can do with ITM. With ITM PC Sampling, we can build a much better Sampling Profiler!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m#enabling-pc-sampling-with-itm-and-openocd"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: PC Sampling with ITM_

You will notice that "PC Sampling" is explicitly called out as one of the things
we can do with ITM. With ITM PC Sampling, we can build a much better Sampling
Profiler!

#### Configuring OpenOCD

First, we must configure OpenOCD to read from the SWO pin and dump the data
somewhere we can read it. This is done via the `tpiu config`
command[^tpiu_config]. This command configures the Trace Port Interface
Unit[^tpiu] in the chip and enables saving to file in openOCD. I've summarized
it below:

```
tpiu config (disable | ((external | internal (filename | -)) (sync port_width | ((manchester | uart) formatter_enable)) TRACECLKIN_freq [trace_freq]))
```

Here is what we want to do here:
1. Set TRACELCKIN_FREQ to our core frequency (168MHz for the STM32F429). This is
   important as you will get corrupted data on your SWO pin otherwise.
2. Redirect the ITM data to a file with `internal <filename>`. Using `external`
   would require we use an adapter to read the data directly from the pin with
e.g. a UART to USB adapter
3. Use UART rather than Manchester encoding to make it easy to decode the data

From GDB, we use `monitor` to send commands to OpenOCD, so we get the following command:
```
(gdb) monitor tpiu config internal itm.fifo uart off 168000000
```

#### Enabling PC Sampling Events

Next, we configure our MCU to output PC Sampling events. This is done using the
DWT Control Register. The register is at address `0xE0001000`, I've reproduced
its layout below:



For our use case, we care about the following bits:
- Bit 12: PCSAMPLEENA. Setting this to 1 will enable PC sampling events.
- Bit 0: CYCCNTENA. This enables the CYCCNT counter which is required for PC
  sampling.
- Bit 9: CYCTAP. This selects which bit in the cycle counter is used to trigger
  PC sampling events. A 1 selects bit 10 to tap, a 0 selects bit 6 to tap.
- Bits 1-4: POSTPRESET. These bits control how many times the time bit must
  toggle before a PC sample event is generated.

Let me explain how the system works: CYCCNTENA enables a cycle counter in the
DWT unit of your microcontroller. This counter is incremented every CPU cycle
(i.e. 168 million times per second). Whenever the CYCTAP bit in the cycle
counter is toggled (0->1 or 1->0), we decrement a counter which started at the
POSTPRESET value. When that counter hits 0, a PC sampling event is generated.

Here's a practical example: if CYCTAP is set to 0 and POSTPRESET is set to 4, we
tap the 6th bit of the cycle counter. This means that the tap is toggled every
64 (or 2^6) cycles. After 4 tap toggles, a PC sample event is generated which
works out to 256 (4 * 64) cycles. In other words, the PC sampling rate is 0.65MHz
(168MHz / 256).

We are limited by the speed of our debug adapter, so in my case, I tapped the
10th bit (CYCTAP = 1), and set POPRESET to 3. This means that we are
sampling the PC every 3,072 cycles, or at 50KHz.

Using OpenOCD, we write the register so that PCSAMPLEENA = 1, CYCCNTENA = 1,
CYCTAP = 1, and POSTPRESET = 3. This requires the following command:

```
(gdb) monitor mww 0xE0001000 0x1207 0x103FF
```

Last but not least, we enable ITM port 0 which is a built in openOCD feature:

```
(gdb) monitor itm port 0 on
```
