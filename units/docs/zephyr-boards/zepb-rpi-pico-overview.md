---
id: "zepb-rpi-pico-overview"
type: "concept"
domain: "bring-up"
title: "rpi_pico: Overview"
summary: "The Raspberry Pi Pico and Pico W are small, low-cost, versatile boards from Raspberry Pi. They are equipped with an RP2040 <RP2040 Datasheet> SoC, an on-board LED, a USB connector, and an SWD interface."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/raspberrypi/rpi_pico/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/raspberrypi/rpi_pico/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The Raspberry Pi Pico and Pico W are small, low-cost, versatile boards from
Raspberry Pi. They are equipped with an RP2040 <RP2040 Datasheet_> SoC, an on-board LED,
a USB connector, and an SWD interface.

The Pico W additionally contains an Infineon CYW43439 2.4 GHz Wi-Fi/Bluetooth module.

The RP2040 has two Cortex-M0+ cores. Zephyr currently runs on one core only;
running code on the second core is not supported.

The USB bootloader allows the ability to flash without any adapter,
in a drag-and-drop manner.
It is also possible to flash and debug the boards with their SWD interface,
using an external adapter.
