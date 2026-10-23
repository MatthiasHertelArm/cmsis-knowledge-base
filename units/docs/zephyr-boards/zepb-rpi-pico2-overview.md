---
id: "zepb-rpi-pico2-overview"
type: "concept"
domain: "bring-up"
title: "rpi_pico2: Overview"
summary: "The Raspberry Pi Pico 2 and Pico 2W are second-generation products in the Raspberry Pi Pico family. From the Raspberry Pi website is referred to as Pico 2."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/raspberrypi/rpi_pico2/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico2/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The Raspberry Pi Pico 2 and Pico 2W are second-generation products in the Raspberry Pi
Pico family. From the [Raspberry Pi website](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) is referred to as Pico 2.

The RP2350 SoC has two Cortex-M33 cores and two Hazard3 (RISC-V) cores. Zephyr
supports builds targeting either CPU architecture, but currently runs on one
core only; running code on the second core is not supported.
