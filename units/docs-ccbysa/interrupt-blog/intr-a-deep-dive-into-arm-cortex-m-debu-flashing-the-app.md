---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-flashing-the-app"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: Flashing the App"
summary: "For the purposes of this experiment we will look at what is happening with SEGGER J-Link. The invocation I used was:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#flashing-the-app"
license: "CC-BY-SA-4.0"
mode: "V"
---

For the purposes of this experiment we will look at what is happening with SEGGER J-Link. The invocation I used was:

```
JLinkGDBServer  -if swd -device nRF52840_xxAA -speed 500
```

I manually set the speed to a low value just to play it safe. You usually want the sampling rate to be at least 4x faster than the maximum frequency being measured. So if SWDCLK is running at 500kHz, we want to sample with a rate of at least 2 MegaSamples / second or greater.[^24] However, the faster we sample, the better our timing resolution will be.

To flash the device and attach to the GDB server, I used my personal favorite debug client, the GDB CLI:

```
arm-none-eabi-gdb-py --eval-command="target remote localhost:2331" --ex="mon reset" --ex="load" --ex="mon reset" --se=_build/nrf52840_xxaa.out
```
