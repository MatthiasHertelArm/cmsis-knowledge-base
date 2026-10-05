---
id: "intr-profiling-firmware-on-cortex-m-decoding-itm-data"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M: PC Sampling with ITM / Decoding ITM Data"
summary: "If all went well, we now have a file named itm.fifo which contains binary ITM data. We must now decode it!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m#decoding-itm-data"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: PC Sampling with ITM_

If all went well, we now have a file named `itm.fifo` which contains binary ITM
data. We must now decode it!

The packet format is specified in detail in the [ARM v7m Architecture Reference
Manual](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf). Thankfully,
others have gone through the trouble of implementing decoders for us.

My favorite tool here is the `itm-tools` suite from Jorge Aparicio, which is
[available on Github](https://github.com/japaric/itm-tools). You will need a
relatively recent Rust toolchain to compile it.

In case you are not familiar with Rust, here are simple steps to run to get the
tools:

```shell
$ git clone https://github.com/japaric/itm-tools
...
$ cd itm-tools
$ cargo build
...
   Compiling addr2line v0.12.1
   Compiling backtrace v0.3.48
   Compiling synstructure v0.12.3
   Compiling failure v0.1.8
   Compiling exitfailure v0.5.1
   Compiling itm v0.4.0 (https://github.com/rust-embedded/itm#9298d128)
   Compiling itm-tools v0.1.0 (/Users/francois/code/itm-tools)
    Finished dev [unoptimized + debuginfo] target(s) in 50.20s
```

You will then find the `itm-decode` and `pcsampl` programs under `target/debug`.

First, we can use `itm-decode` to verify our ITM data contains the PC samples we
expect:

```shell
$ ~/code/itm-tools/target/debug/itm-decode itm.fifo 2>/dev/null
...
PeriodicPcSample { pc: Some(134219118) }
PeriodicPcSample { pc: Some(134219084) }
PeriodicPcSample { pc: Some(134219106) }
PeriodicPcSample { pc: Some(134219072) }
PeriodicPcSample { pc: Some(134219084) }
PeriodicPcSample { pc: Some(134219106) }
PeriodicPcSample { pc: Some(134219072) }
PeriodicPcSample { pc: Some(134219084) }
PeriodicPcSample { pc: Some(134219106) }
PeriodicPcSample { pc: Some(134219118) }
PeriodicPcSample { pc: Some(134219084) }
PeriodicPcSample { pc: Some(134219094) }
PeriodicPcSample { pc: Some(134219106) }
PeriodicPcSample { pc: Some(134219072) }
PeriodicPcSample { pc: Some(134219084) }
PeriodicPcSample { pc: Some(134219094) }
PeriodicPcSample { pc: Some(134219106) }
```

That looks great! Note that if you see too many `Overflow` packets your debug
adapter is not able to keep up with your sampling rate and you should increase
the POSTPRESET value in the DWT Control Register to lower the sampling rate.

Next, we can use the `pcsampl` utility to analyze the profiling data:

```shell
$ ~/code/itm-tools/target/debug/pcsampl itm.fifo -e mandel.elf 2>/dev/null
    % FUNCTION
 0.05 *SLEEP*
51.94 mandel
32.64 spi_xfer
 8.40 lcd_command
 4.63 lcd_draw_pixel
 2.17 msleep
 0.10 uart_putc
 0.02 _realloc_r
 0.01 rcc_clock_setup_pll
 0.01 sys_tick_handler
 0.00 __fputwc
 0.00 _fclose_r
 0.00 __sfvwrite_r
 0.00 gpio_mode_setup
 0.00 _dtoa_r
-----
 100% 23170 samples
```

As you can see, this data is much more detailed than what we got with the Poor
Man's Profiler approach. In fact, we can see that we are spending most of our
time in the `mandel` function, and not in the `spi_xfer` function as we
thought.

> Note: In the process of writing this blog post, I stumbled upon the [Orbuculum
> project](https://github.com/orbcode/orbuculum). While this looks very
> promising for ITM/ETM and other debugging, I was not able to get it to work on
> MacOS.
