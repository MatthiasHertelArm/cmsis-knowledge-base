---
id: "intr-profiling-firmware-on-cortex-m-poor-man-s-profiler"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M: Poor Man's Profiler"
summary: "The simplest way to profile a system is to use a sampling profiler. The concept is simple: record the program counter at regular intervals for a period of time."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m#poor-man-s-profiler"
license: "CC-BY-SA-4.0"
mode: "V"
---

The simplest way to profile a system is to use a sampling profiler. The concept
is simple: record the program counter at regular intervals for a period of time.
Given a high enough sampling rate for a long enough duration, you get a
statistical distribution of what code is running on your device.

One of the main advantages of sampling profilers is that they do not require
modifying the code you are trying to inspect. Other approaches like
instrumenting your code can yield more precise results, but risk changing the
behavior of the program.

So how can we sample our program counter at a regular interval? Using our
debugger! This is a common approach, sometimes dubbed the [poor man's
profiler](https://poormansprofiler.org/).

The concept is simple: we write a script which executes our debugger in a loop
and dumps the current backtrace. After we've collected enough data points, we
parse the backtraces and match them up to get aggregate values.

To do this we must run `arm-none-eabi-gdb` in batch mode: we want it to start,
connect, run our command, and exit without user input. This is supported with the
`-batch` flag. Here's the invocation:

```
$ arm-none-eabi-gdb -ex "set pagination off" -ex "target remote :3333" -ex "thread apply all bt" -batch $elf
```

This will start GDB, disable pagination (it requires user input), run `target
remote :3333` to connect to OpenOCD, run `thread apply all bt` to get the
backtrace of every thread, and exits.

To parse the data, I've adapted the `awk` script provided at
poormansprofiler.org to handle the specific output of `arm-none-eabi-gdb`.

Altogether this gives us the following:

```bash
#!/bin/bash
nsamples=1000
sleeptime=0
elf=mandel.elf

for x in $(seq 1 $nsamples)
  do
    arm-none-eabi-gdb -ex "set pagination off" -ex "target remote :3333" -ex "thread apply all bt" -batch $elf
    sleep $sleeptime
  done | \
awk '
  BEGIN { s = ""; }
  /^Thread/ { print s; s = ""; }
  /^\#/ {
      if (s != "" ) { if ($3 == "in") {  s = s "," $4 } else {  s = s "," $2 }}
      else { if ($3 == "in") {  s = $4 } else {  s = $2 } }
  }
  END { print s }' | \
sort | uniq -c | sort -r -n -k 1,1
```

Running this script, we get the following output:

```shell
$ sh pmp.sh
 592 spi_xfer,lcd_command,??
 408 spi_xfer,lcd_command,lcd_show_frame,main
   1
```

Using these initial results, it appears that we spend most of our time sending
frames to the LCD over SPI.

Unfortunately, we cannot get much more precise results using this approach.
Using GDB and OpenOCD introduces huge overhead, which means that we are limited
to a datapoint every 50ms. Given that our MPU executes on the order of 200
million clock cycles per second, that means that we get a sample every 10
million clock cycles. This is too coarse for any meaningful analysis, so we must
find a better approach
