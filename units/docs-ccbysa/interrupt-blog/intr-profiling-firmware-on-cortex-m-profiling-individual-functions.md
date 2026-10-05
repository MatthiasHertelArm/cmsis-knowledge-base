---
id: "intr-profiling-firmware-on-cortex-m-profiling-individual-functions"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M: PC Sampling with ITM / Profiling Individual Functions"
summary: "So far, we have been profiling our entire program. This is useful to identify overall bottlenecks, but oftentimes we are concerned only with a specific code path."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m#profiling-individual-functions"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: PC Sampling with ITM_

So far, we have been profiling our entire program. This is useful to identify
overall bottlenecks, but oftentimes we are concerned only with a specific code
path. For example, we may want to profile a specific message parser, or an
interrupt service routine.

To do this, we will need to modify our firmware code a bit. Our goal is to write
a `PROFILE` macro which can be used to enable ITM profiling for a specific set
of code.

In our Mandelbrot example, let's profile `lcd_show_frame`. We want our macro to
be invoked as such:

```c
int main(void) {
    ...
    PROFILE(lcd_show_frame());
    ...
}
```

What does our macro need to do? At a high level:
1. Enable PC sampling
2. Execute the code being profiled
3. Disable PC sampling

We can start filling in our macro:

```c
#define PROFILE(code) {         \
  // enable PC sampling         \
  code;                          \
  // disable PC sampling        \
}
```

To enable or disable PC sampling, we need to write to the DWT Control Register.
Thankfully, libopencm3 has a definition for this register[^libopencm3-dwt] and its fields which
makes our life easy.

To enable PC sampling:
```c
DWT_CTRL &= ~DWT_CTRL_POSTPRESET;
DWT_CTRL |= 0x3 << DWT_CTRL_POSTPRESET_SHIFT;
DWT_CTRL |= DWT_CTRL_CYCTAP;
DWT_CTRL |= DWT_CTRL_PCSAMPLENA;
```

and to disable it:

```c
DWT_CTRL &= ~DWT_CTRL_POSTPRESET;
DWT_CTRL &= ~DWT_CTRL_CYCTAP;
DWT_CTRL &= ~DWT_CTRL_PCSAMPLENA;
```

We wrap this into a function to make our life easier:

```c
static void dwt_pcsampler_enable(bool enable) {
    if (enable) {
        DWT_CTRL &= ~DWT_CTRL_POSTPRESET;
        DWT_CTRL |= 0x3 << DWT_CTRL_POSTPRESET_SHIFT;
        DWT_CTRL |= DWT_CTRL_CYCTAP;
        DWT_CTRL |= DWT_CTRL_PCSAMPLENA;
    } else {
        DWT_CTRL &= ~DWT_CTRL_POSTPRESET;
        DWT_CTRL &= ~DWT_CTRL_CYCTAP;
        DWT_CTRL &= ~DWT_CTRL_PCSAMPLENA;
    }
}
```

and fill in our macro:

```c
#define PROFILE(code)                   \
    {                                   \
        dwt_pcsampler_enable(true);     \
        code;                            \
        dwt_pcsampler_enable(false);    \
    }
```

That was easy! We now have a `PROFILE` macro we can use to profile an individual
function. Note that this macro can only be used to profile a single function at
a time since there does not appear to be a way to set an ITM port for PC
sampling data.

Let's rebuild our firmware, collect some data:

```shell
$ make
$ arm-none-eabi-gdb mandel.elf
...
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from mandel.elf...

(gdb) target remote :3333
Remote debugging using :3333
iterate (py=1.00990558, px=<optimized out>) at mandel.c:121
121                     it++;
(gdb) mon reset halt
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x08000c68 msp: 0x20030000
(gdb) load
Loading section .text, size 0x6ea0 lma 0x8000000
Loading section .ARM.exidx, size 0x8 lma 0x8006ea0
Loading section .data, size 0xa1c lma 0x8006ea8
Start address 0x8000ca4, load size 30916
Transfer rate: 26 KB/sec, 7729 bytes/write.
(gdb) monitor tpiu config internal itm.fifo uart off 168000000
(gdb) monitor itm port 0 on
(gdb) continue
Continuing.
```

This will generate some more ITM data, but this time only for our function under
test. After running this for a little bit we can run `pcsampl` on the new data
file:

```shell
$ ~/code/itm-tools/target/debug/pcsampl itm.fifo -e mandel.elf 2>/dev/null
    % FUNCTION
 0.00 *SLEEP*
79.27 spi_xfer
19.20 lcd_command
 1.25 msleep
 0.17 mandel
 0.08 lcd_draw_pixel
 0.01 sys_tick_handler
 0.01 rcc_clock_setup_pll
 0.01 lcd_show_frame
 0.00 gpio_set_output_options
 0.00 _vfprintf_r
-----
 100% 39863 samples
```

As you can see, we now see the breakdown of time spent within `lcd_show_frame`,
and as expected `spi_xfer` takes the lion's share.

> Note: this approach is not perfect. Since IRQs are running, the function we
> are trying to profile could get interrupted which means we will collect some
> samples from other parts of our code as well. In a single threaded program,
> this is not a huge deal but can be more problematic when multiple threads are
> running and pre-empting each other.
