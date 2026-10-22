---
id: "zepb-nucleo-h563zi-overview"
type: "concept"
domain: "bring-up"
title: "nucleo_h563zi: Overview"
summary: "The Nucleo H563ZI board is designed as an affordable development platform for STMicroelectronics ARM® Cortex®-M33 core-based STM32H563ZIT6 microcontroller with TrustZone®. Here are some highlights of the Nucleo H563ZI board:"
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/st/nucleo_h563zi/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/st/nucleo_h563zi/doc/index.html#overview"
license: "Apache-2.0"
mode: "V"
---

The Nucleo H563ZI board is designed as an affordable development platform for
STMicroelectronics ARM® Cortex®-M33 core-based STM32H563ZIT6
microcontroller with TrustZone®.
Here are some highlights of the Nucleo H563ZI board:

- STM32H563ZI microcontroller featuring 2 Mbytes of Flash memory and 640Kbyte of
  SRAM in LQFP144 package
- Board connectors:

  - USB Type-C® Sink device FS
  - Ethernet RJ45 connector compliant with IEEE-802.3-2002 (depending on STM32 support)
  - ST Zio expansion connector including Arduino Uno V3 connectivity (CN7, CN8, CN9, CN10)
  - ST morpho extension connector (CN11, CN12)

- Flexible board power supply:

   - 5V_USB_STLK from ST-Link USB connector
   - VIN (7 - 12V, 0.8A) supplied via pin header CN8 pin 15 or CN11 pin 24
   - 5V_EXT on the ST morpho connector CN11 Pin 6 (5V, 1.3)
   - CHGR from a USB charger via the ST-LINK USB connector
   - USB_USER from the USB user connector (5V, 3A)
   - 3V3_EXT supplied via a pin header CN8 pin 7 or CN11 pin 16 (3.3V, 1.3A)

- On-board ST-LINK/V3EC debugger/programmer

  - mass storage
  - Virtual COM port
  - debug port

- Three users LEDs
- Two push-buttons: USER and RESET
- 32.789 kHz crystal oscillator

More information about the board can be found at the NUCLEO_H563ZI website.
