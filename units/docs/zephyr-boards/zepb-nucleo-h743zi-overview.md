---
id: "zepb-nucleo-h743zi-overview"
type: "concept"
domain: "bring-up"
title: "nucleo_h743zi: Overview"
summary: "The STM32 Nucleo-144 boards offer combinations of performance and power that provide an affordable and flexible way for users to build prototypes and try out new concepts."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@8f62a4a:boards/st/nucleo_h743zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_h743zi/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The STM32 Nucleo-144 boards offer combinations of performance and power that
provide an affordable and flexible way for users to build prototypes and try
out new concepts. For compatible boards, the SMPS (Switched-Mode Power Supply)
significantly reduces power consumption in Run mode.

The Arduino-compatible ST Zio connector expands functionality of the Nucleo
open development platform, with a wide choice of specialized Arduino* Uno V3
shields.

The STM32 Nucleo-144 board does not require any separate probe as it integrates
the ST-LINK/V2-1 debugger/programmer.

The STM32 Nucleo-144 board comes with the STM32 comprehensive free software
libraries and examples available with the STM32Cube MCU Package.

Key Features

- STM32 microcontroller in LQFP144 package
- Ethernet compliant with IEEE-802.3-2002 (depending on STM32 support)
- USB OTG or full-speed device (depending on STM32 support)
- 3 user LEDs
- 2 user and reset push-buttons
- 32.768 kHz crystal oscillator
- Board connectors:

 - USB with Micro-AB
 - SWD
 - Ethernet RJ45 (depending on STM32 support)
 - ST Zio connector including Arduino* Uno V3
 - ST morpho

- Flexible power-supply options: ST-LINK USB VBUS or external sources.
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration
- capability: mass storage, virtual COM port and debug port.
- Comprehensive free software libraries and examples available with the
  STM32Cube MCU package.
- Arm* Mbed Enabled* compliant (only for some Nucleo part numbers)

More information about the board can be found at the Nucleo H743ZI website.


### NUCLEO-H743ZI Board - Obsolescence Notice


**Important Notice:** The NUCLEO-H743ZI development board is now **OBSOLETE** and
no longer recommended for new designs or developments.
STMicroelectronics has officially discontinued this product.
As a result, we strongly advise all users to transition to the recommended replacement
board: **NUCLEO-H753ZI**.
For more information, please refer to the official STMicroelectronics product page Nucleo H743ZI website.
