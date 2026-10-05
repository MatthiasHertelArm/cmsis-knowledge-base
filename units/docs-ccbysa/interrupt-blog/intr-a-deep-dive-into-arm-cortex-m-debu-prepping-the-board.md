---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-prepping-the-board"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: Prepping the board"
summary: "On the nRF52840-DK board I see P18 is labeled as \"Debug In\". Looking at the schematics[^19], I can easily see the pinout:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#prepping-the-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

On the nRF52840-DK board I see `P18` is labeled as "Debug In". Looking at the schematics[^19], I can easily see the pinout:



I attached the Saleae ground to Pin 9, wire 0 to `SWDIO` at P18 Pin 2, and wire 1 to `SWDCLK` at P18 Pin 4.

In the Saleae Logic App, I then enabled these 2 pins, and added the SWD analyzer:


