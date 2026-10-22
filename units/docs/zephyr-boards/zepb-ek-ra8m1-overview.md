---
id: "zepb-ek-ra8m1-overview"
type: "concept"
domain: "bring-up"
title: "ek_ra8m1: Overview"
summary: "The EK-RA8M1 is an Evaluation Kit for Renesas RA8M1 MCU Group which is the first 32-bits MCUs based on new Arm Cortex-M85."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/renesas/ek_ra8m1/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/renesas/ek_ra8m1/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The EK-RA8M1 is an Evaluation Kit for Renesas RA8M1 MCU Group which is the first
32-bits MCUs based on new Arm Cortex-M85. The kit offer multiple external interface
and peripherals set optimized on board allows user to seamlessly evaluate the features
of the RA8M1 MCU and develop embedded system application in various field.

The key features of the EK-RA8M1 board are categorized in three groups as follow:

**MCU Native Pin Access**

- 480MHz Arm Cortex-M85 based RA8M1 MCU in 224 pins, BGA package
- Native pin access through 2 x 50-pin, and 2 x 40-pin male headers
- MCU current measurement points for precision current consumption measurement
- Multiple clock sources - RA8M1 MCU oscillator and sub-clock oscillator crystals,
  providing precision 20.000MHz and 32,768 Hz refeence clocks.
  Additional low precision clocks are available internal to the RA8M1 MCU

**System Control and Ecosystem Access**

- USB Full Speed Host and Device (micro-AB connector)
- Four 5V input sources

  - USB (Debug, Full Speed, High Speed)
  - External power supply (using surface mount clamp test points and power input vias)

- Three Debug modes

  - Debug on-board (SWD)
  - Debug in (ETM, SWD and JTAG)
  - Debug out (SWD)

- User LEDs and buttons

  - Three User LEDs (red, blue, green)
  - Power LED (white) indicating availability of regulated power
  - Debug LED (yellow) indicating the debug connection
  - Two User buttons
  - One Reset button

- Five most popular ecosystems expansions

  - Two Seeed Grove system (I2C/I3C) connectors
  - One SparkFun Qwiic connector
  - Two Digilent Pmod (SPI, UART and I2C/I3C) connectors
  - Arduino (Uno R3) connector
  - MikroElektronika mikroBUS connector

- MCU boot configuration jumper

**Special Feature Access**

- Ethernet (RJ45 RMII interface)
- USB High Speed Host and Device (micro-AB connector)
- 512 Mb (64 MB) External Octo-SPI Flash (present in the MCU Native Pin Access area of the EK-RA8M1 board)
- CAN FD (3-pin header)
