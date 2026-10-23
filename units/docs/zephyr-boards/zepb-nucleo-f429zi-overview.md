---
id: "zepb-nucleo-f429zi-overview"
type: "concept"
domain: "bring-up"
title: "nucleo_f429zi: Overview"
summary: "The Nucleo F429ZI board features an ARM Cortex-M4 based STM32F429ZI MCU with a wide range of connectivity support and configurations. Here are some highlights of the Nucleo F429ZI board:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_f429zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_f429zi/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The Nucleo F429ZI board features an ARM Cortex-M4 based STM32F429ZI MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo F429ZI board:

- STM32 microcontroller in LQFP144 package
- LSE crystal: 32.768 kHz crystal oscillator
- USB OTG
- Ethernet compliant with IEEE-802.3-2002
- Two types of extension resources:

  - ST Zio connector including: support for Arduino* Uno V3 connectivity
    (A0 to A5, D0 to D15) and additional signals exposing a wide range of
    peripherals
  - ST morpho extension pin headers for full access to all STM32 I/Os

- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - 5 V from ST-LINK/V2-1 USB VBUS
  - External power sources: 3.3 V and 7 - 12 V on ST Zio or ST morpho
    connectors, 5 V on ST morpho connector

- Three user LEDs
- Two push-buttons: USER and RESET

More information about the board can be found at the Nucleo F429ZI website.
